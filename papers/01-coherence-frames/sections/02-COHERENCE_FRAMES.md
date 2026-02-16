# Section 2: Coherence Frames and the Geometry of Quantum Description

## 2.1 Definitions

### Definition 2.1 (Coherence Space)
Let H be a Hilbert space describing a quantum system. The **coherence space** Sigma is the space of all physically realizable coherence frames for that system.

For a system with Hilbert space H of dimension d, Sigma can be identified with the space of orthonormal bases of H, modulo physically irrelevant phase redundancies. More precisely, Sigma = U(d) / T^d, where U(d) is the unitary group and T^d is the maximal torus of diagonal phase transformations.

For composite systems H = H_A tensor H_B, Sigma inherits additional structure from the tensor product, reflecting the physical choice of which subsystem decomposition defines "the system" versus "the environment."

### Definition 2.2 (Coherence Frame)
A **coherence frame** F in Sigma is a choice of:
1. A preferred orthonormal basis {|i>_F} of H (or a subspace decomposition)
2. A specification of which degrees of freedom encode "definiteness" in the given measurement context

A coherence frame determines not just a basis but a *perspective*: it specifies which observables have definite values, which correlations are visible, and which aspects of the quantum state appear "coherent" versus "decohered."

### Definition 2.3 (State Representation)
For a given underlying physical reality R, the state representation in coherence frame F is:

    psi_F = Sum_i c_i^{(F)} |i>_F

where the coefficients c_i^{(F)} depend on the frame. The same reality R has different representations in different frames:

    psi_F(R) =/= psi_{F'}(R)    (in general)

but describes the same physical situation.

## 2.2 Simple Examples

### Example 2.1: Single Qubit
For a qubit (d = 2), Sigma is parameterized by a point on the Bloch sphere specifying the measurement axis. The frame F_z corresponds to measuring in the {|0>, |1>} (computational) basis; F_x corresponds to {|+>, |->}; and so on.

A state |psi> = alpha|0> + beta|1> in F_z becomes |psi> = (alpha+beta)/sqrt(2)|+> + (alpha-beta)/sqrt(2)|-> in F_x. The state is the same; only the frame (and hence the description) has changed.

**Coherence in F_z**: The off-diagonal element alpha*beta in the density matrix rho = |psi><psi| represents coherence relative to the z-basis. In F_x, different off-diagonal elements appear. Coherence is not a property of the state alone but of the state-in-a-frame.

### Example 2.2: Double Slit
The double-slit (detailed in Section 4) provides a two-frame example:
- **F_int** (interference frame): Basis is path superpositions. Interference is visible.
- **F_wp** (which-path frame): Basis is path eigenstates. Which-path information is definite.

Both frames describe the same physical setup. The "choice" of frame is determined by the experimental configuration (whether a which-path detector is present).

### Example 2.3: Bipartite System
For a composite system H_A tensor H_B:
- **F_global**: Frame in which the joint state |psi_AB> is described. Entanglement is visible.
- **F_A**: Frame restricted to subsystem A. State is rho_A = Tr_B(|psi_AB><psi_AB|). Entanglement manifests as mixedness.

The transition F_global -> F_A (tracing out B) is a frame transformation that replaces joint coherence with local mixedness. This is the standard decoherence picture, reinterpreted as a frame change.

## 2.3 Metric Structure on Sigma

The coherence space Sigma inherits a natural metric from the Hilbert space structure: the **Fubini-Study metric**.

### Definition 2.4 (Fubini-Study Metric on Sigma)
For a one-parameter family of coherence frames F_lambda parameterized by lambda in [0,1], the metric component is:

    G_{lambda lambda} = Re[<d_lambda psi | d_lambda psi> - <d_lambda psi | psi><psi | d_lambda psi>]

This measures the "information-geometric distance" between nearby frames: how much the quantum description changes as the frame varies.

**Properties**:
- G_{lambda lambda} >= 0 (positive semi-definite)
- G_{lambda lambda} = 0 only when the frame change is a pure phase (physically trivial)
- Geodesic distance d(F, F') = integral sqrt(G_{lambda lambda}) d lambda gives the shortest path in Sigma between two frames

**Physical meaning**: G_{lambda lambda} quantifies how distinguishable two nearby coherence frames are. Large G means small changes in frame produce large changes in the quantum description—the system is "sensitive" to frame choice in that region of Sigma.

### Remark: Connection to Quantum Fisher Information
The Fubini-Study metric is related to the quantum Fisher information F_Q by G = F_Q / 4. This connects the geometry of coherence space to quantum estimation theory: the metric measures how precisely a frame parameter can be estimated from quantum measurements.

## 2.4 Analogy with Special Relativity

The coherence-frame structure parallels the inertial-frame structure of special relativity:

| Special Relativity | Coherence Relativity |
|-------------------|---------------------|
| Spacetime event | Physical reality R |
| Inertial frame | Coherence frame F |
| Coordinates (t, x, y, z) | State representation psi_F |
| Lorentz transformation | Frame transformation U_{F->F'} |
| Invariant interval ds^2 | Born measure mu = |c_i|^2 |
| Minkowski metric | Fubini-Study metric on Sigma |
| Speed of light (invariant) | Total probability = 1 (invariant) |
| Simultaneity (frame-relative) | Coherence (frame-relative) |

The key structural parallel: In SR, there is no absolute fact about whether two events are simultaneous—it depends on the inertial frame. In CR, there is no absolute fact about whether a system is "in superposition" or "has collapsed"—it depends on the coherence frame.

## 2.5 Physical Content

A coherence frame is not an abstract mathematical construct. It corresponds to a concrete physical situation: the measurement apparatus, the environment coupling, the subsystem partition, and the observational access that an agent has to the quantum system.

Changing coherence frame corresponds to physically changing one of these:
- Turning on a detector (F_int -> F_wp)
- Gaining access to an environment (F_local -> F_global)
- Changing measurement basis (F_z -> F_x)
- Opening Schrodinger's box (F_outside -> F_inside)

The tensor field T_AB (Section 2.6, developed fully in Paper 2) encodes which frame transformations are physically accessible from a given frame and with what dynamics. Not all frames are equally accessible; the geometry of Sigma, shaped by T_AB, determines the landscape of possible frame transformations for a given physical setup.
