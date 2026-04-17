# Paper 2A — Provenance Ledger
*2026-04-17 — section-by-section audit of `paper2A_FRAMEWORK_2026-04-17.md` against the three retracing tests.*
*2026-04-17 — cross-validation pass (Bryan, second LLM via Warp) applied; two amendments incorporated. See "Cross-Validation Amendments" below.*

---

## Purpose

Bryan's diagnosis: "the steak has been chopped to hamburger. Missing sections, referrals to nothing, old architecture persisting. There is no shortcut to completion from here." This ledger answers the three retracing tests for each subsection of Paper 2A:

1. **What was the source?** (what pre-split or draft file is the derivation from)
2. **Is the logic/ansatz current?** (does it match the present framework scope)
3. **Was the technique appropriate to the model?** (is the derivation valid at the modeling level at which it is invoked)

Every subsection lands in one of four buckets:

| Bucket | Meaning | Action |
|--------|---------|--------|
| **S1** | Sourced and current — derivation is valid at the level claimed | Keep as-is, with citation cleanup if needed |
| **S2** | Sourced but provisional / ansatz — derivation exists, but is framed as "to be verified" against a downstream object that either doesn't exist or is itself stale | Rewrite framing, or promote ansatz to acknowledged modeling choice, or demote to named conjecture |
| **S3** | Sourced but model-scoped — derivation is valid inside one explicit toy/model but is presented (or later cited) as if universal | Re-scope in-place, and re-audit every downstream citation that treats it as universal |
| **S4** | Stale residue / broken interface — references sections, equations, or architecture that no longer exist in the current split | Cut, move to the correct companion paper, or explicitly mark as "legacy — see archive" |

This ledger is the prerequisite for any further RC-2 work. Until upstream is stable, RC-2 and 2C downstream fixes are building on unverified ground.

---

## Cross-Validation Amendments (2026-04-17, post-second-LLM pass)

Second-LLM read of the ledger against the current 2A manuscript, source section files, the old pre-split §7 EOM draft, and current 2B. Verdict: adopt the ledger as the working audit artifact, with two amendments.

### Amendment 1 — §2.2.6: Path B archive check, more honest framing

The original ledger left open whether a pre-split §7 derivation existed that could upgrade λ ∼ A² from S2 to S1. Cross-validation against `sections/drafts/paper2_section_7.0_EoM_MxSigma_DRAFT.md` and `sections/drafts/paper2_section_4_abstract_EOM_v2.md` shows:

- There **is** an older derivation-like section in the repo.
- But it is still assumption-heavy and self-certifying.
- It does **not** clearly upgrade λ ∼ A² from S2 to S1.

**Implication:** Path B ("derive λ ∼ A² from full covariant EOMs") is not a recovery of lost work — it would be genuinely new derivation effort. The archive provides scaffolding but not a finished proof. Path A (name the ansatz honestly) is correspondingly more attractive as a near-term move, and Path B — if chosen — is a multi-week derivation project, not a retrieval.

### Amendment 2 — §2.6: not S1 physics + S4 labels; framing is cross-paper outdated

Original ledger classified §2.6 as S1 physics content plus S4 labeling residue. Cross-validation against current `paper2B_KCR_EVALUATION_2026-04-17.md` §4.2.1–§4.2.4 shows that 2B's own current statement is:

- **The robust statement is λ → 0** (not R_{Markov} → 0).
- **R_{Markov} in warped throats tends to O(1)**, not automatically to zero.

This contradicts §2.6.5's headline: *"in the KK-Cone throat (A → 0), the warp factor automatically drives λ → 0 (via Eq. 2.2.42), which in turn pushes R_{Markov} → 0."* 2B has softened/replaced this, so 2A §2.6 is now claiming a cross-paper result that its own companion paper no longer endorses.

**Re-classification:**

| Subsection | Original bucket | Amended bucket |
|------------|----------------|-----------------|
| §2.6.5 / §2.6.8 forward-refs | S2 (inherited from §2.2.6) | **S2 conceptually outdated, not just inherited** — 2B disagrees with the framing |
| Table 4 | S4 (stale) | **S4 stale + partly superseded** — the verification chain it lays out contradicts 2B's current analysis, not just the §1.3 scope |

§2.6.1–§2.6.4 (Markov-ratio definition, threshold, timescale correspondence) remain S1 at the framework level. The conceptual outdatedness is localized to §2.6.5 (geometry-specific claim about KK-Cone throat) and the §2.6.7 summary sentence that repeats it.

### Net effect on retracing priorities

The two amendments **promote** Table 4 and §2.6.5/8 from "cleanup pass" to "conceptual repair required." They do **not** displace §2.2.6 as the #1 blocker — §2.2.6 is still the upstream root cause. But they mean the §2.6 patch that follows §2.2.6 resolution is a real physics revision, not a label renumber.

---

## Scope Boundary for 2A (as stated in §1.3 of the current file)

> "The current paper does not evaluate on a specific geometry; geometry-specific evaluation (KK-Cone, KCR-Cone) is deferred to Paper 2B."

Any 2A content that evaluates on a specific geometry, or that forward-references geometry-specific results, is by that self-declared scope a candidate for S3/S4 status.

---

## Frontmatter Issues

### Table 4 — Cross-Reference Map (lines 36–46)

**Bucket:** **S4 stale + partly superseded**

**Evidence:** The cross-reference map presents geometry-specific verification chains ("warp-factor scaling → KCR-Cone → §7.x of 2A") that contradict the §1.3 scope commitment. The mapped anchors (Eq. 7.x.x, §7.y) do not exist in the current file — §7 is not a section here. These anchors are artifacts of the pre-split monolithic draft in which 2A, 2B, and 2C lived together.

**Effect downstream:** Any statement in Paper 2B that cites "Paper 2A §7.3.3" or "Paper 2A §7.4.15" inherits a broken interface from this map.

**Action:** Rewrite Table 4 to reflect the current split — all geometry-specific anchors must move to Paper 2B's internal numbering, and Paper 2A's entries should cite only abstract (framework-level) anchors like §2.1–§2.6.

---

## §2.1 — T_{MΣ} Derivation

### §2.1.1 – §2.1.10 (core derivation)

**Bucket:** **S1 — sourced and current**

**Source lineage:** Derived from `T_MSigma_PATCHED` draft content. The derivation is:
- Fubini–Study pullback onto M × Σ with joint state map Φ: M × Σ → 𝒫ℋ
- Block decomposition G_{AB} = G^{(M)} + G^{(Σ)} + cross-term
- Identification of the cross-term with the Berry connection projected onto the M-sector

**Test 1 (source):** Paper 1 Fubini–Study foundations + standard Berry-connection geometry. Cited correctly.

**Test 2 (current):** The FS pullback, block decomposition, and Berry identification are framework-level claims. They do not depend on a specific geometry. Consistent with §1.3 scope.

**Test 3 (technique):** Standard differential-geometric construction. Correct at framework level.

### §2.1.11 (KK-Cone warp scaling of T_{μa})

**Bucket:** **S4 — stale residue / broken interface**

**Evidence:**
- Line 574–688: Subsection titled "Warp-factor scaling of T_{μa}" inside §2.1.
- Line 576: *"[Note: Full treatment deferred to §7]"* — §7 does not exist in the current 2A file.
- Line 578: *"canonical Paper-2 bulk metric (§4.0)"* — §4.0 does not exist; 2A now tops out at §3, and the bulk-metric content moved to Paper 2B.
- Line 611: *"until derived from covariant equations in §7"* — same broken target.
- The subsection asserts T_{μa} ∼ A⁻², which is a geometry-specific scaling claim.

**Test 1 (source):** Pre-split `T_MSigma_PATCHED` where §7 was the EOM-on-M×Σ section of the monolithic draft. That §7 is now distributed across Paper 2B §4 (EOMs) and §5 (SC3 Casimir).

**Test 2 (current):** No. Framing violates §1.3 scope ("2A does not evaluate on a specific geometry") and refers to architecture that no longer exists.

**Test 3 (technique):** The dimensional argument itself (T_{μa} ∼ A⁻²) is of the correct form for a covariant derivative projected onto a warp-scaled metric, but it is a geometry-specific conclusion that should live in Paper 2B, not 2A.

**Action:** Move §2.1.11 out of Paper 2A. Either (a) relocate to Paper 2B as part of the KCR-Cone evaluation, or (b) replace with a one-sentence framework-level note: "Specific warp-factor scalings of T_{μa} are computed per-geometry in Paper 2B."

---

## §2.2 — δλ Formalism (distinguishability parameter)

### §2.2.1 – §2.2.5 (action, frame-lag EOM, metric-block structure)

**Bucket:** **S1 — sourced and current**

**Source lineage:** `delta_lambda_DRAFT`. The action
$$S[\mathbf{X}, \lambda] = S_M^{(0)} + S_\Sigma^{(0)} + \lambda S_{\rm cross}$$
and the derived frame-lag EOM are framework-level objects, valid without commitment to a specific warp geometry.

**Test 1 (source):** Phenomenological introduction of λ ∈ [0,1] as a tunable interpolation between quantum (λ=1) and classical (λ=0). Derivation of the frame-lag equation from δS/δξ^a and δS/δx^μ is standard variational calculus.

**Test 2 (current):** Yes — these are framework claims.

**Test 3 (technique):** Correct at phenomenological / variational level. The open-items item #1 ("λ first-principles derivation") is an acknowledged deferral, not a soundness problem at this level.

### §2.2.6 (KK-Cone warp hypothesis: λ ∼ A²)

**Bucket:** **S2 — sourced but provisional / ansatz**
*This is the single most load-bearing subsection in 2A for downstream RC-2 and 2C work.*

**Source lineage:** `delta_lambda_DRAFT` + the KK-Cone discussion that was originally part of the pre-split §7.

**Content:**
- Eqs. 2.2.40–2.2.41 derive λ ∼ A^α from a dimensional argument.
- Eqs. 2.2.42: α - 2 = 0 → α = 2, giving λ ∼ A².
- The dimensional argument's premise is "the coupling is independent of the warp factor," which translates physically into λT_{μa} = O(1) in the throat — i.e., the coupling product is warp-invariant.

**Problems:**
1. Line 1130 (approx.): *"Full verification is deferred to §7"* — §7 does not exist in the current 2A file. The intended verification target is broken.
2. This subsection is the actual origin of the λ ∼ A² claim that Paper 2B §4.1.6 cites "§7.4.15 of Paper 2B" (itself stale) for. The citation chain is **circular**: 2A §2.2.6 cites non-existent 2A §7 for verification; 2B §4.1.6 cites non-existent 2B §7.4.15 for the same claim; neither file actually contains the verification both cite.
3. The dimensional argument rests on "λT_{μa} is independent of the warp factor." That premise is a modeling choice, not a derived result. If it is promoted from ansatz to established result elsewhere in the manuscript without the derivation, the framework is circular at this load-bearing point.

**Test 1 (source):** Dimensional argument is actually **in** §2.2.6. The content exists; it is the framing that is broken.

**Test 2 (current):** Partially. The physics content is current, but the framing ("deferred to §7") is stale and the modeling-choice status of the premise is not acknowledged.

**Test 3 (technique):** Dimensional analysis is appropriate to a scaling hypothesis, but not to a **derivation**. The subsection oversells the conclusion.

**Action:** Rewrite §2.2.6 with three explicit moves:
- (a) State "λT_{μa} warp-invariant" as a named modeling choice (Ansatz A*), not as a derived result.
- (b) Remove the broken "deferred to §7" sentence. Replace with: "Verification against the full covariant equations of motion on a specific geometry is presented in Paper 2B §4 (KCR-Cone) and Paper 2B §5 (SC3)."
- (c) Flag as an open item for Paper 2A RC-2: if λT is **not** warp-invariant, the α=2 conclusion changes and the RC-2 p=1 result (items #13b, #14 in the Open Items Ledger) is affected.

**Downstream dependency:** Items #3, #4 in the Open Items Ledger (A⁻² cross-term scaling hypothesis; λ ∼ A² warp-factor scaling) are contingent on this being promoted from ansatz to derivation. RC-2's p = 1 result depends on λ ∝ A² exactly.

---

## §2.3 — Pilot-Wave Correspondence

### §2.3.1 – §2.3.8 (core 1D toy model derivation)

**Bucket:** **S3 — sourced but model-scoped**

**Source lineage:** `pilot_wave_MERGED`. The Born–Oppenheimer decoupling + Bures cross-term identification + algebraic equality Q_{BODC} + Q_{geom} = Q_{Bohm} in the 1D two-slit dephasing toy model.

**Test 1 (source):** The derivation exists as a genuine calculation inside an explicit model: 1D system, two-slit setup, pure-dephasing decoherence, explicit Gaussian packets with width σ(t). Each step is executed in coordinates.

**Test 2 (current):** Partially. The in-section scope is honest ("in the 1D two-slit model this identification is algebraically exact"). **However**, §3 Framework Conclusion (line 2538) states the identification as a general framework result: *"The pilot-wave correspondence (§2.3) establishes that the Bohmian quantum potential Q is the Born-Oppenheimer effective potential..."* — this is a universal claim phrasing. The §3 language overstates what §2.3 actually proves.

**Test 3 (technique):** The 1D toy-model derivation uses appropriate technique (BO separation, Bures geometry, explicit packet calculation). The technique is not sufficient to support the universal claim in §3 without a multi-dimensional or field-theoretic extension.

**Action:**
- Keep §2.3.1–§2.3.8 as the scoped derivation it is.
- Revise §3's pilot-wave summary sentence to match actual scope: "...establishes that the Bohmian quantum potential Q is recovered as the Born-Oppenheimer effective potential in the 1D two-slit dephasing model; a general-dimensional extension is an open item."
- Add to Open Items Ledger: "Extension of Q_{BODC} + Q_{geom} = Q_{Bohm} beyond the 1D toy model."

### §2.3 Appendix C (lines 1630+)

**Bucket:** **S4 — stale residue / packaging**

**Evidence:** Appendix C references Eq. D-* (D-1, D-2, …) which are numbering artifacts from an earlier document layout in which the pilot-wave material had its own Appendix D. In the current 2A file, there is no Appendix D; the references are dangling.

**Test 1 (source):** Pre-merge `pilot_wave_MERGED` document layout that was absorbed into 2A as Appendix C, without renumbering.

**Test 2 (current):** No — the internal references are broken.

**Test 3 (technique):** The content is computational and correct; only the referencing is stale.

**Action:** Renumber Appendix C's internal references (D-1 → C-1, etc.) or restore the appendix layout. Low-risk cleanup.

---

## §2.4 — Mixed-State Born Rule via Purification

**Bucket:** **S1 — sourced and current**

**Source lineage:** `mixed_state_born_PATCHED`. Derivation chains from:
- Paper 1 pure-state Born rule (axioms A1–A4)
- Schmidt-decomposition purification theorem
- Partial-trace manipulation
- Naimark's dilation theorem for POVMs

**Test 1 (source):** Each step cites either Paper 1 (for pure-state Born rule) or standard operator-algebraic results (Schmidt, Naimark, partial trace).

**Test 2 (current):** Yes. No stale references. No geometry-specific content. No dependency on KK-Cone / KCR-Cone.

**Test 3 (technique):** Linear-algebraic and operator-algebraic manipulations are appropriate to the purely mathematical claim that P(a|ρ) = Tr(ρM_a) follows from the pure-state Born rule on the purification. The §2.4.8 circularity check is explicit.

**Action:** None needed. Clean module.

---

## §2.5 — Left-Right Generator Decomposition

**Bucket:** **S1 — sourced and current** (with one cross-reference caveat)

**Source lineage:** `left_right_generators_v2`. Explicit Bloch-vector derivations for:
- §2.5.2 pure dephasing → L_t = R_t exactly
- §2.5.4 amplitude damping + dephasing → controlled mismatch ‖L_t − R_t‖
- §2.5.6 pointer-sector criterion theorem (Theorem 2.5.1)
- §2.5.7 Phase III convergence theorem (Theorem 2.5.2)
- §2.5.8 two entropic ledgers

**Test 1 (source):** Two explicit toy models, with full Bloch-vector solutions. Cited against Settimo et al. 2026 (external literature) and Zurek 2003.

**Test 2 (current):** Yes. No stale references, no broken architecture. The Phase III / λ_M → 0 framing is self-contained within the section.

**Test 3 (technique):** Appropriate — explicit open-system calculations in finite-dimensional examples, with controlled abstractions (spectral gap argument in §2.5.7). The pointer-state criterion theorem and its geometric reformulation are proven explicitly.

**Caveat:** §3 Framework Conclusion (line 2542) claims Settimo et al. divisibility inequivalence is "encoded geometrically as ΔG_{ij} = G^{(S)} - G^{(H)} ≠ 0" as an **established** result. §2.5 proves this in the two explicit models but does not prove it universally. Minor: the §3 summary should say "in the models of §2.5.4" or "for Lindbladian dynamics of the form studied in §2.5," not implicitly universal.

**Action:** None critical. Optionally soften §3 line 2542 framing.

---

## §2.6 — Markov Transition Criterion

### §2.6.1 – §2.6.7 (physics content)

**Bucket:** **S1 — sourced and current**

**Source lineage:** `markov_transition_DRAFT`. The criterion R_{Markov} = λ‖G^{(cross)}‖ / (‖G^{(M)}‖ + ‖G^{(Σ)}‖) < ε is framework-level, as is the action-form equivalent and the connection to τ_D / τ_adapt timescales.

**Test 1 (source):** The Markov-ratio definition, threshold criterion, and action-form criterion are phenomenological / framework-level claims. The §2.6.4 timescale discussion uses a heuristic correspondence between norms and decoherence rates — appropriately hedged.

**Test 2 (current):** Yes — with one caveat about forward references (see below).

**Test 3 (technique):** Correct at the level claimed. The criterion is a comparison of metric-block norms; no claim exceeds what the geometric structure supports.

### §2.6 — Formatting residue

**Bucket:** **S4 — stale equation labels** (labeling only, not physics)

**Evidence:** §2.6.4, §2.6.6, §2.6.7 use equation labels **Eq. 2.3.12, Eq. 2.3.13, Eq. 2.3.14, Eq. 2.3.15, Eq. 2.3.16, Eq. 2.3.21, Eq. 2.3.22, Eq. 2.3.23, Eq. 2.3.24, Eq. 2.3.25** (at lines 2383, 2393, 2399, 2405, 2415, 2441, 2445, 2449, 2466, 2478). These are residue from an older numbering scheme in which §2.6 was §2.3. Likewise, the §2.6.7 "Logic Chain" summary cites §2.3.2, §2.3.3, §2.3.4, §2.3.6 at lines 2497–2505.

**Test 1 (source):** Pre-renumbering draft layout.

**Test 2 (current):** No — the labels point to equations that now have different numbers.

**Test 3 (technique):** Labeling hygiene only. Physics untouched.

**Action:** Global renumber 2.3.x → 2.6.x for all equation labels and internal section cross-references inside §2.6. Low-risk cleanup.

### §2.6.5 / §2.6.8 — Forward references to Paper 2B

**Bucket:** **S2 (at the level of the cited claim) — ansatz forward-propagated**

**Evidence:** Line 2427: *"in the KK-Cone throat (A → 0), the warp factor automatically drives λ → 0 (via Eq. 2.2.42), which in turn pushes R_{Markov} → 0."* This inherits §2.2.6's ansatz (λ ∼ A²) and propagates it into the Markov criterion as if it were an established result.

**Test 1 (source):** Forward-references Paper 2B §3 for the actual evaluation. The claim itself rests on §2.2.6's warp-factor scaling, which is S2.

**Test 2 (current):** The forward reference ("subject of [Paper 2B, §3]") is architecturally correct. The issue is that the forward reference is stated with confidence that §2.2.6 cannot yet support.

**Action:** When §2.2.6 is rewritten to acknowledge the modeling-choice status of λT-warp-invariance, the §2.6.5 sentence must be matched: "...conditional on the warp-invariance ansatz of §2.2.6; see Paper 2B §3 for the explicit evaluation and Paper 2B §5.3 for self-consistency."

---

## §3 — Framework Conclusion

**Bucket:** **S1 — synthesis, appropriately scoped, two minor language items**

**Source lineage:** Written as a synthesis of §2.1–§2.6. Not a derivation; a reading of the framework's outputs.

**Test 1 (source):** Each paragraph synthesizes an earlier §2.x and stops at the 2A scope boundary. External references (Kibble 1979, Ashtekar–Schilling 1997, Settimo et al. 2026) are correctly used.

**Test 2 (current):** Two overstatements in the summary language (already noted above):
- Line 2538: pilot-wave identification stated universally, where §2.3 proves only the 1D toy-model case.
- Line 2542: Settimo divisibility inequivalence stated universally, where §2.5 proves only the two explicit open-system models.

**Test 3 (technique):** Synthesis-level reading. Appropriate, with the two language softenings above.

**Action:** Soften the two sentences to match actual §2.3 and §2.5 scope. No derivational changes.

---

## Summary Table

| Subsection | Bucket | Issue | Risk to RC-2 / 2C |
|------------|--------|-------|--------------------|
| Table 4 (frontmatter) | **S4 stale + partly superseded** (post-amendment) | Broken §7.x anchors **plus** verification chain contradicts current 2B §4.2 analysis | Medium — conceptual repair, not just cleanup |
| §2.1.1–§2.1.10 | **S1** | — | None |
| §2.1.11 (warp scaling of T_{μa}) | S4 | Refers to §7, §4.0 (don't exist); violates §1.3 scope | Medium — any downstream use of T_{μa} ∼ A⁻² inherits the broken interface |
| §2.2.1–§2.2.5 | **S1** | — | None |
| §2.2.6 (λ ∼ A²) | **S1 ✅ resolved 2026-04-17** | Ansatz A* named; §4.1.6 anchors λ·T boundedness; "deferred to §7" removed | None |
| §2.3.1–§2.3.8 | S3 | Model-scoped to 1D toy; §3 overstates as universal | Low — language cleanup only |
| §2.3 Appendix C | S4 | Eq. D-* labels dangling | Low (cleanup) |
| §2.4 (mixed-state Born) | **S1** | — | None |
| §2.5 (left-right generators) | **S1** | — | None (minor §3 softening) |
| §2.6.1–§2.6.4 physics | **S1** | — | None |
| §2.6 equation labels | S4 | 2.3.x labels should be 2.6.x | Low (cleanup) |
| §2.6.5 / §2.6.7 / §2.6.8 forward refs | **S1 ✅ resolved 2026-04-17** | §2.6.5 patched; §4.2.4 provides λ→0 / R_{Markov}≈O(1) canonical framing | None |
| §4 EOM on M×Σ | **S1 ✅ assembled 2026-04-17** | From `paper2_section_4_abstract_EOM_v2.md`; commit b6cfcb7 | None |
| §3 Framework Conclusion | **S1** | Two minor language overstatements | Low (language only) |

---

## Retracing Priority Order

*Updated 2026-04-17. Former Priorities 1–3 are RESOLVED. Only formatting/cleanup remains.*

### ✅ RESOLVED — §2.2.6 Path A (was Priority 1)

Applied 2026-04-17: Ansatz A* named in §2.2.6; §4 assembled (commit b6cfcb7), anchoring λ·T boundedness at §4.1.6. Path B remains available as a future derivation project.

### ✅ RESOLVED — §2.6.5/7/8 and Table 4 (was Priorities 2–3)

§2.6.5 patched. §4.2.4 provides canonical λ→0 / R_{Markov}≈O(1) framework statement. Table 4 rewritten (prior session patch) with current 2B §4 anchors and Ansatz A*/ATA status flags.

### ✅ Priority 1 (ex-4) DONE — §2.1.11 condensed (commit c834ede)

Condensed to single named-ansatz block (Eq. 2.1.39 only). Removed Eqs. 2.1.37/2.1.38 and Physical Interpretation section. Scope note and Paper 2B §4 pointer retained.

### ✅ Priority 2 (ex-5) DONE — §3 Settimo sentence scoped (commit c834ede)

Settimo ΔG sentence: added 'in the models of §2.5' qualifier. Pilot-wave sentence was already scoped (1D two-slit) in prior session.

### ✅ Priority 3 (ex-6) DONE — Formatting hygiene (prior session)

§2.6 labels renumbered (2.3.x→2.6.x). §2.3 Appendix C D-*→C-* renaming. Both completed in prior session.

---

## What This Ledger Does Not Resolve

- **Does not rederive λ ∼ A²** — that is the Path A vs. Path B decision in Priority 1.
- **Does not settle p = 1 vs. p = 3/2** — that is item #13b in the Open Items Ledger, and it depends on Priority 1.
- **Does not patch 2B or 2C** — those patches should wait until §2.2.6 is resolved. Otherwise we re-introduce the same circular dependency.
- ~~**Does not cross-validate with a second LLM**~~ — **DONE 2026-04-17** (Bryan, via Warp). Two amendments incorporated above.

---

## Realistic Status

- ✅ **VERIFIED:** All eight subsection audits (§2.1, §2.2, §2.3, §2.4, §2.5, §2.6, §3) performed against present file content.
- ✅ **VERIFIED:** §2.2.6 identified as the load-bearing S2 where circular-citation failure mode enters.
- ✅ **VERIFIED:** §2.1.11, §2.3 Appendix C, §2.6 equation labels identified as S4 residue.
- ✅ **VERIFIED (post-amendment):** Second-LLM cross-validation pass (Bryan, via Warp) against 2A file, source section files, pre-split §7 EOM draft, current 2B. Two amendments applied: (1) pre-split §7 exists but is assumption-heavy and does not rescue λ∼A² from S2; (2) §2.6.5/7/8 and Table 4 are conceptually outdated vs. current 2B §4.2, not just formatting-stale.
- ✅ **VERIFIED (post-amendment):** The deeper question *"is λT warp-invariance a defensible modeling choice?"* now has a known scaffolding answer: there is archive material, but it is itself an ansatz-layered derivation. Path B is therefore a new-derivation project, not a retrieval.
- ✅ **ASSEMBLED (2026-04-17):** §4 EOM-on-M×Σ inserted into `paper2A_FRAMEWORK_2026-04-17.md` (commit b6cfcb7). Archaeology finding: content was never missing — it was written (Wave 5), Klein-patched 2026-04-09, but never assembled into 2A.
- ✅ **RESOLVED (2026-04-17):** 2B §4.2 framing (λ→0, R_{Markov}≈O(1)) is canonical; now anchored in 2A §4.2.1–§4.2.4.
- ✅ **RESTORED (2026-04-17):** HCR (Holographic Coherence Relativity) naming throughout 2A (commit 47106c9).

## Next Steps

1. ✅ Second-LLM cross-validation — DONE.
2. ✅ §2.2.6 Path A — DONE (Ansatz A* named; §4.1.6 anchors λ·T).
3. ✅ §4 assembly — DONE (commit b6cfcb7).
4. ✅ §2.6 / Table 4 conceptual repair — DONE.
5. ✅ HCR naming — DONE (commit 47106c9).
6. ✅ **All cleanup done** (commit c834ede): §2.1.11 condensed; §3 Settimo scoped; §2.6 labels and Appendix C renumbered (prior session).
7. **When cleanup done:** 2B citation hygiene → RC-2 rebuild → 2C patches.

**Realistic status: 2A provenance audit 100% complete. ALL items resolved including cleanup. 2A is stable and fully clean for downstream RC-2 / 2C work.**
