#!/usr/bin/env python3
"""
T3-A Antiperiodic Casimir — v2: Targeted amplitude and IC grid fix
===================================================================

v1 run established:
  ✅ EOS sign fix: w₃ < 0 everywhere (99.9% of grid), median = −2.0
  ✅ At (a=2, r=0.1): w₃ = −1.009, w_φ = −0.149  (near-ΛK behavior)
  ❌ 0 oscillatory candidates — amplitude and IC grid issues

Root causes of v1 failure:
  1. N_EFF = 1 scalar: κρ/(k/a²) ≈ 0.05 at a=2, b=0.2
     → Need N_EFF ≈ 20 for Casimir ~ curvature at a~2, b~0.2
     → SM content: N_EFF = 50 plausible (thermal fermion dominance)
  2. IC grid: b0 ∈ {0.3, 0.5, …} — misses the b/a << 1 regime
     where Casimir energy is large (K₁(x) → 1/x as x = 2πk√(l²+c)b/a → 0)
     → Need b0 ∈ {0.05, 0.1, 0.15, 0.2, 0.3}
  3. |Hb0| threshold 50 → many physically interesting ICs rejected
     (those where 3k/a² > κρ require Hb0 ~ −k/(a Ha))

This run:
  • N_EFF = 50 (representative of SM thermal fermion content)
  • IC grid: a0 ∈ [0.3, 5.0], b0 ∈ [0.05, 1.0] — small-b regime
  • |Hb0| threshold raised to 20
  • Constraint satisfied at initialization (same formula, now with larger ρ)

Physical regime targeted:
  At a=2, b=0.2 (r=0.1), N_EFF=50:
    ρ = 50 × 1.36e-2 = 0.68,  k/a² = 0.25  → κρ/(k/a²) = 2.7 ✓
    Hb0 = (κρ − 3Ha² − 3k/a²)/(3Ha) ~ moderate for Ha ~ 0.3–1.0 ✓

Prediction from EOS:
  w₃ ≈ −1.0 in the b/a ~ 0.1 regime means the S³ pressure is attractive
  (p₃ ≈ −ρ < 0), which opposes the expansion → allows a(t) to turn around.
  w_φ ≈ −0.15 (nearly flat) at r=0.1 means b(t) evolves slowly.
  These are the conditions under which periodic orbits should be possible.
"""

import os
import sys
import json
import numpy as np

# ─── Path setup ───────────────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

# Import antiperiodic evaluator from v1; override N_EFF before building grid
import T3A_casimir_antiperiodic as _ap_module

# ═══ KEY PARAMETER CHANGE: N_EFF = 50 ══════════════════════════════
N_EFF_V2 = 50.0
_ap_module.N_EFF = N_EFF_V2
# ════════════════════════════════════════════════════════════════════

from T3A_casimir_antiperiodic import (
    CasimirInterpolatorAP,
    casimir_E_antiperiodic,
    rhs_full_5d,
    constraint_residual,
    continuity_residual,
)

from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

KAPPA5 = 1.0
K_CURV = 1.0
OUTPUT_DIR = _HERE


def init_from_constraint_v2(a0, Ha0, b0, source_fn, hb_thresh=20.0):
    """Solve constraint for Hb0; accept if |Hb0| < hb_thresh."""
    if abs(Ha0) < 1e-14:
        return None
    probe = [a0, Ha0, b0, 0.0]
    rho, _, _, _ = source_fn(probe, None)
    Hb0 = (KAPPA5 * rho - 3.0 * Ha0**2 - 3.0 * K_CURV / a0**2) / (3.0 * Ha0)
    if abs(Hb0) > hb_thresh:
        return None
    return np.array([a0, Ha0, b0, Hb0], dtype=float)


def build_init_grid_v2():
    """
    Targeted grid: small-b regime where Casimir ~ curvature.

    At N_EFF=50, Casimir ~ k/a² when b/a ~ 0.05–0.2 for a ~ 0.3–3.
    Ha0 values span slow to fast expansion.
    """
    grid = []
    for a0 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
        for Ha0 in [0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0]:
            for b0 in [0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.8, 1.0]:
                grid.append((a0, Ha0, b0))
    return grid


def run_v2(interp, init_grid, tmax=60.0, label="spectral_antiperiodic_v2"):
    """v2 ODE scan with relaxed Hb0 threshold."""
    source_fn = interp.source
    a_lo, a_hi = interp.a_lo, interp.a_hi
    b_lo, b_hi = interp.b_lo, interp.b_hi

    print(f"\n{'='*72}")
    print(f"CASE: {label}  (N_EFF={N_EFF_V2})")
    print(f"{'='*72}")

    accepted = rejected_hb = rejected_nan = 0
    results = []

    for (a0, Ha0, b0) in init_grid:
        state0 = init_from_constraint_v2(a0, Ha0, b0, source_fn, hb_thresh=20.0)
        if state0 is None:
            rejected_hb += 1
            continue
        if not np.isfinite(state0).all():
            rejected_nan += 1
            continue
        accepted += 1

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
            "b_over_a_ic": b0 / a0,
        }
        results.append((rec, sol, C, D))

    print(f"IC grid total: {len(init_grid)}  accepted: {accepted}"
          f"  rejected_hb: {rejected_hb}  rejected_nan: {rejected_nan}")

    if not results:
        print("No successful trajectories.")
        return []

    total = len(results)
    surv  = sum(r[0]["survived_full_window"] for r in results)
    osc   = sum(r[0]["Ha_crossings"] >= 4 for r in results)
    osc2  = sum(r[0]["Ha_crossings"] >= 2 for r in results)

    print(f"Trajectories integrated: {total}")
    print(f"Survived full window:    {surv}")
    print(f"Ha crossings ≥ 2:        {osc2}")
    print(f"Oscillatory (≥ 4 cross): {osc}")
    print("Constraint |C| range: "
          f"[{min(r[0]['max_abs_constraint'] for r in results):.2e}, "
          f"{max(r[0]['max_abs_constraint'] for r in results):.2e}]")
    print("Continuity |D| range: "
          f"[{min(r[0]['max_abs_continuity'] for r in results):.2e}, "
          f"{max(r[0]['max_abs_continuity'] for r in results):.2e}]")

    ranked = sorted(results,
                    key=lambda x: (-x[0]["Ha_crossings"] - x[0]["Hb_crossings"],
                                    x[0]["max_abs_constraint"]))

    # ── Show top 5 by oscillation ──
    print("\nTop candidates by oscillation count:")
    print(f"  {'a0':>5}  {'Ha0':>6}  {'b0':>5}  {'Hb0':>7}  {'Ha×':>5}  {'Hb×':>5}  "
          f"{'|C|max':>10}  {'surv':>5}")
    for rec_i, _, _, _ in ranked[:min(10, len(ranked))]:
        ic = rec_i["ic"]
        print(f"  {ic['a0']:>5.2f}  {ic['Ha0']:>6.3f}  {ic['b0']:>5.3f}  "
              f"{ic['Hb0']:>7.3f}  {rec_i['Ha_crossings']:>5}  {rec_i['Hb_crossings']:>5}  "
              f"{rec_i['max_abs_constraint']:>10.2e}  {str(rec_i['survived_full_window']):>5}")

    best = ranked[0]
    rec, sol, C, D = best

    # ── Best trajectory plot ──
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle(f"{label}  (N_EFF={N_EFF_V2})\n"
                 f"Best IC: a₀={rec['ic']['a0']}, Ha₀={rec['ic']['Ha0']:.3f}, "
                 f"b₀={rec['ic']['b0']}, Hb₀={rec['ic']['Hb0']:.3f}  "
                 f"[H_a×={rec['Ha_crossings']}, H_b×={rec['Hb_crossings']}]",
                 fontsize=10)

    axes[0, 0].plot(sol.t, sol.y[0], label="a(t)")
    axes[0, 0].plot(sol.t, sol.y[2], label="b(t)")
    axes[0, 0].set_title("Scale factors"); axes[0, 0].legend(); axes[0, 0].set_xlabel("t")

    axes[0, 1].plot(sol.y[0], sol.y[1], lw=0.8)
    axes[0, 1].axhline(0, ls=":", color="k", alpha=0.4)
    axes[0, 1].set_xlabel("a"); axes[0, 1].set_ylabel("H_a"); axes[0, 1].set_title("(a, H_a)")

    axes[0, 2].plot(sol.y[2], sol.y[3], lw=0.8)
    axes[0, 2].axhline(0, ls=":", color="k", alpha=0.4)
    axes[0, 2].set_xlabel("b"); axes[0, 2].set_ylabel("H_b"); axes[0, 2].set_title("(b, H_b)")

    axes[1, 0].semilogy(sol.t, np.abs(C) + 1e-30, label="|constraint|")
    axes[1, 0].semilogy(sol.t, np.abs(D) + 1e-30, label="|continuity|")
    axes[1, 0].legend(); axes[1, 0].set_xlabel("t"); axes[1, 0].set_title("Consistency")

    B2d, A2d = np.meshgrid(interp.b_arr, interp.a_arr)
    axes[1, 1].contourf(A2d, B2d, interp.E_grid, levels=30, cmap="RdBu_r", alpha=0.6)
    axes[1, 1].contour(A2d, B2d, interp.E_grid, levels=[0], colors="k", linewidths=1.5)
    axes[1, 1].plot(sol.y[0], sol.y[2], "g-", lw=1.2)
    axes[1, 1].plot(sol.y[0, 0], sol.y[2, 0], "go", ms=6)
    axes[1, 1].set_xlabel("a"); axes[1, 1].set_ylabel("b"); axes[1, 1].set_title("Traj on E(a,b)")

    source_fn = interp.source
    w3_t, wphi_t = [], []
    for i in range(sol.y.shape[1]):
        rho_i, p3_i, pphi_i, _ = source_fn(sol.y[:, i], None)
        w3_t.append(p3_i / rho_i if abs(rho_i) > 1e-30 else np.nan)
        wphi_t.append(pphi_i / rho_i if abs(rho_i) > 1e-30 else np.nan)
    axes[1, 2].plot(sol.t, w3_t, label="w₃")
    axes[1, 2].plot(sol.t, wphi_t, label="w_φ")
    axes[1, 2].axhline(-1, ls=":", color="k", alpha=0.3)
    axes[1, 2].axhline(-1/3, ls="--", color="g", alpha=0.5)
    axes[1, 2].set_ylim(-5, 5); axes[1, 2].legend(); axes[1, 2].set_xlabel("t")
    axes[1, 2].set_title("EOS along trajectory")

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, f"T3A_{label}_best.png")
    plt.savefig(fig_path, dpi=150); plt.close()
    print(f"\nSaved: {fig_path}")

    # ── Oscillatory candidates plot ──
    osc_results = [r for r in ranked if r[0]["Ha_crossings"] >= 2]
    if osc_results:
        n_plot = min(6, len(osc_results))
        fig, axes = plt.subplots(n_plot, 3, figsize=(18, 4 * n_plot))
        if n_plot == 1:
            axes = axes[np.newaxis, :]
        for idx in range(n_plot):
            rec_i, sol_i, C_i, D_i = osc_results[idx]
            ic = rec_i["ic"]
            axes[idx, 0].plot(sol_i.t, sol_i.y[0], label="a(t)")
            axes[idx, 0].plot(sol_i.t, sol_i.y[2], label="b(t)")
            axes[idx, 0].set_title(
                f"a₀={ic['a0']:.2f} Ha₀={ic['Ha0']:.2f} b₀={ic['b0']:.3f} Hb₀={ic['Hb0']:.3f} | "
                f"H_a×={rec_i['Ha_crossings']} H_b×={rec_i['Hb_crossings']} |C|={rec_i['max_abs_constraint']:.1e}")
            axes[idx, 0].legend(fontsize=8)
            axes[idx, 1].plot(sol_i.y[0], sol_i.y[1], lw=0.7)
            axes[idx, 1].axhline(0, ls=":", color="k", alpha=0.4)
            axes[idx, 1].set_xlabel("a"); axes[idx, 1].set_ylabel("H_a")
            axes[idx, 2].plot(sol_i.y[2], sol_i.y[3], lw=0.7)
            axes[idx, 2].axhline(0, ls=":", color="k", alpha=0.4)
            axes[idx, 2].set_xlabel("b"); axes[idx, 2].set_ylabel("H_b")
        plt.tight_layout()
        fig_path = os.path.join(OUTPUT_DIR, f"T3A_{label}_oscillatory.png")
        plt.savefig(fig_path, dpi=150); plt.close()
        print(f"Saved: {fig_path}")

    # ── JSON ──
    js_path = os.path.join(OUTPUT_DIR, f"T3A_{label}.json")
    with open(js_path, "w") as f:
        json.dump([r[0] for r in ranked], f, indent=2)
    print(f"Saved: {js_path}")

    return ranked


if __name__ == "__main__":
    print("=" * 72)
    print(f"T3-A ANTIPERIODIC CASIMIR v2  —  N_EFF = {N_EFF_V2}")
    print("Targeting b/a << 1 regime where Casimir ~ curvature")
    print("=" * 72)

    # Grid range covers b down to 0.05 (where Casimir energy is large)
    interp = CasimirInterpolatorAP(
        a_range=(0.1, 8.0), b_range=(0.05, 4.0),
        Na=80, Nb=80, c=1/8,
    )

    # Sample EOS at N_EFF=50 to verify amplitude
    print(f"\nAmplitude check (N_EFF={N_EFF_V2}) at a=2.0:")
    print(f"  {'r=b/a':>8}  {'ρ':>12}  {'k/a²':>8}  {'κρ/(k/a²)':>12}  {'w₃':>8}  {'w_φ':>8}")
    a_test = 2.0
    for r in [0.05, 0.10, 0.20, 0.30, 0.50]:
        b_test = a_test * r
        E, dEda, dEdb = interp.eval(a_test, b_test)
        V4 = 4 * np.pi**3 * a_test**3 * b_test
        rho  = E / V4
        p3   = -(a_test / (3 * V4)) * dEda
        pphi = -(b_test / V4) * dEdb
        w3_v   = p3   / rho if abs(rho) > 1e-30 else float('nan')
        wphi_v = pphi / rho if abs(rho) > 1e-30 else float('nan')
        ratio  = KAPPA5 * rho / (K_CURV / a_test**2) if K_CURV > 0 else float('nan')
        print(f"  {r:>8.3f}  {rho:>12.4e}  {K_CURV/a_test**2:>8.4f}  "
              f"{ratio:>12.4f}  {w3_v:>8.3f}  {wphi_v:>8.3f}")

    # Run ODE scan
    grid = build_init_grid_v2()
    print(f"\nInitial condition grid: {len(grid)} points (focused on small b0)")
    run_v2(interp, grid, tmax=80.0, label="spectral_antiperiodic_v2")

    print("\nDone.")
