#!/usr/bin/env python3
"""
Calculate G_λλ(λ) — Fubini-Study metric on coherence space.

Physical model (Paper 1, §6.3, eqs. 7–10):
    |Ψ(λ)⟩ = (1/√2)|0⟩|E₀⟩ + (1/√2)|1⟩|E₁(λ)⟩
    ⟨E₀|E₁(λ)⟩ = 1 − λ   (decoherence distinguishability, eq. 8)

For N identical environment modes, each mode has per-mode overlap
r = (1−λ)^{1/N}, so that the total overlap ∏ r_k = (1−λ).

The FS metric on the total pure state is:
    G_λλ = (1/2) · N · [(dr/dλ)² + (ds/dλ)²]
where s = √(1−r²), and the factor 1/2 comes from the |1⟩ branch
carrying half the amplitude.

For N=1 this reduces analytically to G_λλ = 1/[2λ(2−λ)].

Output: data/g_lambda.csv
"""

import numpy as np
import pandas as pd
import os

N_POINTS = 2000
LAMBDA_MIN = 0.005
LAMBDA_MAX = 0.995


def g_lambda_analytical_N1(lam):
    """Exact G_λλ for N=1 dephasing model."""
    return 1.0 / (2.0 * lam * (2.0 - lam))


def g_lambda_N_modes(lam, N):
    """G_λλ for N identical environment modes.

    Per-mode overlap r = (1−λ)^{1/N}.
    Each mode state: |u_k⟩ = r|E₀⟩ + s|E₀⊥⟩, s = √(1−r²).
    Because ⟨u|du/dλ⟩ = 0 for this parametrization, the product-state
    FS metric simplifies to G = (1/2) · N · ⟨du|du⟩.
    """
    r = (1.0 - lam) ** (1.0 / N)
    s2 = 1.0 - r * r
    if s2 < 1e-30:
        s2 = 1e-30

    # dr/dλ
    dr = -(1.0 / N) * (1.0 - lam) ** (1.0 / N - 1.0)
    # ds/dλ = −r · dr / √(1−r²)
    ds = -r * dr / np.sqrt(s2)

    # ⟨du|du⟩ = (dr)² + (ds)²
    du_du = dr ** 2 + ds ** 2

    # G = (1/2) · N · ⟨du|du⟩
    return 0.5 * N * du_du


def main():
    lambda_vals = np.linspace(LAMBDA_MIN, LAMBDA_MAX, N_POINTS)

    # N=10 multi-mode model (matches paper figures)
    N = 10
    g_vals = np.array([g_lambda_N_modes(lam, N) for lam in lambda_vals])

    df = pd.DataFrame({
        'lambda': lambda_vals,
        'G_lambda_lambda': g_vals,
    })

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '..', 'data', 'g_lambda.csv')
    df.to_csv(output_path, index=False)

    print(f"[AUDIT-FIX] G_λλ calculation (N={N}) → {output_path}")
    print(f"[AUDIT-FIX] Grid: {N_POINTS} points, λ ∈ [{LAMBDA_MIN}, {LAMBDA_MAX}]")
    print(f"[AUDIT-FIX] G_min = {g_vals.min():.4f} at λ = {lambda_vals[np.argmin(g_vals)]:.3f}")
    print(f"[AUDIT-FIX] G(0.5) = {g_vals[N_POINTS // 2]:.6f}")


if __name__ == '__main__':
    main()
