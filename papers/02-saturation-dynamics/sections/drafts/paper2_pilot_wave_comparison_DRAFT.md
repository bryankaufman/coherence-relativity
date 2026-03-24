# T_{MΣ} and the Pilot Wave: A Structural Comparison

**Status:** WORKING DRAFT — roughing out the structural parallel
**Date:** 2026-03-11
**Purpose:** Explore whether the T_{MΣ} cross-term and frame-lag mechanism bear a formal relationship to de Broglie-Bohm pilot wave theory. Assess what CR preserves, what it replaces, and where testable differences arise.

---

## 1. The Bohmian Framework (Setup)

In de Broglie-Bohm theory, a quantum system with wave function ψ = R·e^{iS/ℏ} (where R ≥ 0 is the amplitude and S is the phase, both real functions on configuration space) obeys two coupled equations:

**Guidance equation** (determines particle trajectories):

$$\dot{q}_k = \frac{1}{m_k} \nabla_k S(q_1, \ldots, q_N, t)$$

**(PW-1)**

**Continuity equation** (conserves probability):

$$\frac{\partial R^2}{\partial t} + \sum_k \nabla_k \cdot \left(\frac{R^2}{m_k} \nabla_k S\right) = 0$$

**(PW-2)**

The Hamilton-Jacobi equation for S acquires an extra term — the **quantum potential**:

$$\frac{\partial S}{\partial t} + \sum_k \frac{(\nabla_k S)^2}{2m_k} + V + Q = 0$$

**(PW-3)**

where

$$Q = -\sum_k \frac{\hbar^2}{2m_k} \frac{\nabla_k^2 R}{R}$$

**(PW-4)**

The quantum potential Q is what makes Bohmian trajectories non-classical. It depends on the amplitude R of the wave function, not on its magnitude (it's homogeneous of degree zero in R), so it can produce large effects even for low-amplitude wave packets. It encodes nonlocal correlations: Q for an N-particle system lives on 3N-dimensional configuration space, and a change in one particle's position instantaneously affects Q for all others.

### Key structural features of pilot wave theory:

1. **Deterministic trajectories**: Given initial conditions (q₁(0), ..., qN(0)) and ψ(0), the future is determined.
2. **Wave function as guiding field**: ψ evolves by the Schrödinger equation and generates the velocity field v_k = ∇_k S / m_k.
3. **Quantum potential as the "extra force"**: Q is what distinguishes quantum from classical motion. It vanishes when R is spatially uniform (plane waves), recovers classical Hamilton-Jacobi when ℏ → 0 *and* R varies slowly.
4. **Configuration-space nonlocality**: Q lives on 3N dimensions, not 3. This is the source of Bell-nonlocal correlations.
5. **No intrinsic classicalization mechanism**: The guidance equation holds at all scales. Bohm doesn't predict *when* or *why* the system becomes classical — decoherence must be imported from outside the theory.
6. **Equilibrium hypothesis**: Born's rule |ψ|² emerges only if initial conditions are "typical" (quantum equilibrium). This is an additional postulate.

---

## 2. The CR Framework (Corresponding Objects)

In CR, the joint manifold M × Σ carries the Fubini-Study metric G_{AB} with the cross-term T_{MΣ} encoding quantum-classical coupling (§2.1). The distinguishability parameter λ controls coupling strength (§2.2). The action is:

$$S[\mathbf{X}, \lambda] = \frac{1}{4D} \int \left[\mathcal{V}^\mu G_{\mu\nu} \mathcal{V}^\nu + 2\lambda \mathcal{V}^\mu T_{\mu a} (\dot{\xi}^a - \mathcal{F}^a) + (\dot{\xi}^a - \mathcal{F}^a) G_{ab} (\dot{\xi}^b - \mathcal{F}^b)\right] ds$$

**(CR-1)** [= Eq. 2.2.7]

The frame-lag force is:

$$F^a_{\text{lag}} = \lambda \, T_{\mu a} \, G^{\mu\nu} (\text{M-sector acceleration})_\nu$$

**(CR-2)** [= Eq. 2.2.21]

And the characteristic frame-lag ratio is:

$$\frac{\ddot{\xi}^a}{\ddot{x}^\mu} \sim -\frac{\lambda \, T_{\mu a}}{G_{ab}}$$

**(CR-3)** [= Eq. 2.2.33]

### Key structural features of CR:

1. **Deterministic evolution above the Markov threshold**: For λ > 0, the Euler-Lagrange equations on M × Σ give deterministic trajectories in both spacetime and coherence-frame coordinates.
2. **T_{MΣ} as the coupling mechanism**: The cross-term plays the role of the "guiding" influence — it's what makes M-sector motion affect Σ-sector dynamics.
3. **Frame-lag force as the "extra force"**: F^a_lag (CR-2) is what distinguishes coupled quantum-classical evolution from decoupled classical geodesic motion.
4. **Finite-dimensional geometry**: T_{MΣ} lives on M × Σ (finite-dimensional), not on 3N-dimensional configuration space.
5. **Intrinsic classicalization**: The Markov transition at λ → 0 provides a geometric mechanism for classicalization. This is built into the formalism, not imported.
6. **Born rule from geometry**: The mixed-state Born rule (§2.4) derives measurement probabilities from the geometric structure. No equilibrium hypothesis needed.

---

## 3. The Structural Parallel: Object-by-Object

| Bohm (Pilot Wave) | CR (Coherence Relativity) | Relationship |
|---|---|---|
| Wave function ψ on configuration space Q^{3N} | State map Φ: M × Σ → PH | Both encode the "quantum information" that guides dynamics. ψ lives on 3N-dim config space; Φ lives on finite-dim M × Σ. |
| Phase gradient ∇S/m (velocity field) | Drift field 𝓕^A on M × Σ | Both generate the "preferred" flow. In Bohm, particles follow ∇S. In CR, the system follows 𝓕 = (𝓕^μ, 𝓕^a). |
| Quantum potential Q = -ℏ²∇²R/(2mR) | Frame-lag force F^a_lag = λ T_{μa} G^{μν} (accel)_ν | **This is the central correspondence.** Both are "extra forces" that distinguish quantum from classical motion. Both vanish in the classical limit. Both depend on the global structure of the quantum state, not just local conditions. |
| Guidance equation: q̇ = ∇S/m | Σ-sector EOM: G_{ab}(ξ̈^b - 𝓕̇^b) = λ T_{μa}(ẍ^μ - 𝓕̇^μ) + ... | Both are first-order-in-time evolution equations for the "hidden" degrees of freedom (particle positions / coherence frame coordinates). |
| Configuration space Q^{3N} (3N-dimensional) | Joint manifold M × Σ (finite-dimensional) | CR replaces 3N-dim config space with finite-dim M × Σ. This is a major structural simplification. |
| Nonlocality via Q on Q^{3N} | Nonlocality via connectivity on Σ | Both produce Bell-nonlocal correlations. Bohm achieves this through 3N-dim Q. CR achieves it through geometric connectivity on Σ (states at λ = 1 share fiber structure even when separated on M). |
| No classicalization mechanism | Markov transition at λ → 0 | CR has what Bohm lacks: a built-in mechanism for the quantum-to-classical transition. |
| Born rule from equilibrium hypothesis | Born rule from mixed-state geometry (§2.4) | CR derives |ψ|² from the formalism. Bohm postulates it (or derives it from typicality arguments). |

---

## 4. The Central Correspondence: Q ↔ F^a_lag

### 4.1 What they share

Both the quantum potential Q and the frame-lag force F^a_lag are:

- **State-dependent**: Q depends on R (amplitude of ψ). F^a_lag depends on T_{MΣ} (cross-term of Fubini-Study metric pulled back through the state map Φ).
- **Non-classical**: Both vanish in the classical limit. Q → 0 as ℏ → 0 (or when R is uniform). F^a_lag → 0 as λ → 0.
- **Responsible for quantum interference effects**: In Bohm, Q produces the trajectory bunching near interference maxima. In CR, the frame-lag force causes the coherence frame to respond to M-sector dynamics, producing quantum-coherent behavior.
- **Global/nonlocal**: Q depends on R everywhere (not just at the particle's position). F^a_lag depends on T_{MΣ} which encodes how the state map Φ correlates M-variations with Σ-variations — a global property of Φ, not a local one.

### 4.2 Where they diverge

**Dimensionality:**
Q lives on 3N-dimensional configuration space. For N particles, this is 3N real dimensions. The quantum potential's nonlocality arises because a change at one configuration-space point affects Q at all others.

F^a_lag lives on M × Σ, which is (dim M + dim Σ)-dimensional. For a 4D spacetime and a finite-dimensional Σ, this is a fixed finite number. The "nonlocality" is geometric: it arises from the fiber structure of Σ over M, not from high-dimensional configuration space.

**This is a genuine structural distinction, not a notational one.** The Bohmian quantum potential for a system of N entangled particles requires tracking correlations in 3N dimensions. CR encodes these correlations in the geometry of the finite-dimensional fiber Σ. Whether this is sufficient to reproduce all entanglement phenomena is an open question (see §6).

**Classicalization:**
Q has no built-in mechanism for vanishing. Bohmian mechanics is deterministic at all scales — the pilot wave guides particles forever. Decoherence can be modeled (by tracking environmental degrees of freedom), but it's an emergent phenomenon, not a fundamental feature of the theory.

F^a_lag has a built-in suppression mechanism: the Markov transition at λ → 0. When the coherence parameter drops below the Markov threshold (§2.3), the coupling between M and Σ becomes stochastic and then vanishes. Classicalization is a geometric prediction, not an addition.

**Probabilistic structure:**
In Bohm, the Born rule ρ = |ψ|² is either postulated (quantum equilibrium hypothesis) or derived from typicality arguments (Dürr-Goldstein-Zanghì). There has been debate about whether sub-quantum non-equilibrium distributions could exist.

In CR, the mixed-state Born rule (§2.4) derives measurement probabilities from the geometric structure of mixed states via purification extension and Naimark's theorem. The Born rule is a theorem, not a postulate.

**Coupling mechanism:**
Q modifies the Hamilton-Jacobi equation (PW-3) — it's an addition to the classical potential V. The particle "feels" Q as an extra force alongside V.

F^a_lag couples two *sectors* of a joint manifold: the M-sector acceleration drives Σ-sector acceleration through T_{MΣ}. It's not an extra potential term — it's a cross-sector coupling in the action itself (the middle term in CR-1). This is more analogous to how off-diagonal metric terms in GR couple different coordinate directions than to how a potential modifies a trajectory.

---

## 5. The Semiclassical Limit: Where CR Should Reproduce Bohm

### 5.1 The claim (to be verified)

In the semiclassical regime — where λ is close to 1, the coherence frame is well-defined, and the system is far from the Markov threshold — CR's frame-lag dynamics should reproduce Bohmian trajectories in the following sense:

**Conjecture (PW-CR Correspondence):** For a single-particle system in a slowly-varying potential V(x), in the limit where:
- dim(Σ) = 1 (single coherence parameter),
- G_{ab} and G_{μν} are approximately constant,
- λ ≈ 1,
- The state map Φ is of the form |ψ(x, ξ)⟩ = R(x)·e^{iS(x)/ℏ}·|ξ⟩,

the Σ-sector EOM (Eq. 2.2.27) reduces to a flow equation whose trajectories on M coincide with the Bohmian guidance equation (PW-1), and the frame-lag force F^a_lag reproduces the quantum potential Q to leading order.

### 5.2 Sketch of the argument

**Step 1: Identify the state map.**

Write ψ(x, ξ) = R(x, ξ)·exp(iS(x, ξ)/ℏ). Then:

$$\partial_\mu \psi = \left(\frac{\partial_\mu R}{R} + \frac{i}{\hbar} \partial_\mu S\right) \psi$$

$$\partial_a \psi = \left(\frac{\partial_a R}{R} + \frac{i}{\hbar} \partial_a S\right) \psi$$

**Step 2: Compute T_{MΣ}.**

From Eq. 2.1.9:

$$T_{\mu a} = \text{Re}\left[\langle \partial_\mu \psi | \partial_a \psi \rangle - \langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_a \psi \rangle\right]$$

Substituting the polar decomposition:

$$T_{\mu a} = \frac{\partial_\mu R \cdot \partial_a R}{R^2} + \frac{1}{\hbar^2} \partial_\mu S \cdot \partial_a S - \left(\frac{\partial_\mu R}{R}\right)\left(\frac{\partial_a R}{R}\right) - \frac{1}{\hbar^2}(\partial_\mu S)(\partial_a S)$$

Wait — the second-order terms cancel partially. Let me be more careful.

For a normalized state (⟨ψ|ψ⟩ = 1):

$$\langle \partial_\mu \psi | \partial_a \psi \rangle = \frac{\partial_\mu R \cdot \partial_a R}{R^2} + \frac{1}{\hbar^2} \partial_\mu S \cdot \partial_a S + \frac{i}{\hbar}\left(\frac{\partial_\mu S \cdot \partial_a R}{R} - \frac{\partial_\mu R \cdot \partial_a S}{R}\right)$$

And:

$$\langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_a \psi \rangle = \left(\frac{\partial_\mu R}{R} - \frac{i}{\hbar} \partial_\mu S\right)\left(\frac{\partial_a R}{R} + \frac{i}{\hbar} \partial_a S\right)$$

$$= \frac{\partial_\mu R \cdot \partial_a R}{R^2} + \frac{1}{\hbar^2} \partial_\mu S \cdot \partial_a S + \frac{i}{\hbar}\left(\frac{\partial_\mu R \cdot \partial_a S}{R} - \frac{\partial_\mu S \cdot \partial_a R}{R}\right)$$

Taking the difference and then Re[...]:

$$T_{\mu a} = \text{Re}\left[\frac{i}{\hbar}\left(\frac{\partial_\mu S \cdot \partial_a R}{R} - \frac{\partial_\mu R \cdot \partial_a S}{R}\right) - \frac{i}{\hbar}\left(\frac{\partial_\mu R \cdot \partial_a S}{R} - \frac{\partial_\mu S \cdot \partial_a R}{R}\right)\right]$$

$$= \text{Re}\left[\frac{2i}{\hbar}\left(\frac{\partial_\mu S \cdot \partial_a R - \partial_\mu R \cdot \partial_a S}{R}\right)\right]$$

Since Re[i·(real)] = 0...

**⚠️ PROBLEM**: For a single Hilbert-space state with ψ = R·e^{iS/ℏ}, the Fubini-Study cross-term T_{μa} appears to vanish identically when the state is a single ray in PH parameterized by (x, ξ) through R and S alone.

This suggests the correspondence is more subtle. The non-vanishing of T_{MΣ} requires that the state map Φ produce *genuinely different rays* for different (x, ξ) values — i.e., the dependence on x and ξ must not factorize as ψ(x, ξ) = f(x)·g(ξ).

### 5.3 Resolution: The correspondence requires mixed states or entanglement

The calculation above reveals something important. For a **pure state** parameterized as ψ = R(x,ξ)e^{iS(x,ξ)/ℏ}, the cross-term T_{μa} reduces to the Fubini-Study metric's off-diagonal block, which is non-zero only when the derivatives ∂_μψ and ∂_aψ are not proportional.

For Bohm, the quantum potential Q operates on a single wave function in configuration space. For CR, the cross-term T_{MΣ} operates on the pullback metric of the state map Φ.

The proper correspondence is:

**Bohmian Q arises from spatial variation of the amplitude R(q). CR's F^a_lag arises from the coupling between spatial and frame variation of the state map Φ.**

These are the same physics viewed from different mathematical frameworks when:
- The "amplitude variation" ∂_μR/R in Bohm maps to the M-sector component of the quantum geometric tensor
- The "frame sensitivity" ∂_aR/R + (i/ℏ)∂_aS in CR captures how the coherence basis responds to environmental changes

**The correspondence is not Q = F^a_lag directly, but rather:**

$$\text{Bohm: } Q \sim \frac{\hbar^2}{2m} \frac{\nabla^2 R}{R} \quad \longleftrightarrow \quad \text{CR: } F^a_{\text{lag}} \sim \lambda \cdot \mathcal{G}_{\mu a}^{(\text{Bures})} \cdot (\text{acceleration})$$

where $\mathcal{G}^{(\text{Bures})}$ is the mixed-state (Bures/quantum Fisher) information metric cross-term from §2.1.7.

The quantum potential Q encodes how the amplitude landscape curves in configuration space. The frame-lag force F^a_lag encodes how the information-geometric landscape of the state map curves in M × Σ. **Both measure "how much the quantum state resists being pushed classically."**

---

## 6. The Departures: What CR Does That Bohm Cannot

### 6.1 Dimensionality and the N-body problem

Bohm's quantum potential for N particles requires 3N-dimensional configuration space. This is not merely a technical inconvenience — it's the mechanism for entanglement. Two entangled particles at positions q₁, q₂ share a single Q(q₁, q₂) that cannot be decomposed as Q₁(q₁) + Q₂(q₂). The 3N-dimensionality is the price of nonlocality.

CR's T_{MΣ} lives on finite-dimensional M × Σ regardless of particle number. The "entanglement information" is encoded in the geometry of Σ — specifically, in how the fiber structure over M creates correlations between spatially separated regions.

**Open question**: Can the geometry of a finite-dimensional Σ fully reproduce the entanglement structure that Bohm encodes in 3N dimensions? If yes, this would be a major result (a geometric compression of entanglement). If no, it defines the limits of the correspondence.

### 6.2 The Markov transition (classicalization)

Bohm has no classicalization mechanism. The pilot wave guides particles forever. To recover classical physics, one must invoke environmental decoherence (tracking many degrees of freedom) or take the formal ℏ → 0 limit (which eliminates Q but also eliminates the theory).

CR's Markov transition at λ → 0 (§2.3) provides a geometric classicalization. The transition is:
- **Coordinate-invariant** (defined by the R_Markov criterion, not by basis choice)
- **Gradual** (λ decreases continuously from 1 to 0)
- **Environment-sensitive** (the Markov threshold depends on local curvature/decoherence conditions)
- **Irreversible in practice** (once λ < λ_Markov, the system is stochastic on Σ)

This is the feature that most distinguishes CR from pilot wave theory: CR predicts *when* systems become classical, not just *how* they evolve quantum-mechanically.

### 6.3 The Born rule

In Bohm, the Born rule ρ = |ψ|² is typically introduced as the quantum equilibrium hypothesis: if particles are initially distributed as |ψ(0)|², they remain so distributed for all time (equivariance). This raises the question: why should initial conditions satisfy quantum equilibrium? Dürr, Goldstein, and Zanghì give typicality arguments; Valentini argues that non-equilibrium distributions are possible in principle.

In CR, the Born rule is derived (§2.4) from the mixed-state extension of axioms (A1)–(A4) via purification and Naimark's theorem. The probabilities are geometric consequences of the formalism. No equilibrium hypothesis is needed.

### 6.4 Surreal trajectories and the Englert-Scully-Walther objection

A persistent criticism of Bohm is the "surreal trajectories" problem (Englert, Scully, Walther 1992): in a Mach-Zehnder interferometer, Bohmian trajectories can seem to follow "the wrong path" — going through arm A while the detector fires in arm B. This is because the quantum potential Q can redirect trajectories in counterintuitive ways.

In CR, the analogous dynamics occurs on Σ, not on M. The coherence frame can evolve in ways that are not simply "following one path" — because the frame-lag force couples M-sector and Σ-sector dynamics simultaneously. Whether CR reproduces or avoids the surreal trajectory phenomenon depends on how the state map Φ encodes which-path information. This is a concrete test case for the correspondence.

---

## 7. The Experimental Bridge: Steinberg, Wiseman, and Weak Measurements

### 7.1 Steinberg's Toronto experiments

Steinberg et al. (Science, 2011) used weak measurements to reconstruct "average photon trajectories" in a double-slit experiment. The trajectories they observed look strikingly Bohmian — photons appear to follow smooth paths that avoid the symmetry axis, exactly as Bohm predicts.

### 7.2 Wiseman's theoretical result

Wiseman (New J. Phys., 2007) proved that the trajectories reconstructed from weak measurements *are* the Bohmian trajectories, in a precise operational sense: the weak value of the momentum operator gives the Bohmian velocity field.

### 7.3 CR predictions

If CR reproduces Bohmian trajectories in the semiclassical limit (§5), then Steinberg's experiments are also tests of CR's frame-lag mechanism in that regime. The predictions should agree.

**The interesting question is where they disagree.** CR predicts that near the Markov threshold (λ → λ_Markov), the frame-lag force becomes stochastic. This would manifest as:

1. **Trajectory diffusion**: Near the Markov threshold, reconstructed weak-measurement trajectories should show increased variance — not the smooth Bohmian curves, but noisy, diffusing paths.

2. **Threshold-dependent behavior**: The onset of trajectory diffusion should correlate with environmental decoherence strength, not just with ℏ. Systems with stronger environmental coupling (higher decoherence rate) should show trajectory diffusion at larger scales.

3. **Frame-lag timescale**: The characteristic timescale τ_lag (from §2.2, Eq. 2.2.33) provides a quantitative prediction. Below τ_lag, the coherence frame tracks spacetime dynamics (Bohmian behavior). Above τ_lag, the frame lags and eventually decouples (classical behavior). This timescale is geometry-dependent — it depends on T_{MΣ} and λ — and is in principle measurable via weak measurement sequences.

**⚠️ UNTESTED**: None of these predictions have been worked out quantitatively. The claim that CR reproduces Bohmian trajectories in the semiclassical limit requires verification (§5.2 above hit a subtlety). The predictions about trajectory diffusion near the Markov threshold are qualitative extrapolations, not derived results.

---

## 8. Assessment and Placement

### What we've established:

1. **Structural parallel**: T_{MΣ} ↔ pilot wave, F^a_lag ↔ quantum potential Q. Both are state-dependent "extra forces" that make quantum dynamics non-classical. ✅ VERIFIED (structural argument)

2. **Key departures**: Finite-dimensional geometry (vs. 3N), built-in classicalization (vs. none), derived Born rule (vs. equilibrium hypothesis). ✅ VERIFIED (structural argument)

3. **Semiclassical correspondence**: CR should reproduce Bohm in the appropriate limit. ⚠️ UNTESTED — the polar-decomposition calculation (§5.2) reveals a subtlety in the pure-state case; the correspondence likely works at the mixed-state/Bures level (§2.1.7), not the pure-state Fubini-Study level.

4. **Experimental bridge**: Steinberg/Wiseman experiments test both theories in the semiclassical regime; CR predicts departures near the Markov threshold. ⚠️ UNTESTED — qualitative prediction, not quantitative.

### What remains open:

- **The pure-state subtlety**: The Fubini-Study cross-term T_{μa} may vanish for simple single-ray parameterizations (§5.2). The correspondence likely requires the mixed-state extension (§2.1.7, Bures metric). This needs careful treatment.
- **Quantitative semiclassical limit**: Show explicitly that F^a_lag → Q in appropriate limits. This may be a Paper 2 result if the math is tractable, or a Paper 3 pointer if it requires solving the full EOM.
- **N-body entanglement**: Whether Σ's geometry can encode the same entanglement structure as 3N-dimensional configuration space.
- **Surreal trajectories**: Whether CR reproduces, avoids, or reinterprets the ESW phenomenon.

### Recommended placement:

**Option A**: §2.1 subsection (§2.1.X "Relation to Pilot Wave Theory"). Pro: situates the comparison where T_{MΣ} is first defined, giving the reader an immediate conceptual anchor. Con: §2.1 is already a substantial section; adding 1,000+ words may dilute the derivation focus.

**Option B**: Standalone section between Part I and Part II, or as part of §4 (Part III). Pro: gives the comparison room to breathe; the experimental predictions (§7) pair naturally with the "limitations" analysis of Part III. Con: disrupts the current flow.

**Option C**: §6 Discussion subsection. Pro: low-risk, doesn't reorganize existing sections. Con: buries an important structural insight in the discussion; reviewers interested in Bohm may not read that far.

**Recommendation**: Option A (§2.1 subsection) for the structural parallel and key departures (~800 words), with a forward reference to §6 for the experimental predictions and open questions (~400 words). This gives the reader the conceptual anchor without overloading §2.1.

---

## 9. Revision History

- 2026-03-11: Initial working draft (roughing out the structure)
