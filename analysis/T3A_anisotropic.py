#!/usr/bin/env python3
"""
T3-A Anisotropic Extension: Finding the Oscillatory Regime
==========================================================
Key insight: y = a² satisfies ÿ = -(2w_φ·Λ_eff/3)·y - 2
  - w_φ < 0 (isotropic approx): saddle, no oscillation
  - w_φ > 0 (physical Casimir): center-type, oscillation POSSIBLE

Full anisotropic system:
  ȧ  = a·H_a
  Ḣ_a = -2H_a² - 1/a² - w_φ·Λ(b)/3
  ḃ  = b·H_b
  Ḣ_b = Λ(b)·(1/3 + 2w_φ/3 - w₃) - H_b² - 3H_aH_b

  Constraint: 3H_a² + 3/a² + 3H_aH_b = Λ(b)
  Λ(b) = α/b⁴
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import json

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def aniso_ode(t, state, alpha, w_phi, w_3):
    a, Ha, b, Hb = state
    if a < 1e-10 or b < 1e-10:
        return [0, 0, 0, 0]
    L = alpha / b**4
    da = a * Ha
    dHa = -2*Ha**2 - 1.0/a**2 - w_phi*L/3.0
    db = b * Hb
    coeff_b = 1.0/3 + 2*w_phi/3 - w_3
    dHb = coeff_b*L - Hb**2 - 3*Ha*Hb
    return [da, dHa, db, dHb]

def init_state(a0, Ha0, b0, alpha):
    if abs(Ha0) < 1e-15:
        return None
    L = alpha / b0**4
    Hb0 = (L - 3*Ha0**2 - 3.0/a0**2) / (3*Ha0)
    return np.array([a0, Ha0, b0, Hb0])

def constraint_res(state, alpha):
    a, Ha, b, Hb = state
    return 3*Ha**2 + 3.0/a**2 + 3*Ha*Hb - alpha/b**4

def count_oscillations(Ha_array):
    """Count zero-crossings of H_a"""
    signs = np.sign(Ha_array)
    return np.sum(np.diff(signs) != 0)

# ============================================================
# SCAN 1: w_phi dependence at fixed geometry
# ============================================================
def scan_w_phi():
    print("=" * 60)
    print("SCAN 1: w_φ dependence (α=1, trace condition w₃=(1-w_φ)/3)")
    print("=" * 60)

    alpha = 1.0
    w_phi_range = np.linspace(-1.5, 3.0, 50)
    T_max = 80

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Effect of w_φ on S³ dynamics (α=1)', fontsize=14)

    best_osc = {'w_phi': None, 'n_osc': 0, 'state': None}

    for a0 in [1.0, 1.5]:
        for Ha0 in [0.3, 0.5, 1.0]:
            for b0 in [1.0, 1.5, 2.0]:
                osc_counts = []
                a_survived = []

                for w_phi in w_phi_range:
                    w_3 = (1 - w_phi) / 3  # trace condition
                    s0 = init_state(a0, Ha0, b0, alpha)
                    if s0 is None or abs(s0[3]) > 30:
                        osc_counts.append(0)
                        a_survived.append(False)
                        continue

                    def stop_a(t, s, *args):
                        return s[0] - 1e-6
                    stop_a.terminal = True
                    stop_a.direction = -1

                    def stop_b(t, s, *args):
                        return s[2] - 1e-6
                    stop_b.terminal = True
                    stop_b.direction = -1

                    try:
                        sol = solve_ivp(
                            aniso_ode, [0, T_max], s0,
                            args=(alpha, w_phi, w_3),
                            method='RK45', max_step=0.05,
                            rtol=1e-10, atol=1e-12,
                            events=[stop_a, stop_b]
                        )
                        if len(sol.t) < 50:
                            osc_counts.append(0)
                            a_survived.append(False)
                            continue

                        n_osc = count_oscillations(sol.y[1])
                        survived = sol.t[-1] > 0.9 * T_max
                        osc_counts.append(n_osc)
                        a_survived.append(survived)

                        if n_osc > best_osc['n_osc']:
                            best_osc = {
                                'w_phi': w_phi, 'n_osc': n_osc,
                                'a0': a0, 'Ha0': Ha0, 'b0': b0,
                                'w_3': w_3,
                                'state': s0.copy()
                            }
                    except:
                        osc_counts.append(0)
                        a_survived.append(False)

                osc_arr = np.array(osc_counts)
                surv_arr = np.array(a_survived)

                label = f'a₀={a0},Ha₀={Ha0},b₀={b0}'
                axes[0, 0].plot(w_phi_range, osc_arr, '-', lw=0.8,
                                alpha=0.6, label=label if Ha0 == 0.5 else None)

                # Mark survived (didn't collapse)
                mask = surv_arr & (osc_arr > 0)
                if np.any(mask):
                    axes[0, 1].scatter(w_phi_range[mask], osc_arr[mask],
                                       s=10, alpha=0.5)

    axes[0, 0].set_xlabel('w_φ')
    axes[0, 0].set_ylabel('# H_a zero-crossings')
    axes[0, 0].set_title('Oscillation count vs w_φ')
    axes[0, 0].axvline(0, color='red', ls='--', lw=2, label='w_φ = 0 boundary')
    axes[0, 0].axvline(-1, color='gray', ls=':', label='Isotropic (w_φ=-1)')
    axes[0, 0].legend(fontsize=8)

    axes[0, 1].set_xlabel('w_φ')
    axes[0, 1].set_ylabel('# oscillations (survived only)')
    axes[0, 1].set_title('Survived trajectories with oscillation')

    # Plot best oscillatory case
    if best_osc['w_phi'] is not None:
        w_phi = best_osc['w_phi']
        w_3 = best_osc['w_3']
        s0 = best_osc['state']
        print(f"\n  Best: w_φ={w_phi:.3f}, {best_osc['n_osc']} oscillations")
        print(f"         a₀={best_osc['a0']}, Ha₀={best_osc['Ha0']}, "
              f"b₀={best_osc['b0']}, Hb₀={s0[3]:.4f}")

        sol = solve_ivp(
            aniso_ode, [0, 200], s0,
            args=(alpha, w_phi, w_3),
            method='RK45', max_step=0.02,
            rtol=1e-11, atol=1e-13
        )

        axes[1, 0].plot(sol.t, sol.y[0], 'b-', lw=1, label='a(t)')
        axes[1, 0].plot(sol.t, sol.y[2], 'r-', lw=1, label='b(t)')
        axes[1, 0].set_xlabel('t')
        axes[1, 0].set_ylabel('Scale factors')
        axes[1, 0].set_title(f'Best trajectory (w_φ={w_phi:.3f})')
        axes[1, 0].legend()

        axes[1, 1].plot(sol.y[0], sol.y[1], 'b-', lw=0.6)
        axes[1, 1].set_xlabel('a')
        axes[1, 1].set_ylabel('H_a')
        axes[1, 1].set_title('Phase portrait (a, H_a)')
        axes[1, 1].axhline(0, color='k', ls=':', alpha=0.3)

        # Constraint check
        C = constraint_res(sol.y, alpha)
        print(f"  Constraint: max|C| = {np.max(np.abs(C)):.2e}")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    path = os.path.join(OUTPUT_DIR, 'T3A_aniso_w_phi_scan.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}\n")

    return best_osc

# ============================================================
# SCAN 2: Periodic orbit search in oscillatory regime
# ============================================================
def periodic_orbit_search(w_phi_target, w_3_target):
    print("=" * 60)
    print(f"SCAN 2: Periodic orbit search at w_φ={w_phi_target:.3f}")
    print("=" * 60)

    candidates = []
    alpha_scan = np.logspace(-1, 2, 20)
    T_max = 150

    for alpha in alpha_scan:
        for a0 in [0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0]:
            for Ha0 in [0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0]:
                for b0 in [0.5, 0.7, 1.0, 1.5, 2.0, 3.0]:
                    s0 = init_state(a0, Ha0, b0, alpha)
                    if s0 is None or abs(s0[3]) > 30:
                        continue

                    def stop_a(t, s, *args):
                        return s[0] - 1e-6
                    stop_a.terminal = True
                    stop_a.direction = -1

                    def stop_b(t, s, *args):
                        return s[2] - 1e-6
                    stop_b.terminal = True
                    stop_b.direction = -1

                    def Ha_up(t, s, *args):
                        return s[1]
                    Ha_up.direction = 1

                    try:
                        sol = solve_ivp(
                            aniso_ode, [0, T_max], s0,
                            args=(alpha, w_phi_target, w_3_target),
                            method='RK45', max_step=0.1,
                            rtol=1e-9, atol=1e-11,
                            events=[stop_a, stop_b, Ha_up]
                        )

                        if sol.t_events is None or len(sol.t_events) < 3:
                            continue
                        xings = sol.t_events[2]
                        if len(xings) < 3:
                            continue

                        # Get states at crossings
                        states = []
                        for tc in xings:
                            idx = np.argmin(np.abs(sol.t - tc))
                            states.append(sol.y[:, idx].copy())

                        for j in range(1, len(states)):
                            sr = states[0]
                            sj = states[j]
                            da = abs(sj[0]-sr[0]) / max(abs(sr[0]), 1e-10)
                            db = abs(sj[2]-sr[2]) / max(abs(sr[2]), 1e-10)
                            dHb = abs(sj[3]-sr[3]) / max(abs(sr[3]), 1e-10)

                            if da < 0.01 and db < 0.01:
                                T = xings[j] - xings[0]
                                if T > 0.5:
                                    candidates.append({
                                        'alpha': float(alpha),
                                        'a0': a0, 'Ha0': Ha0, 'b0': b0,
                                        'Hb0': float(s0[3]),
                                        'period': float(T),
                                        'da': float(da), 'db': float(db),
                                        'a_min': float(sol.y[0].min()),
                                        'a_max': float(sol.y[0].max()),
                                        'b_min': float(sol.y[2].min()),
                                        'b_max': float(sol.y[2].max()),
                                    })
                                    break
                    except:
                        continue

    print(f"\n  Candidates: {len(candidates)}")
    if candidates:
        candidates.sort(key=lambda r: r['da'] + r['db'])
        print(f"\n  Top 15:")
        print(f"  {'α':>8s} {'a₀':>5s} {'b₀':>5s} {'T':>8s} "
              f"{'δa':>8s} {'δb':>8s} {'a_range':>14s} {'b_range':>14s}")
        for r in candidates[:15]:
            print(f"  {r['alpha']:8.3f} {r['a0']:5.1f} {r['b0']:5.1f} "
                  f"{r['period']:8.3f} {r['da']:8.5f} {r['db']:8.5f} "
                  f"[{r['a_min']:.3f},{r['a_max']:.3f}] "
                  f"[{r['b_min']:.3f},{r['b_max']:.3f}]")

        # Plot best
        r = candidates[0]
        s0 = init_state(r['a0'], r['Ha0'], r['b0'], r['alpha'])
        sol = solve_ivp(
            aniso_ode, [0, 5*r['period']], s0,
            args=(r['alpha'], w_phi_target, w_3_target),
            method='RK45', max_step=0.01,
            rtol=1e-11, atol=1e-13
        )

        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle(
            f'SCF Periodic Orbit: α={r["alpha"]:.3f}, w_φ={w_phi_target:.2f}, '
            f'T≈{r["period"]:.3f}\n'
            f'a₀={r["a0"]}, b₀={r["b0"]}, Ha₀={r["Ha0"]}',
            fontsize=13)

        axes[0,0].plot(sol.t, sol.y[0], 'b-', lw=1.2)
        axes[0,0].set_xlabel('t'); axes[0,0].set_ylabel('a(t)')
        for k in range(6):
            axes[0,0].axvline(k*r['period'], color='gray', ls=':', alpha=0.3)

        axes[0,1].plot(sol.t, sol.y[2], 'r-', lw=1.2)
        axes[0,1].set_xlabel('t'); axes[0,1].set_ylabel('b(t)')

        axes[1,0].plot(sol.y[0], sol.y[1], 'b-', lw=0.6)
        axes[1,0].set_xlabel('a'); axes[1,0].set_ylabel('H_a')
        axes[1,0].axhline(0, color='k', ls=':', alpha=0.3)

        axes[1,1].plot(sol.y[2], sol.y[3], 'r-', lw=0.6)
        axes[1,1].set_xlabel('b'); axes[1,1].set_ylabel('H_b')
        axes[1,1].axhline(0, color='k', ls=':', alpha=0.3)

        # Constraint
        C = constraint_res(sol.y, r['alpha'])
        axes[0,2].semilogy(sol.t, np.abs(C)+1e-16, 'k-', lw=0.5)
        axes[0,2].set_xlabel('t'); axes[0,2].set_ylabel('|Constraint|')

        # (a, b) joint trajectory
        axes[1,2].plot(sol.y[0], sol.y[2], 'purple', lw=0.6)
        axes[1,2].set_xlabel('a'); axes[1,2].set_ylabel('b')
        axes[1,2].set_title('Joint (a,b) trajectory')

        plt.tight_layout(rect=[0,0,1,0.93])
        path = os.path.join(OUTPUT_DIR, 'T3A_periodic_orbit_aniso.png')
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"\n  Saved: {path}")

        rpath = os.path.join(OUTPUT_DIR, 'T3A_aniso_candidates.json')
        with open(rpath, 'w') as f:
            json.dump(candidates[:50], f, indent=2)
        print(f"  Saved: {rpath}")

    return candidates

# ============================================================
# SCAN 3: w_phi and alpha 2D scan for oscillation map
# ============================================================
def oscillation_map():
    print("\n" + "=" * 60)
    print("SCAN 3: 2D Oscillation Map (w_φ × α)")
    print("=" * 60)

    w_phi_range = np.linspace(-0.5, 3.0, 40)
    alpha_range = np.logspace(-1, 2, 30)
    T_max = 60

    osc_map = np.zeros((len(w_phi_range), len(alpha_range)))
    a0, Ha0, b0 = 1.0, 0.5, 1.0

    for i, w_phi in enumerate(w_phi_range):
        w_3 = (1 - w_phi) / 3
        for j, alpha in enumerate(alpha_range):
            s0 = init_state(a0, Ha0, b0, alpha)
            if s0 is None or abs(s0[3]) > 30:
                continue
            try:
                def stop(t, s, *args):
                    return s[0] - 1e-6
                stop.terminal = True
                stop.direction = -1

                sol = solve_ivp(
                    aniso_ode, [0, T_max], s0,
                    args=(alpha, w_phi, w_3),
                    method='RK45', max_step=0.1,
                    rtol=1e-8, atol=1e-10,
                    events=[stop]
                )
                if len(sol.t) > 20:
                    osc_map[i, j] = count_oscillations(sol.y[1])
            except:
                pass

    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.pcolormesh(alpha_range, w_phi_range, osc_map,
                        cmap='hot', shading='auto')
    ax.set_xscale('log')
    ax.set_xlabel('α (Casimir coupling)')
    ax.set_ylabel('w_φ (KK pressure / energy)')
    ax.set_title('Oscillation Map: # H_a zero-crossings in t∈[0,60]')
    ax.axhline(0, color='cyan', ls='--', lw=2, label='w_φ = 0')
    ax.axhline(-1, color='white', ls=':', lw=1, label='Isotropic (w_φ=-1)')
    ax.legend(fontsize=10, loc='upper left')
    plt.colorbar(im, label='# oscillations')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'T3A_oscillation_map.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")

    # Report
    max_osc = osc_map.max()
    if max_osc > 0:
        idx = np.unravel_index(np.argmax(osc_map), osc_map.shape)
        print(f"  Max oscillations: {int(max_osc)} at "
              f"w_φ={w_phi_range[idx[0]]:.3f}, α={alpha_range[idx[1]]:.3f}")
        print(f"  Oscillation regime: w_φ > {w_phi_range[np.min(np.where(osc_map.max(axis=1)>0))]:.2f}")
    else:
        print("  NO oscillation found in scanned range")

if __name__ == '__main__':
    print("T3-A Anisotropic Extension")
    print("=" * 60)

    # Step 1: Find which w_phi values produce oscillation
    best = scan_w_phi()

    # Step 2: Build 2D oscillation map
    oscillation_map()

    # Step 3: If oscillation found, search for periodic orbits
    if best['w_phi'] is not None and best['n_osc'] > 2:
        w_phi_opt = best['w_phi']
        w_3_opt = (1 - w_phi_opt) / 3
        candidates = periodic_orbit_search(w_phi_opt, w_3_opt)
    else:
        print("\nNo oscillatory regime found. The trace-condition-constrained")
        print("anisotropic system may require additional physics (Path 5/6).")

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
