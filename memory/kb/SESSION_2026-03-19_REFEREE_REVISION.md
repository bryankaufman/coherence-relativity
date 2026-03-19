# Session: 2026-03-19 — Referee Revision (Paper 1) + GitHub Sync

## Status
**Paper 1 referee revision: COMPLETE and PUSHED to GitHub**
Commit: `1671048` on branch `main`
Repo: https://github.com/bryankaufman/coherence-relativity

---

## What Was Accomplished

### 1. EGY Reparameterization — Option A (Fix 7)

**Previous parameterization**: λ = 1 − ⟨W_L|W_R⟩ (linear overlap deficit)
**New EGY parameterization**: λ ≡ √(1 − |⟨W_L|W_R⟩|²) (distinguishability amplitude)

This is the standard quantum distinguishability measure used in quantum information theory.

#### Physics changes under EGY

| Quantity | Old (linear) | New (EGY) |
|---|---|---|
| r(λ) | (1−λ)^(1/N) | (1−λ²)^(1/(2N)) |
| G_λλ(λ=0) | diverges | **1/2 (finite, all N)** |
| G_λλ(λ=1) | finite | **diverges** |
| N=1 G analytic | 1/[2λ(2−λ)] | **1/[2(1−λ²)]** |
| N=10 curve shape | U-shaped (min at λ≈0.41) | **monotone increasing** |
| N=1 geodesic integral | π/(2√2) ≈ 1.107 | **π/(2√2) ≈ 1.107** (same) |
| N=10 geodesic (accessible) | ≈ 1.89 | **≈ 1.5** |
| Max Δ (CR vs QM) | 0.24 at λ≈0.52 | **0.124 at λ≈0.52** |

Key: G_λλ(0) = 1/2 is finite under EGY — the λ=0 endpoint is no longer singular.
The divergence now lives at λ→1 (maximal distinguishability / classical limit).

#### Files updated for EGY
- `code/calculate_g_lambda.py` — r formula, dr/dλ, N=1 analytic, docstring
- `code/calculate_v_lambda.py` — docstring only (integral formula unchanged)
- `code/generate_figures.py` — Fig 1 two-panel (G_λλ + dλ/ds), EGY xlabels, removed U-shape annotation
- `data/g_lambda.csv`, `data/v_lambda.csv`, `data/s_lambda.csv` — regenerated
- `figures/fig1.pdf` through `figures/fig7.pdf` — all regenerated

---

### 2. All 10 Referee Fixes Applied to `papers/01-coherence-frames/main.tex`

#### Referee 1 fixes

**Fix 1**: R as equivalence relation — replaced paragraph to make R an equivalence class
of frame descriptions (not a set of objects); pointer structure language added.

**Fix 2**: Ω_AB ≠ Berry curvature — added clarifying paragraph: Ω_AB is the imaginary
part of the QGT pulled back to Σ; Berry curvature lives on parameter space, not frame space.

**Fix 3**: Gleason NC vs (A1) — added paragraph distinguishing noncontextuality from
frame-invariance; added dim≥2 note for Gleason applicability.

**Fix 4**: Axiom (A3) renamed "Frame locality" with explanatory paragraph justifying
the name via operational locality of frame definitions.

**Fix 5+9**: Two paragraphs added before the prediction list — (i) geometric origin of
predictions: each follows from G_λλ curvature or frame-transformation group structure;
(ii) prediction provenance table: maps each prediction to its geometric source.

**Fix 6**: Unitarity-preservation paragraph after δV estimate — clarifies that frame
transformations are unitary by construction (they are elements of U(d)), so unitarity
is not a derived property but a definitional one.

#### Referee 2 (Grok) fixes

**Fix 7**: λ → EGY definition in main.tex (line ~129); N=1 G formula updated to
1/[2(1−λ²)]; N=10 geodesic integral updated to ≈1.5; endpoint claim corrected.

**Fix 8**: Endpoint claim corrected: G finite at λ→0, diverges at λ→1 (was reversed).
Fig 1 caption, Fig 2 caption, Fig 6 Δ 0.24→0.12 updated.

**Fix 10**: Added sentence after Prop 1 proof: Σ→Σ′ dimension statement (splitting
increases the dimension of the frame manifold from d to d·d_anc).

---

### 3. Referee Response Document

**New file**: `papers/01-coherence-frames/paper1_referee_response.tex` (and `.pdf`)
- 4-page structured response to Referee 1 and Referee 2
- Addresses all 10 points
- PDF compiled cleanly (zero errors)

---

### 4. Paper Statistics (Post-Revision)

| Item | Value |
|---|---|
| Pages | 12 |
| Figures | 7 (Fig 1 two-panel figure*) |
| LaTeX errors | 0 |
| Undefined references | 0 |
| Commit | 1671048 |

---

### 5. GitHub Sync

**Issue**: Remote had unrelated history (different root commit `24ed3fe` vs local `7810cfd`).
`git pull --rebase` triggered add/add conflicts on all code files.

**Resolution**: Aborted rebase; used `git push --force-with-lease origin main`.
Remote now matches local history with `1671048` as HEAD.

---

## Remaining Work (Carry-forward)

- [ ] Regenerate arXiv submission tarball with referee-revised main.tex
- [ ] arXiv endorsement — Dr. Jason Haraldsen (UNF, PRB Associate Editor)
- [ ] Consider Δ ≈ 0.124 (EGY computed) vs Fig 6 caption alignment
- [ ] Paper 2: T_AB dynamics, holographic connections, s(λ) figure, Kramers rate

---

## Key Quantitative Reference (EGY, N=1)

- G_λλ(λ) = 1/[2(1−λ²)]
- G(0) = 1/2, G→∞ as λ→1
- Geodesic integral: π/(2√2) ≈ 1.107
- Max Δ(CR vs QM): 0.124 at λ ≈ 0.52

---

*Session logged: 2026-03-19 09:32 UTC*
