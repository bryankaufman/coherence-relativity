# §1 Introduction

**Status:** DRAFT — Wave 6 (merged: Cowork + Warp)
**Model:** Opus (framing + structural overview)
**Cross-references:** Paper 1 (all); §2.1–§5 (internal)

---

## §1.1 From Coherence Frames to Joint Geometry

Paper 1 introduced *coherence relativity*: a geometric framework in which quantum measurement is understood as a change of coherence frame rather than a dynamical collapse. The central result was that the Born rule — the foundational probability law of quantum mechanics — emerges as the unique measure invariant under all allowed coherence-frame transformations, given additivity on orthogonal alternatives and continuity. The framework rests on four axioms (A1)–(A4) that define a coherence-frame manifold $\Sigma$ equipped with the Fubini-Study metric, and it resolves the measurement problem without modifying unitary dynamics, without postulating many worlds, and without retreating to subjectivism about quantum states.

Paper 1 established the geometry of $\Sigma$ alone — the manifold of coherence frames at a fixed spacetime point. But real quantum systems exist in spacetime. Decoherence conditions vary from place to place. The coherence frame that is natural in one environment may be entirely inappropriate in another. To capture this, the formalism must be extended from $\Sigma$ to the joint manifold $M \times \Sigma$, where $M$ is spacetime.

This is the subject of the present paper.

## §1.2 Seven Deliverables

Paper 1 identified seven open questions whose resolution requires the extended formalism. This paper addresses all seven:

1. **The cross-term tensor $T_{M\Sigma}$** (§2.1). The Fubini-Study metric on $M \times \Sigma$ decomposes into three blocks: the spacetime metric $G_{\mu\nu}$, the coherence-frame metric $G_{ab}$ (which recovers Paper 1's result), and a novel cross-term $T_{\mu a} \equiv G_{\mu a}$ that encodes the coupling between spacetime geometry and coherence-frame evolution. Non-zero $T_{M\Sigma}$ implies that environmental decoherence patterns are encoded geometrically on the joint manifold.

2. **The $\delta\lambda$ formalism** (§2.2). A distinguishability parameter $\lambda \in [0,1]$ controls the effective coupling between sectors. The separated pullback metric decomposes the action into pure-$M$, pure-$\Sigma$, and $\lambda$-controlled cross-term contributions. The Euler-Lagrange equations yield frame-lag dynamics: spacetime acceleration sources coherence-frame response. The classical limit $\lambda \to 0$ recovers standard geodesic motion.

3. **The Markov transition criterion** (§2.3). The Markov ratio $R_{\text{Markov}}$ — a dimensionless ratio comparing effective coupling to diagonal metric contributions — provides a purely geometric criterion for the quantum-to-classical transition. When $R_{\text{Markov}} < \epsilon$, spacetime and coherence decouple, the frame freezes, and semiclassical gravity is recovered. This is a local condition: a system can be quantum in one region and classical in another.

4. **The mixed-state Born rule** (§2.4). Paper 1's axioms (A1)–(A4), which yield the pure-state Born rule, extend to mixed states via purification. The result $P(a|\rho) = \text{Tr}(\rho M_a)$ for general POVMs follows without circularity: the partial trace and Naimark dilation are algebraic operations that do not presuppose the Born rule.

5. **Equations of motion on $M \times \Sigma$** (§4). The abstract Euler-Lagrange system on general $M \times \Sigma$ yields a coupled geodesic system: $M$-sector trajectories are sourced by $\Sigma$-sector acceleration and vice versa, mediated by the cross-term tensor. The frame-lag mechanism — a universal consequence of non-trivial $T_{M\Sigma}$ — is established at the framework level. Where standard evaluation methods hit walls (norm conventions, mode equations, coupling identification) is analyzed explicitly.

6. **$C^1$ regularity** (§4.5). Derived compactification constrains the regularity class of admissible warp profiles, in qualitative contrast to assumed compactification (Randall-Sundrum models) where regularity is tuned via brane tensions and junction conditions. The smooth Hopf bundle structure forbids distributional sources unless they arise dynamically — a framework-level principle.

7. **Holographic connections** (§5). A holographic structure conjecture identifies the $M \times \Sigma$ geometry with a holographic dual: the bulk is $M \times \Sigma$, the boundary is the locus of maximal coherence ($\lambda = 1$), and the holographic direction is the coherence parameter. A complete conceptual dictionary with four entries and three identified departures from standard AdS/CFT is established. Verification requires committing to a specific geometry.

## §1.3 Thesis

The coherence-frame formalism extends to a joint manifold $M \times \Sigma$ carrying a Fubini-Study metric with a cross-term tensor $T_{M\Sigma}$ that encodes quantum-classical coupling. The separation parameter $\delta\lambda$ yields a geometric Markov transition criterion for classicalization. Compactification of extra dimensions is derived from the topology of coherence space — not assumed as in Kaluza-Klein theory, string theory, or braneworld models. The abstract equations of motion on $M \times \Sigma$ reveal a frame-lag mechanism and suggest holographic structure. Evaluating these results on any specific warped geometry exposes convention dependencies that require dedicated treatment — motivating a companion paper that provides the first such evaluation.

## §1.4 The Structure of This Paper

The paper is organized in four parts.

**Part I (§2.1–§2.5): Formalism.** We develop the mathematical machinery of the coherence-frame metric on $M \times \Sigma$.

Section 2.1 derives the cross-term tensor $T_{\mu a}$ from the Fubini-Study pullback. This tensor encodes the coupling between spacetime dynamics (M-sector) and coherence evolution (Σ-sector), and is the central new geometric object of the formalism.

Section 2.2 introduces the distinguishability parameter $\lambda \in [0, 1]$ and develops the $\delta\lambda$ formalism. The separated pullback metric — diagonal blocks plus $\lambda$-weighted cross-term — yields frame-lag equations of motion: when the M-sector accelerates, the Σ-sector responds with a characteristic lag determined by $\lambda$ and $T_{\mu a}$.

Section 2.3 defines the Markov transition criterion. The ratio $R_{\text{Markov}}$ (Eq. 2.3.3) compares the effective coupling strength to the diagonal metric contributions. When $R_{\text{Markov}} < \varepsilon$, the coherence frame decouples from spacetime dynamics — the system is effectively classical. This criterion is coordinate-invariant and model-independent.

Section 2.4 extends the formalism to mixed states via purification, showing that the axioms (A1)–(A4) admit a natural mixed-state generalization through the Naimark dilation theorem.

Section 2.5 decomposes the generator algebra into left-acting (Schrödinger) and right-acting (Heisenberg) sectors, identifying the pointer-sector criterion for decoherence.

**Part II (§3.1–§3.3): Derived Compactification.** We show that the topology of $\Sigma$ is not a free choice but a consequence of the coherence-frame axioms.

Section 3.1 traces a century of *assumed* compactification — from Kaluza (1921) through the string landscape — and identifies the persistent gap: no standard approach derives compactness from first principles.

Section 3.2 closes this gap. The coherence-frame axioms, applied to the simplest quantum system (the qubit), uniquely produce $S^2$ as the coherence manifold. The Hopf fibration $S^1 \to S^3 \to S^2$ then emerges as the minimal ($|c_1| = 1$) principal $U(1)$ bundle over $S^2$. Compactification of the fiber dimension is a topological consequence, not an assumption. The string landscape of $\sim 10^{500}$ Calabi-Yau topologies collapses to a countable discrete set indexed by first Chern number $c_1$.

Section 3.3 catalogs what derived compactification constrains: the landscape of admissible geometries, the moduli space, the Kaluza-Klein spectrum, and the cosmological constant. It also identifies what remains open — and what requires evaluating the framework on a specific geometry.

**Part III (§4–§5): Dynamics, Regularity, and Holography.** This is the key structural contribution of the paper. Each section follows a three-act teaching arc:

1. Present the abstract framework result
2. Show where standard evaluation methods encounter convention dependencies or require geometry-specific input
3. State the framework-level claim and point to the companion paper for evaluation

Section 4 derives the abstract equations of motion on $M \times \Sigma$ from the Euler-Lagrange variation of the action. The coupled geodesic system (Eqs. 4.1.8–4.1.9) and the frame-lag mechanism (Eq. 4.1.10) are established at the framework level. Section 4.2 then shows precisely where evaluation hits walls: norm conventions in $R_{\text{Markov}}$, the coupling identification $\lambda = f(\text{geometry})$, and cross-term scaling all require committing to a specific metric.

Section 4.5 contrasts the $C^1$ regularity properties of the coherence geometry with those of standard Randall-Sundrum models. In RS, brane kinks are absorbed by tunable junction conditions. In derived compactification, regularity is constrained by topology — no arbitrary brane insertion, no tension tuning.

Section 5 states the Holographic Structure Conjecture (Conjecture 5.1) with a complete dictionary: boundary state, bulk depth, cross-term as source coupling, and the classical limit as deep bulk. Three departures from standard AdS/CFT are identified. Section 5.2 shows that all standard verification methods — Ryu-Takayanagi surfaces, entanglement entropy, beta function matching — require a specific metric.

**Part IV (§6–§7): Closing.** Section 6 discusses the implications of the framework and the derived-topology program. Section 7 catalogs open problems.

## §1.5 The Companion Paper

This paper develops the framework. A companion paper — *Coherence Relativity IIb: Self-Consistency, Dark Matter, and Holographic Verification on the KK-Cone* — provides the first evaluation of the abstract framework on a specific geometry: the Kaluza-Klein cone (KK-Cone) arising from derived compactification.

The companion paper specializes the abstract equations of motion (§4) to the 5D warped metric, resolves the norm conventions identified in §4.2, evaluates the Markov transition criterion in the warped throat, tests two of three self-consistency conditions, derives predictions for geometric dark matter, and performs partial holographic verification against Ryu-Takayanagi calculations.

The present paper is fully self-contained. Every result stated here is established at the framework level — no specific geometry is required. The companion paper illustrates the framework's content on the first physically motivated example, but the framework stands independently. Other geometries — higher Chern classes, non-abelian fiber structures — remain to be explored.

## §1.6 Notation and Conventions

We follow the conventions established in Paper 1 and §2.1 of this paper:

- Capital Latin indices $A, B, C, \ldots$ run over all coordinates on $M \times \Sigma$
- Greek indices $\mu, \nu, \rho, \ldots$ run over spacetime coordinates on $M$
- Lowercase Latin indices $a, b, c, \ldots$ run over coherence-frame coordinates on $\Sigma$
- $M$: the spacetime manifold (the M-sector)
- $\Sigma$: the coherence frame manifold (the Σ-sector)
- $\Phi: M \times \Sigma \to \mathcal{P}\mathcal{H}$: the state map
- $G_{AB}$: the Fubini-Study pullback metric on $M \times \Sigma$ (Eq. 2.1.4)
- $T_{\mu a} \equiv G_{\mu a}$: the cross-term tensor (Eq. 2.1.9)
- $\lambda \in [0, 1]$: the distinguishability parameter (§2.2, Eq. 2.2.2)
- $R_{\text{Markov}}$: the Markov transition ratio (§2.3, Eq. 2.3.3)

The metric signature is $(-,+,+,+)$ for the M-sector. Natural units $\hbar = c = 1$ are used unless otherwise stated.

---

## References (within Paper 2)

- Paper 1: Coherence Relativity I (all axioms and foundational results)
- §2.1–§2.5: Part I formalism
- §3.1–§3.3: Part II derived compactification
- §4–§5: Part III dynamics and holography
- [Paper 2B]: Companion paper (KK-Cone evaluation)

---

## Revision History

| Date | Change |
|------|--------|
| 2026-03-10 | Initial drafts — Wave 6 (Cowork + Warp independently) |
| 2026-03-10 | Merged version — thesis paragraph from Warp; detailed structure from Cowork; enriched deliverables from Warp |

---

**Word count:** ~2,200 (target: 1,500–2,500 for an introduction)
**Status:** DRAFT — merged, needs Bryan review
