# SYSTEM-RULES.md

Operating rules for AI agents (Claude Cowork, Claude Code, Warp) in this workspace.

## Core Principles

1. **One canonical repo.** Only `~/Library/CloudStorage/Dropbox/Mac/Documents/coherence-relativity/`
   is authoritative. Desktop copies are scratch space. See `VERSION_CONTROL_PROTOCOL.md`.
2. **Bypass-track all shortcuts.** If you take a shortcut or defer something, add an inline
   `TODO-[CATEGORY]-[NUMBER]` comment immediately. Categories in `WARP.md`.
3. **Verify before asserting.** SymPy check > analytic derivation > numerical run > intuition.
   Never state a physics result as proven without a traceable verification step.
4. **Notation is law.** All symbols must match `notes/EQUATIONS_REFERENCE.md`. If you need
   a new symbol, propose it explicitly — do not introduce it silently.

## When to Ask Before Acting

- The task involves changing notation, parameterization, or sign conventions
- The task restructures paper sections or moves content between papers
- The task touches Paper 1 (content-complete; modifications require explicit approval)
- The goal is ambiguous — you are unsure what the deliverable should be
- There are multiple viable approaches and the choice has downstream consequences

## Execution Behavior

### Before editing any paper file
```bash
git --no-pager log --oneline -5
git --no-pager status
```
Confirm HEAD matches expectations and working tree is clean.

### After completing a task
- Commit with descriptive message and co-author line
- Report: commit hash, files changed, page count (if LaTeX), pass/fail on build
- Post to conv-log if doing multi-agent handoff

### File conventions
- New paper sections → `papers/0X-*/sections/drafts/paper2_section_N.N_TOPIC_DRAFT.md`
- Session logs → `memory/kb/SESSION_YYYY-MM-DD_TOPIC.md`
- Bibliography entries → `bibliography/master.bib` (one file for all papers)
- Figures → `figures/` at repo root (PDF + PNG, 300 DPI)

## Handling Ambiguity

- If a physics claim is uncertain, flag it: *"Conjecture (unverified):"* or add a
  `TODO-DOC` inline comment.
- If two sources disagree, defer to the Source Hierarchy in `context/HOW-I-WORK.md`.
- If a numerical computation gives unexpected results, report the raw numbers and
  the expected range — do not silently adjust.

## What Makes Output Strong

- Compiles / runs without errors
- Notation-consistent with EQUATIONS_REFERENCE.md
- Contains explicit equations, not just prose descriptions
- Distinguishes proven results from conjectures
- Includes quantitative estimates where possible (with units and parameter values)

## What Makes Output Weak

- Generic summaries with no new content
- Prose claims without supporting equations
- Silently changed notation or sign conventions
- "It should work" without a verification step
- Invented citations or parameter values

## Hard Boundaries

- **Never invent citations.** If you need a reference and don't have one, write `[CITE NEEDED]`.
- **Never silently change parameterization.** EGY is locked for Paper 1.
- **Never edit Desktop scratch copies as authoritative.** Always work in the canonical repo.
- **Never commit without a co-author line.**
- **Never assume test framework or build system.** Check README or existing scripts first.

## Pre-Delivery Checklist

Before declaring a task complete:

1. `git diff` — review all changes
2. LaTeX build clean (if paper files touched)
3. Python scripts run without errors (if code touched)
4. Notation spot-check against EQUATIONS_REFERENCE.md
5. New bib entries added to `bibliography/master.bib` (not a local .bib)
6. Page count and figure count reported
