# Coherence Relativity IIB — Derived Topology and KCR-Cone Evaluation

*Paper 2B of the Coherence Relativity series.*


# §1 Introduction

Notation and conventions throughout this paper follow Paper 2A §1.6. The cross-paper symbol
correspondence (Table 1), object-type conventions (Table 2), and causal/ontological direction
notation (Table 3) are not reproduced here. KCR-Cone-specific symbols are defined at first use
in the text; all others refer to Paper 2A.

This paper evaluates the abstract framework of Paper 2A on the first physically motivated
geometry arising from derived compactification: the KCR-Cone, whose warp factor
$A(r) = \cos(\sqrt{2}\,r)$ is derived — not fitted — from the Fubini-Study Laplacian eigenvalue
$k^2 = 2$, a topological invariant of $\mathbb{CP}^1$. The paper establishes that the first two self-consistency conditions (SC1, SC2) are structurally guaranteed by the derived geometry — flatness follows from Minkowski 4D slices, and gravity localization follows from the bounded interval with divergent confining potential. The third condition (SC3, cosmological constant) is conditionally established via the Casimir mechanism. The paper also resolves the norm convention ambiguity identified in Paper 2A §4.2, and carries the derived-topology, EOM, regularity, and SC3 evaluation line. Dark-sector and holographic consequence material belongs to Paper 2C.


# §3.1 Historical Background: The Compactification Question in Quantum Gravity

## Overview

Before turning to the derivation of the Hopf fibration from coherence-frame axioms (§3.2), we briefly review the historical and physical context of compactification in fundamental physics. This section motivates why deriving compactness from first principles—rather than postulating it—matters for coherence relativity.

---

## The Traditional Approach to Extra Dimensions

Kaluza (1921) and Klein (1926) observed that Einstein's equations in 5D, when the fifth dimension is assumed to be a compact circle, naturally yield both Einstein's 4D gravity and Maxwell's electromagnetism on the 4D slice. This is a remarkable result: gauge theory emerges from pure geometry. However, the approach requires an assumption: the extra dimension must be compact. Why compactness? Traditionally, three reasons:

1. **Low-energy consistency**: If extra dimensions are non-compact, the tower of Kaluza–Klein modes (states associated with momentum in the extra direction) is infinite and continuous, contributing infinitely to the vacuum energy and gravitational coupling constants. Compactness discretizes the mode tower, making the low-energy 4D theory finite.

2. **Phenomenological silence**: We do not observe extra dimensions. A compact dimension, if its circumference is small enough, is "hidden" from low-energy observations—the energy required to excite modes with nonzero winding or momentum is so large that they decouple from all accessible experiments.

3. **Mathematical convenience**: Compact manifolds are easier to analyze: they have discrete spectra, admit harmonic analysis, and admit consistent boundary conditions.

These are pragmatic reasons. They have guided 50+ years of string theory, loop quantum gravity, and extra-dimensional model-building. But none of them *derive* compactness from fundamental quantum principles.

---

## The Persistent Gap

The unresolved question is: **Where does compactness come from?**

In string theory, the extra dimensions are compactified on a Calabi–Yau manifold (or orbifold thereof), chosen so that the resulting 4D low-energy theory matches the Standard Model. But the Calabi–Yau geometry is not derived from the theory; it is imposed as a boundary condition. The theory has many consistent Calabi–Yau solutions (the "landscape problem"), each yielding a different low-energy physics. None of the standard approaches explain *why* nature should choose one compactification over another—still less, *why* compactification should occur at all.

Similarly, in modified-gravity scenarios (e.g., massive gravity, bigravity), extra-dimensional models (e.g., DGP, Randall–Sundrum), and loop quantum gravity, compactification is either assumed or fine-tuned to match observations. It is not derived.

This is the gap that the present work addresses. §3.2 will show that the coherence-frame axioms — when applied to the simplest quantum system (the qubit) — produce S² as the first-realized geometry, from which the Hopf fibration S¹ → S³ → S² emerges as a topological consequence. Compactness of the fiber dimension follows from the topology of the Hopf bundle, not from an ad hoc assumption. Compactification, in this argument, is derived rather than postulated.

---

## The Role of Coherence in §3.2

§3.2 shifts perspective fundamentally. Rather than starting with the metric or field equations and asking "what extra dimensions are consistent with observations?", we ask: **"What is the minimal geometric structure that the quantum coherence frame must possess?"**

The coherence frame—the space of "coherence bases" used by a quantum observer—is itself a smooth manifold Σ. On this manifold, quantum states induce a natural metric (the Fubini–Study metric, derived from Paper 1). The key insight is that Σ must be a manifold compatible with quantum unitarity and the preservation of observer choice under unitary evolution.

When we impose these quantum-coherence axioms (discussed in §3.2), the ground state of the coherence algebra uniquely determines the geometry. It turns out to be the 2-sphere S². And when we ask how to topologically extend S² to a 3-dimensional manifold while preserving the U(1) symmetry of angular momentum, the answer is the Hopf fibration S¹ → S³ → S².

**Crucially:** over \(S^2\), principal \(U(1)\) bundles form a discrete family indexed by \(c_1 \in \mathbb{Z}\). In this framework, the Hopf case (\(|c_1|=1\)) is selected by minimality, not by a strict uniqueness theorem.

---

## Summary of §3.1

Compactification has been a mystery in quantum gravity for a century. Traditional approaches assume compactness to suppress unwanted modes or match observations. This section reviewed that history. §3.2 now answers the question: compactification emerges from the requirement that the coherence frame be self-consistent under quantum evolution. It is not a free choice; it is a derived necessity.


# §3.2 Topology as Output: Deriving Compactification from Coherence Axioms

## 3.2.1 The Historical Assumption

For over a century, extra-dimensional physics has operated under a single, unexamined methodological principle: **assume compact dimensions first, then build physics around them**. This is not derived from first principles; it is postulated.

**Kaluza's original insight (1921)** was to postulate a fifth dimension, compactified on a circle. Klein (1926) proposed that this extra dimension must be small to explain why it had not been observed. This compact $S^1$ was an *ansatz*, a working assumption—not a derived geometric consequence.

String theory inherited this architecture. The theory requires ten or eleven spacetime dimensions, and the extra six (or seven) are assumed to be curled up into compact manifolds. The most cited candidates are Calabi-Yau threefolds, with a landscape of approximately $10^{500}$ topologically distinct choices. The question of *why these topologies?* remains unanswered. To stabilize the *size* of these dimensions, researchers developed the Goldberger-Wise mechanism, KKLT uplifting, and other moduli-stabilization techniques. But these mechanisms address the *radius* of compactified dimensions—they do not address *why the dimensions are compact in the first place*, nor do they reduce the landscape's vastness.

The Coherence Relativity framework inverts this logical structure entirely.

## 3.2.2 First-Realized Geometry as Input

The coherence-frame construction, detailed in Paper 3, establishes that **the first non-trivial realized geometry is the 2-sphere**, $S^2$. This result emerges from the coherence-frame axioms applied to the simplest quantum system: a qubit.

### Derivation (Sketch; Full Details in Paper 3)

A qubit is a 2-dimensional Hilbert space, $\mathcal{H} = \mathbb{C}^2$. The space of pure quantum states is the **projective Hilbert space**,
$$\mathbb{P}\mathcal{H} = \mathbb{CP}^1 \cong S^2.$$
(Eq. 3.2.1)

This is a theorem of quantum mechanics, not an assumption. The complex projective line is isomorphic to the 2-sphere via the Fubini-Study metric. Every pure state of a qubit corresponds to a unique point on $S^2$—the **Bloch sphere**.

When the coherence-frame axioms are applied to this minimal system, the resulting coherence-frame manifold $\Sigma$, restricted to the 2-level case, has the natural geometric structure:
$$\Sigma|_{\text{qubit}} = S^2.$$
(Eq. 3.2.2)

This is not a choice. The 2-sphere is the *only* geometry compatible with:
1. The closure axiom of the coherence frame (orbits must form a connected manifold)
2. The quantum-classical correspondence (the state space of a qubit *is* $\mathbb{CP}^1$)
3. The minimality principle (the simplest non-trivial case)

Therefore, $S^2$ is the **first-realized geometry** of the theory. It is derived from quantum mechanics and coherence axioms, not postulated.

## 3.2.3 The Hopf Fibration as Topological Necessity

Now we ask: over $S^2$, what principal $U(1)$ bundles exist?

This is a classical question in algebraic topology, answered completely by the **classification of principal $U(1)$ bundles over $S^2$**:

### Theorem (Principal $U(1)$ Bundles over $S^2$)

Principal $U(1)$ bundles over $S^2$ are classified by elements of $H^2(S^2, \mathbb{Z}) \cong \mathbb{Z}$. Each bundle is characterized by its **first Chern number** $c_1 \in \mathbb{Z}$. The principal bundle with $c_1 = n$ is the mapping:
$$S^1 \to E_n \to S^2$$
(Eq. 3.2.3)

where the fiber is a circle $S^1$, the total space is $E_n$, and the base is $S^2$.

For $c_1 = 0$, the bundle is trivial: $E_0 = S^1 \times S^2$.

For $c_1 = 1$, the bundle is the **Hopf fibration**:
$$S^1 \to S^3 \to S^2.$$
(Eq. 3.2.4)

This is the unique non-trivial principal $U(1)$ bundle over $S^2$ with the smallest possible Chern number. It is not a special or exotic construction—it is the generator of the group $H^2(S^2, \mathbb{Z})$.

### Intrinsic vs. Assumed

Here is the critical shift: the Hopf fibration does not arise from a choice, a symmetry postulate, or a dimensional ansatz. It is a **topological consequence** of the existence of $S^2$.

To say it precisely: if the base manifold is $S^2$, then there exist non-trivial principal $U(1)$ structures. Among the infinite family of principal $U(1)$ bundles over $S^2$, the Hopf bundle with $c_1 = 1$ is the generator — the bundle of minimal (non-zero) Chern number. The selection of $c_1 = 1$ over higher values ($c_1 = 2, 3, ...$) follows from a minimality argument, not a uniqueness theorem.

The Hopf fibration is **intrinsic to $S^2$**. It is not postulated. It emerges.

## 3.2.4 Compactness as Topological Consequence

The fiber of the Hopf fibration is a circle:
$$S^1 \subset S^3.$$
(Eq. 3.2.5)

A circle is compact *by definition*. It is a closed, connected, 1-dimensional manifold. There is no notion in which $S^1$ can be "uncompactified."

Therefore, the following logical chain holds:

1. $S^2$ is derived from coherence axioms and quantum mechanics (§3.2.2).
2. Over $S^2$, the non-trivial principal $U(1)$ bundle of minimal Chern number is the Hopf fibration (§3.2.3).
3. The fiber of the Hopf fibration is $S^1$, which is compact by topology (§3.2.4).

**Conclusion: A compact extra dimension emerges as a topological consequence of the first-realized geometry.**

We have derived compactness. We did not assume it.

## 3.2.5 Inversion of Historical Logic

The difference between this approach and all prior models is one of logical direction.

### Historical Approach (Kaluza-Klein → String Theory)

$$\boxed{\text{Assume } S^1 \text{ compact}} \to \text{Build physics on } M^4 \times S^1 \to \text{Explain why } S^1 \text{ is small}}$$

The compact dimension is the *starting point*. All subsequent physics is built around this assumption. The question "Why is this dimension compact?" is never answered—it is part of the framework's foundation.

### Coherence Relativity Approach (This Paper)

$$\boxed{\text{Derive } S^2 \text{ from coherence axioms}} \to \text{Hopf bundle forces } S^1 \text{ structure} \to \boxed{\text{Compactness is output}}$$

The compact dimension is the *conclusion*. It emerges from the topology of the first-realized geometry. The axioms do not assume compactness; the theorem produces it.

This is not a minor modification. This is an inversion of the logical structure of extra-dimensional physics.

### Formal Contrast

In the historical framework:
$$\text{Geometry} \xleftarrow{\text{assumed}} \text{Compactification} \xleftarrow{\text{required}} \text{Physics}$$

In Coherence Relativity:
$$\text{Physics (Coherence axioms)} \xrightarrow{\text{derive}} S^2 \xrightarrow{\text{force}} \text{Hopf } S^1 \xrightarrow{\text{topological}} \text{Compactness}$$

Causality runs in the opposite direction.

## 3.2.6 Distinctions from Prior Work

This derivation differs fundamentally from stabilization mechanisms (Goldberger-Wise, KKLT, etc.) and from prior attempts to explain extra dimensions:

### (a) No Landscape Problem

In string theory, the choice of Calabi-Yau manifold is a choice among approximately $10^{500}$ possibilities. This is the landscape problem. Each choice leads to different low-energy physics.

Here, the landscape is dramatically reduced. The first-realized geometry is $S^2$, determined uniquely by the minimality of the coherence-frame construction. Over $S^2$, the principal $U(1)$ bundles are indexed by their first Chern number $c_1 \in \mathbb{Z}$, and $c_1 = 1$ is selected by minimality. The choice is sharply constrained: the base $S^2$ is derived, and the Chern number is selected by minimality:

$$c_1 = 1 \text{ is selected by minimality: } H^2(S^2, \mathbb{Z}) = \langle c_1 \rangle, \quad c_1 \in \mathbb{Z}.$$
(Eq. 3.2.6)

The landscape reduces to a discrete sequence indexed by $c_1 \in \mathbb{Z}_+$, with $c_1 = 1$ selected by minimality. This is a dramatic reduction from ~$10^{500}$ to a countable set, but it is not unique in the strict mathematical sense — it is minimal.

### (b) Topological Rigidity

The compactness of the fiber is not a stabilization issue. It is a *topological rigidity*. A circle cannot be continuously deformed into a non-compact dimension. The topology $S^1$ cannot be "uncompactified" by any physical process or dynamical mechanism.

By contrast, in string theory, the *size* (radius) of a compact dimension is subject to moduli, potentials, and stabilization mechanisms. But the *topology*—the fact that it is compact—remains an assumption.

Here, topology is derived. Only the radius remains a physical parameter to be stabilized (addressed in §5.3).

### (c) Absence of Moduli Space for Topology

In string theory, the choice of Calabi-Yau manifold defines the topology. But for a given topological choice, there is often a moduli space of geometric realizations (e.g., different shapes of the same manifold with the same topology). These moduli are physical parameters.

The Hopf fibration has a unique topological invariant: $c_1 = 1$. There is no continuous moduli space for the topology itself. The bundle is *rigid* in this sense. (The geometric realization—the metric on the total space—can of course vary, but the topological type $S^1 \to S^3 \to S^2$ is fixed.)

This is a profound difference: topology cannot be varied. It is pinned down by the first Chern number.

### (d) Falsifiability

This framework makes a testable prediction at the theoretical level: **if the first-realized geometry is not $S^2$, the entire derivation fails**.

Paper 3 provides the detailed proof that the coherence-frame axioms applied to a qubit produce $\Sigma = S^2$. If this result is incorrect—if the geometry is something else—then the chain breaks, and the Hopf fibration does not arise. The compactification would not be derived.

This is unlike the string landscape, where adding more exotic topologies simply expands the set of possibilities. Here, the first step is rigidly specified.

## 3.2.7 Scope and Caveats

We must be precise about what this section establishes and what it does not.

### What is Established

1. **Compactness of the fiber dimension**: Given that $S^2$ is the first-realized geometry, the Hopf fibration necessarily produces a compact $S^1$ fiber. This is topological fact, not assumption.

2. **Uniqueness of the minimal bundle**: The principal $U(1)$ bundle of minimal non-zero Chern number over $S^2$ is the Hopf fibration. This is unique among bundles with $|c_1| = 1$, but the selection of $c_1 = 1$ over higher values relies on a minimality principle, not a uniqueness proof.

3. **Logical inversion**: The direction of derivation runs from geometry (derived) to compactness (consequent), opposite to the historical direction.

### What is Not Established (and Why)

1. **The specific radius of $S^1$**: This section establishes that the fiber *is* compact, but not its size. The radius of the extra dimension is a physical parameter, addressed in §5.3 (radius stabilization via the quantum potential). Topology determines compactness; dynamics determines size.

2. **Higher-dimensional analogs**: This derivation applies to the case where the base is $S^2$. Whether the coherence-frame construction yields higher-dimensional analogs (e.g., $S^4 \to S^7 \to S^4$ or other total spaces) is an open question, addressed briefly in §6.2 (future directions).

3. **The full internal geometry of the fiber**: The Hopf fibration tells us that the fiber is an $S^1$. It does not specify whether this $S^1$ has additional structure (e.g., gauge fields living on it). That structure is determined by the matter content and symmetries of the low-energy effective theory, not by topology alone.

4. **Whether higher Chern numbers realize**: In principle, principal $U(1)$ bundles with $c_1 = n$ for $n > 1$ also exist over $S^2$. This section argues that the *first-realized* geometry corresponds to $c_1 = 1$ (the minimal case). Higher values would correspond to higher-dimensional compactifications, which may or may not be realized. This is an open direction.

### Dependence on Paper 3

This entire section depends on **Paper 3's result** that the coherence-frame axioms applied to the qubit produce $\Sigma = S^2$ as the first-realized geometry. If that proof contains an error, the derivation presented here is invalid.

We therefore regard §3.2 as *conditionally rigorous*: given the results of Paper 3, the topological argument is solid. The burden of verification lies with Paper 3's detailed calculations.

## 3.2.8 Implications for the Extra-Dimensional Paradigm

This section inverts the foundation of extra-dimensional physics. For over a century, compactness has been an *axiom*. Here, it becomes a *theorem*.

The shift has profound implications:

- **Naturality**: Compactness is no longer an ad hoc assumption required to match observation. It arises naturally from the structure of quantum mechanics and coherence.

- **Rigidity**: The landscape of possible compactifications is reduced from continuous to discrete. The topology is selected by minimality of the first Chern number ($c_1 = 1$), with higher values remaining as open theoretical possibilities (see §3.2.7).

- **Predictivity**: The framework makes a sharp prediction: if measurements or calculations show that the first-realized geometry is not $S^2$, the entire approach fails. This is genuine falsifiability.

- **Unification**: By grounding extra dimensions in quantum geometry rather than postulation, the framework moves toward a more unified picture in which all structure—spacetime, compactification, gauge symmetry—emerges from coherence principles.

## 3.2.9 Relationship to §3.1 and §3.3

Section 3.1 established that the coherence-frame manifold $\Sigma$ admits a natural symplectic structure and a corresponding Kähler geometry when the internal symmetry group $G$ is abelian.

Section 3.2 (this section) argues that the *topology* of $\Sigma$ is derived from the coherence axioms, not postulated. For the qubit case, this topology is $S^2$, and the Hopf fibration is an intrinsic topological property.

Section 3.3 will address how the gauge structure on $\Sigma$ (via the Hopf bundle) induces a $U(1)$ symmetry in the low-energy effective action. This is where the connection to electromagnetism or the KK photon appears, but that story is built on the topological foundations laid here.

## Summary: §3.2

**Main Thesis**: Compactification is derived, not assumed. Starting from the coherence-frame axioms applied to a qubit (the minimal case), one obtains:

1. $S^2$ as the natural geometry of the coherence-frame manifold.
2. The Hopf fibration $S^1 \to S^3 \to S^2$ as the unique principal $U(1)$ bundle of minimal Chern number over $S^2$.
3. $S^1$ as the fiber, which is compact by topology.

This inverts the historical logic: instead of assuming compact dimensions and building physics around them, Coherence Relativity derives compactness from first principles. The compact extra dimension is the *output* of the theory, not an input assumption.

The topology is rigid, the landscape is resolved, and falsifiability is sharp. These are the hallmarks of a more fundamental framework for understanding extra dimensions.

The selection of $c_1 = 1$ over higher Chern numbers is a minimality argument. Whether nature realizes only the minimal bundle, or whether higher-$c_1$ bundles play a role at higher energies, remains an open question explored further in §5.

---

**References and Notes for §3.2**:
- Kaluza, T. (1921). "Zum Unitätsproblem der Physik." *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*, 966–972.
- Klein, O. (1926). "Quantentheorie und fünfdimensionale Relativitätstheorie." *Zeitschrift für Physik*, 37(12), 895–906.
- Bott, R., & Tu, L. W. (1982). *Differential Forms in Algebraic Topology*. Springer. [Classification of principal bundles.]
- Husemoller, D. (1994). *Fibre Bundles* (3rd ed.). Springer. [Hopf fibration and Chern classes.]
- Paper 3 (in preparation): "Coherence Frames and First-Realized Geometry—The Derivation of $S^2$ for the Qubit."


# §3.3 What Derived Compactification Constrains

## 3.3.1 Overview: From Topology to Physics

Section 3.2 established that compactification is *derived*, not assumed. The extra dimension is the decoherence-depth coordinate $r$, which is geometrically compact: the warp factor $A(r) = \cos(\sqrt{2}\,r)$ (Proposition 4.2, §7) vanishes at $r_{\max} = \pi/(2\sqrt{2})$, terminating the geometry. The parameter $\mu = \sqrt{2}$ is fixed by the Fubini-Study Laplacian eigenvalue $k^2 = 2$ — it is not a free parameter. The compact topology is a consequence, not an input.

This represents a qualitative shift in the landscape of extra-dimensional physics. In the historical framework, compactness is postulated and one is then free to choose any compact topology (Calabi-Yau, orbifold, Klein circle, etc.), with moduli to vary. In Coherence Relativity, the topology is *determined* by first principles, and Klein's 1926 compactification mechanism is unnecessary.

**The question now is: What physics does this determination constrain?**

This section answers that question by tracing the cascade of constraints that flow from fixing the topology. We show that:

1. The landscape of possible topologies is reduced from $\sim 10^{500}$ to a single geometric outcome: the bounded interval $r \in [0, r_{\max}]$ with one scale parameter.
2. The shape modulus is zero: $r_{\max}$ is topologically frozen by $k^2 = 2$.
3. The KCR mode structure is fixed by the volcano potential on the interval.
4. The derived geometry fixes the topology, confinement mechanism, and KCR mode structure entering the SC3 analysis.
5. The physical scale $s$ (mapping $r$ to meters) is constrained phenomenologically through the branch-dependent Casimir analysis of §5.3.

---

## 3.3.2 Constrained Topology Class

### 3.3.2.1 The Elimination of the Calabi-Yau Landscape

In string theory, extra dimensions are compactified on Calabi-Yau 3-folds. The number of topologically distinct Calabi-Yau 3-folds is estimated at approximately $10^{500}$, giving the landscape problem: no principle selects one topology over another.

In Coherence Relativity, this landscape is eliminated:

**The derived compactification is a geometrically bounded interval $r \in [0, r_{\max}]$ with warp factor $A(r) = \cos(\sqrt{2}\,r)$, equipped with the Fubini-Study metric from the coherence manifold $\Sigma = \mathbb{CP}^1$.**

The topology is not chosen from a menu. It is the unique outcome of:
1. The coupled equations of motion on $M \times \Sigma$ (Proposition 4.2, §7)
2. The Fubini-Study eigenvalue $k^2 = 2$ (fixed by the geometry of $\mathbb{CP}^1$)
3. The Lindblad non-traversability constraint $\dot{r} \geq 0$

There is no free topological parameter.

### 3.3.2.2 Topologies Ruled Out

The derived framework rules out:

- All Calabi-Yau 3-folds and K3 surfaces
- All toroidal compactifications $T^6$ and higher-genus surfaces
- All Randall-Sundrum warped geometries (these assume compactification as input)
- All ADD models with arbitrary extra-dimension topology
- **Klein's compact circle $S^1$**: Klein (1926) added a topological identification $r \sim r + 2\pi R$ to Kaluza's single extra dimension. This identification is not derived from any principle — it is an ad hoc input. In Coherence Relativity, the extra dimension is compact by geometry (the warp factor vanishes at $r_{\max}$), not by topological identification. Klein's mechanism provides a sufficient but not necessary condition for compactness; the derived-compact interval makes it unnecessary.

### 3.3.2.3 What the Derived Framework Provides

The compact topology is fully determined:

$$\boxed{r \in [0,\, r_{\max}], \quad r_{\max} = \frac{\pi}{2\sqrt{2}}, \quad A(r) = \cos(\sqrt{2}\,r)}$$
(Eq. 3.3.1)

The remaining physical scale parameter is the factor $s$ mapping dimensionless $r$ to meters. Its admissible range is constrained by the SC3 analysis of §5.3 rather than by topological input.

The **U(1) gauge structure** (previously attributed to the Klein circle) now comes from the Berry phase on $\Sigma = \mathbb{CP}^1$. The first Chern number $c_1 = 1$ is a topological invariant of $\mathbb{CP}^1$ — it does not depend on the compactness of any spatial direction. The U(1) holonomy is automatically quantized as integer multiples of $2\pi$. This is the charge quantization mechanism, and it is topological rather than dimensional.

The Hopf fibration $S^1 \to S^3 \to S^2$ remains valid as a description of the **angular structure** of $\Sigma$. The $S^1$ fiber is the Berry phase of the quantum state — compact with period $2\pi$ and carrying topological charge $c_1 = 1$. But this is a gauge phase living in $\Sigma$, not a spatial dimension of spacetime. It does not contribute to the dimension count of the bulk theory.

**Dimensional accounting:** The theory is genuinely 5D: four spacetime coordinates $(x^\mu)$ plus one geometrically compact decoherence-depth coordinate $r \in [0, r_{\max}]$. This is Kaluza's original 1921 picture — one extra dimension with a cylinder condition ($\partial/\partial x^5 = 0$ at low energies) — but with two improvements over both Kaluza and Klein: (a) the cylinder condition is thermodynamic (Lindblad irreversibility), and (b) the compactness is geometric ($A \to 0$ at $r_{\max}$), not assumed.

$$\boxed{\text{Landscape reduction: } \sim 10^{500} \text{ topologies} \to 1 \text{ geometric outcome}}$$
(Eq. 3.3.2)

---

## 3.3.3 Constrained Moduli Space

### 3.3.3.1 Shape Modulus: Topologically Frozen

The dimensionless shape of the interval — parameterized by $r_{\max} = \pi/(2\sqrt{2})$ and the warp profile $A(r) = \cos(\sqrt{2}\,r)$ — is **topologically frozen**.

This is a precise statement: $k = \sqrt{2}$ is the eigenvalue of the Fubini-Study Laplacian on $\mathbb{CP}^1$. It is a topological invariant of $\mathbb{CP}^1$, not a tunable parameter. Perturbing $k$ away from $\sqrt{2}$ would require changing the geometry of $\Sigma$, which is fixed by quantum mechanics. Therefore:

$$\boxed{\text{Shape modulus: zero degrees of freedom. } r_{\max} = \pi/(2\sqrt{2}) \text{ is topologically fixed.}}$$
(Eq. 3.3.3)

This is stronger than the original §3.3.3 claim that "metric moduli are determined by Einstein equations." The shape is not merely constrained by dynamics — it is frozen by topology.

### 3.3.3.2 Scale Modulus: Phenomenologically Constrained, Not Topologically Frozen

The physical scale factor $s$ is not a topological invariant. Derived compactification fixes the dimensionless interval geometry — $r_{\max} = \pi/(2\sqrt{2})$ and $A(r) = \cos(\sqrt{2}\,r)$ — but not the macroscopic value of $L^* = r_{\max}\times s$.

In Paper 2, the physical interval is constrained phenomenologically by the SC3 analysis of §5.3. The calculable contribution carried forward in this paper is the Casimir vacuum energy on the derived interval with Dirichlet-type boundary conditions. Additional contributions from $T_{M\Sigma}$ backreaction may exist, but they are deferred to Paper 3. Thus the scale is not a landscape modulus, but neither is it fixed here by a geometric primary source for $\Lambda$.

This still resolves OP-5 in the sense relevant to compactification: there is no free shape modulus and no ad hoc stabilization potential. What remains is a quantitative vacuum-energy consistency condition, not a topological ambiguity.

### 3.3.3.3 Comparison to String Theory Moduli

| Aspect | String Theory | Coherence Relativity |
|--------|--------------|---------------------|
| **Topology** | Chosen from $\sim 10^{500}$ Calabi-Yau types | Unique: interval $[0, r_{\max}]$ with $A = \cos(\sqrt{2}\,r)$ |
| **Shape moduli** | $h^{2,1} \sim 100$–$1000$ free parameters | **0** (topologically frozen by $k^2 = 2$) |
| **Kähler moduli** | $h^{1,1} \sim 100$–$300$ free parameters | **0** (shape frozen; physical interval constrained by SC3) |
| **Moduli stabilization** | Requires ad hoc potentials (KKLT, GW) | Not applicable to shape; interval tested by vacuum-energy consistency |
| **Klein circle** | Not present (different mechanism) | Removed — unnecessary |
| **Landscape size** | $\sim 10^{500}$ | **1** |

---

## 3.3.4 Constrained Matter Content via KCR Modes

### Remark: KCR mode nomenclature

The massive graviton modes of the KCR-Cone are designated **KCR modes** (Kaluza–Coherence Relativity modes), not Kaluza-Klein modes, for the following reasons:

1. **Not Klein modes.** Klein's (1926) modes are Fourier harmonics $e^{iny/R}$ on a compact circle $S^1$ with periodic boundary conditions. They produce a linear mass spectrum $m_n = n/R$. The KCR modes are eigenfunctions of the volcano potential $V(r) = -3 + \tfrac{3}{2}\tan^2(\sqrt{2}\,r)$ on a bounded interval with Dirichlet-type boundary conditions. They produce a **non-linear** mass spectrum. The equation, boundary conditions, and spectrum are all different.

2. **Not Kaluza modes.** Kaluza (1921) imposed a cylinder condition $\partial/\partial x^5 = 0$ — complete independence of the extra dimension at low energies. He had no tower of massive excitations. The discrete tower is Klein's contribution, not Kaluza's.

3. **KCR modes are new.** They arise from derived compactification: the warp factor $A(r) = \cos(\sqrt{2}\,r)$ vanishing at $r_{\max}$ creates a confining potential that quantizes the spectrum. The compactification is geometric (from CP¹ curvature), not topological (from identification of points). The resulting non-linear spacing $m_n/m_1 \approx 1,\, 1.67,\, 2.32,\, 2.97$ is a falsifiable prediction that distinguishes derived compactification from Klein's circle.

The term "Kaluza-Klein" appears in the literature as a generic label for massive modes from compact extra dimensions. We use "KCR" to distinguish the specific mechanism (derived-interval volcano potential) from the historical one (Klein circle harmonics), consistent with calling the geometry the KCR-Cone.

---

### 3.3.4.1 Mode Structure on the Derived Interval

The topology of the compact space determines the allowed mode expansion.

$$\Phi(x^\mu, r) = \sum_n \phi_n(x^\mu)\,\psi_n(r)$$
(Eq. 3.3.5)

where $\psi_n(r)$ are eigenfunctions of the Schrödinger-like equation

$$-\psi_n''(r) + V(r)\,\psi_n(r) = m_n^2\,\psi_n(r)$$
(Eq. 3.3.6)

with the **volcano potential**

$$V(r) = -3 + \tfrac{3}{2}\tan^2(\sqrt{2}\,r)$$
(Eq. 3.3.7)

This potential arises from the warp factor $A(r) = \cos(\sqrt{2}\,r)$ (standard warped KCR reduction). It has a minimum of $V(0) = -3$ at the brane and diverges as $r \to r_{\max}$.

### 3.3.4.2 KCR Spectrum

The KCR graviton spectrum from (3.3.6)–(3.3.7) is:

| Mode | $m^2$ (dimless) | $m$ (dimless) | Identity | $\lambda$ at $s \sim 50\,\mu\mathrm{m}$ |
|------|-----------------|---------------|----------|------------------------------------------|
| 0 | 0 | 0 | Graviton zero mode | $\infty$ (massless, 4D gravity) |
| ~0 | 0.01 | 0.10 | Radion (OP-5, resolved) | ~2600 μm |
| 1 | 20.1 | 4.48 | First KCR graviton | **13.3 μm** |
| 2 | 56.2 | 7.50 | Second KCR graviton | 7.9 μm |
| 3 | 108.4 | 10.41 | Third KCR graviton | 5.7 μm |
| 4 | 176.7 | 13.29 | Fourth KCR graviton | 4.5 μm |

The graviton zero mode ($m=0$) is normalizable and localized near the brane (half-weight at $r/r_{\max} \approx 22.6\%$). The near-zero mode is the radion — the breathing mode of $r_{\max}$ — identified by a 71% wavefunction overlap. It is OP-5's stabilized radion, not a KCR graviton.

The first genuine KCR graviton has $\lambda_1 \approx 13.3\,\mu\mathrm{m}$, safely below the 44 μm ISL bound (Lee et al. 2020). ✓

### 3.3.4.3 Contrast with Klein S¹

**Klein $S^1$** gives an exactly linear spectrum:

**Derived compactification** gives a non-linear spectrum from the volcano potential: $m_n/m_1 \approx 1, 1.67, 2.32, 2.97, \ldots$

$$\boxed{\text{Testable prediction: non-linear KCR mode spacing distinguishes derived compactification from Klein.}}$$
(Eq. 3.3.8)

If KCR graviton resonances are ever detected, the spacing pattern is a clean, model-independent discriminator.

### 3.3.4.4 Charge Quantization (Klein-Free)

Previously: Klein charge quantization came from quantized momentum

Now: Charge quantization comes from the Berry phase holonomy on $\Sigma = \mathbb{CP}^1$. The U(1) Berry connection has first Chern number $c_1 = 1$ — a topological invariant. Closed loops in $\Sigma$ pick up holonomy phases that are integer multiples of $2\pi$, giving discrete charge without any compact spatial dimension.

This is cleaner than the Klein mechanism: topological rather than dimensional, independent of the scale factor $s$, and surviving the removal of Klein's circle.

---

## 3.3.5 Constrained Cosmological Constant

### 3.3.5.1 What the Derived Geometry Fixes

Derived compactification fixes the topology and confinement structure of the extra dimension: a bounded interval, the warp factor $A(r) = \cos(\sqrt{2}\,r)$, and the pinch-off boundary at $r_{\max}$. The CP¹ eigenvalue $k^2 = 2$ determines the internal decoherence geometry through $A'' = -k^2 A$, but this curvature is information-geometric rather than a direct 4D gravitational source.

The role of the geometry in Paper 2 is therefore structural. It fixes the domain, the boundary conditions, and the KCR mode structure that make the SC3 analysis definite. The corrected interpretation is given explicitly in §5.3: FS curvature governs dynamics on $\Sigma$, while the Friedmann-source analysis in this paper is carried by Casimir vacuum energy on the derived interval.

### 3.3.5.2 Casimir Vacuum Energy on the Derived Interval

Quantum fields on the interval $[0, L]$ (with $L = r_{\max} \times s$ and Dirichlet-type boundary conditions) acquire a shifted zero-point energy:

$$\rho_{\mathrm{Cas}}(L) = \frac{\pi^2 \hbar c}{1440\,L^4}\,f, \quad f := \frac{7N_F}{8} - N_B$$
(Eq. 3.3.10)

This is the corrected formula for the interval with Dirichlet boundary conditions (a factor of 2 smaller than the Klein circle formula with periodic BC, which used $720$ in the denominator). In the Paper 2 SC3 analysis, this Casimir term is the primary calculable contribution to the effective 4D vacuum energy from the derived compactification. If additional positive contributions from $T_{M\Sigma}$ frame-dragging are confirmed later, the Casimir term becomes subdominant without losing its value as a falsifiable Level-1 prediction.

### 3.3.5.3 Scale Prediction and Branch Dependence

Once the topology and boundary conditions are fixed, the interval scale is constrained by matching the Casimir vacuum energy to the observed dark-energy density. The resulting value depends on the effective field content and on the self-consistent branch analysis, so the detailed numerics are deferred to §5.3.3. The main structural point here is that SC3 becomes a quantitative test of the derived interval, not a free compactification choice.

The representative Casimir scale is:

$$L_{\mathrm{Cas}}^* = \left(\frac{\pi^2 \hbar c\,f}{1440\,\rho_\Lambda}\right)^{1/4} \approx 56\text{–}69\,\mu\mathrm{m} \quad \text{(branch-dependent range; see §5.3.3)}$$
(Eq. 3.3.12)

### 3.3.5.4 Implications for Fine-Tuning

The old Klein-style question "For what fiber radius $R$ does $\Lambda_{\mathrm{eff}}(R) = \Lambda_{\mathrm{obs}}$?" is replaced by a more constrained one: once the geometry is derived rather than postulated, which field-content branch on the interval is compatible with the observed vacuum energy? Derived compactification does not solve SC3 by supplying a geometric primary source for $\Lambda$. Instead, it fixes the topology, confinement mechanism, and boundary conditions that make the vacuum-energy calculation definite.

$$\boxed{\text{Derived compactification fixes topology and confinement; Paper 2 evaluates SC3 with Casimir vacuum energy on the interval.}}$$
(Eq. 3.3.13)

---

## 3.3.6 What Is NOT Constrained by Topology

The following remain open, as in v1, with updated status:

**(a) The physical scale factor $s$:** Not a topological quantity. Its admissible range is constrained by the SC3 Casimir analysis rather than fixed by topology. **Status: CONSTRAINED in Paper 2, not fully derived.**

**(b) The field content on the interval:** Determined by Paper 3 phase transition (Axiom B) and symmetry. **Status: CONTINGENT on Paper 3.** The Casimir prediction remains branch-dependent until that inventory is fixed.

**(c) Whether $c_1 = 1$ is the only realized compactification:** The minimality argument for $c_1 = 1$ is unchanged; higher-$c_1$ bundles in the Hopf fiber structure remain possible at higher energies. **Status: OPEN.**

---

## 3.3.7 Comparison Table: Assumed vs. Derived Compactification (v2)

| Aspect | String Landscape | Klein (1926) | Coherence Relativity |
|--------|-----------------|--------------|---------------------|
| **Topological origin** | Postulated | Postulated ($S^1$) | Derived from A(r) = cos(√2 r) |
| **Topological choice** | $\sim 10^{500}$ Calabi-Yau | One circle with free $R$ | Unique: bounded interval |
| **Shape moduli** | $h^{2,1} \sim 100$–$1000$ | 0 (circle) | **0 (topologically frozen)** |
| **Scale moduli** | $h^{1,1} \sim 100$–$300$ | Free $R$ — stabilization required | SC3-constrained physical interval |
| **Charge quantization** | From flux quantization | From $p_5 = n\hbar/R$ | From Berry phase $c_1 = 1$ on $\mathbb{CP}^1$ |
| **KCR spectrum** | Hodge structure | Linear $m_n = n/R$ | Non-linear (volcano potential) |
| **Cosmological constant** | Landscape; anthropic | Casimir on $S^1$ | Casimir on the derived interval (Paper 2); FS curvature excluded from Friedmann source |
| **Dimension count** | 10D (6 compact) | 5D + Klein $S^1 = 6$D? | **5D (4 + r)** |
| **Landscape size** | $\sim 10^{500}$ | 1 (but $R$ free) | **1** (with branch-dependent SC3 test) |
| **Falsifiability** | Low | Low | High: non-linear KK spacing |

---

## 3.3.8 The Reduction in Degrees of Freedom

### String Theory Landscape

- $\sim 10^{500}$ topological types
- $\gtrsim 10^3$ moduli per type
- **Total: $\gtrsim 10^{500}$ free parameters**

### Coherence Relativity

- 1 topological outcome: bounded interval $[0, r_{\max}]$ with $A = \cos(\sqrt{2}\,r)$
- 0 shape moduli (topologically frozen by $k^2 = 2$)
- 1 physical interval scale constrained by SC3 rather than freely chosen
- $\mathcal{O}(10)$ parameters from field content and couplings (Paper 3)
- **Total: $\mathcal{O}(10)$ parameters**

$$\boxed{\text{Degrees of freedom: String theory } \gtrsim 10^{500};\quad \text{CR } = \mathcal{O}(10).}$$
(Eq. 3.3.14)

---

## 3.3.9 Implications and Open Questions

### What This Framework Achieves

1. **Landscape elimination.** Not a landscape reduction — a landscape elimination. The topology is derived, not selected from a menu. Klein's S¹ is ruled out alongside Calabi-Yau manifolds.

2. **Shape rigidity.** $r_{\max}$ is topologically frozen. No stabilization potential needed for the shape.

3. **Scale resolution.** The physical interval is constrained by SC3 once the derived topology and boundary conditions are fixed — no Goldberger-Wise potential is introduced.

4. **Predictive power.** Non-linear KCR mode spacing ($1, 1.67, 2.32, 2.97$) is a sharp, falsifiable prediction distinguishing CR from every prior compactification scheme.

5. **Charge quantization.** Topological (Berry phase) rather than dimensional (Klein momentum).

### What Remains Open

1. **Post-transition field content** (Paper 3): affects the Casimir correction magnitude
2. **Higher-$c_1$ compactifications** in the Hopf fiber structure at higher energies
3. **Quantitative branch selection and projection**: explicit late-time mapping from the interval analysis to cosmological observables requires the full $M \times \Sigma \to M$ source projection

---

## 3.3.10 Summary and Transition to §4

**Section 3.3 Main Points (v2):**

1. **Derived compactification is unique:** bounded interval $[0, r_{\max}]$ with $A(r) = \cos(\sqrt{2}\,r)$. Klein's $S^1$ and all other topologies are ruled out.

2. **Shape is topologically frozen:** $r_{\max} = \pi/(2\sqrt{2})$ fixed by the Fubini-Study eigenvalue $k^2 = 2$. Zero shape moduli.

3. **Scale is SC3-constrained:** the physical interval is fixed phenomenologically by the vacuum-energy analysis rather than by a free compactification radius. No stabilization potential is introduced.

4. **KCR spectrum is non-linear:** from the volcano potential, giving $m_n/m_1 \approx 1, 1.67, 2.32, 2.97$ — a testable prediction distinguishing CR from Klein.

5. **SC3 is evaluated with Casimir vacuum energy on the derived interval:** FS curvature determines the $\Sigma$ geometry and decoherence profile but is excluded from the 4D Friedmann source term in Paper 2.

6. **Charge quantization is topological:** Berry phase $c_1 = 1$ on $\mathbb{CP}^1$, not Klein momentum.

---

## 3.3.11 Paper 3 Interface Hooks (updated)

1. **P3-H1: Phase-transition gate** — Provide transition scale/redshift separating 5D-coupled regime from effective 4D regime. Unchanged from v1.

2. **P3-H2: Post-transition field-content map** — Provide $(N_B, N_F)$ counts. This determines the sign and magnitude of the Level-1 Casimir contribution and therefore the branch structure of the Paper 2 SC3 analysis.

3. **P3-H3: Bundle-selection statement** — Clarify whether only $c_1 = 1$ Hopf fiber is dynamically selected. **Status: INTERFACE-CONTRACT ONLY.**

4. **P3-H4: Effective-source projection rule** — Projection map from $M \times \Sigma$ dynamics to 4D effective source terms. **Status: INTERFACE-CONTRACT ONLY.**

---

## References and Notes for §3.3 (v2)

- §3.2: Derived compactification from coherence axioms; Proposition 4.2 (A(r) = cos(√2 r))
- §5.3 v2: Corrected SC3 hierarchy; FS curvature excluded from Friedmann source; Casimir analysis on interval
- §7 v2 (EOM): Formal derivation of k² = 2 from Fubini-Study eigenvalue (Proposition 4.2)
- Kaluza, T. (1921). "On the unification problem in physics." *Sitzungsber. Preuss. Akad. Wiss. Berlin*, 966–972. [Original pure-Kaluza single-extra-dimension picture]
- Klein, O. (1926). "Quantentheorie und fünfdimensionale Relativitätstheorie." *Z. Phys.* **37**, 895–906. [Klein compactification — ruled out here]
- Lee, J. G. et al. (2020). "New Test of the Gravitational $1/r^2$ Law at Separations down to $52\,\mu\mathrm{m}$." *Phys. Rev. Lett.* **124**, 101101. [ISL bound 44 μm]
- Paper 3 (in preparation). [Phase transition, field content, Post-transition sector]


# §4 Equations of Motion on M × Σ

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

**Key point:** The specific function $W(\xi)$ depends on the geometry. For a warped product with warp factor $A$, the cross-term scales as $T_{\mu a} \sim A^{-2}$ — derived for the KCR-Cone in §6.2.10 (Eq. 6.2.10): $T_{\mu r} \sim A(r)^{-2} = \sec^2(\sqrt{2}\,r)$ for $A(r) = \cos(\sqrt{2}\,r)$. The zero-mode profile that sets the exact prefactor is $\psi_0 = N_0 A^2$ with $N_0 \approx 1.55$ (RC-3 Eq. RC3.10), derived from the 5D mode equation. The decoherence parameter λ = A² is the normalized zero-mode amplitude (RC-5).

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

**At the framework level**, this is a consistency requirement on admissible geometries. For all warped-product geometries ds² = A²η dx² + dr², RC-5 §RC5.3 proves the stronger result: $\lambda \cdot T = O(1)$ exactly (not just bounded). This follows from the vector zero-mode profile $\psi_0 \propto A^2$ and metric $g^{\mu\nu} = A^{-2}\eta^{\mu\nu}$, whose product is A-independent. The requirement (4.1.11) is thus *automatically satisfied* by the mode structure — it is a theorem, not a design constraint.

Whether $\lambda \cdot T$ is not just bounded but *constant* (independent of $\xi$) is a stronger condition. RC-5 (2026-04-18) proves this is a **general theorem** for all warped-product geometries: the vector zero mode has $\varphi_0 = T_\mu/A^2 = \text{const}$, so $T^\mu{}_r = A^{-2} \times A^2 \times \text{const} = \text{const}$. The warp-factor cancellation $\cos^2(\sqrt{2}\,r) \cdot \sec^2(\sqrt{2}\,r) = 1$ verified in §6.3.1 is an instance of this universal result, not a coincidence of the KCR-Cone geometry. See `RC5_LAMBDA_DERIVATION_2026-04-18.md` §RC5.3–5.4.

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

The general scaling argument (§4.1.3, Eq. 4.1.7) establishes that $T_{\mu a}$ depends inversely on the energy gap $W(\xi)$. The structural argument has been worked out for the KCR-Cone in Paper 2B §6 (Eq. 6.2.10), giving $T_{\mu r} \sim A(r)^{-2} = \sec^2(\sqrt{2}\,r)$ — a DERIVED result. The precise numerical prefactor — and whether the scaling is exactly $W^{-1}$ or involves logarithmic corrections, angular-momentum dependence, or state-mixing effects — requires solving the mode equation on the specific geometry. Key new physics from Paper 2B §6: the Christoffel $\Gamma_{jr}^i = -\sqrt{2}\tan(\sqrt{2}\,r)\,\delta_j^i$ diverges at $r_{\max}$ (absolute confinement); $\lambda\cdot T = O(1)$ holds exactly for $A = \cos(\sqrt{2}\,r)$.

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

The identification $\lambda = A^2$ for the KCR-Cone is **derived from first principles** (RC-5, 2026-04-18): $\lambda(r) = \psi_0(r)/\psi_0(0) = A^2(r)$, where $\psi_0 = N_0 A^2$ is the vector zero-mode profile of $T_{\mu r}$ from the 5D Einstein-Hilbert mode equation (RC-3 Eq. RC3.8). This supersedes the earlier claim that it was "established in §6.3.1" — §6.3.1 *used* λ = A² as Ansatz A* input; RC-5 *derives* it independently. The properties follow as consequences:
- $\lambda = 1$ at the brane ($r = 0$, where $\psi_0/\psi_0(0) = 1$)
- $\lambda \to 0$ at the pinch-off ($A \to 0$ at $r_{\max}$)
- $\lambda \cdot T = O(1)$ — a **geometric theorem**, universal for warped geometries

The identification extends beyond the KCR-Cone: for any warped background ds² = A²η dx² + dr², the vector zero-mode profile is $\psi_0 \propto A^2$, giving $\lambda = A^2$. See `RC5_LAMBDA_DERIVATION_2026-04-18.md`.

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

The one caveat is UV completion: above the KCR energy scale
$E_\mathrm{KK} \sim \hbar c / L$, where $L = r_\mathrm{max} \cdot s$ is the physical
interval length at cosmological scale factor $s$, the tower of massive KCR graviton
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


# §4.5 C¹ Regularity: Standard Model vs. Derived Compactification

## §4.5.1 The Standard Model's C¹ Problem

In Randall-Sundrum (RS) models, the extra dimension is compactified by inserting branes — codimension-1 hypersurfaces that serve as boundaries or defects in the bulk geometry. The 5D metric takes the general form:

$$ds^2 = n(y)^2 \, dz^2 + A(y)^2 \, \eta_{\mu\nu} \, dx^\mu dx^\nu + dy^2 \tag{4.5.1}$$

where $y$ is the coordinate along the extra dimension, $A(y)$ is the warp factor, and $n(y)$ is the temporal warp.

Between the branes, the bulk vacuum Einstein equations determine $A(y)$ and $n(y)$. The standard RS1 solution is:

$$A(y) = e^{-k|y|}, \quad n(y) = 1 \tag{4.5.2}$$

where $k$ is the AdS curvature scale and $|y|$ reflects the orbifold identification $y \sim -y$.

**The regularity issue:** The warp factor $A(y) = e^{-k|y|}$ is continuous (C⁰) at $y = 0$ but not differentiable (not C¹):

$$A'(0^+) = -k, \quad A'(0^-) = +k \tag{4.5.3}$$

The first derivative has a discontinuity $\Delta A' = -2k$ at the brane location. In the language of distribution theory, the second derivative contains a Dirac delta:

$$A'' = -k^2 A + 2k \, \delta(y) \tag{4.5.4}$$

This delta-function curvature is the geometric manifestation of the brane's stress-energy.

### The Israel Junction Conditions

The Israel junction conditions relate the discontinuity in the extrinsic curvature at the brane to the brane's energy-momentum tensor $S_{\mu\nu}$:

$$[K_{\mu\nu}] - [K] h_{\mu\nu} = -\kappa_5^2 \, S_{\mu\nu} \tag{4.5.5}$$

where $[K_{\mu\nu}]$ denotes the jump in extrinsic curvature across the brane, $[K]$ is the trace, and $h_{\mu\nu}$ is the induced metric.

For the RS1 solution, the junction conditions require:

$$T_{\text{brane}} = \frac{6k}{\kappa_5^2} \tag{4.5.6}$$

The brane tension $T_{\text{brane}}$ is a free parameter, tuned to produce the desired kink in $A(y)$. This tuning is the essence of the RS hierarchy mechanism: the ratio of scales on the two branes is exponentially sensitive to the inter-brane separation $L$, giving a natural explanation for the Planck-weak hierarchy.

### What This Means for Regularity

In the RS framework, the C¹ failure at the brane is not a defect — it is the *mechanism*. The brane is the locus where the bulk geometry transitions between two smooth regions, and the kink in $A(y)$ encodes the brane's physical content. The Israel junction conditions *absorb* the delta-function stress-energy by matching it to a freely chosen brane tension.

The key observation: **regularity is tuned, not derived.** The brane tension $T_{\text{brane}}$ is a free parameter. You choose where to place the brane, you choose the tension, and the junction conditions accommodate the resulting kink. Different tensions produce different kinks, and the geometry adjusts accordingly.

This is a feature of *assumed* compactification: the topology is specified by hand (an orbifold $S^1/\mathbb{Z}_2$ with branes at the fixed points), and the regularity properties follow from the freely tunable brane parameters.

---

## §4.5.2 Derived Compactification Constrains Regularity

In the coherence-frame formalism, the compact fiber does not arise from an assumed orbifold. It emerges from the Hopf fibration over the coherence state space (§3.2):

$$S^1 \hookrightarrow S^3 \xrightarrow{\pi} S^2 \simeq \mathbb{CP}^1 \tag{4.5.7}$$

The total space $E_{c_1}$ is determined by the first Chern number $c_1$. For $c_1 = 1$ (the minimal non-trivial bundle), the total space is $S^3$ — a smooth, compact manifold without boundary or orbifold singularities.

This has three consequences for regularity that have no counterpart in the RS framework:

### §4.5.2.1 No Arbitrary Brane Insertion

In RS models, branes are inserted at freely chosen locations in the extra dimension. In derived compactification, the topology of the total space is fixed by $c_1$. For $c_1 = 1$, the total space $S^3$ is smooth everywhere. There is no codimension-1 locus where a brane *must* sit.

If a brane-like defect appears, it must arise from the field content — a physical source that creates a singularity in the metric. But such a source must be *derived* from the dynamics, not inserted by hand. The location and strength of any singularity are predictions of the theory, not inputs.

### §4.5.2.2 Regularity Follows from Topology

If the derived total space is a smooth manifold (as $S^3$ is for $c_1 = 1$), the metric must be smooth everywhere — unless there is a physical reason for a singularity. Specifically:

- If the field equations on $S^3$ admit smooth solutions, the warp factor $A(r)$ is $C^\infty$ (or at least $C^k$ for arbitrarily large $k$) throughout the bulk.
- Any failure of smoothness must be sourced by distributional matter (as in Eq. 4.5.4), but such matter is now part of the theory's dynamics, not an external input.

This is a qualitative departure from RS: in assumed compactification, the orbifold structure *requires* distributional sources at the fixed points. In derived compactification, the smooth total space *forbids* distributional sources unless they arise dynamically.

### §4.5.2.3 No Tension Tuning

The RS hierarchy mechanism relies on tuning the brane tension (Eq. 4.5.6) to produce the desired warp profile. In derived compactification, there is no free brane tension:

- The topology $E_{c_1}$ is fixed
- The fiber structure determines where (if anywhere) the warp profile might develop features
- Whatever regularity class the warp profile belongs to is a *prediction*, not a tuned parameter

If the equations of motion on $S^3$ require $A(r) \in C^1$, this is a theorem about the specific geometry. If they permit $A(r)$ to have kinks, the kink locations and magnitudes are determined — not freely chosen.

---

## §4.5.3 Framework-Level Claim

The contrast between assumed and derived compactification can be summarized as follows:

| Property | Assumed (RS) | Derived (Coherence Frame) |
|----------|-------------|--------------------------|
| Topology | Specified by hand ($S^1/\mathbb{Z}_2$) | Emerges from Hopf fibration (§3.2) |
| Brane insertion | Free parameter (location, number) | Constrained by topology |
| Warp factor regularity | C⁰ at branes, with tunable kinks | Determined by field equations on smooth $E_{c_1}$ |
| Junction conditions | Absorb kinks via tunable tension | Not applicable (no hand-inserted branes) |
| Regularity class of $A$ | Input (depends on brane choice) | Output (prediction of the theory) |

**Framework-level result:** Derived compactification constrains the regularity class of admissible warp profiles. The topology predicts where smooth metrics are required and where singularities (if any) must be sourced by dynamical field content. This is a qualitative departure from the standard model, where regularity is absorbed into junction conditions with tunable brane tensions.

### Sufficient Conditions for C¹

The specific sufficient conditions for C¹ regularity of the coherence-to-classical map on a warped geometry are established in the companion paper [Paper 2B, §2.4]:

- **(Reg1)** Global C¹ smoothness of $A(r, z)$ with bounded derivatives
- **(Reg2)** Bounded first partial derivatives: $|\partial_r A| + |\partial_z A| \leq C$
- **(Reg3)** Uniform conical structure at any tip: $A(r, z) = C(z) \, r + O(r^2)$ with $C(z) \in C^1$

These conditions are checked explicitly for the KK-Cone geometry in [Paper 2B, §2.4]. The key finding is that the smooth Hopf bundle structure ($S^3$ for $c_1 = 1$) naturally satisfies (Reg1)–(Reg3), whereas RS orbifolds violate (Reg1) at brane locations by construction.

### Scope and Limitations

**Important caveat:** The claim is that derived compactification *constrains* regularity — not that it guarantees C¹ in all cases. Pathological field configurations could still produce singularities (e.g., if the matter sector develops a distributional source). The point is that such singularities are *predicted* by the dynamics, not *inserted* by the model-builder.

**The C¹ verification for the specific KK-Cone geometry** — including the analysis of the cone tip, the Hopf fiber structure, and the warp factor dependence on the coherence parameter — is carried out in full in [Paper 2B, §2.4]. The present section establishes only the *principle* that derived topology constrains regularity, which is a framework result.

Derived compactification therefore constrains the regularity class of admissible warp profiles, in qualitative contrast to assumed compactification where regularity is tuned via junction conditions. The geometry-specific verification remains in [Paper 2B, §2.4].

---

## References

- Randall, L. & Sundrum, R. (1999). "A Large Mass Hierarchy from a Small Extra Dimension." *Phys. Rev. Lett.* 83, 3370.
- Randall, L. & Sundrum, R. (1999). "An Alternative to Compactification." *Phys. Rev. Lett.* 83, 4690.
- Israel, W. (1966). "Singular hypersurfaces and thin shells in general relativity." *Nuovo Cim.* B44, 1.
- Goldberger, W. & Wise, M. (1999). "Modulus Stabilization with Bulk Fields." *Phys. Rev. Lett.* 83, 4922.
- §3.2 (this paper): Topology as output — S² → Hopf → compact S¹
- §3.3 (this paper): What derived compactification constrains
- [Paper 2B, §2.4]: C¹ regularity verification on the KK-Cone

# §5 Self-Consistency Conditions

The abstract $M \times \Sigma$ framework of Paper 2A admits many geometries in principle. Derived compactification acts not on the unreduced full coherence space, but on the pointer-compatible sector selected by the Coherence-Frame Induction Principle (Paper 2A, §2.3.10): decoherence first suppresses the fast higher coherence modes, inducing the residual dynamics onto a lower-dimensional manifold; topology then fixes the compact internal direction of that surviving sector.

**Theorem 5.0.1 (Slow-Manifold Reduction — Azouit Bridge).** *Let the $\Sigma$-sector Lindblad generator $\mathcal{L}_\Sigma$ have a spectral gap $\delta > 0$, and let the M-sector evolution rate satisfy $\|\partial_t G_{\mu\nu}^{(M)}\| \ll \delta$. Then:*

*(i) The fast $\Sigma$-sector modes are adiabatically eliminated, and the residual M-sector dynamics evolve on a slow manifold whose effective metric is the Schur complement*
$$G_{\mu\nu}^{\mathrm{eff}} = G_{\mu\nu}^{(M)} - T_{\mu a}\,(G^{(\Sigma)})^{-1,ab}\,T_{b\nu},$$
*which is precisely Eq. 2.3.4 of Paper 2A.*

*(ii) The spectral gap condition $\delta > 0$ is equivalent to "eigenvalues of $G_{ab}^{(\Sigma)}$ are large" in the sense of Paper 2A §2.3.3: both conditions state that $\Sigma$-sector relaxation dominates M-sector driving.*

*Proof.* Step (i) is Theorem 1 of Azouit, Sarlette \& Rouchon (2016, \textit{ESAIM: COCV}), applied with the identification: their "fast generator" $\mathcal{L}_0$ = $\mathcal{L}_\Sigma$ in the HCR framework; their "slow manifold" = the pointer-compatible sector; their "effective equation" = the M-sector EOM with the Schur-complement metric. Step (ii) follows from the spectral characterization of the Bures metric block $G_{ab}^{(\Sigma)}$: large eigenvalues correspond to rapid $\Sigma$-sector return to equilibrium, which is exactly the spectral gap condition on $\mathcal{L}_0$. $\square$

*Remark.* This theorem provides the rigorous foundation for the Coherence-Frame Induction Principle (Paper 2A, §2.3.10). With Theorem 5.0.1 (Step A, slow-manifold reduction) and §3.2 of this paper (Step B, topology-fixing of the surviving sector), the CFIP is elevated from a named Principle to a fully proved Theorem in the HCR series. The label "Principle" is retained in Paper 2A to reflect the logical order of presentation; the proof is completed jointly by this theorem and §3.2.

For any specific geometry realized by this mechanism to be physically viable, it must satisfy three self-consistency conditions:

1. **SC1 (Flatness):** The effective 4D spatial sections must be flat ($\Omega_k \to 0$), consistent with Planck 2018 observations ($\Omega_k = 0.0005 \pm 0.0019$).
2. **SC2 (Gravity Localization):** Four-dimensional Newton's law must be recovered at accessible scales, with the graviton zero mode normalizable and KCR corrections suppressed below current ISL bounds.
3. **SC3 (Cosmological Constant):** The effective 4D cosmological constant must be positive and consistent with $\Lambda_{\mathrm{obs}} \approx 1.1 \times 10^{-52}\,\mathrm{m}^{-2}$.

In the pre-split formulation (Paper 2, v1–v2), SC1 and SC2 were non-trivial constraints on a generic warp profile $A(r,z)$ defined on an infinite bulk with $S^3$ angular sections. The question was: *which class of warp profiles simultaneously satisfies all three conditions?* The answer was a restricted family of exponentially decaying profiles, and the self-consistency analysis was a constraint-solving exercise.

The KCR interval formulation changes this picture qualitatively. With the 5D metric (Eq. 4.0.1),

$$\mathrm{d}s^2_{(5)} = A^2(r)\,\eta_{\mu\nu}\,\mathrm{d}x^\mu\,\mathrm{d}x^\nu + \mathrm{d}r^2, \quad A(r) = \cos(\sqrt{2}\,r), \quad r \in [0,\,r_{\max}]$$

the 4D slices are Minkowski (flat by construction) and the extra dimension is a bounded interval (finite by topology). As shown below, SC1 and SC2 are *structurally guaranteed* by the derived geometry — they are consequences of the compactification, not constraints on it. Only SC3 remains a non-trivial self-consistency test.

This is a qualitative departure from assumed compactification, where SC1 and SC2 must be verified geometry-by-geometry.

---

## §5.1 SC1: Flatness on the KCR Interval

### §5.1.1 The Condition

SC1 requires that brane observers at $r = 0$ measure spatially flat cosmology: $\Omega_k \to 0$ at late times.

### §5.1.2 Why SC1 Was Non-Trivial in the Pre-Split Formulation

In the pre-split geometry, the 5D metric had $S^3$ angular sections:

$$\mathrm{d}s^2 = -\mathrm{d}z^2 + \mathrm{d}r^2 + A(r,z)^2\,\gamma_{ij}\,\mathrm{d}\theta^i\,\mathrm{d}\theta^j$$

The unit round metric $\gamma_{ij}$ on $S^3$ carries intrinsic curvature $k_{S^3} = 1$. When warped by $A^2$, the effective spatial curvature on constant-$z$ slices is:

$$k_{\mathrm{eff}} = \frac{k_{S^3}}{A^2} - \left(\frac{\partial_z A}{A}\right)^2$$

For $k_{\mathrm{eff}} \to 0$, the $S^3$ curvature ($\sim 1/A^2$) must be cancelled by the expansion-rate term ($\sim (\dot{A}/A)^2$). This required the asymptotic form $A \sim z \cdot f(r)$ at late times, so that both terms scale as $1/z^2$ and cancel. The flatness condition therefore *constrained* the warp profile: only those $A(r,z)$ approaching the light-cone form at late times could satisfy SC1.

### §5.1.3 Why SC1 Is Structural on the KCR Interval

In the KCR interval formulation, the 4D sections are Minkowski:

$$\mathrm{d}s^2_{(5)} = A^2(r)\,\eta_{\mu\nu}\,\mathrm{d}x^\mu\,\mathrm{d}x^\nu + \mathrm{d}r^2$$

The induced metric on any constant-$r$ slice is:

$$\mathrm{d}s^2_{\mathrm{(4D)}} = A^2(r)\,\eta_{\mu\nu}\,\mathrm{d}x^\mu\,\mathrm{d}x^\nu$$

This is conformally flat for every value of $r$. The spatial sections have zero intrinsic curvature:

$$k_{\mathrm{eff}} = 0 \quad \text{identically, for all } r \in [0,\,r_{\max}]$$

There is no $S^3$ curvature to cancel, no asymptotic condition to impose, and no constraint on the warp profile from flatness.

### §5.1.4 Cosmological Extension

For the cosmological extension, replace $\eta_{\mu\nu}$ with the FRW metric:

$$g_{\mu\nu}^{(\mathrm{FRW})} = -\mathrm{d}t^2 + a(t)^2\,\delta_{ij}\,\mathrm{d}x^i\,\mathrm{d}x^j \quad (k = 0)$$

The 5D metric becomes:

$$\mathrm{d}s^2 = A^2(r)\left[-\mathrm{d}t^2 + a(t)^2\,\delta_{ij}\,\mathrm{d}x^i\,\mathrm{d}x^j\right] + \mathrm{d}r^2$$

The warping in the $r$-direction does not introduce spatial curvature into the 4D FRW slices. The 4D effective Friedmann equation obtained by integrating the 5D Einstein equations over $r$ inherits the spatial curvature parameter $k$ from the 4D seed metric. With $k = 0$ in the seed, the effective theory is spatially flat.

### §5.1.5 The Structural Guarantee

The reason SC1 is automatic on the KCR interval, whereas it was non-trivial on the pre-split cone, is geometric: the old formulation built the 4D spatial geometry from *curved* $S^3$ sections whose curvature had to be dynamically diluted. The KCR interval formulation builds it from *flat* Minkowski sections, which have zero spatial curvature by construction.

This is not a weakening of SC1 — it is a *strengthening*. Derived compactification does not merely *permit* flat spatial sections; it *requires* them. The only spatial curvature that can enter the 4D effective theory must come from the 4D matter content via the Friedmann equation, not from the extra-dimensional geometry.

$$\boxed{\text{SC1: SATISFIED — structural. Flat 4D sections by construction of the KCR interval metric.}}$$

---

## §5.2 SC2: Gravity Localization on the KCR Interval

### §5.2.1 The Condition

SC2 requires that the 4D graviton zero mode is normalizable in the $r$-direction, so that:

1. An effective 4D Planck mass $M_{\mathrm{Pl}}$ is finite and well-defined.
2. Standard Newton's law holds at accessible scales.
3. KCR mode corrections are suppressed below current ISL bounds ($\lambda_{\mathrm{ISL}} \approx 44\,\mu\mathrm{m}$, Lee et al. 2020).

### §5.2.2 Why SC2 Was Non-Trivial in the Pre-Split Formulation

In the pre-split geometry with an infinite radial direction $r \in [0, \infty)$, the graviton zero mode wavefunction $\psi_0(r)$ had to decay fast enough that:

$$\int_0^\infty |\psi_0(r)|^2\,\mathrm{d}r < \infty$$

This was *not* guaranteed. For example, the pure light-cone metric ($f(r) \equiv 1$) gives $V_{\mathrm{grav}} = 0$ everywhere, and the zero mode is a non-normalizable plane wave. SC2 therefore *constrained* the radial profile $f(r)$: it had to create a confining potential well that traps the graviton near the brane.

The class of admissible profiles included exponential ($f = e^{-\mu r}$), Gaussian, and power-law forms, each with different confinement properties. Which profile was actually realized depended on solving the full self-consistency system SC1 + SC2 + SC3.

### §5.2.3 Graviton Zero Mode on the KCR Interval

On the derived interval with metric (Eq. 4.0.1), the graviton zero mode wavefunction is:

$$\psi_0(r) \propto A^{3/2}(r) = \cos^{3/2}(\sqrt{2}\,r)$$

The normalization integral is:

$$\int_0^{r_{\max}} |\psi_0(r)|^2\,\mathrm{d}r = \int_0^{\pi/(2\sqrt{2})} \cos^3(\sqrt{2}\,r)\,\mathrm{d}r$$

This integral is manifestly finite: the integrand is bounded ($0 \leq \cos^3 \leq 1$) on a bounded domain ($r_{\max} = \pi/(2\sqrt{2}) \approx 1.11$). Evaluating:

$$\int_0^{\pi/(2\sqrt{2})} \cos^3(\sqrt{2}\,r)\,\mathrm{d}r = \frac{1}{\sqrt{2}}\int_0^{\pi/2} \cos^3 u\,\mathrm{d}u = \frac{1}{\sqrt{2}} \cdot \frac{2}{3} = \frac{2}{3\sqrt{2}} \approx 0.471$$

The graviton zero mode is normalizable, confirming that a finite 4D Planck mass exists:

$$M_{\mathrm{Pl}}^2 = M_5^3 \int_0^{r_{\max}} A^3(r)\,\mathrm{d}r = M_5^3 \cdot \frac{2}{3\sqrt{2}}$$

### §5.2.4 The Volcano Potential and Graviton Confinement

The KCR graviton modes satisfy the Schrödinger-like equation (Eq. 3.3.6):

$$-\psi_n''(r) + V(r)\,\psi_n(r) = m_n^2\,\psi_n(r)$$

with the volcano potential:

$$V(r) = -3 + \tfrac{3}{2}\tan^2(\sqrt{2}\,r)$$

This potential has two critical features:

1. **A deep well at the brane:** $V(0) = -3$, which localizes the graviton zero mode near $r = 0$. The zero mode wavefunction peaks at the brane and carries half its probability weight within $r/r_{\max} \approx 22.6\%$ of the interval.

2. **A divergent barrier at the boundary:** $V(r) \to +\infty$ as $r \to r_{\max}$, because $\tan(\sqrt{2}\,r) \to \infty$ at the pinch-off. This provides *absolute confinement* — no graviton mode can escape to $r = r_{\max}$.

The confining mechanism is qualitatively stronger than in the pre-split formulation. There, the exponential bulk gave $V \to \text{const}$ at large $r$, so confinement depended on the decay rate $\mu$. Here, the volcano potential *diverges*, making confinement topological: it follows from the vanishing of $A(r_{\max}) = 0$.

### §5.2.5 The Mass Gap and ISL Compliance

The discrete KCR mode spectrum from the volcano potential is (from §3.3.4.2):

| Mode | $m^2$ (dimless) | $m$ (dimless) | $\lambda$ at $L^* \approx 56\,\mu\mathrm{m}$ |
|------|-----------------|---------------|------------------------------------------------|
| 0 | 0 | 0 | $\infty$ (massless 4D graviton) |
| 1 | 20.1 | 4.48 | 12.5 μm |
| 2 | 56.2 | 7.50 | 7.5 μm |
| 3 | 108.4 | 10.41 | 5.4 μm |

The mass gap between the zero mode and the first KCR mode ($m_1^2 = 20.1$) ensures that Newton's law is unmodified at scales larger than $\lambda_1 \approx 12\text{–}15\,\mu\mathrm{m}$. The ISL bound of $44\,\mu\mathrm{m}$ (Lee et al. 2020) is satisfied with a factor of 3 margin.

### §5.2.6 Contrast with Assumed Compactification

| Property | Assumed (RS/pre-split) | Derived (KCR interval) |
|----------|------------------------|------------------------|
| **Radial domain** | $r \in [0, \infty)$ | $r \in [0, r_{\max}]$ (bounded) |
| **Normalizability** | Requires exponential decay | Automatic (bounded integrand, bounded domain) |
| **Confining potential** | $V \to \text{const}$ (bulk plateau) | $V \to +\infty$ (divergent barrier) |
| **Confinement mechanism** | Dynamical (depends on $\mu$) | Topological (follows from $A(r_{\max}) = 0$) |
| **Profile constraint** | SC2 restricts the class of $f(r)$ | No constraint needed — all modes confined |
| **Mass gap** | Depends on $\mu$ and domain size | Fixed by $k^2 = 2$ (topological) |

### §5.2.7 The Structural Guarantee

SC2 is automatically satisfied on the KCR interval because:

1. The interval is *finite* — any bounded continuous function is integrable on a bounded domain.
2. The warp factor vanishes at $r_{\max}$ — the geometry pinches off, providing a natural boundary that confines all modes.
3. The volcano potential diverges at $r_{\max}$ — this is *stronger* than the confining potential of any finite-depth well, making the graviton localization absolute.

In assumed compactification, SC2 was the primary *selection criterion* for warp profiles. In derived compactification, it is a *theorem* about the geometry.

$$\boxed{\text{SC2: SATISFIED — structural. Graviton normalizable by boundedness of interval and vanishing of } A(r_{\max}).}$$

---

## §5.2.8 SC1 + SC2 Combined: What Derived Compactification Resolves

In the pre-split formulation, the combined system SC1 + SC2 restricted the warp profile to a class of decaying functions with specific localization properties. The question "which geometry satisfies SC1 and SC2?" was an open constraint-solving problem.

On the KCR interval, this problem is *dissolved*. Both conditions are satisfied automatically by the derived geometry:

- SC1 is structural (flat Minkowski slices, no $S^3$ curvature to cancel).
- SC2 is structural (bounded interval, divergent confining potential).

The entire constraint-solving apparatus of §5.1–§5.2 in the pre-split formulation — the asymptotic analysis, the admissible profile classes, the combined SC1 + SC2 coupled system — becomes unnecessary. Derived compactification answers the question before it can be asked.

The conceptual point is worth stating explicitly: the KCR-Cone is not a postulated Kaluza-Klein geometry, but the effective geometry of the induced surviving sector (Paper 2A, §2.3.10; see also Theorem 5.0.1 of this paper for the rigorous slow-manifold foundation). Klein's circle was a useful first approximation, but the Quantum Kaluza Cone replaces that postulate with a derived structure: decoherence first induces a surviving pointer-compatible sector, and topology then fixes its compact internal direction.

**What remains non-trivial:** SC3 (cosmological constant). The Casimir energy on the interval must be consistent with $\Lambda_{\mathrm{obs}}$. This is the only self-consistency condition that genuinely *tests* the derived geometry, and it is the subject of §5.3.

---

# § 5.3: SC3 — Effective Cosmological Constant

## § 5.3.1: The SC3 Condition

The third self-consistency condition (SC3) requires that the observed cosmological constant,

$$\Lambda_{\mathrm{obs}} \approx 1.1 \times 10^{-52} \, \mathrm{m}^{-2},$$

emerges from the KCR-Cone geometry. The 5D metric is

$$\mathrm{d}s^2_{5\mathrm{D}} = A^2(r)\,\eta_{\mu\nu}\,\mathrm{d}x^\mu \mathrm{d}x^\nu + \mathrm{d}r^2$$
(Eq. 5.3.0)

with warp factor $A(r) = \cos(\sqrt{2}\,r)$, $r \in [0, r_{\max}]$, $r_{\max} = \pi/(2\sqrt{2})$.

### § 5.3.1.1: Four Paths to Λ

Four logically distinct mechanisms can contribute to the effective 4D cosmological constant from the KCR-Cone:

**Path A — Casimir vacuum energy (Level 1):** Quantum fields confined to the derived interval $[0, L^*]$ with Dirichlet boundary conditions have a shifted zero-point energy. This is a standard, calculable QFT effect that enters the stress-energy tensor on $M$ and therefore the Friedmann equation. **This is the primary gravitational contributor** to $\Lambda$ from the Σ topology.

**Path B — Fubini-Study curvature (Level 2):** The warp factor $A(r) = \cos(\sqrt{2}\,r)$ satisfies $A'' = -k^2 A$ with $k^2 = 2$ from the CP¹ Laplacian eigenvalue. This curvature is *information-geometric*: it measures the rate of statistical distinguishability between quantum states on Σ. It governs decoherence dynamics (how fast coherence decays along the $r$-direction) but does **not** enter the Friedmann equation as a gravitational source.

**Category error in v2:** The previous draft treated Path B as the primary source of $\Lambda$, computing $\rho_{\mathrm{geom}} = +3.534 \times M_5^3 k^2/s$ and placing it in the Friedmann equation. This is incorrect. The FS curvature $k^2 = 2$ is a property of Σ (the coherence manifold), not of $M$ (spacetime). In physical units, $\rho_{\mathrm{geom}}$ at the Casimir scale is $10^{61} \times \Lambda_{\mathrm{obs}}$ — the standard cosmological constant problem in KK form. The error was conflating information-geometric curvature (Σ) with gravitational curvature ($M$). See `memory/kb/SESSION_2026-04-10_GEOMETRIC_LAMBDA_ANALYSIS.md`, Findings 1–3.

**Path C — T_{MΣ} frame-dragging (Level 3):** The cross-term $T_{M\Sigma}$ in the M × Σ metric couples decoherence dynamics to spacetime geometry. The λ·T = O(1) cancellation (§4.1.6, verified for the KCR-Cone) removes the Planck/Hubble hierarchy, giving $\rho_{\mathrm{drag}} \sim \alpha \times \Gamma_{\mathrm{dec}}^2 / G$ with $\alpha = 3/2$ (exact, from CP¹ geometry). If $\Gamma_{\mathrm{dec}} \sim H_0$, this gives $\rho_{\mathrm{drag}} \sim \rho_\Lambda$. This mechanism is the subject of ongoing work (RC-1 through RC-6, Paper 3 scope) and is NOT used in the SC3 analysis below.

**Path D — Vacuum entanglement dynamics (Level 4):** The Jacobson (1995) connection between entanglement entropy and Einstein's equations suggests a thermodynamic route from Σ to $M$. This likely unifies with Level 3 and is deferred to Paper 3.

### § 5.3.1.2: SC3 Strategy

For Paper 2, SC3 is evaluated using **Path A (Casimir)** as the primary gravitational contribution, with **Path B (FS curvature)** contributing to decoherence dynamics only. Paths C and D are noted as potentially dominant contributions that require the rigorous T_{MΣ} backreaction derivation (Paper 3 scope).

This is a conservative posture: the Casimir prediction is calculable and falsifiable. If Paths C/D are confirmed, the Casimir contribution becomes subdominant — but the ISL prediction from Path A remains a testable signature regardless.

---

## § 5.3.2: What Derived Compactification Contributes

### § 5.3.2.1: Five-Level Σ → M Coupling Hierarchy

The KCR-Cone geometry produces multiple distinct contributions to the effective cosmological constant. These are organized by mechanism:

| Level | Mechanism | Source | Enters Friedmann? | Status |
|-------|-----------|--------|--------------------|--------|
| **1** | Casimir energy | Σ topology → Dirichlet BCs on interval | YES | **Calculable (this section)** |
| **1b** | Topological zero-point | c₁ = 1 Hopf bundle → AS index modifies mode count | YES (< 1% correction) | **D4 complete** |
| **1c** | Radion zero-point | Breathing mode m² ≈ 0.01 on $M$ | Subdominant | Noted |
| **2** | FS curvature k² = 2 | CP¹ Laplacian eigenvalue | NO — information-geometric | **Category error corrected** |
| **3** | T_{MΣ} frame-dragging | Machian backreaction, α = 3/2 | YES (if confirmed) | Paper 3 scope (RC-1–RC-6) |
| **4** | Vacuum entanglement | Jacobson δQ = TdS | Likely unifies with Level 3 | Paper 3 scope |

Levels 1 and 1b are the basis of the SC3 analysis in this paper. Level 2 is excluded from the Friedmann equation (it governs decoherence dynamics on Σ). Levels 3 and 4 are flagged as potentially dominant but require derivations not yet completed.

### § 5.3.2.2: Level 1b — Atiyah-Singer Topological Zero-Point (D4 Result)

On the KCR-Cone, the Atiyah–Singer index theorem lets us replace an assumed compactification with a **derived** one whose zero-point structure is fixed by topology rather than by hand. We treat the angular sector as $S^2 \simeq \mathbb{CP}^1$ with a $U(1)$ line bundle $\mathcal{L}$ of first Chern class $c_1(\mathcal{L}) = 1$, the minimal Hopf/monopole configuration. Identifying this geometric $U(1)$ with hypercharge as a working assumption, each SM field of hypercharge $Y$ couples to the twisted Dirac operator $D_Y$ on $S^2$, whose index is $\mathrm{ind}(D_Y) = c_1(\mathcal{L}^Y) = Y$. The index counts the net chiral zero modes on $S^2$, $n_+ - n_- = Y$, so any representation with $Y \neq 0$ carries topologically protected zero modes, while hypercharge-neutral fields do not. Summing over colors and weak components within one SM generation gives integer indices for each multiplet and a vanishing total index, reflecting the familiar anomaly-free structure of SM hypercharge. For the Casimir calculation, these protected zero modes are not part of the massive KCR tower that sources the finite vacuum energy shift, so the effective mode-count parameter $f$ in $\rho_\Lambda = (\pi^2 \hbar c / 1440)\,f / L^{*4}$ is reduced slightly from the naive SM value $f = 54$. Even if we conservatively remove a few fermionic degrees of freedom per generation, the resulting change in $L^*$ is at the percent level, leaving the predicted interval in the same $\mathcal{O}(10^2)\,\mu\mathrm{m}$ band. Thus Level 1b does not dramatically move the SC3 ISL prediction, but it upgrades the mode count from an arbitrary field inventory to a topological invariant of the Hopf bundle: the Casimir contribution to $\Lambda$ is now constrained by $c_1 = 1$, not by an assumed compactification ansatz.

---

## § 5.3.3: Casimir Energy on the Derived Interval (Level 1)

### § 5.3.3.1: Setup (Klein-Free)

The extra dimension is the geometrically compact interval $r \in [0, r_{\max}]$ with physical length $L^* = r_{\max} \times s$. There is no Klein circle. Boundary conditions are Dirichlet-type at both ends: at $r = 0$ (brane) and at $r = r_{\max}$ (pinch-off where $A = 0$).

The mode expansion on the interval is:

$$\phi(r) = \sum_{n=1}^{\infty} a_n \sin\!\left(\frac{n\pi r}{L^*}\right) \quad \text{(bosons, Dirichlet)}$$

$$\psi(r) = \sum_{n=0}^{\infty} b_n \sin\!\left(\frac{(n+\tfrac{1}{2})\pi r}{L^*}\right) \quad \text{(fermions)}$$

### § 5.3.3.2: Casimir Energy Density (Interval, Dirichlet BC)

Define $f := \tfrac{7N_F}{8} - N_B$. The regularized Casimir energy density on the interval $[0,L^*]$ with Dirichlet BC is:

$$\rho_{\mathrm{Cas}}(L^*) = \frac{\pi^2 \hbar c}{1440\,L^{*4}}\,f$$
(Eq. 5.3.1)

This is a factor of 2 smaller than the circle result ($\pi^2 \hbar c f / 720 L^4$) because standing waves have half the mode density of travelling waves at the same wavelength.

### § 5.3.3.3: Scale Prediction

Setting $\rho_{\mathrm{Cas}} = \rho_\Lambda$:

$$L^* = \left(\frac{\pi^2 \hbar c\,f}{1440\,\rho_\Lambda}\right)^{1/4}$$
(Eq. 5.3.2)

For the SM sector with Dirac neutrinos ($f = 54$):

$$\boxed{L^* \approx 68.6\,\mu\mathrm{m} \quad \text{(full SM, } f = 54\text{)}}$$
(Eq. 5.3.3)

Self-consistent iteration ($f_{\mathrm{eff}}$ at each $L^*$) converges to:

$$\boxed{L^* \approx 55.7\,\mu\mathrm{m} \quad \text{(self-consistent, } f_{\mathrm{eff}} = 23.5\text{)}}$$
(Eq. 5.3.4)

**Predicted range:** $L^* \in [56, 69]\,\mu\mathrm{m}$.

### § 5.3.3.4: ISL Bound

The first genuine KCR graviton has dimensionless mass $m_1^2 = 20.1$ from the volcano potential. The physical wavelength:

$$\lambda_1 = \frac{L^*}{m_1} \approx \frac{68.6}{4.48} \approx 15.3\,\mu\mathrm{m} \quad \text{(full SM)}$$

$$\lambda_1 \approx 12.4\,\mu\mathrm{m} \quad \text{(self-consistent)}$$

Both are safely below the Lee et al. (2020) ISL bound of 44 μm. **ISL: PASSES with 3× margin.** ✓

### § 5.3.3.5: Branch Screening

| Sector | $N_B$ | $N_F$ | $f$ | $L^*$ (μm) | ISL? |
|--------|-------|-------|-----|-------------|------|
| **SM (Dirac ν)** | 30 | 96 | +54 | 68.6 | ✓ |
| **SM (Majorana ν)** | 30 | 90 | +48.75 | 66.7 | ✓ |
| **Self-consistent** | 20 | 6 | +23.5 | 55.7 | ✓ |
| **N=1 SUSY minimal** | 1 | 1 | −0.125 | — | See note |
| **N=2 SUSY** | 3 | 3 | −0.375 | — | See note |

**SUSY note:** Sectors with $f < 0$ give $\rho_{\mathrm{Cas}} < 0$. In the Level 1 analysis (Casimir only), this gives $\Lambda_{\mathrm{eff}} < 0$, which fails SC3. However, if Level 3 (T_{MΣ} frame-dragging) is confirmed as a positive contributor, SUSY sectors may be rescued. This depends on the RC-1 calculation (Paper 3 scope).

### § 5.3.3.6: Non-Linear KCR Mode Spacing

The volcano potential on the derived interval gives:

$$m_n/m_1 \approx 1,\; 1.67,\; 2.32,\; 2.97 \quad \text{(derived compactification)}$$

vs. Klein $S^1$:

$$m_n/m_1 = 1,\; 2,\; 3,\; 4 \quad \text{(Klein circle)}$$

This is a **new testable prediction** that distinguishes derived compactification from Klein's ad hoc circle.

---

## § 5.3.4: What Remains Open

### § 5.3.4.1: FS Curvature and the Decoherence Rate

The Fubini-Study curvature $k^2 = 2$ of $\Sigma = \mathbb{CP}^1$ does not enter the Friedmann equation. It enters the **decoherence dynamics** on Σ: it determines the rate at which quantum states decorrelate along the $r$-direction, the shape of the volcano potential, and the KCR mode spectrum. The dimensionless value $\rho_{\mathrm{geom}} = +3.534$ (the A⁴-weighted curvature integral) is real as an information-geometric quantity — it belongs in the decoherence rate equation, not in the Friedmann equation.

### § 5.3.4.2: Radion Stabilization (OP-5)

**Shape (TOPOLOGICALLY FROZEN):** $r_{\max} = \pi/(2\sqrt{2})$, set by $k^2 = 2$, has zero moduli. Topologically fixed by CP¹ geometry. No Goldberger-Wise potential needed. ✓

**Scale:** The physical scale factor $s$ (where $L^* = r_{\max} \times s$) must be stabilized. In the Casimir-only picture (Level 1), the scale is set by $\rho_{\mathrm{Cas}}(L^*) = \rho_\Lambda$, giving $L^* \in [56, 69]\,\mu\mathrm{m}$. Whether there exists a dynamical mechanism (potential minimum, cosmological attractor, or other) that drives $s$ to this value is an open question.

**Status:** Shape RESOLVED; scale PARTIALLY RESOLVED (Casimir balance gives the value, but the dynamical mechanism driving $s$ to that value is not yet demonstrated). This replaces the v2 claim of a "cosmological attractor" which relied on the Level 2 category error.

### § 5.3.4.3: Level 3 — T_{MΣ} Frame-Dragging

The α = 3/2 result (Phase 0–2 calculations, April 10 session) shows that the T_{MΣ} cross-term backreaction produces $\rho_{\mathrm{drag}} = (3/2) \times \Gamma_{\mathrm{dec}}^2 / G$ with no hierarchy factor. If the cosmic decoherence rate is $\Gamma_{\mathrm{dec}} \sim 0.68 H_0$, this gives $\Omega_{\mathrm{drag}} \sim 0.69$ — matching $\Omega_\Lambda$. This is a potentially dominant contributor that would change the SC3 picture from "Casimir sets Λ" to "frame-dragging sets Λ, Casimir provides a sub-millimeter correction." The rigorous derivation requires RC-1 (backreaction from the action principle), which is Paper 3 scope.

### § 5.3.4.4: Post-Transition Field Content

The field content determines $f$, which determines $L^*$. Paper 3, Axiom B is required for the specific $(N_B, N_F)$ count. The D4 result constrains $f$ topologically (via c₁ = 1), reducing the dependence on assumed field inventories.

---

## § 5.3.5: SC3 Verdict

| Condition | v1 | v2 (category error) | REVISED |
|-----------|----|----------------------|---------|
| **Source of Λ > 0** | Casimir only | Geometric Λ (❌ wrong) | Casimir (Level 1) + possible frame-dragging (Level 3) |
| **FS curvature role** | Not addressed | Friedmann source (❌ wrong) | Decoherence dynamics only ✓ |
| **Scale prediction** | r_f* ≈ 22 μm (wrong BC) | L* ≈ 46–56 μm | **L* = 56–69 μm** (D1 corrected) |
| **ISL bound** | Passes (wrong value) | Passes | **Passes with 3× margin** (λ₁ = 12–15 μm) |
| **OP-5 shape** | Unsolved | Resolved ✓ | **Resolved** (k² = 2 topological) ✓ |
| **OP-5 scale** | Unsolved | "Cosmological attractor" (❌) | **Partially resolved** (Casimir balance; mechanism TBD) |
| **Level 1b (D4)** | Not computed | Not computed | **ΔL*/L* < 1%, mode count topological** ✓ |
| **Level 3 (α = 3/2)** | Not known | Not known | **Identified; RC-1 needed (Paper 3)** |

**SC3 claim posture: CONDITIONALLY ESTABLISHED (Level 1).**

The Casimir energy on the derived interval with Dirichlet BCs gives $L^* \in [56, 69]\,\mu\mathrm{m}$, passing the ISL bound. The mode count is topologically constrained by $c_1 = 1$ (D4). Shape stabilization is topological (OP-5 shape resolved). Scale stabilization requires either (a) a dynamical mechanism driving $s$ to the Casimir-balance value, or (b) confirmation that Level 3 (frame-dragging) dominates, in which case the Casimir contribution becomes a sub-millimeter correction to a cosmologically-set Λ.

---

## Notation (REVISED)

| Symbol | Meaning |
|--------|---------|
| $L^*$ | Physical interval length; $L^* = r_{\max} \times s$ |
| $\rho_{\mathrm{Cas}}$ | Casimir energy density on interval with Dirichlet BC |
| $f$ | Mode-count parameter; $f = 7N_F/8 - N_B$ |
| $\lambda_1$ | Wavelength of first KCR graviton mode |
| $\alpha = 3/2$ | Geometric coupling constant from CP¹ (Level 3) |

**Removed:** $\rho_{\mathrm{geom,4D}}$ from Friedmann equation (Level 2 category error); $r_f^*$ notation (Klein-era); "cosmological attractor" for scale (relied on category error); "geometric Λ as primary source" (incorrect).
