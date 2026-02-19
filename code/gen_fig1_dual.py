#!/usr/bin/env python3
"""Generate two-panel Fig 1: G_λλ (U-shaped) + dλ/ds (peaked) as dual views."""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex': False,
    'mathtext.fontset': 'cm',
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 9,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
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

# Find extrema
imin = np.argmin(G)
lam_min, G_min = lam[imin], G[imin]
ipeak = np.argmax(dlam_ds)
lam_peak, val_peak = lam[ipeak], dlam_ds[ipeak]

# Accumulated FS length for s*
sqrt_G = np.sqrt(G)
s = np.zeros_like(lam)
dl = np.diff(lam)
for i in range(1, len(lam)):
    s[i] = s[i-1] + 0.5 * (sqrt_G[i-1] + sqrt_G[i]) * dl[i-1]
s_star = s[ipeak]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5))

# ======== Left panel: G_λλ (U-shaped) ========
y_max = 8.0

ax1.axvspan(0, 0.08, alpha=0.15, color='blue')
ax1.axvspan(lam_min - 0.15, lam_min + 0.15, alpha=0.10, color='#2ECC71')
ax1.axvspan(0.92, 1.0, alpha=0.15, color='red')

mask = G < y_max * 1.5
ax1.plot(lam[mask], np.clip(G[mask], 0, y_max * 1.2), 'b-', linewidth=2.5)

# Divergence arrows
ax1.annotate('', xy=(0.01, y_max - 0.3), xytext=(0.01, y_max - 1.5),
             arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
ax1.annotate('', xy=(0.99, y_max - 0.3), xytext=(0.99, y_max - 1.5),
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# Minimum
ax1.plot(lam_min, G_min, 'ko', markersize=7, zorder=5)
ax1.annotate(
    r'Min: $G \approx ' + f'{G_min:.2f}$',
    xy=(lam_min, G_min),
    xytext=(0.60, G_min + 2.2),
    fontsize=10,
    arrowprops=dict(arrowstyle='->', color='black', lw=1.0),
    bbox=dict(boxstyle='round,pad=0.2', facecolor='#D5F5E3',
              edgecolor='gray', alpha=0.9))

ax1.text(0.04, y_max * 0.85, 'Fragile',
         fontsize=9, ha='center', color='blue', style='italic')
ax1.text(0.96, y_max * 0.85, 'Rigid',
         fontsize=9, ha='center', color='red', style='italic')

ax1.set_xlabel(r'$\lambda$ (which-path distinguishability)')
ax1.set_ylabel(r'$G_{\lambda\lambda} = (ds/d\lambda)^2$')
ax1.set_title(r'(a) State sensitivity to $\lambda$', fontsize=13, pad=10)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, y_max)

# ======== Right panel: dλ/ds (peaked) ========
ax2.axvspan(0, 0.08, alpha=0.15, color='blue')
ax2.axvspan(lam_peak - 0.15, lam_peak + 0.15, alpha=0.10, color='#2ECC71')
ax2.axvspan(0.92, 1.0, alpha=0.15, color='red')

ax2.plot(lam, dlam_ds, color='#8E44AD', linewidth=2.5)

# Peak
ax2.plot(lam_peak, val_peak, 'ko', markersize=7, zorder=5)
ax2.annotate(
    r'Max: $d\lambda/ds \approx ' + f'{val_peak:.2f}$',
    xy=(lam_peak, val_peak),
    xytext=(0.62, val_peak - 0.10),
    fontsize=10,
    arrowprops=dict(arrowstyle='->', color='black', lw=1.0),
    bbox=dict(boxstyle='round,pad=0.2', facecolor='#D5F5E3',
              edgecolor='gray', alpha=0.9))

ax2.text(0.04, 0.05, 'Fragile',
         fontsize=9, ha='center', color='blue', style='italic')
ax2.text(0.96, 0.05, 'Rigid',
         fontsize=9, ha='center', color='red', style='italic')

ax2.set_xlabel(r'$\lambda$ (which-path distinguishability)')
ax2.set_ylabel(r'$d\lambda/ds = 1/\sqrt{G_{\lambda\lambda}}$')
ax2.set_title(r'(b) $\lambda$ sensitivity to state motion', fontsize=13, pad=10)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, val_peak * 1.15)

fig.tight_layout(w_pad=3.0)

out = os.path.join(FIGS, 'fig1_g_lambda.pdf')
fig.savefig(out)
plt.close(fig)
print(f'wrote {out}')
print(f'Left panel: min G = {G_min:.4f} at lambda = {lam_min:.4f}')
print(f'Right panel: max dlam/ds = {val_peak:.4f} at lambda = {lam_peak:.4f}')
print(f'Geometric activation distance s* = {s_star:.4f}')
