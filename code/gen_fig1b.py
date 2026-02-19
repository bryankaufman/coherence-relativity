#!/usr/bin/env python3
"""Generate reciprocal metric figure: dλ/ds = 1/√G (peaks in middle)."""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(ROOT, 'figures')

N = 10
eps = 0.005
lam = np.linspace(eps, 1.0 - eps, 2000)
u = 1.0 - lam
exp1 = 2.0 * (N - 1) / N
exp2 = 2.0 / N
denom = 2.0 * N * np.power(u, exp1) * (1.0 - np.power(u, exp2))
G = 1.0 / denom
dlam_ds = 1.0 / np.sqrt(G)

# Find peak
ipeak = np.argmax(dlam_ds)
lam_peak = lam[ipeak]
val_peak = dlam_ds[ipeak]

fig, ax = plt.subplots(figsize=(7, 5))

# Shaded regimes
ax.axvspan(0, 0.08, alpha=0.15, color='blue', label='Coherent regime')
ax.axvspan(lam_peak - 0.15, lam_peak + 0.15, alpha=0.12, color='#2ECC71',
           label='Crossover regime')
ax.axvspan(0.92, 1.0, alpha=0.15, color='red', label='Classical regime')

# Main curve
ax.plot(lam, dlam_ds, color='#8E44AD', linewidth=2.5)

# Peak annotation
ax.plot(lam_peak, val_peak, 'ko', markersize=8, zorder=5)
ax.annotate(
    r'Maximum sensitivity' + '\n'
    + r'$\lambda \approx ' + f'{lam_peak:.2f}' + r'$, '
    + r'$d\lambda/ds \approx ' + f'{val_peak:.3f}' + r'$',
    xy=(lam_peak, val_peak),
    xytext=(0.58, val_peak - 0.12),
    fontsize=11,
    arrowprops=dict(arrowstyle='->', color='black', lw=1.2),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#D5F5E3',
              edgecolor='gray', alpha=0.9))

# Endpoint annotations
ax.text(0.04, 0.06, 'Geometrically\nfragile',
        fontsize=10, ha='center', color='blue', style='italic')
ax.text(0.96, 0.06, 'Geometrically\nrigid',
        fontsize=10, ha='center', color='red', style='italic')

ax.set_xlabel(r'$\lambda$ (which-path distinguishability)')
ax.set_ylabel(r'$d\lambda/ds = 1/\sqrt{G_{\lambda\lambda}}$')
ax.set_title(
    'Distinguishability Gain per Unit Geometric Distance\n'
    + r'(multi-mode decoherence, $N=' + str(N) + r'$)',
    fontsize=13, pad=12)
ax.legend(loc='upper right', framealpha=0.9, fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, val_peak * 1.15)

out = os.path.join(FIGS, 'fig1b_dlam_ds.pdf')
fig.savefig(out)
plt.close(fig)
print(f'wrote {out}')
print(f'Peak: d\u03bb/ds = {val_peak:.4f} at \u03bb = {lam_peak:.4f}')
