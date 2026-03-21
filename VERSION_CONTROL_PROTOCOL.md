# Version Control Protocol — Coherence Relativity Papers

**Established**: 2026-03-21 — after version crisis resolved by Warp + Claude + Bryan  
**Applies to**: All agents (Warp, Claude, Claude Code, Perplexity, OODA, Comet, any future agent)  
**Applies to**: All papers in this repo (Paper 1, Paper 2, Paper 3, Paper 4, ...)

---

## THE RULE: ONE CANONICAL REPO

**The canonical source of truth is the git repository at:**
```
~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/
```

**GitHub remote**: `https://github.com/bryankaufman/coherence-relativity.git`

**No other copy of any paper file is authoritative.** This includes:
- `~/Desktop/coherence-relativity-v3/` — scratch space only, not authoritative
- `~/Desktop/coherence-relativity-revised/` — scratch space only, not authoritative
- `~/Desktop/coherence-relativity/` — scratch space only, not authoritative
- Any agent container path (`/home/claude/`, `/mnt/user-data/`, etc.) — not writable to canonical repo directly

---

## WHAT WENT WRONG (2026-03-19 to 2026-03-21)

Multiple agents applied independent changes to parallel, untracked copies of `main.tex`
simultaneously. Neither the Desktop v3 nor the Desktop revised copy was under git. Agents
compiled different versions, overwrote each other's work, and nobody maintained a single
authoritative state. This cost ~6 hours of recovery work.

**Root cause**: Agents assumed their local working copy was current without checking git.

---

## RULES FOR ALL AGENTS

### 1. Before editing any paper file
```bash
cd ~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/
git --no-pager log --oneline -5   # Know the current HEAD
git --no-pager status              # Confirm working tree is clean
git pull origin main               # Sync with remote if needed
```

### 2. All edits go to the canonical repo
- Edit files **only** inside `~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/`
- Never apply paper edits to Desktop copies and expect them to count
- If you wrote content in a container or scratch space, write it to the canonical repo via the Filesystem MCP tool or post it to conv-log for Warp to apply

### 3. Commit and push after every substantive change
```bash
git add <changed files>
git commit -m "<description>

Co-Authored-By: <AgentName> <agent@domain>"
git push origin main
```
- Always include a co-author line
- Always push — a local-only commit is invisible to other agents

### 4. Post to conv-log after pushing
After every push, post to conv-log with:
- Commit hash
- What changed (files + brief description)
- New compilation status (page count, errors)

### 5. Never commit to a non-canonical copy
If you find yourself in `~/Desktop/coherence-relativity-v3/` or similar:
- **Stop**
- Copy the relevant file changes to the canonical repo
- Commit there instead

### 6. Desktop directories are scratch space
Files in `~/Desktop/coherence-relativity-*/` may be used for:
- Staging figures before they are ready
- Claude container output (pending-repo-additions/)
- Exploration/drafting

They are **never** the target of a final commit. When ready, move to canonical repo.

---

## FILE STRUCTURE (canonical repo)

```
coherence-relativity/
├── papers/
│   ├── 01-coherence-frames/       ← Paper 1 (main.tex, main.pdf, etc.)
│   ├── 02-saturation-dynamics/    ← Paper 2
│   ├── 03-gr-unification/         ← Paper 3
│   └── 04-holography/             ← Paper 4
├── figures/                       ← All shared figures (PDF)
├── bibliography/
│   └── master.bib                 ← Single master bibliography for all papers
├── code/                          ← Numerical scripts
├── data/                          ← Generated CSVs
└── VERSION_CONTROL_PROTOCOL.md   ← This file
```

### Figure management
- All figures live in `figures/` at repo root
- Papers reference them via `\graphicspath{{../../figures/}}`
- When a figure is ready, copy it to `figures/` and commit — not to a Desktop dir
- Replacement figures must be drop-in (same filename) or require a main.tex edit

### Bibliography management
- All citations use `bibliography/master.bib` — one file for all papers
- New entries are added directly to `master.bib` and committed
- Never use per-paper `.bib` files as the source of truth

---

## MULTI-AGENT COORDINATION RULES

### Before starting work on a paper
1. Check conv-log for any pending tasks from other agents
2. Check git log — if HEAD differs from what you expect, read the diff before touching files
3. Post to conv-log that you are starting work on a specific file

### When another agent has pending changes
- If an agent has posted changes to conv-log but they are not yet in git: apply them to the canonical repo first, then build on top
- Do NOT apply your own changes on top of an uncommitted base

### Handoff between agents
When completing a task that another agent will build on:
1. Push to git
2. Post commit hash + page count + "ready for next step" to conv-log
3. The receiving agent reads the git state, not a Desktop copy

### Conflict resolution
If two agents have made changes to the same file in different locations:
1. Git repo wins — it is always authoritative
2. Non-git changes must be diffed against git HEAD and applied as a patch
3. Warp (oz) is responsible for resolving conflicts and committing the merged result

---

## PAPER STATUS (as of 2026-03-21)

### Paper 1 (`papers/01-coherence-frames/`)
- **HEAD**: `ba4e6c9` — "Add fig_geometric_entropy + Remark §6.2 + corrected fig5_double_slit_frames"
- **Build**: 14 pages, 925KB, clean (no errors, no undefined citations)
- **Applied fixes**: 15 content fixes + EGY reparameterization + citation audit (Fixes 1–15)
- **Additional**: Remark on frame-dependence of thermodynamic quantities (§6.2), PtaszynskiEsposito2023
- **Pending evaluation** (not yet in repo):
  - `fig_born_invariant_parallel.pdf` — SR/Bloch parallel diagram (in v3/figures/)
  - `fig4_quasipotential_well.pdf` — replacement quasipotential figure (in v3/figures/)
- **Submission gate**: arXiv endorsement from Dr. Jason Haraldsen (UNF)

### Paper 2 (`papers/02-saturation-dynamics/`)
- Draft sections in `papers/02-saturation-dynamics/sections/drafts/`
- Not yet a compiled LaTeX document

---

## BUILD COMMANDS (Paper 1)

```bash
cd ~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/papers/01-coherence-frames/
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/bibtex main
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/pdflatex main.tex
```

Expected output: 14 pages, ~925KB, no errors.

---

*This protocol was established after a version crisis on 2026-03-19 to 2026-03-21.*  
*Update this file whenever the canonical repo structure changes significantly.*
