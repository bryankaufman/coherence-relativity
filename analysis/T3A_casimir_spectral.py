#!/usr/bin/env python3
"""
T3-A Spectral Casimir Stress-Energy on S³(a) × S¹(b)
=====================================================

Renormalized Casimir stress-energy tensor T^(Cas)_MN(a, b) for a massless
scalar field on S³(a) × S¹(b), computed via ζ-function regularization
using the Chowla-Selberg decomposition.

Metric ansatz:
    ds² = −dt² + a(t)² dΩ₃² + b(t)² dφ²      (k = +1)

Spectral ζ-function ζ(s) = Σ_l l² Σ_m λ_{l,m}^{−s} decomposes as:
    ζ(s) = S₁(s)  +  S₂(s)
where:
    S₁(−½) = bD/(2a²)                          [analytically continued zero-mode]
    S₂(−½) = −(2/(πa)) ΣΣ l²√(l²+c) K₁(…)/k  [exponentially convergent KK sum]

Stress-energy from E(a,b) = ½ζ(−½):
    ρ   =  E / V₄
    p₃  = −(a/(3V₄)) ∂E/∂a
    p_φ = −(b/V₄)) ∂E/∂b

Bianchi identity ∇_M T^M_N = 0 satisfied by construction.

Full 5D Einstein equations:
    3H²_a + 3k/a² + 3H_aH_b = κρ              (constraint)
    Ḣ_a = −(2H²_a + k/a² + κp_φ/3)            (a-EOM)
    Ḣ_b = H²_a + k/a² − 2H_aH_b − H²_b + κ(2p_φ/3 − p₃)  (b-EOM)
    ȧ = aH_a,  ḃ = bH_b
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

# ─── Constants ────────────────────────────────────────────────────────
KAPPA5 = 1.0        # 5D gravitational coupling (units where κ₅ = 1)
K_CURV = 1.0        # S³ curvature k = +1
N_EFF  = 1.0        # effective number of scalar degrees of freedom

# Riemann ζ values
ZETA_R3 = 1.2020569031595942     # ζ(3)  (Apéry's constant)
ZETA_R5 = 1.0369277551433699     # ζ(5)

# ζ'_R at negative even integers:
#   ζ'(-2n) = (-1)^n (2n)! ζ(2n+1) / (2(2π)^{2n})
ZETA_PRIME_M2 = -ZETA_R3 / (4 * np.pi**2)        # ζ'(−2) ≈ −0.03045
ZETA_PRIME_M4 =  3 * ZETA_R5 / (4 * np.pi**4)    # ζ'(−4) ≈  0.00798

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ═══════════════════════════════════════════════════════════════════════
#  1. Casimir energy evaluator with analytical derivatives
# ═══════════════════════════════════════════════════════════════════════

def _D_constant(c):
    """Analytic continuation constant D(c) = 2ζ'_R(−4) + 2c ζ'_R(−2) + c²/4."""
    return 2 * ZETA_PRIME_M4 + 2 * c * ZETA_PRIME_M2 + c**2 / 4


def casimir_E_and_derivs(a, b, c=1/8, l_max=50, k_max=15):
    """
    Compute renormalized Casimir energy E(a,b) and its partial derivatives
    ∂E/∂a, ∂E/∂b analytically from the Chowla-Selberg formula.

    Parameters
    ----------
    a, b : float   (scale factors, > 0)
    c    : float   (curvature coupling: 1/8 conformal, −1 minimal)
    l_max, k_max : int  (sum truncations)

    Returns
    -------
    E, dE_da, dE_db : floats
    """
    D = _D_constant(c)
    r = b / a    # aspect ratio

    # ── S₁ contribution: S₁(−½) = bD/(2a²) ──
    #    E_S1 = ½ S₁ = bD/(4a²)
    E_S1     =  b * D / (4 * a**2)
    dE_S1_da = -b * D / (2 * a**3)       # ∂/∂a [bD/(4a²)] = −bD/(2a³)
    dE_S1_db =  D / (4 * a**2)           # ∂/∂b [bD/(4a²)] =  D/(4a²)

    # ── S₂ contribution: E_S2 = ½ S₂(−½) ──
    #    S₂(−½) = −(2/(πa)) Σ_l l²√(l²+c) Σ_k K₁(x_{lk})/k
    #    where x_{lk} = 2πk√(l²+c) × r
    #
    #    Derivatives use K'₁(x) = −½[K₀(x) + K₂(x)] and:
    #      ∂x/∂a = −x/a,  ∂x/∂b = x/b
    #
    #    ∂E_S2/∂a = (1/(πa²)) F  +  (−1/(πa)) ∂F/∂a
    #    ∂E_S2/∂b = (−1/(πa)) ∂F/∂b
    #    where F = Σ l²√(l²+c) Σ K₁(x)/k
    #    ∂F/∂a = Σ l²√(l²+c) Σ K'₁(x)(−x/a)/k
    #           = Σ l²√(l²+c) Σ x/(2a) [K₀(x)+K₂(x)] / k
    #    ∂F/∂b = Σ l²√(l²+c) Σ K'₁(x)(x/b)/k
    #           = Σ l²√(l²+c) Σ (−x/(2b)) [K₀(x)+K₂(x)] / k

    F       = 0.0
    dF_da   = 0.0
    dF_db   = 0.0

    for l in range(1, l_max + 1):
        l2c = l * l + c
        if l2c <= 0:
            continue
        sqrt_l2c = np.sqrt(l2c)
        prefac = l * l * sqrt_l2c     # l² √(l²+c)

        for k in range(1, k_max + 1):
            x = 2 * np.pi * k * sqrt_l2c * r
            if x > 500:
                break   # K₁ negligible

            K1 = bessel_kv(1, x)
            K0 = bessel_kv(0, x)
            K2 = bessel_kv(2, x)

            F     += prefac * K1 / k
            dF_da += prefac * (x / (2 * a)) * (K0 + K2) / k
            dF_db += prefac * (-x / (2 * b)) * (K0 + K2) / k

        # early l-termination: if smallest x exceeds threshold
        x_min = 2 * np.pi * sqrt_l2c * r   # k=1 term
        if x_min > 100:
            break

    E_S2     = (-1.0 / (np.pi * a)) * F
    dE_S2_da = (1.0 / (np.pi * a**2)) * F + (-1.0 / (np.pi * a)) * dF_da
    dE_S2_db = (-1.0 / (np.pi * a)) * dF_db

    # ── Total (with N_eff multiplier) ──
    E      = N_EFF * (E_S1     + E_S2)
    dE_da  = N_EFF * (dE_S1_da + dE_S2_da)
    dE_db  = N_EFF * (dE_S1_db + dE_S2_db)

    return E, dE_da, dE_db


def casimir_source_direct(a, b, Ha, Hb, c=1/8):
    """
    Compute (ρ, p₃, p_φ, dρ/dt) from the spectral Casimir energy.
    Slow (direct evaluation) — use for validation or single-point checks.
    """
    V4 = 4 * np.pi**3 * a**3 * b
    E, dE_da, dE_db = casimir_E_and_derivs(a, b, c)

    rho  =  E / V4
    p3   = -(a / (3 * V4)) * dE_da
    pphi = -(b / V4) * dE_db

    # chain rule: dρ/dt = (∂ρ/∂a)ȧ + (∂ρ/∂b)ḃ
    drho_dt = (dE_da / V4 - 3 * rho / a) * a * Ha \
            + (dE_db / V4 - rho / b) * b * Hb

    return rho, p3, pphi, drho_dt


# ═══════════════════════════════════════════════════════════════════════
#  2. Interpolation layer for fast ODE evaluation
# ═══════════════════════════════════════════════════════════════════════

class CasimirInterpolator:
    """
    Precomputes E(a,b), ∂E/∂a, ∂E/∂b on a 2D grid and builds bicubic
    spline interpolators for fast evaluation during ODE integration.
    """

    def __init__(self, a_range=(0.1, 8.0), b_range=(0.1, 8.0),
                 Na=100, Nb=100, c=1/8):
        self.c = c
        self.a_lo, self.a_hi = a_range
        self.b_lo, self.b_hi = b_range
        self.a_arr = np.linspace(self.a_lo, self.a_hi, Na)
        self.b_arr = np.linspace(self.b_lo, self.b_hi, Nb)

        print(f"Building Casimir grid ({Na}×{Nb}), c={c:.4f} ...")
        E_grid    = np.zeros((Na, Nb))
        dEda_grid = np.zeros((Na, Nb))
        dEdb_grid = np.zeros((Na, Nb))

        for i, av in enumerate(self.a_arr):
            for j, bv in enumerate(self.b_arr):
                E_grid[i, j], dEda_grid[i, j], dEdb_grid[i, j] = \
                    casimir_E_and_derivs(av, bv, c)

        self.spl_E    = RectBivariateSpline(self.a_arr, self.b_arr, E_grid)
        self.spl_dEda = RectBivariateSpline(self.a_arr, self.b_arr, dEda_grid)
        self.spl_dEdb = RectBivariateSpline(self.a_arr, self.b_arr, dEdb_grid)
        self.E_grid = E_grid
        print("  Grid complete.")

    def _clamp(self, a, b):
        a = np.clip(a, self.a_lo, self.a_hi)
        b = np.clip(b, self.b_lo, self.b_hi)
        return a, b

    def eval(self, a, b):
        """Return E, dE/da, dE/db at (a, b) via interpolation."""
        a, b = self._clamp(a, b)
        E    = float(self.spl_E(a, b, grid=False))
        dEda = float(self.spl_dEda(a, b, grid=False))
        dEdb = float(self.spl_dEdb(a, b, grid=False))
        return E, dEda, dEdb

    def source(self, state, params=None):
        """
        ODE-compatible source function.
        Returns (ρ, p₃, p_φ, dρ/dt).
        """
        a, Ha, b, Hb = state
        a_c, b_c = self._clamp(a, b)

        V4 = 4 * np.pi**3 * a_c**3 * b_c
        E, dEda, dEdb = self.eval(a_c, b_c)

        rho  =  E / V4
        p3   = -(a_c / (3 * V4)) * dEda
        pphi = -(b_c / V4) * dEdb

        drho_dt = (dEda / V4 - 3 * rho / a_c) * a_c * Ha \
                + (dEdb / V4 - rho / b_c) * b_c * Hb

        return rho, p3, pphi, drho_dt


# ═══════════════════════════════════════════════════════════════════════
#  3. Energy landscape visualization
# ═══════════════════════════════════════════════════════════════════════

def plot_energy_landscape(interp):
    """Contour plots of E, ρ, w₃, w_φ over (a, b) space."""
    a_arr = interp.a_arr
    b_arr = interp.b_arr
    Na, Nb = len(a_arr), len(b_arr)

    E_grid    = np.zeros((Na, Nb))
    rho_grid  = np.zeros((Na, Nb))
    w3_grid   = np.full((Na, Nb), np.nan)
    wphi_grid = np.full((Na, Nb), np.nan)

    for i, av in enumerate(a_arr):
        for j, bv in enumerate(b_arr):
            E, dEda, dEdb = interp.eval(av, bv)
            V4 = 4 * np.pi**3 * av**3 * bv
            rho  =  E / V4
            p3   = -(av / (3 * V4)) * dEda
            pphi = -(bv / V4) * dEdb

            E_grid[i, j]   = E
            rho_grid[i, j] = rho
            if abs(rho) > 1e-30:
                w3_grid[i, j]   = p3 / rho
                wphi_grid[i, j] = pphi / rho

    B, A = np.meshgrid(b_arr, a_arr)

    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # E(a,b)
    ax = axes[0, 0]
    cp = ax.contourf(A, B, E_grid, levels=40, cmap="RdBu_r")
    ax.contour(A, B, E_grid, levels=[0], colors="k", linewidths=2)
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("E_Cas(a,b)  [zero contour in black]")

    # ρ(a,b)
    ax = axes[0, 1]
    # symmetric log scale for ρ
    rho_max = np.nanmax(np.abs(rho_grid))
    cp = ax.contourf(A, B, rho_grid, levels=40, cmap="RdBu_r")
    ax.contour(A, B, rho_grid, levels=[0], colors="k", linewidths=2)
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("ρ(a,b)  [zero contour in black]")

    # w₃(a,b)
    ax = axes[1, 0]
    w3_clip = np.clip(w3_grid, -3, 3)
    cp = ax.contourf(A, B, w3_clip, levels=40, cmap="coolwarm")
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("w₃ = p₃/ρ  [clipped to ±3]")

    # w_φ(a,b)
    ax = axes[1, 1]
    wphi_clip = np.clip(wphi_grid, -3, 3)
    cp = ax.contourf(A, B, wphi_clip, levels=40, cmap="coolwarm")
    fig.colorbar(cp, ax=ax)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("w_φ = p_φ/ρ  [clipped to ±3]")

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, "T3A_casimir_landscape.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"Saved: {fig_path}")
    return E_grid


# ═══════════════════════════════════════════════════════════════════════
#  4. Full 5D Einstein ODE system
# ═══════════════════════════════════════════════════════════════════════

def rhs_full_5d(t, state, source_fn, source_params):
    """
    dy/dt for the full 5D system.
    state = [a, Ha, b, Hb]
    """
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


def constraint_residual(state, source_fn, source_params):
    a, Ha, b, Hb = state
    rho, _, _, _ = source_fn(state, source_params)
    return 3.0 * Ha**2 + 3.0 * K_CURV / a**2 + 3.0 * Ha * Hb - KAPPA5 * rho


def continuity_residual(state, source_fn, source_params):
    a, Ha, b, Hb = state
    rho, p3, pphi, drho_dt = source_fn(state, source_params)
    return drho_dt + 3.0 * Ha * (rho + p3) + Hb * (rho + pphi)


def init_from_constraint(a0, Ha0, b0, source_fn, source_params):
    """Solve constraint 3H²_a + 3k/a² + 3H_aH_b = κρ for H_b."""
    if abs(Ha0) < 1e-14:
        return None
    probe = np.array([a0, Ha0, b0, 0.0])
    rho, _, _, _ = source_fn(probe, source_params)
    Hb0 = (KAPPA5 * rho - 3.0 * Ha0**2 - 3.0 * K_CURV / a0**2) / (3.0 * Ha0)
    return np.array([a0, Ha0, b0, Hb0], dtype=float)


# ═══════════════════════════════════════════════════════════════════════
#  5. Integration + periodic orbit search
# ═══════════════════════════════════════════════════════════════════════

def run_spectral_case(interp, init_grid, tmax=60.0, label="spectral_conformal"):
    """
    Integrate the full 5D Einstein system with spectral Casimir source.
    Scan initial conditions and look for oscillatory solutions.
    """
    source_fn = interp.source
    a_lo, a_hi = interp.a_lo, interp.a_hi
    b_lo, b_hi = interp.b_lo, interp.b_hi

    print(f"\n{'='*72}")
    print(f"CASE: {label}")
    print(f"{'='*72}")

    results = []

    for (a0, Ha0, b0) in init_grid:
        state0 = init_from_constraint(a0, Ha0, b0, source_fn, None)
        if state0 is None or not np.isfinite(state0).all():
            continue
        if abs(state0[3]) > 50:
            continue

        # terminal events
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

        C = np.array([constraint_residual(sol.y[:, i], source_fn, None)
                       for i in range(sol.y.shape[1])])
        D = np.array([continuity_residual(sol.y[:, i], source_fn, None)
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

    # ── Summary ──
    total = len(results)
    surv  = sum(r[0]["survived_full_window"] for r in results)
    osc   = sum(r[0]["Ha_crossings"] >= 4 for r in results)
    print(f"Trajectories integrated: {total}")
    print(f"Survived full window:    {surv}")
    print(f"Oscillatory candidates:  {osc}")
    print(
        "Constraint |C| range:",
        f"[{min(r[0]['max_abs_constraint'] for r in results):.2e},",
        f"{max(r[0]['max_abs_constraint'] for r in results):.2e}]",
    )
    print(
        "Continuity |D| range:",
        f"[{min(r[0]['max_abs_continuity'] for r in results):.2e},",
        f"{max(r[0]['max_abs_continuity'] for r in results):.2e}]",
    )

    # ── Rank by oscillatory quality, then constraint ──
    ranked = sorted(results,
                    key=lambda x: (-x[0]["Ha_crossings"] - x[0]["Hb_crossings"],
                                    x[0]["max_abs_constraint"]))
    best = ranked[0]
    rec, sol, C, D = best
    print(f"\nBest trajectory IC: {rec['ic']}")
    print(f"  crossings (Ha, Hb): {rec['Ha_crossings']}, {rec['Hb_crossings']}")
    print(f"  max |C|: {rec['max_abs_constraint']:.2e}")
    print(f"  max |D|: {rec['max_abs_continuity']:.2e}")
    print(f"  survived: {rec['survived_full_window']}")

    # ── Plot best trajectory ──
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    ax = axes[0, 0]
    ax.plot(sol.t, sol.y[0], label="a(t)")
    ax.plot(sol.t, sol.y[2], label="b(t)")
    ax.set_title(f"{label}: scale factors")
    ax.legend()
    ax.set_xlabel("t")

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
    ax.legend()
    ax.set_xlabel("t")

    # 2D trajectory over energy landscape
    ax = axes[1, 1]
    B, A = np.meshgrid(interp.b_arr, interp.a_arr)
    ax.contourf(A, B, interp.E_grid, levels=30, cmap="RdBu_r", alpha=0.6)
    ax.contour(A, B, interp.E_grid, levels=[0], colors="k", linewidths=1.5)
    ax.plot(sol.y[0], sol.y[2], "g-", lw=1.2, label="trajectory")
    ax.plot(sol.y[0, 0], sol.y[2, 0], "go", ms=6)
    ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("Trajectory on E(a,b) landscape")
    ax.legend()

    # effective EOS along trajectory
    ax = axes[1, 2]
    w3_traj = []
    wphi_traj = []
    for i in range(sol.y.shape[1]):
        st = sol.y[:, i]
        rho, p3, pphi, _ = source_fn(st, None)
        w3_traj.append(p3 / rho if abs(rho) > 1e-30 else np.nan)
        wphi_traj.append(pphi / rho if abs(rho) > 1e-30 else np.nan)
    ax.plot(sol.t, w3_traj, label="w₃")
    ax.plot(sol.t, wphi_traj, label="w_φ")
    ax.axhline(-1, ls=":", color="k", alpha=0.3)
    ax.set_xlabel("t")
    ax.set_title("Effective EOS along trajectory")
    ax.set_ylim(-3, 3)
    ax.legend()

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, f"T3A_{label}_best.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"Saved: {fig_path}")

    # ── Plot top oscillatory candidates (if any) ──
    osc_results = [r for r in ranked if r[0]["Ha_crossings"] >= 4]
    if osc_results:
        n_plot = min(4, len(osc_results))
        fig, axes = plt.subplots(n_plot, 2, figsize=(14, 4 * n_plot))
        if n_plot == 1:
            axes = axes[np.newaxis, :]
        for idx in range(n_plot):
            rec_i, sol_i, C_i, D_i = osc_results[idx]
            axes[idx, 0].plot(sol_i.t, sol_i.y[0], label="a(t)")
            axes[idx, 0].plot(sol_i.t, sol_i.y[2], label="b(t)")
            axes[idx, 0].set_title(
                f"IC a₀={rec_i['ic']['a0']:.2f} Ha₀={rec_i['ic']['Ha0']:.2f} "
                f"b₀={rec_i['ic']['b0']:.2f}  |  Ha×={rec_i['Ha_crossings']} Hb×={rec_i['Hb_crossings']}")
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

    # ── Save JSON summary ──
    js = [r[0] for r in ranked]
    js_path = os.path.join(OUTPUT_DIR, f"T3A_{label}.json")
    with open(js_path, "w") as f:
        json.dump(js, f, indent=2)
    print(f"Saved: {js_path}")

    return ranked


# ═══════════════════════════════════════════════════════════════════════
#  6. Main
# ═══════════════════════════════════════════════════════════════════════

def build_init_grid():
    """Grid of (a₀, Ha₀, b₀) initial conditions."""
    grid = []
    for a0 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
        for Ha0 in [0.05, 0.1, 0.3, 0.5, 1.0]:
            for b0 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
                grid.append((a0, Ha0, b0))
    return grid


if __name__ == "__main__":
    print("=" * 72)
    print("T3-A SPECTRAL CASIMIR COMPUTATION")
    print("Conformal coupling  c = 1/8  (ξ = 3/16 in 5D)")
    print("=" * 72)

    # ── Build interpolation grid ──
    interp = CasimirInterpolator(
        a_range=(0.1, 8.0), b_range=(0.1, 8.0),
        Na=100, Nb=100, c=1/8,
    )

    # ── Energy landscape ──
    print("\nPlotting energy landscape ...")
    plot_energy_landscape(interp)

    # ── Validation: check Bianchi at a sample point ──
    print("\nBianchi identity check at (a,b)=(1,1), Ha=0.5, Hb=0.3:")
    rho, p3, pphi, drho_dt = interp.source([1.0, 0.5, 1.0, 0.3], None)
    bianchi = drho_dt + 3 * 0.5 * (rho + p3) + 0.3 * (rho + pphi)
    print(f"  ρ={rho:.6e}  p₃={p3:.6e}  p_φ={pphi:.6e}")
    print(f"  Bianchi residual: {bianchi:.2e}")

    # ── Direct vs interpolated comparison ──
    rho_d, p3_d, pphi_d, _ = casimir_source_direct(1.0, 1.0, 0.5, 0.3, c=1/8)
    print(f"  Direct:  ρ={rho_d:.6e}  p₃={p3_d:.6e}  p_φ={pphi_d:.6e}")
    print(f"  Interp:  ρ={rho:.6e}  p₃={p3:.6e}  p_φ={pphi:.6e}")
    print(f"  Δρ/ρ = {abs(rho - rho_d) / abs(rho_d):.2e}")

    # ── Periodic orbit search ──
    grid = build_init_grid()
    print(f"\nInitial condition grid: {len(grid)} points")

    run_spectral_case(interp, grid, tmax=60.0, label="spectral_conformal")

    print("\nDone.")
