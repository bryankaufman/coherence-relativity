# §X Left vs Right Generators of M×Σ Dynamics
## Settimo et al. (2026) Integration Draft for Paper 2

## Executive Summary
Paper 2 currently develops the mixed-sector structure from the Schrödinger-side generator. This draft adds the dual Heisenberg-side generator and formalizes a left-right decomposition of cross-terms and metric faces on `M×Σ`.

## X.1 Generator Pair and Master-Equation Form
Let `Φ_t` be the dynamical map. Write
`Φ̇_t = L_t ∘ Φ_t` (left / Schrödinger form),
`Φ̇_t = Φ_t ∘ R_t` (right / Heisenberg form),
with
`R_t = Φ_t^{-1} ∘ L_t ∘ Φ_t`.

In general `L_t ≠ R_t`; equality is recovered in commutative (semigroup) sectors.

Domain assumption: the conjugation formula for `R_t` is valid on time intervals where `Φ_t` is invertible on the relevant operator support. At singular/non-invertible times, the right-generator must be defined by a restricted-support inverse or limiting construction.

## X.2 Left-Right Split of the Mixed Cross-Term
Define:
- `T_MΣ^(left)`: mixed `M–Σ` projection induced by `L_t`,
- `T_MΣ^(right)`: mixed `M–Σ` projection induced by `R_t`.

Commutative benchmark:
`T_MΣ^(left) = T_MΣ^(right)`.
Deviation from equality quantifies left-right picture inequivalence in the mixed sector.

## X.3 Two-Face Metric Structure
Introduce two metric faces on the same underlying manifold:
- `G_ij^(S)` (state-side / left-induced),
- `G_ij^(H)` (effect-side / right-induced).

Define the mismatch tensor:
`ΔG_ij := G_ij^(S) - G_ij^(H)`.

Working hypothesis:
`ΔG_ij ≠ 0` iff mixed-sector non-commutativity is active (`Ω_{MΣ} ≠ 0`).

## X.4 Pointer-Sector Consistency Criterion
Refined statement:
pointer sectors are those for which left and right generator actions coincide after physical projection.

Equivalent operational form:
pointer selection occurs where mixed non-commutativity is extinguished in the observable sector.

## X.5 Derivation Program
1. Derive `T_MΣ^(right)` explicitly in the single-qubit decoherence model using `R_t = Φ_t^{-1} ∘ L_t ∘ Φ_t` on invertible intervals, and specify the extension across non-invertible points.
2. Prove or refute `T_MΣ^(left) = T_MΣ^(right)` under pointer-sector assumptions.
3. Compute `||L_t - R_t||_op` as a function of `λ_M` and test suppression toward Phase III.
4. Interpret `G_ij^(H)` as the Heisenberg/effect-side metric face of `M×Σ`.

## X.6 Scope and Placement
This section extends, but does not replace, the current `T_MΣ` derivation. Its role is to formalize dual-generator completion of the mixed sector and to identify where left-only closure is structurally incomplete.
