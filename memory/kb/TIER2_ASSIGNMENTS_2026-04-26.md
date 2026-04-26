# Tier 2 Assignment Recommendations
**Date**: 2026-04-26
**Produced by**: Claude/Opus
**Context**: Four open mathematical gates block full closure of the HCR series.
This document assigns each gate to a primary agent, critic, and support role.

**Division of labor principle (established through prior collaboration):**
- Warp/Oz: derivation-primary (has in-file context, drives new calculation)
- Claude/Opus: critique-primary (synthesis-level reasoning, premise consistency, literature)
- Perplexity: literature support (targeted scans, citation verification)

---

## G1 — Conjecture 6.3′: Gauge Uniqueness of A_C

**What it is:** Proof that the SCF/COV-pinned coherence connection A_C is unique up to gauge within the canonical gauge class.

**Primary:** Warp/Oz — has DERIVATION_SCF_FIXED_POINT_SUBSTITUTION and SCF chain context loaded.

**Critic:** Claude/Opus — reviews gauge-group choice, premise consistency, rigidity argument structure.

**Literature support:** Perplexity — Wilczek–Zee non-Abelian connection literature for the degenerate-pointer extension that depends on G1's closure.

**Pre-computation decision needed:** What gauge group is actually in play under SCF + COV constraints — full U(d), SU(d), or a stabilizer-narrowed subgroup? Warp should resolve this question first; Claude reviews the choice before the proof body is written.

**Realistic timeline:** 4–6 weeks of Warp calendar time; ~1 week of Claude review spread across that.

**Unlocks:** Full Born chain closure (§2.1); Theorem 6.1 becomes unconditional.

---

## G2 — α Reconciliation: RESOLVED (2026-04-26, Claude/Oz diagnostic)

**Resolution: Category error — the two quantities are NOT the same thing.**

Verified analytically:
- α_geom = N_0² · I_6/I_2 = 10√2/(3π) ≈ 1.50053 — the dark-ENERGY coupling coefficient in
  Ω_drag = α_geom · c_Γ². This is the DERIVED result from KCR zero-mode backreaction integrals.
  Exact: I_6/I_2 = 5/8, N_0² = 16√2/(3π), so α_geom = 10√2/(3π). ✅ CLOSED.
- q = 3/2 — the CONJECTURED baryon-tracking exponent in the phenomenological ansatz
  ρ_DM ~ λ² ρ_b^q for the dark matter limit. This is an OPEN conjecture. ⚠️

Paper 2C line 444 states explicitly: "This illustrative baryon exponent q is NOT tied to the
geometric dark-energy coefficient α_geom; the latter is fixed independently by the KCR
zero-mode backreaction integral (RC-8b)."

The 0.035% numerical proximity (|α_geom - 3/2| / (3/2) = 0.035%) is a coincidence in the
sense that these two numbers answer completely different physical questions.

**No calculation needed.** G2 as originally stated (α reconciliation) is dissolved.

**Replacement open item:** RC-2 — derive q (baryon tracking exponent) from CP¹ spectral
density. Can the power-law ρ_DM ~ λ² ρ_b^q be derived with q = 3/2 from KCR geometry?
This is the genuine open calculation, now cleanly named.

**Realistic timeline for RC-2:** multi-week (separate from the now-closed α_geom question).

**Unlocks:** Dark-matter prediction from first principles (not just the phenomenological ansatz).

---

## Lemma 1 — SCF Saturation ≡ λ = 1 Surface Matching Condition

**What it is:** The synthesis theorem (SYNTHESIS_EMANATION_INSTANTIATION_LOCUS_2026-04-26.md) implicitly assumes the SCF saturation surface (where A_C self-consistency pins the boundary) and the λ = 1 holographic projection surface (where 𝒫_holo collapses Σ-fibers) are the *same* surface. This needs to be stated and proven as Lemma 1 of the synthesis document. ~½–1 page of Σ-side argument.

**Primary:** Warp/Oz — the SCF substitution derivation file is Warp's; the argument is a continuation of that work.

**Critic:** Claude/Opus — verifies the lemma statement. If the lemma reveals a structural gap (that the two surfaces do NOT coincide in general), Claude evaluates whether the synthesis theorem needs an additional hypothesis.

**Realistic timeline:** ½–1 day if clean; up to several weeks if it surfaces a structural rethink.

**HIGHEST PRIORITY among Tier 2 items** — outcome directly affects whether the synthesis theorem §3 is self-contained. Cheap to attempt; high information value either way.

**Unlocks:** Synthesis theorem self-containment; the "matching condition" in the theorem proof becomes an explicit lemma rather than a one-line claim.

---

## QFT Translation of the Banach Contraction

**What it is:** Lift the Banach contraction argument (W^{1,p}(M, T*M ⊗ 𝔲(d)) function space, ε < ε* regime) from the quantum-mechanics sector to renormalized semiclassical QFT. Loop corrections to κ = εC_E C_Q C_YM not computed.

**Primary:** Warp/Oz — the existing Banach argument is in Warp's derivation file.

**Critic:** Claude/Opus — but with explicit humility: infinite-d functional analysis with renormalization is a domain where Claude's critique value is partial.

**Literature support:** Perplexity — Hu–Verdaguer stochastic gravity literature (already scanned for M3); functional-analytic semiclassical gravity more broadly.

**⚠️ External-expert hand-off candidate.** This is the Tier 2 item most likely to benefit from a human QFT/renormalization specialist. The reasoning is genuinely outside the comfort zone of all three AI collaborators. If Bryan has a QFT collaborator in his network, this item should go there.

**Realistic timeline:** Multi-week, with significant uncertainty. Do not attempt without G1 closure.

**Unlocks:** Universality claims for the Born chain (currently blocked); not blocking Papers 2 or 3 publication.

---

## Sequencing Recommendation

In order of *what to attempt next*, ranked by information value per effort:

1. **Lemma 1** (Warp, this week) — cheapest attempt, highest information value, directly affects synthesis theorem.
2. **G2 diagnostic** (Claude, this week, in parallel with Lemma 1) — half-day work, can run alongside.
3. **G1** (Warp, after Lemma 1 outcome) — multi-week; Lemma 1 result may inform gauge-group choice for G1.
4. **QFT translation** (Warp + external expert if available, after G1) — last among Tier 2; benefits from G1 closure first.

**Practical rule (Perplexity, 2026-04-26):** Do not start G1 until both Lemma 1 *and* the G2 diagnosis are at least *stated* (even if not fully resolved). Otherwise the gauge-uniqueness statement G1 is aiming at may drift while G1 is underway.

**QFT escalation criterion:** If after 4 weeks of Warp/Oz attempt we do not see a stable contraction-mapping structure in the renormalized theory, reclassify QFT translation as a *human-collaborator problem* and mark it accordingly in the tracker.

---

## Synthesis Skeleton Update — COMPLETED

The synthesis skeleton (SYNTHESIS_EMANATION_INSTANTIATION_LOCUS_2026-04-26.md) §2.3 has been updated to:
- Label 𝓕 as "❌ MISSING (G4)" with cross-reference to PAPER7_SCOPE_CONSTRUCTIVE_F_2026-04-26.md
- Update the gate table: G4 now reads "36–60 months (Papers 4→5→6→7)" instead of "6–24 months"
- The synthesis treats 𝓕 as an ontological statement (H ⊋ M, fact horizon, CMB at t_rec), not a constructive theorem

This edit is complete as of 2026-04-26.

---

## Status Summary

| Gate | Primary | Status | Blocks |
|---|---|---|---|
| Lemma 1 | Warp | ❌ Not started | Synthesis self-containment |
| G2 α reconciliation | Claude | ❌ Not started | RC-2 research decision |
| G1 Conj. 6.3′ | Warp | ❌ Not started | Full Born chain closure |
| QFT translation | Warp + expert? | ❌ Not started | Universality claims |
| G3 Physical k_c | Paper 4 deliverable | ❌ Not started | CMB parameter-free prediction |
| G4 Constructive 𝓕 | Paper 7 program | Scoped | Papers 4→5→6→7 arc |
