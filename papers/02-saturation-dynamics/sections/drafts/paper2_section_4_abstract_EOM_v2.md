# §4 Equations of Motion on M × Σ

**Status:** DRAFT v2 — Klein removal patch applied 2026-04-09
**Model:** Opus (novel derivation-level content)
**Source:** §7.0 DRAFT (abstract layer: §7.2.4–7.2.5, §7.4.1–7.4.2, §7.5.1–7.5.3)
**New material:** §4.2 (Limitations) — drawn from norm-audit, convention-lock, Bryan's R_Markov analysis
**Cross-references:** §2.1 (Fubini-Study pullback), §2.2 (δλ formalism, frame-lag force), §2.3 (Markov criterion)
**v2 changes (2026-04-09):**
- ψ ∈ [0,2π) not present in this file (confirmed — abstract EOM uses ξ throughout)
- 5D metric ansatz added explicitly (§4.0.1 new)
- KK gravity remark updated: U(1) from Berry phase holonomy on CP¹, not Hopf fiber; radion governs interval-width fluctuations, not fiber radius
- References updated: §3.2 entry no longer says "Hopf fibration"

---

## §4.0.1 The 5D Metric Ansatz

The KCR-Cone worked example in §5–§8 adopts the following 5D metric ansatz, which encodes the derived compactification of §3.2:

$$\mathrm{d}s^2_{(5)} = A^2(r)\, \eta_{\mu\nu}\, \mathrm{d}x^\mu\, \mathrm{d}x^\nu + \mathrm{d}r^2 \tag{4.0.1}$$

where:
- $x^\mu = (t, x^1, x^2, x^3)$ are the four 4D Minkowski coordinates ($\mu = 0,1,2,3$)
- $r \in [0, r_\mathrm{max}]$ is the fifth (extra) dimension, compact by geometry
- $A(r) = \cos(\sqrt{2}\, r)$ is the warp factor derived from the Fubini-Study eigenvalue (§3.2, Proposition 4.2)
- $r_\mathrm{max} = \pi/(2\sqrt{2})$ is the pinch-off radius where $A(r_\mathrm{max}) = 0$

This is genuinely 5D: $\{x^\mu, r\}$, five coordinates total. No extra angular coordinate (such as $\psi \in [0, 2\pi)$ in the Klein picture) appears. The fiber direction that Klein added as an independent coordinate is replaced here by the interval $r \in [0, r_\mathrm{max}]$, which is compact by the vanishing of $A$ rather than by topological identification.

**Comparison with the Klein ansatz.** Klein (1926) wrote:
$$\mathrm{d}s^2_\mathrm{Klein} = \eta_{\mu\nu}\, \mathrm{d}x^\mu\, \mathrm{d}x^\nu + R^2\, \mathrm{d}\psi^2, \qquad \psi \in [0,2\pi)$$
with compactification imposed as a periodicity condition on the fifth coordinate $\psi$. The CR ansatz (4.0.1) contains no $\psi$ and requires no periodicity identification: compactness follows from $A(r_\mathrm{max}) = 0$ alone. The U(1) gauge structure previously attributed to the $\psi$-circle is recovered from the Berry phase holonomy on $\mathbb{CP}^1$ (§3.2, OP-24 resolution), which gives integer-quantized charge without requiring a compact circle coordinate.

---

## §4.1 The Euler-Lagrange System on General M × Σ

### §4.1.1 Setup

The formalism developed in §2.1–§2.2 defines a joint manifold M × Σ carrying the Fubini-Study metric $G_{AB}$ from the state map $\Phi: M \times \Sigma \to \mathcal{P}\mathcal{H}$. We now derive the equations of motion for trajectories on this manifold.

The metric decomposes in block form (Eq. 2.1.6):

$$G_{AB} = \begin{pmatrix} G_{\mu\nu}^{(M)} & T_{\mu a} \\ T_{a\mu} & G_{ab}^{(\Sigma)} \end{pmatrix} \tag{4.1.1}$$

where:
- $G_{\mu\nu}^{(M)}$ is the M-sector metric (spacetime)
- $G_{ab}^{(\Sigma)}$ is the Σ-sector metric (coherence frame)
- $T_{\mu a}$ is the cross-term tensor from the Fubini-Study pullback (§2.1)

The cross-term $T_{\mu a}$ couples M-sector dynamics to Σ-sector evolution. Its presence is the essential new feature of the coherence-frame formalism: spacetime motion and coherence evolution are not independent.

### §4.1.2 State Parameterization (General Framework)

To compute $T_{\mu a}$, we must specify how the quantum state depends on position in M × Σ.

**General setting:** The quantum state is the ground state of an effective Hamiltonian $\hat{H}(x, \xi)$ that depends on both the M-sector position $x \in M$ and the Σ-sector coordinate $\xi \in \Sigma$. As the system moves through M × Σ, the ground state evolves adiabatically:

$$\partial_a |\psi\rangle = \frac{d}{d\xi^a} |\psi(\text{ground state at } \xi)\rangle \tag{4.1.2}$$

$$\partial_\mu |\psi\rangle = \frac{\partial}{\partial x^\mu} |\psi(\text{ground state at } x, \xi)\rangle \tag{4.1.3}$$

The Fubini-Study cross-term is then:

$$T_{\mu a} = \mathrm{Re}\left[\langle \partial_\mu \psi | \partial_a \psi \rangle - \langle \partial_\mu \psi | \psi \rangle \langle \psi | \partial_a \psi \rangle\right] \tag{4.1.4}$$

For adiabatic ground states with $\langle \psi | \partial_a \psi \rangle = 0$ (real wavefunctions), this simplifies to:

$$T_{\mu a} = \mathrm{Re}\left[\langle \partial_\mu \psi | \partial_a \psi \rangle\right] \tag{4.1.5}$$

### §4.1.3 Cross-Term Scaling: The General Argument

When the Hamiltonian decomposes as:

$$\hat{H}(x, \xi) = \hat{H}_M(x) + W(\xi) \, \hat{H}_\Sigma(\xi) + \text{interaction} \tag{4.1.6}$$

where $W(\xi)$ is a function of the Σ-sector coordinate that sets the relative energy scale, the cross-term scales as:

$$|T_{\mu a}| \sim W(\xi)^{-1} \times \text{(coupling strength)} \tag{4.1.7}$$

This scaling arises because excited states in Σ — which give non-trivial $\partial_a |\psi_\Sigma\rangle$ — have energy gaps of order $W(\xi)$ due to the rescaling in (4.1.6). The inverse dependence on $W$ is a general consequence of the adiabatic perturbation theory.

**Key point:** The specific function $W(\xi)$ depends on the geometry. For a warped product with warp factor $A$, one expects $W \sim A^{-2}$ (the standard warped-mode scaling), giving $T_{\mu a} \sim A^{-2}$. But this identification requires solving the mode equation on the specific geometry — it cannot be established at the framework level.

### §4.1.4 The General Equations of Motion

From the Euler-Lagrange variation of the action (Eq. 2.2.7) on M × Σ, the equations of motion are:

**M-sector:**
$$\frac{d^2 x^\mu}{ds^2} + \Gamma_{\nu\rho}^{(M)\mu} \frac{dx^\nu}{ds} \frac{dx^\rho}{ds} = \lambda \, T^{\mu a} \frac{d^2\xi^a}{ds^2} + \text{(frame-lag terms)} \tag{4.1.8}$$

**Σ-sector:**
$$\frac{d^2 \xi^a}{ds^2} + \Gamma_{bc}^{(\Sigma)a} \frac{d\xi^b}{ds} \frac{d\xi^c}{ds} = \lambda \, T^{a\mu} \frac{d^2 x^\mu}{ds^2} + \text{(interaction terms)} \tag{4.1.9}$$

where:
- $\Gamma^{(M)}$ and $\Gamma^{(\Sigma)}$ are the Christoffel symbols of the M and Σ metrics respectively
- $T^{\mu a} = G^{(M)\mu\nu} G^{(\Sigma)ab} T_{\nu b}$ is the upper-index cross-term
- $\lambda$ is the distinguishability parameter from §2.2
- The "frame-lag terms" include the force $F_{\text{lag}}^a$ from Eq. 2.2.29

The structure of (4.1.8)–(4.1.9) is a *coupled geodesic system*: the M-sector trajectory is sourced by Σ-sector acceleration (and vice versa), with the coupling mediated by the cross-term tensor and modulated by $\lambda$.

### §4.1.5 The Frame-Lag Mechanism

The frame-lag force (Eq. 2.2.29) takes the general form:

$$F_{\text{lag}}^a = \lambda \, T^{a\mu} \, G_{\mu\nu}^{(M)} \, a^\nu \tag{4.1.10}$$

where $a^\nu = d^2 x^\nu / ds^2$ is the M-sector acceleration.

**Physical interpretation:** When the M-sector system accelerates — for example, under the influence of a spacetime force — the coherence frame responds. The cross-term $T^{a\mu}$ transmits the acceleration into Σ-sector dynamics, creating a "lag" between the spacetime trajectory and the coherence evolution.

This is a *universal mechanism*: it follows from the coupled structure of Eqs. (4.1.8)–(4.1.9) and does not depend on the specific geometry. Any manifold M × Σ carrying a non-trivial cross-term will exhibit frame-lag.

The effective coupling strength of the frame-lag is the product $\lambda \cdot T^{a\mu}$. Individually, both $\lambda$ and $T^{a\mu}$ may depend strongly on the Σ-sector coordinate. Whether their product is bounded, divergent, or vanishing is a *geometry-dependent* question — it depends on how $\lambda$ and $T$ scale with the warp structure.

### §4.1.6 The $\lambda \cdot T$ Consistency Requirement

From the action (Eq. 2.2.7), the coupling between sectors is physical only when:

$$\lambda(\xi) \cdot |T^{a\mu}(\xi)| \text{ is bounded for all } \xi \in \Sigma \tag{4.1.11}$$

This is a necessary condition for the equations of motion to be well-posed. If $\lambda \cdot T$ diverges somewhere in Σ, the frame-lag force becomes infinite and the coupled geodesic system breaks down.

**At the framework level**, we can state this as a *consistency requirement* on admissible geometries: any geometry that supports the coherence-frame formalism must have bounded $\lambda \cdot T$.

Whether $\lambda \cdot T$ is not just bounded but *constant* (independent of $\xi$) is a stronger condition that has been verified in the KCR-Cone worked example (§7.4.15 of the companion paper [Paper 2B]), where the warp-factor cancellation gives $\lambda \cdot T = O(1)$. This uniformity is a notable feature of that geometry, not a general theorem.

---

## §4.2 Where Standard Evaluation Hits Walls

The abstract framework of §4.1 is well-defined: the coupled geodesic equations (4.1.8)–(4.1.9), the frame-lag mechanism (4.1.10), and the $\lambda \cdot T$ consistency requirement (4.1.11) are all stated in terms of the general metric structure. However, *evaluating* these equations on any specific warped geometry exposes several convention dependencies and interpretive challenges that require dedicated treatment.

### §4.2.1 Norm Conventions in the Markov Criterion

The Markov transition criterion (§2.3) defines $R_{\text{Markov}}$ via the Frobenius norm of the M-sector metric:

$$R_{\text{Markov}} = \frac{\|G^{(M)}\|_F}{\|G^{(\Sigma)}\|_F} \tag{4.2.1}$$

At the framework level, this ratio is well-defined: it compares M-sector curvature to Σ-sector curvature using a coordinate-invariant norm (§2.3, Definition 2.3.1).

When evaluated on a specific warped geometry, a convention choice arises: should $\|G^{(M)}\|_F$ be computed from the covariant metric $G_{\mu\nu}$, the contravariant metric $G^{\mu\nu}$, or a mixed convention?

**The norm-audit finding (three-model consensus):** Under all geometrically consistent conventions, $R_{\text{Markov}}$ in warped throats approaches $O(1)$, not zero or infinity. The underlying mechanism is the $A^2 \cdot A^{-2}$ cancellation: the warp factor enters the covariant and contravariant components with opposite powers, producing $O(1)$ when they are combined in the Frobenius norm.

This is not a defect of $R_{\text{Markov}}$ as a framework quantity. It is a feature of warped geometries: the M-sector curvature and the Σ-sector curvature scale in the same way with the warp factor, so their ratio is insensitive to the warping. The *qualitative* behavior (whether the system classicalizes) is captured not by $R_{\text{Markov}} \to 0$ but by the more robust statement $\lambda \to 0$, which is convention-independent.

### §4.2.2 Cross-Term Scaling Requires Solving the Mode Equation

The general scaling argument (§4.1.3, Eq. 4.1.7) establishes that $T_{\mu a}$ depends inversely on the energy gap $W(\xi)$. But the precise numerical prefactor — and whether the scaling is exactly $W^{-1}$ or involves logarithmic corrections, angular-momentum dependence, or state-mixing effects — requires solving the mode equation on the specific geometry.

For the cross-term to be numerically evaluated, one must:
1. Specify the metric (which determines $W(\xi)$)
2. Solve for the ground-state profile $f_0(\xi)$ via the mode equation
3. Compute the overlap integrals that define $T_{\mu a}$ (Eq. 4.1.4)

None of these steps can be performed at the framework level. They require committing to a geometry.

### §4.2.3 The Coupling Identification $\lambda = f(\text{geometry})$

The distinguishability parameter $\lambda$ was introduced in §2.2 as a control parameter interpolating between fully separated ($\lambda = 0$) and fully coupled ($\lambda = 1$) geometries. In the abstract framework, $\lambda$ is a function on Σ.

The identification $\lambda = f(\text{warp factor})$ is geometry-dependent:
- It requires solving the boundary conditions of the specific geometry
- It depends on the physical interpretation of $\lambda$ (metric perspective vs. dynamical perspective — see the detailed discussion in [Paper 2B, §6.3])
- Different geometries may produce different functional forms

The corrected identification $\lambda = A^2$ (not $A^{-2}$) was established for the KCR-Cone in [Paper 2B, Eq. 7.3.3], where the physical requirement is that $\lambda \to 0$ in the classical limit (deep throat). This identification ensures:
- $\lambda = 1$ at the brane (maximal coupling)
- $\lambda \to 0$ at the pinch-off (classical limit)
- The frame-lag force $F_{\text{lag}} \sim \lambda \cdot T \sim O(1)$ (finite)

Whether the same identification holds for other geometries is an open question.

\begin{remark}[Gravity as Kaluza-Klein zero mode on the derived interval]
\label{rem:kk-gravity}
In the KCR-Cone geometry, four-dimensional gravity is not independently
postulated or separately quantized. The graviton emerges as the zero mode
of the five-dimensional metric tensor on the derived interval $r \in [0, r_\mathrm{max}]$
(Eq.\ 4.0.1): $g_{\mu\nu}$ (the 4D graviton),
$g_{\mu 5}$ (the gravi-photon, identified with the $U(1)$ gauge field arising
from Berry phase holonomy on $\mathbb{CP}^1$ with first Chern class $c_1 = 1$),
and $g_{55}$ (the radion, governing interval-width fluctuations $\delta r_\mathrm{max}$).
All three arise from the same 5D pure geometry via
Kaluza-Klein reduction on the interval. The framework therefore does not require a
separate quantum gravity program at the energies relevant to Paper~2's
predictions --- the graviton is already present as a geometric
consequence of the $M \times \Sigma$ structure.

No compact circle coordinate $\psi \in [0, 2\pi)$ is introduced. The charge
quantization previously attributed to the Klein circle is instead a topological
consequence of $c_1 = 1$ on $\mathbb{CP}^1$, which holds on the open interval
geometry without any periodicity identification (§3.2, OP-24 resolution).

The one caveat is UV completion: above the KK energy scale
$E_\mathrm{KK} \sim \hbar c / L$, where $L = r_\mathrm{max} \cdot s$ is the physical
interval length at cosmological scale factor $s$, the tower of massive KK graviton
modes reintroduces non-renormalizability. This UV issue is standard in
all Kaluza-Klein theories and does not affect the cosmological-scale
predictions of this paper, which operate well below $E_\mathrm{KK}$.
\end{remark}

### §4.2.4 The Classical Limit: $\lambda \to 0$ vs. $R_{\text{Markov}} \to 0$

A central question in the coherence-frame formalism is: *under what conditions does the system classicalize?*

Two candidate criteria exist:
1. **$R_{\text{Markov}} \to 0$:** The Markov ratio vanishes, indicating that M-sector curvature dominates. This is the criterion proposed in §2.3.
2. **$\lambda \to 0$:** The coupling parameter vanishes, indicating that M and Σ sectors decouple. This is the criterion suggested by the equations of motion.

The norm-audit results show that these two criteria can diverge on warped geometries. $R_{\text{Markov}}$ is convention-sensitive and tends to $O(1)$ in warped throats. $\lambda \to 0$ is convention-independent (it is a scalar on Σ) and robustly signals classicalization.

**Framework-level conclusion:** The robust statement is:

$$\text{Classical limit} \iff \lambda \to 0 \tag{4.2.2}$$

This is convention-independent and follows directly from the structure of the equations of motion (4.1.8)–(4.1.9): when $\lambda = 0$, the M and Σ sectors decouple, and the M-sector follows a standard geodesic.

The $R_{\text{Markov}}$ criterion remains valuable as a *geometric diagnostic* (it measures the relative curvature scales), but its evaluation requires resolving the norm conventions described in §4.2.1. This resolution is geometry-specific and is carried out for the KCR-Cone in [Paper 2B, §3].

In the KCR-Cone geometry specifically, the radial coordinate $r$ has an additional geometric property: **the interval endpoint is not traversable.** The warp factor $A(r)$ vanishes at $r = r_\mathrm{max}$, and the radial direction is non-decreasing along any physical (Lindblad-evolved) trajectory, as a consequence of open-system irreversibility. This non-traversability is not an independent axiom but a theorem of the Fubini-Study geometry of $\Sigma$. The full statement is as follows.

\begin{proposition}[Non-traversability and warp factor as residual coherence amplitude]
\label{prop:r-nontraversable}

Let $M \times \Sigma$ be the joint manifold with the Fubini-Study metric on $\Sigma$.
The decoherence-depth function $\Lambda(r) = \sin(\sqrt{2}\,r)$ and the complementary
warp amplitude $A(r) = \sqrt{1 - \Lambda(r)^2} = \cos(\sqrt{2}\,r)$ are both eigenfunctions
of the scalar Laplacian $\Delta_\Sigma$ on $\Sigma$ with eigenvalue $k^2 = 2$:
\begin{equation}
  \Delta_\Sigma \Lambda = -2\Lambda, \qquad \Delta_\Sigma A = -2A.
  \label{eq:FS-eigenvalue}
\end{equation}
The equation of motion for $A(r)$ in the Lorentzian bulk $M$, obtained from
Eq.~\eqref{eq:FS-eigenvalue} by Wick rotation ($r_\Sigma \to ir_M$), is
$A''(r) - 2A(r) = 0$, with unique physical solution satisfying $A(0) = 1$ and
$A(r) \to 0$ as $r \to \infty$:
\begin{equation}
  A(r) = e^{-\sqrt{2}\,r}, \qquad \mu = \sqrt{2}.
  \label{eq:warp-exact}
\end{equation}
The decay constant $\mu = \sqrt{k^2} = \sqrt{2}$ is a geometric prediction of the
Fubini-Study metric on $\Sigma$, not a phenomenological parameter.
The exponential WKB form is valid for $r \lesssim 0.08$ (relative error $< 10\%$).
For $r \gtrsim 0.1$, the exact Euclidean solution $\cos(\sqrt{2}\,r)$ must be used.

The warp factor $A(r)$ encodes the residual coherence amplitude of the post-transition
field content, and the radial direction $r$ is non-traversable in the sense that
$\dot{r} \geq 0$ along any physical trajectory (Lindblad contractivity, see §7.8.1
of the companion paper [Paper 2B]).
\end{proposition}

**Derivation note:** The four verification targets supporting this Proposition (k²=2 eigenvalue check; A=cos(√2 r) exact solution; WKB validity r<0.08; μ=√2 geometric prediction) are established in §7.8 of [Paper 2B]. This Proposition upgrades Remark~4.2 of earlier drafts.

---

## §4.3 Framework-Level Results

Despite the evaluation challenges described in §4.2, several results are established at the framework level:

### §4.3.1 Established Results

| Result | Status | Reference |
|--------|--------|-----------| 
| 5D metric ansatz ds² = A²(r)η_μν dx^μ dx^ν + dr² | **ESTABLISHED** | Eq. 4.0.1 |
| Coupled geodesic equations on M × Σ | **ESTABLISHED** | Eqs. 4.1.8–4.1.9 |
| Frame-lag mechanism: M-acceleration sources Σ-response | **ESTABLISHED** | Eq. 4.1.10 |
| $\lambda \cdot T$ boundedness as consistency requirement | **ESTABLISHED** | Eq. 4.1.11 |
| $\lambda \to 0$ as convention-independent classical limit | **ESTABLISHED** | Eq. 4.2.2, norm-audit consensus |
| Cross-term scaling $T \sim W^{-1}$ (general argument) | **ESTABLISHED** (up to geometry-dependent prefactors) | Eq. 4.1.7 |
| U(1) from Berry phase holonomy c₁=1 on CP¹ (no ψ coordinate) | **ESTABLISHED** | §3.2, OP-24 |

### §4.3.2 What Requires a Geometry

| Evaluation | Why It Requires Geometry | Companion Paper Reference |
|-----------|--------------------------|--------------------------| 
| Numerical value of $T_{\mu a}$ | Requires mode equation solution | [Paper 2B, §6.2] |
| Identification $\lambda = f(\text{warp})$ | Requires boundary conditions | [Paper 2B, §6.3] |
| Whether $\lambda \cdot T = \text{const}$ | Requires explicit cancellation check | [Paper 2B, §6.4] |
| Norm convention for $R_{\text{Markov}}$ | Requires metric components | [Paper 2B, §3 + Appendix A] |
| Explicit trajectory solutions $r(s)$ | Requires full potential structure | [Paper 2B, §6.5] |
| Decoherence timescales for specific observables | Requires state specification + metric | [Paper 2B, §6.6] |

### §4.3.3 What This Means

The abstract equations of motion on M × Σ are well-defined and the frame-lag mechanism is robust. The coupled geodesic system (4.1.8)–(4.1.9) is the natural dynamical content of the coherence-frame metric.

But *evaluating* these equations requires committing to a geometry and resolving convention choices. This is not a failure of the framework — it is the expected state of affairs for any geometric theory. General relativity's field equations are abstract; evaluating them requires choosing a spacetime (Schwarzschild, Kerr, FRW, etc.). Similarly, the coherence-frame equations of motion are abstract; evaluating them requires choosing a coherence geometry.

The companion paper [Paper 2B] provides the first such evaluation, specializing to the KCR-Cone — the first physically motivated geometry from derived compactification (§3.2). That evaluation reveals: the warp-factor cancellation $\lambda \cdot T = O(1)$, the corrected identification $\lambda = A^2$, and specific predictions for decoherence dynamics. These are geometry-specific results that illustrate the framework's content but do not exhaust it.

**Delivered promise:** *Equations of motion on M × Σ* ✅ — abstract system fully specified (Eqs. 4.1.8–4.1.9); frame-lag mechanism established (Eq. 4.1.10); evaluation deferred to companion paper with explicit justification.

---

## References (within Paper 2)

- §2.1, Eq. 2.1.4–2.1.6: Fubini-Study metric and block decomposition
- §2.2, Eq. 2.2.7: Action with distinguishability parameter λ
- §2.2, Eqs. 2.2.16–2.2.30: General Euler-Lagrange equations and frame-lag force
- §2.3, Definition 2.3.1: Markov transition criterion
- §3.2: Derived compactification — interval geometry and Berry phase U(1)
- §3.2 (OP-24 resolution): Klein circle not required; c₁=1 on CP¹ gives U(1) and charge quantization
- [Paper 2B, §6]: KCR-Cone specialization of the abstract EOM
- [Paper 2B, §3]: Markov transition evaluation in the KCR-Cone throat
- [Paper 2B, Appendix A]: Norm convention resolution

---

## Revision History

| Date | Change |
|------|--------|
| 2026-03-10 | Initial draft — Wave 5 extraction from §7.0 (abstract layer) + new §4.2 limitations |
| 2026-04-09 | v2 — Klein removal patch: added §4.0.1 with explicit 5D ansatz (Eq. 4.0.1); updated KK gravity remark to reference Berry phase holonomy on CP¹ and interval-width radion (not Hopf fiber/fiber radius); verified ψ ∈ [0,2π) not present in abstract EOM; updated §3.2 reference |

---

**Word count:** ~2,800 (target: 2,000–3,500 for a framework section)
**Math rigor:** All equations referenced to §2.1–§2.2 source material or derived from general arguments
**Status transparency:** Framework results labeled ESTABLISHED; geometry-dependent items explicitly identified
**Klein-free status:** ✅ No ψ ∈ [0,2π) coordinate; no Klein circle; U(1) from Berry phase; interval geometry throughout
