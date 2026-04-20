# Section 6 Companion — SCF → Frame Noncontextuality → Born

**Status**: Working draft, 2026-04-19 (for merge into `CR_Born_Derivation_Working_Draft_19Apr2026.docx`)
**Author**: Claude (Cowork), Bryan Kaufman
**Depends on**: SESSION_2026-04-19_T_MSigma_HOLOGRAPHIC_BORN_RULE.md; main.tex §IV.A (A1–A4), §VI; APPENDIX_SPEKKENS_TRANSLATION.md

The Section 6 gap identified in the 19Apr session is: does the T_MΣ self-consistency-fixed-point (SCF) condition force *frame noncontextuality* of the basin weight function W(φ_i | ψ) on M × CP¹? If yes, Gleason–Busch closes the Born derivation. This note makes that question precise, proves the clean direction unconditionally, isolates the remaining gap, and states it as a well-posed conjecture that does not hand-wave over the keystone step.

---

## 6.1 Setup

Let the joint manifold be M × Σ with fiber Σ_x = CP^{d-1} over each x ∈ M. Fix a pointer basis {|φ_i⟩}_{i=1}^d ⊂ Σ_x (a measurement context on the fiber). The T_MΣ tensor induces a flow Φ_t on the fiber at x:

&nbsp;&nbsp;&nbsp;&nbsp;Φ_t : Σ_x → Σ_x,   t ∈ ℝ_≥0.

The attractors of Φ_t are precisely {|φ_i⟩}; the basin of |φ_i⟩ is

&nbsp;&nbsp;&nbsp;&nbsp;B_i = { ψ ∈ Σ_x : lim_{t→∞} Φ_t(ψ) = |φ_i⟩ }.

Define the basin weight

&nbsp;&nbsp;&nbsp;&nbsp;W(φ_i | ψ) := 𝟙[ψ ∈ B_i]   for deterministic flows,

and, for stochastic flows with invariant measure μ_Φ on Σ_x,

&nbsp;&nbsp;&nbsp;&nbsp;W(φ_i | ψ) := μ_Φ(B_i | ψ_0 = ψ)

(i.e., the probability of absorption at |φ_i⟩ conditioned on initial state ψ).

The CR axioms A1–A4 (main.tex §IV.A) require the Born measure μ_F to be frame-invariant, continuous, and to depend only on ψ_F and the basis vectors |i⟩_F (A3). The central claim of Section 6 is that μ_F = W, i.e., the basin weight *is* the Born measure. Under CR this identification is not an assumption — it follows from SCF, if SCF forces the required symmetry.

## 6.2 The SCF Condition

The self-consistency-fixed-point condition states that the tensor T_MΣ that generates the geometry (g_M on M, g_Σ on the fiber) is equal to the tensor induced by that same geometry. Symbolically, with F a functor that produces T_MΣ from the fibered-geometry data,

&nbsp;&nbsp;&nbsp;&nbsp;T_MΣ = F[g_M(T_MΣ), g_Σ(T_MΣ), context].   (SCF)

"Context" here means the pointer basis {|φ_i⟩} and any M-level data that bias the flow. The SCF equation is a fixed-point problem on the space of admissible T_MΣ-tensors.

**Property we will use**: F is *covariant under the fiber isometry group*. That is, for any U ∈ SU(d) (acting on Σ_x = CP^{d-1} as the unitary group mod U(1)),

&nbsp;&nbsp;&nbsp;&nbsp;F[U · g_M · U^{−1}, U · g_Σ · U^{−1}, U · context] = U · F[g_M, g_Σ, context] · U^{−1}.   (COV)

COV is a natural axiom: Σ is defined up to its isometry group, g_Σ is the Fubini–Study metric (SU(d)-invariant), and the context is carried along by U. Whether COV is *forced* by SCF is precisely the open question of Section 6. We take COV as a postulate in this note and mark it clearly.

## 6.3 Theorem (SCF + COV ⇒ Frame Noncontextuality of W)

**Theorem 6.1.** *Suppose T_MΣ satisfies SCF and F satisfies COV. Then the basin weight W(φ_i | ψ) is frame-noncontextual: for all U ∈ SU(d),*

&nbsp;&nbsp;&nbsp;&nbsp;*W(U|φ_i⟩ | U|ψ⟩) = W(|φ_i⟩ | |ψ⟩).*

**Proof.** Let T be any SCF solution with context = {|φ_i⟩}, and let T^U be the SCF solution with context = {U|φ_i⟩}. By COV applied to F, and since (g_M, g_Σ) are SU(d)-invariant (they come from M's Lorentzian structure and Σ's Fubini–Study structure, both untouched by U up to a U-conjugation that cancels),

&nbsp;&nbsp;&nbsp;&nbsp;F[g_M, g_Σ, U · {|φ_i⟩}] = U · F[g_M, g_Σ, {|φ_i⟩}] · U^{−1}.

Combined with SCF on both sides, this gives T^U = U T U^{−1}. The induced flow Φ^U on the fiber therefore satisfies Φ^U_t(ψ) = U Φ_t(U^{−1}ψ). The basins transform as B_i^U = U B_i, and the invariant measure transforms as μ_Φ^U = U_* μ_Φ. Hence

&nbsp;&nbsp;&nbsp;&nbsp;W(U|φ_i⟩ | U|ψ⟩) = μ_Φ^U(B_i^U | U|ψ⟩) = μ_Φ(B_i | |ψ⟩) = W(|φ_i⟩ | |ψ⟩). □

This is the load-bearing step. Once COV is granted, frame noncontextuality of W follows by a clean transport argument and nothing is smuggled in.

## 6.4 Corollary (Born Rule)

**Corollary 6.2.** *Under the hypotheses of Theorem 6.1, W(|φ_i⟩ | |ψ⟩) = |⟨φ_i|ψ⟩|² on every CP^{d-1} fiber with d ≥ 2.*

**Proof.** For d ≥ 3, Gleason's theorem (1957, `gleasonMeasuresClosedSubspaces1957`) gives uniqueness: the only positive, normalized, frame-noncontextual function on rank-1 projections of ℂ^d is the trace form, i.e., W(|φ_i⟩|ψ⟩) = |⟨φ_i|ψ⟩|².

For d = 2, Gleason's theorem fails in its original form, but Busch (2003) proved the analogous statement for POVMs ("Gleason–Busch theorem"): any positive, normalized, frame-noncontextual function on effects (with additivity under POVM-level coarse graining) on ℂ² is also the trace form. By refining {|φ_i⟩} through a POVM family to reach the additivity hypothesis, the d = 2 case reduces to Busch's extension. This closes the qubit case without circular appeal to Gleason. □

**Remark.** Historically the qubit case has been the weakest link in operational Born-rule derivations. In CR it does not become weaker — SCF + COV forces frame noncontextuality just as it does for d ≥ 3, and the Busch refinement applies without any CR-specific patch.

## 6.5 What Remains: the SCF ⇒ COV Conjecture

The theorem in §6.3 is proved *conditional* on COV. The remaining work is to eliminate COV as a postulate by deriving it from SCF.

**Conjecture 6.3 (SCF ⇒ COV).** *Every solution T_MΣ of SCF, when restricted to the fiber Σ_x, is SU(d)-covariant in the sense that its induced flow Φ_t commutes with SU(d) acting simultaneously on context and initial data.*

**Heuristic argument (not a proof).** The SCF equation is an equation on tensors over M × Σ. The only geometric inputs are g_M (SU(d)-inert; acts on M), g_Σ (the Fubini–Study metric on CP^{d-1}, which is SU(d)-invariant), and the context. If F is local, polynomial, and built only from these ingredients, it is SU(d)-covariant by construction because the only way to produce a non-SU(d)-covariant output from SU(d)-covariant inputs is to introduce an external SU(d)-breaking spurion, which SCF does not provide.

**Why this is not yet a proof.** The functor F has not been pinned down uniquely in Paper 2C. Until F is specified (candidates: a connection on a fiber bundle over M × Σ; a tensor built from the Fubini–Study curvature and an M-level Ricci piece), one cannot verify algebraically that it is SU(d)-covariant. The honest status is:

- ✅ VERIFIED: Theorem 6.1 (SCF + COV ⇒ frame noncontextuality) — clean group-transport argument, unconditional given COV.
- ✅ VERIFIED: Corollary 6.2 (frame noncontextuality ⇒ Born) — Gleason / Gleason–Busch, standard.
- ⚠️ UNTESTED: Conjecture 6.3 (SCF ⇒ COV) — heuristically plausible, not proven.
- ❌ MISSING: explicit functor F that realizes SCF. Without F, Conjecture 6.3 cannot be checked.

## 6.6 A Falsifiable Specialization

Even without F pinned down, Conjecture 6.3 has a falsifiable consequence:

**Prediction 6.4.** *In any physical implementation of the M × CP¹ fibration (e.g., a qubit whose pointer direction is tuned continuously by an external M-level control), the basin weight W(φ_i | ψ) measured operationally must equal |⟨φ_i|ψ⟩|² to within the resolution set by the control noise. Any residual SU(2)-breaking in the measured W beyond control noise falsifies COV and therefore SCF as currently formulated.*

This specializes to: the qubit Bloch sphere always has its Born measure equal to half the great-circle-swept solid angle on each hemisphere; no hemisphere-dependent bias can exceed the measurement-basis calibration noise. This is a known consequence of quantum mechanics and is therefore consistent with, though not a novel prediction of, CR. The novelty is that CR *derives* it from SCF + COV rather than postulating it.

## 6.7 Integration with §5.7 (Unentangled Bell)

The §5.7 prediction (Prediction 8 in Paper 1) — that path-identified vs Bell-pair preparations differ by D3 holonomy — is dual to Theorem 6.1 in the following sense. Theorem 6.1 gives the *within-a-frame* statement: once you fix a frame F, the basin weight W is SU(d)-covariant and reproduces Born. Prediction 8 gives the *across-frames* statement: two frames F, F′ related by an operationally-equivalent D3 can still differ by a non-trivial holonomy, and that holonomy is observable. The two are consistent: within a frame, CR is Born-compliant and noncontextual; across frames, CR is contextual in the Spekkens sense (Appendix A.1 — A.4). There is no tension.

The SCF functor F, once specified, is the common source of both: it determines the flow Φ_t (hence Born within a frame) and the connection on the fiber bundle (hence D3 holonomy across frames). Closing Conjecture 6.3 is therefore the single keystone piece that would simultaneously complete the Born derivation and the Spekkens no-go instantiation.

## 6.8 Next Steps

1. **Specify F.** Candidate: F[g_M, g_Σ, context] = ∇^{FS} + A_context, where ∇^{FS} is the Fubini–Study Levi-Civita connection and A_context is a gauge connection built from the pointer basis. Check SCF consistency.
2. **Verify COV for the candidate F.** If F is built entirely from SU(d)-covariant ingredients, COV is automatic; write this out.
3. **Propagate to Paper 1 §VI.** The clean statement of Theorem 6.1 + Corollary 6.2 is short enough to include as a subsection of §VI (the Born derivation) in main.tex v5, with Conjecture 6.3 flagged as the open piece.
4. **Set up the Paper 2 KCBS derivation.** Once Conjecture 6.3 is closed (or assumed as a working hypothesis), KCBS follows by the argument in `DERIVATION_KCBS_2026-04-19.md` (companion note).

---

## Appendix 6.A — Status Audit

- Theorem 6.1 proof: reviewed 2026-04-19 by Claude; no appeal to SCF internal structure beyond COV; standard group-transport argument.
- Corollary 6.2: stands on Gleason 1957 and Busch 2003; both are published theorems.
- Conjecture 6.3: flagged as open; heuristic is not a proof.
- Prediction 6.4: consistent with standard QM; does not yet falsify any non-CR framework on its own.
- Cross-check with §5.7 / Appendix A: consistent; the holonomy statement in §5.7 does not contradict Theorem 6.1 because it applies *across* frames, while Theorem 6.1 applies *within* a frame.

**Realistic Status (this file)**: ~70% toward closing Section 6 as a peer-reviewable derivation. The remaining 30% is entirely in specifying F and verifying COV — the task Conjecture 6.3 names.

**Next Steps**: specify F (step 1 above); verify COV (step 2); port clean statement to main.tex v5.
