# Equations Reference - Coherence Relativity

**Purpose**: Central definitions, theorems, and key equations with LaTeX labels
**Usage**: Cross-reference when writing paper sections; ensure consistency

---

## Core Definitions

### D1. Coherence Space (Sigma)
Physical reality is described on a joint manifold M x Sigma, where:
- M: emergent spacetime manifold
- Sigma: coherence manifold (space of coherence frames)

A coherence frame F is a choice of section/chart on Sigma.

**LaTeX label**: `\label{def:coherence-space}`

### D2. State Representation
For a given underlying reality R, the state in coherence frame F is:
```
psi_F = psi_F(R)
```
Different frames yield different representations of the same reality:
```
psi_F(R) ≠ psi_{F'}(R)    (in general)
```

**LaTeX label**: `\label{def:state-representation}`

### D3. Frame Transformations
Maps between coherence frames:
```
U_{F->F'}: Sigma -> Sigma
psi_{F'} = U_{F->F'} psi_F
```
These preserve a fundamental invariant (the Born measure).

**LaTeX label**: `\label{def:frame-transformation}`

### D4. Tensor Field T_AB
A field on M x Sigma encoding:
- Information geometry of coherence frames (metric-like part)
- Frame transformation dynamics (connection/flow part)
- In specific regimes, reduces to quasipotential landscapes

**LaTeX label**: `\label{def:tensor-field}`

---

## Axioms (main.tex numbering — authoritative)

### A1. Frame Invariance
mu is invariant under coherence relabelings (Eq. relabeling) and frame splittings (Eq. splitting).
This includes permutation symmetry and phase invariance.

**LaTeX label**: `\label{thm:born}` (A1) in main.tex §IV.A

### A2. Additivity
mu is additive on mutually orthogonal alternatives.

**LaTeX label**: `\label{thm:born}` (A2) in main.tex §IV.A

### A3. Frame Locality (Dependence)
mu_F(i) depends only on |psi>_F and |i>_F — not on the history of frame
transformations leading to F, nor on probability assignments in other frames.
This is a locality assumption on Sigma analogous to independence of probability
assignments from distant reference frames in relativistic theories.

**LaTeX label**: `\label{thm:born}` (A3) in main.tex §IV.A

### A4. Continuity
mu_F(i) is continuous in the coefficients c_i.

**LaTeX label**: `\label{thm:born}` (A4) in main.tex §IV.A

### Legacy mapping (EQUATIONS_REFERENCE.md → main.tex)
Previous versions of this file used a different numbering:
- Old A1 (Born Measure Postulate) → collapsed into main.tex A1+A2+A3+A4
- Old A2 (Relational Invariance) → not a separate axiom in main.tex; follows from A1+A2 via splitting
- Old A3 (Symmetry Under Coherence Relabelings) → subsumed by main.tex A1

**All references in section drafts should use main.tex numbering.**

### Definition 2 addendum (pending integration into main.tex)
Definition 2 (Coherence Frame) should explicitly state:
> Information never received by the observer is excluded from the accessible
> sector on the same footing as information actively decohered into the bath.
This is currently implicit in A3 (frame locality) but should be stated in the definition.

---

## Main Theorems

### T1. Born Rule (Main Result)
Under axioms A1-A3:
```
mu_F(i) = |c_i|^2
```
where psi_F = Sum_i c_i |i>_F.

The Born rule is the **unique** frame-invariant probability assignment.

**Proof outline**: 4 steps (see BORN_RULE_DERIVATION.md)

**LaTeX label**: `\label{thm:born-rule}`

### T2. Equal Coefficient Lemma
For psi_F = (1/sqrt(N)) Sum_{k=1}^N |k>_F:
```
mu_F(k) = 1/N = |c_k|^2
```
Follows from permutation symmetry (A3) and normalization.

**LaTeX label**: `\label{lem:equal-coefficients}`

### T3. Rational Extension
For rational-ratio amplitudes |c_0|^2 = m/(m+n), |c_1|^2 = n/(m+n):
Frame-splitting into enlarged frame F' with (m+n) equal-amplitude sub-alternatives gives:
```
mu_F(0) = m/(m+n) = |c_0|^2
mu_F(1) = n/(m+n) = |c_1|^2
```

**LaTeX label**: `\label{thm:rational-extension}`

---

## Key Equations for Predictions

### E1. Fubini-Study Metric Component
```
G_{lambda lambda} = Re[<d_lambda psi | d_lambda psi> - <d_lambda psi | psi><psi | d_lambda psi>]
```
For double-slit with which-path resolution parameter lambda in [0,1].

**LaTeX label**: `\label{eq:fubini-study}`

### E2. Visibility (Standard QM)
```
V(lambda) = sqrt(1 - lambda^2)
```

**LaTeX label**: `\label{eq:visibility-standard}`

### E3. Visibility (Coherence Relativity)
```
V(lambda) = cos(d(F_lambda, F_0) / L_coherence)
```
where d is geodesic distance in Sigma, L_coherence is curvature scale.

**LaTeX label**: `\label{eq:visibility-cr}`

### E4. Hysteresis
```
V_recovered = V_initial * exp(-S_produced / k_B)
```
where S_produced depends on transformation rate and environmental coupling.

**LaTeX label**: `\label{eq:hysteresis}`

### E5. GHZ Curvature Correction
```
<O_N> = cos^N(theta) * [1 + alpha(N)/L_coherence^2 + O(1/L^4)]
```
where alpha(N) ~ N^2 for GHZ states.

**LaTeX label**: `\label{eq:ghz-correction}`

### E6. Gravitational Decoherence
```
Gamma_CR = Gamma_grav * [1 + beta (dg/dt)^2 tau_coherence^2]
```
Standard: Gamma_grav = (G m^2 / hbar) * <(Delta x)^2>

**LaTeX label**: `\label{eq:grav-decoherence}`

### E7. Transformation Timescale
```
tau_transform = hbar / (E_coupling * f(coherence structure))
```

**LaTeX label**: `\label{eq:transform-time}`

### E8. Action Functional
```
S[gamma] = (1/4D) integral G_{lambda lambda} (d lambda/ds - F^lambda)^2 ds
```
where D = noise intensity, F^lambda = drift toward pointer basis.

**LaTeX label**: `\label{eq:action-functional}`

### E9. Quasipotential
V(lambda) derived from minimizing S[gamma] subject to boundary conditions.
Determines metastability landscape for frame transitions.

**LaTeX label**: `\label{eq:quasipotential}`

---

## Parameter Definitions

| Symbol | Meaning | Typical Value |
|--------|---------|---------------|
| lambda | Which-path resolution parameter | [0, 1] |
| Sigma | Coherence manifold | — |
| F | Coherence frame | — |
| T_AB | Tensor field on M x Sigma | — |
| G_{lambda lambda} | Fubini-Study metric component | Computed numerically |
| L_coherence | Coherence length scale | System-dependent |
| D | Noise intensity (decoherence) | ~ hbar / tau_dec |
| tau_dec | Decoherence time | ~ 10^-6 s (SC qubit) |
| F^lambda | Drift toward pointer basis | Environment-induced |
| V(lambda) | Quasipotential | Computed from S[gamma] |
| mu | Born measure | |c_i|^2 |
