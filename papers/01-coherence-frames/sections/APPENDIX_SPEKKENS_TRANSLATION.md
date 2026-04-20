# Appendix A. Coherence Relativity in Operational / Ontic-Model Vocabulary

**Status**: Draft, integration candidate for Paper 1 v5
**Purpose**: Give the contextuality community a dictionary between CR objects (ψ_F, Σ, M, D_mixed, D3, μ, H_γ) and the operational / ontic-model objects used in Spekkens (2005), Abramsky–Brandenburger (2011), and the preparation-noncontextuality literature.
**Depends on**: main.tex §IV.A (A1–A4), §V (paradox resolution), §VI (Born), PARADOXES.md §5.0, §5.7.

---

## A.1 Why a Translation Is Necessary

CR is stated in geometric vocabulary: coherence frames on Σ, frame transformations D3, invariant measure μ, alignment domain D_mixed. The contextuality literature — which adjudicates whether a given interpretation of quantum mechanics is compatible with an ontic reconstruction — speaks in operational vocabulary: preparations P, transformations T, measurements M, response functions ξ(k|λ, M), and ontic distributions μ(λ|P). Without a dictionary the two literatures do not touch, and reviewers from either side will (correctly) mark the other as "not engaged with."

This appendix makes CR auditable in operational terms and states the CR-native form of preparation and measurement noncontextuality. The payoff is that the Spekkens (2005) no-go theorem and the Kochen–Specker (1967) theorem become *derived structural statements* in CR rather than imposed constraints — and the §5.7 unentangled-Bell instance becomes a concrete operational prediction.

---

## A.2 The Operational Framework (Spekkens 2005, summarized)

An **operational theory** specifies a set **𝒫** of preparation procedures, a set **𝒯** of transformation procedures, and a set **𝒯ₘ** of measurement procedures with outcomes k. For each triple (P, T, M) it gives the outcome distribution

&nbsp;&nbsp;&nbsp;&nbsp;p(k | P, T, M).

Two preparations P, P′ are **operationally equivalent** (written P ≃ P′) if

&nbsp;&nbsp;&nbsp;&nbsp;p(k | P, T, M) = p(k | P′, T, M)   for every T ∈ 𝒯, M ∈ 𝒯ₘ, k.

An **ontic model** for an operational theory is a measurable space (Λ, Σ_Λ) together with, for each P, a probability measure μ_P(λ), and, for each M, a response function ξ(k | λ, M), such that

&nbsp;&nbsp;&nbsp;&nbsp;p(k | P, M) = ∫ ξ(k | λ, M) dμ_P(λ).

**Preparation noncontextuality** (Spekkens 2005): if P ≃ P′ then μ_P(λ) = μ_{P′}(λ). **Measurement noncontextuality** (Kochen–Specker): if M, M′ assign identical statistics to *every* preparation, then ξ(·| λ, M) = ξ(·| λ, M′) for μ-almost-every λ. Ordinary QM is *contextual* in both senses (Kochen–Specker 1967 for measurements; Spekkens 2005 for preparations).

The contextuality question for an interpretation I is: *does I's ontology respect noncontextuality, violate it, or redefine it?*

---

## A.3 The CR Dictionary

The translation rests on one structural identification: **the coherence frame F is the ontic-model label λ, refined by a geometric context**. More precisely, Λ_CR = Σ, μ_P is the frame-pushed Born measure, and the response function is read off the accessible sector D_mixed.

| Operational object | CR object | Reference |
|---|---|---|
| Preparation P | Coherence frame F ∈ Σ + state ψ_F | §II, §IV |
| Preparations P ≃ P′ | Frames F, F′ with agreeing μ_F restricted to a measurement set Ξ | §5.0 meta-theorem |
| Transformation T | Frame transformation D3: F → F′ | §IV.D |
| Measurement M with outcomes {k} | Decomposition of accessible sector D_mixed in F into basis {|k⟩_F} | §IV.A, Def. 2 |
| Response function ξ(k|λ, M) | Overlap |⟨k|_F ψ_F⟩|² read in F | §VI Born |
| Ontic distribution μ_P(λ) | Frame-pushed Born measure μ_F on Σ | §VI.C |
| Operational equivalence class [P] | Σ-orbit of F under Ξ-preserving D3 | §III.C Universality Spectrum |
| Ontic distinction within [P] | Holonomy H_γ of D3 around a loop in Σ that fixes Ξ-statistics | §VI.C, §5.7 |

The dictionary is not merely a relabelling: it carries structural content. The response function in CR is *geometric* (Fubini–Study overlap between ψ_F and |k⟩_F), not an arbitrary stochastic function of an abstract hidden variable. That is why CR can *derive* contextuality theorems rather than simply postulate them.

---

## A.4 Preparation Contextuality as a CR Structural Theorem

**Proposition A.1 (CR-native preparation contextuality).** Let P, P′ be preparations with corresponding frames F, F′ ∈ Σ. Let Ξ = {M_k} be a measurement set. Suppose P ≃_Ξ P′ (operational equivalence restricted to Ξ). Then either
(a) F and F′ are connected by a D3 whose holonomy H_γ around a Ξ-preserving loop is the identity — in which case μ_F = μ_{F′} as ontic distributions on Σ, *and P ≃ P′ on every measurement set, not just Ξ*; or
(b) the holonomy is non-trivial, H_γ ≠ 𝟙 — in which case μ_F ≠ μ_{F′} as ontic distributions, and there exists a measurement set Ξ′ on which P and P′ give different statistics.

**Proof sketch.** By A1 (Frame Invariance, main.tex §IV.A), μ_F is a geometric invariant on Σ in the F-chart. By A3 (Dependence), μ_F(k) depends only on ψ_F and |k⟩_F, so agreement of μ_F, μ_{F′} on Ξ forces agreement of their Ξ-restrictions. The question is whether this agreement extends to all of Σ. Parallel transport of μ around the Ξ-preserving loop yields μ back to μ ∘ H_γ. If H_γ = 𝟙, μ_F = μ_{F′} on the full Σ; if H_γ ≠ 𝟙, the two measures differ on any basis sensitive to the holonomy kernel, producing a witnessing measurement set Ξ′. □

**Corollary A.2 (Spekkens no-go, CR derivation).** Preparation noncontextuality — the claim that P ≃ P′ ⇒ μ_P = μ_{P′} universally — holds iff the D3 holonomy on Σ is trivial on every Ξ-preserving loop. In standard QM Σ = ℂP^{n−1}, which has non-trivial Berry curvature on every generic loop; hence preparation noncontextuality fails generically. This is a structural, not contingent, consequence of the geometry.

**Remark on the 2025 unentangled-Bell experiment.** The Zhang et al. result (§5.7) is the experimental shadow of Proposition A.1(a)-vs-(b). On the CHSH measurement set Ξ, path-identified and Bell-pair preparations coincide; case (a) would require H_γ = 𝟙 on the loop connecting them, which would force the two preparations to remain ontically identical *on every extension* of Ξ. CR instead predicts case (b), with holonomy observable in the weak-measurement and delayed-erasure protocols of Prediction 8.

---

## A.5 Measurement (Kochen–Specker) Contextuality

**Proposition A.3 (CR-native Kochen–Specker).** Let M, M′ be measurements that share an observable O in the sense that O's spectral projections appear as a subset of each of their outcome bases. In CR, M and M′ correspond to two different decompositions of D_mixed in the same frame F. Suppose M ≃ M′ on all preparations — i.e., ξ(·| λ, M) and ξ(·| λ, M′) agree operationally. Then A3 (Dependence) forces them to agree pointwise on the F-ray of any ψ_F. However, since O's spectral projections sit inside non-commuting contexts of different basis completions, no single assignment v : {projectors} → {0,1} can be simultaneously frame-invariant and respect the projective decomposition of both M and M′ — *unless* the projectors belong to a maximal Abelian subalgebra. Outside that subalgebra, the assignment depends on the measurement context.

**Corollary A.4 (KS theorem, CR derivation).** For any Hilbert space dimension d ≥ 3, there exist collections of rays R ⊂ Σ such that no global value assignment v : R → {0,1} respecting orthogonality constraints exists. In CR this is the statement that D_mixed does not admit a frame-invariant classical section over R — i.e., A1 and A3 together forbid the existence of such a section. □

**Remark.** Kochen–Specker is therefore the *d ≥ 3 specialization* of the CR structural theorem that D_mixed has no frame-invariant classical section on non-Abelian subalgebras. KCBS (Cabello 2008, 5-cycle, d = 3) is the first non-trivial quantitative instance; deriving its ≤ 2√5 − √5 ≈ 0.944 bound from A1–A4 + D3 is the Paper 1 quantitative target (outstanding).

---

## A.6 What the Dictionary Buys Us

With A.3–A.5 in place, CR's relationship to the contextuality literature becomes precise:

1. **CR is a contextual ontic model in the Spekkens sense** — but the contextuality is not a free parameter; it is *forced* by the Σ-geometry via D3 holonomy.
2. **CR supplies the geometric origin story** for why quantum mechanics is contextual: the ontic state space is a fiber bundle over M rather than a product M × (classical Λ), and the fiber carries holonomy.
3. **CR makes quantitative predictions** in cases where the holonomy is non-trivial but the operational set Ξ is too narrow to detect it. The Zhang et al. experiment (§5.7) is such a case on the CHSH set; the delayed-erasure protocol in Prediction 8 extends Ξ to witness the holonomy directly.
4. **CR subsumes competing interpretations' contextuality stories**. Bohmian mechanics (Bohm 1952), Relational QM (Rovelli 1996), and QBism (Fuchs et al. 2014) each respond to Kochen–Specker differently; in the CR dictionary all three are restricted readings — Bohmian = single-frame ontic realism, RQM = frame-locality without holonomy geometry, QBism = frame-locality without ontic Σ. CR is the geometric completion they can all be projected onto.

This is the sense in which CR positions as "the formalization of contextuality": the contextuality theorems are structural consequences of A1–A4 + D3 on Σ, not constraints imposed from outside.

---

## A.7 Gaps and Open Items

- ⚠️ UNTESTED: the holonomy triviality criterion in Proposition A.1(a) is stated schematically; the precise measure-theoretic statement (which loops, which measurement sets Ξ preserve which structure) requires the Section 6 / SCF result from `CR_Born_Derivation_Working_Draft_19Apr2026.docx` to be closed.
- ❌ MISSING: the KCBS quantitative derivation referenced in Corollary A.4 — deferred to Paper 1 §VI.D or Paper 2.
- 🤔 UNKNOWN: whether Abramsky–Brandenburger's sheaf-theoretic obstruction cohomology H¹(Σ, …) coincides exactly with the CR holonomy group. Strongly suspected (both are first-cohomological obstructions to a global section), but unproven in this draft.
- Bibliography entries for Kochen–Specker, Spekkens 2005, Cabello 2008, Abramsky–Brandenburger 2011, Mazurek et al. 2016 are in `bibliography/master.bib` as of 2026-04-19.

## A.8 Citation Keys

For cross-reference with main.tex:
- Kochen–Specker 1967: `kochenSpeckerProblemHiddenVariables1967`
- Spekkens 2005: `spekkensContextualityPreparations2005`
- Cabello 2008 (KCBS): `cabelloTestableStateIndependent2008`
- Abramsky–Brandenburger 2011: `abramskySheafTheoreticStructure2011`
- Mazurek et al. 2016: `mazurekExperimentalTestNoncontextuality2016`
- Zhang et al. 2025 (§5.7): `zhangViolationBellUnentangled2025`
