#!/usr/bin/env bash
# Context refresh for Coherence Relativity Paper 1
# Run this at the start of a new Claude session to reload project state.
#
# Usage:
#   source .venv/bin/activate
#   bash scripts/context-refresh.sh
#
# Or paste individual commands into a Claude session prompt.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "============================================================"
echo "COHERENCE RELATIVITY — Context Refresh"
echo "============================================================"
echo ""
echo "Project root: $ROOT"
echo "Date: $(date +%Y-%m-%d)"
echo ""

# ── 1. Paper status ──
echo "── Paper Build Status ──"
if [ -f papers/01-coherence-frames/main.pdf ]; then
    MODIFIED=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" papers/01-coherence-frames/main.pdf 2>/dev/null || echo "unknown")
    echo "  main.pdf: last built ${MODIFIED}"
    echo "  (10 pages as of 2026-02-12 session)"
else
    echo "  main.pdf: NOT FOUND — needs rebuild"
fi

# ── 2. Key files ──
echo ""
echo "── Key Files ──"
echo "  Paper:      papers/01-coherence-frames/main.tex"
echo "  Figures:    scripts/generate_figures.py (figs 1-7)"
echo "  Fig 1 dual: scripts/gen_fig1_dual.py (two-panel G + dλ/ds)"
echo "  Tasks:      TASKS.md"
echo "  Sessions:   memory/kb/SESSION_2026-02-07_FIGURE_AUDIT.md"
echo "              memory/kb/SESSION_2026-02-12_ESTIMATE_AUDIT.md"

# ── 3. Build environment ──
echo ""
echo "── Build Environment ──"
echo "  Python venv: .venv/ (uv, numpy/scipy/matplotlib/sympy/pymupdf)"
echo "  LaTeX: /Library/TeX/texbin/pdflatex (TeX Live 2025, NOT on PATH)"
echo "  Bib: scripts/refresh-bib.sh (Zotero BBT export)"
echo ""
echo "  Build command:"
echo "    cd papers/01-coherence-frames && /Library/TeX/texbin/pdflatex -interaction=nonstopmode main.tex"
echo ""
echo "  Figure generation:"
echo "    source .venv/bin/activate && python scripts/gen_fig1_dual.py  # Fig 1 (two-panel)"
echo "    source .venv/bin/activate && python scripts/generate_figures.py 2  # Fig 2"
echo "    source .venv/bin/activate && python scripts/generate_figures.py 6  # Fig 6"

# ── 4. Multi-mode FS metric (core computation) ──
echo ""
echo "── Multi-mode FS Metric ──"
echo "  Model: N collectively-coupled environment qubits"
echo "  G_λλ = 1/(2N · (1-λ)^{2(N-1)/N} · (1-(1-λ)^{2/N}))"
echo "  λ ≡ 1 - |⟨W_L|W_R⟩| (info-theoretic distinguishability)"
echo ""
echo "  Key values (N=10):"
echo "    G_min ≈ 1.29 at λ ≈ 0.41"
echo "    dλ/ds peak ≈ 0.88 at λ ≈ 0.41"
echo "    s* ≈ 0.72 (geometric activation distance)"
echo "    ∫√G dλ ≈ 2.0 (over [0.01, 0.99]), 3.51 (formal [0,1])"
echo "    R_Σ = 8 (Ricci scalar of CP¹ under FS metric)"
echo "    δV ≈ 2×10⁻³ (hysteresis visibility deficit)"
echo ""
echo "  Key values (N=1):"
echo "    G = 1/(2λ(2-λ)), monotone decreasing"
echo "    ∫√G dλ = π/(2√2) ≈ 1.11 (analytic)"
echo "    τ_frame ≥ 1.1 μs"

# ── 5. Current status ──
echo ""
echo "── Current Status ──"
echo "  Paper 1: 10 pages, zero errors, all estimates verified"
echo "  Figure metric audit: RESOLVED (U-shape embraced)"
echo "  ChatGPT edits: 4/4 applied"
echo "  Estimate audit: 3 corrections applied (R_Σ, cutoff, s*)"
echo ""
echo "── Remaining ──"
echo "  [ ] Regenerate arXiv tarball"
echo "  [ ] arXiv endorsement (Dr. Haraldsen, UNF)"
echo "  [ ] Upload + verify on arXiv"
echo "  [ ] Paper 2: T_AB dynamics, Kramers rate, thermo table"
echo ""
echo "── Files to read for full context ──"
echo "  cat TASKS.md"
echo "  cat memory/kb/SESSION_2026-02-12_ESTIMATE_AUDIT.md"
echo "  cat memory/kb/SESSION_2026-02-07_FIGURE_AUDIT.md"
echo "============================================================"
