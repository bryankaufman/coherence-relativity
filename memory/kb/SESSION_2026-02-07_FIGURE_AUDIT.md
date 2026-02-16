# Session: 2026-02-07 — Figure Audit & ChatGPT Edits

## What was accomplished

### 1. ChatGPT's 4 recommended edits — ALL APPLIED
- **Edit 1** (Sec I.B): Strengthened coherence frame definition — formal axiomatization (equivalence class + pointer observable + dynamical stability). Replaced the "not merely a basis" paragraph.
- **Edit 2** (Sec IV.A): Added splitting-invariance motivation paragraph before Theorem 2 — explains why invariance under refinement of alternatives is physically inevitable.
- **Edit 3** (Abstract, Sec VI.D, Conclusion): Softened "six predictions distinguish" → "six experimentally testable signatures distinguish".
- **Edit 4** (Sec I.B): Added novelty statement before Organization subsection — identifies Σ = U(d)/T^d as geometric arena, Born measure as unique invariant.
- Paper compiles cleanly: 9 pages, zero errors.

### 2. Figure generation script created
- **File**: `scripts/generate_figures.py`
- Generates all 7 figures from data + matplotlib
- Usage: `source .venv/bin/activate && python scripts/generate_figures.py [1-7]`
- Figures used in paper: 1, 2, 4, 5, 6 (fig3 and fig7 are extras not in main.tex)
- Figure 6 in the paper is TikZ inline (CR vs QRF comparison), not an external file

### 3. TASKS.md updated
- Added arXiv submission section (package done, endorsement needed)
- Added UNF contact: Dr. Jason Haraldsen (PRB Assoc. Editor, best endorsement candidate)
- Added ChatGPT evaluation results and all 4 edits (now marked DONE)
- Added FoP submission future section

### 4. CRITICAL: Figure metric audit (ChatGPT + Claude joint analysis)

#### The problem
Figs 1, 2, 6 show G_λλ(λ) as a peaked bump (0.5 → 0.686 → 0.5). This was **illustrative data**, not computed from the Fubini-Study metric Eq. (3). A referee will catch this.

#### Models tested — NONE produce a peaked curve

| Model | Formula | Shape |
|-------|---------|-------|
| 6D orthogonal interpolation | 1/(4λ(1-λ)) | U-shaped, diverges both ends |
| 4D Hamiltonian (constant coupling) | π²/16 ≈ 0.617 | Flat (constant) — geodesic |
| ChatGPT asymmetric decoherence | 1/(2λ(2-λ)) | Monotone decreasing, diverges λ→0 |
| Multi-mode collective (N modes) | 1/(2N·(1-λ)^{2(N-1)/N}·(1-(1-λ)^{2/N})) | U-shaped, min at λ≈0.4 |

#### ChatGPT's corrected state (used for asymmetric model)
```
|ψ(λ)⟩ = (1/√2)(|L⟩⊗|W_L⟩ + |R⟩⊗|W_R(λ)⟩)
|W_L⟩ = |0⟩
|W_R(λ)⟩ = (1-λ)|0⟩ + √(1-(1-λ)²)|1⟩
⟨W_L|W_R(λ)⟩ = 1-λ
```
This is normalized but gives G = 1/(2λ(2-λ)), monotone decreasing.

#### ChatGPT's FIRST attempt had bugs (documented for reference)
- Non-orthogonal coherent+entangled parts in 4D → state unnormalized for λ∈(0,1)
- Wrong component assignment: |R,W_L⟩ was zeroed, |R,W_R⟩ got wrong value

#### Core geometric fact
For ANY model where λ = distinguishability, the FS metric diverges at λ→0 because infinitesimal changes in distinguishability require finite Hilbert space rotations near full coherence. This is a coordinate singularity (like latitude at the poles). The metric in the natural arc-length parameter is smooth and constant.

#### Multi-mode analytic result (N collectively-coupled environment qubits)
```
G_λλ = 1/(2N · (1-λ)^{2(N-1)/N} · (1-(1-λ)^{2/N}))
```
- Diverges at both endpoints for N≥2
- Minimum at λ ≈ 1 - ((N-1)/N)^{N/2} ≈ 0.40 for large N
- For N=1: diverges only at λ→0, monotone decreasing to 0.5
- For N→∞: min at λ ≈ 1-e^{-1/2} ≈ 0.394

## RESOLVED (2026-02-10): Embraced U-shape — Option A

### ChatGPT's response (key insight)
> "The U-shaped FS metric is correct, robust, and physically meaningful.
> The 'peaked in the middle' intuition was attached to the wrong geometric quantity."

The metric minimum at intermediate λ provides a **precise geometric definition of the quantum-classical boundary** — the region where neighboring frames are most similar (maximal geometric robustness).

### Implementation
- **Model**: Multi-mode N=10 collectively-coupled environment
- **Key values**: G_min ≈ 1.29 at λ ≈ 0.41, geodesic integral ≈ 2.03
- **Fig 1**: Two-panel dual view (figure*): (a) U-shaped G_λλ, (b) peaked dλ/ds = 1/√G
- **Fig 2**: S-shaped quasipotential V(λ) = ∫_λ^1 √G dλ' with crossover plateau
- **Fig 6**: CR geometric transition vs standard QM visibility (max deviation Δ ≈ 0.24)
- **main.tex**: Sec II.C text rewritten (crossover narrative + info-theoretic λ def), all 3 captions updated, quantitative estimates updated (τ ≥ 1.1 μs for N=1, ∫√G ≈ 2.0 for N=10), geometric activation distance s* ≈ 0.65 + latent-heat analogy in Sec VI.B
- **Data files**: g_lambda.csv, v_lambda.csv, s_lambda.csv (NEW) all regenerated
- **Paper**: 10 pages, zero errors, clean compile

## Files modified this session
- `papers/01-coherence-frames/main.tex` — 4 ChatGPT edits, crossover rewrite, two-panel fig, λ definition, activation distance
- `scripts/generate_figures.py` — NEW, generates all 7 figures
- `scripts/gen_fig1_dual.py` — NEW, two-panel Fig 1 (G_λλ + dλ/ds)
- `scripts/gen_fig1b.py` — NEW, standalone dλ/ds plot
- `TASKS.md` — updated with arXiv/endorsement/ChatGPT eval sections

## Diagnostic plots created
- `/tmp/multimode_metric.png` — G_λλ for N=1,2,5,10,20,50 (U-shaped curves)
- `/tmp/cr_page_1.png` through `/tmp/cr_page_10.png` — rendered PDF pages

## Key data files
- `data/g_lambda.csv` — REGENERATED from multi-mode N=10
- `data/v_lambda.csv` — REGENERATED from multi-mode N=10
- `data/s_lambda.csv` — NEW (accumulated FS length + dλ/ds)
