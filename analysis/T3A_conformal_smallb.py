#!/usr/bin/env python3
"""
T3-A Periodic Conformal Scalar — S₂-Dominated Negative-Energy Regime
======================================================================

Summary of failure modes so far
---------------------------------
  Conformal scalar, periodic, S₁-dominant (v1):
    w₃=+2/3, w_φ=−1, ρ>0
    b-bounce test: 2w_φ/3 − w₃ + 1/3 = −1 < 0  ❌  b cannot oscillate

  Antiperiodic scalar (v1/v2/v3):
    w₃≈−1, w_φ≈+4, ρ>0
    a-bounce test: w_φ < 0 required  ❌  a cannot oscillate (v3 confirmed)

The unexplored regime
---------------------
For the PERIODIC conformal scalar at small b/a (b/a ≲ 0.1), the S₂ Bessel
sum dominates the S₁ zero-mode term:

  |E_S2| >> E_S1  (S₂ < 0 → total E < 0 → ρ < 0)

In this regime, the source properties FLIP sign:
  ρ < 0  (phantom-like: negative energy density)
  p_φ = w_φ_S2 × ρ ≈ (+1) × (negative) = NEGATIVE  ← satisfies a-bounce!
  p₃ ≈ 0  (∂E_S2/∂a → 0 for small b/a)

Necessary conditions for oscillations:
  a-bounce: κp_φ/3 < −k/a² requires p_φ < 0  ✓  (p_φ = w_φ ρ, ρ<0, w_φ>0)
  b-bounce: 2p_φ/3−p₃ + k/a²/κ > 0  — depends on details

Amplitude check at (a=2, b=0.1, N_EFF=50):
  E_S2 ≈ −(1/(πa)) × K₁(2π×0.05×√1.125) × √1.125 ≈ −0.463  per scalar
  ρ ≈ −0.463 / V₄ ≈ −4.7e−3  (N_EFF=1)
  ρ × 50 ≈ −0.235,  k/a² = 0.25  → |κρ|/(k/a²) ≈ 0.94  ← NEAR BALANCE ✓

This run:
  • N_EFF = 50  (same as v2, but with PERIODIC source)
  • b_range = (0.04, 4.0) to include the S₂-dominated small-b regime
  • IC grid: b0 ∈ {0.05, 0.08, 0.1, 0.15, 0.2, 0.3}  (targeting small b)
  • a0 ∈ {0.5, 1.0, 1.5, 2.0, 3.0}
  • Ha0 ∈ {0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0}
  • Accept |Hb0| ≤ 20 (ρ < 0 means Hb0 < 0 always for Ha > 0)

Diagnostic:
  Plot sign of ρ along trajectories — confirm S₂-dominated (ρ < 0) throughout
  Check if any trajectory has Ha sign change (a-bounce)
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

import T3A_casimir_spectral as _spec_module

# ═══ KEY: Use PERIODIC source (not antiperiodic) with N_EFF=50 ══════
N_EFF_RUN = 50.0
_spec_module.N_EFF = N_EFF_RUN
# ════════════════════════════════════════════════════════════════════

from T3A_casimir_spectral import (
    CasimirInterpolator,
    casimir_E_and_derivs,
    rhs_full_5d,
    constraint_residual,
    continuity_residual,
)

KAPPA5 = 1.0
K_CURV = 1.0
OUTPUT_DIR = _HERE


def casimir_source_periodic_direct(state, params=None):
    """Direct (non-interpolated) periodic conformal scalar source."""
    a, Ha, b, Hb = state
    a = max(a, 0.04)
    b = max(b, 0.04)
    V4 = 4.0 * np.pi**3 * a**3 * b
    E, dEda, dEdb = casimir_E_and_derivs(a, b, c=1/8)
    rho  =  E / V4
    p3   = -(a / (3.0 * V4)) * dEda
    pphi = -(b / V4) * dEdb
    drho_dt = ((dEda / V4) - 3.0 * rho / a) * a * Ha \
            + ((dEdb / V4) - rho / b) * b * Hb
    return rho, p3, pphi, drho_dt


def init_hb(a0, Ha0, b0, source_fn, hb_thresh=20.0):
    if abs(Ha0) < 1e-14:
        return None
    probe = [a0, Ha0, b0, 0.0]
    rho, _, _, _ = source_fn(probe, None)
    Hb0 = (KAPPA5 * rho - 3.0 * Ha0**2 - 3.0 * K_CURV / a0**2) / (3.0 * Ha0)
    return None if abs(Hb0) > hb_thresh else np.array([a0, Ha0, b0, Hb0])


def integrate_trajectory(state0, source_fn, tmax=100.0,
                          a_lo=0.04, a_hi=4.0, b_lo=0.04, b_hi=4.0):
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
            rhs_full_5d, [0.0, tmax], state0,
            args=(source_fn, None),
            method="Radau", max_step=0.02,
            rtol=1e-10, atol=1e-12,
            events=[ev_a_lo, ev_b_lo, ev_a_hi, ev_b_hi, ev_blow],
        )
    except Exception:
        return None, None, None

    C = np.array([constraint_residual(sol.y[:, i], source_fn, None)
                  for i in range(sol.y.shape[1])])
    D = np.array([continuity_residual(sol.y[:, i], source_fn, None)
                  for i in range(sol.y.shape[1])])
    return sol, C, D


def build_init_grid():
    """Target: small b/a where S₂ dominates and ρ < 0."""
    grid = []
    for a0 in [0.5, 1.0, 1.5, 2.0, 3.0]:
        for Ha0 in [0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0]:
            for b0 in [0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.30]:
                grid.append((a0, Ha0, b0))
    return grid


if __name__ == "__main__":
    print("=" * 72)
    print(f"T3-A PERIODIC CONFORMAL SCALAR  —  S₂-dominated negative-ρ regime")
    print(f"N_EFF = {N_EFF_RUN}  |  200×200 grid over (0.3,4.0)×(0.04,1.0)")
    print("=" * 72)

    # ── High-res interpolation grid focused on small-b region ──
    print("\nBuilding interpolation grid (200×200) …")
    interp = CasimirInterpolator(
        a_range=(0.3, 4.0), b_range=(0.04, 1.0),
        Na=200, Nb=200, c=1/8,
    )

    # ── EOS and sign-of-ρ diagnostic at key points ──
    print(f"\nEOS diagnostic (N_EFF={N_EFF_RUN}) at a=2.0:")
    print(f"  {'r=b/a':>8}  {'E':>12}  {'ρ':>12}  {'sign':>5}  {'w₃':>8}  {'w_φ':>8}  "
          f"{'p_φ<0?':>8}  {'κp_φ/(k/a²)':>12}")
    for r in [0.025, 0.05, 0.075, 0.10, 0.15, 0.20, 0.30, 0.50, 1.00]:
        a_t, b_t = 2.0, 2.0 * r
        if b_t < 0.04:
            continue
        E, dEda, dEdb = interp.eval(a_t, b_t)
        V4 = 4.0 * np.pi**3 * a_t**3 * b_t
        rho  =  E / V4
        p3   = -(a_t / (3.0 * V4)) * dEda
        pphi = -(b_t / V4) * dEdb
        w3   = p3 / rho if abs(rho) > 1e-30 else float('nan')
        wp   = pphi / rho if abs(rho) > 1e-30 else float('nan')
        sign = '+' if rho > 0 else '-'
        pphi_neg = 'YES' if pphi < 0 else 'NO'
        ratio = KAPPA5 * pphi / (3 * K_CURV / a_t**2) if K_CURV > 0 else float('nan')
        print(f"  {r:>8.3f}  {E:>12.4e}  {rho:>12.4e}  {sign:>5}  "
              f"{w3:>8.3f}  {wp:>8.3f}  {pphi_neg:>8}  {ratio:>12.4f}")

    # ── a-bounce viability check ──
    print(f"\na-bounce condition:  κp_φ/3 < −k/a²  ↔  κp_φ/(k/a²) < −3")
    print(f"  (Ḣa can be positive only when this holds)")
    print(f"  Antiperiodic scalar had κp_φ/(k/a²) ≈ +17 → impossible")
    print(f"  Periodic S₂-dominated: p_φ < 0 → need |κp_φ|/(k/a²) > 3")

    # ── Initialization check ──
    print(f"\nInitialization check (constraint solve for Hb0):")
    print(f"  {'a0':>5}  {'Ha0':>5}  {'b0':>5}  {'κρ':>10}  {'Hb0':>8}  {'valid':>6}")
    source_fn = interp.source
    for a0, Ha0, b0 in [(2.0, 0.5, 0.1), (2.0, 1.0, 0.1), (1.5, 0.5, 0.1),
                         (1.5, 1.0, 0.08), (2.0, 0.3, 0.05)]:
        probe = [a0, Ha0, b0, 0.0]
        rho_p, _, _, _ = source_fn(probe, None)
        s0 = init_hb(a0, Ha0, b0, source_fn)
        Hb0 = float(s0[3]) if s0 is not None else float('nan')
        print(f"  {a0:>5.2f}  {Ha0:>5.2f}  {b0:>5.3f}  "
              f"{KAPPA5*rho_p:>10.4f}  {Hb0:>8.4f}  "
              f"{'✓' if s0 is not None else '✗'}")

    # ── ODE scan ──
    grid = build_init_grid()
    print(f"\nODE scan: {len(grid)} ICs")
    print("=" * 72)

    results = []
    accepted = rejected = 0

    for (a0, Ha0, b0) in grid:
        state0 = init_hb(a0, Ha0, b0, source_fn, hb_thresh=20.0)
        if state0 is None:
            rejected += 1
            continue
        accepted += 1

        sol, C, D = integrate_trajectory(
            state0, source_fn, tmax=100.0,
            a_lo=interp.a_lo, a_hi=interp.a_hi,
            b_lo=interp.b_lo, b_hi=interp.b_hi,
        )
        if sol is None or len(sol.t) < 20:
            continue

        Ha_cross = int(np.sum(np.diff(np.sign(sol.y[1])) != 0))
        Hb_cross = int(np.sum(np.diff(np.sign(sol.y[3])) != 0))
        max_C    = float(np.max(np.abs(C)))

        # Track fraction of trajectory with ρ < 0
        rho_traj = [source_fn(sol.y[:, i], None)[0]
                    for i in range(0, sol.y.shape[1], max(1, sol.y.shape[1]//50))]
        frac_neg = np.mean(np.array(rho_traj) < 0)

        results.append({
            "ic": {"a0": a0, "Ha0": Ha0, "b0": b0, "Hb0": float(state0[3])},
            "t_end": float(sol.t[-1]),
            "a_range": [float(np.min(sol.y[0])), float(np.max(sol.y[0]))],
            "b_range": [float(np.min(sol.y[2])), float(np.max(sol.y[2]))],
            "Ha_crossings": Ha_cross,
            "Hb_crossings": Hb_cross,
            "max_abs_constraint": max_C,
            "max_abs_continuity": float(np.max(np.abs(D))),
            "frac_rho_negative": float(frac_neg),
            "survived": bool(sol.t[-1] >= 98.0),
            "_sol": sol, "_C": C, "_D": D,
        })

    print(f"Accepted: {accepted}  Rejected: {rejected}  Integrated: {len(results)}")

    if not results:
        print("No successful trajectories.")
    else:
        osc2 = sum(r["Ha_crossings"] >= 2 for r in results)
        osc4 = sum(r["Ha_crossings"] >= 4 for r in results)
        neg_rho = sum(r["frac_rho_negative"] > 0.5 for r in results)
        print(f"Ha× ≥ 2: {osc2}  |  Ha× ≥ 4: {osc4}")
        print(f"Trajectories with ρ < 0 for >50% of time: {neg_rho}")
        print(f"|C| range: [{min(r['max_abs_constraint'] for r in results):.2e}, "
              f"{max(r['max_abs_constraint'] for r in results):.2e}]")

        ranked = sorted(results,
                        key=lambda x: (-x["Ha_crossings"] - x["Hb_crossings"],
                                        x["max_abs_constraint"]))

        print(f"\nTop 10 candidates:")
        print(f"  {'a0':>5}  {'Ha0':>5}  {'b0':>5}  {'Hb0':>7}  "
              f"{'Ha×':>5}  {'Hb×':>5}  {'|C|':>10}  {'ρ<0%':>6}")
        for r in ranked[:10]:
            ic = r["ic"]
            print(f"  {ic['a0']:>5.2f}  {ic['Ha0']:>5.2f}  {ic['b0']:>5.3f}  "
                  f"{ic['Hb0']:>7.3f}  {r['Ha_crossings']:>5}  {r['Hb_crossings']:>5}  "
                  f"{r['max_abs_constraint']:>10.2e}  "
                  f"{100*r['frac_rho_negative']:>5.0f}%")

        # ── Plot best trajectory ──
        best = ranked[0]
        sol = best["_sol"]; C_arr = best["_C"]; D_arr = best["_D"]
        ic = best["ic"]

        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle(f"Periodic conformal scalar, S₂-dominated  (N_EFF={N_EFF_RUN})\n"
                     f"Best IC: a₀={ic['a0']} Ha₀={ic['Ha0']:.2f} b₀={ic['b0']} "
                     f"Hb₀={ic['Hb0']:.3f}  H_a×={best['Ha_crossings']}  "
                     f"|C|max={best['max_abs_constraint']:.2e}", fontsize=10)

        axes[0, 0].plot(sol.t, sol.y[0], label="a(t)")
        axes[0, 0].plot(sol.t, sol.y[2], label="b(t)")
        axes[0, 0].set_title("Scale factors"); axes[0, 0].legend(); axes[0, 0].set_xlabel("t")

        axes[0, 1].plot(sol.y[0], sol.y[1], lw=0.8)
        axes[0, 1].axhline(0, ls=":", color="k", alpha=0.4)
        axes[0, 1].set_xlabel("a"); axes[0, 1].set_ylabel("H_a"); axes[0, 1].set_title("(a, H_a)")

        axes[0, 2].plot(sol.y[2], sol.y[3], lw=0.8)
        axes[0, 2].axhline(0, ls=":", color="k", alpha=0.4)
        axes[0, 2].set_xlabel("b"); axes[0, 2].set_ylabel("H_b"); axes[0, 2].set_title("(b, H_b)")

        axes[1, 0].semilogy(sol.t, np.abs(C_arr) + 1e-30, label="|C|", lw=1.0)
        axes[1, 0].semilogy(sol.t, np.abs(D_arr) + 1e-30, label="|D|", lw=1.0)
        axes[1, 0].legend(); axes[1, 0].set_xlabel("t"); axes[1, 0].set_title("Constraint|Continuity")

        rho_t, p3_t, pphi_t = [], [], []
        for i in range(sol.y.shape[1]):
            r_i, p3_i, pp_i, _ = source_fn(sol.y[:, i], None)
            rho_t.append(r_i); p3_t.append(p3_i); pphi_t.append(pp_i)
        axes[1, 1].plot(sol.t, rho_t, label="ρ", lw=1.0)
        axes[1, 1].axhline(0, ls=":", color="k", alpha=0.4)
        axes[1, 1].set_xlabel("t"); axes[1, 1].set_title("Energy density ρ(t)")
        axes[1, 1].legend()

        w3_t  = [p3_t[i]/rho_t[i]  if abs(rho_t[i]) > 1e-30 else np.nan for i in range(len(rho_t))]
        wp_t  = [pphi_t[i]/rho_t[i] if abs(rho_t[i]) > 1e-30 else np.nan for i in range(len(rho_t))]
        axes[1, 2].plot(sol.t, np.clip(w3_t, -5, 5), label="w₃", lw=1.0)
        axes[1, 2].plot(sol.t, np.clip(wp_t, -5, 5), label="w_φ", lw=0.8)
        axes[1, 2].axhline(-1, ls=":", color="k", alpha=0.3)
        axes[1, 2].set_ylim(-5, 5); axes[1, 2].legend()
        axes[1, 2].set_xlabel("t"); axes[1, 2].set_title("EOS w₃, w_φ")

        plt.tight_layout()
        fig_path = os.path.join(OUTPUT_DIR, "T3A_conformal_smallb_best.png")
        plt.savefig(fig_path, dpi=150); plt.close()
        print(f"\nSaved: {fig_path}")

        # ── JSON ──
        js_out = [{k: v for k, v in r.items() if not k.startswith("_")}
                  for r in ranked]
        js_path = os.path.join(OUTPUT_DIR, "T3A_conformal_smallb.json")
        with open(js_path, "w") as f:
            json.dump(js_out, f, indent=2)
        print(f"Saved: {js_path}")

    print("\nDone.")
