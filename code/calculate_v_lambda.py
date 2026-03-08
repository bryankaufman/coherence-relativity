#!/usr/bin/env python3
"""
Calculate V(λ) and s(λ) on coherence space.

Definitions (Paper 1, §6.2):
    s(λ) = ∫₀^λ √G_λλ dλ'    (accumulated Fubini-Study length)
    V(λ) = ∫_λ^1 √G_λλ dλ'    (FS distance to classical frame)

These are purely geometric quantities derived from the metric G_λλ.
V(λ) is plotted in Fig 2; V(λ)/V(0) vs √(1−λ²) is Fig 6.

Uses the same N-mode dephasing model as calculate_g_lambda.py.

Output: data/v_lambda.csv, data/s_lambda.csv
"""

import numpy as np
import pandas as pd
import os
import sys

# Import G_λλ from sibling script
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calculate_g_lambda import g_lambda_N_modes, N_POINTS, LAMBDA_MIN, LAMBDA_MAX


def standard_qm_visibility(lam):
    """Standard QM visibility = √(1 − λ²)."""
    return np.sqrt(1.0 - lam ** 2)


def main():
    N = 10  # Multi-mode model (matches paper figures)
    lambda_vals = np.linspace(LAMBDA_MIN, LAMBDA_MAX, N_POINTS)
    dlam = lambda_vals[1] - lambda_vals[0]

    # Compute G_λλ
    G_vals = np.array([g_lambda_N_modes(lam, N) for lam in lambda_vals])
    sqrt_G = np.sqrt(G_vals)

    # s(λ) = ∫₀^λ √G dλ'  (accumulated FS length, trapezoidal)
    s_vals = np.zeros_like(lambda_vals)
    for i in range(1, len(lambda_vals)):
        s_vals[i] = s_vals[i - 1] + 0.5 * (sqrt_G[i - 1] + sqrt_G[i]) * dlam

    # V(λ) = ∫_λ^1 √G dλ'  (FS distance to classical frame)
    # V(λ) = s(1) − s(λ)
    s_total = s_vals[-1]
    V_vals = s_total - s_vals

    # Standard QM visibility for comparison
    V_std = standard_qm_visibility(lambda_vals)

    # dλ/ds = 1/√G  (rate of change of λ per unit FS length)
    dlam_ds = 1.0 / sqrt_G

    # --- Save v_lambda.csv ---
    df_v = pd.DataFrame({
        'lambda': lambda_vals,
        'V_lambda': V_vals,
        'V_standard_qm': V_std,
    })
    script_dir = os.path.dirname(os.path.abspath(__file__))
    v_path = os.path.join(script_dir, '..', 'data', 'v_lambda.csv')
    df_v.to_csv(v_path, index=False)

    # --- Save s_lambda.csv ---
    df_s = pd.DataFrame({
        'lambda': lambda_vals,
        's_lambda': s_vals,
        'dlambda_ds': dlam_ds,
    })
    s_path = os.path.join(script_dir, '..', 'data', 's_lambda.csv')
    df_s.to_csv(s_path, index=False)

    # Visibility deviation
    V_norm = V_vals / V_vals[0] if V_vals[0] > 0 else V_vals
    delta_vis = np.abs(V_norm - V_std)
    max_delta = np.max(delta_vis)
    max_lam = lambda_vals[np.argmax(delta_vis)]

    print(f"[AUDIT-FIX] V(λ) and s(λ) calculation (N={N})")
    print(f"[AUDIT-FIX] V(λ) → {v_path}")
    print(f"[AUDIT-FIX] s(λ) → {s_path}")
    print(f"[AUDIT-FIX] V(0) = {V_vals[0]:.6f} (total geodesic length)")
    print(f"[AUDIT-FIX] V(1) = {V_vals[-1]:.6f}")
    print(f"[AUDIT-FIX] s(1) = {s_vals[-1]:.6f}")
    print(f"[AUDIT-FIX] Max Δ(V/V(0) vs √(1−λ²)) = {max_delta:.4f} at λ = {max_lam:.2f}")


if __name__ == '__main__':
    main()
