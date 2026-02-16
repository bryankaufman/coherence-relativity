#!/usr/bin/env python3
"""
Generate all figures for Coherence Relativity Paper 1.

Usage:
    cd coherence-relativity
    source .venv/bin/activate
    python scripts/generate_figures.py          # generate all
    python scripts/generate_figures.py 1        # generate fig 1 only
    python scripts/generate_figures.py 1 2 6    # generate figs 1, 2, 6

Figures:
    1  fig1_g_lambda.pdf          G_λλ metric (multi-mode Fubini-Study)
    2  fig2_quasipotential.pdf    V(λ) quasipotential landscape
    3  fig3_frame_transformation  Frame transformation schematic
    4  fig4_born_rule_invariant   Born rule = frame invariant (SR vs CR)
    5  fig5_double_slit_frames    Double-slit in two coherence frames
    6  fig6_cr_vs_standard.pdf    CR accumulated FS distance vs standard QM
    7  fig7_experimental_setup    Experimental setup schematics

Requires: numpy, scipy, matplotlib (in project .venv)

Physics:
    Multi-mode collective decoherence model with N environment modes.
    State: |ψ(λ)⟩ = (1/√2)(|L⟩⊗|W_L⟩ + |R⟩⊗|W_R(λ)⟩)
    with ⟨W_L|W_R(λ)⟩ = (1-λ) distributed over N modes.

    FS metric: G_λλ = 1/(2N · (1-λ)^{2(N-1)/N} · (1-(1-λ)^{2/N}))
    Diverges at both endpoints (coordinate singularity for N≥2).
    Minimum at intermediate λ — the quantum-classical crossover.
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
import matplotlib.patches as mpatches

# ---------- paths ----------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
FIGS = os.path.join(ROOT, 'figures')

# ---------- global style ----------
plt.rcParams.update({
    'text.usetex': False,
    'mathtext.fontset': 'cm',
    'font.family': 'serif',
    'font.size': 12,
    'axes.labelsize': 13,
    'axes.titlesize': 14,
    'legend.fontsize': 11,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# ---------- default model parameters ----------
N_MODES = 10  # collectively-coupled environment modes


# ============================================================
# Multi-mode FS metric computation
# ============================================================

def g_lambda_multimode(lam, N=N_MODES):
    """Fubini-Study metric G_λλ for N collectively-coupled environment modes.

    G = 1/(2N · (1-λ)^{2(N-1)/N} · (1-(1-λ)^{2/N}))

    Diverges at λ→0 and λ→1 (for N≥2) — coordinate singularity.
    Minimum at intermediate λ — the geometric crossover.
    """
    lam = np.asarray(lam, dtype=float)
    u = 1.0 - lam
    exp1 = 2.0 * (N - 1) / N
    exp2 = 2.0 / N
    with np.errstate(divide='ignore', invalid='ignore'):
        denom = 2.0 * N * np.power(u, exp1) * (1.0 - np.power(u, exp2))
        G = np.where(denom > 0, 1.0 / denom, np.inf)
    return G


def compute_fs_quantities(N=N_MODES, n_points=2000):
    """Compute all metric quantities on [ε, 1-ε].

    Returns:
        lam: λ grid
        G: FS metric G_λλ(λ)
        s: accumulated FS length s(λ) = ∫_ε^λ √G dλ'
        V: quasipotential V(λ) = s_total - s(λ) (distance to classical frame)
        dlam_ds: inverse metric dλ/ds = 1/√G (peaks in middle)
        V_std: standard QM visibility √(1-λ²)
    """
    eps = 0.005
    lam = np.linspace(eps, 1.0 - eps, n_points)
    G = g_lambda_multimode(lam, N)
    sqrt_G = np.sqrt(G)

    # Accumulated FS length: s(λ) = ∫_ε^λ √G dλ'
    s = np.zeros_like(lam)
    dlam = np.diff(lam)
    for i in range(1, len(lam)):
        s[i] = s[i - 1] + 0.5 * (sqrt_G[i - 1] + sqrt_G[i]) * dlam[i - 1]

    # Quasipotential: V(λ) = s_total - s(λ)
    s_total = s[-1]
    V = s_total - s

    # Inverse metric: dλ/ds = 1/√G (peaks in middle)
    dlam_ds = 1.0 / sqrt_G

    # Standard QM visibility
    V_std = np.sqrt(np.clip(1.0 - lam**2, 0, None))

    return lam, G, s, V, dlam_ds, V_std


def find_minimum(lam, G):
    """Find the location and value of the metric minimum."""
    imin = np.argmin(G)
    return lam[imin], G[imin]


def write_data_csvs(lam, G, s, V, dlam_ds, V_std):
    """Write updated data CSV files for reference."""
    os.makedirs(DATA, exist_ok=True)

    # g_lambda.csv
    with open(os.path.join(DATA, 'g_lambda.csv'), 'w') as f:
        f.write('lambda,G_lambda_lambda\n')
        for l, g in zip(lam, G):
            f.write(f'{l},{g}\n')

    # v_lambda.csv
    with open(os.path.join(DATA, 'v_lambda.csv'), 'w') as f:
        f.write('lambda,V_lambda,V_standard_qm\n')
        for l, v, vs in zip(lam, V, V_std):
            f.write(f'{l},{v},{vs}\n')

    # s_lambda.csv (new)
    with open(os.path.join(DATA, 's_lambda.csv'), 'w') as f:
        f.write('lambda,s_lambda,dlambda_ds\n')
        for l, sl, dl in zip(lam, s, dlam_ds):
            f.write(f'{l},{sl},{dl}\n')


# ============================================================
# Figure 1: G_λλ(λ) — Fubini-Study metric on coherence space
# ============================================================
def fig1_g_lambda():
    lam, G, s, V, dlam_ds, V_std = compute_fs_quantities()
    lam_min, G_min = find_minimum(lam, G)

    fig, ax = plt.subplots(figsize=(7, 5))

    # Y-axis limit: show U-shape clearly without divergence dominating
    y_max = 8.0

    # Shaded regimes
    ax.axvspan(0, 0.08, alpha=0.15, color='blue', label='Coherent regime')
    ax.axvspan(lam_min - 0.15, lam_min + 0.15, alpha=0.12, color='#2ECC71',
               label='Crossover regime')
    ax.axvspan(0.92, 1.0, alpha=0.15, color='red', label='Classical regime')

    # Main curve
    mask = G < y_max * 1.5  # clip extreme values for cleaner display
    ax.plot(lam[mask], np.clip(G[mask], 0, y_max * 1.2), 'b-', linewidth=2.5)

    # Show divergence arrows at edges
    ax.annotate('', xy=(0.01, y_max - 0.3), xytext=(0.01, y_max - 1.5),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    ax.annotate('', xy=(0.99, y_max - 0.3), xytext=(0.99, y_max - 1.5),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

    # Minimum annotation
    ax.plot(lam_min, G_min, 'ko', markersize=8, zorder=5)
    ax.annotate(
        f'Crossover minimum\n$\\lambda \\approx {lam_min:.2f}$, '
        f'$G \\approx {G_min:.2f}$',
        xy=(lam_min, G_min),
        xytext=(0.55, G_min + 2.5),
        fontsize=11,
        arrowprops=dict(arrowstyle='->', color='black', lw=1.2),
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#D5F5E3',
                  edgecolor='gray', alpha=0.9))

    # Endpoint annotations
    ax.text(0.04, y_max * 0.85, 'Fragile\ncoherence',
            fontsize=10, ha='center', color='blue', style='italic')
    ax.text(0.96, y_max * 0.85, 'Rigid\nclassicality',
            fontsize=10, ha='center', color='red', style='italic')

    ax.set_xlabel(r'$\lambda$ (which-path distinguishability)')
    ax.set_ylabel(r'$G_{\lambda\lambda}$ (Fubini--Study metric)')
    ax.set_title(
        'Information-Geometric Metric on Coherence Space\n'
        f'(multi-mode decoherence, $N={N_MODES}$)',
        fontsize=13, pad=12)
    ax.legend(loc='upper center', framealpha=0.9, ncol=3, fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, y_max)

    # Write data files
    write_data_csvs(lam, G, s, V, dlam_ds, V_std)

    out = os.path.join(FIGS, 'fig1_g_lambda.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'  wrote {out}')

    # Print key values for paper
    s_total = s[-1]
    print(f'  N={N_MODES}: min G={G_min:.4f} at λ={lam_min:.4f}')
    print(f'  Geodesic integral ∫√G dλ ≈ {s_total:.4f}')


# ============================================================
# Figure 2: V(λ) — Quasipotential landscape
# ============================================================
def fig2_quasipotential():
    lam, G, s, V, dlam_ds, V_std = compute_fs_quantities()
    lam_min, _ = find_minimum(lam, G)

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(lam, V, 'r-', linewidth=2.5, label=r'$V(\lambda)$')

    # Endpoint markers
    ax.plot(lam[0], V[0], 'bo', markersize=10, zorder=5)
    ax.plot(lam[-1], V[-1], 'ro', markersize=10, zorder=5)

    # Shade the crossover plateau region
    cross_lo = lam_min - 0.15
    cross_hi = lam_min + 0.15
    mask_cross = (lam >= cross_lo) & (lam <= cross_hi)
    ax.axvspan(cross_lo, cross_hi, alpha=0.08, color='#2ECC71')

    # Annotations
    ax.annotate('Unstable coherent frame\n(steep geometric wall)',
                xy=(lam[0], V[0]),
                xytext=(0.25, V[0] * 0.92),
                fontsize=11,
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

    ax.annotate('Stable classical frame\n(pointer basis)',
                xy=(lam[-1], V[-1]),
                xytext=(0.6, V[-1] + V[0] * 0.15),
                fontsize=11,
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

    # Crossover annotation
    mid_idx = len(lam) // 2
    ax.annotate('Crossover plateau\n(geometric robustness)',
                xy=(lam_min, V[mid_idx]),
                xytext=(0.65, V[0] * 0.55),
                fontsize=11,
                arrowprops=dict(arrowstyle='->', color='#2ECC71', lw=1.2),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#D5F5E3',
                          edgecolor='gray', alpha=0.8))

    ax.set_xlabel(r'$\lambda$ (which-path distinguishability)')
    ax.set_ylabel(r'$V(\lambda)$ (quasipotential)')
    ax.set_title('Quasipotential Landscape on Coherence Space',
                 fontsize=14, pad=15)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_xlim(0, 1)

    out = os.path.join(FIGS, 'fig2_quasipotential.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'  wrote {out}')


# ============================================================
# Figure 3: Frame transformation schematic (double-slit)
# ============================================================
def fig3_frame_transformation():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-1.5, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(5, 7.5, 'Frame Transformation: Double-Slit Experiment',
            fontsize=18, ha='center', va='center', fontweight='bold')

    # --- Left box: F_int ---
    left_box = FancyBboxPatch((0.2, 1.5), 3.8, 4.5,
                               boxstyle='round,pad=0.2',
                               facecolor='#D4E6F1', edgecolor='blue',
                               linewidth=2.5)
    ax.add_patch(left_box)
    ax.text(2.1, 6.5, r'Frame $F_{int}$',
            fontsize=16, ha='center', color='blue', fontweight='bold')
    ax.text(2.1, 5.0,
            r'$|\psi\rangle = \frac{1}{\sqrt{2}}(|L\rangle + |R\rangle)$',
            fontsize=14, ha='center')
    ax.text(2.1, 3.8, 'Interference visible',
            fontsize=12, ha='center', style='italic', color='blue')
    ax.text(2.1, 2.5, r'$\rho_{LR} \neq 0$',
            fontsize=14, ha='center')

    # --- Right box: F_wp ---
    right_box = FancyBboxPatch((6.5, 1.5), 3.8, 4.5,
                                boxstyle='round,pad=0.2',
                                facecolor='#FEF9E7', edgecolor='orange',
                                linewidth=2.5)
    ax.add_patch(right_box)
    ax.text(8.4, 6.5, r'Frame $F_{wp}$',
            fontsize=16, ha='center', color='#E67E22', fontweight='bold')
    ax.text(8.4, 5.0,
            r'$|\Psi\rangle = \frac{1}{\sqrt{2}}(|L\rangle|W_L\rangle + |R\rangle|W_R\rangle)$',
            fontsize=13, ha='center')
    ax.text(8.4, 3.8, 'Which-path definite',
            fontsize=12, ha='center', style='italic', color='#E67E22')
    ax.text(8.4, 2.5, r'$\rho_{LR} = 0$',
            fontsize=14, ha='center')

    # --- Arrow ---
    ax.annotate('', xy=(6.3, 4.0), xytext=(4.2, 4.0),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='black'))
    ax.text(5.25, 4.5, r'$U_{F \to F\prime}$', fontsize=14, ha='center')
    ax.text(5.25, 3.4, '(detector coupling)', fontsize=11,
            ha='center', style='italic')

    # --- Bottom invariant box ---
    inv_box = FancyBboxPatch((2.5, 0.0), 5.5, 1.2,
                              boxstyle='round,pad=0.2',
                              facecolor='#D5F5E3', edgecolor='green',
                              linewidth=2.5)
    ax.add_patch(inv_box)
    ax.text(5.25, 0.6,
            r'Invariant: $\mu(L) = \mu(R) = \frac{1}{2}$',
            fontsize=14, ha='center', fontweight='bold', color='#1E8449')

    out = os.path.join(FIGS, 'fig3_frame_transformation.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'  wrote {out}')


# ============================================================
# Figure 4: Born rule as frame invariant (SR analogy)
# ============================================================
def fig4_born_rule_invariant():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Left panel: Special Relativity light cone ---
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Special Relativity', fontsize=15, pad=10)

    # Light cone
    ax1.plot([-2.5, 0, 2.5], [-2.5, 0, 2.5], color='#B7950B', linewidth=2.5)
    ax1.plot([-2.5, 0, 2.5], [2.5, 0, -2.5], color='#B7950B', linewidth=2.5)

    # Interior shading
    cone = Polygon([(-2.5, -2.5), (0, 0), (-2.5, 2.5)], alpha=0.08,
                   color='yellow')
    ax1.add_patch(cone)
    cone2 = Polygon([(2.5, -2.5), (0, 0), (2.5, 2.5)], alpha=0.08,
                    color='yellow')
    ax1.add_patch(cone2)

    # Frame S (blue, tilted up-right)
    ax1.annotate('', xy=(1.0, 2.0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax1.text(1.1, 2.1, '$S$', fontsize=14, color='blue', fontweight='bold')

    # Frame S' (red, tilted right)
    ax1.annotate('', xy=(2.0, 0.5), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax1.text(2.1, 0.6, "$S'$", fontsize=14, color='red', fontweight='bold')

    # Invariant label
    ax1.text(0, -2.8, r'Invariant: $ds^2 = -c^2dt^2 + dx^2$',
             fontsize=13, ha='center', color='#1E8449', fontweight='bold')

    # --- Right panel: Coherence Relativity Σ ---
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Coherence Relativity', fontsize=15, pad=10)

    # Σ label
    ax2.text(0, 2.5, r'$\Sigma$', fontsize=18, ha='center', va='center')

    # Circle for Σ
    circle = plt.Circle((0, 0), 1.8, fill=False, color='black', linewidth=2)
    ax2.add_patch(circle)

    # Geodesic arc on top (green)
    theta = np.linspace(0, np.pi, 100)
    xarc = 1.8 * np.cos(theta)
    yarc = 1.8 * np.sin(theta)
    ax2.plot(xarc, yarc, color='green', linewidth=3)

    # Frame points
    ax2.plot(-1.8, 0, 'ro', markersize=12, zorder=5)
    ax2.text(-2.4, 0.2, r'$F_{wp}$', fontsize=13, color='red',
             fontweight='bold')

    ax2.plot(1.8, 0, 'bo', markersize=12, zorder=5)
    ax2.text(2.0, 0.2, r'$F_{int}$', fontsize=13, color='blue',
             fontweight='bold')

    # Invariant label
    ax2.text(0, -2.8, r'Invariant: $\mu_F(i) = |c_i|^2$',
             fontsize=13, ha='center', color='#1E8449', fontweight='bold')

    # Suptitle
    fig.suptitle('The Born Rule as Frame Invariant',
                 fontsize=18, fontweight='bold', y=0.98)

    out = os.path.join(FIGS, 'fig4_born_rule_invariant.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'  wrote {out}')


# ============================================================
# Figure 5: Double-slit in two coherence frames
# ============================================================
def fig5_double_slit_frames():
    x = np.linspace(-3, 3, 500)

    # Interference pattern (F_int)
    envelope = np.exp(-x**2 / 2.0)
    interference = envelope * np.cos(np.pi * x)**2
    interference /= interference.max()

    # Which-path pattern (F_wp): two separated Gaussians
    path_L = 0.5 * np.exp(-(x + 0.7)**2 / 0.8)
    path_R = 0.5 * np.exp(-(x - 0.7)**2 / 0.8)
    combined = path_L + path_R

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left: Interference frame ---
    ax1.plot(x, interference, 'b-', linewidth=2.5)
    ax1.fill_between(x, interference, alpha=0.2, color='blue')
    ax1.set_xlabel('Screen position')
    ax1.set_ylabel('Detection probability')
    ax1.set_title(r'$F_{int}$: Interference Frame',
                  fontsize=14, color='blue')
    ax1.text(0.3, 0.85, 'Coherence visible\n' + r'$\rho_{LR} \neq 0$',
             fontsize=11, style='italic',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#D4E6F1',
                       edgecolor='gray', alpha=0.8),
             transform=ax1.transAxes)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(0, 1.05)

    # --- Right: Which-path frame ---
    ax2.fill_between(x, path_L, alpha=0.3, color='red', label='Path L')
    ax2.fill_between(x, path_R, alpha=0.3, color='orange', label='Path R')
    ax2.plot(x, combined, 'r-', linewidth=2.5)
    ax2.set_xlabel('Screen position')
    ax2.set_ylabel('Detection probability')
    ax2.set_title(r'$F_{wp}$: Which-Path Frame',
                  fontsize=14, color='red')
    ax2.text(0.05, 0.85, 'Paths definite\n' + r'$\rho_{LR} = 0$',
             fontsize=11, style='italic',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDEDEC',
                       edgecolor='gray', alpha=0.8),
             transform=ax2.transAxes)
    ax2.legend(loc='upper right', framealpha=0.9)
    ax2.set_xlim(-3, 3)

    fig.suptitle('Same Physical Setup, Two Coherence Frames',
                 fontsize=16, fontweight='bold', y=1.02)
    fig.tight_layout()

    out = os.path.join(FIGS, 'fig5_double_slit_frames.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'  wrote {out}')


# ============================================================
# Figure 6: CR geometric transition vs standard QM visibility
# ============================================================
def fig6_cr_vs_standard():
    lam, G, s, V, dlam_ds, V_std = compute_fs_quantities()

    # Normalize V to [0, 1]: V(0)→1, V(1)→0
    V_norm = V / V[0]

    fig, ax = plt.subplots(figsize=(7, 5))

    # Shaded deviation region
    ax.fill_between(lam, V_norm, V_std,
                    alpha=0.2, color='green', label='Testable deviation')

    # CR curve (normalized quasipotential = normalized FS distance)
    ax.plot(lam, V_norm, 'r-', linewidth=2.5,
            label=r'CR: $V(\lambda)/V(0)$ (geometric)')

    # Standard QM curve
    ax.plot(lam, V_std, 'b--', linewidth=2.5,
            label=r'Standard QM: $\mathcal{V} = \sqrt{1-\lambda^2}$')

    # Annotations
    # Find max deviation
    dev = np.abs(V_norm - V_std)
    imax = np.argmax(dev)
    ax.annotate(f'Max deviation\n$\\Delta \\approx {dev[imax]:.3f}$',
                xy=(lam[imax], (V_norm[imax] + V_std[imax]) / 2),
                xytext=(0.65, 0.7),
                fontsize=11,
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='gray', alpha=0.9))

    ax.set_xlabel(r'$\lambda$ (which-path distinguishability)')
    ax.set_ylabel('Normalized value')
    ax.set_title('CR Geometric Transition vs Standard QM Visibility',
                 fontsize=13, pad=15)
    ax.legend(loc='lower left', framealpha=0.9, fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)

    out = os.path.join(FIGS, 'fig6_cr_vs_standard.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'  wrote {out}')


# ============================================================
# Figure 7: Experimental setup schematics
# ============================================================
def fig7_experimental_setup():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left panel: Continuous decoherence monitoring ---
    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1, 7)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Prediction 2: Continuous Decoherence\nMonitoring',
                  fontsize=14, fontweight='bold', pad=10)

    # Source box
    src = FancyBboxPatch((0, 2.5), 1.8, 1.5,
                          boxstyle='round,pad=0.15',
                          facecolor='#FDEBD0', edgecolor='black', lw=1.5)
    ax1.add_patch(src)
    ax1.text(0.9, 3.25, 'Source', fontsize=11, ha='center', va='center')

    # Arrow source -> slits
    ax1.annotate('', xy=(2.8, 3.25), xytext=(2.0, 3.25),
                 arrowprops=dict(arrowstyle='->', lw=1.5))

    # Slits
    ax1.plot([3.0, 3.0], [1.5, 2.8], 'k-', lw=3)
    ax1.plot([3.0, 3.0], [3.7, 5.0], 'k-', lw=3)
    ax1.text(3.0, 1.0, 'Slits', fontsize=10, ha='center')

    # Detector box
    det = FancyBboxPatch((4.5, 2.5), 2.2, 1.5,
                          boxstyle='round,pad=0.15',
                          facecolor='#FADBD8', edgecolor='red', lw=1.5)
    ax1.add_patch(det)
    ax1.text(5.6, 3.25, r'Detector' + '\n' + r'$\lambda$ tunable',
             fontsize=10, ha='center', va='center')

    # Arrow detector -> screen
    ax1.annotate('', xy=(7.8, 3.25), xytext=(6.9, 3.25),
                 arrowprops=dict(arrowstyle='->', lw=1.5))

    # Screen
    ax1.plot([8.0, 8.0], [1.5, 5.0], color='blue', lw=3)
    ax1.text(8.0, 1.0, 'Screen', fontsize=10, ha='center')

    # Measurement note
    ax1.text(5.6, 5.5,
             r'Measure $G_{\lambda\lambda}$' + '\nvs. detector strength',
             fontsize=10, ha='center', style='italic',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#D5F5E3',
                       edgecolor='gray', alpha=0.8))

    # --- Right panel: Quantum Darwinism frame selection ---
    ax2.set_xlim(-2, 10)
    ax2.set_ylim(-1, 7)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Prediction 5: Quantum Darwinism\nFrame Selection',
                  fontsize=14, fontweight='bold', pad=10)

    # System circle
    sys_circle = plt.Circle((2, 3.5), 1.0, facecolor='#D4E6F1',
                             edgecolor='blue', linewidth=2.5)
    ax2.add_patch(sys_circle)
    ax2.text(2, 3.5, 'System\n$S$', fontsize=12, ha='center',
             va='center', style='italic')

    # Environment fragments
    env_positions = [(6, 5.5), (6, 3.5), (6, 1.5)]
    env_labels = [r'$E_1$', r'$E_2$', r'$E_3$']
    for (ex, ey), lab in zip(env_positions, env_labels):
        ec = plt.Circle((ex, ey), 0.5, facecolor='#FEF9E7',
                         edgecolor='orange', linewidth=2)
        ax2.add_patch(ec)
        ax2.text(ex, ey, lab, fontsize=12, ha='center', va='center')
        ax2.annotate('', xy=(ex - 0.6, ey), xytext=(3.1, 3.5),
                     arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))

    # E4 (further out)
    e4 = plt.Circle((8.5, 3.5), 0.5, facecolor='#FEF9E7',
                     edgecolor='orange', linewidth=2)
    ax2.add_patch(e4)
    ax2.text(8.5, 3.5, r'$E_4$', fontsize=12, ha='center', va='center')
    ax2.annotate('', xy=(7.9, 3.5), xytext=(6.6, 3.5),
                 arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))

    # Note
    ax2.text(5.5, 0.2,
             r'Increase $N$ fragments $\rightarrow$' + '\n'
             + r'Observe $V(\lambda)$ narrowing',
             fontsize=10, ha='center', style='italic',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#D5F5E3',
                       edgecolor='gray', alpha=0.8))

    fig.tight_layout()

    out = os.path.join(FIGS, 'fig7_experimental_setup.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'  wrote {out}')


# ============================================================
# Main
# ============================================================
GENERATORS = {
    '1': ('fig1_g_lambda',           fig1_g_lambda),
    '2': ('fig2_quasipotential',     fig2_quasipotential),
    '3': ('fig3_frame_transformation', fig3_frame_transformation),
    '4': ('fig4_born_rule_invariant', fig4_born_rule_invariant),
    '5': ('fig5_double_slit_frames', fig5_double_slit_frames),
    '6': ('fig6_cr_vs_standard',     fig6_cr_vs_standard),
    '7': ('fig7_experimental_setup', fig7_experimental_setup),
}

if __name__ == '__main__':
    which = sys.argv[1:] if len(sys.argv) > 1 else sorted(GENERATORS.keys())

    for key in which:
        if key not in GENERATORS:
            print(f'Unknown figure: {key}. Options: {sorted(GENERATORS.keys())}')
            continue
        name, func = GENERATORS[key]
        print(f'Generating {name}...')
        func()

    print('\nDone.')
