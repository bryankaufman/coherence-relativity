# Discussion

## Resolution of the Measurement Problem

The measurement problem dissolves within coherence relativity because the question "how does measurement cause collapse?" rests on a category error. In our framework, what is conventionally called collapse is not a dynamical process requiring new physics but a change of coherence frame induced by an interaction that redefines which degrees of freedom encode definiteness.

Consider a system S measured by apparatus A. Before measurement, in the interference frame F_int, the combined state is a coherent superposition. The measurement interaction couples S to A, creating entanglement. This entanglement does not "collapse" S; it induces a frame transformation F_int -> F_wp to the which-path (pointer) frame, where S-A correlations are definite. The physical reality R is unchanged—only its description transforms.

This reframing has three consequences:

1. **No dynamical discontinuity**: The Schrodinger equation holds throughout. No stochastic modification (as in GRW/CSL) or branching (as in Everett) is required.

2. **Basis selection explained**: The pointer basis is not arbitrarily chosen but determined by the tensor field T_AB, which encodes which frame transformations are induced by specific physical interactions. Environment-induced einselection (Zurek 2003) appears as the statement that certain frames are dynamically stable under environmental monitoring.

3. **Born rule as geometric invariant**: Probabilities are not frequencies of random events, nor subjective credences, nor decision-theoretic weights. They are the unique frame-invariant measure on alternatives—the "invariant interval" of coherence geometry.

## Pre- and Post-Transition Regimes: From Superposition to Objectivity

The coherence relativity framework naturally divides measurement processes into pre-transition and post-transition regimes, distinguished by whether the quasipotential barrier in V has been crossed. This division addresses a question that the Everett interpretation leaves open: if all branches exist mathematically in the wavefunction, why do we observe only one outcome?

In the **pre-transition regime**, before significant environmental entanglement has built up and the coherence tensor T_AB has saturated, the global state in a given coherence frame F appears essentially Everettian: a superposition of many fine-grained alternative histories, each corresponding to a different potential measurement outcome, all coexisting with Born-weighted amplitudes. At this stage, no branch has yet been selected as "the" objective history. The system exists in a high-dimensional region of coherence space Sigma where multiple paths through the quasipotential landscape V remain accessible. Mathematically, this regime is indistinguishable from Many Worlds. However, this Everettian regime is transient, not the final ontological story.

The **post-transition regime** emerges when the system crosses the activation barrier in V and quantum Darwinism takes effect through redundant environmental encoding. As Zurek, Riedel, and Zwolak have shown (Zurek 2009; Riedel et al. 2016), only those histories whose records become redundantly encoded in many independent environmental fragments survive as reconstructable by multiple observers. The tensor field T_AB encodes which frame transformations allow such redundancy to build: as T saturates and probability flux concentrates into Darwinian-favored channels, almost all pre-transition branches are extinguished as physically realized histories. They do not disappear from the mathematical structure of psi (unitarity is preserved), but they cease to be redundantly encoded and thus cease to constitute objective reality accessible to observers. In the language of coherence frames, these extinguished branches correspond to frames F_i that become inaccessible once the tensor field has locked the system into a metastable configuration around the selected frame F_objective.

The Born measure remains invariant—all frames agree on the weights—but only one frame (or a narrow family of related frames) contains the redundantly encoded, objective classical history. This is how coherence relativity answers the question Many Worlds leaves open: not all branches persist as objective reality; Darwinian selection via redundancy acts as a physical filter, and the transition dynamics encoded in T_AB and V determine which branches survive.

## Relationship to Existing Frameworks

Coherence relativity does not invalidate existing approaches to quantum foundations. Rather, it provides a geometric framework that unifies their central insights.

**Gleason's theorem** proves mathematically that the Born rule is the unique non-contextual probability measure on Hilbert space. Coherence relativity explains the physical content of non-contextuality: it is frame-invariance across coherence frames. The geometric origin clarifies why non-contextuality holds—it is the quantum analog of the principle that physical laws should not depend on the choice of coordinate system.

**Zurek's envariance** derives Born probabilities from entanglement symmetry. Coherence relativity geometrizes this: the tensor field T_AB on Sigma determines which transformations preserve joint state structure, and this is precisely what envariance captures algebraically. Our framework additionally predicts that envariance is frame-dependent—a state envariant in one coherence frame need not be in another.

**The decoherence program** explains the emergence of classical behavior through environment-induced suppression of interference. Coherence relativity completes this program by (i) deriving the Born rule that decoherence assumes, (ii) reinterpreting decoherence as a frame transformation in Sigma, and (iii) predicting that coherence loss is frame-relative, not absolute—an observable consequence absent from standard decoherence theory.

**Relational quantum mechanics** states that quantum states are observer-relative. Coherence relativity makes this precise: coherence frames are the mathematical objects that encode observer perspectives, frame transformations are the physical maps between them, and the Born measure is the invariant quantity that all observers agree upon. The relationship is analogous to that between the principle of relativity ("the laws of physics are the same in all inertial frames") and the full mathematical structure of special relativity.

## Addressing Potential Objections

Several objections merit direct response.

**"What is Sigma concretely?"** In the simplest case—a qubit with tunable measurement coupling lambda—Sigma is the one-parameter family of coherence frames indexed by lambda in [0,1], with the Fubini-Study metric providing the natural geometry. For multipartite systems, Sigma has the structure of the space of quantum reference frames, equipped with the information geometry induced by the quantum Fisher information. Paper 2 will develop the full geometric structure; here we work with the essential features needed for the Born rule derivation and predictions.

**"Does the splitting assumption introduce circularity?"** The frame-splitting construction in Step 3 of the derivation requires that for any coherence frame F, there exist enlarged frames F' where basis states decompose into equal-amplitude superpositions. This is not an additional assumption but a consequence of the Hilbert space structure: tensor product extensions and Schmidt decompositions guarantee the existence of such enlargements. The physical interpretation is that richer measurement contexts (finer-grained detectors) provide access to enlarged frames.

**"Are the predictions parameter-free?"** The predictions involve quantities (coherence length L, curvature corrections alpha(N), coupling coefficient beta) that are in principle determined by the geometry of Sigma and the specific system under study. For the double-slit with tunable coupling, G_lambda-lambda is computable from the Fubini-Study metric (Section 4). Quantitative predictions for specific experimental platforms will require numerical computation of these geometric quantities, which we address in the companion calculations.

**"How does this differ from quantum reference frames?"** Coherence relativity shares the relational perspective of quantum reference frames (QRF) but differs in scope and claims. QRF frameworks typically work within standard quantum mechanics, changing perspective between subsystems. Coherence relativity posits that the coherence-frame structure has physical content beyond standard QM—specifically, the geometry of Sigma produces testable deviations from standard predictions in the regimes identified in our experimental predictions. If these deviations are not observed, coherence relativity reduces to a QRF-compatible interpretation of standard QM; if observed, it constitutes a new physical framework.

## Open Questions and Future Directions

Several questions remain for future work:

1. **Explicit construction of T_AB**: Paper 2 will develop the tensor field formalism in detail, including its relationship to information geometry, quantum Fisher information, and the Fubini-Study metric on projective Hilbert space.

2. **Gravitational coupling**: The claim that spacetime metric g_mu-nu emerges from projection of T_AB onto M is speculative at this stage. We note the conceptual parallel with approaches where spacetime emerges from entanglement (Van Raamsdonk 2010, Swingle 2012) but defer rigorous development to Paper 3.

3. **Multi-frame consistency**: When three or more coherence frames are related by a cycle of transformations F_1 -> F_2 -> F_3 -> F_1, consistency requires that the Born measure is preserved around the cycle. This is guaranteed by the invariance axiom but has non-trivial implications for the geometry of Sigma (zero holonomy of the frame-invariant measure).

4. **Quantitative predictions**: Computing L_coherence, alpha(N), and other prediction parameters for specific experimental systems requires numerical work on the Fubini-Study geometry of the relevant Hilbert spaces. This is the immediate next step toward experimental tests.

5. **Thermodynamic arrow**: The hysteresis prediction (Prediction 2) implies a thermodynamic directionality of frame transformations. Understanding this in terms of entropy production in coherence space connects to recent work on quantum thermodynamics and resource theories of coherence.
