# Paper 2C — Idea Assignments & Section Backlog
**Title (working)**: Holographic Structure of Coherence Relativity: Effective Stress Tensor, Dark Sector, and CMB Imprint
**Compiled**: 2026-04-15
**Decision date**: 2026-04-15 — Bryan Kaufman
**Status**: RC-1 first draft complete (Sonnet 4.6); Opus verification needed on §RC1.1 uniqueness proof and §RC1.3B anisotropic tensor structure

**Architecture note**: Paper 2 is now a three-part series:
- **Paper 2A**: Abstract M×Σ framework (§2.1–§2.6: T_MΣ, δλ, Markov, pilot-wave, generators, Born rule)
- **Paper 2B**: Derived topology + KCR-Cone evaluation (§3 compactification, §4 EOM, SC1/SC2/SC3)
- **Paper 2C (this paper)**: Holographic structure — RC-1 as core result; dark sector and CMB as immediate consequences

**Relation to Papers 3 and 4**:
- Paper 3 **cites Paper 2C** for T^(eff)_μν and opens directly with cosmological dynamics (T2.5-B bounce, dark matter halos)
- Paper 4 **cites Paper 2C** for C_ℓ^Σ formula and uses RC-1 result to derive CMB anomaly predictions

---

## Core Result: RC-1 — T^(eff)_μν from the CR Action Principle

**File**: papers/02-saturation-dynamics/sections/drafts/paper2_RC1_effective_stress_tensor_DRAFT.md (631 lines)
**Model**: Sonnet 4.6 — Opus verification needed before paper inclusion on §RC1.1 and §RC1.3B

### The Main Theorem (§RC1.1–RC1.2)

Three symmetry constraints on S^boundary_M:
1. **Diffeomorphism covariance on M**: depends only on γ_ij and K_ij of ∂M
2. **U(d) × T^d invariance on Σ**: unique invariant bilinear is Tr(T_M T_M†)
3. **Locality along ∂M**: local integral, no non-local kernels

These uniquely fix the leading boundary action:
$$S_M^{\rm boundary} = \lambda \int_{\partial M} \sqrt{-\gamma}\, \mathrm{Tr}(T_M T_M^\dagger)$$

Metric variation gives the **effective stress tensor** (the paper's core result):
$$\boxed{T^{\rm (eff)}_{\mu\nu}(x) = \lambda\,\frac{\sqrt{-\gamma}}{\sqrt{-g}}\,\Pi_{\mu\nu}\,|T_M|^2\,\delta_\perp(x,\partial M)}$$

where Π_μν = γ^ij e^α_i e^β_j g_μα g_νβ is the induced-metric projector.

**Properties**: Quadratic in T_M ✅, localized on ∂M ✅, no normal flux ✅.

### Corollary 1: Dark Energy (§RC1.3A)

Uniform Γ_dec → isotropic Π_μν → T^(eff) ∝ g_μν → **w = -1** ✅ DERIVED

Physical: The homogeneous decoherence front (∂M at cosmological scale) sources a cosmological constant.

### Corollary 2: Dark Matter (§RC1.3B)

Γ_dec ∝ ρ_b → T_M = A(ρ_b) u⊗ψ → T^(eff) ∝ u_μ u_ν → **w = 0 (dust)** ✅ DERIVED

Physical: Locally-tracking decoherence generates pressureless dark matter co-moving with baryons.

**α = 3/2 exponent**: Consistent with Ω_DM/Ω_b = 5.29 for λ² ~ 24 ρ_c^{-1/2} ⚠️ CONJECTURED — derivation from CP¹ spectral density is RC-2 target.

### Corollary 3: Primordial Spectrum + CMB (§RC1.4)

From T_M propagator on compact Σ:
$$\Delta^2_\Sigma(k) = A_s \cdot \frac{k^2}{k^2 + k_c^2}$$

Angular power spectrum:
$$C_\ell^\Sigma = \frac{2}{9\pi}\int \frac{dk}{k}\,\Delta^2_\Sigma(k)\,[j_\ell(k\chi_{\rm CMB})]^2$$

**Verified**: k_c = 5/χ_CMB → 69% quadrupole suppression (Planck observed: ~67%, within 3%) ✅

---

## §8 Quantum-Foundations Applications

**Source**: paper2_section_8_QF_applications_DRAFT.md (already integrated into paper2A_COMPRESSED_2026-04-15.md)
**Content**:
- §8.1: Frauchiger-Renner holonomy (Hol = i, ⚠️ Opus verification on Ω=π)
- §8.2: Proietti-type loop holonomy (M×Σ extension)
- §8.3: Quantum Zeno — four-explanation unification in CR geometry
- §8.4: Pointer-basis prediction t_cross(α) = τ_Z sec²α (Prediction 8.4.1)
- §8.5: Collapse as phase transition on Σ (stub — formal derivation Paper 3)

**Paper 2C placement**: §8 belongs in 2C because all applications use T_MΣ and the Markov criterion (§2.6 from 2A) — they are consequences of the same geometric coupling that RC-1 formalizes.

---

## Holographic Dictionary (Upgraded by RC-1)

After RC-1, Paper 2A §5's "conjecture" becomes a calculation in Paper 2C:

| CR object | Holographic role | RC-1 status |
|---|---|---|
| S^boundary_M | GHY-type boundary action on ∂M | ✅ DERIVED |
| T^(eff)_μν | Boundary stress tensor | ✅ DERIVED |
| λ | M-Σ coupling constant | ⚠️ normalization = RC-2 |
| Π_μν δ_⊥ | Support on ∂M = CMB surface | ✅ DERIVED |
| Δ²_Σ(k) | Holographic primordial spectrum | ✅ DERIVED (propagator form) |
| k_c | IR cutoff from Σ geometry | ❌ BLOCKED → RC-3 |

**Bekenstein bound check** (RC-4 in 2C): S_∂M ~ ∫_∂M λ|T_M|² d³y should reproduce S ~ A/4G ~ 10^{123} bits, fixing λ normalization.

---

## Formalization Requirements (RC Gates for Paper 2C)

**RC-1** ✅ First draft complete — see above. Opus verification needed.

**RC-2** (gates α=3/2 derivation and λ normalization):
1. δT_M/δg^μν from M-Σ EOM (Paper 2A §7) — lifts Assumption A3
2. |T_M|²(Γ_dec) → derive α=3/2 from CP¹ spectral density (not insert by hand)
3. Covariant conservation ∇^μ T^(eff)_μν = 0 with T_M EOM as source/sink
4. Propagation: T^(eff)|_∂M at t_rec seeds bulk DM density for t > t_rec

**RC-3** (gates physical k_c — Paper 4 deliverable, not strictly needed for 2C):
Derive k_c from KCR mode spectrum of T_M on U(d)/T^d.

**RC-4** (Paper 2C §5 completion):
Bekenstein consistency check: λ normalization from S_∂M = A/4G.

---

## Section Outline (Draft)

| Section | Content | Status |
|---|---|---|
| §1 Introduction | Series context; paper 2C role; main results preview | Not drafted |
| §2 The Boundary Action | RC-1 §RC1.1: Symmetry derivation of S^boundary_M | ✅ RC-1 draft |
| §3 Effective Stress Tensor | RC-1 §RC1.2: Metric variation → T^(eff)_μν formula | ✅ RC-1 draft |
| §4 Dark Sector from ∂M | RC-1 §RC1.3: DE (w=-1) and DM (w=0) limits | ✅ RC-1 draft; α=3/2 ⚠️ |
| §5 Primordial Spectrum | RC-1 §RC1.4: Δ²_Σ(k) and CMB C_ℓ^Σ | ✅ RC-1 draft; k_c ❌ |
| §6 Holographic Dictionary | Upgraded §5 from 2A; CMB as ∂M | From 2A §5 + SESSION_2026-04-14 |
| §7 Quantum-Foundations | §8.1–8.5 QF applications | ✅ From 2A §8 |
| §8 Discussion | Connection to Papers 3 and 4; open items | Not drafted |
| §9 Open Problems | RC-2 through RC-4; ζ-reg for T2.5-B | From 2A §10 selection |

**Estimated length**: ~18,000–22,000 words (RC-1 draft ~8,000 + §8 QF ~2,400 + dictionary + intro/discussion)

---

## Status Summary

| Track | Status | Blocking |
|---|---|---|
| RC-1 (T^(eff)_μν) | 60-65% complete | Opus verification; RC-2 for α=3/2 |
| QF Applications (§8) | ~90% | §8.1–8.2 Opus verification (Ω=π) |
| Holographic dictionary | Framework ready | RC-1 upgrades conjecture → calculation |
| CMB identification (∂M) | Conceptual complete | RC-3 for physical k_c |
| Dark sector limits | Tensor structure derived | RC-2 for α=3/2 and λ normalization |

**Paper 2C is draftable now** at the conjecture/framework level. Full derivation requires RC-2 (α=3/2 mechanism). RC-3 and RC-4 strengthen but do not block 2C.

---

*Created 2026-04-15 by Oz (Warp). Decision: Bryan Kaufman 2026-04-15.*
*Source material: paper2_RC1_effective_stress_tensor_DRAFT.md; SESSION_2026-04-14_T25B_CMB_BOUNDARY.md; paper2_section_8_QF_applications_DRAFT.md*
