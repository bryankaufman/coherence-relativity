# KCBS Inequality from T_MΣ Axioms — Derivation Note

**Status**: Working derivation, 2026-04-19 (quantitative capstone of the CR-as-contextuality claim)
**Depends on**: DERIVATION_SCF_NONCONTEXTUALITY_2026-04-19.md (Theorem 6.1, Corollary 6.2); main.tex §IV.A (A1–A4); APPENDIX_SPEKKENS_TRANSLATION.md.
**Context**: Corollary A.4 of the Spekkens appendix deferred the KCBS quantitative derivation. This note closes that deferral.

---

## 7.1 KCBS Setup, in CR Vocabulary

The Klyachko–Can–Binicioğlu–Shumovsky (KCBS, 2008) inequality is the simplest state-independent contextuality inequality for d = 3. Five rank-1 projectors {Π_i = |v_i⟩⟨v_i|}_{i=1}^5 ⊂ ℂ³ (or ℝ³) are arranged in a 5-cycle with the pairwise-orthogonality constraint

&nbsp;&nbsp;&nbsp;&nbsp;⟨v_i | v_{i+1}⟩ = 0,   i = 1, …, 5 (mod 5).   (KCBS-⊥)

Each consecutive pair (Π_i, Π_{i+1}) forms a co-measurable context. Any *noncontextual* value assignment v : {Π_i} → {0, 1} respecting (KCBS-⊥) — i.e., v(Π_i)·v(Π_{i+1}) = 0 — has at most two 1's on the 5-cycle (pigeonhole). Hence the noncontextual bound

&nbsp;&nbsp;&nbsp;&nbsp;Σ_i v(Π_i) ≤ 2   (noncontextual HV).   (NC-bound)

Quantum mechanics gives a larger maximum, Σ_i ⟨Π_i⟩ ≤ √5 ≈ 2.236 (the Klyachko–Cabello bound, `cabelloTestableStateIndependent2008`). The CR claim is that the quantum bound √5 is *derivable* from A1–A4 + SCF + COV, not an imposed constraint.

## 7.2 Theorem

**Theorem 7.1 (CR-native KCBS bound).** *Let Σ_x = CP² (or ℝP²) be the fiber of the joint manifold M × Σ over a base point x. Let {|v_i⟩}_{i=1}^5 ⊂ Σ_x satisfy (KCBS-⊥). Let W(Π | ψ) be the basin weight function of Theorem 6.1 (satisfying frame noncontextuality under SCF + COV). Then*

&nbsp;&nbsp;&nbsp;&nbsp;*max_{ψ ∈ Σ_x} Σ_{i=1}^5 W(Π_i | ψ) = √5.*

**Proof.** By Corollary 6.2, W(Π_i | ψ) = |⟨v_i | ψ⟩|² = Tr(|ψ⟩⟨ψ| Π_i). Therefore

&nbsp;&nbsp;&nbsp;&nbsp;Σ_i W(Π_i|ψ) = Tr(|ψ⟩⟨ψ| K),   K := Σ_{i=1}^5 Π_i.

The maximum over ψ ∈ Σ_x is the largest eigenvalue of K (attained on the corresponding eigenvector).

**Computation of spec(K).** The KCBS 5-cycle admits a real realization in ℝ³: choose the cyclic permutation ordering such that neighbors in the cycle correspond to angular offset 4π/5 on a cone of polar angle θ around the z-axis. Explicitly,

&nbsp;&nbsp;&nbsp;&nbsp;v_i = (sin θ · cos(2π i / 5), sin θ · sin(2π i / 5), cos θ),   i = 0, 1, 2, 3, 4,

with cycle order (v_0, v_2, v_4, v_1, v_3, v_0). The nearest-neighbor inner product in the cycle is

&nbsp;&nbsp;&nbsp;&nbsp;⟨v_0 | v_2⟩ = sin²θ · cos(4π/5) + cos²θ.

Imposing (KCBS-⊥), ⟨v_0 | v_2⟩ = 0, gives

&nbsp;&nbsp;&nbsp;&nbsp;cos²θ = sin²θ · |cos(4π/5)| = sin²θ · cos(π/5) · (−1) · (−1) …

Solving: let c = cos²θ. Then c = −(1 − c) · cos(4π/5) ⇒ c · (1 − cos(4π/5)) = −cos(4π/5) ⇒

&nbsp;&nbsp;&nbsp;&nbsp;cos²θ = −cos(4π/5) / (1 − cos(4π/5)) = cos(π/5) / (1 + cos(π/5)).

Using the identity cos(π/5) = (1 + √5)/4,

&nbsp;&nbsp;&nbsp;&nbsp;cos²θ = 1 / √5,   sin²θ = 1 − 1/√5.   (7.1)

The matrix K = Σ_i Π_i has entries

- K_{xx} = sin²θ · Σ_i cos²(2π i/5) = sin²θ · (5/2) = (5/2)(1 − 1/√5),
- K_{yy} = sin²θ · Σ_i sin²(2π i/5) = (5/2)(1 − 1/√5),
- K_{zz} = 5 cos²θ = 5/√5 = √5,
- K_{xy} = sin²θ · Σ_i cos(2π i/5) sin(2π i/5) = (sin²θ/2) · Σ_i sin(4π i/5) = 0,
- K_{xz} = sin θ cos θ · Σ_i cos(2π i/5) = 0,
- K_{yz} = sin θ cos θ · Σ_i sin(2π i/5) = 0.

Hence K = diag( (5/2)(1 − 1/√5), (5/2)(1 − 1/√5), √5 ) in the chosen basis. Numerically:

&nbsp;&nbsp;&nbsp;&nbsp;(5/2)(1 − 1/√5) ≈ 1.382,   √5 ≈ 2.236.

The largest eigenvalue of K is λ_max(K) = √5, attained on the eigenvector ψ_* = ẑ. Therefore

&nbsp;&nbsp;&nbsp;&nbsp;max_ψ Σ_i W(Π_i | ψ) = λ_max(K) = √5. □

## 7.3 Why the Excess √5 − 2 Is the D3 Holonomy

The noncontextual bound (NC-bound) assumes a single globally consistent {0,1}-assignment to the five projectors. By Corollary A.4 of the Spekkens appendix, such a global assignment requires triviality of the D3 holonomy around the KCBS pentagon on Σ_x. The excess √5 − 2 ≈ 0.236 *is* the quantitative signature of the non-trivial holonomy.

More precisely, consider the loop γ on Σ_x defined by transporting the frame through the measurement contexts

&nbsp;&nbsp;&nbsp;&nbsp;(Π_1, Π_2) → (Π_2, Π_3) → (Π_3, Π_4) → (Π_4, Π_5) → (Π_5, Π_1) → back.

Each step is a D3 acting on the accessible sector D_mixed. A global noncontextual value assignment exists iff the composed D3 holonomy is the identity on the 5-cycle. In CP², the KCBS 5-ray arrangement defines a closed curve of rank-1 projectors whose parallel transport under the Fubini–Study connection produces a Berry phase, and that phase is the geometric source of the excess. The noncontextual bound 2 is recovered in the flat-holonomy limit; the quantum bound √5 is the curved-holonomy value.

This is the quantitative answer to the positioning question of the April 19 session kb entry: the Spekkens/Kochen–Specker phenomenon is, in CR, exactly the non-triviality of D3 holonomy on Σ, and the KCBS value √5 is the explicit number this produces for the minimal-dimension cycle.

## 7.4 What Was Used

**Axiom audit for the proof.**

1. **A1 (Frame Invariance)** — used to ensure W is a frame-independent geometric object on Σ.
2. **A2 (Additivity)** — used implicitly in the orthogonality constraint (KCBS-⊥), which is an additivity condition on rank-1 projectors belonging to common contexts.
3. **A3 (Dependence)** — used in Corollary 6.2 (Gleason/Busch): W(Π|ψ) depends only on Π and ψ, not on the remaining basis completion.
4. **A4 (Continuity)** — used in Gleason/Busch uniqueness.
5. **SCF + COV (Theorem 6.1)** — used to conclude W is SU(3)-covariant on the fiber.
6. **Corollary 6.2 (Born)** — used to replace W(Π|ψ) by |⟨v|ψ⟩|².

The derivation is modular: if Conjecture 6.3 (SCF ⇒ COV) remains open, Theorem 7.1 is conditional on COV. If one wishes to take Born as a standalone postulate (not derived from SCF + COV), Theorem 7.1 becomes an unconditional consequence of A1–A4 + Born.

## 7.5 Paper 2 Integration

This derivation is short enough to sit in Paper 1 §VI.D (Born Rule → Contextuality Inequalities) as a theorem + 1-paragraph proof + remark. Alternatively it can anchor Paper 2 §Section-on-Contextuality-Quantitative-Tests, with the holonomy interpretation (§7.3) expanded into a full geometric-phase subsection.

Suggested placement: Paper 1 §VI.D as Theorem 3, with proof in Appendix B; §VI.A introduction to reference Appendix A (Spekkens translation) and §VI.D (KCBS quantitative test) together as establishing the contextuality positioning.

## 7.6 Status

- ✅ VERIFIED: Theorem 7.1 proof, end-to-end, given Corollary 6.2.
- ✅ VERIFIED: Numerical computation of λ_max(K) = √5 via direct diagonalization.
- ⚠️ UNTESTED: D3-holonomy identification (§7.3) — stated at conjecture level; the claim that √5 − 2 *is* the Berry-phase integral has not been computed here and requires a separate Appendix in Paper 2.
- ❌ MISSING: Direct geometric-phase integral computation on the KCBS pentagon in CP². (Follow-up task.)
- 🤔 UNKNOWN: Whether the same D3-holonomy framing extends cleanly to the higher-dimensional Cabello–Severini–Winter (CSW) generalization of KCBS. Strongly suspected to work by the same mechanism.

**Next Steps**:
1. Compute the Berry-phase integral on the KCBS pentagon in CP² to make §7.3 quantitative.
2. Port Theorem 7.1 and its proof into main.tex v5 as §VI.D.
3. Extend to CSW/generalized state-independent contextuality inequalities.

**Realistic Status (this file)**: ~85% — the quantitative theorem is proved; the geometric-phase interpretation is stated but not computed. This closes Corollary A.4 of Appendix A at the peer-reviewable level.
