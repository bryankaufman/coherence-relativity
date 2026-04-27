# Paper 2 Status Marker Triage — 2026-04-17

All status markers across 2A, 2B, 2C audited. Each is categorized as **KEEP** (physics content that tells the reader what's proven vs. assumed), **REMOVE** (process tracking from the writing workflow), or **REWRITE** (useful content buried in process framing).

---

## KEEP — Physics Content (tells reader what's derived, assumed, or open)

### Paper 2A
| Line | Marker | Why keep |
|------|--------|----------|
| 606 | `**Status**: This is an ansatz that requires verification` (A⁻² scaling) | Honest about hypothesis vs. derivation |
| 742 | `**Status**: derivation of λ from first principles...deferred` | Documents phenomenological status of λ |
| 1343 | `**Status**: Deferred to future work` (first-principles λ) | Same |
| 1353 | `**Status**: Deferred to §7` (warp-factor scaling verification) | Points reader to verification location (now in 2B) |
| 1363 | `**Status**: Specific examples deferred to §3` | Points reader forward (now in 2B) |
| 1376 | `**Status**: Beyond the scope of Paper 2` (quantization) | Honest scope boundary |
| 2151–2159 | §2.5.9 "Summary and Status" verification table | Documents proof status of each result in §2.5 |

### Paper 2B
| Line | Marker | Why keep |
|------|--------|----------|
| 540 | `Status: RESOLVED by cosmological attractor` (scale factor s) | Physics resolution |
| 542 | `Status: CONTINGENT on Paper 3` (field content) | Honest dependency |
| 544 | `Status: OPEN` (c₁ = 1 uniqueness) | Open question |
| 632 | `Status: INTERFACE-CONTRACT ONLY` (P3-H3) | Documents Paper 3 interface |
| 634 | `Status: INTERFACE-CONTRACT ONLY` (P3-H4) | Documents Paper 3 interface |
| 991–995 | ⚠️ caveats on C¹ regularity + delivered promise | Physics clarification + Paper 1 fulfillment |
| 1078–1084 | Five-level Σ→M coupling hierarchy table | Core physics content |
| 1183 | `Status: Shape RESOLVED; scale PARTIALLY RESOLVED` | Honest about what's done |

### Paper 2C
| Line | Marker | Why keep |
|------|--------|----------|
| 49+ | All `✅ DERIVED` / `⚠️ CONJECTURED` / `⚠️ ASSUMPTION` markers | Critical — tells reader exactly what's proven vs. assumed |
| 157, 159 | ⚠️ ASSUMPTION (A1), (A2) | Essential transparency |
| 283 | ⚠️ ASSUMPTION (A3) — δT_M/δg requires RC-2 | Essential |
| 301 | ⚠️ ASSUMPTION (A4) — conservation requires M-Σ EOM | Essential |
| 377 | ⚠️ CONJECTURED (C1) — α = 3/2 from CP¹ spectral density | Essential |
| 454–456 | ⚠️ CONJECTURED (C2) + ✅ CONFIRMED ratio consistency | Essential |
| 503 | ⚠️ ASSUMPTION (A5) — T_M propagator form | Essential |
| 564 | ⚠️ NOTE on d vs k_c discrepancy | Important open question |
| 593–604 | "Summary of RC-1 Status" table | Excellent physics summary |
| 641 | ⚠️ Sonnet 4.6 draft — recommend Opus verification | Quality flag |
| 810–811 | ✅ Framework level markers in holographic table | Physics content |
| 853 | `Delivered promise: Holographic connections ✅` | Paper 1 fulfillment |
| 958, 994, 1077 | ⚠️ Verification notes (FR, Proietti, Eq. 8.4.5) | Flags what needs checking |

---

## REMOVE — Process Tracking (writing workflow, not physics)

### Paper 2A
| Line | Marker | Why remove |
|------|--------|------------|
| 1381 | `**Date:** 2026-03-23 (merged from DRAFT...)` | Version history |
| 1683 | Date portion of `VERIFIED (algebraic; 2026-03-13)` | Keep "Verified algebraically", drop date |

### Paper 2B
| Line | Marker | Why remove |
|------|--------|------------|
| 23–36 | `§2 Extraction Status` (entire section) | Extraction provenance |
| 312 | `**Status:** v2 DRAFT — 2026-04-10` | Version tracking |
| 313 | `**Supersedes:** paper2_section_3.3_constraints_DRAFT.md` | File provenance |
| 651 | `**Status:** DRAFT v2 — Klein removal patch applied` | Version tracking |
| 653 | `**Source:** §7.0 DRAFT (abstract layer: ...)` | Source file reference |
| 873 | `**Status:** DRAFT — Wave 5 new section` | Version tracking |
| 1013–1024 | First `## Revision History` block | Version history table |
| 1021 | `**Status transparency:**` line | Meta-commentary |
| 1031 | `**Status:** REVISED — 2026-04-10 (D2)` | Version tracking |
| 1032 | `**Supersedes:** paper2_section_5.3_SC3_Casimir_v2.md` | File provenance |
| 1228–1238 | Second `## Revision History` block | Version history table |
| 1240–1242 | `§6 Extraction Note` section | Extraction provenance |

### Paper 2C
| Line | Marker | Why remove |
|------|--------|------------|
| 5 | `*Status: canonical 2C target; final renumbering...*` | Process provenance |
| 16–29 | `§1.1 Extraction Status` section | Extraction provenance |
| 658 | `*Produced 2026-04-15. Target path: ...*` | Process provenance |
| 663 | `**Status:** DRAFT — Wave 5 extraction` | Version tracking |
| 665 | `**Source:** §8.0 DRAFT (abstract layer: ...)` | Source file reference |
| 880 | `**Status transparency:**` | Meta-commentary |
| 885 | `**Status:** NEW WORK — 2026-04-12` | Version tracking |

---

## REWRITE — Physics Content in Process Framing

### Paper 2A
| Line | Current | Proposed |
|------|---------|----------|
| 1353 | `Deferred to §7` | `Deferred to Paper 2B` (§7 moved to 2B) |
| 1363 | `Specific examples deferred to §3` | `Specific examples deferred to Paper 2B §3` |
| §2.5.9 title | "Summary and Status" | "Summary" (drop "and Status") |
| §2.5.9 table | v1/v2 columns | Single "Status" column with final state only |

### Paper 2B
| Line | Current | Proposed |
|------|---------|----------|
| §5 title (L1024) | "Self-Consistency Status Note" | "Self-Consistency: SC3 Evaluation" |
| L1058 | `⚠️ **Category error in v2:**` | Rewrite as physics remark: "**Remark (D2 guardrail):** The FS curvature k²=2 is a property of Σ, not M. Inserting ρ_geom directly into Friedmann is a category error — see five-level hierarchy below." |

### Paper 2C
| Line | Current | Proposed |
|------|---------|----------|
| L32 | `**Status:** First draft — Sonnet 4.6 (dispatched for Opus...)` | `⚠️ **Verification note:** This derivation was produced by Sonnet 4.6. Independent verification on Opus recommended for §RC1.1 symmetry argument and §RC1.3B anisotropic tensor structure.` |

---

## CARRY FORWARD — Open Items for New Status Ledger

These items are currently UNTESTED, MISSING, OPEN, or CONJECTURED and should be collected into a single tracking document:

### From 2A
1. **λ first-principles derivation** — DEFERRED to future work
2. **A⁻² cross-term scaling hypothesis** — UNTESTED (verification deferred to 2B)
3. **λ ~ A² warp-factor scaling** — UNTESTED (verification deferred to 2B)

### From 2B
4. **Scale factor s dynamical mechanism** — PARTIALLY RESOLVED (Casimir gives value, mechanism not yet demonstrated)
5. **Field content on interval** — CONTINGENT on Paper 3 (Axiom B, phase transition)
6. **c₁ = 1 uniqueness** — OPEN
7. **SC1/SC2 rewrite to KCR interval formulation** — BLOCKING for 2B completion
8. **P3-H3 and P3-H4 interface contracts** — Paper 3 must deliver

### From 2C
9. **α = 3/2 exponent from CP¹ spectral density** — CONJECTURED (C1)
10. **λ normalization for Ω_DM/Ω_b** — CONJECTURED (C2)
11. **T_M propagator form P(k)** — ASSUMED (A5)
12. **k_c identification for CMB (d vs k_c discrepancy)** — OPEN (RC-3 scope)
13. **Opus verification of RC1.1 + RC1.2** — PENDING
14. **FR holonomy exact calculation (Ω = π)** — FLAGGED for Opus verification
15. **Proietti protocol → CR geometric language** — FLAGGED for derivation
16. **Eq. 8.4.5 derivation from ΔG_ij** — FLAGGED for verification
17. **δT_M/δg^μν extraction (RC-2)** — OPEN (requires full M-Σ EOM)
18. **Covariant conservation ∇^μ T^(eff)_μν = 0 verification** — OPEN (requires RC-2)
