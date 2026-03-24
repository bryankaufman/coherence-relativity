#!/usr/bin/env python3
"""
T3-A Multi-Spin Casimir Stress-Energy on S³(a) × S¹(b)
=======================================================

Computes the renormalized Casimir stress-energy tensor summing over:
  spin-0:   conformal scalar (c=1/8)
  spin-1:   co-exact vector on S³ (physical gauge DOF)
  spin-2:   TT tensor on S³ (physical graviton DOF)
  spin-1/2: Dirac fermion (antiperiodic BC on S¹)

Uses ζ-function regularization with Chowla-Selberg decomposition.
S₁ (zero-mode): computed where Z(-½)=0 (scalar, co-exact vector).
S₂ (Bessel KK): computed for ALL sectors (always finite).

Spectral data on unit S³:
  Scalar:    Λ = l²+c,        deg = l²,            l≥1
  Co-exact:  Λ = L²,          deg = 2(L-1)(L+1),   L≥2
  TT tensor: Λ = L(L+2)-2,    deg = 2(L+3)(L-1),   L≥2
  Dirac:     Λ = (n+3/2)²,    deg = 2(n+1)(n+2),   n≥0

Status of S₁ analytic continuation:
  Scalar:    Z(-½)=0  → D = 2ζ'(-4)+2cζ'(-2)+c²/4     [VERIFIED]
  Co-exact:  Z(-½)=0  → D = 4[ζ'(-4)-ζ'(-2)]          [VERIFIED]
  TT tensor: Z(-½)=-64/15 ≠ 0  → pole, needs ghost subtraction [TODO-CAS-001]
  Dirac:     Z(-½)=-1/120 ≠ 0  → pole, needs counterterm       [TODO-CAS-002]

Full 5D Einstein equations:
  3H²_a + 3k/a² + 3H_aH_b = κρ              (constraint)
  Ḣ_a = −(2H²_a + k/a² + κp_φ/3)            (a-EOM)
  Ḣ_b = H²_a + k/a² − 2H_aH_b − H²_b + κ(2p_φ/3 − p₃)  (b-EOM)
"""

import os
import json
import time
import numpy as np
from scipy.special import kv as bessel_kv
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ─── Physical constants ───────────────────────────────────────────────
KAPPA5 = 1.0
K_CURV = 1.0

# Riemann ζ values
ZETA_R3 = 1.2020569031595942      # ζ(3)
ZETA_R5 = 1.0369277551433699      # ζ(5)
ZETA_PRIME_M2 = -ZETA_R3 / (4 * np.pi**2)       # ζ'(−2) ≈ −0.03045
ZETA_PRIME_M4 = 3 * ZETA_R5 / (4 * np.pi**4)    # ζ'(−4) ≈  0.00798

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── S₁ constants D for sectors with Z(−½) = 0 ──────────────────────
C_CONF = 1.0 / 8.0
D_SCALAR = 2*ZETA_PRIME_M4 + 2*C_CONF*ZETA_PRIME_M2 + C_CONF**2 / 4
D_COEXACT = 4 * (ZETA_PRIME_M4 - ZETA_PRIME_M2)


# ═══════════════════════════════════════════════════════════════════════
#  1. Spectral sector definitions
# ═══════════════════════════════════════════════════════════════════════

SPECTRAL_SECTORS = {
    "scalar_conf": {
        "label": "Scalar (conf, c=1/8)",
        "eigenvalue": lambda l: l*l + C_CONF,
        "degeneracy": lambda l: l*l,
        "L_min": 1,
        "is_fermion": False,
        "antiperiodic": False,
        "D_s1": D_SCALAR,
    },
    "coexact_vector": {
        "label": "Co-exact vector",
        "eigenvalue": lambda L: float(L*L),
        "degeneracy": lambda L: 2*(L - 1)*(L + 1),
        "L_min": 2,
        "is_fermion": False,
        "antiperiodic": False,
        "D_s1": D_COEXACT,
    },
    "TT_tensor": {
        "label": "TT tensor (graviton)",
        "eigenvalue": lambda L: float(L*(L + 2) - 2),
        "degeneracy": lambda L: 2*(L + 3)*(L - 1),
        "L_min": 2,
        "is_fermion": False,
        "antiperiodic": False,
        "D_s1": None,   # TODO-CAS-001
    },
    "dirac": {
        "label": "Dirac (AP BC)",
        "eigenvalue": lambda n: (n + 1.5)**2,
        "degeneracy": lambda n: 2*(n + 1)*(n + 2),
        "L_min": 0,
        "is_fermion": True,
        "antiperiodic": True,
        "D_s1": None,   # TODO-CAS-002
    },
}

# Pre-defined field content configurations
CONFIGS = {
    "scalar_only": [("scalar_conf", 1)],
    "graviton_only": [("TT_tensor", 1)],
    "scalar_graviton": [("scalar_conf", 1), ("TT_tensor", 1)],
    "bosonic_mix": [
        ("scalar_conf", 4),
        ("coexact_vector", 12),
        ("TT_tensor", 1),
    ],
    "full_SM": [
        ("scalar_conf", 4),       # Higgs doublet
        ("coexact_vector", 12),   # SU(3)×SU(2)×U(1)
        ("TT_tensor", 1),        # graviton
        ("dirac", 24),           # SM fermions (≈24 Dirac in 5D)
    ],
}


# ═══════════════════════════════════════════════════════════════════════
#  2. Casimir energy evaluator
# ═══════════════════════════════════════════════════════════════════════

def _sector_energy(a, b, sector, l_max=50, k_max=15):
    """
    Compute ½ζ(−½) and its a, b derivatives for ONE spectral sector.
    Returns (E, dE/da, dE/db) for a SINGLE field of this type.
    Sign (boson/fermion) is NOT applied — caller handles that.
    """
    eig_fn = sector["eigenvalue"]
    deg_fn = sector["degeneracy"]
    L_min = sector["L_min"]
    ap = sector["antiperiodic"]
    D = sector["D_s1"]
    r = b / a

    # ── S₁ ──
    if D is not None and abs(D) > 1e-30:
        E_S1     =  b * D / (4.0 * a**2)
        dS1_da   = -b * D / (2.0 * a**3)
        dS1_db   =  D / (4.0 * a**2)
    else:
        E_S1 = dS1_da = dS1_db = 0.0

    # ── S₂ (Bessel sum) ──
    F = 0.0
    dF_da = 0.0
    dF_db = 0.0

    for L in range(L_min, L_min + l_max):
        lam = eig_fn(L)
        if lam <= 0.0:
            continue
        sq = np.sqrt(lam)
        d = deg_fn(L)
        pre = d * sq                           # d_L × √Λ_L

        for k in range(1, k_max + 1):
            x = 2.0 * np.pi * k * sq * r
            if x > 500.0:
                break
            sk = (-1.0)**k if ap else 1.0

            K1 = bessel_kv(1, x)
            K0 = bessel_kv(0, x)
            K2 = bessel_kv(2, x)

            F     += pre * sk * K1 / k
            dF_da += pre * sk * (x / (2.0 * a)) * (K0 + K2) / k
            dF_db += pre * sk * (-x / (2.0 * b)) * (K0 + K2) / k

        if 2.0 * np.pi * sq * r > 100.0:
            break

    E_S2   = (-1.0 / (np.pi * a)) * F
    dS2_da = (1.0 / (np.pi * a**2)) * F + (-1.0 / (np.pi * a)) * dF_da
    dS2_db = (-1.0 / (np.pi * a)) * dF_db

    return (E_S1 + E_S2, dS1_da + dS2_da, dS1_db + dS2_db)


def casimir_multispin(a, b, field_content, l_max=50, k_max=15):
    """
    Total Casimir E(a,b), ∂E/∂a, ∂E/∂b for multi-spin field content.

    Parameters
    ----------
    field_content : list of (sector_key, multiplicity) tuples
    """
    Et = dEa = dEb = 0.0
    for key, mult in field_content:
        sec = SPECTRAL_SECTORS[key]
        E, da, db = _sector_energy(a, b, sec, l_max, k_max)
        sign = -1.0 if sec["is_fermion"] else 1.0
        Et  += sign * mult * E
        dEa += sign * mult * da
        dEb += sign * mult * db
    return Et, dEa, dEb


# ═══════════════════════════════════════════════════════════════════════
#  3. Interpolation layer
# ═══════════════════════════════════════════════════════════════════════

class MultispinInterpolator:
    """Precompute E(a,b) grid for fast ODE evaluation."""

    def __init__(self, field_content, a_range=(0.1, 8.0), b_range=(0.1, 8.0),
                 Na=80, Nb=80, l_max=50, k_max=15):
        self.field_content = field_content
        self.a_lo, self.a_hi = a_range
        self.b_lo, self.b_hi = b_range
        self.a_arr = np.linspace(self.a_lo, self.a_hi, Na)
        self.b_arr = np.linspace(self.b_lo, self.b_hi, Nb)

        label = "+".join(f"{m}×{k}" for k, m in field_content)
        print(f"Building Casimir grid ({Na}×{Nb}) for [{label}] ...")
        t0 = time.time()

        E_grid    = np.zeros((Na, Nb))
        dEda_grid = np.zeros((Na, Nb))
        dEdb_grid = np.zeros((Na, Nb))

        for i, av in enumerate(self.a_arr):
            for j, bv in enumerate(self.b_arr):
                E_grid[i, j], dEda_grid[i, j], dEdb_grid[i, j] = \
                    casimir_multispin(av, bv, field_content, l_max, k_max)

        self.spl_E    = RectBivariateSpline(self.a_arr, self.b_arr, E_grid)
        self.spl_dEda = RectBivariateSpline(self.a_arr, self.b_arr, dEda_grid)
        self.spl_dEdb = RectBivariateSpline(self.a_arr, self.b_arr, dEdb_grid)
        self.E_grid = E_grid

        dt = time.time() - t0
        print(f"  Grid complete in {dt:.1f}s.")

    def _clamp(self, a, b):
        return np.clip(a, self.a_lo, self.a_hi), np.clip(b, self.b_lo, self.b_hi)

    def eval(self, a, b):
        a, b = self._clamp(a, b)
        return (float(self.spl_E(a, b, grid=False)),
                float(self.spl_dEda(a, b, grid=False)),
                float(self.spl_dEdb(a, b, grid=False)))

    def source(self, state, _params=None):
        """ODE-compatible: returns (ρ, p₃, p_φ, dρ/dt)."""
        a, Ha, b, Hb = state
        ac, bc = self._clamp(a, b)
        V4 = 4.0 * np.pi**3 * ac**3 * bc
        E, dEda, dEdb = self.eval(ac, bc)

        rho  =  E / V4
        p3   = -(ac / (3.0 * V4)) * dEda
        pphi = -(bc / V4) * dEdb

        drho_dt = ((dEda / V4 - 3.0 * rho / ac) * ac * Ha
                 + (dEdb / V4 - rho / bc) * bc * Hb)
        return rho, p3, pphi, drho_dt


# ═══════════════════════════════════════════════════════════════════════
#  4. Full 5D Einstein ODE
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


def constraint_residual(state, source_fn, source_params):
    a, Ha, b, Hb = state
    rho, _, _, _ = source_fn(state, source_params)
    return 3.0*Ha**2 + 3.0*K_CURV/a**2 + 3.0*Ha*Hb - KAPPA5*rho


def continuity_residual(state, source_fn, source_params):
    a, Ha, b, Hb = state
    rho, p3, pphi, drho_dt = source_fn(state, source_params)
    return drho_dt + 3.0*Ha*(rho + p3) + Hb*(rho + pphi)


def init_from_constraint(a0, Ha0, b0, source_fn, source_params):
    if abs(Ha0) < 1e-14:
        return None
    probe = np.array([a0, Ha0, b0, 0.0])
    rho, _, _, _ = source_fn(probe, source_params)
    Hb0 = (KAPPA5*rho - 3.0*Ha0**2 - 3.0*K_CURV/a0**2) / (3.0*Ha0)
    return np.array([a0, Ha0, b0, Hb0], dtype=float)


# ═══════════════════════════════════════════════════════════════════════
#  5. EOS landscape diagnostics
# ═══════════════════════════════════════════════════════════════════════

def plot_eos_landscape(interp, config_name):
    """Contour plots of E, ρ, w₃, w_φ for a given field content."""
    a_arr, b_arr = interp.a_arr, interp.b_arr
    Na, Nb = len(a_arr), len(b_arr)

    E_g    = np.zeros((Na, Nb))
    rho_g  = np.zeros((Na, Nb))
    w3_g   = np.full((Na, Nb), np.nan)
    wp_g   = np.full((Na, Nb), np.nan)

    for i, av in enumerate(a_arr):
        for j, bv in enumerate(b_arr):
            E, dEda, dEdb = interp.eval(av, bv)
            V4 = 4.0 * np.pi**3 * av**3 * bv
            rho = E / V4
            p3  = -(av / (3.0 * V4)) * dEda
            pphi = -(bv / V4) * dEdb
            E_g[i, j] = E
            rho_g[i, j] = rho
            if abs(rho) > 1e-30:
                w3_g[i, j] = p3 / rho
                wp_g[i, j] = pphi / rho

    B, A = np.meshgrid(b_arr, a_arr)
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle(f"Casimir EOS Landscape: {config_name}", fontsize=14, y=1.01)

    ax = axes[0, 0]
    cp = ax.contourf(A, B, E_g, levels=40, cmap="RdBu_r")
    ax.contour(A, B, E_g, levels=[0], colors="k", linewidths=2)
    fig.colorbar(cp, ax=ax); ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("E_Cas(a,b)  [zero contour black]")

    ax = axes[0, 1]
    cp = ax.contourf(A, B, rho_g, levels=40, cmap="RdBu_r")
    ax.contour(A, B, rho_g, levels=[0], colors="k", linewidths=2)
    fig.colorbar(cp, ax=ax); ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("ρ(a,b)  [zero contour black]")

    ax = axes[1, 0]
    w3c = np.clip(w3_g, -3, 3)
    cp = ax.contourf(A, B, w3c, levels=40, cmap="coolwarm")
    # Mark w₃ = -1/3 contour (static equilibrium requirement)
    try:
        ax.contour(A, B, w3_g, levels=[-1/3], colors="lime", linewidths=2,
                   linestyles="--")
    except Exception:
        pass
    fig.colorbar(cp, ax=ax); ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("w₃ = p₃/ρ  [green dashed: w₃=-1/3]")

    ax = axes[1, 1]
    wpc = np.clip(wp_g, -3, 3)
    cp = ax.contourf(A, B, wpc, levels=40, cmap="coolwarm")
    fig.colorbar(cp, ax=ax); ax.set_xlabel("a"); ax.set_ylabel("b")
    ax.set_title("w_φ = p_φ/ρ")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, f"T3A_multispin_{config_name}_landscape.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")

    # ── Report EOS statistics in ρ>0 region ──
    pos = rho_g > 0
    if np.any(pos):
        w3_pos = w3_g[pos]
        w3_pos = w3_pos[np.isfinite(w3_pos)]
        neg_w3 = np.sum(w3_pos < 0)
        neg_w3_third = np.sum(w3_pos < -1/3)
        print(f"  ρ>0 region: {np.sum(pos)} points, "
              f"w₃<0: {neg_w3}, w₃<-1/3: {neg_w3_third}")
        if len(w3_pos) > 0:
            print(f"  w₃ range in ρ>0: [{np.min(w3_pos):.3f}, {np.max(w3_pos):.3f}]")
    else:
        print("  ρ>0 region: empty (all negative energy)")


# ═══════════════════════════════════════════════════════════════════════
#  6. Orbit search
# ═══════════════════════════════════════════════════════════════════════

def build_init_grid():
    grid = []
    for a0 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
        for Ha0 in [0.05, 0.1, 0.3, 0.5, 1.0]:
            for b0 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
                grid.append((a0, Ha0, b0))
    return grid


def run_orbit_search(interp, config_name, init_grid=None, tmax=60.0):
    """Integrate 5D Einstein + Casimir and search for oscillatory orbits."""
    src = interp.source
    alo, ahi = interp.a_lo, interp.a_hi
    blo, bhi = interp.b_lo, interp.b_hi

    if init_grid is None:
        init_grid = build_init_grid()

    print(f"\n{'='*72}")
    print(f"ORBIT SEARCH: {config_name}  ({len(init_grid)} ICs)")
    print(f"{'='*72}")

    results = []
    for (a0, Ha0, b0) in init_grid:
        state0 = init_from_constraint(a0, Ha0, b0, src, None)
        if state0 is None or not np.isfinite(state0).all():
            continue
        if abs(state0[3]) > 50:
            continue

        def ev_alo(t, y, *a): return y[0] - alo*1.05
        ev_alo.terminal = True; ev_alo.direction = -1
        def ev_blo(t, y, *a): return y[2] - blo*1.05
        ev_blo.terminal = True; ev_blo.direction = -1
        def ev_ahi(t, y, *a): return ahi*0.95 - y[0]
        ev_ahi.terminal = True; ev_ahi.direction = -1
        def ev_bhi(t, y, *a): return bhi*0.95 - y[2]
        ev_bhi.terminal = True; ev_bhi.direction = -1
        def ev_blow(t, y, *a): return 1e6 - (abs(y[1]) + abs(y[3]))
        ev_blow.terminal = True

        try:
            sol = solve_ivp(
                rhs_full_5d, [0.0, tmax], state0,
                args=(src, None), method="Radau",
                max_step=0.05, rtol=1e-9, atol=1e-11,
                events=[ev_alo, ev_blo, ev_ahi, ev_bhi, ev_blow],
            )
        except Exception:
            continue
        if len(sol.t) < 20:
            continue

        C = np.array([constraint_residual(sol.y[:, i], src, None)
                       for i in range(sol.y.shape[1])])
        D_res = np.array([continuity_residual(sol.y[:, i], src, None)
                           for i in range(sol.y.shape[1])])
        Ha_x = int(np.sum(np.diff(np.sign(sol.y[1])) != 0))
        Hb_x = int(np.sum(np.diff(np.sign(sol.y[3])) != 0))

        rec = {
            "ic": {"a0": a0, "Ha0": Ha0, "b0": b0, "Hb0": float(state0[3])},
            "t_end": float(sol.t[-1]),
            "a_range": [float(np.min(sol.y[0])), float(np.max(sol.y[0]))],
            "b_range": [float(np.min(sol.y[2])), float(np.max(sol.y[2]))],
            "Ha_crossings": Ha_x,
            "Hb_crossings": Hb_x,
            "max_C": float(np.max(np.abs(C))),
            "max_D": float(np.max(np.abs(D_res))),
            "survived": bool(sol.t[-1] >= 0.98*tmax),
        }
        results.append((rec, sol, C, D_res))

    if not results:
        print("  No successful trajectories.")
        return []

    total = len(results)
    surv = sum(r[0]["survived"] for r in results)
    osc  = sum(r[0]["Ha_crossings"] >= 4 for r in results)
    print(f"  Integrated: {total},  Survived: {surv},  Oscillatory (≥4 crossings): {osc}")
    print(f"  |C| range: [{min(r[0]['max_C'] for r in results):.2e}, "
          f"{max(r[0]['max_C'] for r in results):.2e}]")
    print(f"  |D| range: [{min(r[0]['max_D'] for r in results):.2e}, "
          f"{max(r[0]['max_D'] for r in results):.2e}]")

    # Rank and plot best
    ranked = sorted(results,
                    key=lambda x: (-x[0]["Ha_crossings"] - x[0]["Hb_crossings"],
                                    x[0]["max_C"]))
    best_rec, best_sol, best_C, best_D = ranked[0]
    print(f"  Best: Ha×={best_rec['Ha_crossings']} Hb×={best_rec['Hb_crossings']} "
          f"|C|={best_rec['max_C']:.2e} survived={best_rec['survived']}")

    _plot_best(interp, best_sol, best_C, best_D, config_name)

    # Save JSON
    js_path = os.path.join(OUTPUT_DIR, f"T3A_multispin_{config_name}.json")
    with open(js_path, "w") as f:
        json.dump([r[0] for r in ranked], f, indent=2)
    print(f"  Saved: {js_path}")

    return ranked


def _plot_best(interp, sol, C, D_res, config_name):
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle(f"Best trajectory: {config_name}", fontsize=14)

    ax = axes[0, 0]
    ax.plot(sol.t, sol.y[0], label="a(t)")
    ax.plot(sol.t, sol.y[2], label="b(t)")
    ax.set_title("Scale factors"); ax.legend(); ax.set_xlabel("t")

    ax = axes[0, 1]
    ax.plot(sol.y[0], sol.y[1], lw=0.8)
    ax.axhline(0, ls=":", color="k", alpha=0.4)
    ax.set_xlabel("a"); ax.set_ylabel("H_a"); ax.set_title("Phase (a, H_a)")

    ax = axes[0, 2]
    ax.plot(sol.y[2], sol.y[3], lw=0.8)
    ax.axhline(0, ls=":", color="k", alpha=0.4)
    ax.set_xlabel("b"); ax.set_ylabel("H_b"); ax.set_title("Phase (b, H_b)")

    ax = axes[1, 0]
    ax.semilogy(sol.t, np.abs(C) + 1e-30, label="|constraint|")
    ax.semilogy(sol.t, np.abs(D_res) + 1e-30, label="|continuity|")
    ax.set_title("Diagnostics"); ax.legend(); ax.set_xlabel("t")

    ax = axes[1, 1]
    B, A = np.meshgrid(interp.b_arr, interp.a_arr)
    ax.contourf(A, B, interp.E_grid, levels=30, cmap="RdBu_r", alpha=0.6)
    ax.contour(A, B, interp.E_grid, levels=[0], colors="k", linewidths=1.5)
    ax.plot(sol.y[0], sol.y[2], "g-", lw=1.2, label="trajectory")
    ax.plot(sol.y[0, 0], sol.y[2, 0], "go", ms=6)
    ax.set_xlabel("a"); ax.set_ylabel("b"); ax.set_title("Trajectory on E(a,b)")
    ax.legend()

    ax = axes[1, 2]
    w3_t, wp_t = [], []
    for i in range(sol.y.shape[1]):
        rho, p3, pphi, _ = interp.source(sol.y[:, i])
        w3_t.append(p3/rho if abs(rho) > 1e-30 else np.nan)
        wp_t.append(pphi/rho if abs(rho) > 1e-30 else np.nan)
    ax.plot(sol.t, w3_t, label="w₃")
    ax.plot(sol.t, wp_t, label="w_φ")
    ax.axhline(-1, ls=":", color="k", alpha=0.3)
    ax.set_xlabel("t"); ax.set_title("EOS along trajectory")
    ax.set_ylim(-3, 3); ax.legend()

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, f"T3A_multispin_{config_name}_best.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  7. Validation
# ═══════════════════════════════════════════════════════════════════════

def validate_against_scalar():
    """Cross-check: scalar_only config must match original single-spin code."""
    from T3A_casimir_spectral import casimir_E_and_derivs as orig_fn

    print("\n── Validation: scalar_only vs original code ──")
    test_pts = [(1.0, 1.0), (0.5, 2.0), (2.0, 0.5), (3.0, 3.0)]
    max_err = 0.0
    for a, b in test_pts:
        E_orig, da_orig, db_orig = orig_fn(a, b, c=C_CONF)
        E_new, da_new, db_new = casimir_multispin(a, b, CONFIGS["scalar_only"])
        err = abs(E_orig - E_new) / (abs(E_orig) + 1e-30)
        max_err = max(max_err, err)
        print(f"  (a,b)=({a},{b}): E_orig={E_orig:.8e}  E_new={E_new:.8e}  rel_err={err:.2e}")
    print(f"  Max relative error: {max_err:.2e}")
    assert max_err < 1e-10, f"Validation FAILED: max_err={max_err}"
    print("  PASSED ✓")


def validate_bianchi(field_content, label):
    """Verify Bianchi identity ∇_M T^M_N = 0 at a sample point."""
    a, b, Ha, Hb = 1.0, 1.0, 0.5, 0.3
    V4 = 4.0 * np.pi**3 * a**3 * b
    E, dEda, dEdb = casimir_multispin(a, b, field_content)

    rho  =  E / V4
    p3   = -(a / (3.0 * V4)) * dEda
    pphi = -(b / V4) * dEdb

    # dρ/dt via chain rule
    ada, bdb = a * Ha, b * Hb
    drho_dt = (dEda / V4 - 3.0*rho/a)*ada + (dEdb / V4 - rho/b)*bdb

    bianchi = drho_dt + 3.0*Ha*(rho + p3) + Hb*(rho + pphi)
    print(f"  Bianchi [{label}]: ρ={rho:.4e} p₃={p3:.4e} p_φ={pphi:.4e} "
          f"residual={bianchi:.2e}")


# ═══════════════════════════════════════════════════════════════════════
#  8. Main
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 72)
    print("T3-A MULTI-SPIN CASIMIR STRESS-ENERGY")
    print("Sectors: scalar(c=1/8) + co-exact vector + TT tensor + Dirac(AP)")
    print(f"D_scalar = {D_SCALAR:.6e},  D_coexact = {D_COEXACT:.6e}")
    print("=" * 72)

    # ── Validation ──
    try:
        validate_against_scalar()
    except ImportError:
        print("  (Skipping cross-validation: T3A_casimir_spectral not importable)")

    print("\n── Bianchi identity checks ──")
    for cname, fc in CONFIGS.items():
        validate_bianchi(fc, cname)

    # ── Sector-by-sector EOS at reference point ──
    print("\n── Sector EOS at (a,b) = (1,1) ──")
    a0, b0 = 1.0, 1.0
    V4 = 4.0 * np.pi**3
    for sname, sec in SPECTRAL_SECTORS.items():
        E, dEda, dEdb = _sector_energy(a0, b0, sec)
        rho = E / V4
        p3  = -(a0 / (3*V4)) * dEda
        pphi = -(b0 / V4) * dEdb
        w3 = p3/rho if abs(rho) > 1e-30 else float("nan")
        wp = pphi/rho if abs(rho) > 1e-30 else float("nan")
        sign = -1 if sec["is_fermion"] else +1
        d_val = sec['D_s1']
        d_str = "None" if d_val is None else f"{d_val:.5e}"
        print(f"  {sname:20s}: sign={sign:+d}  ρ={rho:+.4e}  w₃={w3:+.4f}  w_φ={wp:+.4f}  "
              f"(S₁ D={d_str})")

    # ── Build grids and run for key configurations ──
    configs_to_run = ["scalar_only", "graviton_only", "scalar_graviton", "full_SM"]
    init_grid = build_init_grid()

    for cname in configs_to_run:
        fc = CONFIGS[cname]
        print(f"\n{'━'*72}")
        print(f"CONFIG: {cname}")
        label = ", ".join(f"{m}×{k}" for k, m in fc)
        print(f"  Content: [{label}]")
        print(f"{'━'*72}")

        interp = MultispinInterpolator(fc, Na=80, Nb=80)

        print("  EOS landscape:")
        plot_eos_landscape(interp, cname)

        run_orbit_search(interp, cname, init_grid, tmax=60.0)

    print("\n" + "=" * 72)
    print("COMPLETE. Check T3A_multispin_*.png and T3A_multispin_*.json")
    print("=" * 72)
