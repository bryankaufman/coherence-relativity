# HCR — Project-Level Open Items Rollup
*2026-04-30 — first consolidation across all papers; updated 2026-05-01 (RC-4 ✅, C4 ✅); updated 2026-05-02 (Paper 2A recasted active draft; Paper 1 promise map added)*

This is the project-level aggregator. It does **not** restate per-paper items — it gives the cross-paper picture: where the critical-path items are, which interface contracts cross which papers, and what the realistic status of each manuscript is.

For full per-item detail, see the per-paper ledgers:

| Paper | Ledger file | Last updated |
|---|---|---|
| Paper 1 | (content-complete; no active ledger needed) | 2026-02 (publication) |
| Paper 2 (omnibus 2A/2B/2C) | `papers/02-saturation-dynamics/PAPER2_OPEN_ITEMS_LEDGER_2026-04-17.md` | 2026-04-20 |
| Paper 2C (2C-specific) | `papers/02C-holographic-structure/PAPER2C_OPEN_ITEMS_LEDGER_2026-04-30.md` | 2026-04-30 |
| Paper 3 | `papers/03-gr-unification/PAPER3_OPEN_ITEMS_LEDGER_2026-04-30.md` | 2026-04-30 |
| Paper 4 | `papers/04-holography/PAPER4_OPEN_ITEMS_LEDGER_2026-04-30.md` | 2026-04-30 |
| Papers 5–6 (stub) | `papers/05-06-transformer-program/PAPER5-6_TRANSFORMER_OPEN_ITEMS_2026-04-30.md` | 2026-04-30 |
| Papers 7–8 (consciousness program) | `papers/07-consciousness-program/HARD-PROBLEM-NOTES.md` + `PROJECT-TRAJECTORY.md` | 2026-04-30 |

---

## Realistic completion estimates (project-wide)

| Paper | Completion | Status | Primary blocker |
|---|---|---|---|
| Paper 1 | 100% | Published 2026-02-14 (OSF MetaArXiv) | — |
| Paper 2A | ~98% | **Active draft** | §7.9 ✅ §2.5 ✅ §4.4.8 ✅ §4.6 ✅ all DRAFTED; §7.9 REWRITTEN 2026-05-02 (3 issues fixed: λ disambiguation, D=Γ₀ constant, finite V_stoch) |
| Paper 2B | ~85% | Active draft | #6 (s dynamical mechanism); spectra exact |
| Paper 2C | ~82% | Publishable | RC-4 ✅ CLOSED (2026-05-01); C4 ✅ CLOSED — Busch 2003 axiom adopted |
| Paper 3 | ~62% | Active development | ζ-regularization, RC-1 Opus pass, s(R) first-principles (RC-4 ✅ CLOSED) |
| Paper 4 | ~50% | Conceptual scaffold | H1-A → H1-C closure gate, RC-1 Opus pass |
| Papers 5–6 | ~10–20% | Scoping only | No manuscript scaffold yet |
| Papers 7–8 | ~55% (notes) | Pre-paper consolidation | Comparison-substrate dissolution drafted; needs M1–M8 from HARD-PROBLEM-NOTES |

---

## Project-wide critical path

The single highest-leverage item across all papers, in priority order:

1. ~~**RC-4 sourced cosmological EOM (k_c^eff and c_Γ).**~~ ✅ **CLOSED 2026-05-01.** c_Γ = √(Ω_Λ/α_geom) = 0.679 ± 0.005 derived; k_c^eff = √(Ω_Λ)H₀ = 0.832 H₀ (leading order). Residual gap → Paper 4 §3 (R_Σ = χ_CMB holographic projection). See `RC4_SOURCED_EOM_2026-05-01.md`.

2. **RC-1 Opus 4.6 verification pass.** Promotes the holographic stress tensor T^(eff)_μν = λ (√−γ/√−g) Π_μν \|T_M\|² δ_⊥(x, ∂M) and α = 3/2 from CONJECTURED to DERIVED. Gates Paper 3 §3 and Paper 4 §3–4. Highest-leverage single verification on the docket.

3. **ζ-regularization of T2.5-B Casimir bounce spectral sums.** Paper 3 tier-1 blocker. Without it, the GW parameter window is structurally undefined. T_osc = 1884.7 b* is currently a lower bound only.

4. ~~**C4 axiom resolution for d=2 Born rule.**~~ ✅ **CLOSED 2026-05-01.** Route A (isotropic FP) definitively closed. Busch 2003 (PRL 91, 120403) adopted as stated axiom for d=2; Corollary 6.2 updated to cite it. Route B (non-isotropic noise ∝ T_MΣ) deferred to Paper 5. See `C4_AXIOM_DECISION_2026-05-01.md`.

5. **Paper 4 H1-A → H1-B → H1-C closure gate.** Entropy identity S_ent(Σ) = ∫_{γ_RT} Ω_MΣ. Primary closure test for Paper 4's holographic machinery. Estimated 2–3 weeks once RC-1 closes.

6. **s(R) first-principles derivation.** Paper 3 central deliverable. Without it, the scale-covariant story is conjectural. No clean sub-task identified yet.

---

## Cross-paper interface contracts

### Paper 3 owes (upstream blocker for Papers 2/2C/4)

| Contract | Owed to | Status |
|---|---|---|
| P3-H1: Radion closure (H1_PAYLOAD_RECORD) | Paper 2 §5.2(6) | K³-VERIFIED record provided; Paper 2 thresholds outstanding |
| P3-H2 (name pending) | Paper 2C §RC-1 (?) | OPEN; cross-reference not located |
| P3-H3: c₁ = 1 bundle-selection rule | Paper 2 §4 (L613); Paper 2C #13 | OPEN |
| P3-H4: Π: M × Σ → T^(eff)_μν projection rule | Paper 2 §4 (L615); Paper 2C #12 | OPEN |
| P3 → P2B: Field content on interval (phase transition / Axiom B) | Paper 2B §3 (L523) | OPEN |
| P3 → P4: Σ-level coherence-frame geometry (norm-preserving J, post-transition admissibility, T_MΣ(ℓ*)) | Paper 4 §9.4 H1 prerequisite | OPEN |
| P3 → P4: ∂M(t) dynamics for time-coordinate foliation; Bekenstein bound | Paper 4 (CMB ↔ ∂M) | OPEN |

### Paper 2 / 2C delivers upstream-to-Paper-3 (consistency required)

| Result | Source | Paper 3 use |
|---|---|---|
| KK graviton spectrum m_n² = 4n(2n + 3) | Paper 2B §6 | Consistency check |
| KK vector spectrum m_n² = 8n(n + 2) | Paper 2B §6 | Consistency check |
| α_geom = 10√2/(3π) ≈ 1.5005 | Paper 2 omnibus #23 | Used in c_Γ derivation (item #7 in Paper 3 ledger) |
| Γ_dec(z) = Γ₀ × H(z)/H₀, Γ₀ ≈ 0.49 H₀ | Paper 2 omnibus #29 | Direct input to Paper 3 §3 |
| CMB ↔ ∂M (three-anchor identification) | Paper 2 + new §3 | Anchors fact-horizon construction |
| r-coordinate r_max = π/(2√2) | Paper 2B/2C | Cross-references Paper 3 emergence |

### Paper 5 (when started) owes / inherits

- **Owes Paper 7/8:** transformer formalism for "filter-as-prior" (HARD-PROBLEM-NOTES items M1, M2).
- **Inherits from Paper 1:** EGY parameterization λ ≡ √(1 − \|⟨W_L\|W_R⟩\|²) and N=1 metric G_λλ = 1/[2(1 − λ²)].
- **Cross-checks with Paper 4:** Σ → M kernel may coincide with Paper 4 Theorem A's RG-smearing isometry.

### Paper 6 (when started) inherits

- λ-manifold = round S² of radius 1/(2√2) (verified).
- Geodesic length π/(2√2) ≈ 1.107 (verified).
- AdS₃ × S³ boundary identification with Σ from Paper 4.

---

## "Already in flight" verification queue (Opus 4.6)

| Item | Source | Status |
|---|---|---|
| Paper 2C §8 FR holonomy / Proietti / Eq. 8.4.5 (omnibus #18, #19, #20) | VERIFICATION_FR_HOLONOMY_OPUS46_2026-04-18 | SUBSTANTIALLY VERIFIED 2026-04-18 |
| Paper 3 RC-1 first draft | idea_assignments §5 update 2026-04-15 | First draft complete; Opus pass required |
| Paper 2C C4 (POVM additivity for d=2) | C4_AXIOM_DECISION_2026-05-01.md | ✅ CLOSED — Busch 2003 axiom adopted; Route B → Paper 5 |

---

## Items where multiple papers all wait on one upstream result

| Upstream result | Owners | Downstream papers | Estimate |
|---|---|---|---|
| RC-4 sourced EOM (k_c^eff, c_Γ) | Paper 3 | 2C §RC1.4 + Paper 3 §3 + Paper 4 §3–4 | ✅ CLOSED 2026-05-01 |
| RC-1 Opus verification | Cowork session | Paper 3 §3 + Paper 4 §3–4 | 1 verification session |
| ζ-regularization | Paper 3 | T2.5-B cosmology + GW parameter window | 1–2 sessions |
| C4 axiom decision (derive or adopt) | Cowork session + Paper 2C §6 | Paper 2C §6 publishability | ✅ CLOSED 2026-05-01 |

---

## Items NOT in any per-paper ledger (project-level only)

- **TASKS.md is stale (last updated 2026-02-14).** Recommendation: rebuild from this rollup or formally retire `TASKS.md` in favor of the per-paper ledgers + this rollup.
- **Paper-1 published version (OSF MetaArXiv 2026-02-14).** No active maintenance; flagged here only to confirm the rollup recognises it as closed.
- **Seraphim post-series program** (`papers/seraphim_consciousness_post_series_program.md`). Held separately; not in physics-paper publication path. Listed here for orientation — see Project-Trajectory note in `papers/07-consciousness-program/PROJECT-TRAJECTORY.md`.
- **Comparative consciousness analysis (LLMs / humans / dogs / cats)** seeded in `seraphim_consciousness_post_series_program.md` 2026-04-13 update. Held until Papers 3/4 close; will become Papers 7/8 input.

---

## Realistic Status (project-wide, 2026-04-30)

**Verified:**
- Paper 1 published.
- Paper 2 omnibus ledger is gold-standard; 2A/2B both ≥85%; 2C structurally complete with closed Phase 1 (D1, D2, D3a) deliverables.
- Per-paper ledgers now exist for Papers 2, 2C, 3, 4 in identical format.
- Bloch↔Penrose verified geometric results (λ-manifold = S²(1/(2√2)), geodesic π/(2√2)).

**Untested:**
- Per-paper ledgers (created today) have not been reviewed against source files line-by-line; counts/categorizations are best-effort from the most recent state of each paper folder.
- The Papers 5/6 stub is purely scoping; no formal ledger structure yet.

**Missing:**
- Paper 5/6 manuscript scaffold.
- Paper 7/8 manuscript scaffold (consciousness program).
- TASKS.md refresh.
- A single project-wide critical-path diagram (Mermaid?) — could be added if requested.

**Unknown:**
- Whether the H-Only / orthoverse / coherosphere vocabulary (Paper 3 items #25–#26) will survive peer review intact, or whether neutral renaming will be needed for physics-journal venues.
- Whether Paper 5 and Paper 6 are best as separate manuscripts or one combined paper — decision deferred until the transformer kernel is written down explicitly.

**Next Steps:**
1. Verify the four new ledger files render and link correctly (Task #13 below).
2. Append the new ledger creation to `memory/kb/INDEX.md`.
3. ~~Bryan to triage~~ — RC-4 and C4 now closed. Next: RC-1 Opus verification pass (critical path item #2).

**Realistic Status: 100% complete on the gap-tracking infrastructure refactor.** All four ledgers and this rollup created today; Papers 2, 2C, 3, 4 now have ledgers in identical format; Papers 5/6 stub anchors the future-paper program; project-level rollup gives the cross-paper picture in one place.

**Paper 2A note (2026-05-02):** "Draft complete" designation was premature. Paper 2A §7 (EOM / F^A derivation from H_SE) and §2.3.1 (open-system transport) are needed to fulfill Paper 1's explicit promises at lines 778 and 331 respectively. Paper 2A status reverted to Active draft until those sections are verifiably closed.


---

## Paper 1 Promise Fulfillment Tracking (added 2026-05-02)

Five structural commitments in Paper 1 are partially delivered and must not fall through the cracks. Each is assigned a canonical section. Items move from PARTIAL to CLOSED when that section is verifiably complete.

### ⚠️ PARTIAL — requires designated section work

| Paper 1 promise | P1 line | Designated section | Status |
|---|---:|---|---|
| Stochastic V_stoch with explicit drift F^A from H_SE | 778 | **Paper 2A §7.9** (`paper2_section_7.9_stochastic_drift_FA_DRAFT.md`) | ✅ DRAFTED 2026-05-02 — F^r = Γ_dec sin(2√2 r)/(2√2), D(r) = A⁴Γ₀ derived from H_SE via Born-Markov; full stochastic action Eq. 7.9.16 explicit; P2/P6 estimates derived, P3/P4 scaffolded |
| Emergent metric + embedding geometry (C¹ regularity explicit form) | 844 | **Paper 2B §4.4.8 + §4.6** (`paper2_section_4.4_addendum_KKcone_regularity_DRAFT.md`, `paper2_section_4.6_emergent_metric_DRAFT.md`) | ✅ DRAFTED 2026-05-02 — Reg1–3 verified for cos(√2 r) (§4.4.8); Gᴇᴹᴼ = N₀²η_μν with N₀²=16√2/(3π)≈2.40, G₄=3G₅/4, K_μν=0 brane minimal (§4.6); Gᴇᴹᴼ=η_μν grounding deferred to Paper 3 Axiom B per architectural split rule |
| Full holographic connections (RT-style closure) | 1034, 1056 | **Paper 2C §RC1.4 + §8** (structure); **Paper 4 §3** (RT closure) | ⚠️ SPLIT — 2C carries structural side; full Ryu–Takayanagi verification is Paper 4 scope |
| Non-unitary transport: coarse-graining, partial trace, open-system reduction | 331 | **Paper 2A §2.5** (`paper2_section_2.5_nonunitary_transport_DRAFT.md`) | ✅ DRAFTED 2026-05-02 — CPTP generalization, coarse-graining, partial-trace, Lindblad transport all formalized; Prop. 2.5.1 (Markov=CPTP dominance); hierarchy table; Paper 2C §5 G1 gauge forward ref |
| Gauge symmetry redundancy test | 377 | **Paper 2C §5 / G1 Phase 2** | ⚠️ OPEN — Phase 1 (covariance proved 2026-04-27) CLOSED; Phase 2 orbit classification ~2–3 weeks |

### Architectural split rule (established 2026-05-02)
**For any Paper 1 promise that has both an effective-theory statement and a first-principles grounding, the effective result lives in Paper 2 (2A abstract / 2B specific geometry / 2C consequences) and the grounding lives in Paper 3 (axioms, field content, interface contracts). Paper 2 delivers the structural result conditionally on Paper 3's grounding; Paper 3 closes the contingency.**
This rule applies uniformly to:
- Line 844 (emergent metric): 2B §4.6 gives Gᴇᴹᴼ = f₀(0)²η_μν = N₀²η_μν by Poincaré symmetry; absorbed to η_μν in 4D Planck units via G₄=G₅/I₂; Paper 3 Axiom B grounds the field-theoretic identification of |e₀⟩
- Lines 1034/1056 (holographic connections): 2C §RC1.4+§8 gives structural side; Paper 4 §3 closes Ryu–Takayanagi
- General principle: 2B/2C results are valid *given* the Paper 3 grounding; Paper 3 closes the contingency (interface contracts P3-H3/P3-H4)

### ✅ APPROPRIATELY DEFERRED — correctly designated, not at risk

| Paper 1 promise | P1 line | Designated section | Status |
|---|---:|---|---|
| FR / Proietti holonomy calculations | 663 | **Paper 2C §8** | Substantially verified (Opus 4.6, 2026-04-18); conditional on composite-angle details |
| Dynamical Born rule (SCF → COV chain) | 1056 | **Paper 2C §6** | ~90% complete; G1 Phase 1 proved |
| Temporal parallel full M×Σ unification | 754, 1034 | **Paper 2B §3–4** (structural) + **Paper 2C** (dynamical) | On track with paper splits |

---

## Deferred Items — Return To

- **λ disambiguation editorial pass** (added 2026-05-02): `notes/NOTATION_DISAMBIGUATION_LAMBDA_2026-05-02.md` is the authoritative reference. Eight distinct λ symbols catalogued. Critical finding: EGY λ (0→1) and KK-cone λ_A = A(r)² (1→0) are INVERTED. Ansatz A* corrected: λ = sin(√2 r), λ_A = 1−λ². Requires 2–3 editorial sessions across P2A/P2B/P2C. P2B §7 is the heaviest hit. P2B §7.9 rewrite is ✅ COMPLETED (see next bullet).
- **Paper 2B §7.9 rewrite** (COMPLETED 2026-05-02): All three issues resolved in `paper2_section_7.9_stochastic_drift_FA_DRAFT.md`. (1) New §7.9.2 notation table + Corrected Ansatz A*: λ = sin(√2 r), λ_A = 1−λ²; (2) New §7.9.4 explains why Lindblad (7.9.8) cannot give logistic dλ/dt (population preservation); (3) New §7.9.5 frames Ansatz (7.9.9) dλ_A/dt = −2Γ_dec λ_A(1−λ_A) explicitly as phenomenological, derives F^r = Γ_dec sin(2√2 r)/(2√2); (4) D = Γ₀ constant, V_stoch(0) = πΓ_dec²/(128√2Γ₀) FINITE derived analytically (§7.9.7); (5) New §7.9.8 Born/Markov validity: m_KK/Γ_dec ≈ 14 verified. F^r formula unchanged; status correctly downgraded to ANSATZ.
- **File migration audit** (added 2026-05-02): When a full-disk grep is needed to find something, the file is misplaced. Audit for: (1) KB entries not in memory/kb/; (2) derivation files outside per-paper ledgers; (3) idea content that should be in section drafts. Use _vault/AGENT_GUIDE.md path registry as authority. Goal: all content findable without grep.
- **Tetris toy model of record settlement** (): Draft placeholder committed 2026-05-02. Correspondence: falling piece → λ-trajectory, locking → G_λλ→∞, complete rows → observer-independent facts, incomplete rows → frame-local, line-clear → immutable causal record. Placement in Paper 2A (§7 EOM or illustrative appendix) and figure TBD. Return to for: (1) figure, (2) named Proposition on line-clear irreversibility, (3) Ω_AB rotation-hysteresis extension as discrete Prediction 2.
