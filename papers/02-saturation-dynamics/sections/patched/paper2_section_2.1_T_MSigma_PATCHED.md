# §2.1 Derivation of the Cross-Term T_{MΣ} on M × Σ

## Executive Summary

We extend the coherence-frame metric from Paper 1—originally defined on the manifold Σ of coherence frames alone—to the joint manifold M × Σ, where M is spacetime. The state map Φ: M × Σ → PH now encodes how both the local spacetime environment and the choice of coherence frame jointly determine the quantum state. The full metric tensor G_AB decomposes into three blocks: the spacetime-spacetime metric G_{μν}, the frame-frame metric G_{ab} (which recovers Paper 1's Fubini-Study result), and the novel cross-term G_{μa} ≡ T_{MΣ}. This cross-term encodes the coupling between spacetime geometry and coherence-frame geometry, with profound physical meaning: non-zero T_{MΣ} implies that environmental decoherence patterns are encoded geometrically on the joint manifold. When T_{MΣ} → 0, spacetime and coherence decouple, recovering the classical limit. The fundamental object on M × Σ is the quantum geometric tensor **Q_AB = G_AB + i F_AB**, where G_AB is the real Fubini-Study metric and F_AB is the real Berry curvature 2-form.

---

## 2.1.1 The Extended State Map: Φ: M × Σ → PH

### Physical Motivation

In Paper 1, the state map Φ: Σ → PH parameterized how the choice of coherence frame ξ^a ∈ Σ determines a quantum state |ψ(ξ)⟩ ∈ PH. The coherence frame was fixed, and only the frame coordinates varied.

Now we lift this to the joint manifold M × Σ. The spacetime position x^μ ∈ M (with coordinates from some chart on spacetime) determines the **local environment**—the decoherence conditions, the stress-energy tensor, the local matter distribution. The coherence-frame coordinates ξ^a ∈ Σ continue to parameterize the choice of coherence basis.

The joint state map is:

$$\boxed{\Phi: M \times \Sigma \to \mathbb{P}H, \quad (x^\mu, \xi^a) \mapsto |\psi(x, \xi)\rangle}$$

**Eq. 2.1.1**

where the notation $|\psi(x, \xi)\rangle$ is shorthand for $|\psi(x^\mu, \xi^a)\rangle$, understood as an element of projective Hilbert space PH.

### Interpretation of the State Map

The dependence on x^μ encodes **environmentally-induced decoherence**:
- At different spacetime points, the local thermal background, curvature, or matter coupling may differ, changing which coherence structures are preferred.
- The state |ψ(x, ξ)⟩ adapts to the local environment.

The dependence on ξ^a encodes the **choice of coherence basis**:
- For a fixed spacetime point x, varying ξ^a sweeps over different ways to decompose the state into "coherent" vs. "incoherent" components.
- The frame choice reflects the observer's or system's preferred basis in that environment.

**Key physical claim**: The joint state |ψ(x, ξ)⟩ is the fundamental object. Coherence is not intrinsic—it emerges from the pair (x, ξ). Changing x without adjusting ξ may destroy coherence; conversely, adjusting ξ to follow the environmental changes maintains coherence. This is the geometric encoding of decoherence avoidance.

---

## 2.1.2 Extending Derivatives: ∂_A and the Joint Manifold

On the joint manifold M × Σ with coordinates X^A = (x^μ, ξ^a), we define multi-indices:
- Capital Latin indices: A, B, C, ... ∈ {1, 2, ..., dim(M) + dim(Σ)}
- Greek indices (spacetime): μ, ν, ρ, σ ∈ {0, 1, 2, 3} or {1, ..., dim(M)}
- Lowercase Latin indices (frame): a, b, c, ... ∈ {1, 2, ..., dim(Σ)}

The coordinate basis vectors are:

$$\frac{\partial}{\partial X^A} = \begin{cases}
\frac{\partial}{\partial x^\mu} & A \text{ corresponds to } x^\mu \\
\frac{\partial}{\partial \xi^a} & A \text{ corresponds to } \xi^a
\end{cases}$$

**Eq. 2.1.2**

Tangent vectors to M × Σ are:

$$\dot{X}^A = \left(\frac{dx^\mu}{ds}, \frac{d\xi^a}{ds}\right)$$

**Eq. 2.1.3**

where s is a parameter along a curve (e.g., proper time or affine parameter).

---

## 2.1.3 Computing the Full Metric G_AB on M × Σ

The Fubini-Study metric (generalized from Paper 1 to the joint manifold) is:

$$G_{AB} = \text{Re}\left[\langle \partial_A \psi | \partial_B \psi \rangle - \langle \partial_A \psi | \psi \rangle \langle \psi | \partial_B \psi \rangle\right]$$

**Eq. 2.1.4**

where:
- $|\psi\rangle = |\psi(x, \xi)\rangle \in H$ (a representative of the projective state)
- $\partial_A |\psi\rangle = \frac{\partial |\psi(x, \xi)\rangle}{\partial X^A}$ is the tangent vector in Hilbert space along direction A on M × Σ
- $\langle \cdot | \cdot \rangle$ is the Hilbert-space inner product

This metric is **independent of the choice of representative** in PH (i.e., it is gauge-invariant under $|\psi\rangle \to e^{i\alpha(x,\xi)} |\psi\rangle$), as shown in Paper 1.

### Block Decomposition

Since the coordinates split as X^A = (x^μ, ξ^a), the metric tensor decomposes into three blocks:

$$G_{AB} = \begin{pmatrix}
G_{\mu\nu} & G_{\mu a} \\
G_{a\mu} & G_{ab}
\end{pmatrix}$$

**Eq. 2.1.5**

where:
1. **$G_{\mu\nu}$**: the metric component measuring how spacetime coordinates change the state
2. **$G_{ab}$**: the metric component measuring how frame coordinates change the state (recovers Paper 1)
3. **$G_{\mu a} = G_{a\mu}$**: the **cross-term T_{MΣ}** (symmetric by the properties of the Fubini-Study metric)

### Computing G_{μν}

$$G_{\mu\nu} = \text{Re}\left[\langle \partial_\mu \psi | \partial_\nu \psi \rangle - \langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_\nu \psi \rangle\right]$$

**Eq. 2.1.6**

where $\partial_\mu \psi = \frac{\partial |\psi(x, \xi)\rangle}{\partial x^\mu}$.

**Physical meaning**: G_{μν} encodes how moving in spacetime (at fixed coherence frame ξ) changes the quantum state. In regions with strong decoherence gradients (e.g., near a thermal boundary), G_{μν} is large. In uniform environments, G_{μν} may be small or vanish if the environment is "coherence-preserving."

### Computing G_{ab}

$$G_{ab} = \text{Re}\left[\langle \partial_a \psi | \partial_b \psi \rangle - \langle \partial_a \psi | \psi \rangle \langle \psi | \partial_b \psi \rangle\right]$$

**Eq. 2.1.7**

where $\partial_a \psi = \frac{\partial |\psi(x, \xi)\rangle}{\partial \xi^a}$.

**Recovered result**: With x^μ held fixed, this reproduces exactly the metric tensor from Paper 1. It is the Fubini-Study metric on the space of coherence frames for a fixed environment. Paper 1 established that this metric generates the action principle:

$$S[\gamma] = \frac{1}{4D} \int (\dot{\xi}^a - \mathcal{F}^a) G_{ab} (\dot{\xi}^b - \mathcal{F}^b) \, ds$$

**Eq. 2.1.8**

where $\mathcal{F}^a$ are the components of the drift field and D is a coupling constant.

### Computing G_{μa}: The Cross-Term T_{MΣ}

This is the new object we compute:

$$\boxed{T_{\mu a} := G_{\mu a} = \text{Re}\left[\langle \partial_\mu \psi | \partial_a \psi \rangle - \langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_a \psi \rangle\right]}$$

**Eq. 2.1.9**

Similarly:

$$\boxed{T_{a\mu} := G_{a\mu} = \text{Re}\left[\langle \partial_a \psi | \partial_\mu \psi \rangle - \langle \partial_a \psi | \psi \rangle \langle \psi | \partial_\mu \psi \rangle\right]}$$

**Eq. 2.1.10**

**Symmetry**: By the symmetry of the Fubini-Study metric,

$$T_{\mu a} = T_{a\mu}$$

**Eq. 2.1.11**

This follows from the hermiticity of the inner product: $\langle \partial_\mu \psi | \partial_a \psi \rangle = \overline{\langle \partial_a \psi | \partial_\mu \psi \rangle}$.

---

## 2.1.4 Physical Interpretation of T_{MΣ}

### Correlation Between Spacetime and Frame Variations

The cross-term $T_{\mu a}$ measures the extent to which moving in spacetime direction μ produces a change in the state that **correlates** with moving in frame direction a.

More precisely: the inner product $\langle \partial_\mu \psi | \partial_a \psi \rangle$ quantifies the overlap of these two tangent vectors in Hilbert space. When this inner product is large (in magnitude), changing x^μ and changing ξ^a produce similar deformations of the state. When it is small, they produce orthogonal deformations.

The second term $\langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_a \psi \rangle$ subtracts off the "trivial" phase correlation—the part of the overlap that is merely a consequence of the state having a norm. What remains is the genuinely geometric correlation.

### Environmentally-Induced Frame Evolution

**Key insight**: Non-zero $T_{\mu a}$ implies that as we move through spacetime, the "natural" coherence frame changes.

Suppose we move along a path x^μ(s) in spacetime at fixed coherence frame ξ^a(0). The state evolves as $|\psi(x(s), \xi(0))\rangle$. If $T_{\mu a} \neq 0$, then changes in the state induced by x can be partially absorbed by choosing ξ^a(s) adaptively—i.e., by following the frame coordinate that "tracks" the environmental decoherence.

This is the geometric encoding of **environment-induced coherence preservation**: the coherence frame naturally evolves with the environment, as if "riding" on the environmental gradients. When the coherence frame parameter ξ^a couples to spacetime position x^μ through non-zero T_{MΣ}, we say the system is **coherence-coupled to its environment**.

### Magnitude as Coupling Strength

The magnitude of $T_{\mu a}$ (in an appropriately contracted sense) measures the **strength of coherence-spacetime coupling**.

Define the coupling strength:

$$\mathcal{C} := \sqrt{T_{\mu a} T^{\mu a}}$$

**Eq. 2.1.12**

where indices are raised with the inverse metric $G^{AB}$.

- When $\mathcal{C} \to 0$, coherence and spacetime decouple. Paths in spacetime are orthogonal to frame-coordinate changes.
- When $\mathcal{C}$ is large, spacetime and frame coordinates are highly intertwined. Environmental variations strongly modulate coherence.

### The Classical Limit: T_{MΣ} → 0

In the classical limit (ℏ → 0 or equivalently, in the regime where decoherence dominates), the coherence frame becomes irrelevant—there is only one "classical" observable basis. In this limit, $T_{MΣ} \to 0$, and the metric block-diagonalizes:

$$G_{AB} \to \begin{pmatrix}
G_{\mu\nu}^{\text{cl}} & 0 \\
0 & G_{ab}^{\text{cl}} \to 0
\end{pmatrix}$$

**Eq. 2.1.13**

The cross-term vanishes, spacetime and coherence decouple, and we recover purely classical dynamics on spacetime.

---

## 2.1.5 The Berry Connection, Curvature, and the Quantum Geometric Tensor Q_AB

We now introduce the fundamental object on M × Σ: the **quantum geometric tensor** Q_AB, which unifies the metric and Berry structures.

### The Berry Connection (1-Form)

The Berry connection is a differential 1-form on M × Σ:

$$A_A = i\langle \psi | \partial_A \psi \rangle$$

**Eq. 2.1.14**

This decomposes into spacetime and frame parts:

$$A_\mu = i\langle \psi | \partial_\mu \psi \rangle, \quad A_a = i\langle \psi | \partial_a \psi \rangle$$

**Eq. 2.1.15**

### The Berry Curvature (2-Form)

The Berry curvature is the exterior derivative of the connection:

$$F_{AB} = \partial_A A_B - \partial_B A_A = \text{Im}\left[\langle \partial_A \psi | \partial_B \psi \rangle - \langle \partial_A \psi | \psi \rangle \langle \psi | \partial_B \psi \rangle\right]$$

**Eq. 2.1.16**

By construction, F_{AB} is **antisymmetric** (F_{AB} = -F_{BA}) and **gauge-invariant** under $|\psi\rangle \to e^{i\alpha(x,\xi)} |\psi\rangle$.

The cross-term in the Berry curvature is:

$$\boxed{F_{\mu a} = \text{Im}\left[\langle \partial_\mu \psi | \partial_a \psi \rangle - \langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_a \psi \rangle\right]}$$

**Eq. 2.1.17**

Note: F_{aμ} = -F_{μa}.

### The Quantum Geometric Tensor Q_AB

The complete quantum geometric structure is captured by:

$$\boxed{Q_{AB} = G_{AB} + i F_{AB}}$$

**Eq. 2.1.18**

where:
- **G_{AB}** (symmetric, real) is the Fubini-Study metric
- **F_{AB}** (antisymmetric, real) is the Berry curvature

Q_AB is **gauge-invariant** as a whole, since both G_AB and F_AB are gauge-invariant. This is the fundamental tensor on M × Σ. It replaces the previous ambiguous use of T_AB.

### Berry Phase and Stokes' Theorem

When traversing a closed loop γ in M × Σ, the geometric (Berry) phase accumulated is given by **Stokes' theorem**:

$$\Phi_{\text{Berry}} = \oint_\gamma A_A dX^A = \int\int_\Sigma F_{AB} dX^A \wedge dX^B$$

**Eq. 2.1.19**

where Σ is any surface bounded by γ. The two sides are equivalent by the generalized Stokes theorem.

For a loop in the (x^μ, ξ^a) space:

$$\Phi_{\text{Berry}} = \oint_\gamma \left[A_\mu dx^\mu + A_a d\xi^a\right]$$

$$= \int\int_\Sigma \left[F_{\mu\nu} dx^\mu \wedge dx^\nu + F_{\mu a} dx^\mu \wedge d\xi^a + F_{a\mu} d\xi^a \wedge dx^\mu + F_{ab} d\xi^a \wedge d\xi^b\right]$$

**Eq. 2.1.20**

The cross-term **F_{μa} dx^μ ∧ dξ^a** contributes when the loop includes simultaneous variations in both spacetime and frame coordinates.

**Physical meaning**: Moving in spacetime while also adapting the coherence frame picks up a phase that depends on the path taken—the signature of a non-trivial connection on M × Σ. This phase has consequences for quantum evolution: it can induce observable shifts in interference patterns or energy-level splittings.

---

## 2.1.6 Gauge Transformations and Preservation of Structure

Under a local gauge transformation $|\psi\rangle \to e^{i\alpha(x,\xi)} |\psi\rangle$ where α is an arbitrary real function on M × Σ:

**The Fubini-Study metric is invariant:**

$$G'_{AB} = G_{AB}$$

**Eq. 2.1.21**

(This is the key property that allows G_{AB} to be well-defined on projective Hilbert space PH.)

**The Berry connection transforms homogeneously:**

$$A'_A = A_A + \partial_A \alpha$$

**Eq. 2.1.22**

**The Berry curvature is invariant:**

$$F'_{AB} = F_{AB}$$

**Eq. 2.1.23**
Here “gauge” refers to the projective phase freedom $|\\psi\\rangle\\to e^{i\\alpha(x,\\xi)}|\\psi\\rangle$ on PH; no additional dynamical Yang-Mills gauge field is introduced at this stage.
This is immediate from the definition F_{AB} = ∂_A A_B − ∂_B A_A, since second derivatives commute and ∂_A(∂_B α) − ∂_B(∂_A α) = 0.

**Consequence for Q_AB**: The quantum geometric tensor Q_{AB} transforms covariantly in the sense that G is invariant and F is invariant, so Q_{AB} itself is gauge-invariant. This is the geometric advantage of the Q_AB formalism over previous notation.

---

## 2.1.7 Metric Symmetry, Index Structure, and Positivity

### Metric Symmetry

The Fubini-Study construction (Eq. 2.1.4) is symmetric:

$$G_{AB} = G_{BA}$$

**Eq. 2.1.24**

This is immediately clear from the inner product: $\langle \partial_A \psi | \partial_B \psi \rangle = \overline{\langle \partial_B \psi | \partial_A \psi \rangle}$ is hermitian.

For the cross-term in particular:

$$T_{\mu a} = T_{a\mu}$$

**Eq. 2.1.25**

### Index Raising and the Inverse Metric

We can raise and lower indices using the full metric:

$$T^{\mu a} = G^{\mu B} G^{aC} T_{BC}$$

**Eq. 2.1.26**

**Important note**: For a non-block-diagonal metric (T_{MΣ} ≠ 0), this sum runs over all indices B, C ∈ {1, ..., dim(M) + dim(Σ)}, not just the spacetime or frame sub-blocks. Explicit block expansion deferred to §2.2. The full inverse metric is:

$$G^{AB} = \begin{pmatrix}
(G - H G^{-1}_{ab} H^T)^{-1} & -(G - H G^{-1}_{ab} H^T)^{-1} H G^{-1}_{ab} \\
-G^{-1}_{ab} H^T (G - H G^{-1}_{ab} H^T)^{-1} & G^{-1}_{ab} + G^{-1}_{ab} H^T (G - H G^{-1}_{ab} H^T)^{-1} H G^{-1}_{ab}
\end{pmatrix}$$

**Eq. 2.1.27**

where G = G_{μν}, H = T_{MΣ} = G_{μa}, and G_{ab} is the frame-metric block. The detailed computation is deferred to §2.2.

### Positivity and Cauchy-Schwarz

The Fubini-Study metric G_{AB} is **positive semi-definite** as a metric on the manifold M × Σ, with kernel spanned by trivial phase directions. This ensures that physical distances are non-negative.

The cross-term T_{μa} satisfies Cauchy-Schwarz bounds:

$$|T_{\mu a}|^2 \leq G_{\mu\mu} \cdot G_{aa}$$

**Eq. 2.1.28**

(This is Cauchy-Schwarz in the Hilbert-space inner product.)

---

## 2.1.8 Computing T_{MΣ} Explicitly: A Model Example

To make Eq. 2.1.9 concrete, consider a simple model:

### Setup: Two-Level System in a Thermal Environment

Let the Hilbert space be $\mathcal{H} = \mathbb{C}^2$, with basis states $|0\rangle, |1\rangle$ (ground and excited states).

The coherence-frame manifold Σ is parameterized by a single angle ξ ∈ [0, 2π), so dim(Σ) = 1. The frame choice corresponds to rotating the basis:

$$|+_\xi\rangle = \cos(\xi/2) |0\rangle + e^{i\phi} \sin(\xi/2) |1\rangle$$

**Eq. 2.1.29**

where φ is a fixed phase.

Spacetime M is one-dimensional (time only), with coordinate x^0 = t.

The state map is:

$$|\psi(t, \xi)\rangle = \cos(\xi/2) e^{i E_0 t/\hbar} |0\rangle + e^{i\phi} \sin(\xi/2) e^{i(E_1 t/\hbar + \gamma_0 t)} |1\rangle$$

**Eq. 2.1.30**

where:
- E_0, E_1 are the energy eigenvalues
- **γ₀ is a constant decoherence rate** (uniform environment)

**Note**: We keep γ₀ constant in this toy model to make the calculation tractable. When the decoherence rate varies with spacetime position (γ = γ(x)), the cross-term becomes non-zero. The position-dependent case is deferred to §2.2.

### Result: Uniform Environment ⟹ Zero Cross-Term

A direct calculation of the Fubini-Study cross-term (Eq. 2.1.9) for this model gives:

$$T_{t\xi} = \text{Re}\left[\langle \partial_t \psi | \partial_\xi \psi \rangle - \langle \partial_t \psi | \psi \rangle \langle \psi | \partial_\xi \psi \rangle\right]$$

**Eq. 2.1.31**

**For constant γ₀** (uniform environment, $\partial_t \gamma = 0$), this evaluates to:

$$T_{t\xi} = 0$$

**Eq. 2.1.32**

The intermediate inner-product algebra is straightforward and omitted here. The key observation is that when all time-dependence enters the state only through global phase factors (as it does when γ₀ is constant), the Fubini-Study projection subtracts out all phase correlations, leaving zero geometric coupling.

**Interpretation**: With uniform decoherence (constant γ₀), spacetime and frame degrees of freedom decouple. The coherence frame does not need to evolve as we move through time.

**When γ varies with spacetime position** (γ = γ(x)), additional terms arise from $\partial_t \gamma \neq 0$, producing non-zero T_{tξ}. The position-dependent case, which captures the physically interesting regime of environment-induced frame evolution, is deferred to §2.2.

---

## 2.1.9 Connection to the Inverse Metric and Action Principle

### Block Decomposition of the Inverse Metric

Given the block form Eq. 2.1.5, the inverse metric $G^{AB}$ satisfies:

$$G^{AB} G_{BC} = \delta^A_C$$

**Eq. 2.1.33**

When T_{MΣ} is small (weak coupling), the inverse metric simplifies approximately:

$$G^{AB} \approx \begin{pmatrix}
G^{-1}_{\mu\nu} & -G^{-1}_{\mu\nu} T_{\nu a} G^{-1ab} \\
-G^{-1ab} T_{b\mu} G^{-1\mu\nu} & G^{-1}_{ab}
\end{pmatrix}$$

**Eq. 2.1.34 (leading order in $T_{M\\Sigma}$)**

to leading order in T_{MΣ}. The full block-matrix inverse is given by the Schur-complement block-inverse formula and is deferred to §2.2.

### Extended Action Principle

The action on M × Σ generalizes the action from Paper 1 (Eq. 2.1.8):

**Notation**: $A_A$ denotes the Berry connection (Eq. 2.1.14); $\mathcal{F}^A = (\mathcal{F}^\mu, \mathcal{F}^a)$ denotes the drift field in the action (the deterministic forcing from the environment, as in Paper 1). These are distinct objects.

$$S[\mathbf{X}] = \frac{1}{4D} \int_0^1 \left[\left(\dot{x}^\mu - \mathcal{F}^\mu\right) G_{\mu\nu} \left(\dot{x}^\nu - \mathcal{F}^\nu\right) + 2\left(\dot{x}^\mu - \mathcal{F}^\mu\right) T_{\mu a} \left(\dot{\xi}^a - \mathcal{F}^a\right) + \left(\dot{\xi}^a - \mathcal{F}^a\right) G_{ab} \left(\dot{\xi}^b - \mathcal{F}^b\right)\right] ds$$

**Eq. 2.1.35**

where $\mathbf{X}(s) = (x^\mu(s), \xi^a(s))$ is a path on M × Σ, $\mathcal{F}^A = (\mathcal{F}^\mu, \mathcal{F}^a)$ are the components of the drift field, and D is the coupling constant from Paper 1.

The **cross-term 2 T_{μa} $\left(\dot{x}^\mu - \mathcal{F}^\mu\right) \left(\dot{\xi}^a - \mathcal{F}^a\right)$** couples the spacetime and frame velocities. When T_{MΣ} is non-zero, there is an energetic "preference" for simultaneous motion in spacetime and frame directions.

The quasipotential becomes:

$$V_{\text{eff}}(x, \xi) = \inf_\gamma S[\gamma]$$

**Eq. 2.1.36**

where the infimum is over all paths connecting a reference point to (x, ξ). This potential encodes the combined effect of spacetime decoherence and coherence-frame cost.

---

## 2.1.10 Kähler Structure and Complex Coordinates

**Note on Kähler geometry**: The Fubini-Study metric on PH is Kähler when PH is viewed as a complex manifold. However, the parameter manifold M × Σ presented here is real. Whether the Kähler structure on projective Hilbert space descends to a Kähler structure on the real manifold M × Σ depends on the holomorphicity properties of the state map Φ(x, ξ), which we do not assume in the general case.

For specific physical systems (e.g., those with holomorphic coherence frames), Kähler structure may be present. However, without explicit holomorphicity assumptions, we work with the real Fubini-Study metric G_{AB} directly. The connection between complex coordinates on PH and real coordinates on M × Σ is a topic for future investigations; we defer detailed treatment to future work.

---

## 2.1.11 Connection to the KK-Cone: Warp-Factor Modulation of T_{MΣ}

[Note: Full treatment deferred to §7. Here we sketch the key point.]

For warped-geometry coupling, we adopt the canonical Paper-2 bulk metric (§4.0):

$$ds^2_{(5)} = -dz^2 + dr^2 + A(r,z)^2 \, \gamma_{ij} d\theta^i d\theta^j$$

**Eq. 2.1.37**

where $z$ is the brane-normal coordinate, $r$ is the radial direction, $A(r,z)$ is the warp factor, and $\gamma_{ij}$ is the unit round metric on S³ (parameterized via the Hopf fibration as in §4.0). All scaling statements below are consequences to be derived from this form.

### Effect on Spacetime Derivatives: Scaling Ansatz

In the warped geometry, distances along spacetime directions are rescaled by the warp factor. We express this through an **ansatz** on how spacetime derivatives scale:

$$\partial_\mu \psi \to A(x, z)^{-1} \partial_\mu^{(0)} \psi$$

**Eq. 2.1.38**

where $\partial_\mu^{(0)}$ is the derivative in flat space, and this scaling reflects the geometric rescaling of tangent vectors in the warped frame.

### Warp-Factor Modulation: Hypothesis

Under the above ansatz, we hypothesize that the cross-term T_{μa} inherits the warp-factor dependence:

$$T_{\mu a}(x, z, \xi) \sim A(x, z)^{-2} T_{\mu a}^{(flat)}(\xi)$$

**Eq. 2.1.39**

where $T_{\mu a}^{(flat)}$ is the cross-term computed in flat space.

**Status**: This is an **ansatz that requires verification** in the full equations of motion (developed in §2.2 and tested in §7). The A^{-2} scaling follows dimensionally from the A^{-1} scaling of derivatives, but actual verification requires:
1. Computing the full covariant derivatives ∇_μ ψ in the warped metric
2. Solving the equations of motion on M × Σ in the KK-cone geometry
3. Checking whether the effective action reproduces this scaling

**No quantitative scaling law for $T_{\mu a}$ is claimed here until derived from covariant equations in §7.**

### Physical Interpretation in the KK-Cone

If this scaling hypothesis is confirmed, the consequences are profound:

- In regions where A(x, z) → 0 (the "deep throat" of the cone), spacetime distances dilate enormously, and the coherence-spacetime coupling becomes **suppressed** (T_{MΣ} → 0).
- Conversely, in regions where A(x, z) is large (the bulk), the coupling strengthens.

This warp-factor modulation would provide a geometric mechanism by which warped geometry protects quantum coherence—a phenomenon of potential relevance to quantum information in extra-dimensional scenarios. However, confirmation requires the detailed calculations in §7.

---

## 2.1.12 Summary and Key Results

### The Three Blocks of the Full Metric

On M × Σ, the Fubini-Study metric tensor G_{AB} decomposes into three physically distinct components:

1. **G_{μν}** (spacetime-spacetime): The gradient of the state as we move through spacetime at fixed coherence frame. It quantifies environmental decoherence variation.

2. **G_{ab}** (frame-frame): The Fubini-Study metric on the coherence-frame manifold Σ (recovered from Paper 1). It measures the cost of changing the coherence basis.

3. **T_{MΣ} = G_{μa}** (cross-term): The coupling between spacetime position and coherence-frame choice. Non-zero T_{MΣ} indicates that the natural coherence frame evolves with the environment.

### Physical Meaning of T_{MΣ}

- **Encodes environment-induced coherence evolution**: As spacetime position changes, the optimal coherence frame changes. T_{MΣ} measures this coupling strength.
- **Bounds the decoherence-avoidance pathway**: The action principle (Eq. 2.1.35) shows that maintaining coherence while moving through a spatially-varying environment requires work proportional to T_{MΣ}.
- **Vanishes in the classical limit**: When decoherence dominates (ℏ → 0), T_{MΣ} → 0, and spacetime and coherence decouple.
- **Is modulated by warp factors**: In extra-dimensional scenarios with warped geometry, the hypothesis predicts T_{MΣ} is suppressed in high-curvature regions, effectively "protecting" coherence (verification in §7).

### The Quantum Geometric Tensor Q_AB

The complete quantum geometric structure is captured by:

$$Q_{AB} = G_{AB} + i F_{AB}$$

where:
- **G_{AB}** (symmetric, real) is the Fubini-Study metric—gauge-invariant
- **F_{AB}** (antisymmetric, real) is the Berry curvature—gauge-invariant

The cross-terms are:
- **G_{μa} = T_{MΣ}**: the metric cross-term (symmetric)
- **F_{μa}**: the Berry curvature cross-term (antisymmetric)

Both are gauge-invariant. Q_AB is the fundamental object on M × Σ, replacing previous ambiguous notation (T_AB was used both for the full tensor and for individual cross-terms).

### The Berry Phase and Connection

The Berry phase acquired on a closed loop γ in M × Σ is:

$$\Phi_{\text{Berry}} = \oint_\gamma A_A dX^A = \int\int_\Sigma F_{AB} dX^A \wedge dX^B$$

where A_A is the Berry connection 1-form and F_{AB} is the Berry curvature 2-form. The cross-term F_{μa} contributes whenever the loop involves simultaneous spacetime-frame motion.

---

## 2.1.13 Outlook

With T_{MΣ} now characterized on the joint manifold M × Σ, the next sections develop:

- **§2.2**: Equations of motion on M × Σ derived from the action principle, showing how spacetime dynamics couples to coherence-frame evolution. Full treatment of index raising and the inverse metric.
- **§3**: Specific solutions in symmetric spacetimes (FLRW, Schwarzschild), computing G_{μν}, G_{ab}, and T_{MΣ} explicitly.
- **§7**: Full treatment of the KK-Cone geometry, including verification of the warp-factor modulation hypothesis and the emergence of low-energy effective physics.

---

## References to Paper 1

This section fulfills the promise made in Paper 1 (line 162, 558) to develop "the complete decomposition into M and Σ coordinates, the cross-term T_{MΣ}." The extension from Σ alone to M × Σ is natural: coherence is genuinely frame-relative and environment-dependent, and the joint manifold M × Σ is the correct arena for describing this dependence geometrically.

The action principle (2.1.35) extends the action from Paper 1 by including spacetime coordinates x^μ as dynamical variables on equal footing with coherence-frame coordinates ξ^a. The coupling term 2 T_{MΣ} \\dot{x}^μ \\dot{ξ}^a is the new physics: it enforces that efficient coherence-preserving pathways through spacetime are those that simultaneously adapt the coherence frame.

The quantum geometric tensor Q_{AB} = G_{AB} + i F_{AB} unifies the metric and Berry structures in a single gauge-invariant object, providing a cleaner mathematical framework than previous notation.

**Section status**: Blocking items cleared except full covariant scaling derivation and nonuniform-environment worked example, both intentionally deferred (to §7 and §2.2, respectively).
