# §2.1 Derivation of the Cross-Term T_{MΣ} on M × Σ

## Executive Summary

We extend the coherence-frame metric from Paper 1—originally defined on the manifold Σ of coherence frames alone—to the joint manifold M × Σ, where M is spacetime. The state map Φ: M × Σ → PH now encodes how both the local spacetime environment and the choice of coherence frame jointly determine the quantum state. The full metric tensor G_AB decomposes into three blocks: the spacetime-spacetime metric G_{μν}, the frame-frame metric G_{ab} (which recovers Paper 1's Fubini-Study result), and the novel cross-term G_{μa} ≡ T_{MΣ}. This cross-term encodes the coupling between spacetime geometry and coherence-frame geometry, with profound physical meaning: non-zero T_{MΣ} implies that environmental decoherence patterns are encoded geometrically on the joint manifold. When T_{MΣ} → 0, spacetime and coherence decouple, recovering the classical limit.

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

**Nomenclature convention used in this section** (to align with standard quantum-geometry usage):
- `A_A`: Berry connection one-form,
- `\Omega_{AB}`: Berry curvature two-form,
- `b^A`: effective drift field in the quasipotential action.

### Block Decomposition

Since the coordinates split as X^A = (x^μ, ξ^a), the metric tensor decomposes into three blocks:

$$G_{AB} = \begin{pmatrix}
G_{\mu\nu} & G_{\mu a} \\
G_{a\mu} & G_{ab}
\end{pmatrix}$$

**Eq. 2.1.5**

where:
1. **$G_{\mu\nu}$**: the pullback information-metric component measuring how spacetime coordinates change the state
2. **$G_{ab}$**: the metric component measuring how frame coordinates change the state (recovers Paper 1)
3. **$G_{\mu a} = G_{a\mu}$**: the **cross-term T_{MΣ}** (symmetric by the properties of the Fubini-Study metric)

### Computing G_{μν}

$$G_{\mu\nu} = \text{Re}\left[\langle \partial_\mu \psi | \partial_\nu \psi \rangle - \langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_\nu \psi \rangle\right]$$

**Eq. 2.1.6**

where $\partial_\mu \psi = \frac{\partial |\psi(x, \xi)\rangle}{\partial x^\mu}$.

**Physical meaning**: G_{μν} encodes how moving in spacetime (at fixed coherence frame ξ) changes the quantum state. This is an information-geometric pullback block on state space, not the Lorentzian spacetime metric tensor used in GR field equations. In regions with strong decoherence gradients (e.g., near a thermal boundary), G_{μν} is large. In uniform environments, G_{μν} may be small or vanish if the environment is "coherence-preserving."

### Computing G_{ab}

$$G_{ab} = \text{Re}\left[\langle \partial_a \psi | \partial_b \psi \rangle - \langle \partial_a \psi | \psi \rangle \langle \psi | \partial_b \psi \rangle\right]$$

**Eq. 2.1.7**

where $\partial_a \psi = \frac{\partial |\psi(x, \xi)\rangle}{\partial \xi^a}$.

**Recovered result**: With x^μ held fixed, this reproduces exactly the metric tensor T_AB from Paper 1. It is the Fubini-Study metric on the space of coherence frames for a fixed environment. Paper 1 established that this metric generates the action principle:

$$S[\gamma] = \frac{1}{4D} \int (\dot{\xi}^a - b^a) G_{ab} (\dot{\xi}^b - b^b) \, ds$$

**Eq. 2.1.8**

where `b^a` is the effective drift field on frame space (obtained after projection/coarse-graining of microscopic dynamics) and D is a coupling constant.

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

## 2.1.5 Berry Connection and Mixed Curvature Term

Define the quantum geometric tensor on `M×Σ` by

$$Q_{AB} := \langle \partial_A \psi | \partial_B \psi \rangle - \langle \partial_A \psi | \psi \rangle \langle \psi | \partial_B \psi \rangle.$$

**Eq. 2.1.14**

Its real part gives the pullback Fubini-Study metric:

$$G_{AB} = \mathrm{Re}(Q_{AB}),$$

and its imaginary part gives the Berry curvature:

$$\Omega_{AB} = 2\,\mathrm{Im}(Q_{AB}).$$

**Eq. 2.1.15**

The mixed curvature block is therefore

$$\boxed{\Omega_{\mu a} = 2\,\mathrm{Im}\!\left[\langle \partial_\mu \psi | \partial_a \psi \rangle - \langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_a \psi \rangle\right].}$$

**Eq. 2.1.16**

Introduce the Berry connection one-form

$$A_A := i\langle \psi|\partial_A\psi\rangle,$$

with curvature

$$\Omega_{AB} = \partial_A A_B - \partial_B A_A.$$

**Eq. 2.1.17**

### Geometric Phase Acquisition in Joint Motion

Consider a closed loop `γ` in `M×Σ` parameterized by `s∈[0,1]`:

$$\gamma: s \mapsto (x^\mu(s), \xi^a(s)).$$

**Eq. 2.1.18**

The Berry phase is computed from the connection (line integral) or, equivalently, from the curvature (surface integral):

$$\Phi_{\text{Berry}} = \oint_{\gamma} A_A\,dX^A = \frac{1}{2}\iint_{\Sigma_\gamma} \Omega_{AB}\,dX^A\wedge dX^B.$$

**Eq. 2.1.19**

In components, the mixed contribution appears through `\Omega_{\mu a}\,dx^\mu\wedge d\xi^a`. This term contributes when the loop has simultaneous variation in spacetime and frame coordinates.

**Physical meaning**: moving in spacetime while adapting the coherence frame can accumulate a path-dependent geometric phase, controlled by the mixed curvature sector `\Omega_{\mu a}`.

---

## 2.1.6 Symmetry, Index Structure, and Verification

### Metric Symmetry

The Fubini-Study construction (Eq. 2.1.4) is symmetric:

$$G_{AB} = G_{BA}$$

**Eq. 2.1.20**

This is immediately clear from the inner product: $\langle \partial_A \psi | \partial_B \psi \rangle = \overline{\langle \partial_B \psi | \partial_A \psi \rangle}$ is hermitian.

For the cross-term in particular:

$$T_{\mu a} = T_{a\mu}$$

**Eq. 2.1.21**

We can raise and lower indices using the full metric:

$$T^{\mu a} = G^{\mu\nu} G^{ab} T_{\nu b}$$

**Eq. 2.1.22**

where $G^{AB}$ is the inverse of the metric tensor (to be computed from the block form).

### Positivity

The Fubini-Study metric G_{AB} is **positive semi-definite** as a metric on the manifold M × Σ, with kernel spanned by trivial phase directions. This ensures that physical distances are non-negative.

The cross-term T_{MΣ} is bounded by the geometric mean of the "self-couplings":

$$|T_{\mu a}|^2 \leq G_{\mu\mu} \cdot G_{aa}$$

**Eq. 2.1.23**

(This is Cauchy-Schwarz in the Hilbert-space inner product.)

### Gauge Invariance

Under a gauge transformation $|\psi\rangle \to e^{i\alpha(x,\xi)} |\psi\rangle$ where α is an arbitrary real function on M × Σ, the metric G_{AB} is invariant:

$$G'_{AB} = G_{AB}$$

**Eq. 2.1.24**

(This is the key property that allows G_{AB} to be well-defined on projective Hilbert space PH.)

For the Berry objects:

$$A'_A = A_A + \partial_A \alpha,$$

$$\Omega'_{AB} = \Omega_{AB}.$$

**Eq. 2.1.25**

So the connection one-form is gauge-dependent, while the curvature two-form (including mixed block $\Omega_{\mu a}$) is gauge-invariant.

---

## 2.1.7 Computing T_{MΣ} in a Consistent Dephasing Model

To make Eq. 2.1.9 concrete without conflating decoherence with pure phase evolution, use a mixed-state dephasing channel.

### Setup: Two-Level System with Spatially Varying Dephasing

Let `\mathcal{H}=\mathbb{C}^2` with basis `|0\rangle, |1\rangle`, and let `x^\mu=(t,\mathbf{x})` denote spacetime coordinates. For pure dephasing, write

$$\rho(x,\xi)=
\begin{pmatrix}
p(\xi) & c(\xi)\,e^{-i\omega t}\,e^{-\Gamma(x)}\\
c^*(\xi)\,e^{+i\omega t}\,e^{-\Gamma(x)} & 1-p(\xi)
\end{pmatrix},$$

where `\Gamma(x)\ge 0` is the integrated decoherence functional (not a phase term).

### Mixed-State Geometry

In this regime, the natural information geometry is the Bures metric (equivalently the quantum Fisher metric), not the pure-state Fubini-Study form. Denote the pullback metric by

$$\mathcal{G}_{AB}^{(\mathrm{Bures})}(\rho) = \frac{1}{4}\,F^{(Q)}_{AB}(\rho),$$

and define the mixed-sector cross-term by

$$T_{\mu a}^{(\mathrm{mix})}:=\mathcal{G}_{\mu a}^{(\mathrm{Bures})}.$$

### Interpretation

`T_{\mu a}^{(\mathrm{mix})}` is nonzero when spacetime gradients of the dephasing functional (`\partial_\mu\Gamma`) correlate with frame gradients (`\partial_a p,\partial_a c`). This is the mathematically consistent statement of environment-frame coupling in an open-system setting.

In particular, if `\Gamma` is spacetime-uniform and frame sensitivity is trivial, the mixed term vanishes; if either sector varies, `T_{\mu a}^{(\mathrm{mix})}` can be nonzero and drives adaptive frame evolution.

---

## 2.1.8 Connection to the Inverse Metric and Action Principle

### Block Decomposition of the Inverse Metric

Given the block-diagonal form Eq. 2.1.5, the inverse metric $G^{AB}$ satisfies:

$$G^{AB} G_{BC} = \delta^A_C$$

**Eq. 2.1.34**

In block form:

$$G^{AB} = \begin{pmatrix}
(G - H G^{-1}_{ab} H^T)^{-1} & -(G - H G^{-1}_{ab} H^T)^{-1} H G^{-1}_{ab} \\
-G^{-1}_{ab} H^T (G - H G^{-1}_{ab} H^T)^{-1} & G^{-1}_{ab} + G^{-1}_{ab} H^T (G - H G^{-1}_{ab} H^T)^{-1} H G^{-1}_{ab}
\end{pmatrix}$$

**Eq. 2.1.35**

where G = G_{μν}, H = G_{μa} = T_{MΣ}, and $G_{ab}$ is the frame-metric block.

When T_{MΣ} is small (weak coupling), the inverse metric simplifies approximately:

$$G^{AB} \approx \begin{pmatrix}
G^{-1}_{\mu\nu} & -G^{-1}_{\mu\nu} T_{\nu a} G^{-1ab} \\
-G^{-1ab} T_{b\mu} G^{-1\mu\nu} & G^{-1}_{ab}
\end{pmatrix}$$

**Eq. 2.1.36**

to leading order in T_{MΣ}.

### Extended Action Principle

The action on M × Σ generalizes the action from Paper 1 (Eq. 2.1.8):

$$S[\mathbf{X}] = \frac{1}{4D} \int_0^1 \left[\left(\dot{x}^\mu - b^\mu\right) G_{\mu\nu} \left(\dot{x}^\nu - b^\nu\right) + 2\left(\dot{x}^\mu - b^\mu\right) T_{\mu a} \left(\dot{\xi}^a - b^a\right) + \left(\dot{\xi}^a - b^a\right) G_{ab} \left(\dot{\xi}^b - b^b\right)\right] ds$$

**Eq. 2.1.37**

where $\mathbf{X}(s) = (x^\mu(s), \xi^a(s))$ is a path on M × Σ, $b^A=(b^\mu,b^a)$ is the effective drift field, and D is the coupling constant from Paper 1.

The **cross-term 2 T_{\mu a} \left(\dot{x}^\mu - b^\mu\right) \left(\dot{\xi}^a - b^a\right)** couples the spacetime and frame velocities. When T_{MΣ} is non-zero, there is an energetic "preference" for simultaneous motion in spacetime and frame directions.

The quasipotential becomes:

$$V_{\text{eff}}(x, \xi) = \inf_\gamma S[\gamma]$$

**Eq. 2.1.38**

where the infimum is over all paths connecting a reference point to (x, ξ). This potential encodes the combined effect of spacetime decoherence and coherence-frame cost.

---

## 2.1.9 Symmetry Properties and Preservation Under Gauge Transformations

### The Fubini-Study Metric is Kähler

Although we work on a real manifold M × Σ here, if we complexify to allow Σ to carry complex structure (as it can in more general formulations), the Fubini-Study metric G_{AB} is **Kähler**—it is the metric induced from a Kähler potential.

The standard Fubini-Study potential is:

$$K(x, \xi; \bar{x}, \bar{\xi}) = \log \langle \psi(x, \xi) | \psi(x, \xi) \rangle$$

**Eq. 2.1.39**

and in complex coordinates $(z^I,\bar z^{\bar J})$ the metric is:

$$G_{I\bar J} = \partial_I \partial_{\bar J} K.$$

**Eq. 2.1.40**

In the real-coordinate presentation used in this section, we work directly with the pullback definition Eq. 2.1.4; the Kähler statement is a consistency check in the complexified chart.

### Preservation Under Gauge Transformations

The metric part is invariant under gauge transformations:

$$G'_{AB} = G_{AB}$$

**Eq. 2.1.41**

and the Berry connection/curvature transformation is given in Eq. 2.1.25.

---

## 2.1.10 Connection to the KK-Cone: Warp-Factor Modulation of T_{MΣ}

[Note: Full treatment deferred to §7. Here we sketch the key point.]

When spacetime M is replaced by the 5-dimensional Kaluza-Klein cone with warped geometry, the metric is:

$$ds^2 = A(r, z)^2 \left[dx_\mu dx^\mu + dz^2\right]$$

**Eq. 2.1.43**

where A(r, z) is the warp factor.

### Effect on Spacetime Derivatives

The derivatives with respect to spacetime coordinates become:

$$\partial_\mu \psi \to A(x, z)^{-1} \partial_\mu \psi$$

**Eq. 2.1.44**

(in the sense that distances along μ directions are rescaled by the warp factor).

Consequently, the cross-term T_{μa} inherits the warp-factor dependence:

$$T_{\mu a}(x, z, \xi) \propto A(x, z)^{-2} T_{\mu a}^{(0)}(\xi)$$

**Eq. 2.1.45**

where $T_{\mu a}^{(0)}$ is a "bare" cross-term.

### Physical Interpretation in the KK-Cone

In regions where A(x, z) → 0 (the "deep throat" of the cone), spacetime distances dilate enormously, and the coherence-spacetime coupling becomes **suppressed** (T_{MΣ} → 0). Conversely, in regions where A(x, z) is large, the coupling strengthens.

This warp-factor modulation has immediate physical consequences:
- In the bulk (large A), coherence is strongly coupled to the environment.
- In the throat (small A), spacetime is so curved that quantum coherence effects decouple from environmental variations.

This is the geometric mechanism by which warped geometry protects quantum coherence—a phenomenon of potential relevance to quantum information in extra-dimensional scenarios.

---

## 2.1.11 Summary and Key Results

### The Three Blocks of the Full Metric

On M × Σ, the Fubini-Study metric tensor G_{AB} decomposes into three physically distinct components:

1. **G_{μν}** (spacetime-indexed pullback block): The gradient of the state as we move through spacetime at fixed coherence frame. It quantifies environmental decoherence variation in information geometry.

2. **G_{ab}** (frame-frame): The Fubini-Study metric on the coherence-frame manifold Σ (recovered from Paper 1). It measures the cost of changing the coherence basis.

3. **T_{MΣ} = G_{μa}** (cross-term): The coupling between spacetime position and coherence-frame choice. Non-zero T_{MΣ} indicates that the natural coherence frame evolves with the environment.

### Physical Meaning of T_{MΣ}

- **Encodes environment-induced coherence evolution**: As spacetime position changes, the optimal coherence frame changes. T_{MΣ} measures this coupling strength.
- **Bounds the decoherence-avoidance pathway**: The action principle (Eq. 2.1.37) shows that maintaining coherence while moving through a spatially-varying environment requires work proportional to T_{MΣ}.
- **Vanishes in the classical limit**: When decoherence dominates (ℏ → 0), T_{MΣ} → 0, and spacetime and coherence decouple.
- **Is modulated by warp factors**: In extra-dimensional scenarios with warped geometry, T_{MΣ} is suppressed in high-curvature regions, effectively "protecting" coherence.

### The Mixed Berry Curvature Cross-Term Ω_{μa}

The imaginary part of the quantum geometric tensor defines curvature `Ω_{μa}`, which controls geometric (Berry) phase accumulation for joint spacetime/frame loops. These phases are observable in interference shifts and level splittings.

---

## 2.1.12 Outlook

With T_{MΣ} now characterized on the joint manifold M × Σ, the next sections develop:

- **§2.2**: Equations of motion on M × Σ derived from the action principle, showing how spacetime dynamics couples to coherence-frame evolution.
- **§3**: Specific solutions in symmetric spacetimes (FLRW, Schwarzschild), computing G_{μν}, G_{ab}, and T_{MΣ} explicitly.
- **§7**: Full treatment of the KK-Cone geometry, including the warp-factor modulation of T_{MΣ} and the emergence of low-energy effective physics.

---

## References to Paper 1

This section fulfills the promise made in Paper 1 (line 162, 558) to develop "the complete decomposition into M and Σ coordinates, the cross-term T_{MΣ}." The extension from Σ alone to M × Σ is natural: coherence is genuinely frame-relative and environment-dependent, and the joint manifold M × Σ is the correct arena for describing this dependence geometrically.

The action principle (2.1.37) extends (2.1.8) from Paper 1 by including spacetime coordinates x^μ as dynamical variables on equal footing with coherence-frame coordinates ξ^a. The coupling term 2 T_{MΣ} \dot{x}^\mu \dot{\xi}^a is the new physics: it enforces that efficient coherence-preserving pathways through spacetime are those that simultaneously adapt the coherence frame.
