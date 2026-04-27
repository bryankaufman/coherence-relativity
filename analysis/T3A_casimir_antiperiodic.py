#!/usr/bin/env python3
"""
T3-A Spectral Casimir — Antiperiodic Variant
==============================================

Tests antiperiodic boundary conditions on S¹(b) as a diagnostic for
whether the S₁ zero-mode term is responsible for the EOS sign failure
observed in the conformal scalar run.

Physical argument
-----------------
The conformal scalar run showed w₃ ≈ 0.5–1.5 throughout the ρ > 0 region.
Root cause: the S₁ contribution E_S₁ = bD/(4a²) gives ∂E/∂a ∝ −1/a³,
which forces p₃ = (2/3)ρ (radiation-like) regardless of N_EFF.

Antiperiodic BCs (m → m+½) have NO zero mode (no integer n satisfies
n+½=0), so S₁ = 0 by construction.  The S₂ Bessel sum picks up the
Poisson-resummation phase e^{iπk} = (−1)^k per winding number.

Chowla-Selberg decomposition for antiperiodic BCs
---------------------------------------------------
E_ap(a,b) = 0  [S₁]
           − (1/(πa)) Σ_{l≥1,k≥1} (−1)^k l²√(l²+c) K₁(x_{lk}) / k  [S₂_ap]

where x_{lk} = 2πk√(l²+c) b/a.

Sign check (b/a → 0):
  K₁(x) → 1/x  →  Σ_k (−1)^k/k² = −π²/12  →  F_ap < 0
  E_ap = −(1/(πa)) × F_ap > 0   ✓  (positive energy density)

EOS prediction (b/a → 0 limit, analytic):
  E_ap ≈ C/b  →  ∂E/∂a → 0  →  w₃ → 0
  For intermediate b/a: rG′(r)/G(r) < −1 possible  →  w₃ < 0

The ODE system is unchanged from T3A_casimir_spectral.py (correct 5D
Einstein equations with anisotropic Casimir source).

Comparison run structure
------------------------
  1. Build AP interpolation grid (100×100)
  2. Plot E, ρ, w₃, w_φ landscape
  3. Compare w₃ landscape against conformal scalar results
  4. Run ODE periodic-orbit search
"""

import os
import json
import numpy as np
from scipy.special import kv as bessel_kv
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ─── Constants ─────────────────────────────────────────────────────────
KAPPA5 = 1.0       # 5D gravitational coupling (units: κ₅ = 1)
K_CURV = 1.0       # S³ curvature k = +1
N_EFF  = 1.0       # scalar d.o.f. multiplier

ZETA_R3 = 1.2020569031595942    # ζ(3)
ZETA_R5 = 1.0369277551433699    # ζ(5)
ZETA_PRIME_M2 = -ZETA_R3 / (4 * np.pi**2)       # ζ′(−2) ≈ −0.03045
ZETA_PRIME_M4 =  3 * ZETA_R5 / (4 * np.pi**4)   # ζ′(−4) ≈  0.00798

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def _D_constant(c):
    """D(c) = 2ζ′(−4) + 2c ζ′(−2) + c²/4  (periodic S₁ constant, for reference)."""
    return 2 * ZETA_PRIME_M4 + 2 * c * ZETA_PRIME_M2 + c**2 / 4


# ═══════════════════════════════════════════════════════════════════════
#  1.  Antiperiodic energy evaluator
# ═══════════════════════════════════════════════════════════════════════

def casimir_E_antiperiodic(a, b, c=1/8, l_max=50, k_max=20):
    """
    Renormalized Casimir energy and derivatives for ANTIPERIODIC BCs on S¹(b).

    Modification from the periodic formula:
      • S₁ = 0  (no zero-mode contribution)
      • S₂ Bessel sum: each k-winding gets factor (−1)^k
          sign(k) = +1 for k even, −1 for k odd

    Returns
    -------
    E, dE_da, dE_db : float
    """
    r = b / a

    # ── Antiperiodic S₂: Σ (−1)^k prefac K₁(x_{lk}) / k ──
    F     = 0.0
    dF_da = 0.0
    dF_db = 0.0

    for l in range(1, l_max + 1):
        l2c = l * l + c
        if l2c <= 0:
            continue
        sqrt_l2c = np.sqrt(l2c)
        prefac   = l * l * sqrt_l2c       # l² √(l²+c)

        for k in range(1, k_max + 1):
            sign = 1.0 if (k % 2 == 0) else -1.0   # (−1)^k
            x    = 2.0 * np.pi * k * sqrt_l2c * r

            if x > 500.0:
                break   # K₁ exponentially negligible

            K1 = bessel_kv(1, x)
            K0 = bessel_kv(0, x)
            K2 = bessel_kv(2, x)

            F     += sign * prefac * K1 / k
            dF_da += sign * prefac * ( x / (2.0 * a)) * (K0 + K2) / k
            dF_db += sign * prefac * (-x / (2.0 * b)) * (K0 + K2) / k

        # Early l-termination when even k=1 is already negligible
        if 2.0 * np.pi * sqrt_l2c * r > 100.0:
            break

    # E = −(1/(πa)) F,   ∂E/∂a = (F/(πa²)) − (dF_da/(πa)),   ∂E/∂b = −dF_db/(πa)
    E     = N_EFF * (-1.0 / (np.pi * a)) * F
    dE_da = N_EFF * ( (1.0 / (np.pi * a**2)) * F
                     + (-1.0 / (np.pi * a)) * dF_da )
    dE_db = N_EFF * ( (-1.0 / (np.pi * a)) * dF_db )

    return E, dE_da, dE_db


def casimir_source_ap_direct(a, b, Ha, Hb, c=1/8):
    """Direct (slow) evaluation of (ρ, p₃, p_φ, dρ/dt) for spot-checks."""
    V4 = 4.0 * np.pi**3 * a**3 * b
    E, dE_da, dE_db = casimir_E_antiperiodic(a, b, c)

    rho  =  E / V4
    p3   = -(a / (3.0 * V4)) * dE_da
    pphi = -(b / V4) * dE_db

    drho_dt = ((dE_da / V4) - 3.0 * rho / a) * a * Ha \
            + ((dE_db / V4) - rho / b) * b * Hb

    return rho, p3, pphi, drho_dt


# ═══════════════════════════════════════════════════════════════════════
#  2.  Interpolation layer
# ═══════════════════════════════════════════════════════════════════════

class CasimirInterpolatorAP:
    """
    Precomputed bicubic-spline interpolator for the antiperiodic Casimir
    energy and its partial derivatives.
    """

    def __init__(self, a_range=(0.1, 8.0), b_range=(0.1, 8.0),
                 Na=100, Nb=100, c=1/8):
        self.c = c
        self.a_lo, self.a_hi = a_range
        self.b_lo, self.b_hi = b_range
        self.a_arr = np.linspace(self.a_lo, self.a_hi, Na)
        self.b_arr = np.linspace(self.b_lo, self.b_hi, Nb)

        print(f"Building ANTIPERIODIC Casimir grid ({Na}×{Nb}), c={c:.4f} …")
        E_g    = np.zeros((Na, Nb))
        dEda_g = np.zeros((Na, Nb))
        dEdb_g = np.zeros((Na, Nb))

        for i, av in enumerate(self.a_arr):
            if i % 10 == 0:
                print(f"  row {i}/{Na}", end="\r", flush=True)
            for j, bv in enumerate(self.b_arr):
                E_g[i, j], dEda_g[i, j], dEdb_g[i, j] = \
                    casimir_E_antiperiodic(av, bv, c)

        self.spl_E    = RectBivariateSpline(self.a_arr, self.b_arr, E_g)
        self.spl_dEda = RectBivariateSpline(self.a_arr, self.b_arr, dEda_g)
        self.spl_dEdb = RectBivariateSpline(self.a_arr, self.b_arr, dEdb_g)
        self.E_grid   = E_g
        print(f"\n  Grid complete.  E range: [{E_g.min():.3e}, {E_g.max():.3e}]")

    def _clamp(self, a, b):
        return (np.clip(a, self.a_lo, self.a_hi),
                np.clip(b, self.b_lo, self.b_hi))

    def eval(self, a, b):
        a, b = self._clamp(a, b)
        E    = float(self.spl_E(a, b,    grid=False))
        dEda = float(self.spl_dEda(a, b, grid=False))
        dEdb = float(self.spl_dEdb(a, b, grid=False))
        return E, dEda, dEdb

    def source(self, state, params=None):
        """ODE-compatible source: returns (ρ, p₃, p_φ, dρ/dt)."""
        a, Ha, b, Hb = state
        a_c, b_c = self._clamp(a, b)
        V4 = 4.0 * np.pi**3 * a_c**3 * b_c
        E, dEda, dEdb = self.eval(a_c, b_c)

        rho  =  E / V4
        p3   = -(a_c / (3.0 * V4)) * dEda
        pphi = -(b_c / V4) * dEdb

        drho_dt = ((dEda / V4) - 3.0 * rho / a_c) * a_c * Ha \
                + ((dEdb / V4) - rho / b_c) * b_c * Hb

        return rho, p3, pphi, drho_dt


# ═══════════════════════════════════════════════════════════════════════
#  3.  Energy-landscape diagnostics
# ═══════════════════════════════════════════════════════════════════════

def plot_landscape_comparison(interp_ap, label="antiperiodic"):
    """
    Four-panel plot: E, ρ, w₃, w_φ over (a,b) space.
    Annotations show where w₃ < 0 (the region needed for periodic orbits).
    """
    a_arr, b_arr = interp_ap.a_arr, interp_ap.b_arr
    Na, Nb = len(a_arr), len(b_arr)

    E_g    = np.zeros((Na, Nb))
    rho_g  = np.zeros((Na, Nb))
    w3_g   = np.full((Na, Nb), np.nan)
    wphi_g = np.full((Na, Nb), np.nan)

    for i, av in enumerate(a_arr):
        for j, bv in enumerate(b_arr):
            E, dEda, dEdb = interp_ap.eval(av, bv)
            V4 = 4.0 * np.pi**3 * av**3 * bv
            rho  =  E / V4
            p3   = -(av / (3.0 * V4)) * dEda
            pphi = -(bv / V4) * dEdb

            E_g[i, j]   = E
            rho_g[i, j] = rho
            if abs(rho) > 1e-30:
                w3_g[i, j]   = p3 / rho
                wphi_g[i, j] = pphi / rho

    B, A = np.meshgrid(b_arr, a_arr)

    # ── Report fraction of (a,b) space with w₃ < 0 ──
    w3_finite = w3_g[np.isfinite(w3_g)]
    frac_neg  = np.sum(w3_finite < 0) / len(w3_finite) if len(w3_finite) > 0 else 0.0
    print(f"\nEOS statistics ({label}):")
    print(f"  w₃ range (finite):  [{np.nanmin(w3_g):.3f}, {np.nanmax(w3_g):.3f}]")
    print(f"  w_φ range (finite): [{np.nanmin(wphi_g):.3f}, {np.nanmax(wphi_g):.3f}]")
    print(f"  Fraction of grid with w₃ < 0:  {100*frac_neg:.1f}%")
    print(f"  Fraction of grid with ρ > 0:   "
          f"{100*np.sum(rho_g > 0)/(Na*Nb):.1f}%")

    # ── Sample points for EOS table ──
    sample_ratios = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    print(f"\n  EOS at a=2.0, varying r=b/a:")
    print(f"  {'r=b/a':>8}  {'E':>12}  {'ρ':>12}  {'w₃':>8}  {'w_φ':>8}")
    for r in sample_ratios:
        av, bv = 2.0, 2.0 * r
        if bv < interp_ap.b_hi:
            E, dEda, dEdb = interp_ap.eval(av, bv)
            V4 = 4.0 * np.pi**3 * av**3 * bv
            rho  =  E / V4
            p3   = -(av / (3.0 * V4)) * dEda
            pphi = -(bv / V4) * dEdb
            w3_v   = p3   / rho if abs(rho) > 1e-30 else np.nan
            wphi_v = pphi / rho if abs(rho) > 1e-30 else np.nan
            print(f"  {r:>8.2f}  {E:>12.4e}  {rho:>12.4e}  {w3_v:>8.3f}  {wphi_v:>8.3f}")

    # ── Four-panel plot ──
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle(f"Antiperiodic Casimir EOS landscape  [c={interp_ap.c:.3f}]",
                 fontsize=13)

    ax = axes[0, 0]
    cp = ax.contourf(A, B, E_g, levels=40, cmap="RdBu_r")
    ax.contour(A, B, E_g, levels=[0], colors="k", linewidths=2)
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("E_Cas(a,b)  [zero contour = black]")

    ax = axes[0, 1]
    cp = ax.contourf(A, B, rho_g, levels=40, cmap="RdBu_r")
    ax.contour(A, B, rho_g, levels=[0], colors="k", linewidths=2)
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("ρ(a,b)  [zero contour = black]")

    ax = axes[1, 0]
    w3_clip = np.clip(w3_g, -3, 3)
    cp = ax.contourf(A, B, w3_clip, levels=40, cmap="coolwarm",
                     vmin=-3, vmax=3)
    ax.contour(A, B, w3_g, levels=[0], colors="k", linewidths=2, linestyles="--")
    ax.contour(A, B, w3_g, levels=[-1/3], colors="g", linewidths=1.5, linestyles=":")
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("w₃ = p₃/ρ  [clipped ±3; black=0, green=−⅓]")

    ax = axes[1, 1]
    wphi_clip = np.clip(wphi_g, -3, 3)
    cp = ax.contourf(A, B, wphi_clip, levels=40, cmap="coolwarm",
                     vmin=-3, vmax=3)
    ax.contour(A, B, wphi_g, levels=[0], colors="k", linewidths=2, linestyles="--")
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("w_φ = p_φ/ρ  [clipped ±3; black=0]")

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, f"T3A_casimir_ap_landscape.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"\nSaved: {fig_path}")

    return w3_g, wphi_g, rho_g


# ═══════════════════════════════════════════════════════════════════════
#  4.  Full 5D Einstein ODE
# ═══════════════════════════════════════════════════════════════════════

def rhs_full_5d(t, state, source_fn, source_params):
    a, Ha, b, Hb = state
    if a <= 0 or b <= 0:
        return [0.0, 0.0, 0.0, 0.0]
    rho, p3, pphi, _ = source_fn(state, source_params)
    da  = a * Ha
    dHa = -(2.0 * Ha**2 + K_CURV / a**2 + KAPPA5 * pphi / 3.0)
    db  = b * Hb
    dHb = (Ha**2 + K_CURV / a**2
           - 2.0 * Ha * Hb - Hb**2
           + KAPPA5 * (2.0 * pphi / 3.0 - p3))
    return [da, dHa, db, dHb]


def constraint_residual(state, source_fn):
    a, Ha, b, Hb = state
    rho, _, _, _ = source_fn(state, None)
    return 3.0 * Ha**2 + 3.0 * K_CURV / a**2 + 3.0 * Ha * Hb - KAPPA5 * rho


def continuity_residual(state, source_fn):
    a, Ha, b, Hb = state
    rho, p3, pphi, drho_dt = source_fn(state, None)
    return drho_dt + 3.0 * Ha * (rho + p3) + Hb * (rho + pphi)


def init_from_constraint(a0, Ha0, b0, source_fn):
    """Solve 3H_a² + 3k/a² + 3H_a H_b = κρ for H_b."""
    if abs(Ha0) < 1e-14:
        return None
    probe = [a0, Ha0, b0, 0.0]
    rho, _, _, _ = source_fn(probe, None)
    Hb0 = (KAPPA5 * rho - 3.0 * Ha0**2 - 3.0 * K_CURV / a0**2) / (3.0 * Ha0)
    return np.array([a0, Ha0, b0, Hb0], dtype=float)


# ═══════════════════════════════════════════════════════════════════════
#  5.  Periodic-orbit search
# ═══════════════════════════════════════════════════════════════════════

def run_ap_case(interp, init_grid, tmax=60.0, label="spectral_antiperiodic"):
    """Integrate 5D system with antiperiodic Casimir source; search for oscillations."""
    source_fn = interp.source
    a_lo, a_hi = interp.a_lo, interp.a_hi
    b_lo, b_hi = interp.b_lo, interp.b_hi

    print(f"\n{'='*72}")
    print(f"CASE: {label}")
    print(f"{'='*72}")

    results = []

    for (a0, Ha0, b0) in init_grid:
        state0 = init_from_constraint(a0, Ha0, b0, source_fn)
        if state0 is None or not np.isfinite(state0).all():
            continue
        if abs(state0[3]) > 50:
            continue

        def ev_a_lo(t, y, *a): return y[0] - a_lo * 1.05
        ev_a_lo.terminal = True; ev_a_lo.direction = -1

        def ev_b_lo(t, y, *a): return y[2] - b_lo * 1.05
        ev_b_lo.terminal = True; ev_b_lo.direction = -1

        def ev_a_hi(t, y, *a): return a_hi * 0.95 - y[0]
        ev_a_hi.terminal = True; ev_a_hi.direction = -1

        def ev_b_hi(t, y, *a): return b_hi * 0.95 - y[2]
        ev_b_hi.terminal = True; ev_b_hi.direction = -1

        def ev_blow(t, y, *a): return 1e6 - (abs(y[1]) + abs(y[3]))
        ev_blow.terminal = True

        try:
            sol = solve_ivp(
                rhs_full_5d,
                [0.0, tmax],
                state0,
                args=(source_fn, None),
                method="Radau",
                max_step=0.05,
                rtol=1e-9,
                atol=1e-11,
                events=[ev_a_lo, ev_b_lo, ev_a_hi, ev_b_hi, ev_blow],
            )
        except Exception:
            continue

        if len(sol.t) < 20:
            continue

        C = np.array([constraint_residual(sol.y[:, i], source_fn)
                      for i in range(sol.y.shape[1])])
        D = np.array([continuity_residual(sol.y[:, i], source_fn)
                      for i in range(sol.y.shape[1])])

        Ha_cross = int(np.sum(np.diff(np.sign(sol.y[1])) != 0))
        Hb_cross = int(np.sum(np.diff(np.sign(sol.y[3])) != 0))

        rec = {
            "ic": {"a0": a0, "Ha0": Ha0, "b0": b0, "Hb0": float(state0[3])},
            "t_end": float(sol.t[-1]),
            "a_range": [float(np.min(sol.y[0])), float(np.max(sol.y[0]))],
            "b_range": [float(np.min(sol.y[2])), float(np.max(sol.y[2]))],
            "Ha_crossings": Ha_cross,
            "Hb_crossings": Hb_cross,
            "max_abs_constraint": float(np.max(np.abs(C))),
            "max_abs_continuity": float(np.max(np.abs(D))),
            "survived_full_window": bool(sol.t[-1] >= 0.98 * tmax),
        }
        results.append((rec, sol, C, D))

    if not results:
        print("No successful trajectories.")
        return []

    total = len(results)
    surv  = sum(r[0]["survived_full_window"] for r in results)
    osc   = sum(r[0]["Ha_crossings"] >= 4 for r in results)
    print(f"Trajectories integrated: {total}")
    print(f"Survived full window:    {surv}")
    print(f"Oscillatory candidates (H_a crossings ≥ 4):  {osc}")
    print("Constraint |C| range: "
          f"[{min(r[0]['max_abs_constraint'] for r in results):.2e}, "
          f"{max(r[0]['max_abs_constraint'] for r in results):.2e}]")
    print("Continuity |D| range: "
          f"[{min(r[0]['max_abs_continuity'] for r in results):.2e}, "
          f"{max(r[0]['max_abs_continuity'] for r in results):.2e}]")

    ranked = sorted(results,
                    key=lambda x: (-x[0]["Ha_crossings"] - x[0]["Hb_crossings"],
                                    x[0]["max_abs_constraint"]))
    best = ranked[0]
    rec, sol, C, D = best
    print(f"\nBest trajectory IC: {rec['ic']}")
    print(f"  crossings (H_a, H_b): {rec['Ha_crossings']}, {rec['Hb_crossings']}")
    print(f"  max |C|: {rec['max_abs_constraint']:.2e}")
    print(f"  max |D|: {rec['max_abs_continuity']:.2e}")
    print(f"  survived: {rec['survived_full_window']}")

    # ── Plot best trajectory ──
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle(f"{label} — best trajectory\n"
                 f"IC: a₀={rec['ic']['a0']}, Ha₀={rec['ic']['Ha0']:.2f}, "
                 f"b₀={rec['ic']['b0']}, Hb₀={rec['ic']['Hb0']:.3f}",
                 fontsize=11)

    ax = axes[0, 0]
    ax.plot(sol.t, sol.y[0], label="a(t)")
    ax.plot(sol.t, sol.y[2], label="b(t)")
    ax.set_title("Scale factors vs time")
    ax.legend(); ax.set_xlabel("t")

    ax = axes[0, 1]
    ax.plot(sol.y[0], sol.y[1], lw=0.8)
    ax.axhline(0, ls=":", color="k", alpha=0.4)
    ax.set_xlabel("a"); ax.set_ylabel("H_a")
    ax.set_title("Phase portrait (a, H_a)")

    ax = axes[0, 2]
    ax.plot(sol.y[2], sol.y[3], lw=0.8)
    ax.axhline(0, ls=":", color="k", alpha=0.4)
    ax.set_xlabel("b"); ax.set_ylabel("H_b")
    ax.set_title("Phase portrait (b, H_b)")

    ax = axes[1, 0]
    ax.semilogy(sol.t, np.abs(C) + 1e-30, label="|constraint|")
    ax.semilogy(sol.t, np.abs(D) + 1e-30, label="|continuity|")
    ax.set_title("Consistency diagnostics")
    ax.legend(); ax.set_xlabel("t")

    ax = axes[1, 1]
    B2d, A2d = np.meshgrid(interp.b_arr, interp.a_arr)
    ax.contourf(A2d, B2d, interp.E_grid, levels=30, cmap="RdBu_r", alpha=0.6)
    ax.contour(A2d, B2d, interp.E_grid, levels=[0], colors="k", linewidths=1.5)
    ax.plot(sol.y[0], sol.y[2], "g-", lw=1.2, label="trajectory")
    ax.plot(sol.y[0, 0], sol.y[2, 0], "go", ms=6)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("Trajectory on E(a,b)")
    ax.legend()

    ax = axes[1, 2]
    w3_traj, wphi_traj = [], []
    for i in range(sol.y.shape[1]):
        rho_i, p3_i, pphi_i, _ = source_fn(sol.y[:, i], None)
        w3_traj.append(p3_i / rho_i if abs(rho_i) > 1e-30 else np.nan)
        wphi_traj.append(pphi_i / rho_i if abs(rho_i) > 1e-30 else np.nan)
    ax.plot(sol.t, w3_traj, label="w₃")
    ax.plot(sol.t, wphi_traj, label="w_φ")
    ax.axhline(0,    ls=":",  color="k", alpha=0.3)
    ax.axhline(-1/3, ls="--", color="g", alpha=0.5, label="w=−⅓")
    ax.axhline(-1,   ls="--", color="b", alpha=0.4, label="w=−1")
    ax.set_xlabel("t"); ax.set_title("Effective EOS along trajectory")
    ax.set_ylim(-3, 3); ax.legend(fontsize=8)

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, f"T3A_{label}_best.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"Saved: {fig_path}")

    # ── Plot oscillatory candidates if any ──
    osc_results = [r for r in ranked if r[0]["Ha_crossings"] >= 4]
    if osc_results:
        n_plot = min(4, len(osc_results))
        fig, axes = plt.subplots(n_plot, 2, figsize=(14, 4 * n_plot))
        if n_plot == 1:
            axes = axes[np.newaxis, :]
        for idx in range(n_plot):
            rec_i, sol_i, _, _ = osc_results[idx]
            axes[idx, 0].plot(sol_i.t, sol_i.y[0], label="a(t)")
            axes[idx, 0].plot(sol_i.t, sol_i.y[2], label="b(t)")
            axes[idx, 0].set_title(
                f"a₀={rec_i['ic']['a0']:.2f}  Ha₀={rec_i['ic']['Ha0']:.2f}  "
                f"b₀={rec_i['ic']['b0']:.2f}  |  "
                f"H_a×={rec_i['Ha_crossings']}  H_b×={rec_i['Hb_crossings']}")
            axes[idx, 0].legend()
            axes[idx, 1].plot(sol_i.y[0], sol_i.y[2], "b-", lw=0.7)
            axes[idx, 1].plot(sol_i.y[0, 0], sol_i.y[2, 0], "go", ms=5)
            axes[idx, 1].set_xlabel("a"); axes[idx, 1].set_ylabel("b")
            axes[idx, 1].set_title("(a, b) trajectory")
        plt.tight_layout()
        fig_path = os.path.join(OUTPUT_DIR, f"T3A_{label}_oscillatory.png")
        plt.savefig(fig_path, dpi=150)
        plt.close()
        print(f"Saved: {fig_path}")

    # ── JSON summary ──
    js_path = os.path.join(OUTPUT_DIR, f"T3A_{label}.json")
    with open(js_path, "w") as f:
        json.dump([r[0] for r in ranked], f, indent=2)
    print(f"Saved: {js_path}")

    return ranked


# ═══════════════════════════════════════════════════════════════════════
#  6.  Main
# ═══════════════════════════════════════════════════════════════════════

def build_init_grid():
    grid = []
    for a0 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
        for Ha0 in [0.05, 0.1, 0.3, 0.5, 1.0]:
            for b0 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
                grid.append((a0, Ha0, b0))
    return grid


if __name__ == "__main__":
    print("=" * 72)
    print("T3-A ANTIPERIODIC CASIMIR — S₁=0, S₂ with (−1)^k winding signs")
    print("Conformal coupling  c = 1/8  (ξ = 3/16 in 5D)")
    print("=" * 72)

    # ── Build interpolation grid ──
    interp = CasimirInterpolatorAP(
        a_range=(0.1, 8.0), b_range=(0.1, 8.0),
        Na=100, Nb=100, c=1/8,
    )

    # ── Bianchi check at sample point ──
    print("\nBianchi identity check at (a,b)=(1,1), Ha=0.5, Hb=0.3:")
    rho, p3, pphi, drho_dt = interp.source([1.0, 0.5, 1.0, 0.3], None)
    bianchi = drho_dt + 3 * 0.5 * (rho + p3) + 0.3 * (rho + pphi)
    print(f"  ρ={rho:.6e}  p₃={p3:.6e}  p_φ={pphi:.6e}")
    print(f"  Bianchi residual: {bianchi:.2e}  (should be ~machine ε)")

    # Direct vs interpolated comparison
    rho_d, p3_d, pphi_d, _ = casimir_source_ap_direct(1.0, 1.0, 0.5, 0.3, c=1/8)
    print(f"  Direct:  ρ={rho_d:.6e}  p₃={p3_d:.6e}  p_φ={pphi_d:.6e}")
    print(f"  Δρ/ρ = {abs(rho - rho_d) / max(abs(rho_d), 1e-30):.2e}")

    # ── Energy landscape + EOS diagnostics ──
    print("\nComputing EOS landscape …")
    w3_g, wphi_g, rho_g = plot_landscape_comparison(interp, label="antiperiodic")

    # ── Key diagnostic: compare w₃ distribution to conformal scalar ──
    w3_finite = w3_g[np.isfinite(w3_g) & (np.abs(rho_g) > 1e-30)]
    if len(w3_finite) > 0:
        print(f"\nDetailed w₃ statistics (antiperiodic scalar):")
        print(f"  mean(w₃) = {np.mean(w3_finite):.4f}")
        print(f"  median(w₃) = {np.median(w3_finite):.4f}")
        print(f"  min(w₃) = {np.min(w3_finite):.4f}")
        print(f"  max(w₃) = {np.max(w3_finite):.4f}")
        print(f"  % with w₃ < 0:    {100*np.mean(w3_finite < 0):.1f}%")
        print(f"  % with w₃ < -1/3: {100*np.mean(w3_finite < -1/3):.1f}%")
        print(f"  % with w₃ < -1:   {100*np.mean(w3_finite < -1.0):.1f}%")
        print(f"\nComparison (conformal scalar run had w₃ ≈ 0.5–1.5 everywhere)")

    # ── Periodic orbit search ──
    grid = build_init_grid()
    print(f"\nInitial condition grid: {len(grid)} points")
    run_ap_case(interp, grid, tmax=60.0, label="spectral_antiperiodic")

    print("\nDone.")
