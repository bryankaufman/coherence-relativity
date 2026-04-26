# M2: Spekkens Positioning + Lemma 1 Draft
**Date**: 2026-04-26
**Sources**: DERIVATION_SCF_NONCONTEXTUALITY_2026-04-19.md §6.3, §6.7; DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md §3–6; DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20.md

---

# PART 1 — M2: Spekkens Positioning for Theorem 6.1

## The Precise Relationship

**Spekkens preparation-noncontextuality (2005, PRA 71, 052108):** Two preparation procedures P and P' are *operationally equivalent* if they yield identical outcome statistics for every possible measurement. Spekkens' noncontextuality principle requires that operationally equivalent preparations receive identical ontological representations. Violation is *preparation contextuality*.

**HCR frame-noncontextuality (Theorem 6.1):** The basin weight W(φ_i | ψ) satisfies:
W(U|φ_i⟩ | U|ψ⟩) = W(|φ_i⟩ | |ψ⟩)  for all U ∈ SU(d).
This is SU(d)-equivariance of W — simultaneously rotating both pointer state and input state by U leaves Born statistics unchanged.

**Precise relationship — three levels:**

1. **HCR is Spekkens-noncontextual for frame-equivalent preparations.** Two preparations that differ only by a coherence-frame rotation U ∈ SU(d) have identical outcome statistics (by Theorem 6.1) and receive the same W-value. For this restricted class, HCR satisfies Spekkens' principle.

2. **HCR is Spekkens-contextual across frames.** Two operationally equivalent preparations in *different* coherence frames (related by a non-trivial frame holonomy, not a mere SU(d) rotation) may receive different coherence-frame representations. The D3 holonomy prediction (Paper 1, Prediction 8) is the signature of this across-frame contextuality: two Bell preparations that are locally operationally equivalent but frame-holonomy-separated receive different geometric representations. This is an explicit Spekkens-contextual scenario.

3. **HCR Theorem 6.1 is strictly weaker than Spekkens preparation-noncontextuality** for the full theory (all preparations), but is equivalent to it for the subclass of frame-equivalent preparations.

**Position in the contextuality hierarchy:**
- Spekkens full preparation-noncontextuality: covers ALL operationally equivalent preparations → violated by HCR across frames
- KS/KCBS measurement contextuality: covers measurement settings → tested by KCBS inequalities (DERIVATION_KCBS_2026-04-19.md)
- HCR frame-noncontextuality (Theorem 6.1): SU(d)-equivariance within a fixed frame → satisfied given COV

---

## Draft Paragraph for Paper 2C (insert before/after Theorem 6.1)

**Relation to Spekkens generalized noncontextuality.** Theorem 6.1 establishes that the basin weight W(φ_i | ψ) is SU(d)-equivariant within a fixed coherence frame — a form of *within-frame noncontextuality*. We briefly situate this result within the generalized noncontextuality program \cite{Spekkens:2005} to prevent both under- and over-claiming.

Spekkens' preparation-noncontextuality principle requires that any two preparation procedures yielding identical outcome statistics for every possible measurement be assigned identical representations in any valid ontological model. Theorem 6.1 is consistent with Spekkens' principle for the class of *frame-equivalent preparations*: two preparations differing only by U ∈ SU(d) have identical Born statistics and receive the same W-value. In this restricted class, HCR satisfies Spekkens' noncontextuality.

The full HCR theory is, however, Spekkens-contextual *across* frames. Two operationally equivalent preparations related by a non-trivial frame holonomy receive different coherence-frame representations in HCR. The D3 holonomy prediction (Paper 1, Prediction 8 \cite{Kaufman:Paper1}) is the primary observable signature: two Bell-state preparations that are operationally equivalent for local measurements but holonomy-separated are geometrically distinguishable in HCR. There is no tension with Theorem 6.1, which applies within a fixed frame.

Whether HCR violates Kochen-Specker-type *measurement* contextuality inequalities is a separate question addressed in §8.3 (Quantum Zeno) and in the KCBS analysis of \cite{internal:KCBS}. The outcome is consistent with Theorem 6.1: within-frame noncontextuality does not preclude KS-type contextuality at the level of measurement sequences.

In summary: Theorem 6.1 establishes within-frame noncontextuality (SU(d)-equivariance of W), which is a necessary condition for Spekkens' full principle within frame-equivalent preparations but not sufficient for the full principle across all preparation equivalences. HCR occupies a precise position: Born-compliant and SU(d)-noncontextual within a frame; genuinely Spekkens-contextual across frames, with the contextuality being physically observable via coherence holonomy.

---

## Status of M2

- ✅ Positioning is accurate given DERIVATION_SCF_NONCONTEXTUALITY_2026-04-19 §6.7
- ✅ No new derivation needed — framing paragraph only
- ⚠️ The claim "frame-equivalent preparations are operationally equivalent" needs formal verification against Spekkens' operational definition. It is plausible by construction but not explicitly checked in the derivation files.
- ❌ KCBS analysis (DERIVATION_KCBS_2026-04-19.md) still needs to be merged into Paper 2C §8 before submission

---
---

# PART 2 — Lemma 1: SCF Saturation Surface ≡ λ=1 Holographic Projection Surface

## Preliminary: Resolving the λ Convention Ambiguity

Before stating Lemma 1, a notation ambiguity must be resolved. The synthesis skeleton (SYNTHESIS_EMANATION_INSTANTIATION_LOCUS_2026-04-26.md §1.3) states:

> "ξ_0(x) := arg max_{ξ ∈ Σ} λ(x, ξ) — boundary ray on Σ over each x ∈ M... with λ=1 = full distinguishability/classicality and λ=0 = full coherence."

This is the **EGY convention** from Paper 1: λ=1 means maximally distinguishable (classical, pointer-like), λ=0 means maximally coherent.

However, Paper 2A §2.2 uses the **coupling convention**: "λ=0 (classical limit): spacetime and coherence sectors are completely distinguishable (separable)..." and "λ=1 (quantum regime): sectors maximally coupled."

**These are opposite orientations.** The synthesis skeleton explicitly adopts the EGY convention (λ=1 = classical). Lemma 1 is stated and proved under the EGY convention throughout.

The Paper 2A coupling λ satisfies λ_coupling = 1 - λ_EGY to leading order (they measure complementary aspects of the same physical parameter). **This notation inconsistency between Paper 1/synthesis (EGY: λ=1 classical) and Paper 2A §2.2 (coupling: λ=0 classical) should be reconciled in Paper 2A §1.6 as part of the cross-paper notation table.** This is a manuscript-discipline task, not a physics task.

---

## Lemma 1 Statement

**Lemma 1 (SCF Saturation ≡ λ_EGY = 1 Surface).** *Let λ_EGY: Σ_x → [0,1] be the EGY distinguishability parameter on the fiber Σ_x = CP^{d-1} over x ∈ M. Let {|φ_i⟩}_{i=1}^d be the pointer basis at x (the attractor set of the T_MΣ-induced flow Φ_t). Then:*

*(i) λ_EGY(|φ_i⟩) = 1 for each pointer state |φ_i⟩.*

*(ii) For any ψ ∈ Σ_x that is not a pointer state, λ_EGY(ψ) < 1.*

*(iii) Consequently, arg max_{ξ ∈ Σ_x} λ_EGY(x, ξ) = {|φ_i⟩}_{i=1}^d — the SCF saturation surface coincides with the λ_EGY = 1 surface.*

---

## Proof of Lemma 1

**Setup.** The EGY parameter λ_EGY is defined as λ_EGY = √(1 - |⟨W_L | W_R⟩|²), where W_L and W_R are the two which-path states in the two-slit analogy, or more generally as the statistical distinguishability between the state ψ and the pointer basis state |φ_i⟩ that is closest to ψ (measuring how "definite" the state is in the pointer basis).

More precisely, for a pure state |ψ⟩ = Σ_i c_i |φ_i⟩ in the pointer basis {|φ_i⟩}:

  λ_EGY(ψ) := 1 - max_i |c_i|²

This measures how much |ψ⟩ is *not* a pointer state: it is 0 when |ψ⟩ = |φ_j⟩ for some j (no distinguishability needed — already definite), and approaches 1 when all |c_i|² = 1/d (maximally coherent superposition — maximally hard to distinguish which pointer state will be recorded). 

*[Notation note: this is the complementary convention from λ_EGY = 0 meaning coherent (Paper 1's two-slit λ). The synthesis uses λ_EGY = 1 for classical, λ_EGY = 0 for coherent — so under the synthesis convention, λ_synthesis = 1 - λ_EGY_Paper1. This is the source of the apparent sign flip between Paper 1 and the synthesis. Both are consistent under the appropriate translation.]*

Under the synthesis convention (λ_synthesis ∈ [0,1], λ_synthesis = 1 means classical/pointer-like):

  λ_synthesis(ψ) = max_i |⟨φ_i | ψ⟩|²

This equals 1 iff |ψ⟩ is a pointer state |φ_j⟩, and is strictly less than 1 for any superposition. ✓

**Proof of (i).** For |ψ⟩ = |φ_j⟩: λ_synthesis = |⟨φ_j | φ_j⟩|² = 1. □

**Proof of (ii).** For |ψ⟩ = Σ_i c_i |φ_i⟩ with |c_i|² < 1 for all i (genuine superposition): max_i |⟨φ_i | ψ⟩|² = max_i |c_i|² < 1. □

**Proof of (iii).** From (i) and (ii), max_{ξ ∈ Σ_x} λ_synthesis(x, ξ) = 1, achieved exactly at the pointer states {|φ_i⟩}. These are also the SCF-saturated states (the attractors of the flow Φ_t; exact fixed points in the constant-basis branch, Banach-unique fixed points in the QM regime of the varying-basis branch). Therefore arg max_ξ λ_synthesis(x,ξ) = {|φ_i⟩} = SCF saturation set. □

---

## What Lemma 1 Establishes (and What It Does Not)

**Established:**
- Under the synthesis convention for λ, the SCF saturation surface and the λ=1 surface on each fiber Σ_x coincide exactly.
- This means 𝒫_holo (which projects to ξ_0 = arg max λ) projects to the pointer states — precisely the SCF-attractor states.
- The synthesis theorem §3 "matching condition" is now a theorem, not an assumption.

**Not established (residual openings):**
1. The proof uses λ_synthesis = max_i |⟨φ_i|ψ⟩|², which is the most natural choice given the synthesis convention. Whether this is *forced* by the SCF structure or is an additional input depends on pinning down the definition of λ in the SCF context. In the derivation files, λ is introduced phenomenologically, not derived from SCF. This is the structural question that remains open.

2. The proof treats the fiber in isolation at a fixed x ∈ M. The global statement — that the section {ξ_0(x)}_{x∈M} forms a smooth section of the bundle Σ → M — requires an additional smoothness argument (that the arg max of a smooth function on smooth fibers varies smoothly). This holds generically but has not been checked at the degenerate/boundary cases.

3. The identification λ_synthesis = max_i |⟨φ_i|ψ⟩|² is the *fiber-level* λ. The full λ(x,ξ) on M × Σ also has M-dependence through the pointer basis {|φ_i(x)⟩} varying over x. Lemma 1 gives the fiber result; the statement that ξ_0(x) varies smoothly with x is the additional content needed for the bundle picture.

---

## Impact on the Synthesis Theorem

The synthesis theorem §3 proof sketch says:
> "(III) follows from §2.3 + the matching condition that 𝒫_holo respects ξ_0 = arg max λ"

Lemma 1 provides this matching condition as a theorem (under the synthesis λ convention and with the caveats above). The synthesis theorem can now be stated:

**Corollary (improved statement of Synthesis §3 proof).** *Under the synthesis convention λ_synthesis = max_i |⟨φ_i(x)|ψ⟩|², the holographic projection 𝒫_holo: M × Σ → M × {ξ_0} respects the SCF-saturation structure: ξ_0(x) = arg max λ_synthesis(x,·) = the pointer states of the SCF flow at x. The boundary fibration ∂M × Σ is therefore the locus where SCF is saturated (pointer states reached) and λ_synthesis = 1 simultaneously. These are not two independent conditions — they are the same condition under Lemma 1.*

---

## What Still Needs to Be Done

1. **Notation reconciliation**: Update Paper 2A §1.6 notation table to clarify λ_EGY (Paper 1/synthesis: classical=1) vs λ_coupling (Paper 2A §2.2: classical=0). One of these needs to be renamed to avoid reader confusion. Recommended: keep λ for EGY/synthesis convention throughout (λ=1 classical); rename Paper 2A §2.2's coupling parameter to μ or κ_coupling.

2. **Smooth section argument**: Verify that ξ_0(x) = arg max_ξ λ(x,ξ) varies smoothly with x under the SCF dynamics. This is a technical smoothness check, not a conceptual gap.

3. **Definition of λ from SCF**: Pin down whether λ_synthesis = max_i |⟨φ_i|ψ⟩|² is the definition of λ in the HCR framework or a derived identity. If it's a definition, Lemma 1 is a tautology; if it's derived, Lemma 1 has more content. The synthesis skeleton should be explicit about this.
