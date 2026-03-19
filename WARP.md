# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Development Standards

### Bypass Tracking System (MANDATORY)

**⚠️ CRITICAL: All development MUST follow bypass tracking workflow**

When you take shortcuts or create workarounds:
1. **Immediately** add inline TODO comment: `TODO-[CATEGORY]-[NUMBER]`
2. **End of day**: Run `python tools/extract_todos.py` to generate `ACTIVE_TODOS.md`
3. **End of day**: Update phase-specific bypass document

```bash
# Check current TODOs
python tools/extract_todos.py
cat ACTIVE_TODOS.md

# Sync to GitHub (if configured)
python tools/sync_todos_to_github.py
```

**Documentation:**
- [System Overview](BYPASS_TRACKING_SYSTEM_README.md) - Start here
- [Full Workflow](DEVELOPMENT_WORKFLOW_TEMPLATE.md) - Complete spec
- [Quick Reference](BYPASS_TRACKING_QUICK_REFERENCE.md) - Templates
- [GitHub Integration](GITHUB_INTEGRATION_GUIDE.md) - GitHub setup

**15 TODO Categories:**
LOI (LOINC), PLAY (Playbook), VOCAB (Vocabulary), CDE (CARDS), TID (Templates),
EVID (Evidence), VAL (Validation), ORT (Orthanc), DCM (DCM4CHEE), FHIR,
SEC (Security), DOC (Documentation), TEST, PERF (Performance), API

**Priority Levels:**
- 🔴 HIGH: Blocks production, security/PHI risk (fix within sprint)
- 🟡 MEDIUM: Single feature affected, stable workaround (fix within 2 sprints)
- 🟢 LOW: Nice-to-have, optimization (backlog)

**Rule:** "If you bypass it, document it IMMEDIATELY"

---

## Project-Specific Notes

### Project: Coherence Relativity

**Paper 1** (`papers/01-coherence-frames/`)
- Status: Referee revision complete (2026-03-19), pushed to GitHub (commit `1671048`)
- Parameterization: **EGY** — λ ≡ √(1 − |⟨W_L|W_R⟩|²)
- N=1 metric: G_λλ = 1/[2(1−λ²)]; G(0)=1/2 finite, G→∞ at λ→1
- Pending: arXiv endorsement (Dr. Jason Haraldsen, UNF), submission tarball regeneration

**Paper 2** (`papers/02-tensor-dynamics/` — not yet started)
- Focus: Full T_AB tensor field dynamics, equations of motion
- Deferred items: s(λ) figure, thermodynamic table, Kramers rate, holographic connections

### Key Files
- `code/calculate_g_lambda.py` — EGY metric computation (N-mode, analytic N=1)
- `code/generate_figures.py` — All 7 figures (run from repo root with venv)
- `papers/01-coherence-frames/main.tex` — Main manuscript (RevTeX4-2)
- `bibliography/master.bib` — Master BibTeX (refresh via `scripts/refresh-bib.sh`)
- `memory/kb/` — Per-session knowledge base logs

### Build Commands
```bash
# Activate Python environment
source .venv/bin/activate

# Regenerate data
python3 code/calculate_g_lambda.py
python3 code/calculate_v_lambda.py

# Regenerate figures
python3 code/generate_figures.py

# Build PDF (from papers/01-coherence-frames/)
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/bibtex main
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/pdflatex main.tex
```

### Relevant TODO Categories for This Project
DOC (Documentation), TEST (numerical validation), PERF (figure generation),
API (arXiv/OSF submission interfaces)

### Session Logs
- `memory/kb/SESSION_2026-02-07_FIGURE_AUDIT.md` — U-shape metric, ChatGPT edits
- `memory/kb/SESSION_2026-02-12_ESTIMATE_AUDIT.md` — R_Σ=8, s*=0.72, geodesic cutoff
- `memory/kb/SESSION_2026-02-14_PUBLICATION.md` — OSF publication milestone
- `memory/kb/SESSION_2026-03-19_REFEREE_REVISION.md` — EGY reparameterization, 10 fixes
