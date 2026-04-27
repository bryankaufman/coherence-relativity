# Paper 2: Coherence Relativity II — Restructured Outline
## Scope Decision (2026-04-11)
The April 9–10 revision session resolved OP-5, derived μ=√2 from first principles, established geometric Λ>0, and removed all Klein dependencies. These changes dissolved the Paper 2 / Paper 2B boundary: essentially everything in the assembled document follows from the coherence axioms without plugging in physical constants.
**Excluded from Paper 2:** Dark matter (schematic, needs full perturbation eigenvalue problem) and holographic worked example (needs GKPW dictionary completion). These move to Paper 3.
**Included in Paper 2:** Everything that follows from the axiomatic derivation chain, including the self-consistency conditions, the warp factor derivation, and the KK spectrum.
## Revised Series Structure
* **Paper 1:** Coherence frames, Born rule, axioms (A1)–(A4) — SUBMITTED
* **Paper 2:** Joint geometry, derived compactification, warp factor, geometric Λ, self-consistency, predictions (THIS PAPER)
* **Paper 3:** Dark-sector predictions + holographic verification on the KCR-Cone (was Paper 2B)
* **Paper 4:** Emergence and unification (was Paper 3)
## Paper 1 Update Required (Zenodo revision)
Before Paper 2 publishes, update Paper 1 on Zenodo with a brief addendum noting:
* Promises met in Paper 2: T_{MΣ} decomposition, δλ formalism, Markov criterion, emergent geometry, EOM, Born rule extension
* Promises deferred with scope explanation: LQG unification → Paper 4; gauge redundancy test → Paper 4; T_AB dimension-changing compatibility → Paper 4
* F^A derivation: completed in Paper 3 development, result asserted in Paper 2 (promise met at publication time)
* FR holonomy and Zeno framework: included in Paper 2 (promise met)
## Paper 2 Section Outline
### Part I: Formalism (§1–§2)
**§1 Introduction**
* §1.1 From coherence frames to joint geometry
* §1.2 Deliverables (update to reflect unified paper scope + new items: FR holonomy, Zeno)
* §1.3 Thesis
* §1.4 Structure of this paper (REWRITE to match new numbering)
* §1.5 Notation and conventions
**§2 The Coherence-Frame Metric on M × Σ**
* §2.1 The cross-term tensor T_{MΣ} (from Fubini-Study pullback)
* §2.2 The δλ formalism (separated pullback, frame-lag EOM)
* §2.3 Connection to pilot-wave theory (Bohmian Q from BO reduction)
* §2.4 Mixed-state Born rule via purification
* §2.5 Left-right generator decomposition (pointer-sector criterion)
* §2.6 The Markov transition criterion (R_Markov, geometric classicality)
Note: §2.3 moves from its current displaced position to its natural home after §2.2. The Markov criterion becomes §2.6 (matching the HTML comment in the current file). §1.2 and §1.4 need updating to reflect this ordering.
### Part II: Derived Compactification (§3)
**§3 Derived Compactification**
* §3.1 Historical background (century of assumed topology)
* §3.2 Topology as output (S² → Hopf → compact fiber)
* §3.3 What derived compactification constrains (landscape elimination, frozen moduli, KK spectrum, geometric Λ, charge quantization)
Note: §3.3 now absorbs results that were previously in §5.3 (geometric Λ as primary source, Casimir as correction, non-linear KK spacing). The key change: these are framework consequences of A(r) = cos(√2 r), not geometry-specific evaluation.
### Part III: Dynamics and Self-Consistency (§4–§7)
**§4 The 5D Metric and Warp Factor**
* §4.1 The 5D ansatz: ds² = A²(r) η_μν dx^μ dx^ν + dr² (derived, not assumed)
* §4.2 Eigenvalue derivation: k²=2 from FS Laplacian on CP¹
* §4.3 Exact warp factor: A(r) = cos(√2 r), μ=√2 as geometric prediction
* §4.4 WKB validity range (r < 0.08) and Euclidean/Lorentzian duality
* §4.5 Non-traversability and Lindblad contractivity
Note: This merges old §7.8 (eigenvalue analysis) with old §4.0.1 (5D ansatz). The warp factor is now presented as a derived result, not a trial ansatz.
**§5 Abstract Equations of Motion on M × Σ**
* §5.1 The coupled geodesic system (Euler-Lagrange from §2.2 action)
* §5.2 The frame-lag mechanism (universal consequence of T_{MΣ} ≠ 0)
* §5.3 The λ·T consistency requirement
* §5.4 Where evaluation requires geometry-specific input
* §5.5 C¹ regularity: derived vs. assumed compactification
Note: This is the current §4 (abstract EOM) + §4.4 (C¹ regularity), now following the warp factor derivation rather than preceding it.
**§6 Self-Consistency Conditions**
* §6.1 SC1: Spatial flatness (A ~ z·f(r) at late times)
* §6.2 SC2: Gravity localization (volcano potential, graviton zero mode)
* §6.3 SC3: Geometric cosmological constant (warp curvature → Λ_geom > 0)
* §6.4 Casimir quantum correction on the derived interval
* §6.5 The combined SC1+SC2+SC3 system
* §6.6 KK graviton spectrum and ISL bounds
* §6.7 Radion stabilization (OP-5 resolution: topology + cosmology)
Note: This merges old §5.1–§5.2 (SC1/SC2) and old §5.3 (SC3). All results follow from A(r) = cos(√2 r) — they are consequences of the derived warp factor, not independent evaluation.
**§7 Holographic Structure Conjecture**
* §7.1 Motivation: why the M × Σ geometry suggests holography
* §7.2 The conceptual dictionary (4 entries)
* §7.3 Three departures from standard AdS/CFT
* §7.4 Why verification requires dedicated treatment
Note: This is the ABSTRACT holographic conjecture only (old §5). The worked example (old §8), RT numerics, and dS/CFT comparison move to Paper 3.
### Part IV: Quantum-Foundations Applications (§8)
**§8 Quantum-Foundations Applications**
* §8.1 Explicit holonomy for Frauchiger-Renner loops (promised in Paper 1, line 531)
* §8.2 Explicit holonomy for Proietti-type loops
* §8.3 Quantum Zeno: four-explanation comparative framework (promised in Paper 1, line 558)
* §8.4 Pointer-basis dependence as CR-specific Zeno prediction
Note: These are self-contained quantum-foundations applications of the M×Σ formalism that Paper 1 explicitly defers to Paper 2. They require only the transport/holonomy machinery of §2 and the pointer-sector criterion of §2.5. NEW WORK REQUIRED.
### Part V: Closing (§9–§10)
**§9 Discussion**
* §9.1 What the framework achieves
* §9.2 The abstract-evaluation split (GR analogy)
* §9.3 The derived-topology program
* §9.4 Connections to existing physics
* §9.5 Relation to Paper 3 (dark matter and holographic verification)
* §9.6 Scope evolution from Paper 1 (explicit accounting of deferred promises)
**§10 Open Problems**
* Organized by tier: Paper 3 questions, Paper 4 questions, experimental questions, internal consistency
* OP-5 RESOLVED, OP-24 RESOLVED, OP-18 RESOLVED
* OP-25/26 (TSVF connections) remain open
* F^A derivation: result from Paper 3 to be pulled forward before publication
## Key Numbering Changes
Current → New mapping:
* §2.3 (pilot wave) → §2.3 (stays, now in correct position)
* §2.3/§2.6 (Markov) → §2.6
* §4.0 (5D ansatz) → §4.1
* §7.8 (eigenvalue) → §4.2–§4.4
* §4 (abstract EOM) → §5
* §4.4 (C¹ regularity) → §5.5
* §5.1–§5.2 (SC1/SC2) → §6.1–§6.2
* §5.3 (SC3) → §6.3–§6.4
* §5 (abstract holographic) → §7
* §6 (dark matter) → PAPER 3
* §7 (EOM worked example) → absorbed into §4 and §5
* §8 (holographic worked example) → PAPER 3
* §6 (discussion) → §8 [NOTE: outline says §9]
* §7/§10 (open problems) → §9 [NOTE: outline says §10]
## What Moves to Paper 3
1. §6 Geometric dark matter (entire section)
2. §8 Holographic worked example (§8.0–§8.10: dictionary verification, RT numerics, dS/CFT comparison, boundary correlators)
3. §5.2.8 Quantitative SC2 results (specific μ values, physical-unit predictions) — the abstract SC2 structure stays
4. Appendix B (G_eff KK tower schematic)
## Equation Renumbering Required
All internal equation references (Eq. 2.3.x for Markov → Eq. 2.6.x, etc.) need updating. This is mechanical but extensive — best done by script after the section structure is approved.
## Abstract Update Needed
The March 25 abstract references Paper 2B and uses old notation (r_fiber, Klein-era framing). Needs full rewrite to reflect:
* Single unified paper
* Geometric Λ (not Casimir-primary)
* μ=√2 as geometric prediction
* Non-linear KK spectrum as key prediction
* OP-5 resolved
* Dark matter and holographic verification deferred to Paper 3
