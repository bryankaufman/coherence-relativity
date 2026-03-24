## Footnote for §5.3.2 — Spinor vs. Tensor Mode Counting on the Hopf Fiber
**Placement**: Footnote attached to the sentence defining $N_F$ in §5.3.2
**Anchor text**: "Massless Weyl fermionic d.o.f. (counted with antiperiodic BC in Casimir formula)"
**Date added**: 2026-03-23

---

**Footnote (spinor mode counting).**\footnote{
The $N_F = 96$ count (SM with Dirac neutrinos) used in Eq.~(5.3.1) treats each Weyl fermion as contributing one degree of freedom with antiperiodic boundary conditions on the Hopf fiber $S^1$. This is the standard Casimir counting for a scalar field in the spin-$\tfrac{1}{2}$ representation. A more careful treatment would derive $N_F$ from the spectrum of the Dirac operator $\slashed{D}$ on $S^3$ with the spin structure inherited from the Hopf fibration $S^1 \hookrightarrow S^3 \to S^2$.

The relevant point is that $S^3 \cong \mathrm{SU}(2)$ carries a natural left-invariant spin structure, and the Dirac spectrum on $S^3$ is known exactly: the eigenvalues of $\slashed{D}$ are $\pm(n + \tfrac{3}{2})$ for $n = 0, 1, 2, \ldots$, with multiplicity $(n+1)(n+2)$ for each sign (see, e.g., Camporesi \& Higuchi 1996). The zero-mode ($n = 0$) sector has multiplicity $2$, consistent with two Weyl spinors. The Kaluza-Klein tower then populates the higher modes.

For the Casimir calculation in this section, only the lightest mode (the approximate zero-mode at the compactification scale $\sim 1/r_f$) contributes significantly at long wavelengths. The spinor-correct counting modifies $N_F$ by a representation-theoretic factor relative to a naive scalar count. For Weyl fermions on $S^1$, the relevant representation is the fundamental of $\mathrm{SU}(2)$ restricted to $\mathrm{U}(1)$, which gives the standard antiperiodic boundary condition. The $N_F = 96$ count is therefore a tensor-level approximation that agrees with the spinor-level count for the zero-mode sector, up to factors that enter at the level of the KK tower and are suppressed by $e^{-r_f/r}$ at scales $r \gg r_f$.

A fully rigorous spinor-level derivation of $N_F$ from the Hopf Dirac spectrum is deferred to the companion paper, where the full KK spectrum is analyzed. The qualitative conclusion ($f > 0$ for SM content, and the sign condition being satisfied) is robust against this correction.

\textit{Reference}: Camporesi, R., \& Higuchi, A. (1996). On the eigenfunctions of the Dirac operator on spheres and real hyperbolic spaces. \textit{Journal of Geometry and Physics}, 20(1), 1–18.
}

---

## How to integrate into §5.3.2

Locate this sentence in §5.3.2:

> "Define $f := \frac{7N_F}{8} - N_B.$"

Add a footnote marker after "$N_F$":

> "Define $f := \frac{7N_F}{8} - N_B.$\footnotemark"

And place the footnote text (above) at the bottom of that page/section.

Alternatively, the footnote can be attached to the first mention of "$N_F = 96$" in the branch screening table (§5.3.3), with the text shortened to:

> "$^*$The $N_F = 96$ count treats each Weyl fermion as one d.o.f. with antiperiodic BCs on $S^1$. A spinor-level derivation from the Dirac operator on $S^3$ with the Hopf spin structure gives the same zero-mode count but modifies the KK tower. See Remark 3.2.1 and companion paper §[KK spectrum]."
