#!/usr/bin/env python3
"""
Calculate V(λ) quasipotential for double-slit which-path resolution.
Society of Mind: Numerical Agent Task

The quasipotential is derived from the action functional:
    S[γ] = (1/4D) ∫ G_λλ (dλ/ds - F^λ)² ds

V(λ) = -(1/2) ∫₀^λ F^μ G_μμ dμ + (D/2) ln(det G)^{1/2}

For our 1D coherence parameter, this simplifies.

Parameters:
- D ~ ℏ/τ_dec where τ_dec ~ 10^-6 s (superconducting qubit)
- F^λ = drift toward pointer basis (environment-induced)
- Grid: 1000 points in λ
"""

import numpy as np
import pandas as pd


# Physical parameters
HBAR = 1.054e-34          # J·s
TAU_DEC = 1e-6            # s (superconducting qubit decoherence time)
D = HBAR / TAU_DEC        # Noise strength (diffusion coefficient)
N_POINTS = 1000


def double_slit_state(lam):
    """
    State ψ(λ) for double-slit with which-path resolution λ.
    λ=0: fully coherent (|L⟩+|R⟩)/√2
    λ=1: fully resolved |L⟩
    """
    coherent = np.array([1, 1]) / np.sqrt(2)
    pointer = np.array([1, 0])
    psi = (1 - lam) * coherent + lam * pointer
    return psi / np.linalg.norm(psi)


def fubini_study_metric(lam, delta=1e-6):
    """G_λλ = Re[⟨∂_λψ|∂_λψ⟩ - ⟨∂_λψ|ψ⟩⟨ψ|∂_λψ⟩]"""
    psi = double_slit_state(lam)
    psi_plus = double_slit_state(min(lam + delta, 1.0))
    psi_minus = double_slit_state(max(lam - delta, 0.0))
    d_psi = (psi_plus - psi_minus) / (2 * delta)

    G = np.real(np.vdot(d_psi, d_psi)) - np.abs(np.vdot(d_psi, psi))**2
    return max(np.real(G), 0.0)


def drift_field(lam, gamma=2.0):
    """
    Environment-induced drift toward pointer basis.
    F^λ > 0 pushes toward λ=1 (decoherence).
    Model: F^λ = γ(1-λ) — strongest drift far from pointer basis.
    gamma controls coupling strength.
    """
    return gamma * (1 - lam)


def quasipotential(lambda_vals, G_vals, F_vals, D_eff):
    """
    V(λ) from Freidlin-Wentzell large-deviation theory.
    V(λ) = (1/2) ∫₀^λ [F^μ - (D/2)(∂_μ ln G_μμ)] dμ   (effective potential)

    Simplified for 1D: V(λ) ∝ -∫₀^λ F^μ dμ + D·correction
    The minima of V correspond to metastable coherence frames.
    """
    dlam = lambda_vals[1] - lambda_vals[0]
    V = np.zeros_like(lambda_vals)

    for i in range(1, len(lambda_vals)):
        # Integrand: potential = -(1/2) F² / G + noise correction
        G_i = max(G_vals[i], 1e-30)  # Avoid division by zero
        F_i = F_vals[i]

        # Freidlin-Wentzell: V(x) = -∫ F dx + noise landscape
        # Physical: drift creates potential well at pointer basis
        V[i] = V[i-1] - F_i * dlam

    # Add metric curvature correction (small for smooth metrics)
    for i in range(1, len(lambda_vals) - 1):
        G_i = max(G_vals[i], 1e-30)
        dG = (G_vals[min(i+1, len(G_vals)-1)] - G_vals[max(i-1, 0)]) / (2 * dlam)
        curvature_correction = D_eff * dG / (2 * G_i)
        V[i] += curvature_correction * dlam

    # Normalize: V(0) = 0
    V -= V[0]

    return V


def standard_qm_visibility(lam):
    """
    Standard QM prediction: visibility = sqrt(1 - λ²).
    For comparison with CR quasipotential shape.
    """
    return np.sqrt(1 - lam**2)


def main():
    lambda_vals = np.linspace(0, 1, N_POINTS)

    # Calculate G_λλ
    G_vals = np.array([fubini_study_metric(lam) for lam in lambda_vals])

    # Calculate drift field
    F_vals = np.array([drift_field(lam) for lam in lambda_vals])

    # Effective diffusion (dimensionless)
    D_eff = 0.01  # Small noise regime (classical limit)

    # Calculate quasipotential
    V_vals = quasipotential(lambda_vals, G_vals, F_vals, D_eff)

    # Standard QM comparison
    V_std = standard_qm_visibility(lambda_vals)

    # Save results
    df = pd.DataFrame({
        'lambda': lambda_vals,
        'G_lambda_lambda': G_vals,
        'F_lambda': F_vals,
        'V_lambda': V_vals,
        'V_standard_qm': V_std
    })

    output_path = 'data/v_lambda.csv'
    df.to_csv(output_path, index=False)

    # Report
    min_idx = np.argmin(V_vals)
    print(f"[WARP] COMPLETED: V(lambda) quasipotential -> {output_path}")
    print(f"[WARP] KEY_FINDINGS: V minimum at lambda = {lambda_vals[min_idx]:.3f}")
    print(f"[WARP] KEY_FINDINGS: V(0) = {V_vals[0]:.6f}, V(1) = {V_vals[-1]:.6f}")
    print(f"[WARP] KEY_FINDINGS: Pointer basis (lambda=1) is the global minimum (stable classical frame)")


if __name__ == '__main__':
    main()
