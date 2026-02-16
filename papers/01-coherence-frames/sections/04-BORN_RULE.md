# Section 4: The Born Rule as Frame-Invariant Measure

## 4.1 Statement of the Main Result

**Theorem (Born Rule from Frame Invariance)**: Let Sigma be the coherence space of a quantum system with Hilbert space H (dim >= 2). Let mu be a measure on the alternatives {|i>_F} in any coherence frame F, satisfying:

(A1) **Frame invariance**: mu is invariant under all allowed coherence-frame transformations U_{F->F'}
(A2) **Additivity**: mu is additive on mutually orthogonal alternatives
(A3) **Dependence**: mu_F(i) depends only on the state psi_F and the component |i>_F
(A4) **Continuity**: mu_F(i) is continuous in the coefficients c_i

Then:
    mu_F(i) = |c_i|^2

where psi_F = Sum_i c_i |i>_F. The Born rule is the unique frame-invariant probability assignment.

## 4.2 Derivation

### Step 1: Frame Invariance as Symmetry Constraint

Consider frames F and F' related by a coherence relabeling:

    U_{F->F'}: |i>_F -> e^{i theta_i} |pi(i)>_{F'}

By axiom A1, the measure must satisfy:

    mu_F(i) = mu_{F'}(pi(i))

This means mu is invariant under arbitrary permutations and phase rotations of basis states. In particular, mu_F(i) depends on the state and basis only through |c_i| (modulus), since phases are removable by frame transformation.

### Step 2: Equal Coefficients Yield Equal Weights

For the state:
    psi_F = (1/sqrt(N)) Sum_{k=1}^N |k>_F

all |c_k| = 1/sqrt(N) are equal. By permutation invariance (Step 1):

    mu_F(1) = mu_F(2) = ... = mu_F(N)

Normalization (Sum mu_F(k) = 1, from additivity A2) gives:

    mu_F(k) = 1/N = |c_k|^2

The Born rule holds for all equal-amplitude states.

### Step 3: Rational Amplitudes via Frame Splitting

For a state with rational-ratio amplitudes:

    psi_F = sqrt(m/(m+n)) |0>_F + sqrt(n/(m+n)) |1>_F

with positive integers m, n, construct an enlarged frame F' via frame splitting (Definition 3.3):

    |0>_F -> (1/sqrt(m)) Sum_{k=1}^m |0,k>_{F'}
    |1>_F -> (1/sqrt(n)) Sum_{l=1}^n |1,l>_{F'}

In F', the state becomes:

    psi_{F'} = (1/sqrt(m+n)) [Sum_{k=1}^m |0,k>_{F'} + Sum_{l=1}^n |1,l>_{F'}]

This is an equal-amplitude superposition of (m+n) states. By Step 2:

    mu_{F'}(0,k) = mu_{F'}(1,l) = 1/(m+n)

Frame invariance (A1) and additivity (A2) give:

    mu_F(0) = Sum_{k=1}^m mu_{F'}(0,k) = m/(m+n) = |c_0|^2
    mu_F(1) = Sum_{l=1}^n mu_{F'}(1,l) = n/(m+n) = |c_1|^2

### Step 4: Extension to General Amplitudes

For arbitrary complex amplitudes c_i:

1. Approximate |c_i|^2 by rationals r_i^{(n)} with |r_i^{(n)} - |c_i|^2| < 1/n
2. For each rational approximation, Step 3 gives mu^{(n)}(i) = r_i^{(n)}
3. By continuity (A4): mu_F(i) = lim_{n->infty} mu^{(n)}(i) = |c_i|^2

QED.

## 4.3 Comparison with Previous Derivations

The derivation above follows a parallel logical structure to previous Born rule derivations but with a crucial conceptual difference: the symmetries exploited are coherence-frame transformations with physical content, not abstract mathematical properties of Hilbert space.

### Comparison Table

| Derivation | Symmetry Used | Physical Content | Assumes Born? | Result |
|-----------|---------------|-----------------|--------------|--------|
| **Gleason (1957)** | Non-contextuality of projectors | Mathematical structure of H | No | mu = Tr(rho P) |
| **Zurek (2005)** | Envariance of entangled states | Entanglement + environment | Debated | mu = |c_i|^2 |
| **Deutsch-Wallace** | Rational equivalence in branching | Many-worlds ontology | Debated | mu = |c_i|^2 |
| **Masanes et al. (2019)** | Operational axioms | Compositional structure | No | Born rule unique |
| **This work** | Coherence-frame invariance | Geometric (Sigma, T_AB) | No | mu = |c_i|^2 |

### Relation to Gleason
Gleason's theorem proves that non-contextuality on projectors forces the Born rule. Our derivation shows that coherence-frame invariance forces non-contextuality: if the measure mu must be the same in all frames, then it cannot depend on which measurement context (frame) contains a given projector. The coherence-relativity derivation thus provides the physical reason for Gleason's mathematical assumption.

### Relation to Envariance
Zurek's envariance argument exploits the fact that swapping system labels in an entangled state can be "undone" by a compensating swap on the environment. In our language, envariance is a specific type of frame transformation (frame splitting + permutation) applied to bipartite systems. Our derivation generalizes this: we use the full group of frame transformations, not just swap-type operations on entangled pairs.

### Relation to Deutsch-Wallace
The decision-theoretic derivation assumes rational agents in a branching universe and derives Born weights from axioms about preferences. Our derivation replaces the branching ontology and rationality axioms with geometric frame-invariance. The logical structure is similar (equal amplitudes first, then rational, then general), but the physical picture is different: we have one reality and many frames, not many worlds and one agent.

## 4.4 Physical Interpretation

The Born rule, in this framework, is not:
- A mysterious postulate appended to quantum mechanics
- A statement about frequencies of random events
- A normative constraint on rational beliefs
- A consequence of many-worlds branching

It is:
- **The unique frame-invariant probability assignment** on the coherence manifold Sigma
- The quantum analog of the invariant interval ds^2 in special relativity
- A geometric feature of the coherence space, independent of any particular frame, interpretation, or observer

Just as the invariant interval encodes the causal structure of spacetime regardless of which reference frame you use to describe it, the Born measure encodes the probabilistic structure of quantum reality regardless of which coherence frame you use to describe it.

## 4.5 Addressing the Splitting Assumption

The key non-trivial step is the existence of frame splittings (Step 3). We justify this on three grounds:

1. **Hilbert space structure**: Tensor product extensions and Schmidt decompositions guarantee that for any rational amplitude ratio, an enlarged Hilbert space with the required equal-amplitude decomposition exists. This is a theorem, not an assumption.

2. **Physical realization**: The enlarged frame F' corresponds to a finer-grained measurement. Any measurement with discrete outcomes i can, in principle, be refined to a measurement with sub-outcomes (i, k) by coupling to an additional degree of freedom (ancilla). Quantum mechanics guarantees this possibility.

3. **Self-consistency**: The Born rule derived via splitting is consistent with the Born rule applied to the enlarged system. There is no circularity because the splitting construction uses only the equal-amplitude result (Step 2), which itself follows from symmetry alone.

The splitting assumption is thus not an independent postulate but a consequence of the Hilbert space formalism that coherence relativity inherits from standard quantum mechanics.
