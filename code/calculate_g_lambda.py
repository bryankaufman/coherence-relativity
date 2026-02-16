#!/usr/bin/env python3
"""
Calculate G_λλ(λ) for double-slit which-path resolution
Society of Mind: Numerical Agent Task
Input: λ ∈ [0,1] (which-path resolution parameter)
Output: data/g_lambda.csv
"""

import numpy as np
import pandas as pd

def double_slit_state(lam):
    """
    State ψ(λ) for double-slit with which-path resolution λ
    λ=0: fully coherent (|L⟩+|R⟩)/√2
    λ=1: fully resolved |L⟩ or |R⟩
    """
    # Interpolate between coherent and pointer states
    coherent = np.array([1, 1]) / np.sqrt(2)
    pointer = np.array([1, 0])  # Left slit (could also be [0,1])
    
    # Smooth interpolation
    psi = (1 - lam) * coherent + lam * pointer
    return psi / np.linalg.norm(psi)

def derivative_wrt_lambda(lam, delta=1e-6):
    """Numerical derivative ∂ψ/∂λ"""
    psi_plus = double_slit_state(lam + delta)
    psi_minus = double_slit_state(lam - delta)
    return (psi_plus - psi_minus) / (2 * delta)

def fubini_study_metric(lam):
    """
    Calculate G_λλ = Re[⟨∂_λψ|∂_λψ⟩ - ⟨∂_λψ|ψ⟩⟨ψ|∂_λψ⟩]
    This is the Fubini-Study metric component
    """
    psi = double_slit_state(lam)
    d_psi = derivative_wrt_lambda(lam)
    
    # Inner products
    dot_d_psi_d_psi = np.real(np.vdot(d_psi, d_psi))
    dot_d_psi_psi = np.vdot(d_psi, psi)
    
    # Fubini-Study formula
    G_ll = dot_d_psi_d_psi - np.abs(dot_d_psi_psi)**2
    
    return np.real(G_ll)

def main():
    # Grid of λ values
    lambda_vals = np.linspace(0, 1, 1000)
    
    # Calculate G_λλ for each point
    g_lambda = np.array([fubini_study_metric(lam) for lam in lambda_vals])
    
    # Save to CSV
    df = pd.DataFrame({
        'lambda': lambda_vals,
        'G_lambda_lambda': g_lambda
    })
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '..', 'data', 'g_lambda.csv')
    df.to_csv(output_path, index=False)
    print(f"[Claude Code] COMPLETED: G_λλ calculation → {output_path}")
    print(f"[Claude Code] KEY_FINDINGS: Peak at λ = {lambda_vals[np.argmax(g_lambda)]:.3f}")
    print(f"[Claude Code] KEY_FINDINGS: Max G_λλ = {np.max(g_lambda):.6f}")

if __name__ == '__main__':
    main()
