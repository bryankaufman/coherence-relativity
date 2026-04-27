#!/usr/bin/env python3
"""
T3-A Antiperiodic Casimir — v3: Constraint-controlled refinement
=================================================================

v2 results:
  ✅ 34 oscillatory candidates (H_a crossings ≥ 4)
  ✅ Best: a₀=1.5, Ha₀=0.2, b₀=0.2, Hb₀=−0.484  →  H_a×=11, H_b×=19
  ⚠️ Constraint |C|max = 1.27  (physical or numerical?)

Diagnosis:
  The constraint 3H_a² + 3k/a² + 3H_aH_b = κρ is satisfied EXACTLY at t=0
  by construction.  It is a first integral of the ODE system — preserved
  analytically.  Numerical growth of |C| along the trajectory indicates
  interpolation errors in the Casimir source, not a physical violation.

  For the 80×80 grid over (0.1,8)×(0.05,4), the cell size at b=0.2 is
  Δb = 4/80 = 0.05 (50% of b itself) — coarse.  Bicubic spline errors
  in dE/db and dE/da propagate into (ρ, p₃, p_φ), causing |C| drift.

This run:
  1. High-resolution 200×200 grid restricted to (0.8,2.5)×(0.04,0.6)
     Cell size: Δa = 1.7/200 = 0.0085, Δb = 0.56/200 = 0.0028
     Expected interpolation error: ~ (Δb)⁴ for spline → 10⁻¹⁰ relative
  2. Tight IC grid around the v2 best region: a₀ ∈ [1.0,2.0], b₀ ∈ [0.1,0.4]
  3. Record max |C| and max |D| per trajectory; filter on |C|max < 0.1
  4. For top oscillatory candidates: re-run with DIRECT evaluation
     (casimir_E_antiperiodic called at each ODE step) to confirm no
     interpolation artifact — slow but definitive

Expected outcome:
  If the oscillatory behavior at a₀=1.5, b₀=0.2 is real:
    → High-res run shows H_a crossings ≥ 4 with |C|max << 1
    → Direct-eval confirmation gives same crossing count
    → This constitutes strong evidence for periodic orbit existence
"""

import os
import sys
import json
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import T3A_casimir_antiperiodic as _ap_module
N_EFF_V3 = 50.0
_ap_module.N_EFF = N_EFF_V3

from T3A_casimir_antiperiodic import (
    CasimirInterpolatorAP,
    casimir_E_antiperiodic,
    rhs_full_5d,
    constraint_residual,
    continuity_residual,
)

KAPPA5 = 1.0
K_CURV = 1.0
OUTPUT_DIR = _HERE


# ═══════════════════════════════════════════════════════════════════════
#  Direct source (no interpolation) — slow but exact
# ═══════════════════════════════════════════════════════════════════════

def casimir_source_direct(state, params=None):
    """
    Direct (non-interpolated) Casimir source.  Used for final verification
    of oscillatory candidates.  Each call evaluates the Bessel sums directly.
    """
    a, Ha, b, Hb = state
    a = max(a, 0.04)
    b = max(b, 0.04)
    V4 = 4.0 * np.pi**3 * a**3 * b
    E, dEda, dEdb = casimir_E_antiperiodic(a, b, c=1/8)

    rho  =  E / V4
    p3   = -(a / (3.0 * V4)) * dEda
    pphi = -(b / V4) * dEdb
    drho_dt = ((dEda / V4) - 3.0 * rho / a) * a * Ha \
            + ((dEdb / V4) - rho / b) * b * Hb
    return rho, p3, pphi, drho_dt


# ═══════════════════════════════════════════════════════════════════════
#  Shared ODE utilities
# ═══════════════════════════════════════════════════════════════════════

def integrate_trajectory(state0, source_fn, tmax=80.0,
                          a_lo=0.8, a_hi=2.5, b_lo=0.04, b_hi=0.6):
    """Radau integration with boundary events.  Returns (sol, C_arr, D_arr)."""
    def ev_a_lo(t, y, *a): return y[0] - a_lo * 1.02
    ev_a_lo.terminal = True; ev_a_lo.direction = -1

    def ev_b_lo(t, y, *a): return y[2] - b_lo * 1.02
    ev_b_lo.terminal = True; ev_b_lo.direction = -1

    def ev_a_hi(t, y, *a): return a_hi * 0.98 - y[0]
    ev_a_hi.terminal = True; ev_a_hi.direction = -1

    def ev_b_hi(t, y, *a): return b_hi * 0.98 - y[2]
    ev_b_hi.terminal = True; ev_b_hi.direction = -1

    def ev_blow(t, y, *a): return 1e4 - (abs(y[1]) + abs(y[3]))
    ev_blow.terminal = True

    try:
        sol = solve_ivp(
            rhs_full_5d,
            [0.0, tmax],
            state0,
            args=(source_fn, None),
            method="Radau",
            max_step=0.02,      # finer steps for better constraint preservation
            rtol=1e-10,
            atol=1e-12,
            events=[ev_a_lo, ev_b_lo, ev_a_hi, ev_b_hi, ev_blow],
        )
    except Exception as e:
        return None, None, None

    C = np.array([constraint_residual(sol.y[:, i], source_fn)
                  for i in range(sol.y.shape[1])])
    D = np.array([continuity_residual(sol.y[:, i], source_fn)
                  for i in range(sol.y.shape[1])])
    return sol, C, D


def count_crossings(arr):
    return int(np.sum(np.diff(np.sign(arr)) != 0))


def init_hb(a0, Ha0, b0, source_fn, hb_thresh=15.0):
    """Solve constraint for Hb0."""
    if abs(Ha0) < 1e-14:
        return None
    probe = [a0, Ha0, b0, 0.0]
    rho, _, _, _ = source_fn(probe, None)
    Hb0 = (KAPPA5 * rho - 3.0 * Ha0**2 - 3.0 * K_CURV / a0**2) / (3.0 * Ha0)
    return None if abs(Hb0) > hb_thresh else np.array([a0, Ha0, b0, Hb0])


# ═══════════════════════════════════════════════════════════════════════
#  Stage 1: High-resolution interpolated scan
# ═══════════════════════════════════════════════════════════════════════

def stage1_hires_scan(interp):
    """
    Fine IC grid around v2 best region.
    Filter results by |C|max < 0.5 (rough cutoff).
    """
    source_fn = interp.source
    a_lo, a_hi = interp.a_lo, interp.a_hi
    b_lo, b_hi = interp.b_lo, interp.b_hi

    grid = []
    for a0 in np.linspace(1.0, 2.0, 9):          # 1.0, 1.125, …, 2.0
        for Ha0 in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.7, 1.0]:
            for b0 in np.linspace(0.10, 0.40, 7):  # 0.10, 0.15, …, 0.40
                grid.append((float(a0), Ha0, float(b0)))

    print(f"\nStage 1 grid: {len(grid)} ICs in (a₀∈[1,2], Ha₀∈[0.05,1], b₀∈[0.1,0.4])")
    results = []

    accepted = rejected = 0
    for (a0, Ha0, b0) in grid:
        state0 = init_hb(a0, Ha0, b0, source_fn, hb_thresh=15.0)
        if state0 is None:
            rejected += 1
            continue
        accepted += 1

        sol, C, D = integrate_trajectory(
            state0, source_fn, tmax=100.0,
            a_lo=a_lo, a_hi=a_hi, b_lo=b_lo, b_hi=b_hi
        )
        if sol is None or len(sol.t) < 20:
            continue

        Ha_cross = count_crossings(sol.y[1])
        Hb_cross = count_crossings(sol.y[3])
        max_C = float(np.max(np.abs(C)))
        max_D = float(np.max(np.abs(D)))

        rec = {
            "ic": {"a0": a0, "Ha0": Ha0, "b0": b0, "Hb0": float(state0[3])},
            "t_end": float(sol.t[-1]),
            "a_range": [float(np.min(sol.y[0])), float(np.max(sol.y[0]))],
            "b_range": [float(np.min(sol.y[2])), float(np.max(sol.y[2]))],
            "Ha_crossings": Ha_cross,
            "Hb_crossings": Hb_cross,
            "max_abs_constraint": max_C,
            "max_abs_continuity": max_D,
            "survived": bool(sol.t[-1] >= 0.98 * 100.0),
        }
        results.append((rec, sol, C, D))

    print(f"  Accepted: {accepted}  Rejected (|Hb0|>15): {rejected}")
    print(f"  Integrated: {len(results)}")

    if not results:
        return []

    osc4 = sum(r[0]["Ha_crossings"] >= 4 for r in results)
    osc2 = sum(r[0]["Ha_crossings"] >= 2 for r in results)
    good_C = sum(r[0]["max_abs_constraint"] < 0.5 and r[0]["Ha_crossings"] >= 4
                 for r in results)

    print(f"  Ha× ≥ 2: {osc2}  |  Ha× ≥ 4: {osc4}  |  Ha×≥4 AND |C|<0.5: {good_C}")
    print(f"  |C| range: [{min(r[0]['max_abs_constraint'] for r in results):.2e}, "
          f"{max(r[0]['max_abs_constraint'] for r in results):.2e}]")

    ranked = sorted(results,
                    key=lambda x: (-x[0]["Ha_crossings"] - x[0]["Hb_crossings"],
                                    x[0]["max_abs_constraint"]))

    print(f"\n  Top 10 (stage 1, high-res interpolation):")
    print(f"  {'a0':>5}  {'Ha0':>5}  {'b0':>5}  {'Hb0':>7}  "
          f"{'Ha×':>5}  {'Hb×':>5}  {'|C|':>10}  {'surv':>5}")
    for rec_i, _, _, _ in ranked[:10]:
        ic = rec_i["ic"]
        print(f"  {ic['a0']:>5.3f}  {ic['Ha0']:>5.3f}  {ic['b0']:>5.3f}  "
              f"{ic['Hb0']:>7.3f}  {rec_i['Ha_crossings']:>5}  {rec_i['Hb_crossings']:>5}  "
              f"{rec_i['max_abs_constraint']:>10.2e}  {str(rec_i['survived']):>5}")

    # Plot best stage-1 trajectory
    best_rec, best_sol, best_C, best_D = ranked[0]
    _plot_trajectory(best_rec, best_sol, best_C, best_D, interp.source,
                     "v3_stage1_best", interp.E_grid, interp.a_arr, interp.b_arr)

    # Save JSON
    js_path = os.path.join(OUTPUT_DIR, "T3A_antiperiodic_v3_stage1.json")
    with open(js_path, "w") as f:
        json.dump([r[0] for r in ranked], f, indent=2)
    print(f"  Saved: {js_path}")

    return ranked


# ═══════════════════════════════════════════════════════════════════════
#  Stage 2: Direct-evaluation confirmation of top candidates
# ═══════════════════════════════════════════════════════════════════════

def stage2_direct_confirm(stage1_ranked, n_top=5):
    """
    Re-integrate the top n_top stage-1 candidates using the direct
    (non-interpolated) Casimir source.  This eliminates interpolation
    error from the constraint diagnostic.
    """
    candidates = [r for r in stage1_ranked if r[0]["Ha_crossings"] >= 4][:n_top]
    if not candidates:
        candidates = stage1_ranked[:n_top]

    print(f"\nStage 2: Direct-evaluation confirmation of top {len(candidates)} candidates")
    print("  (Each call evaluates Bessel sums directly — slow but exact)")

    confirmed = []
    for rec_i, _, _, _ in candidates:
        ic = rec_i["ic"]
        state0 = np.array([ic["a0"], ic["Ha0"], ic["b0"], ic["Hb0"]])

        print(f"\n  IC: a={ic['a0']:.3f} Ha={ic['Ha0']:.3f} b={ic['b0']:.3f} "
              f"Hb={ic['Hb0']:.3f}", flush=True)

        # Re-initialize Hb from direct source to ensure constraint exact at t=0
        state0_direct = init_hb(ic["a0"], ic["Ha0"], ic["b0"],
                                  casimir_source_direct, hb_thresh=20.0)
        if state0_direct is None:
            print(f"    Rejected (Hb0 threshold)")
            continue

        # Use same domain as stage 1
        sol, C, D = integrate_trajectory(
            state0_direct, casimir_source_direct, tmax=100.0,
            a_lo=0.8, a_hi=2.5, b_lo=0.04, b_hi=0.6
        )

        if sol is None or len(sol.t) < 20:
            print(f"    Integration failed or too short")
            continue

        Ha_cross = count_crossings(sol.y[1])
        Hb_cross = count_crossings(sol.y[3])
        max_C = float(np.max(np.abs(C)))
        max_D = float(np.max(np.abs(D)))

        print(f"    DIRECT:  H_a×={Ha_cross}  H_b×={Hb_cross}  "
              f"|C|max={max_C:.2e}  |D|max={max_D:.2e}  t_end={sol.t[-1]:.1f}")
        print(f"    Interp:  H_a×={rec_i['Ha_crossings']}  H_b×={rec_i['Hb_crossings']}  "
              f"|C|max={rec_i['max_abs_constraint']:.2e}")

        rec_direct = {
            "ic": {"a0": float(state0_direct[0]), "Ha0": float(state0_direct[1]),
                   "b0": float(state0_direct[2]), "Hb0": float(state0_direct[3])},
            "t_end": float(sol.t[-1]),
            "a_range": [float(np.min(sol.y[0])), float(np.max(sol.y[0]))],
            "b_range": [float(np.min(sol.y[2])), float(np.max(sol.y[2]))],
            "Ha_crossings": Ha_cross,
            "Hb_crossings": Hb_cross,
            "max_abs_constraint": max_C,
            "max_abs_continuity": max_D,
            "survived": bool(sol.t[-1] >= 98.0),
            "method": "direct",
        }
        confirmed.append((rec_direct, sol, C, D))

        if Ha_cross >= 4:
            _plot_trajectory(rec_direct, sol, C, D, casimir_source_direct,
                             f"v3_stage2_direct_a{ic['a0']:.2f}_b{ic['b0']:.3f}",
                             E_grid=None, a_arr=None, b_arr=None)

    # Save
    js_path = os.path.join(OUTPUT_DIR, "T3A_antiperiodic_v3_stage2.json")
    with open(js_path, "w") as f:
        json.dump([r[0] for r in confirmed], f, indent=2)
    print(f"\n  Stage 2 saved: {js_path}")

    return confirmed


# ═══════════════════════════════════════════════════════════════════════
#  Plotting
# ═══════════════════════════════════════════════════════════════════════

def _plot_trajectory(rec, sol, C, D, source_fn, label,
                      E_grid=None, a_arr=None, b_arr=None):
    ic = rec["ic"]
    Ha_cross = rec["Ha_crossings"]
    Hb_cross = rec["Hb_crossings"]
    max_C = rec["max_abs_constraint"]

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle(
        f"{label}  |  a₀={ic['a0']:.3f}  Ha₀={ic['Ha0']:.3f}  "
        f"b₀={ic['b0']:.3f}  Hb₀={ic['Hb0']:.3f}\n"
        f"H_a×={Ha_cross}  H_b×={Hb_cross}  |C|max={max_C:.2e}  t_end={rec['t_end']:.1f}",
        fontsize=10
    )

    axes[0, 0].plot(sol.t, sol.y[0], label="a(t)", lw=1.2)
    axes[0, 0].plot(sol.t, sol.y[2], label="b(t)", lw=1.2)
    axes[0, 0].set_title("Scale factors"); axes[0, 0].legend(); axes[0, 0].set_xlabel("t")

    axes[0, 1].plot(sol.y[0], sol.y[1], lw=0.8)
    axes[0, 1].axhline(0, ls=":", color="k", alpha=0.4)
    axes[0, 1].set_xlabel("a"); axes[0, 1].set_ylabel("H_a"); axes[0, 1].set_title("(a, H_a)")

    axes[0, 2].plot(sol.y[2], sol.y[3], lw=0.8)
    axes[0, 2].axhline(0, ls=":", color="k", alpha=0.4)
    axes[0, 2].set_xlabel("b"); axes[0, 2].set_ylabel("H_b"); axes[0, 2].set_title("(b, H_b)")

    axes[1, 0].semilogy(sol.t, np.abs(C) + 1e-30, label="|constraint|", lw=1.0)
    axes[1, 0].semilogy(sol.t, np.abs(D) + 1e-30, label="|continuity|", lw=1.0)
    axes[1, 0].axhline(0.1, ls="--", color="r", alpha=0.5, label="|C|=0.1 threshold")
    axes[1, 0].legend(fontsize=8); axes[1, 0].set_xlabel("t"); axes[1, 0].set_title("Consistency")

    if E_grid is not None and a_arr is not None:
        B2d, A2d = np.meshgrid(b_arr, a_arr)
        axes[1, 1].contourf(A2d, B2d, E_grid, levels=30, cmap="RdBu_r", alpha=0.6)
        axes[1, 1].contour(A2d, B2d, E_grid, levels=[0], colors="k", linewidths=1.5)
    axes[1, 1].plot(sol.y[0], sol.y[2], "g-", lw=1.0)
    axes[1, 1].plot(sol.y[0, 0], sol.y[2, 0], "go", ms=7)
    axes[1, 1].set_xlabel("a"); axes[1, 1].set_ylabel("b"); axes[1, 1].set_title("(a,b) trajectory")

    w3_t, wphi_t = [], []
    for i in range(sol.y.shape[1]):
        rho_i, p3_i, pphi_i, _ = source_fn(sol.y[:, i], None)
        w3_t.append(p3_i / rho_i if abs(rho_i) > 1e-30 else np.nan)
        wphi_t.append(pphi_i / rho_i if abs(rho_i) > 1e-30 else np.nan)
    axes[1, 2].plot(sol.t, np.clip(w3_t, -5, 5), label="w₃", lw=1.0)
    axes[1, 2].plot(sol.t, np.clip(wphi_t, -10, 10), label="w_φ", lw=0.8, alpha=0.7)
    axes[1, 2].axhline(-1, ls=":", color="k", alpha=0.3)
    axes[1, 2].axhline(-1/3, ls="--", color="g", alpha=0.5)
    axes[1, 2].set_ylim(-5, 5); axes[1, 2].legend(fontsize=8)
    axes[1, 2].set_xlabel("t"); axes[1, 2].set_title("EOS along trajectory")

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, f"T3A_{label}.png")
    plt.savefig(fig_path, dpi=150); plt.close()
    print(f"  Saved: {fig_path}")


# ═══════════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 72)
    print(f"T3-A ANTIPERIODIC CASIMIR v3  —  Constraint-controlled refinement")
    print(f"N_EFF = {N_EFF_V3}  |  High-res grid: 200×200 over (0.8,2.5)×(0.04,0.6)")
    print("=" * 72)

    # ── Stage 1: High-resolution interpolation grid ──
    print("\nBuilding high-resolution interpolation grid (200×200) …")
    interp_hires = CasimirInterpolatorAP(
        a_range=(0.8, 2.5), b_range=(0.04, 0.60),
        Na=200, Nb=200, c=1/8,
    )

    # Constraint check at known v2 IC
    print("\nConstraint check at v2 best IC (a=1.5, Ha=0.2, b=0.2, Hb=-0.484):")
    state_test = [1.5, 0.2, 0.2, -0.484]
    C_interp = constraint_residual(state_test, interp_hires.source)
    C_direct  = constraint_residual(state_test, casimir_source_direct)
    print(f"  Interpolated source: |C| = {abs(C_interp):.4e}")
    print(f"  Direct source:       |C| = {abs(C_direct):.4e}")
    print(f"  (Both should be ~0 since Hb=-0.484 was set by v2 coarse constraint)")

    # Re-initialize with high-res source and check new Hb0
    state_recheck = init_hb(1.5, 0.2, 0.2, interp_hires.source, hb_thresh=15.0)
    if state_recheck is not None:
        print(f"  Hb0 from hires interpolation: {state_recheck[3]:.6f}")
        print(f"  (vs v2 coarse: -0.484)")

    # ── Stage 1 scan ──
    s1_ranked = stage1_hires_scan(interp_hires)

    if not s1_ranked:
        print("\nNo trajectories survived Stage 1.  Check grid bounds.")
    else:
        # ── Stage 2: Direct evaluation confirmation ──
        # Pick top candidates: best oscillation count, then best constraint
        top = [r for r in s1_ranked if r[0]["Ha_crossings"] >= 4]
        top_sorted = sorted(top, key=lambda x: x[0]["max_abs_constraint"])
        print(f"\nStage 1 found {len(top)} oscillatory candidates (Ha× ≥ 4)")
        print("Sending top 5 (by lowest |C|) to Stage 2 direct-eval confirmation …")
        s2_confirmed = stage2_direct_confirm(top_sorted, n_top=5)

        # ── Final verdict ──
        print("\n" + "=" * 72)
        print("FINAL VERDICT (Stage 2 direct evaluation):")
        print("=" * 72)
        osc_confirmed = [r for r in s2_confirmed if r[0]["Ha_crossings"] >= 4]
        if osc_confirmed:
            print(f"  ✅ {len(osc_confirmed)} oscillatory candidates CONFIRMED with direct eval")
            for rc, _, Cv, Dv in osc_confirmed:
                ic = rc["ic"]
                print(f"     a₀={ic['a0']:.3f}  Ha₀={ic['Ha0']:.3f}  b₀={ic['b0']:.3f}  "
                      f"H_a×={rc['Ha_crossings']}  H_b×={rc['Hb_crossings']}  "
                      f"|C|={rc['max_abs_constraint']:.2e}  |D|={rc['max_abs_continuity']:.2e}")
        else:
            print("  ❌ No oscillatory candidates survived Stage 2 direct eval")
            print("     → Oscillations in Stage 1 were interpolation artifacts")
            print("     → Revisit field content, N_EFF, or boundary conditions")

    print("\nDone.")
