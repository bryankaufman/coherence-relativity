#!/usr/bin/env python3
"""
T3-A Full 5D Ansatz Solver
==========================
Metric:
  ds^2 = -dt^2 + a(t)^2 dΩ_3^2 + b(t)^2 dφ^2,  k=+1

Evolved system uses full 5D Einstein equations (not reduced-only form):

  G^t_t = -κρ
    3H_a^2 + 3k/a^2 + 3H_aH_b = κρ                               (constraint)

  G^φ_φ = κp_φ
    Ḣ_a = -(2H_a^2 + k/a^2 + κp_φ/3)

  G^i_i = κp_3
    Ḣ_b = H_a^2 + k/a^2 - 2H_aH_b - H_b^2 + κ(2p_φ/3 - p_3)

  ȧ = aH_a,  ḃ = bH_b

Continuity equation (diagnostic):
  ρ̇ + 3H_a(ρ+p_3) + H_b(ρ+p_φ) = 0

This script runs three sanity suites:
  1) Vacuum-Λ (constant source, isotropic EOS)
  2) Isotropic Casimir ansatz ρ=α/b^4, p_3=p_φ=-ρ
  3) Anisotropic Casimir with conservation-closed p_3
"""

import os
import json
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
KAPPA5 = 1.0
K_CURV = 1.0


def source_vacuum_lambda(state, params):
    """ρ=Λ/κ, p_3=p_φ=-ρ."""
    rho = params["Lambda"] / KAPPA5
    p3 = -rho
    pphi = -rho
    # explicit time derivative for continuity diagnostic
    drho_dt = 0.0
    return rho, p3, pphi, drho_dt


def source_casimir_isotropic(state, params):
    """ρ=α/b^4, p_3=p_φ=-ρ (effective isotropic vacuum form)."""
    _, _, b, Hb = state
    alpha = params["alpha"]
    rho = alpha / (b**4)
    p3 = -rho
    pphi = -rho
    drho_dt = -4.0 * rho * Hb
    return rho, p3, pphi, drho_dt


def source_casimir_aniso_conservation_closed(state, params):
    """
    ρ=α/b^4, p_φ=w_φ ρ, and p_3 is closed by continuity equation.
    This enforces ∇·T = 0 by construction for this parametric source.
    """
    _, Ha, b, Hb = state
    alpha = params["alpha"]
    wphi = params["wphi"]

    rho = alpha / (b**4)
    pphi = wphi * rho
    drho_dt = -4.0 * rho * Hb

    # From continuity: p3 = -(ρ + (ρ̇ + Hb(ρ+pφ))/(3Ha))
    eps = 1e-12
    if abs(Ha) < eps:
        # near Ha=0 this closure is singular; caller should stop near this region
        p3 = np.sign(Ha if Ha != 0 else 1.0) * 1e30
    else:
        p3 = -(rho + (drho_dt + Hb * (rho + pphi)) / (3.0 * Ha))
    return rho, p3, pphi, drho_dt


def rhs_full_5d(t, state, source_fn, source_params):
    a, Ha, b, Hb = state
    if a <= 0 or b <= 0:
        return [0.0, 0.0, 0.0, 0.0]

    rho, p3, pphi, _ = source_fn(state, source_params)
    da = a * Ha
    dHa = -(2.0 * Ha**2 + K_CURV / a**2 + KAPPA5 * pphi / 3.0)
    db = b * Hb
    dHb = (
        Ha**2
        + K_CURV / a**2
        - 2.0 * Ha * Hb
        - Hb**2
        + KAPPA5 * (2.0 * pphi / 3.0 - p3)
    )
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
    """Solve constraint for Hb0."""
    if abs(Ha0) < 1e-14:
        return None
    probe = np.array([a0, Ha0, b0, 0.0])
    rho, _, _, _ = source_fn(probe, source_params)
    Hb0 = (KAPPA5 * rho - 3.0 * Ha0**2 - 3.0 * K_CURV / a0**2) / (3.0 * Ha0)
    return np.array([a0, Ha0, b0, Hb0], dtype=float)


def run_case(case_name, source_fn, source_params, init_grid, tmax=80.0):
    print("\n" + "=" * 72)
    print(f"CASE: {case_name}")
    print("=" * 72)

    results = []

    for (a0, Ha0, b0) in init_grid:
        state0 = init_from_constraint(a0, Ha0, b0, source_fn, source_params)
        if state0 is None or not np.isfinite(state0).all():
            continue
        if abs(state0[3]) > 100:
            continue

        def ev_a(t, y, *args):
            return y[0] - 1e-6
        ev_a.terminal = True
        ev_a.direction = -1

        def ev_b(t, y, *args):
            return y[2] - 1e-6
        ev_b.terminal = True
        ev_b.direction = -1

        def ev_blow(t, y, *args):
            return 1e8 - (abs(y[1]) + abs(y[3]))
        ev_blow.terminal = True

        try:
            sol = solve_ivp(
                rhs_full_5d,
                [0.0, tmax],
                state0,
                args=(source_fn, source_params),
                method="Radau",
                max_step=0.05,
                rtol=1e-9,
                atol=1e-11,
                events=[ev_a, ev_b, ev_blow],
            )
        except Exception:
            continue

        if len(sol.t) < 20:
            continue

        C = np.array([constraint_residual(sol.y[:, i], source_fn, source_params) for i in range(sol.y.shape[1])])
        D = np.array([continuity_residual(sol.y[:, i], source_fn, source_params) for i in range(sol.y.shape[1])])

        Ha_cross = int(np.sum(np.diff(np.sign(sol.y[1])) != 0))
        Hb_cross = int(np.sum(np.diff(np.sign(sol.y[3])) != 0))

        rec = {
            "ic": {"a0": a0, "Ha0": Ha0, "b0": b0, "Hb0": float(state0[3])},
            "t_end": float(sol.t[-1]),
            "a_min": float(np.min(sol.y[0])),
            "a_max": float(np.max(sol.y[0])),
            "b_min": float(np.min(sol.y[2])),
            "b_max": float(np.max(sol.y[2])),
            "Ha_crossings": Ha_cross,
            "Hb_crossings": Hb_cross,
            "max_abs_constraint": float(np.max(np.abs(C))),
            "max_abs_continuity": float(np.max(np.abs(D))),
            "survived_full_window": bool(sol.t[-1] >= 0.98 * tmax),
        }
        results.append((rec, sol))

    if not results:
        print("No successful trajectories.")
        return []

    # summary
    total = len(results)
    surv = sum(r[0]["survived_full_window"] for r in results)
    osc = sum(r[0]["Ha_crossings"] >= 4 for r in results)
    print(f"Trajectories integrated: {total}")
    print(f"Survived full window:    {surv}")
    print(f"Oscillatory candidates:  {osc}")
    print(
        "Constraint max |C| range:",
        f"[{min(r[0]['max_abs_constraint'] for r in results):.2e},",
        f"{max(r[0]['max_abs_constraint'] for r in results):.2e}]",
    )
    print(
        "Continuity max |D| range:",
        f"[{min(r[0]['max_abs_continuity'] for r in results):.2e},",
        f"{max(r[0]['max_abs_continuity'] for r in results):.2e}]",
    )

    # store best by smallest constraint then continuity
    ranked = sorted(results, key=lambda x: (x[0]["max_abs_constraint"], x[0]["max_abs_continuity"]))
    best = ranked[0]
    rec, sol = best
    print("Best trajectory IC:", rec["ic"])
    print("Best trajectory crossings (Ha, Hb):", rec["Ha_crossings"], rec["Hb_crossings"])
    print("Best max |C|:", f"{rec['max_abs_constraint']:.2e}")
    print("Best max |D|:", f"{rec['max_abs_continuity']:.2e}")

    # plot best
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    ax[0, 0].plot(sol.t, sol.y[0], label="a(t)")
    ax[0, 0].plot(sol.t, sol.y[2], label="b(t)")
    ax[0, 0].set_title(f"{case_name}: scale factors")
    ax[0, 0].legend()

    ax[0, 1].plot(sol.y[0], sol.y[1], lw=1)
    ax[0, 1].axhline(0, ls=":", color="k", alpha=0.4)
    ax[0, 1].set_xlabel("a")
    ax[0, 1].set_ylabel("H_a")
    ax[0, 1].set_title("Phase portrait (a, H_a)")

    C = np.array([constraint_residual(sol.y[:, i], source_fn, source_params) for i in range(sol.y.shape[1])])
    D = np.array([continuity_residual(sol.y[:, i], source_fn, source_params) for i in range(sol.y.shape[1])])
    ax[1, 0].semilogy(sol.t, np.abs(C) + 1e-30, label="|constraint|")
    ax[1, 0].semilogy(sol.t, np.abs(D) + 1e-30, label="|continuity|")
    ax[1, 0].set_title("Consistency diagnostics")
    ax[1, 0].legend()

    ax[1, 1].plot(sol.y[2], sol.y[3], lw=1)
    ax[1, 1].axhline(0, ls=":", color="k", alpha=0.4)
    ax[1, 1].set_xlabel("b")
    ax[1, 1].set_ylabel("H_b")
    ax[1, 1].set_title("Phase portrait (b, H_b)")

    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, f"T3A_full5d_{case_name.replace(' ', '_')}.png")
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print("Saved:", fig_path)

    # save summary json
    js = [r[0] for r in ranked]
    js_path = os.path.join(OUTPUT_DIR, f"T3A_full5d_{case_name.replace(' ', '_')}.json")
    with open(js_path, "w") as f:
        json.dump(js, f, indent=2)
    print("Saved:", js_path)

    return ranked


def build_init_grid():
    grid = []
    for a0 in [0.6, 1.0, 1.5, 2.0]:
        for Ha0 in [0.1, 0.3, 0.6, 1.0]:
            for b0 in [0.6, 1.0, 1.5, 2.0]:
                grid.append((a0, Ha0, b0))
    return grid


if __name__ == "__main__":
    grid = build_init_grid()

    # 1) Vacuum lambda sanity
    run_case(
        "vacuum_lambda",
        source_vacuum_lambda,
        {"Lambda": 2.0},
        grid,
        tmax=20.0,
    )

    # 2) Isotropic Casimir source
    run_case(
        "casimir_isotropic",
        source_casimir_isotropic,
        {"alpha": 5.0},
        grid,
        tmax=40.0,
    )

    # 3) Anisotropic, conservation-closed source
    run_case(
        "casimir_aniso_closed_wphi_pos",
        source_casimir_aniso_conservation_closed,
        {"alpha": 5.0, "wphi": 0.5},
        grid,
        tmax=40.0,
    )

