# Section 3: Frame Transformations and Invariants

## 3.1 Frame Transformation Maps

### Definition 3.1 (Frame Transformation)
A **frame transformation** U_{F->F'} is a map from coherence frame F to coherence frame F' that takes the state representation psi_F to psi_{F'}:

    psi_{F'} = U_{F->F'} psi_F

In the Hilbert space picture, U_{F->F'} is a unitary operator relating the two bases:

    |i>_{F'} = Sum_j (U_{F->F'})_{ji} |j>_F

### Definition 3.2 (Coherence Relabeling)
A **coherence relabeling** is a frame transformation that permutes and phase-rotates basis vectors:

    U_{F->F'}: |i>_F -> e^{i theta_i} |pi(i)>_{F'}

where pi is a permutation of indices and theta_i are real phases.

Coherence relabelings form a subgroup of all frame transformations. They are analogous to rotations and boosts within the Lorentz group: they change the description without changing the physics.

## 3.2 Group Structure

### Proposition 3.1
The set of frame transformations has the following algebraic structure:

1. **Composition**: U_{F->F''} = U_{F'->F''} . U_{F->F'} (chaining frame changes)
2. **Identity**: U_{F->F} = I (staying in the same frame)
3. **Inverse**: (U_{F->F'})^{-1} = U_{F'->F} (frame changes are reversible)

Frame transformations therefore form a **groupoid** over Sigma (a group if we fix a base frame).

### Proposition 3.2 (Unitary Representation)
For finite-dimensional Hilbert spaces, each frame transformation U_{F->F'} has a unitary matrix representation in H. This follows from the requirement that the inner product structure is preserved:

    <psi|phi>_F = <U psi | U phi>_{F'}

ensuring that probabilities (Born measures) are consistently defined across frames.

## 3.3 Frame Splitting

### Definition 3.3 (Frame Splitting)
A **frame splitting** is a frame transformation from F to an enlarged frame F' where a single basis state in F is represented as an equal-amplitude superposition of multiple states in F':

    |i>_F -> (1/sqrt(m_i)) Sum_{k=1}^{m_i} |i,k>_{F'}

where {|i,k>_{F'}} are orthonormal in the enlarged space.

**Physical realization**: Frame splitting corresponds to replacing a coarse measurement (outcome i) with a finer measurement that resolves sub-alternatives (outcome i,k). This is always possible in quantum mechanics via tensor product extensions: couple the system to an ancilla and perform a joint measurement with finer resolution.

### Proposition 3.3 (Existence of Splittings)
For any state psi_F = Sum_i c_i |i>_F with rational |c_i|^2 = m_i / M (where m_i are positive integers and M = Sum m_i), there exists a frame splitting F -> F' such that:

    psi_{F'} = (1/sqrt(M)) Sum_{i,k} |i,k>_{F'}

is an equal-amplitude superposition of M orthogonal states.

**Proof sketch**: Construct F' by tensorproduct with an ancilla of dimension max(m_i). Define |i,k>_{F'} = |i>_F tensor |k>_ancilla with appropriate normalization. The unitary embedding exists by construction.

This proposition is the key technical ingredient for Step 3 of the Born rule derivation.

## 3.4 Invariants Under Frame Transformations

### Theorem 3.1 (Frame Invariants)
The following quantities are invariant under all coherence-frame transformations:

1. **Total probability**: Sum_i mu_F(i) = 1 in all frames
2. **Born measure of physical alternatives**: mu_F(i) = mu_{F'}(pi(i)) for relabelings
3. **Inner products**: |<psi|phi>|^2 is frame-independent
4. **Eigenvalue spectra**: The spectrum of any observable is frame-independent
5. **Entanglement measures**: For bipartite systems, entanglement entropy S(rho_A) is frame-independent

### Remark: What Is NOT Invariant
The following are frame-dependent:
- Which observables appear to have definite values
- Whether a state appears "coherent" or "decohered"
- The specific form of the density matrix (diagonal vs off-diagonal structure)
- Whether a system appears entangled with its environment

This distinction—frame-invariant physical content versus frame-dependent description—is the core conceptual contribution of coherence relativity.

## 3.5 Worked Example: Double-Slit Frame Transformation

Consider the double-slit setup with:
- F_int (interference frame): psi_{F_int} = (1/sqrt(2))(|A> + |B>)
- F_wp (which-path frame, with detector W): psi_{F_wp} = (1/sqrt(2))(|A>|W_A> + |B>|W_B>)

The transformation U_{F_int -> F_wp} is physically realized by coupling the particle to detector W:

    U: |A>|W_0> -> |A>|W_A>
       |B>|W_0> -> |B>|W_B>

where |W_0> is the detector ready state and <W_A|W_B> = 0 (orthogonal detector states).

**Frame invariants in this example**:
- Born measure: mu(A) = mu(B) = 1/2 in both frames
- Total probability: 1 in both frames
- Inner product |<psi|psi>|^2 = 1 in both frames

**Frame-dependent quantities**:
- In F_int: Interference visible. Off-diagonal terms Re[<A|rho|B>] nonzero.
- In F_wp: No interference. Reduced density matrix rho_particle is diagonal.

The interference "disappeared" not because something physical changed, but because we changed frames. This is exactly analogous to how the magnetic field "appears" when boosting an electric charge in SR—it was always there in the electromagnetic field tensor, but frame-dependent.

## 3.6 Connection to the Tensor Field T_AB

The tensor field T_AB on M x Sigma encodes the dynamics of frame transformations. While its full development is deferred to Paper 2, we note its essential role:

1. **Metric part**: The symmetric part of T_AB restricts to the Fubini-Study metric on Sigma, measuring information-geometric distance between frames.

2. **Connection part**: The antisymmetric part encodes how physical interactions (measurement couplings, environmental decoherence) drive frame transformations. It determines:
   - Which frames are dynamically accessible from a given starting frame
   - The rate of frame transformation (related to measurement interaction strength)
   - The metastable frame configurations (classical pointer states)

3. **Quasipotential**: In the limit of strong environmental coupling, the scalar functional V(lambda) derived from T_AB defines a quasipotential landscape whose minima correspond to stable classical frames (pointer states) and whose barriers determine transition rates between them.

For the purposes of this paper, we use only the metric part (Fubini-Study) and the qualitative features of the quasipotential in formulating our experimental predictions.
