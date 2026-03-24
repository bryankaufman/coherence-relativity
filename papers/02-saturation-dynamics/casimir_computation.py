"""
Casimir energy density on S¹ Hopf fiber — SC3 branch-screening computation
Context: paper2_mathematical_spine_2026-02-28.md §3.6 and §3.7

Tasks:
  1. Symbolic ρ_Casimir(N_B, N_F, r) via zeta-function regularization
  2. Branch 3 evaluation: N_B=2 photon polarizations, N_F=0, periodic BCs
  3. Minimum N_F for sign-positivity given N_B=2
  4. Numerical sweep vs Λ_obs; required r_fiber for SC3 closure
  5. Multi-sector branch-screening table (FAIL / MARGINAL / PASS)

Sign/convention locking (Step A of §3.7):
  - (+,-,-,-,-) signature; Euclidean continuation for vacuum sum
  - Periodic BCs on bosons → negative Casimir density (Scherk-Schwarz phase = 0)
  - Antiperiodic BCs on fermions → positive contribution (phase = 1/2)
  - Renormalization: zeta-function regularization, no normal-ordering subtraction
  - Mapping: Λ_eff = 8πG₄ ρ_Casimir  [SI: Λ in m⁻², ρ in J/m³]
"""

import sympy as sp
from sympy import pi, Rational, sqrt, symbols, simplify, Eq, solve, latex
import numpy as np

# ── Physical constants (CODATA 2018) ──────────────────────────────────────────
hbar   = 1.054571817e-34   # J·s
c      = 2.99792458e8      # m/s
G4     = 6.67430e-11       # m³ kg⁻¹ s⁻²
ell_P  = 1.616255e-35      # m  (Planck length)
Lambda_obs = 1.1e-52       # m⁻²  (observed cosmological constant)

# Energy density corresponding to Λ_obs  [J/m³]
rho_obs_target = Lambda_obs * c**4 / (8 * np.pi * G4)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. SYMBOLIC FORMULA — derivation sketch + closed form
# ═══════════════════════════════════════════════════════════════════════════════

N_B, N_F, r = symbols('N_B N_F r', positive=True, real=True)

# Standard result (Dowker & Critchley 1976; Candelas & Raine 1976):
# Massless fields on R^{3,1} × S¹ (radius r, circumference L = 2πr).
# Zeta-function sum over KK tower gives:
#
#   ρ_boson   = −π²/(90 r⁴)  per real bosonic d.o.f. (periodic BCs)
#   ρ_fermion = +7π²/(720 r⁴) per fermionic d.o.f.   (antiperiodic BCs)
#             = +(7/8) × π²/(90 r⁴)
#
# Combined (ℏ = c = 1 natural units):
#   ρ_Casimir = π²/(90 r⁴) × (7 N_F/8 − N_B)

rho_sym = (pi**2 / (90 * r**4)) * (Rational(7, 8) * N_F - N_B)

# SC3 positivity condition
SC3_condition = Rational(7, 8) * N_F - N_B  # must be > 0

# Minimum N_F (real) for positivity given N_B
N_F_min_sym = solve(Eq(SC3_condition, 0), N_F)[0]  # = 8 N_B / 7


# ═══════════════════════════════════════════════════════════════════════════════
# 2. BRANCH-SCREENING TABLE  (§3.7 Step B + Step C)
# Each entry: label, N_B, N_F, BC_note, integer_N_F_min, verdict
# ═══════════════════════════════════════════════════════════════════════════════

def sc3_factor(nb, nf):
    """Dimensionless factor (7 nf/8 - nb); sign determines SC3 verdict."""
    return 7 * nf / 8 - nb

def verdict(nb, nf, margin=0.05):
    f = sc3_factor(nb, nf)
    if f > margin:
        return "PASS (provisional)"
    elif f >= -margin:
        return "MARGINAL"
    else:
        return "FAIL"

sectors = [
    # (label,                          N_B, N_F, BC note)
    ("Branch 3: 2 photon polz, no fermions",     2,   0, "periodic bosons only"),
    ("SM photon + graviton (2+2, no fermions)",  4,   0, "periodic bosons"),
    ("1 boson + 1 Weyl fermion",                 1,   1, "mixed"),
    ("2 bosons + 3 Weyl fermions",               2,   3, "mixed — min integer N_F for N_B=2"),
    ("2 bosons + 4 Weyl fermions",               2,   4, "mixed — comfortable margin"),
    ("Pure fermion sector N_F=4",                0,   4, "antiperiodic fermions only"),
    ("Gravitino sector N_B=2, N_F=2",            2,   2, "SUSY-like partial"),
    ("Full SUSY (N_B = N_F = 4)",                4,   4, "exact boson/fermion balance"),
]


# ═══════════════════════════════════════════════════════════════════════════════
# 3. NUMERICAL EVALUATION
# ═══════════════════════════════════════════════════════════════════════════════

def rho_casimir_SI(nb, nf, r_m):
    """ρ_Casimir in J/m³ for given species count and fiber radius in metres."""
    return (np.pi**2 * hbar * c) / (90 * r_m**4) * (7 * nf / 8 - nb)

def required_r_fiber(nb, nf):
    """Radius r_fiber [m] at which |ρ_Casimir| = ρ_obs_target, for given factor."""
    f = abs(sc3_factor(nb, nf))
    if f == 0:
        return float('inf')
    return ((np.pi**2 * hbar * c * f) / (90 * rho_obs_target))**0.25

# Radius grid: from ℓ_P up to sub-mm
r_values = {
    'Planck length ℓ_P': ell_P,
    '10 × ℓ_P':         10 * ell_P,
    '1 μm':              1e-6,
    '10 μm':             1e-5,
    '50 μm':             5e-5,
    '100 μm':            1e-4,
}


# ═══════════════════════════════════════════════════════════════════════════════
# 4. WRITE RESULTS
# ═══════════════════════════════════════════════════════════════════════════════

output_path = "casimir_results.txt"

with open(output_path, "w") as f:

    def out(s=""):
        print(s)
        f.write(s + "\n")

    out("═" * 78)
    out("  SC3 CASIMIR SIGN-CLOSURE — BRANCH-SCREENING COMPUTATION")
    out("  paper2_mathematical_spine_2026-02-28.md  §3.6 / §3.7")
    out("═" * 78)
    out()

    # ── Section 1: conventions ─────────────────────────────────────────────
    out("── SECTION 1: CONVENTIONS (Step A, §3.7) ──────────────────────────────────")
    out()
    out("  Geometry:    R^{3,1} × S¹(r),  circumference L = 2πr")
    out("  Signature:   (+−−−−)")
    out("  BCs:         bosons → periodic;  fermions → antiperiodic")
    out("  Regularization: zeta-function (no normal-ordering subtraction)")
    out("  Sign convention:")
    out("    ρ_Casimir > 0  ← fermion-dominated (antiperiodic contribution wins)")
    out("    ρ_Casimir < 0  ← boson-dominated  (periodic contribution wins)")
    out()
    out("  Mapping to Λ_eff:")
    out("    Λ_eff = 8πG₄ ρ_Casimir    [SI: Λ in m⁻², ρ in J/m³]")
    out()

    # ── Section 2: symbolic formula ────────────────────────────────────────
    out("── SECTION 2: SYMBOLIC FORMULA ─────────────────────────────────────────────")
    out()
    out("  Derivation route (zeta-function regularization on S¹):")
    out()
    out("  Bosons (periodic, massless scalar):")
    out("    E_vac = ½ Σ_{n∈ℤ} |n|/r = (1/r) × ζ_R(-1)  [Hurwitz/Epstein]")
    out("    After dimensional integration over R³:")
    out("    ρ_boson = −π²/(90 r⁴)  per real d.o.f.")
    out()
    out("  Fermions (antiperiodic, Weyl):")
    out("    Antiperiodic BCs introduce (−1)^n twist → alternating sum")
    out("    ρ_fermion = +7π²/(720 r⁴) = +(7/8) × π²/(90 r⁴)  per d.o.f.")
    out()
    out("  Combined (natural units ℏ=c=1):")
    out(f"    ρ_Casimir = (π²/90r⁴) × (7 N_F/8 − N_B)")
    out()
    out("  SC3 positivity condition:")
    out(f"    7 N_F/8 − N_B > 0  ⟺  N_F > 8 N_B/7")
    out()
    out(f"  For N_B = 2:  N_F_min (real)  = {float(N_F_min_sym.subs(N_B, 2)):.4f}")
    out(f"                N_F_min (integer) = 3")
    out()

    # ── Section 3: branch-screening table ─────────────────────────────────
    out("── SECTION 3: BRANCH-SCREENING TABLE (Steps B & C, §3.7) ──────────────────")
    out()
    out(f"  {'Sector':<46} {'N_B':>4} {'N_F':>4} {'Factor':>8}  {'Verdict'}")
    out("  " + "─" * 76)
    for label, nb, nf, bc in sectors:
        fac = sc3_factor(nb, nf)
        v   = verdict(nb, nf)
        out(f"  {label:<46} {nb:>4} {nf:>4} {fac:>8.3f}  {v}")
    out()
    out("  Factor = 7 N_F/8 − N_B.  PASS threshold: > 0.05. MARGINAL: |factor| ≤ 0.05.")
    out()

    # ── Section 4: numerical at r_fiber = ℓ_P ─────────────────────────────
    out("── SECTION 4: NUMERICAL EVALUATION — KEY BRANCHES ─────────────────────────")
    out()
    out("  Physical constants used:")
    out(f"    ℏ       = {hbar:.6e}  J·s")
    out(f"    c       = {c:.9e}  m/s")
    out(f"    G₄      = {G4:.5e}  m³ kg⁻¹ s⁻²")
    out(f"    ℓ_P     = {ell_P:.6e}  m")
    out(f"    Λ_obs   = {Lambda_obs:.2e}  m⁻²")
    out(f"    ρ_target = Λ_obs c⁴/(8πG₄) = {rho_obs_target:.4e}  J/m³")
    out()

    # Branch 3 (N_B=2, N_F=0) across radius values
    out("  Branch 3  (N_B=2, N_F=0 — periodic bosons only):")
    out(f"  {'r_fiber':<20}  {'ρ_Casimir [J/m³]':>22}  {'ρ / ρ_target':>16}")
    out("  " + "─" * 62)
    for label, rv in r_values.items():
        rho = rho_casimir_SI(2, 0, rv)
        ratio = rho / rho_obs_target if rho_obs_target != 0 else float('nan')
        out(f"  {label:<20}  {rho:>22.4e}  {ratio:>16.4e}")
    out()

    # Branch: N_B=2, N_F=3 (minimum integer PASS candidate)
    out("  Branch: N_B=2, N_F=3  (minimum-integer PASS candidate):")
    out(f"  {'r_fiber':<20}  {'ρ_Casimir [J/m³]':>22}  {'ρ / ρ_target':>16}")
    out("  " + "─" * 62)
    for label, rv in r_values.items():
        rho = rho_casimir_SI(2, 3, rv)
        ratio = rho / rho_obs_target
        out(f"  {label:<20}  {rho:>22.4e}  {ratio:>16.4e}")
    out()

    # ── Section 5: required r_fiber for SC3 closure ────────────────────────
    out("── SECTION 5: REQUIRED r_fiber FOR SC3 CLOSURE  ──────────────────────────")
    out()
    out("  Fiber radius r* at which |ρ_Casimir| = ρ_target (one species factor):")
    out()
    out(f"  {'Sector':<46} {'r* [m]':>16}  {'r* / ℓ_P':>12}")
    out("  " + "─" * 78)
    for label, nb, nf, bc in sectors:
        r_req = required_r_fiber(nb, nf)
        if np.isinf(r_req):
            out(f"  {label:<46} {'(exact cancel)':>16}  {'—':>12}")
        else:
            ratio_lP = r_req / ell_P
            out(f"  {label:<46} {r_req:>16.4e}  {ratio_lP:>12.2e}")
    out()
    out("  NOTE: r* >> ℓ_P for all sectors. At r_fiber = ℓ_P, |ρ_Casimir| >> ρ_target")
    out("  by ~10¹²² — the standard cosmological-constant hierarchy problem.")
    out("  SC3 closure via Casimir requires r_fiber ~ 50–100 μm (near fifth-force bound)")
    out("  OR near-exact boson/fermion cancellation leaving a tiny residual.")
    out()

    # ── Section 6: SC3 decision summary ────────────────────────────────────
    out("── SECTION 6: SC3 DECISION SUMMARY  ────────────────────────────────────────")
    out()
    out("  Branch 3 (N_B=2, N_F=0, periodic):")
    out("    ρ_Casimir < 0  → FAIL.  Cannot close SC3 in this sector.")
    out()
    out("  Minimum integer fermion content for sign-positivity given N_B=2:")
    out("    N_F ≥ 3  (antiperiodic).  Factor = 7×3/8 − 2 = +0.625 > 0.")
    out("    Status: provisional PASS on sign.  Scale requires r* ~ 50–100 μm.")
    out()
    out("  Full SUSY (N_B = N_F): factor = 7 N_F/8 − N_F = −N_F/8 < 0 → FAIL.")
    out("  Exact SUSY cancels in the wrong direction — does not help SC3.")
    out()
    out("  Overall SC3 status: OPEN (staged)")
    out("    - Casimir route requires fermion-dominated post-transition sector.")
    out("    - No PASS branch established without Paper 3 species/BC inputs.")
    out("    - If r_fiber ~ ℓ_P, the Casimir approach faces the CC hierarchy")
    out("      problem and cannot close SC3 without ~ 10¹²² cancellation.")
    out("    - Alternative: r_fiber ~ 50–100 μm with N_F=3, N_B=2 gives correct")
    out("      scale but requires an independent stabilization argument.")
    out()
    out("  Claim-strength policy (§5.6): SC3 remains 'contingent candidate'.")
    out("  Re-entry trigger: finalized Paper 3 species/BC dataset.")
    out()
    out("═" * 78)
    out("  Computation complete.")
    out("═" * 78)

print(f"\nResults written to: {output_path}")
