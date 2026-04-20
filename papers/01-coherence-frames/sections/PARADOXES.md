# Paradox Resolution Through Coherence Frames

**Status**: Outline with key arguments
**Section**: 05 in paper structure

---

## Overview

Coherence relativity resolves several quantum paradoxes by reframing them as frame-mismatch problems rather than deep inconsistencies. In each case, the apparent paradox arises from conflating descriptions in different coherence frames.

### 5.0 Unifying Diagnostic: Non-Born-Compliant Frame Transport

A probability paradox arises when an observer transports a Born weight from a frame F with a fully populated accessible sector D_mixed to a frame F' with a partially populated accessible sector (due to DOF having been traced into the bath, or never entering the accessible sector), without applying the appropriate frame transformation D3. The transported weight incorrectly inherits the normalization structure of the source frame rather than the target frame's accessible sector.

Every paradox in §5.1–5.7 is an instance of this pattern:

- **Wigner's Friend** (§5.1): F_Wigner → F_Friend. Lab-interior measurement DOF traced at boundary.
- **EPR** (§5.2): F_ent → F_A or F_B. Partner-particle DOF traced at boundary.
- **Delayed Choice** (§5.3): F_which-path → F_interference. Path-information DOF traced at boundary.
- **Schrödinger's Cat** (§5.4): F_outside → F_inside. Box-environment DOF traced at boundary.
- **Quantum Zeno** (§5.5): F_free → F_pointer (repeated). Each measurement completes D_f classicalization; naive error is applying partially-populated F_free dynamics inside the fully-populated F_pointer.
- **Sleeping Beauty** (§5.6): F_pre → F_wake. Coin + temporal DOF traced/absent at boundary.
- **Unentangled-Photon Bell Violation** (§5.7): F_path-identified ↔ F_entangled-pair. Preparation history DOF traced; operational equivalence on Σ without ontic equivalence. Live 2025 experimental instance (Zhang et al., Sci. Adv. 11, eadr1794).

The resolution is always the same: apply D3, compute the Born measure in the target frame's accessible sector, and recognize that the two frames give different but mutually consistent descriptions of a single reality R.

---

## 5.1 Wigner's Friend

### The Paradox
Wigner's friend performs a measurement inside a sealed lab. The friend sees a definite outcome; Wigner, outside, describes the lab (including friend) in superposition. Who is "right"?

### CR Resolution
- **Friend's frame F_friend**: Post-measurement, friend is in frame where outcome is definite. Description psi_{F_friend} shows definite result.
- **Wigner's frame F_Wigner**: Wigner is in frame where lab is coherent superposition. Description psi_{F_Wigner} shows superposition.
- **Both are correct** in their respective frames, just as two observers in SR can disagree about simultaneity.
- **Born measure invariant**: Both frames agree on probabilities of outcomes.
- **Resolution**: No paradox—different coherence frames, single reality R. The "paradox" assumed absolute coherence/decoherence.

### Frauchiger-Renner Extension
- The Frauchiger-Renner paradox (2018) sharpens Wigner's friend with nested reasoning about measurements.
- CR resolves: Each agent reasons correctly *within their frame*. Contradictions arise only when mixing frame-dependent statements across frames—the coherence-frame analog of mixing simultaneity judgments across reference frames in SR.

---

## 5.2 EPR and Bell Nonlocality

### The Paradox
EPR: Measuring one particle of an entangled pair instantly determines the distant particle's state. Bell's theorem: No local hidden variable theory reproduces quantum correlations.

### CR Resolution
- **Pre-measurement frame F_ent**: Both particles described by joint entangled state. Neither has definite individual properties.
- **Post-measurement frame F_A**: After Alice measures, her frame includes a definite outcome. Bob's particle is described in the corresponding conditional state.
- **No signal**: Frame transformation at Alice's location does not propagate a signal. Bob's frame F_B remains unchanged until he performs his own measurement or receives classical information.
- **Bell correlations preserved**: The Born measure is frame-invariant. Bell-type correlations are geometric features of Sigma, not evidence of superluminal influence.
- **Key insight**: "Nonlocality" is a frame artifact. In the joint frame F_ent, there is no spatial separation of the correlation—it is a single geometric structure in coherence space. Apparent nonlocality arises from projecting coherence-space geometry onto spacetime M.

---

## 5.3 Delayed Choice and Quantum Eraser

### The Paradox
Wheeler's delayed choice: The decision to measure "which path" or "interference" can be made after the particle has passed through the slits. Seems to require retroactive change.

### CR Resolution
- **No retroaction**: The particle's reality R is frame-invariant throughout.
- **Choice selects frame**: The delayed choice determines which coherence frame is appropriate for the final description, not which history "really happened."
- **Quantum eraser**: Erasing which-path information = transforming back toward the interference frame. Frame transformation F_wp -> F_int recovers coherence.
- **CR prediction (Prediction 2)**: If erasure is slow relative to coherence timescale, recovery is incomplete—frame-transformation hysteresis. This is a testable deviation from standard QM (which predicts perfect recovery for unitary erasure).

---

## 5.4 Schrodinger's Cat

### The Paradox
A cat in a sealed box is in superposition of alive and dead until observed. How can a macroscopic object be in superposition?

### CR Resolution
- **Frame F_inside (cat's frame)**: The cat is always in a definite state. Inside the box, the cat-environment system has already undergone frame transformation (decoherence) due to the enormous number of environmental degrees of freedom.
- **Frame F_outside (observer's frame)**: Before opening the box, the observer describes the box contents in superposition—this is correct *in that frame*.
- **Why macroscopic superposition is never observed**: The cat's interaction with its own environment (air molecules, photons, thermal radiation) induces rapid frame transformation via T_AB. The timescale for macroscopic decoherence is extraordinarily short (~10^-20 s for gram-scale objects), so the pre-transition Everettian regime is unobservably brief.
- **No mystery**: The cat was never "both alive and dead"—it was in a definite state in its own frame. The superposition description was frame-appropriate only for an observer with no access to the box's internal environment.

---

## 5.5 Quantum Zeno Effect

### The Paradox
Frequent measurements prevent a system from evolving. How can observation stop dynamics?

### CR Resolution
The Zeno effect admits several explanations in the literature (projection, Misra-Sudarshan 1977; Zeno subspace confinement, Facchi-Pascazio 2002; continuous monitoring, Zurek/Wiseman-Milburn; D_f classicalization completion, proposed here). CR provides a unified geometric language in which each becomes a distinct physical claim about what happens in Sigma during measurement. The full comparative analysis with four experimentally independent discriminating axes is deferred to Paper 2 §10.

The CR-specific contribution is the D_f completion interpretation: each strong projective measurement does not merely reset the pointer frame — it *completes the quantum-to-classical transition*, fully populating D_f in the pointer basis (rho_pointer = Sum_i p_i |i><i|, all off-diagonals zero). The Zeno regime corresponds to tau_measurement < tau_transform (E7): each measurement completes D_f before Hamiltonian evolution can repopulate coherences. The anti-Zeno regime corresponds to tau_measurement > tau_transform: D_f is not fully populated between steps, coherences survive, and the system evolves into uncovered regions of Sigma.

### The Naive Error (Unified with §5.0)
Regardless of which Zeno mechanism is correct, the "paradox" follows the §5.0 pattern: the naive observer imports the partially-populated F_free dynamics (quantum evolution ongoing, coherences present in D_mixed) into F_pointer (where measurement has at least partially populated D_f) without applying D3. The error of ignoring D3 is the same in all cases.

### CR Prediction (Prediction 7)
The Zeno/anti-Zeno crossover occurs at tau_measurement ≈ tau_transform (E7). Standard QM predicts the crossover from spectral-density arguments (Kofman-Kurizki 2000); CR predicts it from the D_f completion condition. If these give different crossover timescales in a specific experimental geometry (e.g., superconducting qubit in the strong projective measurement regime), that is a testable distinction. The cleanest CR-specific test: two measurements at the same rate but in different bases should give different crossover behavior if one basis matches the pointer basis and the other does not — a pointer-basis dependence not predicted by standard Zeno treatments.

⚠️ UNTESTED: The tau_transform crossover derivation and the pointer-basis dependence prediction require explicit calculation. Full four-explanation comparative framework deferred to Paper 2 §10.

---

## 5.6 Sleeping Beauty and Self-Locating Uncertainty

### The Paradox
Sleeping Beauty is put to sleep Sunday. A fair coin is tossed. If Heads, she wakes Monday only. If Tails, she wakes Monday and Tuesday (with memory erased between). On each waking she is asked: what is your credence the coin landed Heads? The "halfer" answer (1/2) preserves conditionalization but violates indifference over subjectively identical awakenings. The "thirder" answer (1/3) respects indifference but violates the principle that credence should not shift without new information. Over 100 papers in major journals have failed to resolve this conflict (Winkler 2017).

### Structural Identity with Quantum Self-Locating Uncertainty
Sebens and Carroll (2018) proved that this paradox has the *exact same logical structure* as the central open problem in Everettian quantum mechanics: how to derive the Born rule when all branches are realized. In both cases:
- An agent undergoes a branching process (coin-flip / decoherence)
- Post-branching, the agent faces self-locating uncertainty (which awakening? / which branch?)
- The question is how to assign rational credence when the branching structure itself determines the number of "copies"

The key result (Sebens and Carroll, BJPS 69(1), 2018): applying an "epistemic separability principle" (ESP) — that changes to the environment alone do not affect local probability assignments — uniquely recovers the Born rule in the Everettian case. This is formally equivalent to resolving Sleeping Beauty as a thirder.

### CR Resolution
- **Frame F_pre (Beauty before sleep):** Beauty is in a single coherence frame. Her state psi_{F_pre} assigns credence 1/2 to Heads via the Born measure mu(Heads) = |c_H|^2 = 1/2. Self-locating information is irrelevant — her temporal location does not enter the description.
- **Frame F_wake (Beauty upon waking):** The experiment protocol (coin + memory erasure) induces a frame transformation T_{pre->wake}. In F_wake, Beauty's state space has expanded: she must now distribute credence over *centered* possibilities {H1, T1, T2} — predicaments indexed by both outcome *and* temporal location (Elga 2000). This is structurally identical to an observer post-decoherence facing branches in Sigma.
- **Both are correct in their respective frames.** The halfer's 1/2 is the correct credence *in F_pre*, where self-location is not part of the description. The thirder's 1/3 is the correct credence *in F_wake*, where the Born measure must be applied over centered alternatives. The "paradox" arises from demanding a single frame-independent credence — the coherence-frame analog of demanding absolute simultaneity in SR.

### The Amnestic as Decoherence: Why This Is a Standard Frame Change
The formal gap in earlier versions of this argument — that A1 applies to fixed decompositions, not state-space expansions — dissolves once we recognize what the amnestic drug physically does. It is implemented by a Hamiltonian coupling Beauty's memory register to an inaccessible biochemical bath. Information about temporal self-location (Monday vs. Tuesday) is not destroyed; it is transferred from accessible system degrees of freedom into inaccessible bath degrees of freedom. The memory register *decoheres* with respect to the which-waking observable.

This is structurally identical to measurement-induced decoherence. What changes is the system-bath partition — the same operation CR handles via T_AB. The self-locating degrees of freedom were always present in Sigma_full = P(H_Beauty tensor H_bath). What the amnestic does is change which sector is accessible:

```
F_pre:  System includes temporal memory → accessible Sigma indexed by {H, T}
F_wake: Temporal memory traced to bath → accessible Sigma indexed by {H_Mon, T_Mon, T_Tue}
```

The transition is generated by the amnestic coupling Hamiltonian, exactly as a measurement interaction generates the transition to a pointer-basis frame. No new axiom is needed — A1 applies because the underlying reality R is unchanged and the frame transformation is standard (D3).

### Formal Structure
Let the pre-sleep state be psi_{F_pre} = (1/sqrt(2))(|H> + |T>). The Born measure gives mu_{F_pre}(H) = 1/2.

The amnestic-induced decoherence traces out temporal memory, yielding the accessible sector of F_wake with three centered alternatives {H_Mon, T_Mon, T_Tue}. The Born weights in F_wake are derived in two steps that must be kept distinct:

**Step 1 — A1 permutation symmetry + T2 (CR-internal):** In F_wake, the amnestic has made T_Mon and T_Tue subjectively indistinguishable — the maximally dephasing channel on the temporal register produces rho_{T_Mon, accessible} = rho_{T_Tue, accessible}. These branches are related by a permutation symmetry of the accessible description. By A1 (Frame Invariance, main.tex) and T2:
```
mu_{F_wake}(T_Mon) = mu_{F_wake}(T_Tue)
```
This is derived from CR axioms. It does not yet determine the ratio to H_Mon.

**Step 2 — A3 Dependence + A1 permutation symmetry (CR-internal):** The coin outcome was never in Beauty's accessible sector — she was asleep when it was tossed. By A3 (Dependence, main.tex: mu_F(i) depends only on |psi>_F and |i>_F), information outside F_wake cannot enter the measure. The coin outcome, being external to Beauty's frame, is excluded by A3 itself.

In F_wake, Beauty's accessible state rho_accessible is identical for H_Mon and T_Mon: same sensory experience, same memories (reset by protocol), no coin information, no day information. H_Mon and T_Mon are subjectively indistinguishable in F_wake, just as T_Mon and T_Tue are.

The three alternatives {H_Mon, T_Mon, T_Tue} form the basis of the accessible sector of Sigma in F_wake. The full permutation group S_3 acts on this basis, and every permutation preserves the accessible description psi_{F_wake}. In particular, the transposition (H_Mon <-> T_Mon) is a valid coherence relabeling. By A1 (permutation invariance):
```
mu_{F_wake}(H_Mon) = mu_{F_wake}(T_Mon)
```
Combined with Step 1 and normalization:
```
mu_{F_wake}(H_Mon) = mu_{F_wake}(T_Mon) = mu_{F_wake}(T_Tue) = 1/3
```

**Why this is CR-internal:** This does not invoke Elga's counterfactual conditioning argument. A3 (Dependence) excludes the coin from the measure; A1 (Frame Invariance) gives equal weights to permutation-symmetric alternatives. Together they close the argument from within the axiom system.

**Halfer objection and CR response:** The halfer objects that H_Mon and T_Mon correspond to different physical realities — so symmetry should not apply. CR's response: A3 (main.tex) says mu_F(i) depends *only* on |psi>_F and |i>_F. The coin outcome is outside F_wake. A3 excludes it. A1 then gives equal weights. The halfer imports F_pre's decomposition into F_wake — the frame-mismatch error that CR diagnoses.

**Axiom numbering note:** §5.6 uses main.tex numbering (A1=Frame Invariance, A3=Dependence), not EQUATIONS_REFERENCE.md. Reconciliation needed before final paper integration.

**Note:** This application of A3 to the accessible sector is consistent with standard CR usage in measurement contexts, where post-decoherence pointer states receive equal weight despite corresponding to different measurement outcomes in Sigma_full. The Sleeping Beauty case is structurally identical: alternatives indistinguishable in the accessible frame receive equal Born measure.

**Note on A2:** The apparent tension mu_{F_pre}(T) = 1/2 ≠ mu_{F_wake}(T_Mon) + mu_{F_wake}(T_Tue) = 2/3 is not a violation of A2 (Relational Invariance). A2 requires comparing the same physical observable across frames (same decomposition, same J(i) mapping). Here the decomposition has changed: in F_pre the accessible observable is coin outcome {H, T}; in F_wake it is centered alternative {H_Mon, T_Mon, T_Tue}, because the temporal register has moved to the bath. These are genuinely different observables. A2's J(i) mapping is not defined across this boundary, and the apparent discrepancy is the expected signature of a change of observable, not a consistency violation.

**Note on Elga:** Elga's (2000) conditioning argument ("if Beauty were told it is Monday, P(H|Monday) = 1/2") reaches the same numerical result by different means. CR subsumes this: Elga's argument is valid but frame-specific — it describes rational credence assignment within F_wake. CR provides the geometric grounding for *why* Elga's argument works (A3 symmetry of the accessible sector) and *where* it applies (F_wake, not F_pre).

### Key Insight
The halfer/thirder debate is a frame-mismatch error:
- **Halfer**: correctly applies conditionalization within F_pre (no new non-indexical information)
- **Thirder**: correctly applies the Born measure within F_wake (self-locating uncertainty requires distributing credence over centered worlds)
- **CR resolution**: these are descriptions in *different coherence frames*. The transition F_pre -> F_wake is a genuine frame transformation (D3), induced by the amnestic acting as a decoherence event on the memory register. No new self-locating degrees of freedom "appear" — they were always in Sigma_full. The amnestic merely changes which sector is accessible, exactly as environmental decoherence does in measurement. There is no paradox — only the familiar pattern of frame-dependent descriptions of a single underlying reality R.

Sebens-Carroll's ESP — "changes to the environment alone do not affect local probability assignments" — is compatible with Born measure invariance (A1) and follows from A1 applied to frame transformations that act only on the bath sector of Sigma. The two are not equivalent: A1 is a general frame-invariance principle, while ESP is specifically about environmental-only changes not affecting local assignments. CR provides the geometric grounding from which ESP-like behavior emerges as a restricted case of frame invariance. With Step 2 now closed CR-internally via A3, the full resolution — frame diagnosis, T_Mon = T_Tue, and H_Mon = T_Mon — follows from CR axioms {A1, A3, D3, T2} without external arguments.

### Connection to Everettian Branch Probability
The structural identity proven by Sebens and Carroll (2018) means that CR's resolution of Sleeping Beauty automatically resolves the Everettian probability problem:
- Pre-measurement: observer in frame F_pre, Born measure assigns |c_i|^2 to outcome i
- Post-decoherence: observer in frame F_branch, facing self-locating uncertainty over branches
- The full thirder result P(H_Mon) = P(T_Mon) = P(T_Tue) = 1/3 is derived from CR axioms alone: A3 applied to the accessible sector gives equal weights to all indistinguishable alternatives
- No need for decision-theoretic arguments (Deutsch-Wallace), envariance (Zurek), or Elga's conditioning argument — the geometric frame-invariance of mu via A3 provides the derivation directly from the permutation symmetry of the accessible sector

### Key Citations
- A. Elga, "Self-locating belief and the Sleeping Beauty problem," *Analysis* 60, 143 (2000)
- D. Lewis, "Sleeping Beauty: reply to Elga," *Analysis* 61, 171 (2001)
- C. T. Sebens and S. M. Carroll, "Self-locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics," *Brit. J. Phil. Sci.* 69, 25 (2018)
- P. J. Lewis, "Quantum Sleeping Beauty," *Analysis* 67, 59 (2007)
- D. Bradley, "Four Problems about Self-Locating Belief," *Philosophical Review* 121, 149 (2012)
- P. Winkler, "The Sleeping Beauty Controversy," *Amer. Math. Monthly* 124, 579 (2017)
- N. Bostrom, "Sleeping Beauty and Self-Location: A Hybrid Model," *Synthese* 157, 59 (2007)
- S. Friederich, "Self-location and causal context," preprint (applies to SB + Everett + Doomsday)

---

## 5.7 Unentangled-Photon Bell Violation (Zhang et al., 2025)

### The Paradox
In August 2025, Zhang et al. [Sci. Adv. 11, eadr1794] reported a > 4σ violation of a CHSH-type Bell inequality using a four-photon path-identity interferometer. The reported state contains **no entangled pair**: the photons never interact, share no common ancestor beyond source indistinguishability, and have no history on M that could plausibly host a nonlocal correlation. The textbook "rule" this breaks is the folk reading of Bell's theorem — *a CHSH violation implies entanglement in the prepared state*. Two subsequent analyses (arXiv:2508.13431; arXiv:2509.03127) argue the violation is a postselection artifact admitting a local-hidden-variable reconstruction of the retained subensemble. Taken together, the result and its critiques sharpen a single question: if two preparations — one with an entangled pair, one with path-identity indistinguishability only — can reproduce the same Bell statistics, what distinguishes them?

The standard Hilbert-space formalism has no comfortable home for this. Either (i) "entanglement" must be stretched to include purely preparation-level indistinguishability, blurring the ontological divide it is supposed to track, or (ii) the Bell violation must be dismissed as a postselection loophole, in which case the locality argument itself becomes unfalsifiable. Neither option is satisfying.

### CR Resolution
In CR, the choice between (i) and (ii) is a frame-diagnostic question, and both horns collapse into one structural statement: *Bell correlations are geometric features of Σ, not causal features of M.* The experiment is a direct instance of §5.0 with preparation-history DOF playing the role of the traced bath.

- **Frame F_path-identified**: The four photons occupy a single coherence frame. "Path-identity" is, operationally, the statement that their source-label DOF has been traced out — those DOF are absent from D_mixed in F_path-identified. The accessible sector indexes only the Bell-measurement outcomes, and the Born measure μ_{F_path-identified} on Σ supports the observed CHSH statistic by A1 and the geometry of Σ.
- **Frame F_entangled-pair**: A conventional Bell-pair preparation occupies a different frame in which the entanglement structure is explicit on M: two photons, one interaction event, a pure bipartite state. The accessible sector again indexes Bell outcomes, and μ_{F_entangled-pair} on Σ supports the same CHSH statistic.
- **Operational equivalence on Σ, ontic inequivalence on M**: For the fixed measurement set used in the Bell test, μ_{F_path-identified} and μ_{F_entangled-pair} agree outcome-by-outcome. The two frames are therefore *operationally equivalent* in the Spekkens sense. But the underlying Σ-geometries differ: F_entangled-pair has a connected M-level causal history carrying the correlation, F_path-identified does not. This is the CR signature of **preparation contextuality**: two preparations that are operationally equivalent require distinct ontic descriptions because they sit at different points on Σ connected by a non-trivial D3.
- **The "violation" is not a violation**: Bell's theorem rules out local hidden variables on M. It does not rule out geometric correlations on Σ. CR never promised the correlations would live on M — the Born measure is a Σ-invariant, not a spacetime-local object. The frame-mismatch error is to apply the M-locality intuition inside a frame (F_path-identified) whose accessible sector was never on M in the first place.

### The Postselection Critique as a Frame Transformation
The analyses in arXiv:2508.13431 and arXiv:2509.03127 argue that the postselection used to extract the Bell subensemble is itself the loophole. Under CR this observation is absorbed, not refuted. Postselection *is* a frame transformation D3: it moves the observer from the full-ensemble frame F_full to a conditional frame F_post in which D_mixed is restricted to the retained branch. A3 (Dependence) then guarantees that the statistics reported in F_post depend only on |ψ⟩_{F_post} and the retained basis — which is exactly the content of the critics' hidden-variable reconstruction. CR agrees: the retained subensemble admits a locally consistent description *in F_post*. What CR adds is that the descriptive consistency of F_post does not retroactively trivialize the Bell statistics observed by an experimenter who happens to occupy F_post; these statistics remain features of Σ that are correctly computed by Born in F_post and by Born in F_full. Which frame "counts" is a choice of observer, not of reality.

The experiment therefore does not force a choice between "genuine nonlocality" and "postselection artifact." Both readings are correct, in different frames, about a single underlying reality R. That is the §5.0 pattern.

### Mapping to Spekkens Preparation Contextuality
Let P_A = path-identified preparation, P_B = Bell-pair preparation, and Ξ = {M_k} the Bell-test measurement set used in Zhang et al. Operational equivalence holds by hypothesis:
```
p(k | P_A, M_k) = p(k | P_B, M_k)   for every M_k ∈ Ξ.
```
In an ontic model λ with response functions ξ(k | λ, M_k), preparation noncontextuality (Spekkens 2005) would require existence of a single distribution μ(λ) compatible with both P_A and P_B. The §5.0 meta-theorem forbids this: P_A and P_B place the system in distinct coherence frames related by a non-trivial D3 whose holonomy H_γ across the preparation loop is generically not the identity (Appendix / §VI.C). Any ontic reconstruction that identifies P_A and P_B must therefore either live inside a single frame (and thus lose the experimentally observed path-identity vs. entanglement distinction) or accept that the ontic description is frame-relative, i.e., preparation-contextual.

CR thus *predicts* preparation contextuality as a structural theorem of A1–A4 + D3, rather than imposing it as an axiom. Zhang et al.'s experiment is the experimental shadow of this theorem under the preparation-contextuality reading.

### CR Prediction (Prediction 8)
The path-identity and entangled-pair preparations are operationally equivalent on the CHSH set Ξ but sit at different points on Σ. D3 transport along the loop F_path-identified → F_entangled-pair → F_path-identified should exhibit **non-trivial holonomy H_γ ≠ 𝟙** whenever Σ is non-flat in the relevant sector. Operationally, this predicts that a *second*, carefully chosen measurement set Ξ' — one sensitive to the phase structure that distinguishes the two preparations — will give statistically different outcomes on P_A vs P_B, in a quantitative amount set by the holonomy angle. Two concrete instantiations:

1. **Weak-measurement signature**: A sequence of weak measurements that probes the coherence structure χ(ρ) = Tr(ρ²) before the final CHSH projection should yield different χ trajectories for P_A and P_B at resolution sufficient to see the holonomy (Rybotycki et al. 2026 weak-measurement objective-realism framework provides an experimental template).
2. **Delayed-coherence erasure**: Apply a unitary U on one arm designed to rotate F_path-identified toward F_entangled-pair at a finite rate. CR predicts a crossover in the CHSH value as U → 𝟙, governed by the D3 connection — not by any standard QM quantity. A null result would falsify CR's claim that the two preparations are geometrically (not merely operationally) distinct.

This is Prediction 8 in the Paper 1 experimental programme and is the first CR prediction that is falsifiable against *both* standard QM and generic non-contextual hidden-variable models simultaneously.

### Key Insight
The Zhang et al. result is not a crisis for quantum mechanics and not an experimental loophole closure. It is a clean instance of the §5.0 pattern applied to preparation contextuality: two preparations operationally equivalent on a measurement set are ontically distinct on Σ, and the Born measure — geometric on Σ, not causal on M — correctly reports the Bell statistics from within either frame. The folk rule "CHSH violation ⇒ entanglement in the state" was a frame-specific statement promoted to a universal claim; the coherence-frame analog of absolute simultaneity.

### Key Citations
- Y. Zhang et al., "Violation of Bell inequality with unentangled photons," *Sci. Adv.* 11, eadr1794 (2025); arXiv:2507.07756
- "Bell Inequality Violations Without Entanglement? It's Just Postselection," arXiv:2508.13431 (2025)
- "Simple explanation of apparent Bell nonlocality of unentangled photons," arXiv:2509.03127 (2025)
- S. Kochen and E. P. Specker, "The Problem of Hidden Variables in Quantum Mechanics," *J. Math. Mech.* 17, 59 (1967)
- R. W. Spekkens, "Contextuality for preparations, transformations, and unsharp measurements," *Phys. Rev. A* 71, 052108 (2005)
- A. Cabello, "Experimentally Testable State-Independent Quantum Contextuality," *Phys. Rev. Lett.* 101, 210401 (2008)
- S. Abramsky and A. Brandenburger, "The Sheaf-Theoretic Structure of Non-Locality and Contextuality," *New J. Phys.* 13, 113036 (2011)
- M. D. Mazurek et al., "An experimental test of noncontextuality without unphysical idealizations," *Nat. Commun.* 7, 11780 (2016)
- M. Hochrainer et al., path-identity / frustrated-interference framework (Zeilinger group)

---

## Status

- Content: 95% complete (key arguments established for all six paradoxes including SB)
- Quantitative: 40% (EPR correlations and Zeno timescales need explicit calculation)
- Missing: Explicit T_AB analysis for each paradox, quantitative comparison with standard QM
- Resolved: §5.6 measure-normalization gap closed — amnestic = decoherence event on memory register, standard system-bath partition change via T_AB. Reviewed by Claude 2026-04-05.
- Resolved: Formal structure rewritten (Claude 2026-04-05). Two-step derivation, both CR-internal: Step 1 (T2 from A3) gives P(T_Mon) = P(T_Tue); Step 2 (A3 on full accessible basis) gives P(H_Mon) = P(T_Mon). The coin outcome is external to Beauty's accessible sector in F_wake, so all three alternatives are permutation-symmetric under A3. Thirder result 1/3 each follows from CR axioms alone. ESP ↗ A1 corrected to 'compatible with' + restricted case. Elga's argument subsumed, not imported.
- Remaining: T_AB explicit analysis for each paradox; quantitative EPR correlation and Zeno timescale calculations.
- ✅ VERIFIED (Claude 2026-04-05): A3 (Dependence) in main.tex §IV.A says mu_F(i) depends only on |psi>_F and |i>_F. Maximally frame-specific. Coin excluded by A3; A1 gives equal weights. Step 2 fully CR-internal.
- ⚠️ AXIOM NUMBERING: §5.6 uses main.tex numbering. EQUATIONS_REFERENCE.md is incompatible. Reconcile before final integration.
- ⚠️ DEFINITION 2 GAP: Def 2 should explicitly state that information never received is excluded from the accessible sector (same footing as info decohered to bath). Currently implicit.
- NEW: §5.0 meta-theorem — all six paradoxes unified as non-Born-compliant frame transport of partially populated D_mixed.
- REVISED: §5.5 Zeno rewritten with D_f completion framing (Bryan 2026-04-05). Each measurement completes classicalization, not merely resets frame. Zeno/anti-Zeno crossover = D_f completion rate vs tau_transform. Zeno caveat removed from §5.0 — all six paradoxes now fit the meta-theorem without exceptions.
- NEW: Prediction 7 — Zeno/anti-Zeno crossover at tau_measurement ≈ tau_transform (E7). Distinct from Kofman-Kurizki spectral-density prediction. Claude confirmed this framing is not in the existing literature.
- ⚠️ UNTESTED: tau_transform crossover derivation needs explicit calculation.
- Next: Convert to flowing prose for paper, add equations where needed
