# §2.5 Left-Right Generator Decomposition of M×Σ Dynamics
**Status**: DRAFT — first explicit derivation 2026-03-23
**Depends on**: §2.1 (T_MΣ^left, dephasing model), §2.4 (Born rule via purification)
**Cite**: Settimo et al. (2026), PRX Quantum 7, 010340, DOI: 10.1103/6dt2-sq44
**Placement**: New section §2.5 between Mixed-State Born Rule (§2.4) and Markov Transition (§2.6)

---

## §2.5.1 Motivation: The Schrödinger Picture Is Half the Story

The cross-term $T_{M\Sigma}$ derived in §2.1 arises from the Fubini-Study/Bures metric
on the space of density matrices $\rho(x,\xi)$, where $x \in M$ and $\xi \in \Sigma$.
The dynamical map $\Phi_t$ was implicitly treated in the Schrödinger picture: states evolve
as $\dot{\rho} = \mathcal{L}_t[\rho]$ via the left generator $\mathcal{L}_t$ (a Lindblad
superoperator). This gives one face of the $M\times\Sigma$ metric — the state-side (S) face.

Settimo et al. (2026) show that every dynamical map simultaneously satisfies a *right*
master equation:
\[
\dot{\Phi}_t = \Phi_t \circ \mathcal{R}_t, \qquad
\mathcal{R}_t = \Phi_t^{-1} \circ \mathcal{L}_t \circ \Phi_t. \tag{2.5.1}
\]
The right generator $\mathcal{R}_t$ governs observable evolution in the Heisenberg picture
and equals $\mathcal{L}_t$ if and only if the dynamics is commutative (Markovian semigroup).
For non-Markovian dynamics, $\mathcal{L}_t \neq \mathcal{R}_t$, and there is a distinct
*effect-side* (H) face of the metric.

**Consequence for Paper 2**: $T_{M\Sigma}$ as derived in §2.1 is $T_{M\Sigma}^{(\mathrm{S})}$
— the Schrödinger-picture cross-term. There exists a dual $T_{M\Sigma}^{(\mathrm{H})}$
from the Heisenberg picture. Their difference encodes the degree of non-Markovianity
in the mixed $M$-$\Sigma$ sector.

---

## §2.5.2 Explicit Derivation: Single-Qubit Dephasing Model

We derive $T_{M\Sigma}^{(\mathrm{H})}$ explicitly in the dephasing model of §2.1.7.

### Setup

The density matrix and its M-dependence:
\[
\rho(x,\xi) = \begin{pmatrix} p(\xi) & c(\xi)\,e^{-\Gamma(x)} \\
c^*(\xi)\,e^{-\Gamma(x)} & 1-p(\xi) \end{pmatrix}, \tag{2.5.2}
\]
with Bloch vector $\vec{r} = (r_x, r_y, r_z) = (2\mathrm{Re}(c)e^{-\Gamma},\,
2\mathrm{Im}(c)e^{-\Gamma},\, 2p-1)$.

The left (Schrödinger) generator for pure dephasing:
\[
\mathcal{L}_t[\rho] = \gamma(x)\bigl(\sigma_z\rho\sigma_z - \rho\bigr), \tag{2.5.3}
\]
where $\gamma(x) \geq 0$ is the local dephasing rate. In terms of Bloch components:
\[
\dot{r}_x = -2\gamma\, r_x, \quad \dot{r}_y = -2\gamma\, r_y, \quad \dot{r}_z = 0.
\tag{2.5.4}
\]

### Dynamical Map

The exact solution is:
\[
\Phi_t: \vec{r}(0) \mapsto \vec{r}(t) = \bigl(r_x(0)e^{-2\Gamma_t},\,
r_y(0)e^{-2\Gamma_t},\, r_z(0)\bigr), \tag{2.5.5}
\]
where $\Gamma_t = \int_0^t \gamma(x(s))\,ds$. The map is:
\[
\Phi_t = \mathrm{diag}(e^{-2\Gamma_t},\, e^{-2\Gamma_t},\, 1) \quad \text{(on Bloch vector).}
\tag{2.5.6}
\]

### Right Generator

On invertible intervals (finite $\Gamma_t$):
\[
\mathcal{R}_t = \Phi_t^{-1} \circ \mathcal{L}_t \circ \Phi_t. \tag{2.5.7}
\]

Computing $\mathcal{L}_t \circ \Phi_t$: apply $\Phi_t$ first, then $\mathcal{L}_t$:
\[
(\mathcal{L}_t \circ \Phi_t)[\vec{r}] = \mathcal{L}_t\bigl[\vec{r}'(t)\bigr]
= -2\gamma\,(r_x'(t),\, r_y'(t),\, 0) = -2\gamma\,(r_x e^{-2\Gamma_t},\,
r_y e^{-2\Gamma_t},\, 0). \tag{2.5.8}
\]

Applying $\Phi_t^{-1} = \mathrm{diag}(e^{+2\Gamma_t},\, e^{+2\Gamma_t},\, 1)$:
\[
\mathcal{R}_t[\vec{r}] = -2\gamma\,(r_x,\, r_y,\, 0) = \mathcal{L}_t[\vec{r}].
\tag{2.5.9}
\]

**Result**: For pure dephasing, $\mathcal{R}_t = \mathcal{L}_t$ exactly. The dephasing
channel is commutative — it belongs to the Markovian semigroup class — so the left and
right generators coincide.

---

## §2.5.3 Mismatch Tensor $\Delta G_{ij}$ in the Dephasing Model

Since $\mathcal{R}_t = \mathcal{L}_t$ for pure dephasing:
\[
T_{M\Sigma}^{(\mathrm{H})} = T_{M\Sigma}^{(\mathrm{S})} \quad \Rightarrow \quad
\Delta G_{ij} := G_{ij}^{(\mathrm{S})} - G_{ij}^{(\mathrm{H})} = 0. \tag{2.5.10}
\]

This is consistent: dephasing is Markovian, so both pictures agree. The full
$M\times\Sigma$ metric has only one face for this model, as derived in §2.1.

**Physical interpretation**: The equality $\mathcal{R}_t = \mathcal{L}_t$ is the precise
condition for the Markov transition criterion (§2.6). When it holds, the system evolves
identically whether described by state evolution (Schrödinger) or observable evolution
(Heisenberg). There is no measurement problem in the dephasing sector — preparation-side
and measurement-side statistics agree.

---

## §2.5.4 When $\Delta G_{ij} \neq 0$: The Non-Markovian Case

The dephasing model saturates the Markovian limit. To see $T_{M\Sigma}^{(\mathrm{H})}
\neq T_{M\Sigma}^{(\mathrm{S})}$, consider a non-Markovian extension: two-level system
with amplitude damping plus dephasing, or any generator where off-diagonal relaxation
couples to $r_z$ (coherence-population coupling).

In the general case, the right generator is:
\[
\mathcal{R}_t = \Phi_t^{-1} \circ \mathcal{L}_t \circ \Phi_t \neq \mathcal{L}_t,
\tag{2.5.11}
\]
and the mismatch is:
\[
\Delta G_{ij} = G_{ij}^{(\mathrm{S})} - G_{ij}^{(\mathrm{H})} \propto
\|\mathcal{L}_t - \mathcal{R}_t\|_{\mathrm{op}}, \tag{2.5.12}
\]
with $\|\mathcal{L}_t - \mathcal{R}_t\|_{\mathrm{op}} \to 0$ as the dynamics approaches
commutativity (Markovian limit, $\lambda_M \to 0$, Phase III).

The operator norm $\|\mathcal{L}_t - \mathcal{R}_t\|_{\mathrm{op}}$ is a
directly measurable quantity: it corresponds to the difference in trace-distance
distinguishability (Schrödinger, $D_1$) and operator-norm distinguishability
(Heisenberg, $D_\infty$) established by Settimo et al. (2026).

---

## §2.5.5 Born Rule as Invariant of $|H_{M\Sigma}|$

The two-face structure of the metric is naturally unified by promoting $G_{ij}$ to a
complex Hermitian tensor:
\[
H_{ij} = G_{ij} + i\Omega_{ij} = G_{ij}(1 + iJ), \tag{2.5.13}
\]
where $J$ is the complex structure (Kähler operator) satisfying $\omega(X,Y) = g(JX,Y)$,
and $\Omega_{ij} = J \cdot G_{ij}$ is the Kähler form.

- $\mathrm{Re}(H_{ij}) = G_{ij}^{(\mathrm{S})}$: Schrödinger face (what §2.1 derived).
- $\mathrm{Im}(H_{ij}) = \Omega_{ij} = J \cdot G_{ij}$: Heisenberg face.
- $|H_{M\Sigma}|$: the modulus, invariant under both coherence-frame rotations and
  Schrödinger/Heisenberg picture changes simultaneously.

The Born rule from Paper 1 — $|\langle\psi|\phi\rangle|^2$ — is the invariant of $|H|$,
not just of $G$. It survives all allowed picture changes. This is the geometric reason
why the Born rule is the unique frame-invariant of the CR framework: it is the modulus
of the full complex metric, which cannot be changed by either coherence-frame
transformations (acting on $|H|$) or S/H picture rotations (acting on $\arg H$).

---

## §2.5.6 Pointer States from Generator Coincidence

The pointer-state criterion takes its sharpest form in this language:

**Theorem 2.5.1 (Pointer-Sector Criterion)**:
*A state $\rho$ lies in the pointer sector if and only if*
\[
\mathcal{L}_t[\rho] = \mathcal{R}_t[\rho] \quad \text{(as operators on the support of $\rho$).}
\tag{2.5.14}
\]

**Proof sketch**: $\mathcal{L}_t = \mathcal{R}_t$ on the support of $\rho$ iff
$\Phi_t\rho = \rho\Phi_t$ — i.e., $\rho$ commutes with the dynamical map. For a
Lindblad generator $\mathcal{L}_t[\rho] = -i[H,\rho] + \sum_k(L_k\rho L_k^\dagger
- \tfrac{1}{2}\{L_k^\dagger L_k, \rho\})$, commutativity with $\Phi_t$ is equivalent
to $[L_k, \rho] = 0$ for all $k$ (the pointer-state condition of Zurek 2003). $\square$

**Connection to $T_{M\Sigma}$**: When $\mathcal{L}_t = \mathcal{R}_t$ on the pointer
sector, $\Delta G_{ij} = 0$ on that sector, meaning both faces of the $M\times\Sigma$
metric agree. The pointer states are precisely those for which the complex metric $H_{ij}$
is real: $\mathrm{Im}(H_{ij})\big|_{\mathrm{pointer}} = 0$.

This gives a new geometric derivation of the pointer basis: it is the zero set of
$\mathrm{Im}(H_{M\Sigma})$, or equivalently, the locus where the Kähler structure $J$
vanishes on the $M$-$\Sigma$ cross-sector.

---

## §2.5.7 Two Entropic Ledgers

The two-face structure implies two distinct entropy production rates:

\[
\frac{dS^{(\mathrm{S})}}{dt} = -\mathrm{Tr}\bigl(\dot{\rho}\ln\rho\bigr) \geq 0
\quad \text{(Schrödinger ledger)}, \tag{2.5.15}
\]
\[
\frac{dS^{(\mathrm{H})}}{dt} \geq 0
\quad \text{(Heisenberg ledger, from effect-side divisibility)}, \tag{2.5.16}
\]
with $S^{(\mathrm{S})}$ and $S^{(\mathrm{H})}$ satisfying independent second-law
inequalities but potentially *diverging* when $\mathcal{L}_t \neq \mathcal{R}_t$.

The thermodynamic uncertainty relation (§2.3.6, from the currency framework) reads:
\[
\frac{dS}{d\lambda_M} \leq \frac{1}{2}\sqrt{F_Q^{MM}}, \tag{2.5.17}
\]
where $F_Q^{MM}$ is the quantum Fisher information in the $M$-direction. When both
ledgers are active, (2.5.17) bounds the *total* entropy production rate, not each
separately.

**Physical consequence**: In regimes where $S^{(\mathrm{S})}$ and $S^{(\mathrm{H})}$
diverge, the system cannot simultaneously satisfy preparation-side and measurement-side
entropy accounting with a single thermodynamic arrow. This is the microscopic origin
of the measurement problem (§2.6.4) and, at cosmic scales, of the $H_0$ tension
(Paper 3, §5).

---

## §2.5.8 Summary and Status

| Item | Result | Status |
|---|---|---|
| $\mathcal{R}_t$ for pure dephasing | $\mathcal{R}_t = \mathcal{L}_t$ exactly | ✅ Derived |
| $T_{M\Sigma}^{(\mathrm{H})}$ for pure dephasing | $= T_{M\Sigma}^{(\mathrm{S})}$ | ✅ Derived |
| $\Delta G_{ij}$ for dephasing model | $= 0$ (Markovian) | ✅ Derived |
| Complex metric $H = G + i\Omega$ | Structure identified | ✅ Conceptual |
| Born rule as $|H|$-invariant | Geometric reframing of Paper 1 result | ✅ No new derivation needed |
| Pointer states as $\mathrm{Im}(H) = 0$ | Theorem 2.5.1 (proof sketch) | ✅ Draft |
| Two entropic ledgers | Conceptual structure, bounds cited | ✅ Draft |
| $T_{M\Sigma}^{(\mathrm{H})}$ for non-Markovian models | Proportional to $\|\mathcal{L}_t - \mathcal{R}_t\|_{\mathrm{op}}$ | ⚠️ Not derived explicitly |
| $\|\mathcal{L}_t - \mathcal{R}_t\|_{\mathrm{op}}$ as function of $\lambda_M$ | Monotone suppression in Phase III conjectured | ⚠️ Not verified numerically |
| Full proof of Theorem 2.5.1 | Proof sketch only | ⚠️ Needs formalization |

**Section placement**: §2.5, after §2.4 (Mixed-State Born Rule) and before §2.6
(Markov Transition Criterion). The left-right decomposition motivates the Markov
criterion (§2.6) — the Markov transition is precisely where $\mathcal{L}_t = \mathcal{R}_t$.

**References**:
- Settimo, F. et al. (2026). Divisibility of dynamical maps: Schrödinger versus
  Heisenberg picture. *PRX Quantum* **7**, 010340. DOI: 10.1103/6dt2-sq44
- Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the
  classical. *Rev. Mod. Phys.* **75**, 715–775.
- Braunstein, S. L. & Caves, C. M. (1994). Statistical distance and the geometry
  of quantum states. *Phys. Rev. Lett.* **72**, 3439.
