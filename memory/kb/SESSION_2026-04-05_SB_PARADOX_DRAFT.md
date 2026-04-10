Session: 2026-04-05 — §5.6 Sleeping Beauty / Self-Locating Uncertainty Draft

Status: DRAFT COMPLETE — AWAITING CLAUDE REVIEW

## What Was Done
Warp agent drafted §5.6 for papers/01-coherence-frames/sections/PARADOXES.md.
This adds Sleeping Beauty and self-locating uncertainty as the sixth paradox resolution in the CR framework.

## Source Material
- YouTube video: "The Sleeping Beauty Paradox Was Never Solved — The Answer Destroys What We Mean By Probability" (Faultlines Studio, 78:55)
  URL: https://www.youtube.com/watch?v=exNTyeSvQjA
  Retrieved from Notion Video Knowledge Base (database 9d7c7178-368b-40f8-a4d4-ad4923fceade)
- Transcript excerpt stored in Notion page 338712332b1f81d0bfcbec5a728d83f5

## Key References (all verified via web search)
1. A. Elga, "Self-locating belief and the Sleeping Beauty problem," Analysis 60, 143 (2000) — original thirder argument
2. D. Lewis, "Sleeping Beauty: reply to Elga," Analysis 61, 171 (2001) — halfer reply
3. C. T. Sebens and S. M. Carroll, "Self-locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics," Brit. J. Phil. Sci. 69, 25 (2018) — structural identity proof
4. P. J. Lewis, "Quantum Sleeping Beauty," Analysis 67, 59 (2007) — SB ↔ MWI connection
5. D. Bradley, "Four Problems about Self-Locating Belief," Philosophical Review 121, 149 (2012) — unified treatment (SB + Everett + Doomsday + Fine-Tuning)
6. P. Winkler, "The Sleeping Beauty Controversy," Amer. Math. Monthly 124, 579 (2017) — comprehensive survey, 100+ papers
7. N. Bostrom, "Sleeping Beauty and Self-Location: A Hybrid Model," Synthese 157, 59 (2007)
8. S. Friederich, "Self-location and causal context," preprint — causal principle applied to SB + Everett

## CR Resolution Summary
The halfer/thirder debate is a coherence-frame mismatch:
- F_pre (pre-sleep): credence 1/2, correct — self-location absent from description
- F_wake (upon waking): credence 1/3, correct — Born measure applied over centered alternatives {H1, T1, T2}
- The transition F_pre → F_wake is a genuine frame transformation (D3)
- Memory-erasure protocol introduces self-locating degrees of freedom into Sigma
- No paradox: frame-dependent descriptions of single reality R

Sebens-Carroll's ESP = special case of Born measure invariance (A1) under environmental-only frame transformations.

## Items Flagged for Claude Review
1. **Notation consistency**: Does the draft correctly use D3, A1, A2, A3, T2 as defined in EQUATIONS_REFERENCE.md?
2. **A2 at the boundary**: The draft notes that relational invariance (A2) "applies across frames for the same decomposition, not across frames with different indexical structure." Is this a valid restriction, or does it weaken A2 beyond what Paper 1 establishes?
3. **ESP ↔ A1 claim**: The draft asserts Sebens-Carroll's ESP is a special case of A1. Is this defensible, or is it an overclaim? ESP says "changes to the environment alone don't affect local probabilities." A1 says mu is invariant under frame transformations. These are related but potentially not identical.
4. **Conjectures vs. proven**: The equal-coefficient assignment to {H1, T1, T2} via T2 (Equal Coefficient Lemma) assumes the centered alternatives form a permutation-symmetric set. Is this justified, or should it be flagged as "Conjecture (unverified)"?
5. **The measure-normalization issue**: The draft explicitly flags that mu_{F_pre}(T) = 1/2 does NOT equal mu_{F_wake}(T1) + mu_{F_wake}(T2) = 2/3 in the naive calculation. It argues this is the frame-mismatch itself. Is this argument sound, or does it break A2?

## Files Modified
- papers/01-coherence-frames/sections/PARADOXES.md (§5.6 added, status updated 80% → 90%)
- COORDINATION.md (handoff logged)
- memory/kb/SESSION_2026-04-05_SB_PARADOX_DRAFT.md (this file)

## Files NOT Modified (per SYSTEM-RULES.md — Paper 1 is content-complete)
- papers/01-coherence-frames/main.tex — NOT touched
- bibliography/master.bib — NOT touched (new citations listed but not yet added)

Logged: 2026-04-05 00:10 UTC
Agent: Warp
