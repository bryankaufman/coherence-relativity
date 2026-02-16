#!/usr/bin/env python3
"""
Generate all figures for Paper 1: Coherence Frames.
Uses data from numerical calculations.
Output: figures/*.pdf (publication-quality, 300 DPI)
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.patches as mpatches

# Publication style
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.figsize': (7, 5),
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'text.usetex': False,  # Set True if LaTeX is available
})


def figure1_g_lambda():
    """Figure 1: Fubini-Study metric G_lambda(lambda) on coherence space."""
    df = pd.read_csv('data/g_lambda.csv')

    fig, ax = plt.subplots()
    ax.plot(df['lambda'], df['G_lambda_lambda'], 'b-', linewidth=2)
    ax.set_xlabel(r'$\lambda$ (which-path resolution)')
    ax.set_ylabel(r'$G_{\lambda\lambda}$ (Fubini-Study metric)')
    ax.set_title('Information-Geometric Distance on Coherence Space')

    # Annotate regions
    ax.axvspan(0, 0.15, alpha=0.1, color='blue', label='Coherent regime')
    ax.axvspan(0.85, 1.0, alpha=0.1, color='red', label='Classical regime')

    peak_idx = df['G_lambda_lambda'].idxmax()
    peak_lam = df['lambda'].iloc[peak_idx]
    peak_val = df['G_lambda_lambda'].iloc[peak_idx]
    ax.annotate(f'Peak: $\\lambda$ = {peak_lam:.2f}',
                xy=(peak_lam, peak_val),
                xytext=(peak_lam + 0.15, peak_val * 0.85),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=11)

    ax.legend(loc='upper right')
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3)

    fig.savefig('figures/fig1_g_lambda.pdf')
    fig.savefig('figures/fig1_g_lambda.png')
    plt.close(fig)
    print("[WARP] Figure 1: G_lambda(lambda) -> figures/fig1_g_lambda.pdf")


def figure2_quasipotential():
    """Figure 2: Quasipotential V(lambda) landscape."""
    df = pd.read_csv('data/v_lambda.csv')

    fig, ax = plt.subplots()
    ax.plot(df['lambda'], df['V_lambda'], 'r-', linewidth=2, label=r'$V(\lambda)$ (CR)')
    ax.set_xlabel(r'$\lambda$ (which-path resolution)')
    ax.set_ylabel(r'$V(\lambda)$ (quasipotential)')
    ax.set_title('Quasipotential Landscape on Coherence Space')

    # Mark stable frame
    min_idx = df['V_lambda'].idxmin()
    min_lam = df['lambda'].iloc[min_idx]
    min_val = df['V_lambda'].iloc[min_idx]
    ax.plot(min_lam, min_val, 'ko', markersize=8)
    ax.annotate('Stable classical frame\n(pointer basis)',
                xy=(min_lam, min_val),
                xytext=(min_lam - 0.35, min_val + abs(df['V_lambda'].max() - df['V_lambda'].min()) * 0.3),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=10)

    # Mark unstable coherent frame
    ax.plot(0, df['V_lambda'].iloc[0], 'bs', markersize=8)
    ax.annotate('Unstable coherent frame',
                xy=(0, df['V_lambda'].iloc[0]),
                xytext=(0.15, df['V_lambda'].iloc[0] + abs(df['V_lambda'].max() - df['V_lambda'].min()) * 0.1),
                arrowprops=dict(arrowstyle='->', color='blue'),
                fontsize=10)

    ax.legend()
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3)

    fig.savefig('figures/fig2_quasipotential.pdf')
    fig.savefig('figures/fig2_quasipotential.png')
    plt.close(fig)
    print("[WARP] Figure 2: V(lambda) -> figures/fig2_quasipotential.pdf")


def figure3_frame_transformation():
    """Figure 3: Coherence frame transformation diagram (conceptual)."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw two frames as boxes
    frame1 = mpatches.FancyBboxPatch((0, 0.5), 1.5, 2.0,
                                      boxstyle="round,pad=0.1",
                                      facecolor='lightblue', edgecolor='blue', linewidth=2)
    frame2 = mpatches.FancyBboxPatch((3, 0.5), 1.5, 2.0,
                                      boxstyle="round,pad=0.1",
                                      facecolor='lightyellow', edgecolor='orange', linewidth=2)
    ax.add_patch(frame1)
    ax.add_patch(frame2)

    # Labels
    ax.text(0.75, 2.8, r'Frame $F_{int}$', ha='center', fontsize=13, fontweight='bold', color='blue')
    ax.text(3.75, 2.8, r'Frame $F_{wp}$', ha='center', fontsize=13, fontweight='bold', color='darkorange')

    # State descriptions
    ax.text(0.75, 2.0, r'$|\psi\rangle = \frac{1}{\sqrt{2}}(|L\rangle + |R\rangle)$',
            ha='center', fontsize=10)
    ax.text(0.75, 1.5, 'Interference visible', ha='center', fontsize=9, style='italic')
    ax.text(0.75, 1.0, r'$\rho_{LR} \neq 0$', ha='center', fontsize=10)

    ax.text(3.75, 2.0, r'$|\Psi\rangle = \frac{1}{\sqrt{2}}(|L\rangle|W_L\rangle + |R\rangle|W_R\rangle)$',
            ha='center', fontsize=9)
    ax.text(3.75, 1.5, 'Which-path definite', ha='center', fontsize=9, style='italic')
    ax.text(3.75, 1.0, r'$\rho_{LR} = 0$', ha='center', fontsize=10)

    # Arrow between frames
    ax.annotate('', xy=(2.9, 1.5), xytext=(1.6, 1.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    ax.text(2.25, 1.8, r"$U_{F \to F'}$", ha='center', fontsize=12, fontweight='bold')
    ax.text(2.25, 1.15, '(detector coupling)', ha='center', fontsize=9, style='italic')

    # Invariants box
    inv_box = mpatches.FancyBboxPatch((1.2, -0.3), 2.1, 0.6,
                                       boxstyle="round,pad=0.1",
                                       facecolor='lightgreen', edgecolor='green', linewidth=1.5)
    ax.add_patch(inv_box)
    ax.text(2.25, 0.0, r'Invariant: $\mu(L) = \mu(R) = \frac{1}{2}$',
            ha='center', fontsize=10, fontweight='bold', color='darkgreen')

    ax.set_title('Frame Transformation: Double-Slit Experiment', fontsize=14, pad=20)

    fig.savefig('figures/fig3_frame_transformation.pdf')
    fig.savefig('figures/fig3_frame_transformation.png')
    plt.close(fig)
    print("[WARP] Figure 3: Frame transformation diagram -> figures/fig3_frame_transformation.pdf")


def figure4_born_rule_invariant():
    """Figure 4: Born rule as frame invariant -- SR analogy."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left panel: SR
    ax = axes[0]
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')

    # Light cone
    ax.plot([2, 4], [2, 4], 'y-', linewidth=2)
    ax.plot([2, 4], [2, 0], 'y-', linewidth=2)
    ax.plot([2, 0], [2, 4], 'y-', linewidth=2)
    ax.plot([2, 0], [2, 0], 'y-', linewidth=2)
    ax.fill_between([0, 2, 4], [2, 0, 2], [2, 4, 2], alpha=0.1, color='yellow')

    # Two frames
    ax.arrow(2, 2, 1.5, 1.5, head_width=0.15, head_length=0.1, fc='blue', ec='blue')
    ax.arrow(2, 2, 2, 0.5, head_width=0.15, head_length=0.1, fc='red', ec='red')
    ax.text(3.6, 3.6, r"$S$", fontsize=12, color='blue')
    ax.text(4.2, 2.4, r"$S'$", fontsize=12, color='red')

    # Invariant
    ax.text(2, -0.5, r'Invariant: $ds^2 = -c^2dt^2 + dx^2$',
            ha='center', fontsize=10, fontweight='bold', color='darkgreen')
    ax.set_title('Special Relativity', fontsize=13)
    ax.axis('off')

    # Right panel: CR
    ax = axes[1]
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')

    # Coherence space (circle representing Sigma)
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(2 + 1.5*np.cos(theta), 2 + 1.5*np.sin(theta), 'k-', linewidth=1.5)
    ax.text(2, 4, r'$\Sigma$', ha='center', fontsize=14, fontweight='bold')

    # Two frames as points on Sigma
    f1_angle = np.pi/4
    f2_angle = 3*np.pi/4
    f1_x, f1_y = 2 + 1.5*np.cos(f1_angle), 2 + 1.5*np.sin(f1_angle)
    f2_x, f2_y = 2 + 1.5*np.cos(f2_angle), 2 + 1.5*np.sin(f2_angle)

    ax.plot(f1_x, f1_y, 'bo', markersize=10)
    ax.plot(f2_x, f2_y, 'ro', markersize=10)
    ax.text(f1_x + 0.2, f1_y + 0.2, r'$F_{int}$', fontsize=12, color='blue')
    ax.text(f2_x - 0.5, f2_y + 0.2, r'$F_{wp}$', fontsize=12, color='red')

    # Arc between frames (geodesic on Sigma)
    arc_angles = np.linspace(f1_angle, f2_angle, 50)
    ax.plot(2 + 1.5*np.cos(arc_angles), 2 + 1.5*np.sin(arc_angles), 'g--', linewidth=2)

    # Invariant
    ax.text(2, -0.5, r'Invariant: $\mu_F(i) = |c_i|^2$',
            ha='center', fontsize=10, fontweight='bold', color='darkgreen')
    ax.set_title('Coherence Relativity', fontsize=13)
    ax.axis('off')

    fig.suptitle('The Born Rule as Frame Invariant', fontsize=15, fontweight='bold', y=1.02)
    fig.tight_layout()

    fig.savefig('figures/fig4_born_rule_invariant.pdf')
    fig.savefig('figures/fig4_born_rule_invariant.png')
    plt.close(fig)
    print("[WARP] Figure 4: Born rule invariant -> figures/fig4_born_rule_invariant.pdf")


def figure5_double_slit_frames():
    """Figure 5: Double-slit experiment in two coherence frames (side-by-side)."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left: Interference frame
    ax = axes[0]
    x = np.linspace(-3, 3, 500)
    # Two-slit interference pattern
    d = 0.5   # slit separation
    pattern = (np.cos(np.pi * d * x))**2 * np.exp(-x**2 / 4)
    ax.fill_between(x, 0, pattern, alpha=0.3, color='blue')
    ax.plot(x, pattern, 'b-', linewidth=2)
    ax.set_xlabel('Screen position')
    ax.set_ylabel('Detection probability')
    ax.set_title(r'$F_{int}$: Interference Frame', fontsize=13, color='blue')
    ax.text(0, max(pattern)*0.85, 'Coherence visible\n' + r'$\rho_{LR} \neq 0$',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    # Right: Which-path frame
    ax = axes[1]
    # Two separate Gaussian peaks (no interference)
    peak_L = 0.5 * np.exp(-(x + d)**2 / 0.8)
    peak_R = 0.5 * np.exp(-(x - d)**2 / 0.8)
    envelope = peak_L + peak_R
    ax.fill_between(x, 0, peak_L, alpha=0.3, color='red', label='Path L')
    ax.fill_between(x, 0, peak_R, alpha=0.3, color='orange', label='Path R')
    ax.plot(x, envelope, 'r-', linewidth=2)
    ax.set_xlabel('Screen position')
    ax.set_ylabel('Detection probability')
    ax.set_title(r'$F_{wp}$: Which-Path Frame', fontsize=13, color='red')
    ax.text(0, max(envelope)*0.85, 'Paths definite\n' + r'$\rho_{LR} = 0$',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    ax.legend(loc='upper right')

    fig.suptitle('Same Physical Setup, Two Coherence Frames', fontsize=14, fontweight='bold')
    fig.tight_layout()

    fig.savefig('figures/fig5_double_slit_frames.pdf')
    fig.savefig('figures/fig5_double_slit_frames.png')
    plt.close(fig)
    print("[WARP] Figure 5: Double-slit frames -> figures/fig5_double_slit_frames.pdf")


def figure6_cr_vs_standard():
    """Figure 6: V(lambda) comparison -- CR prediction vs standard QM."""
    df = pd.read_csv('data/v_lambda.csv')

    fig, ax = plt.subplots()

    # Normalize V(lambda) for comparison
    V_range = df['V_lambda'].max() - df['V_lambda'].min()
    if V_range > 0:
        V_norm = (df['V_lambda'] - df['V_lambda'].min()) / V_range
    else:
        V_norm = df['V_lambda']

    ax.plot(df['lambda'], V_norm, 'r-', linewidth=2, label=r'CR: $V(\lambda)$ (normalized)')
    ax.plot(df['lambda'], df['V_standard_qm'], 'b--', linewidth=2,
            label=r'Standard QM: $\mathcal{V} = \sqrt{1-\lambda^2}$')

    # Highlight deviation region
    deviation = np.abs(V_norm - df['V_standard_qm'])
    significant = deviation > 0.05
    if significant.any():
        ax.fill_between(df['lambda'], V_norm, df['V_standard_qm'],
                        where=significant, alpha=0.2, color='green',
                        label='Testable deviation')

    ax.set_xlabel(r'$\lambda$ (which-path resolution)')
    ax.set_ylabel('Normalized value')
    ax.set_title(r'CR Quasipotential vs Standard QM Visibility')
    ax.legend()
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3)

    fig.savefig('figures/fig6_cr_vs_standard.pdf')
    fig.savefig('figures/fig6_cr_vs_standard.png')
    plt.close(fig)
    print("[WARP] Figure 6: CR vs Standard QM -> figures/fig6_cr_vs_standard.pdf")


def figure7_experimental_setup():
    """Figure 7: Experimental setup schematic for Predictions 2 and 5."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Prediction 2 -- Continuous decoherence monitoring
    ax = axes[0]
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-1, 4)
    ax.axis('off')
    ax.set_title('Prediction 2: Continuous Decoherence\nMonitoring', fontsize=12, fontweight='bold')

    # Source
    source = mpatches.FancyBboxPatch((0, 1), 0.8, 1,
                                      boxstyle="round,pad=0.05",
                                      facecolor='lightyellow', edgecolor='black')
    ax.add_patch(source)
    ax.text(0.4, 1.5, 'Source', ha='center', fontsize=9)

    # Slits
    ax.plot([2, 2], [0.5, 1.3], 'k-', linewidth=3)
    ax.plot([2, 2], [1.7, 2.5], 'k-', linewidth=3)
    ax.plot([2, 2], [2.9, 3.5], 'k-', linewidth=3)
    ax.text(2, 0, 'Slits', ha='center', fontsize=9)

    # Tunable detector
    det = mpatches.FancyBboxPatch((3, 1.2), 1, 0.8,
                                   boxstyle="round,pad=0.05",
                                   facecolor='lightcoral', edgecolor='red')
    ax.add_patch(det)
    ax.text(3.5, 1.6, 'Detector\n' + r'$\lambda$ tunable', ha='center', fontsize=8)

    # Screen
    ax.plot([5, 5], [0, 3.5], 'b-', linewidth=3)
    ax.text(5, -0.5, 'Screen', ha='center', fontsize=9)

    # Arrows
    ax.annotate('', xy=(1.9, 1.5), xytext=(0.9, 1.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(4.9, 1.5), xytext=(4.1, 1.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))

    # Measure
    ax.text(3.5, 3.2, r'Measure $G_{\lambda\lambda}$' + '\nvs. detector strength',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    # Right: Prediction 5 -- Quantum Darwinism test
    ax = axes[1]
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-1, 4)
    ax.axis('off')
    ax.set_title('Prediction 5: Quantum Darwinism\nFrame Selection', fontsize=12, fontweight='bold')

    # System
    system = plt.Circle((1.5, 2), 0.5, facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(system)
    ax.text(1.5, 2, 'System\n' + r'$\mathcal{S}$', ha='center', fontsize=9)

    # Environment fragments
    for i, (x, y, label) in enumerate([(3.5, 3.2, r'$E_1$'), (3.5, 2, r'$E_2$'),
                                         (3.5, 0.8, r'$E_3$'), (5, 2, r'$E_4$')]):
        env = plt.Circle((x, y), 0.35, facecolor='lightyellow', edgecolor='orange', linewidth=1.5)
        ax.add_patch(env)
        ax.text(x, y, label, ha='center', fontsize=9)
        ax.annotate('', xy=(x - 0.35, y if i < 3 else y),
                    xytext=(2.0, 2),
                    arrowprops=dict(arrowstyle='->', lw=1, color='gray'))

    ax.text(3, -0.5, r'Increase $N$ fragments $\rightarrow$' + '\n' + r'Observe $V(\lambda)$ narrowing',
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    fig.tight_layout()

    fig.savefig('figures/fig7_experimental_setup.pdf')
    fig.savefig('figures/fig7_experimental_setup.png')
    plt.close(fig)
    print("[WARP] Figure 7: Experimental setups -> figures/fig7_experimental_setup.pdf")


def main():
    print("=" * 60)
    print("Generating Paper 1 figures...")
    print("=" * 60)

    figure1_g_lambda()
    figure2_quasipotential()
    figure3_frame_transformation()
    figure4_born_rule_invariant()
    figure5_double_slit_frames()
    figure6_cr_vs_standard()
    figure7_experimental_setup()

    print("=" * 60)
    print("All 7 figures generated in figures/")
    print("=" * 60)


if __name__ == '__main__':
    main()
