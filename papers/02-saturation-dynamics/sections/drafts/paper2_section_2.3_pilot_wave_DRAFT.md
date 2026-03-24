# §2.3 Connection to Pilot-Wave Theory

**Status:** DRAFT — structural demonstration with caveats
**Date:** 2026-03-13
**Depends on:** §2.1 (T_{MΣ}, Bures cross-term), §2.2 (δλ formalism, frame-lag)
**Placement note:** New section between §2.2 and the current §2.3 (Markov transition, to be renumbered §2.4)

---

The cross-term tensor $T_{M\Sigma}$ developed in §2.1, together with the frame-lag dynamics of §2.2, carries an unexpected consequence: when the coherence-frame sector $\Sigma$ is integrated out of the joint $M \times \Sigma$ dynamics, the effective potential on spacetime $M$ reproduces the functional form of the Bohmian quantum potential. This section establishes the structural correspondence and its physical interpretation.

## 2.3.1 The Pure-State Subtlety

A natural first attempt is to compare the frame-lag force $F^a_{\text{lag}}$ from §2.2 directly with the Bohmian quantum potential $Q = -(\hbar^2/2m)\nabla^2 R/R$ acting on a particle guided by $\psi = Re^{iS/\hbar}$. Both are state-dependent forces that vanish in the classical limit, and both arise from the global structure of the quantum state rather than local interactions.

However, the pure-state Fubini-Study cross-term $T_{\mu a}^{(\text{FS})}$ vanishes identically for single-ray parameterizations of the form $\psi(x) = R(x)e^{iS(x)/\hbar}$, because the Fubini-Study metric is insensitive to overall phase and amplitude rescaling. The pilot-wave correspondence therefore cannot operate at the pure-state level.

This is not an obstruction but a *clue*. The Bohmian picture describes a particle moving in a wave field, but the pilot-wave effect — the non-classical force that deflects trajectories — has its physical origin in the coupling between the particle and its environment. In CR, this coupling is encoded precisely in the mixed-state cross-term $T_{\mu a}^{(\text{mix})}$, which measures how the *open-system* quantum state responds jointly to spacetime variation and frame adaptation.

## 2.3.2 The Mixed-State Cross-Term and Its Factorization

For the dephasing model introduced in §2.1.7, with density matrix

$$\rho(x, \xi) = \begin{pmatrix} p(\xi) & c(\xi)\,e^{-\Gamma(x)} \\ c^*(\xi)\,e^{-\Gamma(x)} & 1-p(\xi) \end{pmatrix},$$

**Eq. 2.3.1**

the Bures cross-term (computed in Appendix C) factorizes as:

$$T^{(\text{mix})}_{\mu a} = -\frac{1}{8}\,\partial_\mu\Gamma \cdot \mathcal{F}_a(\xi),$$

**Eq. 2.3.2**

where the **frame sensitivity function** $\mathcal{F}_a$ depends only on the coherence parameters:

$$\mathcal{F}_a := \frac{\partial_a\eta\,(1-\zeta) + \eta\,\partial_a\zeta}{1-\eta-\zeta},$$

**Eq. 2.3.3**

with $\eta := 4|c|^2 e^{-2\Gamma}$ (transverse Bloch length squared) and $\zeta := (2p-1)^2$ (longitudinal component squared).

The factorization (2.3.2) has a clean physical meaning: the cross-term separates into a spacetime factor ($\partial_\mu\Gamma$, the decoherence gradient) and a frame factor ($\mathcal{F}_a$, the sensitivity of the state to frame changes). The coupling vanishes if either factor is zero — that is, if decoherence is spatially uniform *or* if the state is insensitive to frame choice.

## 2.3.3 Adiabatic Elimination: The Effective Metric on M

When the $\Sigma$-sector relaxes fast compared to spacetime dynamics — that is, when the eigenvalues of $G_{ab}$ are large — the frame coordinates $\xi^a$ can be adiabatically eliminated. The standard Schur complement procedure (see Appendix C.2) yields an effective action on $M$ alone, with the effective metric:

$$G^{\text{eff}}_{\mu\nu} = G_{\mu\nu} - \frac{\lambda^2\,\chi}{64}\,\partial_\mu\Gamma\,\partial_\nu\Gamma,$$

**Eq. 2.3.4**

where $\chi := \mathcal{F}_a(G^{-1})^{ab}\mathcal{F}_b \geq 0$ is the **frame susceptibility scalar**, measuring how responsive the $\Sigma$-sector is to perturbations. The correction is rank-1 and negative semi-definite: integrating out $\Sigma$ *shortens* effective spacetime distances along the decoherence gradient.

## 2.3.4 Born-Oppenheimer Decomposition and the Quantum Potential

The metric correction (2.3.4) contributes to the effective dynamics but produces velocity-dependent (geodesic-type) forces, while the Bohmian quantum potential $Q$ is a velocity-independent scalar. To recover the scalar piece, we apply the Born-Oppenheimer decomposition — treating $x^\mu \in M$ as "slow" degrees of freedom and $\xi^a \in \Sigma$ as "fast" — and perform the standard Kaluza-Klein dimensional reduction.

**The adiabatic contribution.** The Born-Oppenheimer diagonal correction (BODC) captures the energy cost of adiabatically dragging the $\Sigma$-state through a varying decoherence landscape:

$$V_{\text{BODC}}(x) = \frac{\hbar^2}{2M_{\text{eff}}}\,\alpha(\eta,\zeta)\,|\nabla\Gamma|^2,$$

**Eq. 2.3.5**

where $\alpha := \eta(1-\zeta)/[4(1-\eta-\zeta)]$ is a purity-dependent factor derived from the spacetime block of the Bures metric, and $M_{\text{eff}}$ is the effective mass in the BO problem.

Under the standard decoherence-amplitude identification $\Gamma = -2\ln R$ (Joos-Zeh 1985, Zurek 2003), which relates the dephasing functional to the Bohmian amplitude via $R \sim e^{-\Gamma/2}$, this becomes:

$$V_{\text{BODC}} \propto \frac{|\nabla R|^2}{R^2}.$$

**Eq. 2.3.6**

This reproduces the $(\nabla R/R)^2$ part of the quantum potential.

**The geometric contribution.** Dimensional reduction from $M \times \Sigma$ to $M$ introduces a measure factor $\sqrt{\det G_{ab}(x)}$ in the effective kinetic operator. The standard Weyl transformation $\Psi = (\det G_{ab})^{-1/4}\Phi$ absorbs this measure factor and generates a **geometric potential**:

$$V_{\text{geom}}(x) = \frac{\hbar^2}{2M_{\text{eff}}}\left[\frac{1}{2}\nabla^2\ln g_\Sigma + \frac{1}{4}|\nabla\ln g_\Sigma|^2\right],$$

**Eq. 2.3.7**

where $g_\Sigma := \det G_{ab}(x)$. Since $G_{ab}$ depends on $x$ through $\eta(x)$, the Laplacian $\nabla^2\ln g_\Sigma$ contains a term proportional to $\nabla^2\Gamma$, which under $\Gamma = -2\ln R$ gives:

$$V_{\text{geom}} \supset \text{const} \times \frac{\nabla^2 R}{R}.$$

**Eq. 2.3.8**

This reproduces the $\nabla^2 R/R$ part of the quantum potential.

## 2.3.5 The Structural Correspondence

Combining both contributions, the effective potential on $M$ after integrating out $\Sigma$ takes the form:

$$V_{\text{eff}}(x) = C_1\,|\nabla\Gamma|^2 + C_2\,\nabla^2\Gamma + \text{(subleading)},$$

**Eq. 2.3.9**

where $C_1$ and $C_2$ are model-dependent constants built from the purity parameters $\alpha$, $\gamma := \eta\,g'(\eta)/g(\eta)$, and the effective mass $M_{\text{eff}}$.

The Bohmian quantum potential, expressed in terms of $\Gamma = -2\ln R$, has precisely this structure:

$$Q = \frac{\hbar^2}{4m}\left[\nabla^2\Gamma - \frac{1}{2}|\nabla\Gamma|^2\right].$$

**Eq. 2.3.10**

The identification $V_{\text{eff}} \leftrightarrow Q$ therefore holds at the level of functional form, with the mapping:

$$\frac{\hbar^2}{2m} \longleftrightarrow \lambda^2 \times (\text{Bures geometric factors}).$$

**Eq. 2.3.11**

The exact coefficients $C_1$ and $C_2$ depend on the specific mixed-state model through the purity-dependent factors $\alpha$ and $\gamma$. The sign condition $\gamma < 0$ — corresponding physically to the $\Sigma$-sector volume *decreasing* with increasing coherence — is required for the $\nabla^2\Gamma$ term to carry the correct sign. This condition is physically natural: more coherent states constrain the system to fewer accessible frame configurations, reducing the effective volume of $\Sigma$.

## 2.3.6 Physical Interpretation

The correspondence established above admits a concise physical reading:

*The Bohmian quantum potential is the Born-Oppenheimer effective potential that arises when the coherence-frame sector $\Sigma$ is integrated out of the joint $M \times \Sigma$ dynamics.*

More specifically:

The adiabatic piece $V_{\text{BODC}}$ captures the energetic cost of maintaining coherence-frame alignment as the system traverses a spatially varying decoherence landscape. The geometric piece $V_{\text{geom}}$ captures the measure effect: the $x$-dependent volume of the coherence-frame space generates a scalar correction upon dimensional reduction, analogous to the Kaluza-Klein scalar potential in higher-dimensional gravity.

Both contributions share three essential properties with $Q$: (i) they are velocity-independent scalar potentials, resolving the contrast with the velocity-dependent metric correction of Eq. 2.3.4; (ii) they vanish when $\lambda \to 0$ (no spacetime-frame coupling); and (iii) they require genuine mixed states — for pure states ($\eta + \zeta = 1$), the Bures metric becomes singular and the BO approximation breaks down.

The third property is significant. In the de Broglie-Bohm interpretation, $Q$ is a property of the pure wave function $\psi$. In CR, the analogous object arises from the mixed-state Bures geometry of an open system. The pilot-wave effect, in this reading, is not a primitive feature of the wave function but an emergent consequence of decoherence-mediated coupling between spacetime and the coherence-frame sector — present whenever the system is genuinely open ($\eta + \zeta < 1$) and the decoherence landscape is spatially inhomogeneous ($\nabla\Gamma \neq 0$).

## 2.3.7 Scope and Limitations

The correspondence demonstrated here is structural: it establishes that the $M \times \Sigma$ formalism generates the correct derivative structures ($|\nabla\Gamma|^2$ and $\nabla^2\Gamma$) with the correct physical properties (velocity-independent, classically vanishing, mixed-state-requiring). The exact coefficient matching that would promote this from structural correspondence to quantitative identity depends on the specific choice of mixed-state model through the purity parameters $\alpha$ and $\gamma$, and is deferred to future work.

Additionally, the present analysis treats a single-particle dephasing model. The extension to $N$-body systems — where Bohmian nonlocality manifests through the configuration-space dependence of $Q$ — maps in CR to entanglement structure within the $\Sigma$-sector. This extension, which requires a multi-particle generalization of the Bures cross-term, lies beyond the scope of the present paper.

The experimental bridge between these formalisms may be accessible through weak-measurement reconstructions of Bohmian trajectories (Kocsis *et al.* 2011, Mahler *et al.* 2016), which measure the local momentum field $\nabla S/m$. The CR framework predicts specific decoherence-dependent modifications to these trajectories — a prediction that could distinguish the two pictures experimentally.

---

**References for this section:**

- Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of "hidden" variables. *Phys. Rev.* **85**, 166–193.
- Braunstein, S. L. & Caves, C. M. (1994). Statistical distance and the geometry of quantum states. *Phys. Rev. Lett.* **72**, 3439.
- Hübner, M. (1992). Explicit computation of the Bures distance for density matrices. *Phys. Lett. A* **163**, 239–242.
- Joos, E. & Zeh, H. D. (1985). The emergence of classical properties through interaction with the environment. *Z. Phys. B* **59**, 223–243.
- Kocsis, S. *et al.* (2011). Observing the average trajectories of single photons in a two-slit interferometer. *Science* **332**, 1170–1173.
- Mahler, D. H. *et al.* (2016). Experimental nonlocal and surreal Bohmian trajectories. *Sci. Adv.* **2**, e1501466.
- Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Rev. Mod. Phys.* **75**, 715–775.

---

## Appendix C: Derivation of the Pilot-Wave Correspondence (Skeleton)

*Full computation to appear in appendix. Skeleton for structure:*

### C.1 Bures Cross-Term for the Dephasing Model
- Bloch representation (Eq. D-2)
- Spacetime derivatives (Eqs. D-5–D-8)
- Frame derivatives (Eqs. D-9–D-11)
- Cross-term computation and factorization (Eqs. D-12–D-19)

### C.2 Adiabatic Elimination via Schur Complement
- Full M × Σ action (Eq. D-20)
- Adiabatic limit and Σ equilibrium (Eqs. D-21–D-22)
- Effective M-sector action (Eq. D-23)
- Substitution of factored cross-term → Eq. 2.3.4 (Eqs. D-24–D-27)

### C.3 Born-Oppenheimer Decomposition
- BO analogy: Σ = "fast", M = "slow" (§12.1 of working document)
- BODC computation (Eqs. D-60–D-68)
- Decoherence-amplitude bridge Γ = -2 ln R (Eqs. D-33–D-37)
- Match to (∇R/R)² part of Q

### C.4 Kaluza-Klein Reduction and Geometric Potential
- Effective Schrödinger equation with measure factor (Eq. D-75)
- Weyl transformation Ψ = g_Σ^{-1/4} Φ (Eqs. D-76–D-78)
- Geometric potential V_geom (Eq. D-79)
- Evaluation for dephasing model (Eqs. D-80–D-84)
- Match to ∇²R/R part of Q

### C.5 Combined Result and Assessment
- V_eff = V_BODC + V_geom (Eq. D-87)
- Structural match summary (Eq. D-88)
- Sign condition γ < 0
- What is structural vs. numerical
