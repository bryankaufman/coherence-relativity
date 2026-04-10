# §3.3 What Derived Compactification Constrains

**Status:** v2 DRAFT — 2026-04-10. Klein removal applied throughout; geometric Λ from §5.3 v2 incorporated.
**Supersedes:** `paper2_section_3.3_constraints_DRAFT.md`
**Changes from v1:** (1) Compactification language updated to interval geometry. (2) Klein S¹ added to ruled-out topologies. (3) KK mode expansion replaced with volcano potential spectrum. (4) Cosmological constant section updated: geometric Λ primary, Casimir correction secondary. (5) Moduli section updated: shape frozen by $k^2 = 2$, not just "dynamically determined."

---

## 3.3.1 Overview: From Topology to Physics

Section 3.2 established that compactification is *derived*, not assumed. The extra dimension is the decoherence-depth coordinate $r$, which is geometrically compact: the warp factor $A(r) = \cos(\sqrt{2}\,r)$ (Proposition 4.2, §7) vanishes at $r_{\max} = \pi/(2\sqrt{2})$, terminating the geometry. The parameter $\mu = \sqrt{2}$ is fixed by the Fubini-Study Laplacian eigenvalue $k^2 = 2$ — it is not a free parameter. The compact topology is a consequence, not an input.

This represents a qualitative shift in the landscape of extra-dimensional physics. In the historical framework, compactness is postulated and one is then free to choose any compact topology (Calabi-Yau, orbifold, Klein circle, etc.), with moduli to vary. In Coherence Relativity, the topology is *determined* by first principles, and Klein's 1926 compactification mechanism is unnecessary.

**The question now is: What physics does this determination constrain?**

This section answers that question by tracing the cascade of constraints that flow from fixing the topology. We show that:

1. The landscape of possible topologies is reduced from $\sim 10^{500}$ to a single geometric outcome: the bounded interval $r \in [0, r_{\max}]$ with one scale parameter.
2. The shape modulus is zero: $r_{\max}$ is topologically frozen by $k^2 = 2$.
3. The KK mode structure is fixed by the volcano potential on the interval.
4. The cosmological constant has a geometric primary source and a Casimir quantum correction.
5. The scale $s$ (mapping $r$ to meters) is determined by the Friedmann balance at each epoch.

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

The single free parameter is the physical scale factor $s$ (mapping dimensionless $r$ to meters), which is determined dynamically by the Friedmann balance at each epoch (§5.3.2.2).

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

### 3.3.3.2 Scale Modulus: Cosmological Attractor

The physical scale factor $s$ is not a free parameter. It is determined by the Friedmann balance:

$$H^2(t) = \frac{8\pi G_4}{3}\bigl[\rho_{\mathrm{geom}}(s) + \rho_{\mathrm{Cas}}(s)\bigr]$$
(Eq. 3.3.4)

At each cosmic epoch, $H(t)$ determines $s(t)$. The scale grows with cosmic expansion at the Hubble rate ($\dot{s}/s \sim H$). It cannot decrease (non-traversability, Proposition 4.2). The scale is a cosmological attractor — not a potential minimum in the traditional sense, but a dynamically determined value at each epoch.

This resolves OP-5 (radius stabilization). No Goldberger-Wise potential or KKLT flux is required.

### 3.3.3.3 Comparison to String Theory Moduli

| Aspect | String Theory | Coherence Relativity |
|--------|--------------|---------------------|
| **Topology** | Chosen from $\sim 10^{500}$ Calabi-Yau types | Unique: interval $[0, r_{\max}]$ with $A = \cos(\sqrt{2}\,r)$ |
| **Shape moduli** | $h^{2,1} \sim 100$–$1000$ free parameters | **0** (topologically frozen by $k^2 = 2$) |
| **Kähler moduli** | $h^{1,1} \sim 100$–$300$ free parameters | **0** (shape frozen; scale from Friedmann) |
| **Moduli stabilization** | Requires ad hoc potentials (KKLT, GW) | Not applicable to shape; scale from cosmology |
| **Klein circle** | Not present (different mechanism) | Removed — unnecessary |
| **Landscape size** | $\sim 10^{500}$ | **1** |

---

## 3.3.4 Constrained Matter Content via KK Modes

### 3.3.4.1 Mode Structure on the Derived Interval

The topology of the compact space determines the allowed Kaluza-Klein mode expansion. For the derived interval $[0, r_{\max}]$ with Dirichlet-type boundary conditions at both ends (brane at $r=0$, pinch-off at $r = r_{\max}$), the mode expansion is:

$$\Phi(x^\mu, r) = \sum_n \phi_n(x^\mu)\,\psi_n(r)$$
(Eq. 3.3.5)

where $\psi_n(r)$ are eigenfunctions of the Schrödinger-like equation

$$-\psi_n''(r) + V(r)\,\psi_n(r) = m_n^2\,\psi_n(r)$$
(Eq. 3.3.6)

with the **volcano potential**

$$V(r) = -3 + \tfrac{3}{2}\tan^2(\sqrt{2}\,r)$$
(Eq. 3.3.7)

This potential arises from the warp factor $A(r) = \cos(\sqrt{2}\,r)$ (standard warped KK reduction). It has a minimum of $V(0) = -3$ at the brane and diverges as $r \to r_{\max}$.

### 3.3.4.2 KK Spectrum

The KK graviton spectrum from (3.3.6)–(3.3.7) is:

| Mode | $m^2$ (dimless) | $m$ (dimless) | Identity | $\lambda$ at $s \sim 50\,\mu\mathrm{m}$ |
|------|-----------------|---------------|----------|------------------------------------------|
| 0 | 0 | 0 | Graviton zero mode | $\infty$ (massless, 4D gravity) |
| ~0 | 0.01 | 0.10 | Radion (OP-5, resolved) | ~2600 μm |
| 1 | 20.1 | 4.48 | First KK graviton | **13.3 μm** |
| 2 | 56.2 | 7.50 | Second KK graviton | 7.9 μm |
| 3 | 108.4 | 10.41 | Third KK graviton | 5.7 μm |
| 4 | 176.7 | 13.29 | Fourth KK graviton | 4.5 μm |

The graviton zero mode ($m=0$) is normalizable and localized near the brane (half-weight at $r/r_{\max} \approx 22.6\%$). The near-zero mode is the radion — the breathing mode of $r_{\max}$ — identified by a 71% wavefunction overlap. It is OP-5's stabilized radion, not a KK graviton.

The first genuine KK graviton has $\lambda_1 \approx 13.3\,\mu\mathrm{m}$, safely below the 44 μm ISL bound (Lee et al. 2020). ✓

### 3.3.4.3 Contrast with Klein S¹

**Klein $S^1$** gives an exactly linear KK spectrum: $m_n = n/R$, hence $m_n/m_1 = 1, 2, 3, 4, \ldots$

**Derived compactification** gives a non-linear spectrum from the volcano potential: $m_n/m_1 \approx 1, 1.67, 2.32, 2.97, \ldots$

$$\boxed{\text{Testable prediction: non-linear KK mode spacing distinguishes derived compactification from Klein.}}$$
(Eq. 3.3.8)

If KK graviton resonances are ever detected, the spacing pattern is a clean, model-independent discriminator.

### 3.3.4.4 Charge Quantization (Klein-Free)

Previously: KK charge quantization came from quantized momentum $p_5 = n\hbar/R$ on the Klein circle.

Now: Charge quantization comes from the Berry phase holonomy on $\Sigma = \mathbb{CP}^1$. The U(1) Berry connection has first Chern number $c_1 = 1$ — a topological invariant. Closed loops in $\Sigma$ pick up holonomy phases that are integer multiples of $2\pi$, giving discrete charge without any compact spatial dimension.

This is cleaner than the Klein mechanism: topological rather than dimensional, independent of the scale factor $s$, and surviving the removal of Klein's circle.

---

## 3.3.5 Constrained Cosmological Constant

### 3.3.5.1 Geometric Λ (Primary Source)

The warp factor $A(r) = \cos(\sqrt{2}\,r)$ has intrinsic curvature energy that, when integrated over the interval with $A^4$ weighting, produces a **positive** effective 4D cosmological constant classically:

$$\rho_{\mathrm{geom,4D}} = \frac{\int_0^{r_{\max}} A^4(r)\,\rho_{\mathrm{geom}}(r)\,\mathrm{d}r}{\int_0^{r_{\max}} A^3(r)\,\mathrm{d}r} = +3.534 \times \frac{M_5^3\,k^2}{s}$$
(Eq. 3.3.9)

with the GHY boundary term vanishing at $r_{\max}$ (since $A(r_{\max}) = 0$). This is positive for all field contents — it does not depend on $N_B$ or $N_F$. The sign of $\Lambda_{\mathrm{eff}}$ is geometrically guaranteed.

### 3.3.5.2 Casimir Quantum Correction

The quantum Casimir energy on the interval $[0, L]$ (with $L = r_{\max} \times s$, Dirichlet BC) provides a correction:

$$\rho_{\mathrm{Cas}}(L) = \frac{\pi^2 \hbar c}{1440\,L^4}\,f, \quad f := \frac{7N_F}{8} - N_B$$
(Eq. 3.3.10)

This is the corrected formula for the interval with Dirichlet boundary conditions (a factor of 2 smaller than the Klein circle formula with periodic BC, which used $720$ in the denominator).

The total effective 4D cosmological constant:

$$\Lambda_{\mathrm{eff}} = \frac{8\pi G_4}{c^4}\bigl[\rho_{\mathrm{geom,4D}}(s) + \rho_{\mathrm{Cas}}(L)\bigr]$$
(Eq. 3.3.11)

**Key consequence:** The sign of $\Lambda_{\mathrm{eff}}$ is determined by the geometric term (always positive). The Casimir term can be positive or negative depending on the field content; it modifies the magnitude, not the sign.

### 3.3.5.3 The Scale

The physical scale factor $s$ is not a free parameter. It is set by the Friedmann balance (Eq. 3.3.4). The scale of the Casimir correction (where $\rho_{\mathrm{Cas}} \sim \rho_\Lambda$) is:

$$L_{\mathrm{Cas}}^* = \left(\frac{\pi^2 \hbar c\,f}{1440\,\rho_\Lambda}\right)^{1/4} \approx 46\text{–}56\,\mu\mathrm{m} \quad \text{(SM sector, self-consistent)}$$
(Eq. 3.3.12)

### 3.3.5.4 Implications for Fine-Tuning

The old question "For what fiber radius $R$ does $\Lambda_{\mathrm{eff}}(R) = \Lambda_{\mathrm{obs}}$?" is replaced by the question "What is the Friedmann balance at the current epoch?" The cosmological constant is not a fine-tuned parameter; it is the energy density of the geometrically curved extra dimension, which grows (very slowly, at the Hubble rate) with cosmic expansion. The observed smallness of $\Lambda_{\mathrm{obs}}$ reflects the fact that the universe has been decohering for 13.8 Gyr, producing a large scale factor $s$.

$$\boxed{\Lambda_{\mathrm{eff}} \text{ has geometric primary source } + \text{ Casimir correction. Scale from Friedmann.}}$$
(Eq. 3.3.13)

---

## 3.3.6 What Is NOT Constrained by Topology

The following remain open, as in v1, with updated status:

**(a) The physical scale factor $s$:** Not a topological quantity. Determined by Friedmann balance — now explicitly resolved as a cosmological attractor (not a potential minimum). **Status: RESOLVED by cosmological attractor.**

**(b) The field content on the interval:** Determined by Paper 3 phase transition (Axiom B) and symmetry. **Status: CONTINGENT on Paper 3.** (Note: sign of $\Lambda$ is no longer contingent on field content.)

**(c) Whether $c_1 = 1$ is the only realized compactification:** The minimality argument for $c_1 = 1$ is unchanged; higher-$c_1$ bundles in the Hopf fiber structure remain possible at higher energies. **Status: OPEN.**

---

## 3.3.7 Comparison Table: Assumed vs. Derived Compactification (v2)

| Aspect | String Landscape | Klein (1926) | Coherence Relativity |
|--------|-----------------|--------------|---------------------|
| **Topological origin** | Postulated | Postulated ($S^1$) | Derived from A(r) = cos(√2 r) |
| **Topological choice** | $\sim 10^{500}$ Calabi-Yau | One circle with free $R$ | Unique: bounded interval |
| **Shape moduli** | $h^{2,1} \sim 100$–$1000$ | 0 (circle) | **0 (topologically frozen)** |
| **Scale moduli** | $h^{1,1} \sim 100$–$300$ | Free $R$ — stabilization required | Cosmological attractor |
| **Charge quantization** | From flux quantization | From $p_5 = n\hbar/R$ | From Berry phase $c_1 = 1$ on $\mathbb{CP}^1$ |
| **KK spectrum** | Hodge structure | Linear $m_n = n/R$ | Non-linear (volcano potential) |
| **Cosmological constant** | Landscape; anthropic | Casimir on $S^1$ | Geometric primary + Casimir correction |
| **Dimension count** | 10D (6 compact) | 5D + Klein $S^1 = 6$D? | **5D (4 + r)** |
| **Landscape size** | $\sim 10^{500}$ | 1 (but $R$ free) | **1** (scale from Friedmann) |
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
- 0 scale moduli (cosmological attractor)
- $\mathcal{O}(10)$ parameters from field content and couplings (Paper 3)
- **Total: $\mathcal{O}(10)$ parameters**

$$\boxed{\text{Degrees of freedom: String theory } \gtrsim 10^{500};\quad \text{CR } = \mathcal{O}(10).}$$
(Eq. 3.3.14)

---

## 3.3.9 Implications and Open Questions

### What This Framework Achieves

1. **Landscape elimination.** Not a landscape reduction — a landscape elimination. The topology is derived, not selected from a menu. Klein's S¹ is ruled out alongside Calabi-Yau manifolds.

2. **Shape rigidity.** $r_{\max}$ is topologically frozen. No stabilization potential needed for the shape.

3. **Scale resolution.** The physical scale is a cosmological attractor — no Goldberger-Wise potential needed.

4. **Predictive power.** Non-linear KK mode spacing ($1, 1.67, 2.32, 2.97$) is a sharp, falsifiable prediction distinguishing CR from every prior compactification scheme.

5. **Charge quantization.** Topological (Berry phase) rather than dimensional (Klein momentum).

### What Remains Open

1. **Post-transition field content** (Paper 3): affects the Casimir correction magnitude
2. **Higher-$c_1$ compactifications** in the Hopf fiber structure at higher energies
3. **Quantitative Friedmann balance**: explicit $s_{\mathrm{now}}$ from $H_0$ requires the 5D-to-4D reduction factor

---

## 3.3.10 Summary and Transition to §4

**Section 3.3 Main Points (v2):**

1. **Derived compactification is unique:** bounded interval $[0, r_{\max}]$ with $A(r) = \cos(\sqrt{2}\,r)$. Klein's $S^1$ and all other topologies are ruled out.

2. **Shape is topologically frozen:** $r_{\max} = \pi/(2\sqrt{2})$ fixed by the Fubini-Study eigenvalue $k^2 = 2$. Zero shape moduli.

3. **Scale is a cosmological attractor:** determined by the Friedmann balance at each epoch. No stabilization potential needed.

4. **KK spectrum is non-linear:** from the volcano potential, giving $m_n/m_1 \approx 1, 1.67, 2.32, 2.97$ — a testable prediction distinguishing CR from Klein.

5. **$\Lambda_{\mathrm{eff}}$ has a geometric primary source:** $\rho_{\mathrm{geom,4D}} = +3.534 \times M_5^3 k^2/s > 0$ classically. Casimir is a correction.

6. **Charge quantization is topological:** Berry phase $c_1 = 1$ on $\mathbb{CP}^1$, not Klein momentum.

---

## 3.3.11 Paper 3 Interface Hooks (updated)

1. **P3-H1: Phase-transition gate** — Provide transition scale/redshift separating 5D-coupled regime from effective 4D regime. Unchanged from v1.

2. **P3-H2: Post-transition field-content map** — Provide $(N_B, N_F)$ counts. This determines the Casimir correction sign and magnitude. Note: the sign of $\Lambda$ is no longer contingent on this outcome (geometry guarantees $\Lambda > 0$). The field content affects only the correction term.

3. **P3-H3: Bundle-selection statement** — Clarify whether only $c_1 = 1$ Hopf fiber is dynamically selected. **Status: INTERFACE-CONTRACT ONLY.**

4. **P3-H4: Effective-source projection rule** — Projection map from $M \times \Sigma$ dynamics to 4D effective source terms. **Status: INTERFACE-CONTRACT ONLY.**

---

## References and Notes for §3.3 (v2)

- §3.2: Derived compactification from coherence axioms; Proposition 4.2 (A(r) = cos(√2 r))
- §5.3 v2: Geometric Λ calculation; OP-5 resolution; Casimir correction on interval
- §7 v2 (EOM): Formal derivation of k² = 2 from Fubini-Study eigenvalue (Proposition 4.2)
- Kaluza, T. (1921). "On the unification problem in physics." *Sitzungsber. Preuss. Akad. Wiss. Berlin*, 966–972. [Original pure-Kaluza single-extra-dimension picture]
- Klein, O. (1926). "Quantentheorie und fünfdimensionale Relativitätstheorie." *Z. Phys.* **37**, 895–906. [Klein compactification — ruled out here]
- Lee, J. G. et al. (2020). "New Test of the Gravitational $1/r^2$ Law at Separations down to $52\,\mu\mathrm{m}$." *Phys. Rev. Lett.* **124**, 101101. [ISL bound 44 μm]
- Paper 3 (in preparation). [Phase transition, field content, Post-transition sector]
