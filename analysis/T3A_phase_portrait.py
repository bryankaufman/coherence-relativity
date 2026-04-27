#!/usr/bin/env python3
"""
T3-A: Phase Portrait Analysis for SCF Periodic Orbits
=====================================================
5D Einstein equations on S¹_t × S³ × S¹_φ
Metric: ds² = -dt² + a(t)²dΩ₃² + b(t)²dφ²
Curvature: k = +1 (round S³)

Key analytical result (vacuum no-go):
  y = a² linearizes to ÿ = (2Λ₅/3)y - 2
  No periodic orbits exist for any constant Λ₅.
  
This script explores the Casimir-sourced system Λ₅(b) = α/b⁴
to determine whether the b-dependence enables periodic SCF solutions.

System (isotropic Casimir approximation):
  ȧ  = a·H_a
  Ḣ_a = Λ₅(b)/3 - 2H_a² - 1/a²
  ḃ  = b·H_b
  Ḣ_b = 2Λ₅(b)/3 - H_b² - 3H_aH_b
  
  Constraint: 3H_a² + 3/a² + 3H_aH_b = Λ₅(b)
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import json

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# PART A: Vacuum Validation
# ============================================================

def vacuum_y_exact(t, y0, ydot0, L5):
    """Exact solution of ÿ = (2Λ₅/3)y - 2"""
    omega_sq = 2*L5/3
    if L5 > 0:
        omega = np.sqrt(omega_sq)
        y_eq = 3.0/L5
        A = ((y0 - y_eq) + ydot0/omega)/2
        B = ((y0 - y_eq) - ydot0/omega)/2
        return A*np.exp(omega*t) + B*np.exp(-omega*t) + y_eq
    elif L5 < 0:
        omega = np.sqrt(-omega_sq)
        y_eq = 3.0/L5  # negative
        C = y0 - y_eq
        D = ydot0/omega
        return C*np.cos(omega*t) + D*np.sin(omega*t) + y_eq
    else:
        return -t**2 + ydot0*t + y0

def vacuum_ode(t, state, L5):
    a, Ha, b, Hb = state
    if a < 1e-12:
        return [0, 0, 0, 0]
    da = a * Ha
    dHa = L5/3.0 - 2*Ha**2 - 1.0/a**2
    db = b * Hb
    dHb = 2*L5/3.0 - Hb**2 - 3*Ha*Hb
    return [da, dHa, db, dHb]

def run_vacuum_validation():
    print("=" * 60)
    print("PART A: Vacuum Case — y = a² Linearization Validation")
    print("=" * 60)

    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('Vacuum No-Go: y = a² dynamics for constant Λ₅', fontsize=14)

    cases = [(2.0, 'Λ₅ = +2 (de Sitter)'), (-2.0, 'Λ₅ = −2 (AdS)'), (0.0, 'Λ₅ = 0')]
    a0, Ha0, b0 = 1.5, 0.3, 1.0

    for idx, (L5, label) in enumerate(cases):
        y0 = a0**2
        ydot0 = 2 * a0**2 * Ha0

        # Analytical
        t_span = np.linspace(0, 8 if L5 >= 0 else 15, 2000)
        y_ana = vacuum_y_exact(t_span, y0, ydot0, L5)

        # Numerical
        if abs(Ha0) > 1e-15:
            Hb0 = (L5 - 3*Ha0**2 - 3/a0**2) / (3*Ha0) if L5 != 0 else -Ha0
        else:
            Hb0 = 0.0
        state0 = [a0, Ha0, b0, Hb0]

        def stop_a(t, s, L5):
            return s[0] - 1e-6
        stop_a.terminal = True
        stop_a.direction = -1

        try:
            sol = solve_ivp(vacuum_ode, [0, t_span[-1]], state0, args=(L5,),
                            max_step=0.005, rtol=1e-12, atol=1e-14,
                            events=[stop_a], dense_output=True)
            y_num = sol.y[0]**2

            # y(t)
            axes[0, idx].plot(t_span, y_ana, 'b-', lw=2, label='Analytical')
            axes[0, idx].plot(sol.t, y_num, 'r--', lw=1.2, label='Numerical')
            axes[0, idx].axhline(0, color='k', ls=':', alpha=0.3)
            axes[0, idx].set_xlabel('t')
            axes[0, idx].set_ylabel('y = a²')
            axes[0, idx].set_title(label)
            axes[0, idx].legend(fontsize=9)

            # Phase portrait
            axes[1, idx].plot(sol.y[0], sol.y[1], 'b-', lw=1.2)
            axes[1, idx].axhline(0, color='k', ls=':', alpha=0.3)
            axes[1, idx].set_xlabel('a')
            axes[1, idx].set_ylabel('H_a')
            axes[1, idx].set_title(f'Phase portrait ({label})')
            if L5 > 0:
                afp = np.sqrt(3/L5)
                axes[1, idx].plot(afp, 0, 'ro', ms=8, zorder=5,
                                  label=f'Saddle a*={afp:.2f}')
                axes[1, idx].legend(fontsize=9)

            # Error
            t_shared = sol.t[sol.t <= t_span[-1]]
            y_ana_at_num = vacuum_y_exact(t_shared, y0, ydot0, L5)
            y_num_shared = sol.y[0, :len(t_shared)]**2
            max_err = np.max(np.abs(y_ana_at_num - y_num_shared))
            print(f"  {label}: max |y_ana - y_num| = {max_err:.2e}")

        except Exception as e:
            print(f"  {label}: integration failed — {e}")

    # Prove y hits zero for Λ₅ < 0
    L5_neg = -2.0
    y_eq = 3.0/L5_neg
    omega = np.sqrt(-2*L5_neg/3)
    C = y0 - y_eq
    D = ydot0 / omega
    amp = np.sqrt(C**2 + D**2)
    y_min = y_eq - amp
    print(f"\n  Λ₅ < 0 proof: y_eq = {y_eq:.3f}, amplitude = {amp:.3f}, "
          f"y_min = {y_min:.3f}")
    print(f"  y_min < 0: {y_min < 0} → S³ ALWAYS collapses ✓")

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'T3A_vacuum_validation.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}\n")

# ============================================================
# PART B: Casimir-Sourced Phase Portraits
# ============================================================

def casimir_ode(t, state, alpha):
    a, Ha, b, Hb = state
    if a < 1e-10 or b < 1e-10:
        return [0, 0, 0, 0]
    L5 = alpha / b**4
    da = a * Ha
    dHa = L5/3.0 - 2*Ha**2 - 1.0/a**2
    db = b * Hb
    dHb = 2*L5/3.0 - Hb**2 - 3*Ha*Hb
    return [da, dHa, db, dHb]

def casimir_jac(t, state, alpha):
    """Jacobian for stiff integration"""
    a, Ha, b, Hb = state
    if a < 1e-10 or b < 1e-10:
        return np.zeros((4, 4))
    L5 = alpha / b**4
    dL5db = -4*alpha / b**5
    J = np.zeros((4, 4))
    # da/d(a,Ha,b,Hb)
    J[0, 0] = Ha
    J[0, 1] = a
    # dHa/d(a,Ha,b,Hb)
    J[1, 0] = 2.0 / a**3
    J[1, 1] = -4*Ha
    J[1, 2] = dL5db / 3.0
    # db/d(a,Ha,b,Hb)
    J[2, 2] = Hb
    J[2, 3] = b
    # dHb/d(a,Ha,b,Hb)
    J[3, 1] = -3*Hb
    J[3, 2] = 2*dL5db / 3.0
    J[3, 3] = -2*Hb - 3*Ha
    return J

def init_state(a0, Ha0, b0, alpha):
    """Derive Hb0 from constraint. Returns None if singular."""
    if abs(Ha0) < 1e-15:
        return None
    L5 = alpha / b0**4
    rhs = L5 - 3*Ha0**2 - 3.0/a0**2
    Hb0 = rhs / (3*Ha0)
    return np.array([a0, Ha0, b0, Hb0])

def constraint_residual(state, alpha):
    a, Ha, b, Hb = state
    return 3*Ha**2 + 3.0/a**2 + 3*Ha*Hb - alpha/b**4

def run_casimir_exploration():
    print("=" * 60)
    print("PART B: Casimir-Sourced Phase Portraits")
    print("=" * 60)

    fig = plt.figure(figsize=(18, 16))
    gs = GridSpec(4, 3, figure=fig, hspace=0.4, wspace=0.3)
    fig.suptitle('Casimir Source Λ₅(b) = α/b⁴: Phase Portraits', fontsize=14)

    alpha_list = [0.5, 5.0, 50.0]
    T_max = 100

    for col, alpha in enumerate(alpha_list):
        print(f"\n  α = {alpha}")
        ax_at = fig.add_subplot(gs[0, col])
        ax_bt = fig.add_subplot(gs[1, col])
        ax_aH = fig.add_subplot(gs[2, col])
        ax_bH = fig.add_subplot(gs[3, col])
        ax_at.set_title(f'α = {alpha}')

        trajectories = 0
        oscillatory = 0

        for a0 in [0.5, 1.0, 2.0]:
            for Ha0 in [0.1, 0.3, 0.5, 1.0, 1.5]:
                for b0 in [0.5, 1.0, 2.0, 4.0]:
                    s0 = init_state(a0, Ha0, b0, alpha)
                    if s0 is None:
                        continue
                    if abs(s0[3]) > 50:
                        continue

                    def stop_a(t, s, alpha):
                        return s[0] - 1e-6
                    stop_a.terminal = True
                    stop_a.direction = -1

                    def stop_b(t, s, alpha):
                        return s[2] - 1e-6
                    stop_b.terminal = True
                    stop_b.direction = -1

                    def stop_blowup(t, s, alpha):
                        return 1e6 - abs(s[1]) - abs(s[3])
                    stop_blowup.terminal = True

                    try:
                        sol = solve_ivp(
                            casimir_ode, [0, T_max], s0, args=(alpha,),
                            method='Radau', jac=casimir_jac,
                            max_step=0.1, rtol=1e-10, atol=1e-12,
                            events=[stop_a, stop_b, stop_blowup],
                            dense_output=True
                        )

                        if len(sol.t) < 20:
                            continue

                        a_s = sol.y[0]
                        Ha_s = sol.y[1]
                        b_s = sol.y[2]
                        Hb_s = sol.y[3]

                        # Detect oscillatory behavior
                        Ha_crossings = np.sum(np.diff(np.sign(Ha_s)) != 0)
                        Hb_crossings = np.sum(np.diff(np.sign(Hb_s)) != 0)

                        is_osc = Ha_crossings > 3
                        lw = 1.5 if is_osc else 0.3
                        c = 'red' if is_osc else 'steelblue'
                        al = 0.9 if is_osc else 0.2

                        ax_at.plot(sol.t, a_s, color=c, lw=lw, alpha=al)
                        ax_bt.plot(sol.t, b_s, color=c, lw=lw, alpha=al)
                        ax_aH.plot(a_s, Ha_s, color=c, lw=lw, alpha=al)
                        ax_bH.plot(b_s, Hb_s, color=c, lw=lw, alpha=al)

                        trajectories += 1
                        if is_osc:
                            oscillatory += 1
                            if Ha_crossings > 6:
                                print(f"    OSC: a0={a0}, Ha0={Ha0:.1f}, b0={b0}, "
                                      f"Ha_x={Ha_crossings}, Hb_x={Hb_crossings}, "
                                      f"a∈[{a_s.min():.3f},{a_s.max():.3f}], "
                                      f"b∈[{b_s.min():.3f},{b_s.max():.3f}]")
                    except:
                        continue

        print(f"  Trajectories: {trajectories}, Oscillatory: {oscillatory}")

        for ax, xl, yl in [(ax_at, 't', 'a(t)'),
                           (ax_bt, 't', 'b(t)'),
                           (ax_aH, 'a', 'H_a'),
                           (ax_bH, 'b', 'H_b')]:
            ax.set_xlabel(xl)
            ax.set_ylabel(yl)
            if 'H' in yl:
                ax.axhline(0, color='k', ls=':', alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    path = os.path.join(OUTPUT_DIR, 'T3A_casimir_exploration.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"\n  Saved: {path}\n")

# ============================================================
# PART C: Periodic Orbit Search
# ============================================================

def run_periodic_orbit_search():
    print("=" * 60)
    print("PART C: Systematic Periodic Orbit Search")
    print("=" * 60)

    candidates = []

    alpha_scan = np.logspace(-1, 3, 40)
    a0_scan = [0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]
    Ha0_scan = [0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0]
    b0_scan = [0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]

    total_trials = 0
    T_max = 300

    for alpha in alpha_scan:
        for a0 in a0_scan:
            for Ha0 in Ha0_scan:
                for b0 in b0_scan:
                    s0 = init_state(a0, Ha0, b0, alpha)
                    if s0 is None:
                        continue
                    if abs(s0[3]) > 50 or s0[3] != s0[3]:
                        continue

                    total_trials += 1

                    def stop_a(t, s, alpha):
                        return s[0] - 1e-6
                    stop_a.terminal = True
                    stop_a.direction = -1

                    def stop_b(t, s, alpha):
                        return s[2] - 1e-6
                    stop_b.terminal = True
                    stop_b.direction = -1

                    # Poincare section: Ha = 0 crossing upward
                    def Ha_section(t, s, alpha):
                        return s[1]
                    Ha_section.direction = 1

                    try:
                        sol = solve_ivp(
                            casimir_ode, [0, T_max], s0, args=(alpha,),
                            method='Radau', jac=casimir_jac,
                            max_step=0.2, rtol=1e-9, atol=1e-11,
                            events=[stop_a, stop_b, Ha_section]
                        )

                        # Get Poincare section crossings
                        if sol.t_events is None or len(sol.t_events) < 3:
                            continue
                        crossings_t = sol.t_events[2]
                        if len(crossings_t) < 3:
                            continue

                        # Get state at each crossing via interpolation
                        cross_states = []
                        for tc in crossings_t:
                            idx = np.argmin(np.abs(sol.t - tc))
                            cross_states.append(sol.y[:, idx].copy())

                        # Check for return: compare each crossing to the first
                        for j in range(1, len(cross_states)):
                            s_ref = cross_states[0]
                            s_j = cross_states[j]

                            # Relative differences
                            da = abs(s_j[0] - s_ref[0]) / max(abs(s_ref[0]), 1e-10)
                            db = abs(s_j[2] - s_ref[2]) / max(abs(s_ref[2]), 1e-10)
                            dHb = abs(s_j[3] - s_ref[3]) / max(abs(s_ref[3]), 1e-10)

                            if da < 0.02 and db < 0.02 and dHb < 0.05:
                                period = crossings_t[j] - crossings_t[0]
                                if period > 0.1:
                                    # Check constraint preservation
                                    C_init = abs(constraint_residual(s0, alpha))
                                    C_end = abs(constraint_residual(sol.y[:, -1], alpha))

                                    candidates.append({
                                        'alpha': float(alpha),
                                        'a0': a0, 'Ha0': Ha0, 'b0': b0,
                                        'Hb0': float(s0[3]),
                                        'period': float(period),
                                        'delta_a': float(da),
                                        'delta_b': float(db),
                                        'delta_Hb': float(dHb),
                                        'a_min': float(sol.y[0].min()),
                                        'a_max': float(sol.y[0].max()),
                                        'b_min': float(sol.y[2].min()),
                                        'b_max': float(sol.y[2].max()),
                                        'constraint_init': float(C_init),
                                        'constraint_end': float(C_end),
                                        'n_crossings': len(crossings_t),
                                    })
                                    break  # Found match for this IC
                    except:
                        continue

    print(f"\n  Total trials: {total_trials}")
    print(f"  Candidates found: {len(candidates)}")

    if candidates:
        # Sort by quality
        candidates.sort(key=lambda r: r['delta_a'] + r['delta_b'])

        print("\n  Top 15 candidates:")
        print(f"  {'α':>8s} {'a₀':>5s} {'b₀':>5s} {'T':>8s} "
              f"{'δa':>8s} {'δb':>8s} {'a_range':>14s} {'b_range':>14s}")
        for r in candidates[:15]:
            print(f"  {r['alpha']:8.3f} {r['a0']:5.1f} {r['b0']:5.1f} "
                  f"{r['period']:8.3f} {r['delta_a']:8.5f} {r['delta_b']:8.5f} "
                  f"[{r['a_min']:.3f},{r['a_max']:.3f}] "
                  f"[{r['b_min']:.3f},{r['b_max']:.3f}]")

        # Plot best candidate
        r = candidates[0]
        s0 = init_state(r['a0'], r['Ha0'], r['b0'], r['alpha'])
        sol = solve_ivp(
            casimir_ode, [0, 4*r['period']], s0, args=(r['alpha'],),
            method='Radau', jac=casimir_jac,
            max_step=0.01, rtol=1e-11, atol=1e-13,
            dense_output=True
        )

        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle(
            f'Best Periodic Orbit: α={r["alpha"]:.3f}, T≈{r["period"]:.3f}\n'
            f'a₀={r["a0"]}, b₀={r["b0"]}, H_a0={r["Ha0"]}, H_b0={r["Hb0"]:.4f}',
            fontsize=13)

        # a(t), b(t)
        axes[0, 0].plot(sol.t, sol.y[0], 'b-', lw=1.2)
        axes[0, 0].set_xlabel('t'); axes[0, 0].set_ylabel('a(t)')
        for k in range(4):
            axes[0, 0].axvline(k*r['period'], color='gray', ls=':', alpha=0.3)

        axes[0, 1].plot(sol.t, sol.y[2], 'r-', lw=1.2)
        axes[0, 1].set_xlabel('t'); axes[0, 1].set_ylabel('b(t)')

        # Phase portraits
        axes[1, 0].plot(sol.y[0], sol.y[1], 'b-', lw=0.8)
        axes[1, 0].set_xlabel('a'); axes[1, 0].set_ylabel('H_a')
        axes[1, 0].axhline(0, color='k', ls=':', alpha=0.3)

        axes[1, 1].plot(sol.y[2], sol.y[3], 'r-', lw=0.8)
        axes[1, 1].set_xlabel('b'); axes[1, 1].set_ylabel('H_b')
        axes[1, 1].axhline(0, color='k', ls=':', alpha=0.3)

        # Constraint preservation
        L5_t = r['alpha'] / sol.y[2]**4
        C_t = 3*sol.y[1]**2 + 3/sol.y[0]**2 + 3*sol.y[1]*sol.y[3] - L5_t
        axes[0, 2].semilogy(sol.t, np.abs(C_t) + 1e-16, 'k-', lw=0.5)
        axes[0, 2].set_xlabel('t'); axes[0, 2].set_ylabel('|Constraint residual|')

        # y = a² to check against linearization
        y_t = sol.y[0]**2
        ydot = np.gradient(y_t, sol.t)
        yddot_num = np.gradient(ydot, sol.t)
        yddot_ana = (2*L5_t/3)*y_t - 2
        axes[1, 2].plot(sol.t, yddot_num, 'b-', lw=0.8, label='ÿ (numerical)')
        axes[1, 2].plot(sol.t, yddot_ana, 'r--', lw=0.8, label='(2Λ₅/3)y − 2')
        axes[1, 2].set_xlabel('t'); axes[1, 2].set_ylabel('ÿ')
        axes[1, 2].legend(fontsize=9)

        plt.tight_layout(rect=[0, 0, 1, 0.93])
        path = os.path.join(OUTPUT_DIR, 'T3A_periodic_orbit.png')
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"\n  Saved: {path}")

        # Save results
        results_path = os.path.join(OUTPUT_DIR, 'T3A_candidates.json')
        with open(results_path, 'w') as f:
            json.dump(candidates[:50], f, indent=2)
        print(f"  Saved: {results_path}")

    else:
        print("\n  NO PERIODIC ORBIT CANDIDATES found in scan range.")
        print("  Implications:")
        print("    1. Scan range may be insufficient — expand α, a₀, b₀")
        print("    2. Isotropic Casimir approx may be too restrictive")
        print("    3. Anisotropic stress tensor (p₃ ≠ p_φ) may be required")
        print("    4. Periodic orbits may genuinely not exist (critical finding)")

    return candidates

# ============================================================
# PART D: Negative-α Exploration (SUSY-like, Λ₅ < 0)
# ============================================================

def run_negative_alpha_exploration():
    """Explore α < 0 (net negative Casimir), which gives Λ₅ < 0"""
    print("\n" + "=" * 60)
    print("PART D: Negative-α Exploration (Λ₅ < 0)")
    print("=" * 60)

    candidates = []
    alpha_scan = -np.logspace(-1, 3, 30)
    T_max = 300

    for alpha in alpha_scan:
        for a0 in [0.5, 1.0, 2.0, 5.0]:
            for Ha0 in [0.1, 0.3, 0.5, 1.0, 2.0]:
                for b0 in [0.5, 1.0, 2.0, 5.0]:
                    s0 = init_state(a0, Ha0, b0, alpha)
                    if s0 is None:
                        continue
                    if abs(s0[3]) > 50 or s0[3] != s0[3]:
                        continue

                    def stop_a(t, s, alpha):
                        return s[0] - 1e-6
                    stop_a.terminal = True
                    stop_a.direction = -1

                    def stop_b(t, s, alpha):
                        return s[2] - 1e-6
                    stop_b.terminal = True
                    stop_b.direction = -1

                    def Ha_sect(t, s, alpha):
                        return s[1]
                    Ha_sect.direction = 1

                    try:
                        sol = solve_ivp(
                            casimir_ode, [0, T_max], s0, args=(alpha,),
                            method='Radau', jac=casimir_jac,
                            max_step=0.2, rtol=1e-9, atol=1e-11,
                            events=[stop_a, stop_b, Ha_sect]
                        )

                        if sol.t_events is None or len(sol.t_events) < 3:
                            continue
                        crossings_t = sol.t_events[2]
                        if len(crossings_t) < 3:
                            continue

                        cross_states = []
                        for tc in crossings_t:
                            idx = np.argmin(np.abs(sol.t - tc))
                            cross_states.append(sol.y[:, idx].copy())

                        for j in range(1, len(cross_states)):
                            s_ref = cross_states[0]
                            s_j = cross_states[j]
                            da = abs(s_j[0] - s_ref[0]) / max(abs(s_ref[0]), 1e-10)
                            db = abs(s_j[2] - s_ref[2]) / max(abs(s_ref[2]), 1e-10)
                            if da < 0.02 and db < 0.02:
                                period = crossings_t[j] - crossings_t[0]
                                if period > 0.1:
                                    candidates.append({
                                        'alpha': float(alpha),
                                        'a0': a0, 'Ha0': Ha0, 'b0': b0,
                                        'period': float(period),
                                        'delta_a': float(da),
                                        'delta_b': float(db),
                                        'a_min': float(sol.y[0].min()),
                                        'a_max': float(sol.y[0].max()),
                                        'b_min': float(sol.y[2].min()),
                                        'b_max': float(sol.y[2].max()),
                                    })
                                    break
                    except:
                        continue

    print(f"  Negative-α candidates: {len(candidates)}")
    if candidates:
        candidates.sort(key=lambda r: r['delta_a'] + r['delta_b'])
        for r in candidates[:10]:
            print(f"    α={r['alpha']:.3f}, T≈{r['period']:.3f}, "
                  f"a∈[{r['a_min']:.3f},{r['a_max']:.3f}], "
                  f"b∈[{r['b_min']:.3f},{r['b_max']:.3f}]")
    return candidates

# ============================================================
# Main
# ============================================================

if __name__ == '__main__':
    print("T3-A: SCF Phase Portrait Analysis")
    print("Coherence-Relativity Project — Paper 2")
    print("=" * 60)

    run_vacuum_validation()
    run_casimir_exploration()
    pos_candidates = run_periodic_orbit_search()
    neg_candidates = run_negative_alpha_exploration()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Vacuum no-go: PROVEN (y = a² linearization)")
    print(f"  Positive-α candidates: {len(pos_candidates)}")
    print(f"  Negative-α candidates: {len(neg_candidates)}")

    if len(pos_candidates) == 0 and len(neg_candidates) == 0:
        print("\n  ⚠ NO PERIODIC ORBITS FOUND IN SCANNED RANGE")
        print("  This is a PRELIMINARY negative result.")
        print("  Before concluding the model lacks SCF solutions:")
        print("    1. Expand parameter scan (wider α, finer grid)")
        print("    2. Try anisotropic Casimir stress tensor")
        print("    3. Include temporal-circle Casimir contribution")
        print("    4. Check whether KK-Casimir cross terms stabilize")
    elif pos_candidates or neg_candidates:
        print("\n  ✓ PERIODIC ORBIT CANDIDATES FOUND")
        print("  Next steps:")
        print("    1. Refine with Newton-Raphson shooting method")
        print("    2. Check stability (Floquet multipliers)")
        print("    3. Compute time-averaged ⟨b⟩ and compare to r*")

    print("\n  Analysis complete.")
