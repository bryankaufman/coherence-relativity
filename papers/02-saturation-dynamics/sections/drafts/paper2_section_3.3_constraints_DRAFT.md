# §3.3 What Derived Compactification Constrains

## 3.3.1 Overview: From Topology to Physics

Section 3.2 established that compactification is *derived*, not assumed. The compact fiber $S^1$ emerges topologically from the Hopf fibration over $S^2$, which in turn emerges from the first-realized geometry of coherence axioms.

This represents a qualitative shift in the landscape of extra-dimensional physics. In the historical framework, compactness is postulated, and one is then free to choose *any* compact topology (Calabi-Yau, orbifold, etc.), with moduli to vary. In Coherence Relativity, the topology is *determined* by first principles.

The question now is: **What physics does this determination constrain?**

This section answers that question by tracing the cascade of constraints that flow from fixing the topology. We show that:

1. The landscape of possible topologies is reduced from ~$10^{500}$ to a countable discrete set.
2. The moduli space for each topology is zero (topologically rigid).
3. The KK mode structure and matter content are fixed by the fiber topology.
4. The cosmological constant becomes a function of a single parameter (fiber radius).
5. Significant degrees of freedom remain unconstrained by topology alone.

This is a profound reduction in freedom—but it is not a complete determination of physics. The distinction between what is constrained and what is left open is crucial.

---

## 3.3.2 Constrained Topology Class

### The Elimination of the Calabi-Yau Landscape

In string theory, six (or seven) extra dimensions are compactified on a Calabi-Yau 3-fold. The defining property of a Calabi-Yau manifold is that it has holonomy group $\text{SU}(3)$ and vanishing first Chern class $c_1(X) = 0$, making the metric Ricci-flat. The number of topologically distinct Calabi-Yau 3-folds is estimated at approximately $10^{500}$.

The landscape problem: different Calabi-Yau choices yield different low-energy physics (different gauge groups, matter representations, coupling constants). There is no principle for preferring one topology over another—hence the "landscape."

In Coherence Relativity, this landscape is eliminated at the topological level and drastically reduced overall:

**The derived compactification is the Hopf fibration $S^1 \to S^3 \to S^2$, with base geometry $S^2$ and fiber topology $S^1$.**

This is the minimal ($c_1 = 1$) principal $U(1)$ bundle over the first-realized geometry. The total space is $S^3 \\cong \\text{SU}(2)$ as a manifold (though we keep the fibration structure explicit to highlight the compactification). More generally, principal $U(1)$ bundles over $S^2$ form a discrete family indexed by $c_1\\in\\mathbb{Z}$; the minimal case is selected here by model minimality, not by a strict uniqueness theorem.

### Topologies Ruled Out

The derived framework **rules out**:
- All Calabi-Yau 3-folds (these have complex dimension 3, not 1; base geometry $\approx \mathbb{CP}^3$ or more complex, not $S^2$).
- All K3 surfaces and other K3-fibered spaces.
- All Calabi-Yau orbifolds and singularities (these introduce discrete identifications incompatible with the smooth Hopf structure).
- All toroidal compactifications $T^6$ and higher-genus surfaces.
- All Randall-Sundrum warped geometries (these assume the compactified dimension *a priori*, then solve Einstein equations; here, compactness is prior).
- All ADD models with single or multiple extra dimensions of arbitrary size and topology.

### What Remains Possible

Within the derived framework, the following topologies remain as open possibilities:

1. **The $c_1 = 1$ Hopf fibration (minimal case)**: $S^1 \to S^3 \to S^2$.
   - This is the first-realized compactification, selected by minimality.

2. **Higher-Chern-number bundles ($c_1 = n, n > 1$)**: The principal $U(1)$ bundles with $c_1 = 2, 3, 4, \ldots$ also exist over $S^2$.
   - Their total spaces remain 3-manifolds (for $n>1$, lens spaces $L(n,1)$), with the same base dimension (2) and fiber dimension (1).
   - Whether nature realizes any of these higher-$c_1$ bundles is an open question (see [Paper 2B] for energy-scale analysis).
   - These correspond to different bundle topology classes, not higher-dimensional total spaces.

3. **Twisted bundles and associated vector bundles**: Once the principal bundle is fixed, associated vector bundles (e.g., for gauge fields or matter fields) can have different transition functions.
   - However, the base principal structure remains $S^1 \to E_{c_1} \to S^2$.

### Precision Statement

The **topological constraint** from derived compactification is:

$$\boxed{\text{Base geometry: } S^2 \quad ; \quad \text{Fiber: } S^1 \quad ; \quad \text{Total space: } E_{c_1} \text{ with } c_1 \in \mathbb{Z}_+}$$
(Eq. 3.3.1)

The minimal case $c_1 = 1$ gives $E_1 = S^3$. Higher-$c_1$ bundles give distinct manifolds, but all share the same base $S^2$ and fiber dimension 1.

**Consequence**: The landscape of topological choices is reduced from ~$10^{500}$ (Calabi-Yau) to a **countable discrete set** $\{ E_n : n \in \mathbb{Z}_+ \}$ indexed by Chern number, with $c_1 = 1$ selected by minimality.

This is a reduction of approximately 100 orders of magnitude in the space of topological possibilities.

---

## 3.3.3 Constrained Moduli Space

### String Theory Moduli: The Landscape Problem

In string theory with a Calabi-Yau 3-fold $X$, the metric on $X$ is Ricci-flat but not unique. For a given topological type, there is a **moduli space** of distinct geometric realizations. Specifically:

- **Complex structure moduli**: Deformations of the complex structure that preserve the Calabi-Yau condition. For typical Calabi-Yau 3-folds, this space has dimension $\approx 100$ to $1000$.
- **Kähler moduli**: Deformations of the Kähler form. This space also has dimension $\mathcal{O}(100)$.

Each point in the moduli space corresponds to a different geometric shape of the same topological manifold, with different physical consequences (different gauge groups, matter content, coupling constants). Stabilizing these moduli requires explicit potentials (Goldberger-Wise, KKLT, etc.), and the number of moduli varies between Calabi-Yau spaces.

**The problem**: The moduli space is continuous and vast. String theory landscape estimates include the uncertainty of which moduli values are physically realized, contributing to the ~$10^{500}$ estimate.

### Coherence Relativity: Topological Rigidity

In contrast, the Hopf fibration $S^1 \to S^3 \to S^2$ is **topologically rigid**.

This is a precise statement: the principal $U(1)$ bundle structure is entirely determined by its first Chern number $c_1$. Two principal $U(1)$ bundles over $S^2$ are isomorphic (as principal bundles) if and only if they have the same Chern number. There is no continuous moduli space for the topology itself.

More formally:

$$\\boxed{\\text{No continuous topological moduli for fixed }(S^2,S^1);\\ \\text{topology classes are discrete and indexed by } c_1\\in\\mathbb{Z}.}$$
(Eq. 3.3.2)

That is, there are no continuous families of topologically distinct Hopf bundles. Each integer value of $c_1$ specifies a unique topological type (up to isomorphism).

### Geometric Moduli (Metric Deformations)

It is important to clarify: we are not claiming that the metric on $S^3$ or $E_{c_1}$ is uniquely determined. The *topology* is rigid, but the *geometry* (the metric) can be deformed.

For instance, one could consider Einstein metrics on $S^3$, or warped metrics, or metrics with additional structure (e.g., Kähler-Einstein metrics if an additional complex structure is present). These metric deformations correspond to geometric moduli, analogous to Kähler moduli in Calabi-Yau geometry.

However, unlike the string landscape, these geometric moduli are *not* free parameters. They are determined by the dynamical equations (Einstein equations, with boundary conditions set by the low-energy effective action; see §4 for the abstract framework and [Paper 2B, §6] for the KK-Cone system). The geometry is not chosen; it is solved for.

### Comparison to String Moduli

|  | String Theory | Coherence Relativity |
|---|---|---|
| **Topology** | Chosen from ~$10^{500}$ Calabi-Yau types | Derived: $S^1 \to E_{c_1} \to S^2$; $c_1=1$ minimal |
| **Complex structure moduli** | $\\mathcal{O}(100)$–$\\mathcal{O}(1000)$ free parameters | Not a free landscape variable here; discrete $c_1$ class instead |
| **Kähler moduli** | $\mathcal{O}(100)$ free parameters | Determined by Einstein equations |
| **Moduli stabilization problem** | Unsolved (KKLT, swampland, landscape) | Not applicable to topology |

---

## 3.3.4 Constrained Matter Content via KK Modes

### Mode Structure on the Fiber $S^1$

The topology of the compact space directly determines the allowed **Kaluza-Klein (KK) modes**—the harmonic eigenfunctions of fields on the compact dimensions. These modes determine which particles appear in the 4D low-energy effective theory.

For a field $\Phi(x^\mu, y)$ living on $M^4 \times S^1$ (where $y$ is the angular coordinate on the fiber $S^1$ with radius $R$), the expansion in harmonics is:

$$\Phi(x^\mu, y) = \sum_{n=-\infty}^{\infty} \phi_n(x^\mu) e^{i n y / R}$$
(Eq. 3.3.3)

The integer $n$ is the **winding number** around the fiber. Each winding mode has mass:

$$m_n = \sqrt{\frac{n^2}{R^2} + \text{internal masses}}$$
(Eq. 3.3.4)

This simple structure—quantized by the fundamental group of $S^1$, which is $\mathbb{Z}$—is a **direct consequence** of the fiber being topologically a circle.

### Contrast with Calabi-Yau Compactifications

On a Calabi-Yau 3-fold $X$, the harmonic eigenfunctions are forms on $X$, with eigenvalues determined by the Hodge structure of $X$. For instance:

- Scalars (0-forms): $h^{0,0} = 1$, giving the dilaton and overall volume modulus.
- (1,1)-forms: There are $h^{1,1}$ independent such forms, giving $h^{1,1}$ moduli (Kähler moduli).
- (2,1)-forms: There are $h^{2,1}$ independent forms, giving $h^{2,1}$ moduli (complex structure moduli).

The Hodge numbers $h^{p,q}$ depend on the topological type of $X$. For a typical Calabi-Yau 3-fold:

$$h^{1,1} \approx 100-300 \quad ; \quad h^{2,1} \approx 100-1000$$

Each independent form corresponds to a 4D scalar field, which must be "stabilized" (given a mass or potential) to match observation.

### Consequence for Coherence Relativity

For the Hopf fiber $S^1$, the mode structure is completely determined by the $\mathbb{Z}$ winding number. The matter content is therefore **constrained by the topology**:

- The fiber admits no local moduli. The only degree of freedom is the global radius $R$ of the circle.
- All fields living on the fiber organize into KK towers with definite winding numbers (Eq. 3.3.3).
- The low-energy spectrum consists of the $n=0$ (zero-mode) fields, plus massive $n \neq 0$ KK excitations.

**Key difference**: In Calabi-Yau compactifications, the topology determines the number of moduli. In Hopf compactifications, the topology determines the mode structure *directly*, and there are no topological moduli at all.

$$\boxed{\text{KK spectrum} = \left\{ \phi_{n}(x^\mu) : n \in \mathbb{Z}, \, m_n \text{ from Eq. 3.3.4} \right\}}$$
(Eq. 3.3.5)

---

## 3.3.5 Constrained Cosmological Constant

### The Vacuum Energy on the Fiber

The quantum vacuum energy (Casimir energy) of fields on a compact space depends on topology, radius, field content, and boundary conditions. To keep conventions fixed across this paper, define

$$L := 2\pi R, \qquad f := \frac{7N_F}{8} - N_B.$$

For massless modes with periodic bosons and antiperiodic fermions, the regularized **vacuum energy density** is

$$\rho_{\text{Casimir}}(L)=\frac{\pi^2\hbar c}{90\,L^4}\,f,$$
(Eq. 3.3.6)

equivalently,

$$\rho_{\text{Casimir}}(R)=\frac{\hbar c}{1440\pi^2\,R^4}\,f.$$
(Eq. 3.3.7)

This section tracks the density form ($\propto L^{-4}$ or $R^{-4}$). One-dimensional vacuum energies of the form $E\propto L^{-1}$ are not mixed into these equations unless an explicit dimensional-reduction volume factor is shown.

### In the Derived Framework

**The topology of the fiber is fixed**: The Hopf fibration gives $S^1$, and the mode expansion (Eq. 3.3.3) is therefore fixed.

**The field content on the fiber**: This is determined by the low-energy effective action coming from Paper 3's phase transition (see §2.3 and [Paper 2B]). The field content includes the coherence field, coupled scalars, and possibly additional matter.

**The cosmological constant becomes a function of the radius $R$**:

$$\Lambda_{\text{eff}}(R)=\frac{8\pi G_4}{c^4}\,\rho_{\text{Casimir}}(R)$$
(Eq. 3.3.8)

In the string landscape, one asks: "For each of ~$10^{500}$ topologies, what are the possible values of the cosmological constant?" The answer is a (roughly) continuous distribution of possible values.

In Coherence Relativity, one asks: "For the fixed topology $S^1 \to S^3 \to S^2$, what values of $\Lambda_{\text{eff}}$ are possible as a function of $R$?" The answer is a one-parameter family (parametrized by the fiber radius).

### Implications for Fine-Tuning

The observed value of the cosmological constant is extraordinarily small: $\Lambda_{\text{obs}} \sim 10^{-120}$ in Planck units. This is the cosmological constant problem.

In the string landscape, explaining this requires anthropic selection: among the ~$10^{500}$ vacua, those with small $\Lambda$ are rare but exist, and we anthropically select one of them.

In Coherence Relativity, the question is different:

**Is there a value of the fiber radius $R$ for which $\Lambda_{\text{eff}}(R) \approx \Lambda_{\text{obs}}$?**

This is no longer an anthropic selection among a vast landscape. It is a single-parameter fine-tuning problem. Whether this can be solved via:
- A residual symmetry that suppresses the vacuum energy to all orders, or
- A dynamical mechanism that stabilizes $R$ at the correct value (see [Paper 2B, §4.3]), or
- An exact cancellation via quantum properties of the coherence field,

is an open question. The abstract dynamics are developed in §4; evaluation on a specific geometry is deferred to [Paper 2B].

**Constraint statement**:

$$\boxed{\Lambda_{\text{eff}} = \Lambda_{\text{eff}}(R, \text{field content}) \quad ; \quad R \text{ is the sole } \text{topological parameter}}$$
(Eq. 3.3.9)

This is a profound reduction: from a ~$10^{500}$-dimensional moduli space of possible vacuum energies, to a one-parameter family.

---

## 3.3.6 What Is NOT Constrained by Topology

It is crucial to state honestly what derived compactification does **not** determine. Topology is powerful, but it is not physics.

### (a) The Fiber Radius $R$

**Not constrained by topology**: The fact that the fiber is $S^1$ tells us it is a circle. It does not tell us the radius. A circle can be arbitrarily large or small.

**Constrained by dynamics**: The radius $R$ must be determined by some physical mechanism. In [Paper 2B, §4.3], quantum properties of the coherence field, combined with the scalar potential, are explored as a mechanism to stabilize $R$ to a particular value. But this is a *separate* calculation, not a topological consequence.

The derived framework replaces the landscape problem ("Which of ~$10^{500}$ topologies?") with a radius problem ("What stabilizes the radius?"). This is progress—it is a simpler problem—but it is not a complete solution.

**Status**: **OPEN**.

### (b) The Field Content on the Fiber

**Not constrained by topology**: The topology of $S^1$ does not determine what fields live on it. Whether the fiber carries a gauge field (e.g., a $U(1)$ photon), scalar fields, fermions, or other matter is not a topological question.

**Constrained by symmetry and dynamics**: The field content is determined by:
1. The symmetries of the effective action (gauge invariance, Lorentz invariance, etc.).
2. The dynamics of the phase transition described in Paper 3 (§2.3).
3. The requirement of consistency with low-energy observation (e.g., electromagnetism, the Higgs mechanism).

In [Paper 2B], we detail what fields appear when the framework is specialized to a geometry. But this is derived from *physical* reasoning (coupling to matter, gauge interactions), not from topology.

**Status**: **Determined by Paper 3's dynamics; not by compactification topology**.

### (c) The Warp Profile $A(r, z)$

**Not constrained by topology**: The Hopf fibration specifies the topological structure $S^1 \to S^3 \to S^2$, but not the metric. In particular, if the compact dimension varies with the macroscopic coordinates (r, z) — which would be natural in a cosmological setting with spatial inhomogeneity — the warp profile $A(r, z)$ describes this variation.

**Constrained by Einstein equations**: The warp factor $A$ is determined by solving the Einstein equations with appropriate stress-energy sources (matter fields, curvature energy, etc.). The abstract frame-lag mechanism (§4) determines how the warp profile enters the dynamics; explicit solutions require a geometry [Paper 2B, §6].

**Status**: **Determined dynamically by Einstein equations; not by topology**.

### (d) Whether $c_1 = 1$ Is the Only Realized Compactification

**The argument for $c_1 = 1$ is minimality**: Section 3.2 argues that the Hopf fibration with $c_1 = 1$ is the *minimal* non-zero-Chern-number principal $U(1)$ bundle over $S^2$. This is a good reason to expect it to be realized first at low energies.

**But higher-$c_1$ bundles also exist**: In principle, at higher energies or in different regions of the phase diagram, principal bundles with $c_1 = 2, 3, \ldots$ could be realized, corresponding to additional extra dimensions.

**Not uniquely constrained**: The framework predicts that if any compactification is realized, it must be of the form $S^1 \to E_{c_1} \to S^2$. But whether the one observed is $c_1=1$, or whether multiple values coexist, is an open question.

**Status**: **OPEN. The minimality argument suggests $c_1 = 1$, but does not exclude higher values**.

---

## 3.3.7 Comparison Table: Assumed vs. Derived Compactification

| Aspect | String Landscape ("Assumed") | Coherence Relativity ("Derived") |
|--------|---|---|
| **Topological Origin** | Postulated; no derivation | Derived from coherence axioms → $S^2$ → Hopf bundle |
| **Topological Choice** | ~$10^{500}$ Calabi-Yau 3-folds | Countable discrete set $\{E_n : n \in \mathbb{Z}_+\}$; minimal case $c_1=1$ |
| **Complex Structure Moduli** | $h^{2,1} \sim 100$–$1000$ per topology | **0** (topologically rigid) |
| **Kähler Moduli** | $h^{1,1} \sim 100$–$300$ per topology | Determined by Einstein equations |
| **Moduli Stabilization** | Requires ad hoc potentials (KKLT, Goldberger-Wise) | Not applicable to topology; only radius needs stabilization |
| **KK Mode Structure** | Determined by Hodge structure of Calabi-Yau | Simple $e^{in y/R}$ towers; determined by $\mathbb{Z}$ winding |
| **Landscape Size** | ~$10^{500}$ | Countable; dramatic reduction |
| **Cosmological Constant** | Landscape of possible values; anthropic selection | Single-parameter family $\Lambda(R)$; may be more amenable to exact solutions |
| **Radius Stabilization** | Part of the landscape problem | Separate dynamical problem; addressed in [Paper 2B, §4.3] |
| **Field Content Origin** | Determined by topology; varies with Calabi-Yau | Determined by Paper 3 phase transition and symmetry; not by topology |
| **Warp Profile** | Assumed to exist (Randall-Sundrum); not derived | Abstract framework in §4; derived from Einstein equations in [Paper 2B, §6] |
| **Falsifiability** | Low (landscape explains everything) | High (specific prediction: first-realized geometry is $S^2$) |

---

## 3.3.8 The Reduction in Degrees of Freedom

To quantify the constraint, consider the counting of free parameters:

### String Theory Landscape

A given Calabi-Yau 3-fold has:
- $1$ choice of topological type (among ~$10^{500}$)
- $h^{2,1} \approx 100$–$1000$ complex structure moduli
- $h^{1,1} \approx 100$–$300$ Kähler moduli
- Additional continuous choices of coupling constants, fluxes, and wrapping numbers

**Total degrees of freedom**: $\gtrsim 10^{500} \times (10^3)^2 \sim 10^{506}$ (rough order of magnitude).

### Coherence Relativity (Minimal $c_1=1$ Case)

- $1$ topological choice: $S^1 \to S^3 \to S^2$ (the $c_1=1$ Hopf bundle)
- $0$ topological moduli (rigid)
- $1$ geometric parameter: the fiber radius $R$ (constrained dynamically, not free)
- $\mathcal{O}(10)$ parameters from field content and couplings (determined by symmetry and Paper 3's dynamics)

**Total degrees of freedom**: $\mathcal{O}(10)$.

**Reduction factor**: ~$10^{500}$ to $\sim 10$, a factor of $\sim 10^{500}$.

$$\boxed{\text{Degrees of freedom: String theory } \approx 10^{500} ; \quad \text{Coherence Relativity } \approx 10}$$
(Eq. 3.3.10)

This is a reduction by many orders of magnitude—but *not* to a single point. Open questions remain, particularly the radius stabilization and the field content.

---

## 3.3.9 Implications and Open Questions

### What This Framework Achieves

1. **Landscape elimination**: By deriving the topology from first principles, Coherence Relativity does not solve the landscape problem—it eliminates it. The landscape was always an assumption dressed up as physics. Here, the assumption is replaced by derivation.

2. **Rigidity**: Topologies cannot be continuously deformed. This is not a burden; it is a strength. It means the framework makes sharp, falsifiable predictions (see §3.2.7 on falsifiability).

3. **Simplification of moduli**: From thousands of topological moduli to zero. This is real progress toward a unified theory.

4. **Predictive power**: The framework predicts that if extra dimensions exist, they must have the structure $S^1 \to E_{c_1} \to S^2$. This is testable in principle (though the scale is likely far beyond current experiments).

### What Remains Open

1. **Radius stabilization**: What mechanism stabilizes $R$? This is the subject of [Paper 2B, §4.3], where quantum potential mechanisms and self-consistency conditions are explored.

2. **Field content**: What fields live on the compact space, and why? The abstract dynamics (§4) constrain the possibilities; specific field content is determined when a geometry is chosen [Paper 2B].

3. **Higher-$c_1$ compactifications**: Are they realized? At what energies? Energy-scale analysis and future directions are addressed in [Paper 2B].

4. **Quantitative predictions**: Can the framework make quantitative predictions (mass ratios, coupling constants, dark energy density) that are testable? The abstract equations of motion (§4) set the framework; quantitative evaluation on a specific geometry is the subject of [Paper 2B].

5. **Consistency with observation**: Does the derived compactification lead to low-energy physics consistent with the Standard Model and observations? This is the subject of Part B of the paper series (not covered in the present manuscript).

---

## 3.3.10 Summary and Transition to §4

**Section 3.3 Main Points**:

1. **Topology is constrained**: The derived compactification is $S^1 \to E_{c_1} \to S^2$, not a choice among ~$10^{500}$ options.

2. **Moduli are eliminated**: There are no continuous moduli for the topology. Geometric moduli (if any) are determined by Einstein equations, not chosen freely.

3. **KK spectrum is fixed**: The mode structure on $S^1$ is simple and completely determined: integer winding numbers, mass ladder from Eq. 3.3.4.

4. **Cosmological constant is constrained**: Instead of a landscape, $\Lambda_{\text{eff}}$ is a one-parameter function $\Lambda(R)$.

5. **Significant open questions remain**: The fiber radius, the field content, the warp profile, and whether higher-$c_1$ bundles are realized, are all determined by *dynamics*, not topology.

6. **Order of magnitude reduction**: From ~$10^{500}$ candidate configurations in the string landscape to $\mathcal{O}(10)$ topological and dynamical choices in the coherence framework, representing an enormous (but approximate) reduction in freedom.

This constraint-and-clarify framework is the foundation for §4 (Equations of Motion) and the companion paper [Paper 2B]. In §4, we develop the abstract equations of motion on $M \times \Sigma$, establishing the dynamical framework in geometry-independent language. [Paper 2B] then specializes this framework to the KK-Cone—the first physically motivated geometry—evaluating the self-consistency conditions, deriving explicit dynamics, and extracting testable predictions.

---

## 3.3.11 Paper 3 Interface Hooks (for staged closure)
To preserve continuity across papers, this section records the specific Paper 3 outputs that Paper 2 depends on but does not derive.
1. **P3-H1: Phase-transition gate**  
   Provide an explicit phase classifier (equivalently a transition scale/redshift) separating the 5D-coupled regime from the effective 4D regime. Paper 2 uses this gate to state where reduced 4D formulas are valid.
2. **P3-H2: Post-transition field-content map**  
   Provide the realized post-transition sector(s) with explicit $(N_B,N_F)$ counts and boundary-condition assignments. This is required to instantiate Eqs. 3.3.6–3.3.9 without branch ambiguity.
3. **P3-H3: Bundle-selection statement**  
   Clarify whether only the minimal $c_1=1$ branch is dynamically selected at low energy or whether multiple $c_1$ branches can coexist in the accessible phase diagram.
4. **P3-H4: Effective-source projection rule**  
   Provide the projection map from the full $M\times\Sigma$ dynamics into 4D effective source terms used in late-time phenomenology, so that "derived vs assumed" status remains explicit across the paper boundary.
**Status**: INTERFACE-CONTRACT ONLY. These hooks define dependencies; they are not claimed as completed derivations in Paper 2.

## References and Notes for §3.3

- Callahan, J. J. (2010). *The Geometry of Spacetime: An Introduction to Special and General Relativity*. Springer. [Cosmological constant and vacuum energy.]
- Goldberger, W. D., & Wise, M. B. (2000). "Modulus Stabilization with Bulk Fields." *Physical Review Letters*, 83(24), 4922–4925. [Radius stabilization.]
- Candelas, P., de la Ossa, X. C., Green, P. S., & Parkes, L. (1991). "A Pair of Calabi-Yau Manifolds as an Exactly Soluble Superconformal Theory." *Nuclear Physics B*, 359(1), 21–74. [Calabi-Yau moduli.]
- Paper 3 (in preparation): "Coherence Frames and First-Realized Geometry." [Derivation of $S^2$ and implications for the topology.]
- §4 (Equations of Motion): Abstract dynamical framework on $M \times \Sigma$.
- [Paper 2B] (companion paper): Self-consistency conditions, radius stabilization, EOM on the KK-Cone, holographic verification.
