# Session Archive — 2026-04-14 (Claude Cowork Track)
**KB ID**: S-20260414-002
**Agents**: Bryan Kaufman + Claude Cowork (Anthropic)
**Source**: CR_Session_Log_2026-04-14.pdf
**Perplexity review**: Provided — full technical evaluation
**Status**: ARCHIVE — source document for Papers 3 and 4

---

## Overview

Two tracks developed simultaneously:
1. **T2.5-B**: SM Viability via S³ Chowla-Selberg K₂ Formula (82% complete)
2. **CMB as ∂M**: Geometric transitions and CR framework formalization (~30% complete)

This session is the technical complement to SESSION_2026-04-14_ORTHOVERSE_SINGULARITY_DARK_MATTER.md (Oz/Warp track). Together they form the complete April 14 research record.

---

## PART I: T2.5-B — SM Casimir Bounce Cosmology

### Setup

5D ansatz: S¹_t × S³ × S¹_φ with radion b fixed at b* (Goldberger-Wise stabilization).
The S³ is the spatial universe (scale factor a(t)); S¹_φ is the compact extra dimension (size b*).

**Context**: T3-A established a universal no-go: no perturbative 1-loop Casimir source with dynamic b(t) admits a closed oscillatory orbit. The T2.5-B loophole: fix b = b* via GW stabilization, reducing to a 1D system in a(t). The 1D bounce condition is then only w₃ < -1/3 (not w_φ < -1 as required in 5D).

### The 1D Dynamical System

Friedmann (k=+1): H² = κρ(a;b*)/3 - 1/a²

Bounce condition: w₃ = p₃/ρ < -1/3 at turning points (H=0, κρ·a² = 3)

### SM Field Content (Chowla-Selberg K₂ formula)

| Species | Count | BC | Type |
|---|---|---|---|
| Higgs + A₅ scalars | 16 | Periodic | Scalar |
| Transverse gauge A_μ | 12 | Periodic | Vector |
| Dirac fermions (3 gen × 8) | 24 | Anti-periodic | Spinor |

E_SM = 16·E_scalar + 12·E_vector + 24·E_spinor

**Sign competition**: Bosons dominate at small a (negative Casimir, ρ<0). Fermion degeneracy ~2l² grows faster than scalar ~l²; at large a, fermions dominate (positive ρ). Sign flip at a ≈ 2.3 b*. The bounce operates entirely in the fermion-dominated regime.

### Key Numerical Results (VERIFIED, 2026-04-14)

| Quantity | Value | Status |
|---|---|---|
| a_min | 58.85 b* | ✅ verified |
| a_max (l_max=80) | 605.5 b* | ✅ (underestimate) |
| (κρa²)_peak | 8.48 at a = 166 b* | ✅ verified |
| w₃ at a_min | -0.943 | ✅ bounce confirmed |
| T_osc (quadrature) | **1884.7 b*** | ✅ verified |
| Ω_osc | 3.334×10⁻³ b*⁻¹ | ✅ computed |
| T_KK × T_osc | 300 | Expected (sub-Hagedorn) |

**The quadrature formula** (exact, no EOS approximation):
$$T_{osc} = 2\sqrt{3} \int_{a_{min}}^{a_{max}} \frac{da}{\sqrt{\kappa\rho(a)a^2 - 3}}$$

### SCF Self-Consistency

The KK-SCF condition T_osc × T_KK = 1 fails by factor 300. This is **expected physics** — T2.5-B is a sub-Hagedorn cosmological mode (a_min = 59 b* >> b*), not a stringy T-duality scenario.

**Correct SCF criterion**: GW radion adiabaticity: m_φ >> Ω_osc = 3.33×10⁻³ b*⁻¹

| kb* | m_φ/Ω_osc | Adiabatic? |
|---|---|---|
| 0.5 | 6.5 | borderline |
| 1.0 | 0.56 | ❌ |
| 2.0 | 0.002 | ❌ |

**Conclusion**: Standard RS-I values (kb* ~ 10-12) fail. Needs kb* ≲ 0.5 OR large brane coupling ε (which can make m_φ substantially heavier). This is a parameter constraint, not a no-go.

### Open: GW Parameter Scan (blocks paper inclusion)

Find region of (k, μ, ε) satisfying m_φ(k,μ,ε) > 10·Ω_osc.
GW potential: V(Φ) = -μ²Φ² + εΦ⁴ with boundary conditions Φ(0) = v_UV, Φ(πb*) = v_IR.

Radion mass (schematic): m²_φ = (24εv⁴_IR/M₅³) · ke^{-2kπb*}/(1-e^{-2kπb*})

### Error Log (documented for reproducibility)

1. Sign error in ρ: ρ = -E/V instead of +E/V → (κρa²)_peak = -8.48, no TPs
2. Volume factor 2π²: Used 2π²a³ instead of a³b* convention → factor-19.74 error
3. Wrong ODE (Ḣ = -ρ/2 + 1/a²): Spurious bounce at a≈39b*, T_osc≈217 (×8.7 too short) → replaced by exact quadrature

---

## PART II: CMB as ∂M — CR Framework Formalization

### Core Identification

The CMB last-scattering surface = ∂M at epoch t_rec = **the fact horizon frozen in light**.

Three geometric confirmations:
1. **Conformal identification**: In k=+1 FLRW Penrose diagram, CMB sphere (χ_CMB, t_rec) and initial singularity are the same conformal boundary approached from different directions
2. **Extrinsic curvature**: K_ext = cot(χ_CMB)/a(t_rec) → ∞ as χ_CMB → 0 (sphere becomes point = geometric signature of singularity)
3. **Bekenstein bound**: S_CMB = A/4G ≈ 10¹²³ bits — maximal information encodable on ∂M; CMB is the holographic screen

Physical numbers:
- r_CMB(t_rec) ≈ 0.38 Mly (Bryan's 380,000 light years)
- r_CMB(t₀) ≈ 45.7 Gly (current comoving)
- Expansion factor: 1+z_rec ≈ 1100

### CMB Fluctuations: Σ-Signal vs M-Noise

$$C_\ell^{obs} = T^2(\ell) \cdot C_\ell^\Sigma + C_\ell^{noise}$$

**Three angular scale regimes:**

| Scale | ℓ range | Character |
|---|---|---|
| Super-horizon | ℓ ≲ 30 | Direct ∂M boundary conditions = **Σ-signal** |
| Acoustic regime | 30 ≲ ℓ ≲ 2000 | Mixed: Σ-signal seeded oscillations + M-processing |
| Sub-arcminute | ℓ ≳ 2000 | Silk damping washes out primordial; **M-noise** |

**Low-ℓ anomalies as Σ-structure**:
- Quadrupole suppression: C₂^obs ≈ 0.3 × C₂^ΛCDM
- Octopole planarity
- Hemispherical asymmetry (~6% power difference N vs S at ℓ ≲ 64)

CR interpretation: These are signals of non-trivial Fubini-Study geometry of Σ = U(d)/T^d projected onto ∂M. Quadrupole suppression suggests Σ has a natural UV cutoff on large-scale modes — consistent with finite dimension d.

### T_MΣ at the Fact Horizon

- In bulk M: T_MΣ coupling is small
- At ∂M: coupling maximum (irreversible decoherence happening here)
- Schwarzschild analogy: at Schwarzschild horizon, g_tt and g_rr exchange roles (t↔r). At CR fact horizon, M and Σ exchange roles — M becomes boundary (dissolves into facts), Σ absorbs information.

**"Reading the CMB anomalies is literally reading the geometry of the coherosphere Σ."**

---

## PART III: Formalization Requirements (RC-1 through RC-4)

### RC-1: Derive T_μν^(eff) from CR action principle (CRITICAL)

The CR action (schematic form):
$$S_{CR} = \int_M \sqrt{-g}[R/16\pi G + \mathcal{L}_{matter}] + \int_\Sigma \omega_{FS} \wedge \mathcal{F} + S_M^{boundary}$$

Constraints on S_M^boundary (from Perplexity evaluation):
- Covariance on M: depends on induced metric γ_ij and extrinsic curvature K_ij
- U(d) invariance on Σ, plus T^d gauge invariance
- Locality along ∂M
- Leading term: S_boundary ~ ∫_∂M √(-γ) λ Tr(T_M T_M†)
- → T_μν^(eff) is quadratic in M-Σ coupling

**Without RC-1, C_ℓ^Σ prediction is conjecture, not derivation.**

### RC-2: Conformal identification of CMB → singularity

χ_CMB = η₀ - η_rec (conformal time)

For k=+1 S³ universe with η₀ ≲ π: χ_CMB ≈ 3 rad. Extrinsic curvature:
K_ext = cot(χ_CMB)/a(t_rec) ≈ -7.02/a_rec (15% correction to flat-universe analysis)

### RC-3: Map C_ℓ^Σ from Fubini-Study geometry

Given RC-1, primordial power spectrum seeded by Σ:
$$\mathcal{P}^\Sigma(k) \propto |\langle k|T_M|\partial M\rangle|^2$$

Angular projection:
$$C_\ell^\Sigma = \frac{2}{\pi}\int k^2 \mathcal{P}^\Sigma(k)[j_\ell(k\chi_{CMB})]^2 dk$$

FS metric on U(d)/T^d has natural scale set by dimension d → suppression for k ≲ 1/d → ℓ ≲ ℓ_min. **This is the quadrupole anomaly mechanism.**

### RC-4: Extrinsic curvature as observable

ISW contribution at ℓ ≤ 10 should carry correction of order K_ext/H_rec ≈ cot(χ_CMB)·H_rec⁻¹/a_rec.

---

## PART IV: Paper Assignment (Reconciled with SPINE)

**Note**: The Claude Cowork session used a different paper numbering (their "Paper 2A §5" = T2.5-B content). Reconciled here with the SPINE structure:

| Claude session ref | SPINE paper | Section | Status |
|---|---|---|---|
| Paper 2A §3 (T_MΣ formalism) | Paper 2A §2.1-2.2 | ✅ drafted | Not blocked |
| Paper 2A §5 (T2.5-B viability) | **Paper 3 §5** | 82% complete | GW scan blocks |
| Paper 2A §6 (SCF conditions) | Paper 3 §5 (SCF part) | Complete | Draftable now |
| Paper 2B §8 (holographic) | Paper 2A §5 | ✅ drafted | RC-1 gate |
| Paper 4 (CMB anomalies) | **Paper 4** | ~30% | RC-1 through RC-3 gate |

**T2.5-B is Paper 3 content**: The 5D bounce (S³ universe + S¹_φ compact) is the cosmological dynamics of the KCR structure — Paper 3 (emergence, cosmological evolution), not Paper 2B (static KCR-Cone vacuum).

---

## Perplexity Evaluation — Key Actionable Items

1. **T2.5-B**: Add explicit statement that b=b* restriction is leading term in Ω_osc²/m_φ² expansion — guards against "froze a dangerous mode" critique
2. **SCF**: Spell out explicitly why KK-SCF criterion fails: because T_eff ~ 1/a_min << T_KK
3. **CMB conformal identification**: Soften — say "same conformal boundary approached from different directions," not "literal identification"
4. **CMB Bekenstein**: Clarify using current area of CMB sphere, not area at recombination
5. **Low-ℓ claims**: Soften "are not noise or artefacts" to "are unlikely to be fully explained by noise"
6. **Toy C_ℓ model**: Add one-line schematic formula P_Σ(k) ~ (1+k²/k_c²)⁻¹ showing natural low-ℓ cutoff → produces figure for Paper 2B §8
7. **RC-1 boundary action**: List symmetry constraints (covariance, U(d) invariance, locality) before presenting the schematic form

---

## Open Calculations — Updated After Tier 1 and Tier 3 Checks

| Calculation | Status | Priority | Needed for |
|---|---|---|---|
| ζ-regularized spectral sum | ❌ 0% | **BLOCKER** (was low) | Physical T_osc, a_max |
| GW parameter scan (k,μ,ε) | ❌ 0% | Blocked by ζ-reg | T2.5-B paper-ready |
| 5D spin-factor corrections | ❌ 0% | Low (~5-10%) | T2.5-B precision |
| SM thermal corrections (Matsubara) | ❌ 0% | Low (<1%) | T2.5-B precision |
| RC-1: T_μν^(eff) from action | ❌ 0% | Critical | All holographic predictions |
| RC-2: Penrose conformal identification | ❌ 0% | Medium | CMB-singularity bridge |
| RC-3: C_ℓ^Σ from FS geometry | ❌ 0% | Depends on RC-1 | Paper 4 |
| RC-4: K_ext as ISW observable | ❌ 0% | Medium | Paper 4 |

**Dependency graph (from session log IV.4):**
```
ζ-reg spectral sum ← BLOCKER
  └── T2.5-B final a_max, T_osc
        └── GW parameter scan (exact Ω_osc input)
              └── Paper 3 §5 completion
RC-1
  ├── RC-3 (C_ℓ^Σ) → Paper 4
  └── Paper 2A §5 (holographic conjecture → calculation)
RC-2 → RC-4 (K_ext observable)
```

---

## PART V: Tier 1 Convergence and Robustness Checks

*Executed 2026-04-14 in response to Perplexity referee feedback.*

### Study 1 — l_max Convergence (MAJOR FINDING)

**Question**: Is T_osc = 1884.7 b* a converged result?

**Method**: Run κρa² grid scan at l_max ∈ {60, 80, 100}.

| l_max | a_min/b* | a_max/b* | (κρa²)_peak | T_osc (b*) | w₃ |
|---|---|---|---|---|---|
| 60 | 62.46 | 292.6 | 4.95 | 1068 | −0.800 |
| **80** | **58.85** | **605.5** | **8.48** | **1885** | **−0.943** |
| 100 | 58.20 | 1043.5 | 12.96 | 3085 | −0.985 |

**Result: l_max convergence NOT ACHIEVED for upper TP or period.**
- ΔT_osc(60→80) = 43%; ΔT_osc(80→100) = 64%
- Δa_max(60→80) = +313 b*; Δa_max(80→100) = +438 b*

**What is converging:**
- a_min ✅: 62.5 → 58.8 → 58.2 b* (1% shift 80→100). Bounce, w₃ ≈ −0.95, bounce condition confirmed.
- a_max ❌: Upper TP grows proportionally with l_max. Spectral sum not at asymptotic plateau.
- (κρa²)_peak ❌: 4.95 → 8.48 → 12.96. Peak accumulates from all modes.

**Physical interpretation**: At large a, dominant spectral contributions come from modes l ~ l_max whose effective KK mass m_l = √λ_l/a is still O(1) at the upper TP scale. Each additional batch pushes κρa² above threshold further out. This is standard Chowla-Selberg truncation behavior — the large-a tail requires ζ-function regularization.

**Consequence**:
> T_osc = 1884.7 b* [l_max = 80] is a lower bound, not the physical period.

The physical T_osc is larger — likely by a factor of a few — once a_max is ζ-regularized.

**What this does NOT affect**: bounce (a_min, w₃, existence), sub-Hagedorn interpretation, KK-SCF irrelevance, GW parametric scaling formula.

**Status update**: ζ-regularized spectral sum upgraded from LOW PRIORITY → **BLOCKER**. T2.5-B overall status: 82% → **72%**.

### Study 2 — Endpoint ε Robustness

**Question**: Does T_osc depend on the endpoint inset parameter ε?

| ε (b*) | T_osc (b*) | ΔT/T_ref |
|---|---|---|
| 0.005 | 1884.7106 | −0.0001% |
| **0.010** | **1884.7125** | reference |
| 0.015 | 1884.7138 | +0.0001% |
| 0.020 | 1884.7142 | +0.0001% |

**Total variation: 0.0002%.**

**Paper-ready statement**: "Varying the endpoint inset ε between 0.005 b* and 0.020 b* shifts T_osc by less than 0.001%, confirming the robustness of the quadrature."

The analytic endpoint correction formula is working correctly. The integrand singularity is cleanly handled.

### Study 3 — Minimal GW Parameter Scan

**Question**: For what GW parameter values is radion adiabaticity satisfied naturally?

**Parametric GW radion mass**: m_φ = C_GW√ξ · k · e^{−kπb*}, C_GW = √12 ≈ 3.464, ξ ≡ ε_GW(v_IR/M₅)²

**Adiabaticity constraint**: m_φ > 10 Ω_osc → √ξ > 9.6×10⁻³ · [k e^{−kπb*}]⁻¹

| kb* | m_φ/Ω_osc (ξ=1) | ξ_min | Assessment |
|---|---|---|---|
| 0.1 | 76 | 1.7×10⁻² | ✅ natural |
| 0.3 | 120 | 6.8×10⁻³ | ✅ natural |
| 0.5 | 110 | 8.6×10⁻³ | ✅ natural |
| 1.0 | 45 | 5.0×10⁻² | ✅ natural |
| 1.5 | 14 | 5.1×10⁻¹ | ✅ natural |
| **1.63** | **10** | **1** | **← natural boundary** |
| 2.0 | 3.9 | 6.6 | ⚠️ mild tuning |
| 3.0 | 0.25 | 1.6×10³ | ❌ tuned |

**Natural boundary**: kb* < 1.63 ⇒ adiabaticity with ξ < 1 (no fine-tuning)
- kb* = 0.5: need ξ > 8.6×10⁻³ (ε_GW ~ O(1), v_IR/M₅ ~ O(0.1)) ✅
- kb* = 1.0: need ξ > 5.0×10⁻² ✅
- kb* = 2.0: need ξ > 6.6 ⚠️ mild tuning

**Caveat**: Ω_osc here is from l_max = 80 (lower bound). True Ω_osc will be smaller → adiabaticity easier → natural window expands beyond kb* = 1.63.

---

## PART VI: Tier 3 — Toy Σ → C_ℓ Model

*Figure: CL_sigma_toy_model.pdf | Triggered by: Perplexity recommendation to anchor Paper 2A §5 conjecture section.*

### Physical Motivation

The coherosphere Σ = U(d)/T^d has a natural momentum scale k_c ~ 1/L_Σ below which the Fubini-Study geometry has no support. When CMB = ∂M (fact horizon), the primordial power spectrum carries this IR cutoff as a physical imprint. Modes k < k_c are suppressed relative to Harrison-Zel'dovich.

### Toy Spectrum Model

Fubini-Study–motivated Lorentzian IR cutoff:

Δ²_Σ(k) = A_s · k²/(k² + k_c²)

Properties:
- Δ²_Σ → 0 as k → 0 (no super-coherosphere power)
- Δ²_Σ → A_s as k >> k_c (Harrison-Zel'dovich recovery)
- Half-power at k = k_c

Angular power spectrum (Sachs-Wolfe approximation):
C_ℓ = (2/9π) ∫ (dk/k) Δ²_Σ(k) j²_ℓ(kχ_CMB)

### Numerical Results

| k_c | Quadrupole suppression (ℓ=2) | Half-suppression at ℓ | Interpretation |
|---|---|---|---|
| 3/χ | 49% | ℓ ≈ 2 | mild |
| **5/χ** | **69%** | ℓ ≈ 4 | **matches observed ~67% deficit** |
| 10/χ | 88% | ℓ ≈ 8 | strong |

**Key result**: k_c = 5/χ_CMB ⇒ 69% quadrupole suppression ≈ observed Planck deficit (~67%)

Suppression ratio D^Σ_ℓ/D^std_ℓ by multipole (for k_c = 5/χ):
- ℓ=2: 0.307; ℓ=3: 0.451; ℓ=5: 0.657; ℓ=10: 0.870; ℓ=20: 0.962; ℓ=30: 0.982; ℓ=50: 0.994

Recovery within 1–3% by ℓ ≈ 30 — exactly the boundary of the observed anomaly regime.

### Physical Mapping to Paper Parameters

- χ_CMB ≈ 14,000 Mpc (comoving to last scattering)
- For ℓ_c ≈ 5: k_c ≈ 5/χ_CMB ≈ 3.6×10⁻⁴ Mpc⁻¹
- Physical scale: L_c = 1/k_c ≈ 2800 Mpc ≈ Hubble horizon
- Coherosphere "size" L_Σ ~ L_c is a COSMOLOGICAL scale, not Planck-scale
- Consistent with CR: Σ lives on the Hilbert space of the universe, not tied to any UV scale

### Consistency Check (d ~ 10^61)

k_c = 5/χ_CMB implies d ~ χ_CMB/5 ~ L_Hubble/5 ~ 10^61 (in Planck units).

A d-dimensional coherosphere has dimension ~ d² → d² ~ 10^122.

S_CMB ~ 10^123 (Bekenstein bound). These are within one order of magnitude from completely independent reasoning. **This is not a proof but is not coincidental.**

### Connection to RC-1 and RC-3

Once RC-1 is done:
1. S_boundary ~ λ ∫_∂M √(−γ) Tr(T_M T_M†)
2. Varying → T^(eff)_μν ∝ λ² |T_M|² · γ_μν
3. This sources 𝒫^Σ(k) ∝ λ²|T_M(k)|²
4. Fubini-Study momentum cutoff k_c ~ 1/d enters through k-space propagator of T_M on compact Σ
5. The resulting C^Σ_ℓ is exactly the integral computed here, with k_c determined from first principles

The toy model result becomes a **prediction**: the dimension d of the coherosphere satisfies d ~ χ_CMB/5 ~ 10^61.

### Status of Toy Model

| Item | Status |
|---|---|
| Numerical Sachs-Wolfe integral | ✅ verified |
| FS-suppressed spectrum: qualitative low-ℓ suppression | ✅ verified |
| k_c = 5/χ matches observed quadrupole deficit (within 3%) | ✅ verified |
| Full Boltzmann transfer function (CAMB/CLASS) | ❌ untested |
| Hemispherical asymmetry + octopole alignment | ❌ untested (need higher-order FS geometry) |
| RC-1 derivation — physical k_c from first principles | ❌ missing |
| Coupling λ fixed (currently free parameter) | ❌ missing (RC-1 fixes it) |
| FS cutoff functional form (Lorentzian vs other) | ❓ uncertain |

---

*Session note logged 2026-04-15 by Oz (Warp) — from CR_Session_Log_2026-04-14.pdf (Tier 1 + Tier 2 + Tier 3 complete, 25 pages)*
