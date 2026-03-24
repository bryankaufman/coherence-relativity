# Paper 2 Split: Framework (2) + Application (2B)
**Date:** 2026-03-10 (v2 — revised per Bryan's structural insight)
**Status:** DRAFT — for Bryan review
**Prior version:** v1 split all seven Paper 1 promises across two papers. Bryan's feedback: "Can we combine all of the deliveries on promises from Paper 1 into Paper 2 as we originally planned?" and "Can we present the KK-Cone-entangled concepts first in standard model, show their limitations, and then what's left as a segue to Paper 2B?"

---

## Rationale (v2)

The v1 outline split EOM and holographic into Paper 2B. But both have an *abstract layer* that is genuine framework — the Euler-Lagrange system on general M × Σ, and the conceptual holographic dictionary — plus a *KK-Cone-specific layer* (explicit Christoffel symbols, Ryu-Takayanagi checks, etc.).

Bryan's insight: don't just abstract these away — use the KK-Cone-entangled concepts as a *teaching device*. Present the abstract framework, then show where standard evaluation methods hit walls. This transforms the segue to Paper 2B from "we're deferring this" into "here's exactly why a dedicated evaluation paper is needed."

**Result:** Paper 2 delivers ALL SEVEN Paper 1 promises within a single manuscript. Four via full derivation (Part I–II). Three via the Part III teaching arc: present the abstract framework, contrast with the standard model's limitations, establish the framework-level claim. The companion paper provides geometry-specific evaluation for all three.

---

## Paper 2: Coherence-Space Geometry, Derived Compactification, and the Equations of Motion

**Working title:** *Coherence Relativity II: The Cross-Term Tensor, Derived Compactification, and Equations of Motion on M × Σ*

**Thesis:** The coherence-frame formalism extends to a joint manifold M × Σ with a cross-term tensor T_{MΣ} that encodes quantum-classical coupling. The separation δλ yields a geometric Markov transition criterion. Compactification is derived from topology, not assumed. The abstract equations of motion on M × Σ reveal a frame-lag mechanism and suggest holographic structure — but evaluating these on any specific warped geometry exposes convention dependencies that require dedicated treatment.

### Structure

| § | Title | Content | Source | Status | Model |
|---|-------|---------|--------|--------|-------|
| **Part I: Formalism** |
| 1 | Introduction | Paper 1 recap; seven deliverables; arc of argument | NEW | Not started | sonnet → opus |
| 2.1 | The Cross-Term T_{MΣ} | Fubini-Study pullback on M × Σ; cross-term as coupling tensor | §2.1 FINAL | ✅ FINAL | opus |
| 2.2 | The δλ Formalism | Separated pullback metric; frame-lag EOM; τ_lag prediction | §2.2 DRAFT | Draft exists | opus + sonnet |
| 2.3 | Markov Transition Criterion | Coordinate-invariant R_Markov; model independence; qualitative behavior | §2.3 DRAFT (§2.3.1–2.3.4, §2.3.6 only) | Draft exists, needs trim | sonnet |
| 2.4 | Mixed-State Born Rule | Purification extension of (A1)–(A4); POVM via Naimark | §2.4 FINAL | ✅ FINAL | sonnet |
| 2.5 | Left-Right Generator Decomposition | Schrödinger vs Heisenberg generators; ΔG_{ij}; pointer-sector criterion | Left-Right Draft (2026-03-05) | Draft exists | opus |
| **Part II: Derived Compactification** |
| 3.1 | A Century of Assumed Topology | Kaluza (1921) → string landscape; the persistent gap | §3.1 FINAL | ✅ FINAL | sonnet |
| 3.2 | Topology as Output | S² → Hopf → compact S¹; c₁ = 1 as minimal | §3.2 FINAL | ✅ FINAL | opus |
| 3.3 | What Derived Compactification Constrains | Landscape reduction; moduli elimination; KK spectrum; Λ(R); what remains open | §3.3 DRAFT | Draft exists, needs forward-ref revision | sonnet |
| **Part III: Dynamics, Regularity, and Holography** |
| 4 | Equations of Motion on M × Σ | Abstract Euler-Lagrange system; frame-lag mechanism; standard-model limitations | §7.0 DRAFT (abstract layer) + NEW (limitations) | ⚠️ DRAFT (Wave 5) | opus |
| 4.5 | C¹ Regularity: Standard Model vs. Derived Compactification | RS junction conditions; why derived topology constrains regularity; framework-level claim | §4.4 FINAL (concept) + NEW (SM comparison) | ⚠️ DRAFT (Wave 5) | sonnet |
| 5 | Holographic Structure Conjecture | Conceptual dictionary; three departures from AdS/CFT; why verification needs a geometry | §8.0 DRAFT (abstract layer) + NEW (limitations) | ⚠️ DRAFT (Wave 5) | opus |
| **Part IV: Closing** |
| 6 | Discussion | Framework implications; the derived-topology program; segue to companion paper | NEW | Not started | sonnet → opus |
| 7 | Open Problems | What Paper 2 leaves unresolved; pointers to 2B and Paper 3 | NEW | Not started | sonnet |

### The Teaching Arc of Part III

This is the key structural innovation. Each section in Part III follows a three-act structure:

**§4 — Equations of Motion on M × Σ:**

- **Act 1 — Abstract framework** (from §7.4.1–7.4.2):
  The Euler-Lagrange variation of Paper 1's action on general M × Σ. The M-sector geodesic equation sourced by cross-term coupling. The Σ-sector dynamics driven by frame-lag. The general consistency requirement that λ · T must remain bounded. The frame-lag force as a *universal mechanism*: spatial acceleration on M drives coherence response on Σ.

  *Source material:* §7.0 Eqs. 7.4.1–7.4.2 (general form), §7.2.4–7.2.5 (adiabatic decomposition stated abstractly), §7.5.1–7.5.3 (physical interpretation — geometry-independent parts).

- **Act 2 — Standard-model evaluation hits walls:**
  When you try to evaluate these equations on any specific warped geometry:
  1. **Norm conventions:** The Frobenius norm ||G^(M)|| that defines R_Markov depends on whether you use covariant or contravariant indices. Under all geometrically consistent conventions, R_Markov → O(1) in warped throats (the A²·A^{-2} = O(1) cancellation).
  2. **Cross-term scaling:** T_{μa} depends on the state parameterization, which requires choosing a metric and solving for the ground-state profile.
  3. **Coupling identification:** The identification λ = f(warp factor) requires solving boundary conditions — you need the geometry to determine the function.
  4. **Classical limit:** The "simple" question "does the system classicalize?" turns out to be convention-dependent when evaluated via R_Markov. The robust statement is λ → 0 (convention-independent), but this is a *coupling* statement, not a *geometric norm* statement.

  *Source material:* The §2.3.5 norm audit results (three-model consensus), the convention-lock analysis, Bryan's deep analysis showing R_Markov → O(1).

- **Act 3 — What this means:**
  These are not failures of the framework. The abstract EOM are well-defined and the frame-lag mechanism is robust. But *evaluating* them requires committing to a geometry and resolving convention choices. The companion paper [Paper 2B] provides this evaluation for the KK-Cone — the first physically motivated geometry from derived compactification.

  **Delivered promise:** EOM on M × Σ ✅ (abstract system fully specified; evaluation deferred with explicit justification)

**§5 — Holographic Structure Conjecture:**

- **Act 1 — Conceptual dictionary:**
  The general structure: bulk = M × Σ with state map Φ, boundary = quantum state at maximal coherence (λ = 1), holographic direction = coherence parameter (λ → 0 as decoherence). T_{MΣ} as the boundary-bulk dictionary: cross-term couples boundary observables to bulk dynamics.

  Three ways this departs from standard AdS/CFT:
  1. Unwarped time (breaks conformal symmetry)
  2. 1D coherence sector (not a standard radial direction)
  3. Quantum-information interpretation (r parameterizes coherence, not just energy scale)

  *Source material:* §8.1.1–8.1.3 (motivation and conjecture statement), §8.2.1–8.2.2 (dictionary entries stated in general terms).

- **Act 2 — Standard tools require a geometry:**
  To *verify* the conjecture, you need:
  1. **Ryu-Takayanagi:** Requires computing minimal surfaces, which requires a metric.
  2. **Entanglement entropy:** Requires a UV cutoff and a specific field theory on the boundary.
  3. **Beta function matching:** Requires identifying the RG flow with radial evolution, which requires the warp factor profile A(r).
  4. **Boundary correlators:** Require propagators in the bulk, which require the full metric and field content.

  None of these can be done at the framework level. They all require choosing a geometry.

- **Act 3 — What this means:**
  The conjecture is well-posed. The dictionary is conceptually clear. But it remains a *conjecture* until verified on a concrete geometry. The companion paper provides this verification for the KK-Cone.

  **Delivered promise:** Holographic connections ✅ (conjecture stated with dictionary; verification deferred with explicit justification)

**§4.5 — C¹ Regularity: Standard Model vs. Derived Compactification:**

- **Act 1 — The standard model's C¹ problem:**
  In Randall-Sundrum models, the brane is inserted by hand as a codimension-1 hypersurface. The warp factor A(r) solves the bulk Einstein equations on each side, but at the brane location the solutions are glued together with a kink. A(r) is C⁰ (continuous) but not C¹ (not differentiable) at the brane. The Israel junction conditions relate the discontinuity in A'(r) to the brane tension T_brane. This requires distributional (delta-function) stress-energy — the metric is only piecewise smooth.

  This is not a bug in RS models; it's a feature of *assumed* compactification. When you insert a brane by hand, you're free to choose its tension, and the junction conditions absorb the resulting kink. But it means regularity is *tuned*, not *derived*.

  *Source material:* Standard RS1/RS2 literature; Israel junction conditions; §4.4 FINAL discusses this contrast briefly.

- **Act 2 — Derived compactification constrains regularity:**
  In the coherence framework, you don't insert branes by hand. The compact fiber S¹ emerges from the Hopf fibration over S² (§3.2). The topology of the total space E_{c₁} is fixed. This imposes regularity constraints that assumed compactification simply doesn't have:

  1. **No arbitrary brane insertion:** The locus where the fiber closes off (if any) is determined by the topology, not by a free parameter. You can't place a brane wherever you want.
  2. **Regularity follows from topology:** If the derived total space is a smooth manifold (S³ for c₁ = 1), the metric must be smooth everywhere — unless there is a physical source that creates a singularity. But that source must be *derived* from the field content, not inserted.
  3. **No tension tuning:** The RS approach has brane tension as a free parameter that is tuned to produce the correct hierarchy. In derived compactification, there is no free brane tension. Whatever regularity class the warp profile belongs to is a *prediction*.

- **Act 3 — Framework-level claim:**
  Derived compactification constrains the regularity class of admissible warp profiles. The topology predicts where smooth metrics are required and where singularities (if any) must be sourced by dynamical field content. This is a qualitative departure from the standard model, where regularity is absorbed into junction conditions with tunable brane tensions.

  The specific verification — does the KK-Cone warp factor satisfy C¹ at the cone tip? — requires the explicit geometry and is provided in [Paper 2B, §2.4]. But the *principle* that regularity is constrained by derived topology, not by brane-tuning, is a framework result established here.

  **Delivered promise:** C¹ regularity ✅ (framework principle established; geometry-specific verification in companion paper)

---

### Paper 1 Promise Delivery — All Seven Fulfilled

| Promise | Paper 2 Section | Delivery Type | Status |
|---------|----------------|---------------|--------|
| T_{MΣ} derivation | §2.1 | Full derivation | ✅ FINAL |
| δλ formalism | §2.2 | Full derivation | Draft exists |
| Markov transition criterion | §2.3 | Full derivation (abstract) | Draft exists (needs trim) |
| Mixed-state Born rule | §2.4 | Full derivation | ✅ FINAL |
| EOM on M × Σ | §4 | Abstract system + limitations analysis | Partial draft + new |
| C¹ regularity | §4.5 | SM comparison + framework principle | New (source material exists) |
| Holographic connections | §5 | Conjecture + dictionary + limitations | Partial draft + new |

**All seven promises addressed within Paper 2.** Four are full derivations (§2.1–2.4). Three use the Part III teaching arc: present the abstract framework, contrast with the standard model's limitations, establish the framework-level claim, and point to the companion paper for geometry-specific evaluation.

---

### §4 Source Material Map (§7.0 Draft → Paper 2 §4)

The current §7.0 draft (560 lines) splits into two destinations:

| §7.0 Content | Abstract? | → Paper 2 §4 | → Paper 2B |
|---|---|---|---|
| §7.1 Setup (KK-Cone coords, A(r)=e^{-μr}) | No | — | §EOM setup |
| §7.2.1–7.2.3 (specific zero-mode profile) | No | — | §EOM computation |
| §7.2.4 (state parameterization — general) | **Yes** | §4.1 (abstract) | — |
| §7.2.5 (cross-term scaling — general argument) | **Mostly** | §4.1 (general T scaling) | Specific A^{-2} result |
| §7.3 (λ = A² verification) | No | §4.2 limitations (why λ needs geometry) | §EOM warp verification |
| §7.4.1 (general EOM from §2.2) | **Yes** | §4.1 (abstract EOM) | — |
| §7.4.2–7.4.5 (KK-Cone Christoffel, explicit eqns) | No | — | §EOM explicit |
| §7.5.1–7.5.2 (physical interpretation) | **Mostly** | §4.1 (frame-lag as mechanism) | Specific r-interpretation |
| §7.5.3–7.5.4 (decoherence connection) | **Mostly** | §4.1 (general mechanism) | Specific timescales |
| §7.6 (status summary) | Mixed | Split across both | Split across both |

**Estimate:** ~40% of §7.0 content is abstract enough for Paper 2 §4. ~60% is KK-Cone-specific and goes to Paper 2B.

### §5 Source Material Map (§8.0 Draft → Paper 2 §5)

| §8.0 Content | Abstract? | → Paper 2 §5 | → Paper 2B |
|---|---|---|---|
| §8.1.1 (AdS-like structure) | No (uses KK-Cone metric) | — | §Holographic motivation |
| §8.1.2 (coherence interpretation) | **Yes** | §5.1 (general dictionary) | — |
| §8.1.3 (conjecture statement) | **Yes** | §5.1 (Conjecture 8.1) | — |
| §8.2.1 (state map / boundary state) | **Yes** | §5.1 (dictionary entry 1) | — |
| §8.2.2 (radial direction / RG flow) | **Mostly** | §5.1 (dictionary entry 2) | Specific λ(r) evaluation |
| §8.2.3+ (source coupling, specific checks) | No | §5.2 (why verification needs geometry) | Full evaluation |

**Estimate:** ~30% of §8.0 is abstract enough for Paper 2 §5. ~70% goes to Paper 2B.

---

### Key Changes to Existing Material

**§2.3 — Markov Transition (TRIM):**
- KEEP: §2.3.1–2.3.4, §2.3.6 (abstract framework)
- MOVE TO 2B: §2.3.5 (KK-Cone throat evaluation), §2.3.7 (numerical estimates)

**§2.5 — Left-Right Generators (PROMOTE):**
- Promote from "§X" to §2.5
- Framework-only, no KK-Cone dependency

**§3.3 — Constraints (REVISE forward references):**
- 8 forward references to §4–§8 → point to "companion paper [Paper 2B]" or to new §4/§5
- §3.3.6(c) warp profile: now can point to §4 within the same paper (abstract EOM discusses warp identification as an open question)
- §3.3.11 Paper 3 hooks: KEEP as-is

**§4 — EOM (NEW, drawing from §7.0):**
- Extract abstract layer from §7.0
- Write new "limitations" subsection using norm-audit results
- The abstract EOM (Eqs. 7.4.1–7.4.2) are restated as Eqs. 4.X.Y
- Frame-lag mechanism described in geometry-independent language
- Limitations subsection cites the three-model consensus on convention dependence

**§5 — Holographic Conjecture (NEW, drawing from §8.0):**
- Extract conceptual dictionary from §8.0
- Conjecture statement (restated as Conjecture 5.1)
- Three departures from standard AdS/CFT
- New "verification requires a geometry" subsection

---

## Paper 2B: The KK-Cone Evaluation

**Working title:** *Coherence Relativity IIb: Self-Consistency, Dark Matter, and Holographic Verification on the KK-Cone*

(Note: "IIb" signals this is a companion to Paper II, not a fully independent Paper III. Bryan to confirm.)

**Thesis:** The KK-Cone — the first physically motivated geometry from derived compactification — is evaluated against the framework of Paper 2. Two of three self-consistency conditions close. The equations of motion, specialized to the 5D warped metric, yield testable predictions. The holographic conjecture receives partial verification.

### Structure

| § | Title | Content | Source | Status | Model |
|---|-------|---------|--------|--------|-------|
| 1 | Introduction | Paper 2 recap; the KK-Cone as first evaluation; what this paper tests | NEW | Not started | sonnet |
| 2 | The KK-Cone Model | Metric ansatz, coordinates, conventions | §4.0 FINAL | ✅ FINAL (light reframe) | sonnet |
| 2.4 | C¹ Regularity | Warp-factor regularity verification | §4.4 FINAL | ✅ FINAL | opus |
| 3 | Markov Transition in the Throat | R_Markov evaluation; convention dependence; λ → 0 as primary mechanism | §2.3.5/2.3.7 DRAFT + convention-lock | Draft exists (heavily revised) | sonnet |
| 4.1 | SC1: Spatial Flatness | CLOSED | §5.1 DRAFT | Draft exists | sonnet |
| 4.2 | SC2: Gravity Localization | CLOSED | §5.2 DRAFT | Draft exists | sonnet |
| 4.3 | SC3: Cosmological Constant | Four-path analysis; Casimir on Hopf fiber; r_f* = 13 μm | §5.3 DRAFT | Draft exists | sonnet + numerics |
| 5 | Geometric Dark Matter | Perturbation setup; rotation curves; Bullet Cluster; falsification | §6.0 FINAL | ✅ FINAL | sonnet |
| 6 | Equations of Motion: KK-Cone Specialization | T_{MΣ} computation, λ = A², frame-lag force, explicit dynamics | §7.0 DRAFT (KK-Cone layer) | Draft exists | opus |
| 7 | Holographic Verification | Ryu-Takayanagi check; entanglement entropy; boundary correlators | §8.0 DRAFT (KK-Cone layer) | Draft exists | opus |
| 8 | Discussion | What the KK-Cone teaches; template for future geometries | NEW | Not started | sonnet → opus |
| 9 | Open Problems | Stabilization, higher-c₁, experimental tests | NEW | Not started | sonnet |
| A | Appendix: Metric Norm Conventions | Mixed convention; Eq. 2.3.2b; full derivation | Rederivation + Warp cross-check | Source material exists | — |

### Key Changes from v1

- **§6 (EOM) is now the KK-Cone-specific layer only.** The abstract framework lives in Paper 2 §4. This section opens with: "We now specialize the abstract EOM of [Paper 2, §4] to the KK-Cone geometry."
- **§7 (Holographic) is now the verification layer only.** The conjecture and dictionary live in Paper 2 §5. This section opens with: "We now test Conjecture 5.1 of [Paper 2] against the KK-Cone."
- **Cleaner dependency:** Paper 2B references Paper 2 for *all* formalism. No redundant re-derivations.

---

## Dependency Map (v2)

```
Paper 2                              Paper 2B
========                             ========

§2.1 T_{MΣ}  ───────────────────→  §6 EOM-KKCone (specializes T_{MΣ})
                                     §7 Holographic (uses T_{MΣ})

§2.2 δλ formalism  ─────────────→  §3 Markov in throat (uses λ ~ A²)
                                     §6 EOM-KKCone (uses frame-lag)

§2.3 Markov criterion  ─────────→  §3 Markov in throat (evaluates R_Markov)

§3.2 Topology as output  ───────→  §2 KK-Cone model (geometry from §3.2)
                                     §4.3 SC3 (Hopf fiber → Casimir)

§3.3 Constraints  ──────────────→  §4.3 SC3 (evaluates Λ(R))
                                     §5 Dark matter (tests predictions)

§4 Abstract EOM  ───────────────→  §6 EOM-KKCone (specializes abstract system)

§5 Holographic conjecture  ─────→  §7 Holographic verification (tests conjecture)
```

**Paper 2B cites Paper 2 for ALL formalism and conjectures.** Paper 2 is fully self-contained. Paper 2B is the first worked example.

---

## §2.3.5 Dependency Items: Where They Land (v2)

Unchanged from v1 — all 11 items still land in Paper 2B except item 1 (clean in Paper 2).

| # | Item | Paper | Action |
|---|------|-------|--------|
| 1 | Eq. 2.3.9 (threshold condition) | 2 | Clean as-is (abstract) |
| 2–7, 10 | Concrete norm evaluations | 2B §3 | UPDATE with corrected scaling |
| 8 | ||G^(cross)|| convention | 2B Appendix A | RESOLVED (mixed convention) |
| 9 | §7.0 cross-check | 2B §6 | ✅ CLEAN |
| 11 | Convention lock appendix | 2B Appendix A | WRITE |

**Additionally:** Paper 2 §4.2 (limitations subsection) *references* items 1, 8 as motivation for why norm evaluation requires a geometry — but does not resolve them. Resolution is in Paper 2B.

---

## §3.3 Forward References: Required Edits (v2)

Some references now point *within* Paper 2 (to the new §4 and §5), not all to the companion paper:

| Location | Current Reference | Revised Reference |
|----------|-------------------|-------------------|
| §3.3.5, after Eq. 3.3.9 | "explored in §5 and §7" | "The abstract dynamics are developed in §4; evaluation on the KK-Cone is in [Paper 2B]" |
| §3.3.6(a) radius stabilization | "In §5.3..." | "[Paper 2B, §4.3]" |
| §3.3.6(b) field content | "In §4..." | "[Paper 2B]" |
| §3.3.6(c) warp profile | "This is done in §7" | "The abstract frame-lag mechanism (§4) determines how the warp profile enters the dynamics; explicit solutions require a geometry [Paper 2B, §6]" |
| §3.3.9 open questions | §4, §5, §6, §7, §8 | Mix of §4/§5 (within Paper 2) and [Paper 2B] |
| §3.3.10 transition | "foundation for §4: Low-Energy Effective Action" | "foundation for §4 (Equations of Motion) and the companion paper [Paper 2B]" |

---

## File Inventory with Paper Assignment (v2)

### Paper 2 Files

| File | Current Location | Status | Needs Work |
|------|-----------------|--------|------------|
| §2.1 T_{MΣ} | sections/paper2_section_2.1_TMSIGMA.md | FINAL | None |
| §2.2 δλ | sections/drafts/paper2_section_2.2_delta_lambda_DRAFT.md | DRAFT | Warp review pending |
| §2.3 Markov | sections/drafts/paper2_section_2.3_markov_transition_DRAFT.md | DRAFT | Trim §2.3.5/2.3.7 |
| §2.4 Born rule | sections/paper2_section_2.4_mixed_state_born.md | FINAL | None |
| §2.5 Left-Right | sections/drafts/paper2_section_left_right_generators_...DRAFT.md | DRAFT | Promote from "§X" |
| §3.1 History | sections/paper2_section_3.1_century_assumed_topology.md | FINAL | None |
| §3.2 Topology | sections/paper2_section_3.2_topology_as_output.md | FINAL | None |
| §3.3 Constraints | sections/drafts/paper2_section_3.3_constraints_DRAFT.md | DRAFT | Revise forward refs |
| **§4 Abstract EOM** | paper2_section_4_abstract_EOM_DRAFT.md | ⚠️ DRAFT | Bryan review needed |
| **§4.5 C¹ Regularity** | paper2_section_4.5_C1_regularity_SM_comparison_DRAFT.md | ⚠️ DRAFT | Bryan review needed |
| **§5 Holographic** | paper2_section_5_holographic_conjecture_DRAFT.md | ⚠️ DRAFT | Bryan review needed |
| §1 Introduction | — | NOT STARTED | Write |
| §6 Discussion | — | NOT STARTED | Write |
| §7 Open Problems | — | NOT STARTED | Write |

### Paper 2B Files

| File | Current Location | Status | Needs Work |
|------|-----------------|--------|------------|
| §2 KK-Cone model | sections/paper2_section_4.0_KK_Cone_model.md | FINAL | Light reframe |
| §2.4 C¹ regularity | sections/paper2_section_4.4_C1_regularity.md | FINAL | None |
| §3 Markov in throat | (extract from §2.3 DRAFT) | DRAFT | Reframe with λ→0 primary |
| §4.1–4.2 SC1, SC2 | sections/drafts/paper2_section_5.1_5.2_SC1_SC2_DRAFT.md | DRAFT | Split and finalize |
| §4.3 SC3 | sections/drafts/paper2_section_5.3_SC3_DRAFT.md | DRAFT | Integrate Casimir |
| §5 Dark matter | sections/paper2_section_6.0_geometric_dark_matter.md | FINAL | None |
| §6 EOM-KKCone | sections/drafts/paper2_section_7.0_EoM_MxSigma_DRAFT.md (60%) | DRAFT | Remove abstract layer; add 2 cross-refs |
| §7 Holographic verif. | sections/drafts/paper2_section_8.0_holographic_...DRAFT.md (70%) | DRAFT | Remove dictionary; add 2 cross-refs |
| §A Convention lock | — | NOT STARTED | Write |
| §1, §8, §9 | — | NOT STARTED | Write bookends |

---

## Build Order (v2)

### Paper 2 Build

```
Wave 1 (already done):
  §2.1 ✅, §2.4 ✅, §3.1 ✅, §3.2 ✅

Wave 2 (in progress):
  §2.2 — Warp review pending, then finalize
  §2.5 — Promote left-right draft; Opus polish

Wave 3 (after §2.2):
  §2.3 — Trim KK-Cone subsections; finalize abstract criterion

Wave 4 (after §3.2):
  §3.3 — Revise forward references; address Opus review issues

Wave 5 (after §2.3 + §3.3):    ← THIS IS THE NEW WORK
  §4 — Abstract EOM (extract from §7.0 + write limitations subsection)
  §4.5 — C¹ Regularity (SM comparison + framework claim; sonnet, shorter section)
  §5 — Holographic conjecture (extract from §8.0 + write limitations subsection)
  MODEL: Opus for §4 and §5 (novel derivation-level); Sonnet for §4.5 (structured comparison)

CHECKPOINT: Human review of §4 + §5 (the new Part III)

Wave 6 (after checkpoint):
  §1 — Introduction (sonnet → opus)
  §6 — Discussion (sonnet → opus)
  §7 — Open Problems (sonnet)
```

### Paper 2B Build

```
Wave 1 (after Paper 2 §4/§5 are final):
  §2 — KK-Cone reframe (light edits to §4.0 FINAL)
  §3 — Markov in throat (extract from §2.3, reframe)
  §A — Convention lock appendix

Wave 2 (parallel):
  §4.1–4.2 — SC1, SC2 (finalize drafts)
  §4.3 — SC3 + Casimir (integrate numerics)
  §5 — Dark matter (already FINAL, light reframe)

Wave 3 (after Paper 2 §4 is final):
  §6 — EOM-KKCone (§7.0 minus abstract layer + Paper 2 cross-refs)

Wave 4 (after Paper 2 §5 is final):
  §7 — Holographic verification (§8.0 minus dictionary + Paper 2 cross-refs)

CHECKPOINT: Human review of §6 + §7

Wave 5 (after checkpoint):
  §1 — Introduction
  §8 — Discussion
  §9 — Open Problems
```

---

## Status Summary (v2)

### Paper 2
- 4 of 13 sections FINAL (§2.1, §2.4, §3.1, §3.2)
- 4 sections have drafts needing revision (§2.2, §2.3, §2.5, §3.3)
- 3 sections now have Wave 5 DRAFTS (§4, §4.5, §5) — need Bryan review
- 3 sections not started (§1, §6 Discussion, §7 Open Problems)
- **Realistic estimate: 65% of content exists in some form** (up from 55%)

### Paper 2B
- 3 of 13 sections FINAL or near-final (§2 KK-Cone, §2.4 C¹, §5 Dark matter)
- 6 sections have drafts (§3, §4.1–4.3, §6, §7) — some need to shed abstract layer
- 4 sections not started (§1, §8, §9, Appendix A)
- **Realistic estimate: 50% of content exists in some form**

### ✅ COMPLETED (Wave 5 — 2026-03-10)
- §4 Abstract EOM draft written — extracted abstract layer from §7.0 + new §4.2 limitations subsection (~2,500 words)
- §4.5 C¹ Regularity SM comparison draft written — three-act teaching arc: RS junction conditions → derived topology → framework claim (~1,800 words)
- §5 Holographic Conjecture draft written — extracted dictionary from §8.0 + new §5.2 verification-requires-geometry (~2,800 words)
- §3.3 forward-reference edits applied by Warp (16 edits, verified v2-compatible)

### ⚠️ UNTESTED
- The §4/§5/§4.5 drafts have NOT been reviewed by Bryan — they are first drafts
- The §2.3 trim has not been done (Warp — Wave 3)
- Paper 2B's convention lock appendix has not been written
- The residual §7.0 and §8.0 content (KK-Cone layers for Paper 2B) has not been separated into standalone files

### 🤔 UNKNOWN
- Whether "Paper 2B" or "Paper IIb" or some other numbering
- Whether the left-right generators draft is mature enough for §2.5
- Whether §3.3's Opus review issues should be addressed before or after the split
- Whether the §4 limitations subsection (§4.2) captures all the relevant norm-audit findings — Bryan should verify

---

## Next Steps (updated 2026-03-10)

1. ~~**Extract §4 from §7.0**~~ — ✅ DONE (Wave 5)
2. ~~**Extract §5 from §8.0**~~ — ✅ DONE (Wave 5)
3. ~~**Write §4.5 C¹ Regularity**~~ — ✅ DONE (Wave 5)
4. ~~**Revise §3.3 forward references**~~ — ✅ DONE (Warp)
5. **Bryan reviews Part III drafts (§4, §4.5, §5)** — CHECKPOINT
6. **Trim §2.3** — remove §2.3.5/2.3.7; file them for Paper 2B (Warp — Wave 3)
7. **Finalize §2.2** — Warp review results pending
8. **Promote §2.5** — left-right generators
9. **Write Paper 2 bookends** — §1 intro, §6 discussion, §7 open problems (Wave 6)
10. **Begin Paper 2B** — once Paper 2's Part III is stable
