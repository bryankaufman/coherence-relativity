# RC-6 — α Audit: Provenance, Errors, and Disambiguation

**Date:** 2026-04-18
**Author:** Claude (Opus 4.6 pass)
**Scope:** Trace all appearances of "α = 3/2" across Papers 2A–2C and RC documents; identify which are derived, which are conjectured, and which are erroneous. Fix the π error in RC-2. Collapse the notation.
**Inputs:** RC-2 (2026-04-17), RC-3 (2026-04-18), RC-5 (2026-04-18), Paper 2A/2B/2C, RC-1 verification memo

---

## RC-6.1 — The Problem: Three Different α's Sharing a Symbol

Three distinct quantities have been written as "α = 3/2" in the Paper 2 manuscripts:

| Label | What it is | Where introduced | Status |
|-------|-----------|-----------------|--------|
| **α_spec** | Spectral-density exponent: $\|T_M\|^2 \propto \Gamma_{\rm dec}^{3/2}$ | Paper 2C §RC1.3 (Conjecture C1) | ❌ **KILLED** — Weyl formula on CP¹ gives α = 1, not 3/2 (RC-1 Issue #4) |
| **p** | Dynamical scaling: $\|T_M\|^2 \propto \Gamma_{\rm dec}^p$ | RC-2 §RC-2.2 | ❌ **KILLED** — p = 1 derived, then p = 1 withdrawn; p is ill-defined at leading order when T ~ A⁻² (ledger #13b) |
| **α_geom** | Geometric coefficient in Ω_drag = α_geom (Γ_dec/H₀)² | Paper 2A §3.3.5.3, RC-2 §RC-2.5 | 🤔 **UNVERIFIED** — claimed "exact from CP¹" but no traceable derivation |

The first two are dead. Only α_geom survives, and its value is not established.

**Resolution: retire α_spec and p from the notation entirely.** Use only **α_geom** going forward, and characterize it cleanly.

---

## RC-6.2 — The π Error in RC-2

### The error

RC-2 §RC-2.5 (Path C) writes:

$$\rho_{\rm drag} = \frac{3}{2} \cdot \frac{H_0^2}{G_4} \tag{RC-2, Eq. in §RC-2.5}$$

and then computes:

$$\rho_\Lambda \approx \frac{0.26\, H_0^2}{G_4}$$

giving ρ_drag/ρ_Λ ≈ 5.8. The "factor of 6" discrepancy in ledger item #23 refers to this ratio.

### The fix

The value 0.26 = 0.69 × 3/8 drops π from the Friedmann equation. The correct relation is:

$$\rho_{\rm crit} = \frac{3H_0^2}{8\pi G_4}, \qquad \rho_\Lambda = \Omega_\Lambda \cdot \rho_{\rm crit} = \frac{0.69 \times 3}{8\pi} \cdot \frac{H_0^2}{G_4} \approx 0.0824\, \frac{H_0^2}{G_4}$$

With the RC-2 formula ρ_drag = (3/2) H₀²/G₄:

$$\frac{\rho_{\rm drag}}{\rho_\Lambda} = \frac{1.5}{0.0824} \approx 18.2 \quad \text{(not 5.8)}$$

The "factor of 6" is actually a **factor of 18**.

### Which convention is correct?

Paper 2A §3.3.5.3 claims: "If Γ_dec ~ 0.68 H₀, this gives Ω_drag ~ 0.69."

Checking: with ρ_drag = (3/2) Γ²/G and Γ = 0.68H₀:
$$\Omega_{\rm drag} = \frac{\rho_{\rm drag}}{\rho_{\rm crit}} = \frac{(3/2)(0.68)^2 H_0^2/G}{3H_0^2/(8\pi G)} = \frac{3}{2} \cdot (0.68)^2 \cdot \frac{8\pi}{3} = 5.81$$

This gives Ω = 5.81, NOT 0.69. The stated claim is inconsistent with the stated formula.

The claim Ω_drag ~ 0.69 is only consistent with the formula:

$$\boxed{\Omega_{\rm drag} = \alpha_{\rm geom} \times \left(\frac{\Gamma_{\rm dec}}{H_0}\right)^2} \tag{RC6.1}$$

equivalently:

$$\rho_{\rm drag} = \alpha_{\rm geom} \times \frac{3\Gamma_{\rm dec}^2}{8\pi G_4} \tag{RC6.2}$$

RC-2's formula is missing the factor 3/(8π). The correct version has ρ_drag in units of ρ_crit, not H₀²/G.

**Action:** All instances of ρ_drag = α Γ²/G must be corrected to Eq. (RC6.2) or rewritten as Eq. (RC6.1). The ledger #23 "factor-of-6" entry is an artifact of the π error and should be withdrawn.

---

## RC-6.3 — The Logical Tension with λ·T = 1

### The constraint

RC-5 proves (as a universal theorem): the mixed tensor T^μ_r is r-independent for the vector zero mode on any warped background. Equivalently:

$$\lambda(r) \cdot T_{\rm kinetic}(r) = A^2(r) \cdot A^{-2}(r) = 1 \quad \forall\, r$$

### The naive implication

If the decoherence rate is Γ_dec = (λ · T) × H₀, then λ·T = 1 gives:

$$\Gamma_{\rm dec} = H_0 \quad \text{(exactly, at every r)}$$

Substituting into (RC6.1):

$$\Omega_{\rm drag} = \alpha_{\rm geom} \times 1 = \alpha_{\rm geom}$$

For Ω_drag = Ω_Λ = 0.69, this requires **α_geom = 0.69**, not 3/2.

### The escape: Γ_dec ≠ λ·T·H₀ literally

The identification Γ_dec = λ·T·H₀ is a parametric scaling argument, not a field-theoretic derivation. The actual decoherence rate comes from solving the sourced vector EOM:

$$\Box B_\mu^{(0)} = J_\mu^{\rm dec}$$

The source J depends on the cosmic expansion rate (hence the H₀ scale), but the precise coefficient involves:
- The normalization N₀ of the vector zero mode
- The overlap integral between the source and the mode profile
- Phase-space factors from the 4D → 5D embedding

The λ·T = 1 theorem guarantees Γ_dec = O(H₀) (the hierarchy is eliminated), but the precise coefficient **c** in Γ_dec = c·H₀ is determined by the sourced dynamics — which is RC-4 scope.

### The observational constraint

The dark energy density fixes the product:

$$\boxed{\alpha_{\rm geom} \times c^2 = \Omega_\Lambda = 0.69} \tag{RC6.3}$$

Neither α_geom nor c is independently derived. We have **one equation and two unknowns**.

If α_geom = 3/2: c = √(0.69/1.5) = **0.678** (the "0.68" quoted in §3.3.5.3 — but this was computed backward, not derived)

If c = 1 (naive λ·T = 1): α_geom = **0.69** (not 3/2)

---

## RC-6.4 — Provenance of α_geom = 3/2

### What the documents say

1. **Paper 2A §3.3.5.3:** "the geometric coupling constant α = 3/2 exact from CP¹"
2. **RC-2 §RC-2.5:** "α_geom = 3/2 is the CP¹ holographic area coefficient (zero-mode-weighted KCR backreaction integral; see Paper 2B §5.3.4.3, not rederived here)"
3. **Paper 2B §5.3.4.3:** "The α = 3/2 result (Phase 0–2 calculations, April 10 session)" — one paragraph, no derivation

### What the documents don't say

No document contains the actual integral that produces 3/2. The "Phase 0–2 calculations, April 10 session" are not archived in any RC document. The claim "exact from CP¹" is unsupported.

### Exact integral search

All Wallis integrals $I_n = \int_0^{r_{\max}} A^n(r)\,dr$ on the KCR-Cone were computed (§8 integral table). The systematic search for ratios equal to 3/2 found:

**Unique simple ratio:** $I_1/I_3 = \int_0^{r_{\max}} A\,dr \,\Big/\, \int_0^{r_{\max}} A^3\,dr = \frac{3}{2}$ exactly.

In terms of zero-mode profiles:
- $I_3 = \int \Psi_0^{(g)\,2}\,dr$ where $\Psi_0^{(g)} = A^{3/2}$ is the Schrödinger graviton zero mode
- $I_1 = \int A\,dr$ has no obvious physical role in the KK reduction

No physical derivation was identified that produces the ratio I₁/I₃.

**Near miss:** $N_0^2 \cdot I_6/I_2 = 10\sqrt{2}/(3\pi) \approx 1.5005$. This is the normalized vector energy density ∫N₀²A⁴·A²dr divided by the graviton normalization ∫A²dr. It is close to 3/2 but **not exactly** 3/2.

### Assessment

**α_geom = 3/2 is not derived.** The original computation is lost, the claimed provenance ("exact from CP¹") is untraceable, and the only exact integral giving 3/2 (I₁/I₃) lacks physical motivation. The near-miss N₀²I₆/I₂ ≈ 1.5005 is suggestive but not exact, and its physical interpretation (while more natural) doesn't match the claimed "graviton zero-mode-weighted" description.

---

## RC-6.5 — The Correct Formulation of Path C

### Clean version

The frame-dragging backreaction from the T_{MΣ} field produces:

$$\Omega_{\rm drag} = \alpha_{\rm geom} \times c_\Gamma^2 \tag{RC6.4}$$

where:
- $\alpha_{\rm geom}$ is a dimensionless geometric coefficient from integrating zero-mode profiles on the KCR-Cone
- $c_\Gamma = \Gamma_{\rm dec}/H_0$ is the ratio of the cosmic decoherence rate to the Hubble rate
- The λ·T = 1 theorem (RC-5) guarantees $c_\Gamma = O(1)$ (no hierarchy)

### What is established

| Quantity | Status | Source |
|----------|--------|--------|
| Parametric form Ω_drag ~ H₀²/G ~ ρ_crit | ✅ DERIVED | λ·T = 1 theorem (RC-5) removes hierarchy |
| c_Γ = O(1), not O(M_Pl/H₀) | ✅ DERIVED | λ·T = 1 theorem |
| α_geom = 3/2 | ❌ NOT DERIVED | No traceable calculation |
| c_Γ = 0.678 | ❌ NOT DERIVED | Computed backward from Ω_Λ, assuming α = 3/2 |
| α_geom × c_Γ² = 0.69 | ✅ OBSERVATIONAL CONSTRAINT | One equation, two unknowns |

### What is needed

1. **Derive α_geom** from the 5D action: compute the backreaction integral properly, using the known zero-mode profiles (N₀ from RC-3) and normalizations.

2. **Derive c_Γ** from the sourced EOM □B_μ = J_μ^{dec}. This is RC-4 item #22.

3. **Verify** that α_geom × c_Γ² = 0.69. If the product matches Ω_Λ from first principles, Path C becomes the most compelling result in the paper.

---

## RC-6.6 — Notation Consolidation

### Kill list

| Old notation | What it was | Replacement |
|-------------|-------------|-------------|
| α = 3/2 (spectral density) | Conjectured exponent in $\|T_M\|^2 \propto \Gamma^{3/2}$ | **Killed.** Weyl gives α = 1; route withdrawn (RC-1 #4) |
| p (dynamical exponent) | $\|T_M\|^2 \propto \Gamma^p$ | **Killed.** Ill-defined at leading order (ledger #13b) |
| α_geom = 3/2 (geometric coefficient) | Coefficient in Ω_drag formula | **Retained as α_geom, value OPEN** |
| ρ_drag = α Γ²/G | RC-2 formula | **Killed.** Replace with Ω_drag = α_geom c_Γ² or ρ = α × 3Γ²/(8πG) |
| "factor of 6" (ledger #23) | Discrepancy claim | **Killed.** Artifact of the π error. Actual status: α_geom underived |

### Surviving notation

| Symbol | Definition | Dimension | Status |
|--------|-----------|-----------|--------|
| α_geom | Geometric backreaction coefficient: Ω_drag = α_geom c_Γ² | dimensionless | **OPEN — value not derived** |
| c_Γ | Γ_dec/H₀ | dimensionless | **OPEN — requires sourced EOM (RC-4)** |
| λ_dist | HCR decoherence parameter = A²(r) | dimensionless | ✅ DERIVED (RC-5) |
| λ_bdry | Boundary coupling in S_bdry = λ_bdry ∫√γ Tr(T_M T_M†) | [M³] | OPEN |

---

## RC-6.7 — Impact on the Papers

### Paper 2A §3.3.5.3

**Current text:** "the geometric coupling constant α = 3/2 exact from CP¹. If Γ_dec ~ 0.68 H₀, this gives Ω_drag ~ 0.69"

**Problem:** α_geom = 3/2 is not "exact from CP¹" (no derivation). The 0.68 is computed backward from Ω_Λ. The claim is circular.

**Required revision:** State the *parametric* result (Ω_drag ~ c² × α_geom, both O(1), no hierarchy) as derived. Flag the coefficient as open. State the observational constraint α_geom × c² = 0.69 without claiming individual values.

### Paper 2B §5.3.4.3

**Current text:** One paragraph citing "Phase 0–2 calculations, April 10 session"

**Required revision:** Expand to state the correct formula (RC6.1/6.2). Remove the specific "α = 3/2" claim. State that α_geom is a KCR-Cone integral determined by the zero-mode profiles (now known from RC-3) and the backreaction structure (not yet computed).

### RC-2

**Current:** ρ_drag = (3/2) H₀²/G; "ρ_drag ≈ 5.8 ρ_Λ"; "factor of 6"

**Required revision:** Fix the π error throughout. Replace ρ_drag = α Γ²/G with Ω_drag = α_geom c_Γ². Retract the "5.8" and "factor of 6" claims.

### Open Items Ledger

**Item #23:** "Factor-of-6 in Path C Λ_eff" → **Retract.** Replace with: "α_geom underived; formula convention corrected (RC-6). Observational constraint: α_geom × c_Γ² = 0.69."

---

## RC-6.8 — KCR-Cone Integral Table (Reference)

Wallis integrals on the KCR-Cone, $A(r) = \cos(\sqrt{2}\,r)$, $r_{\max} = \pi/(2\sqrt{2})$:

| n | $I_n = \int_0^{r_{\max}} A^n\,dr$ | Exact | Numerical |
|---|-------------------------------------|-------|-----------|
| 0 | $\frac{\sqrt{2}\pi}{4}$ | $\frac{\pi}{2} \times \frac{1}{\sqrt{2}}$ | 1.11072 |
| 1 | $\frac{\sqrt{2}}{2}$ | $\frac{1}{\sqrt{2}}$ | 0.70711 |
| 2 | $\frac{\sqrt{2}\pi}{8}$ | $\frac{\pi}{4} \times \frac{1}{\sqrt{2}}$ | 0.55536 |
| 3 | $\frac{\sqrt{2}}{3}$ | $\frac{2}{3} \times \frac{1}{\sqrt{2}}$ | 0.47140 |
| 4 | $\frac{3\sqrt{2}\pi}{32}$ | $\frac{3\pi}{16} \times \frac{1}{\sqrt{2}}$ | 0.41652 |
| 5 | $\frac{4\sqrt{2}}{15}$ | $\frac{8}{15} \times \frac{1}{\sqrt{2}}$ | 0.37712 |
| 6 | $\frac{5\sqrt{2}\pi}{64}$ | $\frac{5\pi}{32} \times \frac{1}{\sqrt{2}}$ | 0.34710 |

Zero-mode normalizations:
- **Vector:** $N_0^2 = 1/I_4 = 16\sqrt{2}/(3\pi) \approx 2.401$, $N_0 \approx 1.549$
- **Graviton:** $N_g^2 = 1/I_2 = 4\sqrt{2}/\pi \approx 1.801$, $N_g \approx 1.342$

Unique ratio giving 3/2: $I_1/I_3 = 3/2$ exactly.

Near miss: $N_0^2 \cdot I_6/I_2 = 10\sqrt{2}/(3\pi) \approx 1.5005$.

---

## RC-6.9 — Remaining Questions

1. **What physical integral gives α_geom?** The backreaction calculation requires: (a) the 5D action for the T_μr field, (b) the sourced solution on the cosmological background, (c) integration over the extra dimension with appropriate metric weights. The known N₀ and mode profiles from RC-3 are inputs, but the backreaction structure itself is not written down.

2. **Is the near-miss 10√2/(3π) ≈ 1.5005 a coincidence?** This is the ratio N₀²I₆/I₂ — physically the normalized vector energy density with graviton measure, divided by the graviton normalization. If the actual backreaction integral has this structure, α_geom ≈ 1.5005 ≈ 3/2 to 0.035%, which would be a remarkable near-integer result. But it is NOT exactly 3/2.

3. **Can c_Γ be computed independently?** The sourced EOM □B_μ = J_μ^{dec} with J determined by cosmological dynamics would give c_Γ. Combined with α_geom, this predicts Ω_Λ — a zero-parameter prediction of the dark energy density.

---

## Revision History

| Date | Change |
|------|--------|
| 2026-04-18 | Initial audit — three α's identified and disambiguated; π error in RC-2 found and documented; logical tension with λ·T = 1 exposed; α_geom = 3/2 flagged as underived. |
