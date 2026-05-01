# RC-1 Opus 4.6 Verification Pass
**Date:** 2026-05-01
**Reviewer:** Opus-level pass (Oz/Claude)
**Source draft:** `paper2_RC1_effective_stress_tensor_DRAFT.md` (2026-04-15, 631 lines, Sonnet 4.6)
**Session context:** `SESSION_2026-04-10_GEOMETRIC_LAMBDA_ANALYSIS.md` (primary computation source)

---

## Executive Summary

| Section | Status in Draft | Verdict After Opus Pass | Key Issue |
|---------|----------------|------------------------|-----------|
| §RC1.1 — Uniqueness of S^bdy | ✅ DERIVED | ✅ VERIFIED | Minor: Σ-index range d² should be d(d−1) |
| §RC1.2 — Metric variation → T^(eff) | ✅ DERIVED | ✅ VERIFIED | Calculation correct step by step |
| §RC1.3A — w = −1 dark energy | ✅ DERIVED | ⚠️ DEMOTED | Π_μν purely spatial → ρ_eff = 0; w=−1 comes from bulk EOM, not boundary variation |
| §RC1.3A — α = 3/2 exponent | ⚠️ CONJECTURED | ❌ MISIDENTIFIED | α = 3/2 is a COEFFICIENT in Ω_drag = (3/2)(Γ_dec/H₀)², not an exponent; exponent is 2 |
| §RC1.3B — w = 0 dark matter | ✅ DERIVED (A3) | ✅ PLAUSIBLE | Correct under A3 + anisotropic ansatz |
| §RC1.3B — Ω_DM/Ω_b consistency | ⚠️ CONJECTURED | ⚠️ REFRAME NEEDED | Consistency check references wrong α formula |
| §RC1.4 — 𝒫^Σ(k) formula | ✅ DERIVED | ✅ VERIFIED (with A5) | k_c^eff update needed from RC-4 |
| §RC1.4 — 69% quadrupole suppression | ✅ VERIFIED | ✅ VERIFIED | Numerics stand |

**Net result:** §RC1.1 and §RC1.2 are solid. §RC1.3A contains two significant errors; the w=−1 and α=3/2 claims need correction. §RC1.3B and §RC1.4 are structurally sound with appropriate caveats.

---

## §RC1.1 — Symmetry Derivation: VERIFIED ✅

The three-constraint argument (diffeomorphism covariance → boundary integral form; U(d)×T^d invariance → unique bilinear; locality → local product) is logically correct.

**Uniqueness of |T_M|²:**
Under U(d): T_M^{μa} → U^a_b T_M^{μb}. The only U(d)-invariant real bilinear from T_M and T_M† is:
$$|T_M|^2 = g_{\mu\nu}\,h_{ab}\,T_M^{\mu a}\,(T_M^*)^{\nu b} = \text{Tr}(T_M T_M^\dagger)$$
- A linear invariant would require a fixed U(d)-breaking background vector in Σ → forbidden ✓
- Antisymmetric bilinears require an ε tensor on Σ, not U(d)-invariant for complex representations ✓
- Non-Hermitian bilinear T_M^{μa} T_M^{νb} h_{ab} is NOT U(d)-invariant (transforms as U⊗U rather than U⊗U†) ✓

**Minor notation error (does not affect conclusion):** Line 72 sums Σ_{a=1}^{d²}. Σ = U(d)/T^d has real dimension d² − d = d(d−1), so the Σ-index runs over d(d−1) values, not d². Should read Σ_{a=1}^{d(d-1)}.

**No structural issues. §RC1.1 stands as DERIVED.**

---

## §RC1.2 — Metric Variation → T^(eff)_μν: VERIFIED ✅

Step-by-step check:

**Step 1:** δγ_{ij}(y)/δg^{μν}(x) = −g_{μα}g_{νβ} e^α_i e^β_j δ^{(4)}(x−y) — **CORRECT** (standard formula)

**Step 2:** δ√(−γ) = ½√(−γ) γ^{ij} δγ_{ij} — **CORRECT** (standard metric determinant variation)

**Step 3:** Definition Π_{μν} = γ^{ij} e^α_i e^β_j g_{μα} g_{νβ} — **CORRECT.** In FLRW with spatial ∂M, this equals diag(0, a², a², a²) = g_{μν} + n_μ n_ν where n^μ = (1,0,0,0) is the unit timelike normal. ✓

**Step 4:** Reduction of 4D delta function over 3D integral to δ_⊥(x, ∂M) — **CORRECT.** The formula δ_⊥(x,∂M) = δ(n(x))/√(g_{nn}) is standard in thin-shell formalism. ✓

**Sign check:**
$$T^{(\rm eff)}_{\mu\nu} = -\frac{2}{\sqrt{-g}} \cdot \left(-\frac{\lambda}{2}\right)\sqrt{-\gamma}\,\Pi_{\mu\nu}\,|T_M|^2\,\delta_\perp = \lambda\frac{\sqrt{-\gamma}}{\sqrt{-g}}\Pi_{\mu\nu}\,|T_M|^2\,\delta_\perp \quad ✓$$

**Result stands.** The formula
$$\boxed{T^{(\rm eff)}_{\mu\nu}(x) = \lambda\,\frac{\sqrt{-\gamma}}{\sqrt{-g}}\,\Pi_{\mu\nu}\,|T_M|^2\,\delta_\perp(x,\partial M)}$$
is correctly derived from S^bdy = λ ∫_{∂M} d³y √(−γ)|T_M|².

**§RC1.2 stands as DERIVED.**

---

## §RC1.3A — Dark Energy w = −1: DEMOTED ⚠️

### Issue 1: The boundary tensor is PURELY SPATIAL

For a constant-t spatial hypersurface (∂M = t-slice in FLRW):
- Induced metric: γ_{ij} = a²δ_{ij}
- Unit normal: n^μ = (1, 0, 0, 0), n_μ = (−1, 0, 0, 0)
- Boundary projection: Π_{μν} = g_{μν} + n_μ n_ν = diag(0, a², a², a²)

**Π_{μν} has zero time-time component.** Consequently:

$$T^{(\rm eff)}_{00} = \lambda\,\Pi_{00}\,|T_M|^2\,\times(\ldots) = 0$$

$$\Rightarrow\quad \rho_{\rm eff} = T^{(\rm eff)}_{\mu\nu} u^\mu u^\nu = 0$$

with P_eff ∝ a² > 0. This gives **w = P/ρ → ∞**, not w = −1.

The draft's claim at line 312–313 that ⟨T^(eff)_{μν}⟩ = λ|T_M|²/ℓ × g_{μν} (dropping the n_μn_ν term) is **unjustified**. The g_{μν} form would require averaging over different orientations of ∂M — this is not stated or derived.

### Issue 2: Where does w = −1 actually come from?

The actual w = −1 identification comes from the April 10 session (`SESSION_2026-04-10_GEOMETRIC_LAMBDA_ANALYSIS.md`, lines 252–258):

**From the KCR-Cone bulk EOM (not boundary variation):**
$$\rho_{\rm drag} = \alpha\,\frac{\Gamma_{\rm dec}^2}{H_0^2}\,\rho_{\rm crit} = \frac{3}{2}\left(\frac{\Gamma_{\rm dec}}{H_0}\right)^2\rho_{\rm crit}$$

When $\Gamma_{\rm dec} = \text{const}$ (Scenario C: permanently decohered modes):
$$\rho_{\rm drag} = \text{const} \quad\Rightarrow\quad w = -1$$

When $\Gamma_{\rm dec} = \beta H(t)$ (Scenario B: modes crossing Hubble horizon):
$$\rho_{\rm drag} \propto H^2 \propto a^{-3}\quad\Rightarrow\quad w = 0\;\text{(dark matter)}$$

**The w = −1 result is an equation-of-state consequence of Γ_dec = const, not a tensor-structure result from the boundary variation.** The RC-1 draft conflates two distinct derivation routes.

### Corrective instruction for draft:

Change §RC1.3A status from "✅ DERIVED" to:
> **⚠️ PARTIAL — requires bulk EOM route:** The boundary action variation gives T^(eff)_{μν} ∝ Π_{μν} (purely spatial for constant-t ∂M), which contributes zero energy density. The w = −1 identification follows from the April 10 result ρ_drag = (3/2)(Γ_dec/H₀)² ρ_crit with Γ_dec = const. The bridge between the boundary action S^bdy and the bulk density ρ_drag requires the Israel junction condition formalism (extrinsic curvature variation) or an explicit bulk EOM — flagged for RC-2.

---

## §RC1.3A — α = 3/2: MISIDENTIFIED ❌

### The confusion

The RC-1 draft (lines 331–350) interprets α = 3/2 as an **exponent** in ρ_eff ~ Γ_dec^{3/2}. This is incorrect.

### What April 10 actually showed

From `SESSION_2026-04-10_GEOMETRIC_LAMBDA_ANALYSIS.md`, lines 248–252:
> "With graviton zero-mode f₀ = N cos^{3/2}(√2 r): α = 3/2 (from ∫A / ∫A³ = (1/√2) / (2/3√2))"
> "Ω_drag = **(3/2)** × (Γ_dec/H₀)²"

The formula is: **Ω_drag = (3/2) × (Γ_dec/H₀)²**

- **Exponent = 2** (quadratic in Γ_dec/H₀)
- **α = 3/2 = COEFFICIENT**, not exponent
- Origin: ratio of KCR graviton zero-mode integrals

$$\alpha = \frac{\int_0^{\pi/(2\sqrt{2})} f_0(r)\,dr}{\int_0^{\pi/(2\sqrt{2})} f_0^3(r)\,dr} = \frac{1/\sqrt{2}}{2/(3\sqrt{2})} = \frac{3}{2}$$

where f₀ = N cos^{3/2}(√2 r) is the KCR graviton zero-mode wavefunction.

### What the RC-1 spectral density argument gives

The draft (lines 341–350) claims ρ(λ) ~ λ^{1/2} for CP¹ from the Weyl law. This is **incorrect**:

Weyl law for a Riemannian manifold of real dimension n: N(λ) ~ λ^{n/2}, ρ(λ) = dN/dλ ~ λ^{n/2−1}.

For CP¹ (real dim n = 2): ρ(λ) ~ λ^0 = **constant** (not λ^{1/2}).

For ρ(λ) ~ λ^{1/2} one would need n = 3 (3-real-dimensional manifold). But CP¹ = S² has n = 2.

Therefore the spectral density argument in the RC-1 draft does NOT support |T_M|² ~ Γ_dec^{3/2}. The CP¹ Weyl law gives |T_M|² ~ ∫₀^{Γ_dec} dλ ~ Γ_dec (exponent = 1, not 3/2).

### Corrective instruction for draft:

Lines 341–352: Replace the Weyl law argument for α = 3/2. The correct statement is:

> α = 3/2 is a **geometric coefficient** (not exponent) appearing in the dark energy formula Ω_drag = (3/2)(Γ_dec/H₀)². It is derived from the KCR graviton zero-mode coupling integral on the compact interval (April 10 result, commit d325098). The exponent in Ω_drag is 2, not 3/2. The spectral density argument via CP¹ Weyl law is incorrect (ρ(λ) ~ const for CP¹, not λ^{1/2}). Status: ⚠️ CONJECTURED pending full RC-2 derivation of the bulk EOM coefficient.

---

## §RC1.3B — Dark Matter w = 0: PLAUSIBLE ✅ (under A3)

The anisotropic ansatz T_M = A(ρ_b) u⊗ψ giving T^(eff) ~ u_μu_ν is structurally consistent with a pressureless dust equation of state. The analysis is correct under Assumption A3 (lifting A3 requires the T_M EOM from Paper 2A §7, deferred to RC-2).

Note: the Ω_DM/Ω_b consistency check at lines 415–427 references the formula ρ_DM ~ λ² ρ_b^α with α = 3/2 as an exponent. Given the correction above (α = 3/2 is a coefficient, exponent is 2), this check needs to be redone with:

$$\Omega_{\rm DM} = \alpha\,\beta^2 = \frac{3}{2}\beta^2 = 0.259 \quad\Rightarrow\quad \beta = 0.416$$

(April 10 result, line 273: "DM: Ω_DM = (3/2)β² = 0.259, β = 0.416") ✓

The consistency check holds with the correct formula. The dark matter abundance is correctly reproduced by the two-channel model with α = 3/2 as COEFFICIENT, exponent = 2.

**§RC1.3B structural conclusion stands; Ω_DM/Ω_b check valid with corrected formula.**

---

## §RC1.4 — Primordial Power Spectrum: UPDATE NEEDED ✅

### k_c^eff from RC-4 (2026-05-01)

The draft at line 537 identifies k_c^eff as a key open question. RC-4 (2026-05-01) provides the leading-order result:

$$k_c^{\rm eff} = \sqrt{\Omega_\Lambda}\,H_0 = 0.832\,H_0$$

This is the leading-order EOM estimate. The connection to k_c^{SW} = 5/χ_CMB requires the holographic projection R_Σ = χ_CMB (Paper 4 §3, factor ~1.9 gap).

**Update instruction for §RC1.4:** Replace text around "physical k_c from first principles" with:
> RC-4 (2026-05-01) provides the leading-order physical cutoff: $k_c^{\rm eff} = \sqrt{\Omega_\Lambda}\,H_0 = 0.832\,H_0$. Full agreement with $k_c^{\rm SW} = 5/\chi_{\rm CMB}$ requires the holographic projection $R_\Sigma = \chi_{\rm CMB}$ (Paper 4 §3).

The remainder of §RC1.4 (propagator form A5, angular power spectrum formula, 69% quadrupole suppression) is structurally sound. The numerical verification (k_c = 5/χ_CMB → 69% suppression) stands.

---

## Updated §RC1.5 Status Table

| Section | Target | Status After Opus Pass | Key Gap |
|---------|--------|----------------------|---------|
| §RC1.1 | Symmetry constraints → S^boundary_M | ✅ DERIVED | Minor d² notation |
| §RC1.2 | Metric variation → T^(eff)_μν | ✅ DERIVED | — |
| §RC1.3A | DE limit: w = −1 | ⚠️ REQUIRES BULK EOM | Π_μν purely spatial; bulk density from April 10 EOM route |
| §RC1.3A | α = 3/2 as exponent | ❌ MISIDENTIFIED | Exponent is 2; 3/2 is coefficient from ∫f₀/∫f₀³ |
| §RC1.3A | α = 3/2 as coefficient in Ω_drag=(3/2)(Γ_dec/H₀)² | ✅ DERIVED (April 10) | Cite commit d325098 |
| §RC1.3B | DM limit: w = 0 from anisotropic T^(eff) | ✅ PLAUSIBLE under A3 | Needs RC-2 |
| §RC1.3B | Ω_DM/Ω_b consistency | ✅ CONSISTENT | Use corrected formula (exponent=2, coeff=3/2) |
| §RC1.4 | 𝒫^Σ(k) formula | ✅ DERIVED (A5) | — |
| §RC1.4 | 69% quadrupole suppression | ✅ VERIFIED | — |
| §RC1.4 | k_c^eff from first principles | ✅ RC-4 leading order | Paper 4 §3 for full closure |

---

## RC-2 Scope (revised based on Opus findings)

The primary RC-2 task is to **reconcile the boundary action route with the bulk EOM route** for dark energy:

1. **Show the equivalence**: S^bdy = λ∫_{∂M} √(-γ)|T_M|² d³y produces, via Israel junction conditions (not direct T_{μν} variation), an effective bulk contribution ρ_eff = (3/2)(Γ_dec/H₀)² ρ_crit when Γ_dec = const.

2. **Derive T_M EOM** from the full S_CR (Paper 2A §7 EOM) and lift A3.

3. **Correct α = 3/2 context**: Formally show that the coupling integral ∫f₀/∫f₀³ = 3/2 (from the KCR graviton zero-mode) enters the Israel junction-condition coefficient, making α = 3/2 emerge as the dark energy proportionality constant.

4. **Verify covariant conservation** ∇^μ T^(eff)_μν = 0 using T_M EOM.

---

## Summary of Promotions and Demotions

**Promoted:**
- §RC1.1 uniqueness: confirmed ✅ (notation caveat noted)
- §RC1.2 variational calc: confirmed ✅
- §RC1.4 k_c^eff: updated with RC-4 result

**Demoted / Corrected:**
- §RC1.3A w=−1: ⚠️ from "✅ DERIVED" to "REQUIRES BULK EOM / ISRAEL JC"
- §RC1.3A α=3/2 as exponent: ❌ incorrect; it is a coefficient (exponent = 2)

**Net gate status:** RC-1 provides the correct formal framework (S^bdy → T^(eff)_{μν} derivation is solid). The physical identification of dark energy requires the bulk EOM route, which is the primary RC-2 task. The α=3/2 = ∫f₀/∫f₀³ is already derived (April 10) and should be correctly cited as a COEFFICIENT in Ω_drag = (3/2)(Γ_dec/H₀)².

**Recommendation:** Update RC-1 draft §RC1.3A and §RC1.5 table with corrections. Paper 3 §5 can proceed using the April 10 formula as the working result, clearly labeling the bulk EOM route as "leading-order, pending RC-2 formal derivation."
