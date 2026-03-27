# HOW-I-WORK.md

This file tells AI agents who I am inside this workspace, how I think, and what I value.

## What I Do

I am a physicist developing the **Coherence Relativity** framework — a geometric
reinterpretation of quantum mechanics where coherence frames play the role that
inertial frames play in special relativity. The project spans multiple papers:

- **Paper 1** (published): Coherence frames, Born rule as frame invariant, EGY parameterization
- **Paper 2** (in progress): Full T_AB tensor field dynamics, saturation conditions, 5D cosmology
- **Papers 3–4** (planned): GR unification, holographic connections

## Who I Create For

- **Primary audience**: Referees and readers of Foundations of Physics, Physical Review A, arXiv quant-ph
- **Secondary**: Collaborators and AI agents working on the same codebase
- **What they value**: Mathematical precision, explicit derivations, falsifiable predictions,
  clear distinction between proven results and conjectures

## How I Think

- **Derivation-first**: I trust results that come from explicit calculation, not analogies.
  SymPy verification > analytic derivation > numerical result > heuristic argument.
- **Notation-sensitive**: Consistency matters. If Paper 1 uses λ for distinguishability, Paper 2
  must use the same symbol with the same definition. Check `notes/EQUATIONS_REFERENCE.md`.
- **Geometric intuition**: I reason about physics problems through manifold structure, fiber
  bundles, and information geometry. Translate abstract claims into geometric language when possible.
- **Skeptical of hand-waving**: If a claim cannot be stated as a theorem, proposition, or
  quantitative estimate, flag it rather than asserting it.

## How I Communicate

- **Concise and technical**. Skip preamble. Get to the equation or the decision.
- **I use LaTeX notation in prose** (e.g., "G_λλ diverges at λ→1") — agents should do the same.
- **I dislike**: generic summaries that restate what I already said, filler paragraphs,
  over-explaining context I provided, softening language that weakens claims.
- **I value**: precise diffs ("changed Eq. 14 from X to Y"), commit hashes, page counts,
  clear pass/fail on validation checks.

## Source Hierarchy (when sources conflict)

1. Published Paper 1 (`papers/01-coherence-frames/main.tex`) — highest authority
2. `notes/EQUATIONS_REFERENCE.md` — canonical definitions and labels
3. Session logs in `memory/kb/` — record of decisions and their rationale
4. `WARP.md` / `VERSION_CONTROL_PROTOCOL.md` — operational rules
5. Paper 2 draft sections — working material, may contain inconsistencies

## Decision-Making Style

- I commit only when something is verified. "It looks right" is not sufficient.
- I prefer to defer a decision explicitly (with a bypass-tracked TODO) rather than
  guess and risk propagating an error.
- When I say "proceed," I mean execute without further confirmation.
- When I say "let me think," I mean stop and wait.

## What Good Output Looks Like

- LaTeX compiles with zero errors and zero undefined references
- Bianchi identity residuals < 10⁻¹⁵
- New sections use notation consistent with EQUATIONS_REFERENCE.md
- Figures are publication-quality (300 DPI, serif fonts, proper axis labels)
- Every numerical claim has a traceable computation in `code/` or `analysis/`
