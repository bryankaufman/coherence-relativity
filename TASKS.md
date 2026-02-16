# Coherence-Relativity Project Tasks

**Last Updated**: 2026-02-14
**Overall Status**: Paper 1 — **PUBLISHED** on OSF MetaArXiv
**Preprint URL**: https://osf.io/preprints/metaarxiv/3g8ub_v1

---

## Status Overview

### Environment & Tooling
- [x] Python venv (uv) with numpy, pandas, scipy, matplotlib, sympy
- [x] Zotero Better BibTeX configured, 31 papers in collection DZX5AAD3
- [x] LaTeX build verified (RevTeX4-2, pdflatex + bibtex, TeX Live 2025)
- [x] `scripts/refresh-bib.sh` for on-demand Zotero → master.bib export
- [ ] Configure persistent BBT auto-export (Zotero GUI)

### Numerical Calculations
- [x] G_λλ(λ) — computed from multi-mode FS metric (N=10), U-shaped with min at λ≈0.41
- [x] V(λ) — quasipotential = accumulated FS distance to classical frame
- [x] s(λ) — accumulated FS length, showing crossover plateau
- [x] Validated standard QM visibility V = sqrt(1 - λ²)

### Figures (7/7 complete)
- [x] Figure 1: G_λλ(λ) metric plot
- [x] Figure 2: V(λ) quasipotential landscape
- [x] Figure 3: Frame transformation diagram
- [x] Figure 4: Born rule as frame invariant (SR analogy)
- [x] Figure 5: Double-slit in two coherence frames
- [x] Figure 6: CR prediction vs standard QM
- [x] Figure 7: Experimental setup schematics

### Paper Content
- [x] Abstract (230 words)
- [x] Section I: Introduction (measurement problem as frame problem)
- [x] Section II: Coherence Frames (definitions, examples, metric, **T_AB definition**, SR analogy)
- [x] Section III: Frame Transformations (maps, group structure, splitting with **proof**, invariants)
- [x] Section IV: Born Rule (statement, derivation, comparison, interpretation)
- [x] Section V: Paradox Resolutions (double-slit, Wigner, EPR, cat)
- [x] Section VI: Discussion (measurement problem, quasipotential **with action**, Darwinism, **quantitative** predictions, QRF comparison)
- [x] Section VII: Conclusion
- [x] Bibliography: 34 entries, 28 cited (5 QRF + 2 flag manifold + 1 coherence-entanglement invariance)

### LaTeX
- [x] `papers/01-coherence-frames/main.tex` — **10-page** paper, zero errors, zero undefined refs
- [x] All 7 figures included with captions
- [x] 2 comparison tables (SR analogy, Born rule derivations)
- [x] Theorem/definition/proposition environments
- [x] Cross-references and equation numbering
- [x] Bibliography via `\bibliography{../../bibliography/master}`

### Reviews (triple cross-reference complete)
- [x] Perplexity v1 (2026-02-08): Markdown section drafts
- [x] Claude Code (2026-02-10): Final compiled paper
- [x] Perplexity v2 (2026-02-10): Complete paper + TENSOR_FIELD_DEFINITION.md
- [x] Triple cross-reference: `notes/REVIEW_CROSS_REFERENCE.md`

---

## P0 Critical Fixes (DONE)

1. [x] **T_AB defined** — New subsection II.E with T_AB = G_AB + Ω_AB decomposition, Fubini-Study pullback formula, Ω_AB properties, 1D double-slit reduction
2. [x] **Splitting proposition proved** — Explicit ancilla construction with isometry V: H → H⊗H_anc
3. [x] **Quantitative predictions added** — Hysteresis deficit δV ~ 4×10⁻⁴ for transmon qubit; frame-transformation timescale τ ≥ 0.6 μs
4. [x] **QRF literature cited** — 5 papers added, distinguishing paragraph in Sec. VI.E

---

## Remaining Work

### Phase 2: Strengthen (DONE)
- [x] Preempt "just a basis change" objection — new paragraph in Sec I.B
- [x] Specify "allowed transformations" — axiom (A1) now references relabelings + splittings explicitly
- [x] Distinguish Born derivation from Zurek's envariance — 3-point comparison after Table II
- [x] Cite flag manifold / Kähler geometry — Bengtsson-Życzkowski 2017, Brody-Hughston 2001 after Def. 1
- [x] Connect V(λ) to T_AB — action functional in Sec VI.B (done in Phase 1)

### Phase 3: Polish (DONE)
- [x] Define "reality R" — operational definition as equivalence class of frame descriptions
- [x] Cite Cepollaro et al. 2025 (PRL 135, 010201) — entanglement+coherence invariance under QRF
- [x] Full proofreading pass — notation consistency, cross-refs, "allowed" terminology tightened
- [x] Venue decision: arXiv → FoP strategy

### Paper 2 Prep
- [ ] Full tensor field T_AB development (building on TENSOR_FIELD_DEFINITION.md)
- [ ] Equations of motion for frame dynamics
- [ ] Holographic connections (coherence-space geometry ↔ emergent spacetime)

---

## Critical Path

```
Triple review ✅ → P0 fixes ✅ → Phase 2 strengthen → Phase 3 polish → arXiv submission
                                                                        |
                                                    Phase 2+3 expand → FoP submission
```

**Next milestone**: Endorsement → rebuild tarball → submit to arXiv.

---

## arXiv Submission

### Submission Package (DONE)
- [x] Created `~/Desktop/coherence-relativity-arxiv.tar.gz` (137KB)
- [x] Contents: `main.tex` (paths adjusted), `main.bbl`, 5 figure PDFs
- [x] Category: **quant-ph** (primary), cross-list hep-th or math-ph
- [x] License: **CC BY 4.0** (recommended)

### Endorsement (REQUIRED)
- [ ] arXiv requires endorsement for first-time quant-ph submitters
- [ ] Request endorsement from an established quant-ph author (3+ papers in category)
- **UNF contact**: Dr. Jason T. Haraldsen — Associate Editor of Physical Review B, quantum materials theory. Faculty page: UNF Physics Department. Best local candidate for endorsement.
- **Alternative**: Dr. Daniel Santavicca (UNF) — superconducting nanowire devices, less aligned but still quant-ph-adjacent
- **Process**: Contact endorser → they receive arXiv email → click endorsement link → submitter gets approved

### Post-Endorsement
- [x] Apply ChatGPT recommended edits (4/4 DONE)
- [x] Resolve figure metric computation — U-shaped metric embraced (2026-02-10)
- [x] Regenerate figs 1, 2, 6 from multi-mode FS metric (N=10)
- [x] Update captions and narrative for crossover interpretation
- [ ] Regenerate submission tarball with final edits
- [ ] Upload to arxiv.org, fill metadata (title, abstract, authors, category)
- [ ] Verify PDF renders correctly in arXiv preview
- [ ] Submit

---

## ChatGPT Evaluation (2026-02-10)

**Source**: `/Users/bryankaufman/Downloads/Paper Evaluation and Validation.pdf`

### Validation Results
- **References**: All 29 citations validated as legitimate, correctly applied
- **Equations**: All core math correct (Fubini-Study, Born rule, splitting map); later physics (action, quasipotential, δV, τ_frame) intentionally heuristic — acceptable for foundations paper
- **Overall**: "This is a real foundations paper, not a speculative essay"

### Recommended Edits (4 items)

#### Edit 1: Strengthen coherence frame definition
- [x] Replaced "not merely a basis" paragraph in Sec I.B with formal definition (equivalence class of bases + pointer observable + dynamical stability)
- **Priority**: High — DONE

#### Edit 2: Make frame splitting invariance sound inevitable
- [x] Added motivating paragraph before Theorem 2 explaining why splitting invariance is physically inevitable (refinement of alternatives argument)
- **Priority**: High — DONE

#### Edit 3: Soften prediction claims
- [x] Changed "six predictions distinguish" → "six experimentally testable signatures distinguish" in abstract, Sec VI.D, and conclusion
- **Priority**: Medium — DONE

#### Edit 4: Add novelty statement at end of Introduction
- [x] Added structural novelty paragraph at end of Sec I.B (before Organization): identifies Σ = U(d)/Tᵈ as geometric arena, Born measure as unique invariant
- **Priority**: Medium — DONE

### Figure Suggestions (LOW PRIORITY)
- matplotlib figures described as "conceptually excellent but visually look like quick matplotlib scripts"
- Consider professional-quality figures for journal submission (FoP stage)
- Not blocking for arXiv preprint

---

## Figure Metric Audit (RESOLVED — 2026-02-10)

**Full analysis**: `memory/kb/SESSION_2026-02-07_FIGURE_AUDIT.md`

### Resolution
The U-shaped FS metric is **correct, robust, and physically meaningful**. The "peaked in the middle" intuition was attached to the wrong geometric quantity.

**Model chosen**: Multi-mode N-qubit collective coupling (N=10)
**Parameterization**: Distinguishability λ ∈ [0,1]
**Presentation**: U-shape embraced as crossover manifold signature

### Key results
- G_λλ = 1/(2N·(1-λ)^{2(N-1)/N}·(1-(1-λ)^{2/N}))
- Minimum at λ ≈ 0.41 with G_min ≈ 1.29 (N=10)
- Geodesic integral ∫√G dλ ≈ 2.03 (N=10), π/(2√2) ≈ 1.11 (N=1)
- Quasipotential V(λ) = ∫_λ^1 √G dλ': S-shaped (steep-flat-steep)

### Physical interpretation
- **Near λ≈0**: metric diverges → coherence is geometrically fragile
- **Near λ≈1**: metric diverges → classical records are geometrically rigid
- **At minimum**: frames most similar → geometric definition of quantum-classical boundary
- The crossover plateau in V(λ) explains why systems rapidly depart coherence, linger in the crossover, and rapidly lock into classicality

### All items completed
- [x] **Choose model**: multi-mode N=10
- [x] **Update main.tex**: Sec II.C, Fig 1/2/6 captions, Sec VI.D quantitative estimates
- [x] **Regenerate data**: `data/g_lambda.csv`, `data/v_lambda.csv`, `data/s_lambda.csv` (NEW)
- [x] **Regenerate figures**: `python scripts/generate_figures.py 1 2 6`
- [x] **Rebuild paper**: 9 pages, zero errors

---

## FoP Submission (Future)
- [ ] Expand paper to 12-15 pages
- [ ] Professional figures
- [ ] Address all ChatGPT edits above
- [ ] Target: Foundations of Physics
