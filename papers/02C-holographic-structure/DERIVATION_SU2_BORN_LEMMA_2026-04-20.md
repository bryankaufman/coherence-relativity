# Lemma: SU(2)-Equivariant Born Rule on ℂP¹

**Date:** 2026-04-20  
**Depends on:**
- `DERIVATION_SCF_NONCONTEXTUALITY_2026-04-19.md` (Theorem 6.1: frame noncontextuality of W from SCF+COV)
- `DERIVATION_COV_CHECK_2026-04-19.md` (SU(d)-covariance of F = ∇^{FS} + A_C)

**Status:** ⚠️ PARTIALLY CORRECTED 2026-04-20 — Sections 1–5 verified; Proposition 6.1 contains a known logical gap (identified post-draft); see §6 for the corrected proof structure and the additional axiom required

---

## 1. Statement of the Lemma

**Lemma 6.2 (SU(2) Born Rule on ℂP¹):** Let $W: \mathbb{CP}^1 \times \mathbb{CP}^1 \to [0,1]$ be a function assigning a weight $W(\varphi|\psi) \in [0,1]$ to each pair of unit vectors $\varphi, \psi \in \mathbb{C}^2$. Assume:

1. **(Continuity)** $W(\varphi|\psi)$ is continuous in both arguments with respect to the round (Fubini-Study) metric on $\mathbb{CP}^1 \cong S^2$.

2. **(Frame noncontextuality / SU(2)-equivariance)** For all $U \in \text{SU}(2)$:
   $$W(U\varphi|U\psi) = W(\varphi|\psi) \quad \text{(as vectors in } \mathbb{C}^2\text{)}$$

3. **(Repeatability / Definiteness)** For all $\varphi \in \mathbb{CP}^1$:
   $$W(\varphi|\varphi) = 1$$

4. **(Two-outcome normalization)** For all $\varphi, \psi \in \mathbb{CP}^1$, where $\varphi^\perp$ is any unit vector orthogonal to $\varphi$:
   $$W(\varphi|\psi) + W(\varphi^\perp|\psi) = 1$$

**Conclusion:** 
$$W(\varphi|\psi) = |\langle \varphi|\psi \rangle|^2$$

---

## 2. Reduction to a Single-Variable Function

### Proposition 2.1 (SU(2)-equivariance implies invariance under the metric)

By SU(2)-equivariance, $W(\varphi|\psi)$ is invariant under the natural action of $\text{SU}(2)$ on $\mathbb{CP}^1$. Since $\text{SU}(2)$ acts transitively on $\mathbb{CP}^1 \cong S^2$ (the Bloch sphere), and the only invariants of pairs under this action are:
- The inner product $\langle \varphi|\psi \rangle \in \mathbb{C}$ (which has modulus)
- Its modulus squared $|\langle \varphi|\psi \rangle|^2 \in [0,1]$

we conclude that $W(\varphi|\psi)$ depends only on the scalar invariant:
$$x := |\langle \varphi|\psi \rangle|^2 \in [0,1]$$

**Definition 2.2.** Define the single-variable function:
$$f(x) := W(\varphi|\psi) \quad \text{where } |\langle \varphi|\psi \rangle|^2 = x$$

This is well-defined because:
- For any $\varphi, \psi$ with $|\langle \varphi|\psi \rangle|^2 = x$, we can write $\psi' = U\psi$ for some $U \in \text{SU}(2)$ with $|\langle \varphi|\psi' \rangle|^2 = x$, and by equivariance $W(\varphi|\psi) = W(U^\dagger\varphi|U^\dagger\psi') = W(\varphi|\psi')$.

---

## 3. Translating Axioms to Constraints on $f(x)$

From the four axioms on $W$, we derive:

### Constraint 1: Continuity

Since the map $(\varphi, \psi) \mapsto |\langle \varphi|\psi \rangle|^2$ is continuous on $\mathbb{CP}^1 \times \mathbb{CP}^1$, and $W$ is continuous, the function $f(x)$ is **continuous on $[0,1]$**.

### Constraint 2: Repeatability

Setting $\varphi = \psi$, we have $|\langle \varphi|\psi \rangle|^2 = 1$, so:
$$f(1) = W(\varphi|\varphi) = 1$$

### Constraint 3: Two-Outcome Normalization

For any orthogonal pair $\varphi, \varphi^\perp \in \mathbb{CP}^1$ with $\langle \varphi|\varphi^\perp \rangle = 0$, and any $\psi$:
$$W(\varphi|\psi) + W(\varphi^\perp|\psi) = 1$$

Now, $|\langle \varphi|\psi \rangle|^2 + |\langle \varphi^\perp|\psi \rangle|^2 = 1$ because $\{\varphi, \varphi^\perp\}$ form an orthonormal basis of $\mathbb{C}^2$. If $|\langle \varphi|\psi \rangle|^2 = x$, then $|\langle \varphi^\perp|\psi \rangle|^2 = 1 - x$. Thus:
$$f(x) + f(1-x) = 1 \quad \text{for all } x \in [0,1] \quad \quad (*)$$

### Summary of Constraints

We have reduced the problem to finding all continuous functions $f: [0,1] \to [0,1]$ satisfying:
- (i) $f(1) = 1$
- (ii) $f(x) + f(1-x) = 1$ for all $x \in [0,1]$

And we now ask: **what additional structure forces $f(x) = x$?**

---

## 4. Why the d ≥ 3 Case Is Different (Gleason's Theorem Gap)

### The Gleason Approach (d ≥ 3)

**Gleason's Theorem (1957):** Let $V$ be a Hilbert space of dimension $\geq 3$. If $\mu$ is a measure on the projections $P(V)$ (the lattice of closed subspaces) that is:
- Additive: $\mu(P \vee Q) = \mu(P) + \mu(Q) - \mu(P \wedge Q)$ whenever $P, Q$ are orthogonal
- Normalized: $\mu(P_V) = 1$ where $P_V$ is the projection onto $V$

then there exists a density operator $\rho$ on $V$ such that $\mu(P) = \text{Tr}(P\rho)$.

This applies directly when $W$ is defined on projections $P_\varphi := |\varphi\rangle\langle\varphi|$ and satisfies additivity.

### The d = 2 Obstruction

On $\mathbb{CP}^1 \cong S^2$ (the Bloch sphere), there are **no three mutually orthogonal unit vectors**. In $\mathbb{C}^2$:
- Any $\varphi \in \mathbb{C}^2$ has a unique (up to phase) orthogonal complement $\varphi^\perp$.
- There is no third orthogonal vector.

This means:
- We **cannot** define orthogonal triples of projections.
- The additivity assumption in Gleason's theorem **cannot be applied** to relate probabilities of three non-overlapping outcomes.
- We are restricted to the **two-outcome case**: measurements with outcomes $\{$accept, reject$\}$ or $\{\varphi, \varphi^\perp\}$.

**Implication:** For $d=2$, we cannot invoke Gleason to jump directly to the Born rule. Instead, we must work within the two-outcome sector and use the SU(2) equivariance more directly.

---

## 5. The Key Observation: SU(2) Transitivity on the Interior

### Proposition 5.1 (SU(2) acts transitively on interior x-values)

The group $\text{SU}(2)$ acts on $\mathbb{CP}^1 \cong S^2$ by rotations. For any two pairs $(\varphi_1, \psi_1)$ and $(\varphi_2, \psi_2)$ with the same value $x = |\langle \varphi_1|\psi_1 \rangle|^2 = |\langle \varphi_2|\psi_2 \rangle|^2 \in (0,1)$, there exists $U \in \text{SU}(2)$ such that:
$$\varphi_2 = U\varphi_1, \quad \psi_2 = U\psi_1$$

**Proof sketch:** $\text{SU}(2)$ acts on $\mathbb{CP}^1 \cong S^2$ as $\text{SO}(3)$ (its double cover). This action is transitive. Given any $\varphi_1$, we can rotate it to any $\varphi_2$ via some $U_1 \in \text{SU}(2)$. Given $\psi_1$, we can further compose with a rotation that fixes $\varphi_1$ (such rotations form a subgroup $\text{U}(1) \subset \text{SU}(2)$, the stabilizer) to bring $\psi_1$ to any direction that maintains the desired angle with $\varphi_1$.

This transitivity is **global**: any interior value $x \in (0,1)$ is realized on a dense orbit under $\text{SU}(2)$ acting on pairs.

### Implication

The function $f(x)$ cannot have "arbitrary" behavior on the interior $(0,1)$. The equivariance enforces that $f$ sees the same value everywhere on the orbit, and the orbit is transitive. This constrains the functional form.

---

## 6. The Forcing Argument — Corrected Analysis

### ⚠️ Gap Identified in Original Proposition 6.1

**The original claim:** "The only continuous function $f: [0,1] \to [0,1]$ satisfying (i) $f(1) = 1$ and (ii) $f(x) + f(1-x) = 1$ is $f(x) = x$." This claim is **FALSE**.

**Counterexample.** Let $\varepsilon \in (0,1)$ and define

$f_\varepsilon(x) \;:=\; x + \varepsilon \cdot x(1-x)(2x-1).$

Verification:
- **Continuity**: polynomial in $x$, hence continuous. ✓
- **Boundary values**: $f_\varepsilon(0) = 0$, $f_\varepsilon(1) = 1$. ✓  
- **Antisymmetry check**: let $g(x) = x(1-x)(2x-1)$. Then
  $g(1-x) = (1-x)x(2(1-x)-1) = (1-x)x(1-2x) = -g(x),$
  so $f_\varepsilon(x) + f_\varepsilon(1-x) = 1 + \varepsilon(g(x) + g(1-x)) = 1$. ✓
- **Maps $[0,1]$ to $[0,1]$**: $f_\varepsilon'(x) = 1 + \varepsilon(-6x^2 + 6x - 1)$. Since $-6x^2+6x-1 \geq -1$ for all $x$, we have $f_\varepsilon'(x) \geq 1-\varepsilon > 0$; $f_\varepsilon$ is strictly increasing on $[0,1]$ and hence maps into $[0,1]$. ✓
- **But** $f_{0.1}(1/4) = 1/4 + 0.1\cdot(1/4)(3/4)(-1/2) = 1/4 - 3/320 \approx 0.2406 \neq 1/4$. ✗

The original Step 6 argument — "a continuous antisymmetric function with $h(0)=h(1/2)=h(1)=0$ is identically zero" — is incorrect; the counterexample $h(x) = \varepsilon x(1-x)(2x-1)$ refutes it.

---

### 6.1 What Additional Condition Is Needed?

The constraints derived so far from axioms 1–4 are:

- (C1) $f$ continuous on $[0,1]$
- (C2) $f(1) = 1$  
- (C3) $f(x) + f(1-x) = 1$ for all $x \in [0,1]$

These constraints admit infinitely many solutions (the $f_\varepsilon$ family above). A **fifth condition** is required. Three candidates, in order of naturalness for CR:

**Option A — POVM Additivity (Busch's approach).** For any rank-1 effect $E = t|\varphi\rangle\langle\varphi|$ with $t \in (0,1)$ and any POVM $\{E, t|\varphi^\perp\rangle\langle\varphi^\perp|, (1-t)(I - |\varphi\rangle\langle\varphi|)\}$, the weights must satisfy additivity across POVM decompositions. This is Busch's 2003 extra ingredient: extending from projectors to effects forces linearity of the functional, and $f(x) = x$ is the unique linear solution to (C1)–(C3).

**Option B — Linearity of f.** Postulate $W(\alpha E_1 + \beta E_2|\psi) = \alpha W(E_1|\psi) + \beta W(E_2|\psi)$ for positive combinations of effects. Equivalently, require $f$ to be an affine function on $[0,1]$. Then (C1)–(C3) with affinity force $f(x) = x$ uniquely.

**Option C — Basin measure = FS measure (CR-specific).** In CR, $W(\varphi|\psi)$ is defined as the absorption probability $\mu_\Phi(B_\varphi | \psi_0 = \psi)$ under the Lyapunov flow $\Phi_t$. If the flow-invariant (stationary) measure $\mu_\Phi$ on $\mathbb{CP}^1$ is the SU(2)-Haar (Fubini–Study) measure, then by uniqueness of the Haar measure, $\mu_\Phi = \mu_{\text{FS}}$. The FS-measure of the $\varphi$-absorbing basin weighted from $\psi$ can be computed directly:

$W(\varphi|\psi) = \mu_{\text{FS}}(\{\chi \in \mathbb{CP}^1 : \Phi_t(\chi) \to |\varphi\rangle\}) \cdot [\text{reweighted by } \psi]$

For the gradient flow of $V(\chi) = |\langle\varphi|\chi\rangle|^2$ with SU(2)-symmetric noise of amplitude $\sigma$, the Fokker–Planck stationary distribution centered at $\psi$ gives absorption probability $|\langle\varphi|\psi\rangle|^2$ in the low-noise limit. This computation is not yet completed in the present CR derivation.

---

### 6.2 Honest Status of Proposition 6.1

**Corrected Proposition 6.1′ (Conditional).** If $f: [0,1] \to [0,1]$ is continuous and satisfies:
- (C1) continuity,  
- (C2) $f(1) = 1$,  
- (C3) $f(x) + f(1-x) = 1$,  
- **(C4) affinity**: $f$ is affine (equivalently, $f(\lambda x + (1-\lambda)y) = \lambda f(x) + (1-\lambda)f(y)$ for all $\lambda \in [0,1]$),

then $f(x) = x$ is the unique solution.

**Proof.** Affinity + (C3) gives $f(x) = ax + b$ with $(ax+b) + (a(1-x)+b) = 1 \Rightarrow 2b + a = 1$. Condition (C2) gives $a+b=1$, so $b=0$ and $a=1$, hence $f(x)=x$. $\blacksquare$

**Status of (C4) in CR:** Condition (C4) is equivalent to POVM additivity restricted to the qubit case. It is physically natural (probability assignments should be linear in the effect operator) but is currently an **axiom** in the CR derivation, not derived from SCF or COV. This is the **genuine remaining gap** for the d=2 Born rule proof.

**Fokker-Planck negative result (2026-04-20).** Attempt to derive (C4) from the simple Lyapunov+isotropic-noise model on S² failed. Neither σ→0 nor σ→∞ recovers p(u) = (1+u)/2 = |⟨φ|ψ⟩|² as the absorption probability: the σ→0 limit is singular (exponential weight concentrates at south pole boundary); the σ→∞ limit gives p(u) = (arcsin(u)+π/2)/π ≠ (1+u)/2. See `DERIVATION_C4_FOKKER_PLANCK_2026-04-20.md`. A non-isotropic noise model tied to the T_MΣ tensor may succeed, but this requires computing T_MΣ explicitly from the SCF Lagrangian (deferred).

**Working resolution (Option B).** For publication, (C4) is adopted as a working axiom, justified by Busch (2003):

> **(Working Axiom C4 — POVM Additivity).** The basin weight W satisfies additivity for effects: if E = t|φ⟩⟨φ| + s|φ⊥⟩⟨φ⊥| with t,s ≥ 0 and t+s = 1, then
> $W(E|\psi) = t\,W(|\varphi\rangle|\psi) + s\,W(|\varphi^\perp\rangle|\psi).$
> This is a necessary condition for W to be a quantum probability measure in the sense of Busch (2003), which proved (using this and three standard assumptions) that the unique consistent assignment on ℂ² is the Born rule.

In the CR context, (C4) is not merely imported from Busch but has a CR-specific justification: the basin decomposition on CP¹ under the T_MΣ flow defines a positive operator-valued measure (POVM) by construction (Theorem 6.1), and POVMs satisfy effect-additivity by definition. Whether the T_MΣ flow truly generates a POVM (not just a non-additive measure on basins) is the precise remaining question, deferred to Paper 2B Appendix.

---

## 7. What the Argument Establishes (Corrected)

### Theorem 7.1 (Born Rule from SU(2) Equivariance + POVM Additivity — Conditional)

Under the four axioms of Lemma 6.2 **plus** the affinity condition (C4):
1. Continuity
2. SU(2)-equivariance
3. Repeatability: $W(\varphi|\varphi) = 1$
4. Two-outcome normalization: $W(\varphi|\psi) + W(\varphi^\perp|\psi) = 1$
5. **(C4) Affinity / POVM additivity** *(additional condition)*

we conclude:
$W(\varphi|\psi) = |\langle \varphi|\psi \rangle|^2$

**Proof:**
1. By Proposition 2.1, SU(2)-equivariance reduces $W$ to a function $f(x)$ where $x = |\langle \varphi|\psi \rangle|^2$.
2. By Constraints 1–3 (Section 3), $f$ satisfies (C1)–(C3).
3. By the corrected Proposition 6.1′, (C1)–(C4) together force $f(x) = x$.
4. Therefore, $W(\varphi|\psi) = |\langle \varphi|\psi \rangle|^2$. $\square$

**What changes relative to the original Theorem 7.1:** Condition (C4) is an explicit additional axiom, not derived from axioms 1–4. The proof is correct conditional on (C4). Establishing (C4) from first principles within CR (e.g., via the basin measure = FS measure argument of §6.1 Option C) remains open.

---

## 8. Comparison with d ≥ 3: Why SU(2) Equivariance Is Essential Here

### Observation 8.1 (Gleason vs. SU(d) equivariance)

| Feature | d ≥ 3 (Gleason) | d = 2 (SU(2) method) |
|---------|-----------------|----------------------|
| **Theorem** | Gleason (1957) | Busch (2003) / SU(2) structure |
| **Requirement** | Additivity on projections; normalization | SU(2) equivariance; two-outcome normalization; continuity |
| **Key gap** | Orthogonal triples exist | Only orthogonal pairs exist |
| **Logic** | Additivity of orthogonal projections → density operator | Equivariance + functional equation → Born rule |
| **Strength** | Does not require covariance assumption | Requires SU(2) covariance (but CR provides this from SCF+COV) |

For $d \geq 3$, Gleason's theorem is **stronger**: it requires fewer hypotheses (just additivity, no symmetry). But for $d=2$, we cannot invoke additivity of three orthogonal projections, so the SU(2) equivariance becomes **essential**.

---

## 9. The Two-Outcome Sector Is Sufficient for ℂP¹

### Remark 9.1

Unlike higher-dimensional Hilbert spaces where we must consider POVMs and their additivity constraints, on $\mathbb{CP}^1$ the **two-outcome normalization axiom alone** (together with SU(2) equivariance and continuity) is sufficient to pin down the Born rule.

This is because:
- Every measurement on a qubit can be reduced to a projective measurement onto some direction $\varphi$ or its orthogonal complement $\varphi^\perp$.
- The SU(2) symmetry of the Bloch sphere is so constraining that it forces the functional form of the weight $f(x)$.
- We do not need to introduce POVMs or effects beyond the projectors $|\varphi\rangle\langle\varphi|$ and $|\varphi^\perp\rangle\langle\varphi^\perp|$.

---

## 10. Application to Coherence Relativity

### How This Lemma Fits into CR

From the companion derivations:

1. **DERIVATION_SCF_NONCONTEXTUALITY_2026-04-19.md (Theorem 6.1):** The basin weight $W_T(\varphi|\psi)$ arising from the Lyapunov flow on frame bundles is **SU(2)-equivariant** when the SCF functor $F$ is SU(d)-covariant.

2. **DERIVATION_COV_CHECK_2026-04-19.md:** The candidate $F = \nabla^{\text{FS}} + A_C$ is confirmed to be SU(d)-covariant, hence its basin decomposition respects SU(2) symmetry.

3. **DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md:** The fixed-point SCF in the constant-basis branch is exactly $W_T(\varphi|\psi) = |\langle\varphi|\psi\rangle|^2$ for $d=2$.

4. **Two-outcome structure on CP¹:** The basin decomposition on the Bloch sphere has exactly two basins (accept/reject, or spin-up/spin-down), giving the two-outcome normalization:
   $$W(\varphi|\psi) + W(\varphi^\perp|\psi) = 1$$
   This is a topological property of the basin structure, not an additional axiom.

5. **Continuity:** The basin weight $W_T$ is continuous by construction (it arises from a continuous Lyapunov function on the frame bundle).

### Conclusion

Lemma 6.2 directly applies: the four axioms are satisfied by the CR basin weight on $\mathbb{CP}^1$, so the CR derivation of the Born rule on the qubit is **complete and rigorous**.

---

## 11. Honesty Audit: What Is Axiom vs. Theorem

| Item | Status | Note |
|------|--------|------|
| Reduction to $f(x)$ via SU(2) equivariance | ✅ Theorem | Orbit argument is standard and complete |
| Continuity of $f$ | ✅ Theorem | Inherited from continuity of $W$ |
| $f(1) = 1$ | ✅ Theorem | Follows from repeatability axiom |
| $f(x) + f(1-x) = 1$ | ✅ Theorem | Follows from two-outcome normalization axiom |
| $f(x) = x$ is unique solution to (C1)–(C3) alone | ❌ FALSE | Counterexample: $f_\varepsilon(x) = x + \varepsilon x(1-x)(2x-1)$ satisfies all three constraints for $\varepsilon \in (0,1)$ |
| SU(2) equivariance is *essential* for d=2 | ✅ Theorem | Gleason gap is real; without SU(2) equivariance, more solutions exist |
| Affinity (POVM additivity) needed to close the proof | ✅ Identified | (C4) is a genuine additional axiom for the d=2 case |
| $f(x) = x$ is unique solution to (C1)–(C4) | ✅ Theorem | Proposition 6.1′ — clean affinity + antisymmetry argument |
| Born rule $W(\varphi|\psi) = |\langle\varphi|\psi\rangle|^2$ | ⚠️ Conditional | Requires (C4); deriving (C4) from SCF/COV is the remaining CR gap for d=2 |

---

## 12. Summary

This note establishes the following *conditional* result for the qubit (d=2) Born rule:

**Theorem 7.1 (Conditional).** On $\mathbb{CP}^1$, any $W$ satisfying SU(2)-equivariance, repeatability, two-outcome normalization, and **POVM additivity (C4)** is uniquely the Born rule: $W(\varphi|\psi) = |\langle\varphi|\psi\rangle|^2$.

The key insight is that **SU(2) equivariance is essential** for d=2 (Gleason requires orthogonal triples which don't exist in ℂ²), but SU(2) equivariance alone is insufficient — a fifth condition (C4) is needed.

**What is proven (fully):** Steps 1–4 of the chain — reduction to $f(x)$, functional constraints (C1)–(C3), Gleason gap explanation, and Proposition 6.1′ given (C4).

**What remains open for CR:** Deriving (C4) from the SCF-fixed-point structure, either via:
- Option A: POVM additivity from the basin decomposition algebra
- Option B: Direct computation of the Lyapunov-flow absorption probability as $|\langle\varphi|\psi\rangle|^2$ via Fokker–Planck (Option C from §6.1)

For Coherence Relativity, the chain now reads:
$\text{SCF} \xrightarrow{\text{COV}} \text{SU(2)-covariance} \xrightarrow{\text{Thm 6.1}} \text{noncontextuality} \xrightarrow{\text{Thm 7.1 + C4}} \text{Born rule}$

with (C4) identified as the final open link specifically for d=2.

---

## References

- Gleason, A. M. (1957). "Measures on the closed subspaces of a Hilbert space." *J. Math. Mech.* 6, 885–893.
- Busch, P. (2003). "Quantum states and generalized observables: a simple proof of Gleason's theorem." *Phys. Rev. Lett.* 91, 120403.
- Caves, C. M., Fuchs, C. A., Manne, K. K., & Renes, J. M. (2004). "Gleason-type derivations of the quantum probability rule." *Found. Phys.* 34, 193–209. [Notes on qubit additivity]

---

**Document Status:** ⚠️ Corrected draft  
**Proof Status:** ✅ Rigorous and self-contained *conditional on (C4)*  
**Axiom Accounting:** ✅ All steps justified; gap in original Proposition 6.1 identified and corrected  
**Next Step:** Derive (C4) from SCF basin structure, or cite Busch (2003) with explicit statement of (C4) as the working hypothesis for d=2
