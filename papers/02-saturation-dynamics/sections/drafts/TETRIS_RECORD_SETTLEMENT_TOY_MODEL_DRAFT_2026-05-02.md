# §X (DRAFT PLACEHOLDER) — A Toy Model of Record Settlement: The Tetris Analogy

**Status:** Draft placeholder, 2026-05-02. For inclusion in Paper 2A §7 (Equations of Motion and Record Constitution) or as a dedicated illustrative section. Caveats on deviations from the full HCR framework are noted inline.

---

## Motivation

The abstract machinery of T_AB, λ-trajectories, and quasipotential wells can be grounded in a concrete discrete model that makes the key concepts — sequential record settlement, irreversibility, the distinction between frame-local and observer-independent facts, and Born-rule sampling — immediately visible. We use the game of Tetris as this model, not as a rigorous derivation but as a scaffolding that captures the essential topology of the record-settlement process. Deviations from full HCR are noted; they do not undermine the structural correspondences.

---

## The Correspondence Table

| Tetris element | HCR object | Paper 1 reference |
|---|---|---|
| Falling piece (in flight) | Quantum alternatives open; λ ≈ 0 to 0 < λ < 1 | §2.3, EGY parameterization |
| Piece height (normalized 0 = spawn, 1 = floor) | λ, the decoherence parameter | Eq. (2.1) |
| Gravity | Drift field F^A, quasipotential V(λ) | §6.3 |
| Piece **locking** onto the stack | Record settlement, λ → 1, G_λλ → ∞ | §2.4 |
| Locked cells (the stack) | 𝒟_F — the definite record set of frame F | §3.3 |
| **Incomplete rows** | Frame-local facts (not yet observer-independent) | Prop. 3.3 |
| **Complete rows** | Observer-independent facts: H_γ(r) = r | Prop. 3.3 |
| Line-clear recorded in score | Causal record persisting after visible erasure | §6.2 |
| Random piece draw (I, L, T, S, Z, O, J) | Born-rule sampling over alternatives | Thm. 2 (Paper 1) |
| Board width W | Accessible Hilbert-space dimension d | §2.1 |
| Stack height reaching ceiling | Measurement-induced phase transition / fact-horizon saturation | §6.5 |

---

## Formal Structure

**State space.** Let the board be a W × H binary grid B ∈ {0,1}^{W×H}. The *active piece* at time t is a quantum register |ψ⟩ ∈ ℂ^W encoding a superposition over horizontal positions x ∈ {1,...,W}, with Born amplitudes |c_x|² giving the probability of locking at column x. The normalized height above the floor defines the decoherence parameter:

$$\lambda(t) = 1 - \frac{h(t)}{H}$$

where h(t) is the piece's height at time t. At spawn (h = H): λ = 0. At locking (h = 0): λ = 1.

**The metric.** The information-geometric cost of a lateral displacement δx at height λ is:

$$G_{\lambda\lambda}(\lambda) = \frac{1}{2(1-\lambda^2)}$$

(the N=1 HCR metric, Paper 1 §2.3). As λ → 1 (approaching the floor), G_λλ → ∞: the piece's horizontal position becomes metrically rigid, unable to change without infinite cost. **This is the G_λλ divergence made discrete and visual.**

**The quasipotential.** Gravity acts as the drift field F^λ = const > 0, driving the piece downward (toward λ = 1). The geometric quasipotential

$$V(\lambda) = s(1) - s(\lambda) = \int_\lambda^1 \sqrt{G_{\lambda\lambda}(\lambda')}\,d\lambda'$$

measures the remaining geodesic distance to the floor. V(λ) → 0 as the piece approaches locking: the piece is "falling into the potential well" of the classical configuration.

**Record constitution.** A locked cell at position (x, y) is an element of 𝒟_F. A *complete row* y with all W cells filled satisfies the observer-independent fact criterion (Proposition 3.3 of Paper 1): no future piece can alter the existence of that row's contribution to the score. It is globally portable across all frames. An *incomplete row* is frame-local: a future piece can complete or fail to complete it, changing its status. The line-clear event records the fact immutably in the score — the board resets but the causal record persists, exactly as an HCR-past event is geometrically rigid even after the "present moment" moves on.

**Born-rule sampling.** The piece-type draw is a discrete Born-rule event: the probability of each piece type (I, L, T, S, Z, O, J) is determined before observation, but the specific draw is definite only when instantiated. This maps onto the distinction between latent Born weights (which exist throughout all λ-zones, including the future) and instantiated facts (which exist only after locking). The future is pre-record, not pre-Born.

---

## What the Model Captures

**1. Sequential irreversibility.** Each piece locks in sequence; the past stack does not change. This is the discrete analogue of the G_λλ → ∞ rigidity preventing reversal once λ → 1.

**2. The three temporal zones.** The spawning zone (top of board) is the HCR-future: all positions open, no stable record. The falling zone is the HCR-present: the piece is in flight, position still undetermined, records forming. The locked stack is the HCR-past: stable, definite, globally portable.

**3. Observer-independent vs. frame-local facts.** Complete rows = observer-independent (H_γ(r) = r); incomplete rows = frame-local (H_γ(r) ≠ r for some future-piece loop γ). The distinction between the two is not metaphysical but structural: it depends on whether any future coherence can alter the record's status.

**4. The Wigner's-Friend structure.** An observer who sees only the score (not the board state) operates in a coarser coherence space. They cannot distinguish board configurations that yield the same score sequence. This is precisely the Σ_F ⊂ Σ_W submanifold structure of the Hilbert-space depth remark (Paper 1, Remark rem:hilbert-depth): a higher-dimensional observer can treat what the score-observer calls "settled past" as still quantum-open at the board-configuration level.

**5. Quantum Darwinism.** Multiple simultaneous observers see identical locked configurations (the stack). The record is redundantly encoded: adding more "environment fragments" (observers) narrows the quasipotential well around the classical configuration, consistent with the N-fragment narrowing of V(λ) shown in Paper 1 Fig. 4.

---

## Caveats and Deviations from Full HCR

1. **Classical during fall.** In standard Tetris, a falling piece has a definite position at every moment; there is no genuine quantum superposition. In the HCR-extended version, the piece is modelled as a superposition |ψ⟩ = Σ_x c_x |x⟩ that collapses upon collision with the stack. This is an idealization; the physical analogue is an open quantum system undergoing decoherence as it interacts with the environment (the stack).

2. **Discrete vs. continuous λ.** The falling height h(t) gives a discrete approximation to the continuous λ ∈ [0,1]. In the continuum limit (H → ∞), the model recovers the smooth G_λλ(λ) curve of Paper 1.

3. **The T^d quotient is absent.** Real Tetris has no analogue of the T^d phase-redundancy of the coherence space Σ = U(d)/T^d. The model captures the quasipotential and record-constitution structure but not the gauge-theoretic aspects of the frame manifold.

4. **Line clearing removes visible information.** In HCR, the past is fixed but visible; in Tetris, completed rows are erased from the board (though recorded in the score). This deviation is actually structurally useful: it models the distinction between the *accessible board state* (present coherence frame) and the *immutable causal record* (past facts), which maps cleanly onto the difference between 𝒟_F and the underlying physical reality ℛ.

5. **No holonomy / Ω_AB term.** Piece rotations (L→J→S→Z) are closed loops in orientation space. If Ω_AB ≠ 0, a full rotation cycle should exhibit hysteresis — the piece should not return to its original configuration after forward+reverse rotation. Standard Tetris ignores this; a full HCR-Tetris would implement measurable orientation hysteresis as a discrete Prediction 2.

---

## Status and Next Steps

This section is a **placeholder draft**. Before inclusion in the paper, the following should be resolved:

- [ ] Decide placement: §7 (EOM and record constitution) vs. a standalone illustrative appendix
- [ ] Decide level of formalism: the current version is semi-formal; a more rigorous version would define the Hilbert space, T_AB operator, and EOM explicitly on the discrete grid
- [ ] Add a figure: a schematic Tetris board annotated with λ-zones (future/present/past), G_λλ curve inset, and complete/incomplete row distinction
- [ ] Calibrate citations: connects to Paper 1 §2.3–2.4, §3.3, §6.2–6.3, Thm. 2; connects to Paper 2A §7 (EOM), §2.2 (T_AB decomposition)
- [ ] Consider whether the line-clear irreversibility should be elevated to a named Proposition ("Proposition X.1: A complete row is an observer-independent fact under the discrete record-constitution criterion")

---

*Draft produced 2026-05-02. For structural reference only; not yet reviewed for inclusion.*
