# C4 Axiom Decision — d=2 Born Rule Closure
**Date**: 2026-05-01
**Status**: DECISION MADE — Adopt Busch 2003 as stated working axiom
**Closes**: omnibus #39 (C4 POVM additivity for d=2), 2C ledger item #21

---

## The Issue

The Born rule derivation in Paper 2C §6 (Theorem 7.1, SU(2) Born lemma) requires a fifth condition beyond the four established in Paper 1:

- (C1) Continuity
- (C2) f(x) + f(1-x) = 1
- (C3) f(1) = 1
- (C4) **POVM additivity** (affine linearity): W(αE₁ + βE₂|ψ) = αW(E₁|ψ) + βW(E₂|ψ)

Without (C4), the counterexample f_ε(x) = x + ε·x(1-x)(2x-1) satisfies (C1)–(C3) for any ε ∈ (0,1) but is not the Born rule. The derivation chain is: (C1)–(C4) + SU(2)-equivariance + repeatability + two-outcome normalization ⇒ f(x) = x = W(↑|θ) = cos²(θ/2).

---

## Derivation Routes Tried (Both Fail or Underdeveloped)

### Route A: Fokker-Planck via isotropic noise on S²
**Status**: ❌ CLOSED — Definitively fails.

The isotropic Lyapunov flow (-∇V drift + isotropic Brownian noise on S²) does not produce W(φ|ψ) = |⟨φ|ψ⟩|² as the absorption probability. The detailed calculation (DERIVATION_C4_FOKKER_PLANCK_2026-04-20.md, §§4–8) shows:

- For σ → 0: The absorption probability concentrates at the south pole (θ = π), giving p(u) → 0 for all u < 1. ❌
- For σ > 0 fixed: The exponential weight e^{-arcsin(t)/(2σ)} makes the absorption asymmetric; p(0) ≠ 1/2. ❌
- The drift V(θ) = cos²(θ/2) and its gradient do NOT produce p(u) = (1+u)/2 for any isotropic noise model.

**Root cause**: The absorption probability p satisfies Lp = 0 where L includes *both* drift and diffusion. Having V(θ) as a Lyapunov function for the deterministic part does NOT imply p ∝ V for the full stochastic generator. These are logically independent.

### Route B: Non-isotropic noise tied to T_MΣ
**Status**: ⚠️ Possible but undeveloped.

The DERIVATION_C4_FROM_SCF_2026-04-20.md identifies that a noise term proportional to σ(r) = λ(r)² = e^{-4μr} (r-dependent, from the 5D coupling) breaks the pathology of isotropic noise by ensuring λ·T = O(1) (the uniform noise regime). The argument is:

1. The T_MΣ flow with position-dependent noise σ(r) avoids concentration at the south pole.
2. Approach 1 (direct CPTP from Fokker-Planck) is "viable" in principle.
3. BUT: The explicit gap is that the generator L is a valid Lindblad-type operator on L²(ℂP¹) has **not** been verified. The Stinespring dilation or Kraus representation bridging the classical Markov semigroup to a quantum channel M₂(ℂ) has **not** been constructed.

**Assessment**: This route could work, but it requires:
1. Explicit computation that σ(r) = λ(r)² gives absorption probability p(u) = (1+u)/2
2. Construction of the Stinespring dilation
3. Verification that the result is independent of the specific r-profile

These are 2-3 weeks of mathematical work that have not been done. The route remains open but undeveloped.

### Route C: CDP theorem (SU(2)-equivariance → POVM)
**Status**: ⚠️ Potentially circular.

The Chiribella-D'Ariano-Perinotti (CDP) theorem states: an SU(d)-equivariant positive normalized function on ℂP^{d-1} is a POVM. If this applies, (C4) follows automatically from SU(2)-equivariance (Theorem 6.1).

**The circularity concern** (identified in DERIVATION_C4_FROM_SCF §3): The CDP theorem requires the assignment to be *a priori* linear in effects. This is exactly what (C4) asserts. Invoking CDP to prove (C4) is therefore circular unless an independent proof of the linear extension is given.

**Assessment**: Not a clean derivation path without additional work.

---

## Decision: Adopt Busch 2003 as a Stated Working Axiom

**Rationale**:

1. **The counterexample is real.** f_ε(x) = x + ε·x(1-x)(2x-1) is a genuine counterexample to (C1)–(C3) alone. (C4) is a mathematically necessary additional condition.

2. **Busch 2003 provides rigorous coverage.** Busch (2003) "Quantum States and Generalized Observables: A Simple Proof of Gleason's Theorem" (Phys. Rev. Lett. 91, 120403) proves that any positive operator-valued measure on a qubit satisfying normalization is of the Born-rule form. This is precisely (C4) + standard conditions. The reference is rigorous, well-cited, and specifically addresses the d=2 case.

3. **This is the honest academic position.** The Fokker-Planck route has been tried and closed (Route A). Route B is open but undeveloped and represents 2-3 weeks of additional work. Route C is potentially circular. Publishing Paper 2C with Busch 2003 as a stated working axiom is:
   - Mathematically honest (no false claim of derivation)
   - Academically credible (Busch 2003 is a published rigorous result)
   - Publishable immediately (no open gap)
   - Leaves Route B open for future work (could become a strengthening paper)

4. **The philosophical position is stronger than it looks.** Axiom (C4) — POVM additivity — is weaker than Gleason's original non-contextuality and is independently well-motivated: it says that quantum measurement implements a POVM, which is standard quantum theory. The Born rule derivation in Paper 2C derives it for d ≥ 3 via Gleason (which does not require (C4)); for d = 2 specifically, Busch 2003 supplies the missing ingredient. This is a genuine strength, not a weakness.

---

## Manuscript Instruction

**Paper 2C §6 (Corollary 6.2) should read:**

> **Corollary 6.2 (Noncontextuality ⇒ Born, d ≥ 2).** Under the hypotheses of Theorem 6.1, the unique positive, normalized, SU(d)-equivariant function on rank-1 projections is the Born measure W(|φᵢ⟩|ψ⟩) = |⟨φᵢ|ψ⟩|².
>
> *For d ≥ 3*: Gleason's theorem (1957) applies directly: the unique positive normalized frame-noncontextual function on rank-1 projections of ℂ^d is the trace form.
>
> *For d = 2*: Gleason's theorem does not apply in its original form. We adopt the Busch (2003) extension to effects under POVM-additivity as a **working axiom (C4)**. Busch (2003) establishes that any positive normalized POVM-additive function on CP¹ is the Born measure. The POVM-additivity condition (C4) is equivalent to standard quantum measurement theory and is not independently derived here; derivation from T_MΣ dynamics remains open. *(See Appendix for the status of Route B via non-isotropic noise.)*

**Bibliography entry** (already in master.bib or to be added):
```
@article{Busch2003,
  author  = {Busch, Paul},
  title   = {Quantum States and Generalized Observables: A Simple Proof of Gleason's Theorem},
  journal = {Physical Review Letters},
  volume  = {91},
  pages   = {120403},
  year    = {2003},
  doi     = {10.1103/PhysRevLett.91.120403}
}
```

---

## Impact on 2C Status

| Item | Before | After |
|---|---|---|
| d=2 Born rule (C4) | ⚠️ Working axiom, no justification | ✅ Working axiom, Busch 2003 cited |
| Path B (non-isotropic noise) | ❌ Not attempted | ⚠️ Open for future work, documented |
| Route A (isotropic Fokker-Planck) | ❌ Unclear status | ❌ Definitively closed (documented) |

**Net**: Paper 2C §6 is now publication-ready with an explicit working axiom + authoritative reference for d=2. The Fokker-Planck investigation is documented as a closed negative result (which has independent value: it constrains which noise models cannot derive (C4)).

---

## Open for Future Work: Route B (Non-Isotropic Noise)

Route B remains open and has a plausible structure. To close it would require:

1. **Compute** p(u) = absorption probability for the r-dependent noise model σ(r) = λ(r)² = e^{-4μr} on S².
2. **Show** p(u) = (1+u)/2 (the Born measure).
3. **Construct** the Stinespring dilation bridging the Fokker-Planck propagator (classical Markov on L¹(S²)) to a quantum channel on M₂(ℂ).
4. **Verify** the result is independent of the specific form of σ(r) (depends only on λ·T = O(1)).

If closed, this would upgrade d=2 Born from "stated axiom (Busch)" to "derived from T_MΣ dynamics" — a paper-worthy result in its own right.

**Recommended venue for Route B**: Either a short standalone note or a section of Paper 5 (transformer program), since the result would establish the Fokker-Planck-to-quantum-channel bridge that the transformer formalism needs anyway.

---

*Decision made 2026-05-01. Closes 2C ledger item #21 and omnibus #39.*
