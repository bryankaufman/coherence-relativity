# Paper 2 — Assembly Manifest
**Date**: 2026-03-23
**Purpose**: Map every existing draft file to its final section in the assembled manuscript.
**Target structure**: paper2_split_outline_2A_2B.md (v2)
**Assembly task**: Build paper2_ASSEMBLED_2026-03-23.md from the files below.

---

## Assembly Map

| Final Section | Source File | Status | Action |
|---|---|---|---|
| §1 Introduction | sections/drafts/paper2_section_1_introduction_MERGED.md | ✅ Draft complete | Copy as-is |
| §2.1 T_MΣ derivation | sections/patched/paper2_section_2.1_T_MSigma_PATCHED.md | ✅ Patched final | Use patched version |
| §2.2 δλ formalism | sections/drafts/paper2_section_2.2_delta_lambda_DRAFT.md | ✅ Complete | Copy as-is |
| §2.3 Markov transition | sections/drafts/paper2_section_2.3_markov_transition_DRAFT.md | ✅ Complete | Rename: now §2.6 per split outline |
| §2.3 Pilot wave | sections/drafts/paper2_section_2.3_pilot_wave_DRAFT.md + paper2_section_2.3_pilot_wave_COMPLETION.md | ✅ + Completion written 2026-03-23 | Merge DRAFT + COMPLETION |
| §2.4 Mixed-state Born | sections/patched/paper2_section_2.4_mixed_state_born_PATCHED.md | ✅ Patched final | Use patched version |
| §2.5 Left-right generators | sections/drafts/paper2_section_2.5_left_right_generators_DRAFT.md | ✅ NEW 2026-03-23 | Copy as-is |
| §3.1 Historical narrative | sections/patched/paper2_section_3.1_historical_PATCHED.md | ✅ Patched final | Use patched version |
| §3.2 Topology as output | sections/patched/paper2_section_3.2_topology_as_output_PATCHED.md | ✅ Patched final | Use patched version |
| §3.3 Constraints | sections/drafts/paper2_section_3.3_constraints_DRAFT.md | ✅ Complete | Copy as-is |
| §4 KK-Cone model | sections/patched/paper2_section_4.0_KK_Cone_model_PATCHED.md | ✅ Patched final | Use patched version |
| §4.4 C¹ regularity | sections/patched/paper2_section_4.4_C1_regularity_PATCHED.md | ✅ Patched final | Use patched version |
| §4.5 C¹ regularity SM comparison | sections/drafts/paper2_section_4.5_C1_regularity_SM_comparison_DRAFT.md | ⚠️ Draft | Review before include |
| §5 Holographic conjecture abstract | sections/drafts/paper2_section_5_holographic_conjecture_DRAFT.md | ✅ Complete (~2800 words) | Copy as-is |
| §5.1–5.2 SC1/SC2 | sections/drafts/paper2_section_5.1_5.2_SC1_SC2_DRAFT.md | ⚠️ Draft | Review, renumber to §5.1–5.2 in Part III |
| §5.3 SC3 Casimir | sections/drafts/paper2_section_5.3_SC3_Casimir_DRAFT.md | ⚠️ Draft | Review |
| §6 Geometric dark matter | sections/patched/paper2_section_6_geometric_dark_matter_PATCHED.md | ✅ Patched final | Use patched version |
| §7 EOM on M×Σ | sections/drafts/paper2_section_7.0_EoM_MxSigma_DRAFT.md | ✅ Verified | Copy as-is |
| §8 Holographic conjecture full | sections/drafts/paper2_section_8.0_holographic_conjecture_DRAFT.md | ✅ Verified + numerics done | Copy as-is |
| §9 Discussion | sections/drafts/paper2_section_6_discussion_MERGED.md | ✅ Draft complete | Copy as-is |
| §10 Open problems | sections/drafts/paper2_section_7_open_problems_MERGED.md | ✅ Draft complete | Copy as-is |
| Appendix A Block inverse | sections/patched/paper2_appendix_A_block_inverse_PATCHED.md | ✅ Patched | Copy as-is |
| Appendix B Geff KK tower | sections/patched/paper2_appendix_B_Geff_KK_tower_PATCHED.md | ✅ Patched | Copy as-is |
| Appendix C Pilot wave derivation | sections/drafts/paper2_pilot_wave_derivation_WORKING.md | ✅ Working doc | Trim to appendix format |

---

## Spine Edits Still Needed

The mathematical spine (paper2_mathematical_spine_2026-02-28.md) contains §§2–4 in their
original form. The patched sections above **have not been reflected back into the spine**.

Options:
A. Build the assembled manuscript from the individual section files (recommended — cleaner)
B. Update the spine in-place to match patched sections (risky — very long file)

**Recommendation**: Option A. Build paper2_ASSEMBLED_2026-03-23.md as a new file that
concatenates the sections in order. Keep the spine as a reference document.

---

## Renumbering Required (per split outline v2)

The split outline restructured sections from the spine. The final numbering is:

```
Part I: Formalism
  §1  Introduction
  §2.1 T_MΣ derivation
  §2.2 δλ formalism
  §2.3 Pilot wave connection  ← was unnamed; now explicit section
  §2.4 Mixed-state Born rule
  §2.5 Left-right generator decomposition  ← NEW 2026-03-23
  §2.6 Markov transition criterion  ← was §2.3 in spine

Part II: Derived Compactification
  §3.1 Historical narrative
  §3.2 Topology as output
  §3.3 What derived compactification constrains

Part III: Dynamics, Regularity, Holography
  §4   KK-Cone model (with §4.4 C¹ regularity)
  §5   Holographic conjecture (abstract layer)
  §5.1 SC1 flatness
  §5.2 SC2 gravity localization + H1 PASS (Spike 11 done)
  §5.3 SC3 Casimir + cosmological constant
  §6   Geometric dark matter response

Part IV: EOM and Holographic Verification
  §7   EOM on M×Σ
  §8   Holographic conjecture (KK-Cone specific, with numerics)

Part V: Closing
  §9   Discussion
  §10  Open problems

Appendices
  A    Block inverse
  B    G_eff KK tower
  C    Pilot wave derivation (from WORKING doc)
```

---

## Missing Pieces (genuinely new writing needed)

1. **§2.3 merge**: Pilot wave DRAFT + COMPLETION need to be stitched together as one coherent section.
2. **§4.5 SM comparison review**: Needs a read-through before inclusion.
3. **Open problems update**: Should include new ideas from idea_assignments_2026-03-23.md
   (ℓ* = S_max/2, Decoherence Recapitulates Cosmogenesis, Settimo citation block).
4. **Bibliography consolidation**: All draft-level bib entries need to be merged into master.bib.

---

## Estimated Word Count (assembled)

| Section | Estimated Words |
|---|---|
| §1 Introduction | ~1,200 |
| §2.1–2.6 Formalism | ~8,500 |
| §3.1–3.3 Compactification | ~4,500 |
| §4 KK-Cone + §5 Holographic abstract | ~7,000 |
| §5.1–5.3 SC1–SC3 | ~6,000 |
| §6 Geometric dark matter | ~3,000 |
| §7–§8 EOM + Holographic KK | ~10,000 |
| §9–§10 Discussion + Open problems | ~4,000 |
| Appendices | ~5,000 |
| **Total** | **~49,200** |

Target for submission: 15,000–20,000 words (journal version).
This means the assembled draft will need significant tightening for submission.
The full draft is appropriate for a working manuscript / arXiv long version.

---

## Next Actions

1. [ ] Run assembly: concatenate sections in order → paper2_ASSEMBLED_2026-03-23.md
2. [ ] Merge §2.3 pilot wave DRAFT + COMPLETION
3. [ ] Update §10 open problems with new ideas
4. [ ] Consolidate bibliography entries into master.bib
5. [ ] Commit assembled draft to git (via Warp)

**Realistic status after assembly**: ~75% of a submittable draft.
**Remaining gaps for submission**: tightening to journal length, full proof of Theorem 2.5.1,
numerical verification of exact pilot wave coefficients.
