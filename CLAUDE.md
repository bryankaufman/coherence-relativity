# CLAUDE.md

This file provides guidance to Claude (Cowork / Claude Code) when working in this repository.

## Start Here

Read these files in order before executing any task:

1. `context/HOW-I-WORK.md` — who I am, how I think, what I value in outputs
2. `system/SYSTEM-RULES.md` — operating rules for this workspace
3. `VERSION_CONTROL_PROTOCOL.md` — canonical repo rules (MANDATORY)
4. `WARP.md` — bypass tracking categories and build commands

Then read the relevant project folder:
- `papers/01-coherence-frames/` — Paper 1 (content-complete, do not modify unless explicitly asked)
- `papers/02-saturation-dynamics/` — Paper 2 (active draft, ~75% complete)
- `analysis/` — numerical computations (Casimir spectral, T3A dynamics)

## Do Not

- Execute immediately if the goal, audience, or output format is unclear — ask first.
- Invent facts, citations, parameter values, or physical claims.
- Edit Paper 1 files without explicit instruction (it is content-complete).
- Edit Desktop scratch copies — only the canonical repo is authoritative.

## Save Outputs

- Figures → `figures/`
- Data → `data/`
- Session logs → `memory/kb/SESSION_YYYY-MM-DD_TOPIC.md`
- Paper sections → `papers/0X-*/sections/drafts/`

## Build Commands

```bash
# Python environment
source .venv/bin/activate

# Regenerate data
python3 code/calculate_g_lambda.py
python3 code/calculate_v_lambda.py

# Regenerate figures
python3 code/generate_figures.py

# Build Paper 1 PDF (from papers/01-coherence-frames/)
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/bibtex main
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/pdflatex main.tex
```

## Key References

- `notes/EQUATIONS_REFERENCE.md` — all definitions, axioms, equations with LaTeX labels
- `bibliography/master.bib` — single master bibliography for all papers
- `memory/kb/` — per-session knowledge base (figure audits, referee revisions, etc.)
- `COORDINATION.md` — Society of Mind agent log
- `TASKS.md` — project-wide task tracker

## Parameterization

Paper 1 uses **EGY**: λ ≡ √(1 − |⟨W_L|W_R⟩|²)
- N=1 metric: G_λλ = 1/[2(1−λ²)]
- G(0) = 1/2 (finite), G→∞ at λ→1
- Geodesic integral: π/(2√2) ≈ 1.107

Paper 2 extends this with the full T_AB tensor field dynamics on M × Σ.

---

## HCR Vault (added 2026-04-28)

The project is now named **HCR (Holographic Coherence Relativity)**. The canonical Obsidian vault is rooted at this repo.

**Orientation for new sessions:**
1. Read `_vault/AGENT_GUIDE.md` — authoritative path registry, write rules, paper status
2. Read `memory/kb/INDEX.md` — session log index (newest first)
3. Check `TASKS.md` for active tasks

**Do NOT write to `_vault/*.md` MOC files** — those are human-curated navigation.

**Session log convention:** `memory/kb/SESSION_YYYY-MM-DD_TOPIC.md` + append to `memory/kb/INDEX.md`
