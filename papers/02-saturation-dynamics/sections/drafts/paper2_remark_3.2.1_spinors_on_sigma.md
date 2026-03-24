## Remark 3.2.1 — Spin Structure and Spinors on $\Sigma$
**Placement**: Insert after §3.2.8 (Physical Implications), before §3.2.9 (Relationship to §3.1 and §3.3)
**Date added**: 2026-03-23

---

**Remark 3.2.1 (Spin structure and spinors on $\Sigma$).** The Hopf fibration $S^1 \hookrightarrow S^3 \to S^2$ established in §3.2.2 is not merely a topological curiosity — it is the *spin structure* on $S^2$. More precisely, $S^3 \cong \mathrm{SU}(2)$ is the double cover of $\mathrm{SO}(3)$, and sections of the Hopf bundle over $S^2$ are spin-$\tfrac{1}{2}$ objects in the representation-theoretic sense, not vectors.

For the coherence-frame metric on $\Sigma = S^2 \cong \mathbb{CP}^1$, this distinction is harmless at the level of the current paper: the Fubini-Study metric $G_{ab}$, the cross-term $T_{M\Sigma}$, and the Kähler structure $J = \Omega \cdot G^{-1}$ are all rank-$(p,q)$ tensors on $\Sigma$, and the equations of motion (§2.2, §4) are formulated entirely in the tensor language of a Riemannian manifold. No inconsistency arises.

However, the identification $\Sigma = \mathbb{CP}^1$ carries a spin structure that becomes relevant in two downstream contexts:

1. **Fermionic KK modes.** The Kaluza-Klein spectrum on $S^3$ includes fermion zero-modes that are spinors on the fiber, not scalars or vectors. The $N_F$ counting entering the Casimir analysis (§5.3) implicitly assumes these are Weyl spinors with antiperiodic boundary conditions on the $S^1$ fiber. A fully rigorous treatment would verify this assignment from the Dirac operator on $S^3$ with the Hopf spin structure — ensuring that the mode counting is spinor-correct rather than tensor-correct. This is noted as a precision caveat; the qualitative result ($f > 0$ for SM content) is not expected to change.

2. **The state $|\psi\rangle$ as a section of the tautological bundle.** The quantum state $|\psi\rangle$, viewed as a section of the tautological line bundle $\mathcal{O}(-1) \to \mathbb{CP}^1$, is a spinor under the $\mathrm{SU}(2)$ action — not a vector. The "square root" of the canonical bundle of $\mathbb{CP}^1$ is the spinor bundle $S$, and $|\psi\rangle \in \Gamma(S)$. What looks like a vector field on $\Sigma$ (e.g., $\partial_a |\psi\rangle$ in the FS metric computation of §2.1) is, more precisely, a section of $T\Sigma \otimes \mathcal{O}(-1) \cong S^+ \otimes S^-$ — a bispinor. For the current level of computation this makes no difference: the Fubini-Study metric is gauge-invariant under $U(1)$ phase rotations precisely because it contracts the tautological bundle indices. But in a more refined treatment that tracks the spin structure explicitly, the natural language on $\Sigma = \mathbb{CP}^1$ is spinor bundles rather than tensor bundles.

**Summary**: The tensor formalism used throughout this paper is correct and complete for all calculations presented. Spinors on $\Sigma$ are the appropriate refinement when (a) computing the Dirac spectrum on the Hopf fiber for fermionic KK mode counting, or (b) giving a fully rigorous geometric account of the quantum state as a section of the tautological bundle. The distinction does not affect any numerical result in this paper but is relevant for the fermion content analysis of §5.3 and for the full KK spectrum analysis deferred to the companion paper.
