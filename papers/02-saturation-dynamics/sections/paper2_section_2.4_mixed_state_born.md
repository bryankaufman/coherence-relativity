# §2.4 Mixed-State Born Rule via Purification

## 2.4.1 Introduction: From Pure to Mixed States

Paper 1 established axioms (A1)–(A4) for coherence-frame geometry and proved that these axioms recover the Born rule for pure states:
$$P(a|\psi) = |\langle a|\psi\rangle|^2 \quad \text{(Pure state)}$$

However, real quantum systems are rarely in pure states. Decoherence, thermal noise, entanglement with uncontrolled environments, and incomplete information all produce **mixed states** described by density operators $\rho \in \mathcal{D}(\mathcal{H})$. Paper 1 (line 45) explicitly deferred the mixed-state extension to Paper 2.

This section delivers that extension. The strategy is conceptually simple: every mixed state is the partial trace of *some* pure state on a larger system (the **purification theorem**). We apply Paper 1's axioms (A1)–(A4) to that pure-state purification, then trace over the environment to recover the standard mixed-state Born rule:
$$P(a|\rho) = \text{Tr}(\rho M_a)$$

Crucially, we show that this result is **purification-independent**: different purifications of the same $\rho$ yield identical probabilities. This independence confirms that the axioms are extracting objective physics, not sensitive artifacts of the mathematical representation.

We also extend to general POVMs (positive-operator-valued measures) via Naimark dilation, completing the measurement framework. Finally, we address potential circularity: the partial trace and Naimark dilation rely on no hidden assumptions about probability—they are purely mathematical constructions in Hilbert space.

---

## 2.4.2 Purification Theorem and Existence

**Theorem 2.4.1 (Purification).** Let $\rho$ be a density operator on system $S$ with $\text{rank}(\rho) = r \leq d_S = \dim(\mathcal{H}_S)$. For any auxiliary system $E$ (environment) with $\dim(\mathcal{H}_E) \geq r$, there exists a pure state $|\Psi\rangle \in \mathcal{H}_S \otimes \mathcal{H}_E$ such that
$$\rho_S = \text{Tr}_E(|\Psi\rangle\langle\Psi|).$$
Any two purifications $|\Psi\rangle$ and $|\Psi'\rangle$ are related by a unitary $U_E$ on the environment:
$$|\Psi'\rangle = (\mathbb{I}_S \otimes U_E) |\Psi\rangle. \quad \text{(Eq. 2.4.1)}$$

**Sketch of proof:** Given a spectral decomposition $\rho = \sum_{j=1}^r \lambda_j |\phi_j\rangle\langle\phi_j|$ with $\lambda_j > 0$, define
$$|\Psi\rangle = \sum_{j=1}^r \sqrt{\lambda_j} |\phi_j\rangle_S \otimes |e_j\rangle_E$$
where $\{|e_j\rangle_E\}$ is an orthonormal basis of $\mathcal{H}_E$. Then $\text{Tr}_E(|\Psi\rangle\langle\Psi|) = \rho_S$ by direct calculation. The unitary freedom (Eq. 2.4.1) reflects that we can always perform a unitary on $E$ without changing the reduced density matrix on $S$.

This theorem is a foundational result in quantum information theory. Its key feature is **purification independence**: the full pure state on $S \otimes E$ is not unique, but the reduced state on $S$ is. This is exactly what we exploit.

---

## 2.4.3 Applying Axioms (A1)–(A4) to the Purification

**Step 1: Extend the state space.**

Take a mixed state $\rho$ on system $S$ and construct any purification $|\Psi\rangle \in \mathcal{H}_S \otimes \mathcal{H}_E$. The state $|\Psi\rangle$ is a pure state on the combined system $S \otimes E$.

**Step 2: Define the metric on the enlarged system.**

Since $|\Psi\rangle$ is pure, Paper 1's axioms (A1)–(A4) apply directly to it. The Fubini-Study metric $G_{AB}$ on $\mathcal{H}_S \otimes \mathcal{H}_E$ is well-defined:
$$G_{AB} = \partial_A \partial_B \left[ \log \langle \Psi | \Psi \rangle \right], \quad \text{(Eq. 2.4.2)}$$
where indices $A, B$ collectively label all parameters in the enlarged Hilbert space. By (A1), $G_{AB}$ depends on $|\Psi\rangle$. By (A2), it is invariant under $|\Psi\rangle \to e^{i\alpha}|\Psi\rangle$. By (A3) and (A4), it satisfies the monotonicity and normalization axioms.

**Step 3: Measurement model on the enlarged system.**

Consider a projective measurement on $S$ alone: a set of orthogonal projectors $\{\Pi_a\}$ on $\mathcal{H}_S$. On the enlarged system, this extends to
$$\tilde{\Pi}_a = \Pi_a \otimes \mathbb{I}_E. \quad \text{(Eq. 2.4.3)}$$

By Paper 1's construction, the probability of outcome $a$ is given by the Born rule applied to the pure state $|\Psi\rangle$:
$$P_{\text{enlarged}}(a|\Psi) = \langle\Psi|\tilde{\Pi}_a|\Psi\rangle = \langle\Psi|(\Pi_a \otimes \mathbb{I}_E)|\Psi\rangle.$$

This is the fundamental input from Paper 1's axioms: for a pure state, the projection postulate holds.

---

## 2.4.4 Derivation of the Mixed-State Born Rule

**Step 1: Trace over the environment.**

Compute the probability of outcome $a$ by tracing over the environment:
$$P(a|\rho) = \text{Tr}_E \left[\langle\Psi|(\Pi_a \otimes \mathbb{I}_E)|\Psi\rangle\right].$$

Using the definition of the partial trace (Definition: $\text{Tr}_E(X) = \sum_j (\mathbb{I}_S \otimes \langle e_j|_E) X (\mathbb{I}_S \otimes |e_j\rangle_E)$), we have
$$P(a|\rho) = \sum_j \langle e_j|_E \langle\Psi|(\Pi_a \otimes \mathbb{I}_E)|\Psi\rangle|e_j\rangle_E$$
$$= \sum_j \text{Tr}_S\left[\Pi_a (\text{Tr}_E(|\Psi\rangle\langle\Psi|))\right].$$

By the purification theorem, $\text{Tr}_E(|\Psi\rangle\langle\Psi|) = \rho_S$:
$$P(a|\rho) = \text{Tr}_S(\Pi_a \rho_S) = \text{Tr}(\rho M_a), \quad \text{(Eq. 2.4.4)}$$
where $M_a = \Pi_a$ is the projector (which is a special case of a POVM element).

**Step 2: Physical interpretation.**

Equation 2.4.4 is the standard mixed-state Born rule. It says: the probability of outcome $a$ given a mixed state $\rho$ is the expectation value of the measurement operator $M_a$ in state $\rho$. This is Gleason's theorem in the context of finite-dimensional Hilbert spaces (Gleason, 1957), but here it emerges from applying Paper 1's axioms (A1)–(A4) to a purification rather than being assumed a priori.

**Key point:** The derivation depends on two inputs:
1. Paper 1's axioms (A1)–(A4), which give the pure-state Born rule.
2. The purification theorem, which asserts the mathematical existence of a pure-state extension.

Neither of these inputs assumes the mixed-state Born rule—we derive it, not presuppose it.

---

## 2.4.5 Purification Independence

A critical question: does $P(a|\rho)$ depend on which purification $|\Psi\rangle$ we choose?

**Theorem 2.4.2 (Purification Independence).** The probability $P(a|\rho) = \text{Tr}(\rho M_a)$ is **independent** of the choice of purification.

**Proof:**

Let $|\Psi\rangle$ and $|\Psi'\rangle$ be two purifications of $\rho$. By Theorem 2.4.1,
$$|\Psi'\rangle = (\mathbb{I}_S \otimes U_E) |\Psi\rangle$$
for some unitary $U_E$ on $\mathcal{H}_E$. Compute the probability using $|\Psi'\rangle$:
$$P'(a|\rho) = \langle\Psi'|(\Pi_a \otimes \mathbb{I}_E)|\Psi'\rangle$$
$$= \langle\Psi|(\mathbb{I}_S \otimes U_E^\dagger)(\Pi_a \otimes \mathbb{I}_E)(\mathbb{I}_S \otimes U_E)|\Psi\rangle.$$

Since $\Pi_a$ acts only on $S$, it commutes with all operators on $E$:
$$= \langle\Psi|(\Pi_a \otimes (\mathbb{I}_E U_E^\dagger U_E))|\Psi\rangle = \langle\Psi|(\Pi_a \otimes \mathbb{I}_E)|\Psi\rangle = P(a|\rho).$$

Thus, $P'(a|\rho) = P(a|\rho)$ for any choice of unitary $U_E$.

**Physical meaning:** This theorem confirms that the mixed state $\rho_S$ contains all the objective information needed to compute probabilities. The environment $E$ and its description are auxiliary; different choices amount to unitary relabelings of unobserved degrees of freedom, which do not affect observable probabilities. $\square$

---

## 2.4.6 Extension to Positive-Operator-Valued Measures (POVMs)

Equation 2.4.4 derived the Born rule for **projective measurements** on system $S$. In general, however, quantum measurements are described by POVMs, not just projectors. We extend using Naimark's theorem.

**Theorem 2.4.3 (Naimark Dilation).** Let $\{M_a\}_{a \in X}$ be a POVM on system $S$, so
$$\sum_a M_a = \mathbb{I}_S, \quad M_a \geq 0.$$
Then there exists an auxiliary (ancilla) Hilbert space $\mathcal{H}_A$ and a set of orthogonal projectors $\{\tilde{\Pi}_a\}$ on $\mathcal{H}_S \otimes \mathcal{H}_A$ such that
$$M_a = \text{Tr}_A(\tilde{\Pi}_a), \quad \text{(Eq. 2.4.5)}$$
and $\dim(\mathcal{H}_A) \leq \dim(\mathcal{H}_S)$.

In other words, every POVM can be "dilated" to a projective measurement on a larger space—its outcome is obtained by measuring projectively on $S \otimes A$ and ignoring the ancilla $A$.

**Derivation of the POVM Born rule:**

Given a mixed state $\rho$ on $S$ and a POVM $\{M_a\}$, purify $\rho$ to $|\Psi\rangle \in \mathcal{H}_S \otimes \mathcal{H}_E$. Now dilate the POVM to a projective measurement $\{\tilde{\Pi}_a\}$ on $S \otimes A$. On the enlarged space $S \otimes E \otimes A$, the state is still $|\Psi\rangle \otimes |0_A\rangle$ (or more precisely, $|\Psi\rangle$ extended to $\mathcal{H}_A$ trivially). The projective measurement yields
$$P(a|\rho) = \text{Tr}_{E,A}(\text{Tr}_{E,A}((\tilde{\Pi}_a \otimes \mathbb{I}_E)|\Psi\rangle\langle\Psi| \otimes |0_A\rangle\langle 0_A|)).$$

By the partial trace formula:
$$= \text{Tr}_{A}(\text{Tr}_{E}(\tilde{\Pi}_a |\Psi\rangle\langle\Psi|))= \text{Tr}(\rho M_a), \quad \text{(Eq. 2.4.6)}$$
using Eq. 2.4.5 in the last step.

Thus, Equations 2.4.4 and 2.4.6 are consistent: the POVM Born rule is a generalization of the projective case, and it follows from the same framework.

---

## 2.4.7 Checking for Hidden Circularity

A natural concern: have we smuggled in the Born rule through the back door? We address three potential sources of circularity.

### 2.4.7.1 Does the partial trace presuppose the Born rule?

**No.** The partial trace $\text{Tr}_E : \mathcal{B}(\mathcal{H}_S \otimes \mathcal{H}_E) \to \mathcal{B}(\mathcal{H}_S)$ is a linear map defined by:
$$\text{Tr}_E(X) = \sum_j (\mathbb{I}_S \otimes \langle e_j|_E) X (\mathbb{I}_S \otimes |e_j\rangle_E),$$
where $\{|e_j\rangle_E\}$ is any orthonormal basis of $\mathcal{H}_E$. This definition is algebraic and basis-independent. It depends only on the tensor-product structure of Hilbert space, not on any probabilistic postulate.

Similarly, the fact that $\text{Tr}_E(|\Psi\rangle\langle\Psi|) = \rho$ is a pure algebraic identity, verified by direct calculation. No invocation of probability is needed.

### 2.4.7.2 Does Naimark's theorem introduce new assumptions?

**No.** Naimark's theorem (Theorem 2.4.3) asserts the existence of an ancilla space $\mathcal{H}_A$ and projectors $\{\tilde{\Pi}_a\}$ such that Eq. 2.4.5 holds. This is a theorem in linear algebra / Hilbert space theory. The existence proof constructs the space explicitly using spectral decomposition; no probabilistic reasoning is involved.

The dilation is a mathematical enlargement of the state space, exactly as purification is. Once the dilated measurement exists, we apply Paper 1's axioms (A1)–(A4) to it—but those axioms themselves are the only probabilistic input.

### 2.4.7.3 Does applying (A1)–(A4) to the purification reintroduce the problem?

**No.** Paper 1 proved that axioms (A1)–(A4) imply the Born rule for pure states. That derivation—and all its assumptions—are transparent in Paper 1. We do not reprove that derivation here; we cite it. The only new step in this section is to extend from pure to mixed states via purification and partial trace. These are algebraic operations, not probabilistic.

**Conclusion:** The logic is linear and acyclic:
1. Paper 1's axioms (A1)–(A4) → pure-state Born rule (Paper 1).
2. Purification theorem → mixed state is the partial trace of a pure state (Theorem 2.4.1, standard QIT).
3. Apply pure-state Born rule to the purification → mixed-state Born rule (Eq. 2.4.4).
4. Generalize via Naimark dilation (Theorem 2.4.3, standard QIT).

No circularity; no hidden assumptions.

---

## 2.4.8 Self-Containedness and Independence from Models

This section makes no reference to:
- The KK-Cone or any geometric model from Papers 1 or 3.
- Any assumption beyond the existence of purifications (guaranteed by linear algebra) and axioms (A1)–(A4) from Paper 1.
- Any special structure of the coherence frame beyond what is needed for the pure-state Born rule.

The extension to mixed states is thus **model-independent**. If axioms (A1)–(A4) hold for pure states in any framework, then by this section's argument, they automatically extend to mixed states with the standard Born rule. This is a general principle, not specific to the coherence-frame interpretation.

---

## 2.4.9 Summary and Implications

**Main Results:**

1. **Theorem 2.4.1 (Purification):** Every mixed state $\rho$ on $S$ is the partial trace of a pure state on $S \otimes E$. Different purifications are related by unitaries on $E$ only.

2. **Mixed-State Born Rule (Eq. 2.4.4):** For any mixed state $\rho$ and projective measurement $\{\Pi_a\}$,
   $$P(a|\rho) = \text{Tr}(\rho \Pi_a).$$
   This follows from applying Paper 1's axioms (A1)–(A4) to a purification and tracing over the environment.

3. **Theorem 2.4.2 (Purification Independence):** The probability is independent of the choice of purification, confirming that the mixed-state density operator contains all objective information.

4. **POVM Extension (Eq. 2.4.6):** The framework extends to general POVMs via Naimark dilation. The Born rule $P(a|\rho) = \text{Tr}(\rho M_a)$ holds for any POVM $\{M_a\}$.

5. **No Circularity:** The derivation relies only on Paper 1's axioms and standard quantum information theory (purification, partial trace, Naimark dilation). The partial trace and dilation are algebraic; they do not presuppose the Born rule.

**Implications for the Coherence-Frame Picture:**

- Axioms (A1)–(A4) are sufficient to recover both the pure and mixed-state Born rule.
- The coherence-frame geometry, while defined for pure states, automatically induces the correct probabilities for mixed states via purification.
- The framework is physically consistent: different choices of environmental extension (different purifications) yield the same observable probabilities.

**Bridge to Papers 1 and 3:**

- Paper 1 showed that (A1)–(A4) yield the pure-state Born rule and sketched the need for extension to mixed states.
- This section delivers that extension rigorously and model-independently.
- Paper 3 will apply this framework to specific models (e.g., the KK-Cone) and show how decoherence and purification dynamics emerge naturally within the coherence-frame geometry.

---

## References

- Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *J. Math. Mech.*, 6(6), 885–893.
- Naimark, M. A. (1940). On a representation of additive operator set functions. *C. R. (Dokl.) Acad. Sci. URSS*, 41(5), 373–375.
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information* (10th ed.). Cambridge University Press.
- Uhlmann, A. (1976). The "transition probability" in the state space of a *-algebra. *Rep. Math. Phys.*, 9(2), 273–279.
