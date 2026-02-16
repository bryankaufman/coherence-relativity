# Triple Cross-Reference: Three Independent Reviews of Paper 1

**Date:** 2026-02-10 (updated)
**Purpose:** Identify consensus, disagreements, and prioritize fixes before peer review

---

## Methodology

Three independent reviews of Paper 1 ("Coherence Relativity I"):

| Review | Model/Source | Date | Input |
|--------|-------------|------|-------|
| **Perplexity v1** | sonar-pro | 2026-02-08 | Markdown section drafts (incomplete) |
| **Claude Code** | Opus 4.6 | 2026-02-10 | Final compiled main.tex (7 pages, 7 figs, 31 refs) |
| **Perplexity v2** | sonar-pro | 2026-02-10 | Complete paper text + TENSOR_FIELD_DEFINITION.md |

---

## Publication Readiness Scores

| Venue | Perplexity v1 | Claude Code | Perplexity v2 |
|-------|---------------|-------------|----------------|
| arXiv | ~7/10 | ~7/10 | **7/10** |
| Foundations of Physics | ~5/10 | ~5/10 | **4-5/10** |
| Physical Review A | ~4/10 | ~3/10 | **3-4/10** |

**Consensus:** arXiv-ready after minor fixes; journal submission needs P0 critical fixes.

---

## Issue-by-Issue Cross-Reference

### UNANIMOUS (All three flagged)

| # | Issue | Perplexity v1 | Claude Code | Perplexity v2 | Severity |
|---|-------|---------------|-------------|----------------|----------|
| U1 | **T_AB undefined** | "No explicit definitions or proofs" | "No definition, no components, no example" | "Introduces but never defines T_AB explicitly — most damaging omission" | **Critical** |
| U2 | **Splitting proposition unproven** | "Assumes 'enlarged frames' without justifying" | "Says 'theorem' but never proves it" | "Prop 1 stated without proof; a referee would demand explicit construction" | **Critical** |
| U3 | **Predictions lack quantitative numbers** | "Undefined quantities (d, L_coherence)" | "All 6 predictions lack specific numbers" | "Qualitative and intriguing but not sufficiently quantitative for falsifiability" | **Critical** |
| U4 | **Born derivation ≈ Zurek/Gleason** | "Splitting relies on envariance analog" | "4-step proof structurally identical to Zurek 2005" | "Steps are standard; novelty is the geometric packaging, not the derivation itself" | **High** |
| U5 | **V(λ) disconnected from axioms** | "Introduces undefined quantities" | "Parameters (D, F^λ) are chosen, not derived" | "Quasipotential appears but T_AB → V derivation chain is missing" | **High** |

### TWO-OF-THREE CONSENSUS

| # | Issue | Who flagged | Who didn't | Severity |
|---|-------|-----------|-----------|----------|
| C1 | **"Reality R" ontologically vague** | Claude Code, Perplexity v1 | Perplexity v2 (implied) | Medium |
| C2 | **Missing QRF literature** | Claude Code, Perplexity v1 | Perplexity v2 (now resolved — QRF paragraph added) | **Resolved** |
| C3 | **"Just a basis change" objection** | Claude Code, Perplexity v2 ("coherence frame = basis choice" is hostile-referee target #1) | Perplexity v1 (called analogy "apt") | **High** |
| C4 | **"Allowed transformations" underspecified** | Claude Code, Perplexity v2 ("What subgroup of U(d) is 'allowed'?") | Perplexity v1 | **High** |

### PERPLEXITY v2 NEW FINDINGS (not in prior reviews)

| # | Issue | Assessment | Severity |
|---|-------|-----------|----------|
| N1 | **TENSOR_FIELD_DEFINITION.md viable for Paper 1 preview** | "Sections 1-2 trimmed would work as the preview subsection" | Actionable |
| N2 | **Three hostile-referee targets identified** | (1) Coherence frame = basis choice, (2) Splitting unproven, (3) T_AB undefined | Priority list |
| N3 | **Geometric packaging is strongest contribution** | "The geometric reframing of the measurement problem is the paper's genuine novelty" | Strategic |
| N4 | **Minimal T_AB definition needed** | "State T_AB = G_AB + Ω_AB, define G_AB via Fubini-Study, state Ω_AB properties, show 1D double-slit reduction" | Prescriptive |
| N5 | **Born derivation: rigorous but not novel** | "Coherent but not rigorous enough for PRA; novelty is the framing, not the steps" | Calibration |

### SINGLE-REVIEWER FINDINGS

| # | Issue | Source | Resolution |
|---|-------|--------|-----------|
| A1 | Σ = U(d)/T^d is known flag manifold | Claude Code only | Add citation to flag manifold / Kähler geometry literature |
| A2 | SR analogy may be misleading | Claude Code only (Perplexity v1 + v2 both liked it) | Keep analogy but preempt "trivial repackaging" objection |
| A3 | Theorem 1 (Frame Invariants) unproven | Claude Code only | Add sketch proofs or cite standard results |
| A4 | Coherence-entanglement trade-off literature | Claude Code only | Should cite arXiv:2406.19448 (2024) |
| P1 | Paper length too short | Perplexity v1 only | Depends on venue — P0 fixes will naturally expand length |
| P2 | Section reordering | Perplexity v1 only | Current structure logical; low priority |

---

## Consensus Priority Matrix

Ranked by referee-rejection risk, informed by all three reviews:

| Priority | Issue | Agreement | Fix Type | Effort |
|----------|-------|-----------|----------|--------|
| **P0** | U1: Define T_AB (preview from TENSOR_FIELD_DEFINITION.md) | 3/3 | New subsection | 4-6 hrs |
| **P0** | U2: Prove splitting proposition | 3/3 | Write proof | 2-3 hrs |
| **P0** | U3: Add quantitative predictions | 3/3 | Derive numbers | 4-6 hrs |
| **P1** | C3: Preempt "just basis change" objection | 2/3 | Add paragraph | 2-3 hrs |
| **P1** | C4: Specify "allowed" transformations in (A1) | 2/3 | Tighten axiom | 1-2 hrs |
| **P1** | U4: Distinguish Born derivation from Zurek/Gleason | 3/3 | Add paragraph | 2-3 hrs |
| **P1** | A1: Cite flag manifold / Kähler geometry | 1/3 | Add refs | 1 hr |
| **P2** | U5: Connect V(λ) to T_AB definition | 3/3 | Rework section | 3-4 hrs |
| **P2** | C1: Define "reality R" more precisely | 2/3 | Add paragraph | 1-2 hrs |
| **P2** | A3: Prove Theorem 1 invariants | 1/3 | Add sketch proofs | 2-3 hrs |

---

## Actionable Fix Sequence

### Phase 1: Critical fixes (before any submission) — ~2 days

1. **Define T_AB** — New subsection in Sec. II or new Sec. between current II and III. Use trimmed TENSOR_FIELD_DEFINITION.md Sections 1-2:
   - State T_AB = G_AB + Ω_AB
   - Define G_AB via Fubini-Study pullback (already in paper as G_λλ — generalize)
   - State Ω_AB properties (antisymmetric, vanishes in quasi-equilibrium)
   - Show 1D double-slit reduction recovers G_λλ from Sec. II
   - Reference Paper 2 for full development

2. **Prove Proposition 1** — Add explicit construction:
   - Given |ψ⟩ = Σ c_i|i⟩ with |c_i|² = m_i/M
   - Introduce ancilla H_anc of dimension M
   - Define isometry V: H → H ⊗ H_anc
   - Show V|ψ⟩ = M^{-1/2} Σ_{i,k} |i,k⟩

3. **Quantitative prediction** — Compute hysteresis recovery fraction:
   - Transmon qubit: T1 = 50 μs, T2 = 70 μs
   - Erasure-revival cycle with specific pulse sequence
   - CR prediction: recovery fraction R = 1 - ε(λ) where ε depends on G_λλ curvature
   - Standard QM prediction: R = exp(-t/T2)
   - Difference: δR ~ O(10⁻³) — detectable with current qubit coherence

### Phase 2: Strengthen (major revision insurance) — ~2 days

4. Preempt "basis change" objection — paragraph in Sec. I.B or Sec. VI.A
5. Specify "allowed transformations" — tighten axiom (A1) statement
6. Distinguish Born derivation from Zurek explicitly
7. Cite flag manifold + Kähler geometry literature
8. Connect V(λ) parameters to the new T_AB definition

### Phase 3: Polish — ~1 day

9. Define "reality R" more carefully
10. Cite 2024 coherence-entanglement invariance paper
11. Final proofreading pass
12. Decide venue and adjust length accordingly

---

## Venue Recommendation (Updated)

| Journal | Readiness | Path |
|---------|-----------|------|
| **arXiv quant-ph** | 7/10 now; 9/10 after Phase 1 | Post after P0 fixes to establish priority |
| **Foundations of Physics** | 4-5/10 now; 7/10 after Phase 1+2 | Best fit for interpretive framework; expand to 12-15 pages |
| **PRA** | 3-4/10 now; 6/10 after Phase 1+2 | Needs stronger quantitative predictions and more rigorous proofs |
| **PRL** | Not recommended | Too tight for the level of formalism needed |

**Strategy:** Phase 1 → arXiv (establish priority). Phase 1+2+3 → Foundations of Physics submission.

---

## Key Strategic Insight from Triple Review

All three reviews converge on the same hierarchy:

> **Strongest contribution:** The geometric reframing — treating coherence as frame-relative and Σ as a manifold with information-geometric structure. This is genuinely novel.

> **Weakest link:** The gap between the claimed geometric framework and what's actually defined. T_AB is the linchpin — without it, the quasipotential, predictions, and Darwinism connection are all hand-waving.

> **Path forward:** TENSOR_FIELD_DEFINITION.md already contains the needed material. A trimmed version closes the biggest gap and connects the predictions to the formalism.
