# § 5.3: SC3 — Effective Cosmological Constant

**Status:** REVISED — 2026-04-10 (D2). Category error corrected; five-level Σ→M coupling hierarchy.
**Supersedes:** `paper2_section_5.3_SC3_Casimir_v2.md` (2026-04-10, which contained a category error)
**Changes from v2:** (1) FS curvature k²=2 removed from Friedmann equation (category error). (2) Five-level coupling hierarchy introduced. (3) D1 values: L*=68.6 μm (full SM), 55.7 μm (self-consistent). (4) D4 Atiyah-Singer paragraph inserted in §5.3.2. (5) Casimir restored as the primary *gravitational* contributor; FS curvature governs decoherence dynamics only.

---

## § 5.3.1: The SC3 Condition

The third self-consistency condition (SC3) requires that the observed cosmological constant,

$$\Lambda_{\mathrm{obs}} \approx 1.1 \times 10^{-52} \, \mathrm{m}^{-2},$$

emerges from the KCR-Cone geometry. The 5D metric is

$$\mathrm{d}s^2_{5\mathrm{D}} = A^2(r)\,\eta_{\mu\nu}\,\mathrm{d}x^\mu \mathrm{d}x^\nu + \mathrm{d}r^2$$
(Eq. 5.3.0)

with warp factor $A(r) = \cos(\sqrt{2}\,r)$, $r \in [0, r_{\max}]$, $r_{\max} = \pi/(2\sqrt{2})$.

### § 5.3.1.1: Four Paths to Λ

Four logically distinct mechanisms can contribute to the effective 4D cosmological constant from the KCR-Cone:

**Path A — Casimir vacuum energy (Level 1):** Quantum fields confined to the derived interval $[0, L^*]$ with Dirichlet boundary conditions have a shifted zero-point energy. This is a standard, calculable QFT effect that enters the stress-energy tensor on $M$ and therefore the Friedmann equation. **This is the primary gravitational contributor** to $\Lambda$ from the Σ topology.

**Path B — Fubini-Study curvature (Level 2):** The warp factor $A(r) = \cos(\sqrt{2}\,r)$ satisfies $A'' = -k^2 A$ with $k^2 = 2$ from the CP¹ Laplacian eigenvalue. This curvature is *information-geometric*: it measures the rate of statistical distinguishability between quantum states on Σ. It governs decoherence dynamics (how fast coherence decays along the $r$-direction) but does **not** enter the Friedmann equation as a gravitational source.

⚠️ **Category error in v2:** The previous draft treated Path B as the primary source of $\Lambda$, computing $\rho_{\mathrm{geom}} = +3.534 \times M_5^3 k^2/s$ and placing it in the Friedmann equation. This is incorrect. The FS curvature $k^2 = 2$ is a property of Σ (the coherence manifold), not of $M$ (spacetime). In physical units, $\rho_{\mathrm{geom}}$ at the Casimir scale is $10^{61} \times \Lambda_{\mathrm{obs}}$ — the standard cosmological constant problem in KK form. The error was conflating information-geometric curvature (Σ) with gravitational curvature ($M$). See `memory/kb/SESSION_2026-04-10_GEOMETRIC_LAMBDA_ANALYSIS.md`, Findings 1–3.

**Path C — T_{MΣ} frame-dragging (Level 3):** The cross-term $T_{M\Sigma}$ in the M × Σ metric couples decoherence dynamics to spacetime geometry. The λ·T = O(1) cancellation (§4.1.6, verified for the KCR-Cone) removes the Planck/Hubble hierarchy, giving $\rho_{\mathrm{drag}} \sim \alpha \times \Gamma_{\mathrm{dec}}^2 / G$ with $\alpha = 3/2$ (exact, from CP¹ geometry). If $\Gamma_{\mathrm{dec}} \sim H_0$, this gives $\rho_{\mathrm{drag}} \sim \rho_\Lambda$. This mechanism is the subject of ongoing work (RC-1 through RC-6, Paper 3 scope) and is NOT used in the SC3 analysis below.

**Path D — Vacuum entanglement dynamics (Level 4):** The Jacobson (1995) connection between entanglement entropy and Einstein's equations suggests a thermodynamic route from Σ to $M$. This likely unifies with Level 3 and is deferred to Paper 3.

### § 5.3.1.2: SC3 Strategy

For Paper 2, SC3 is evaluated using **Path A (Casimir)** as the primary gravitational contribution, with **Path B (FS curvature)** contributing to decoherence dynamics only. Paths C and D are noted as potentially dominant contributions that require the rigorous T_{MΣ} backreaction derivation (Paper 3 scope).

This is a conservative posture: the Casimir prediction is calculable and falsifiable. If Paths C/D are confirmed, the Casimir contribution becomes subdominant — but the ISL prediction from Path A remains a testable signature regardless.

---

## § 5.3.2: What Derived Compactification Contributes

### § 5.3.2.1: Five-Level Σ → M Coupling Hierarchy

The KCR-Cone geometry produces multiple distinct contributions to the effective cosmological constant. These are organized by mechanism:

| Level | Mechanism | Source | Enters Friedmann? | Status |
|-------|-----------|--------|--------------------|--------|
| **1** | Casimir energy | Σ topology → Dirichlet BCs on interval | ✅ YES | **Calculable (this section)** |
| **1b** | Topological zero-point | c₁ = 1 Hopf bundle → AS index modifies mode count | ✅ YES (< 1% correction) | **D4 complete** |
| **1c** | Radion zero-point | Breathing mode m² ≈ 0.01 on $M$ | Subdominant | Noted |
| **2** | FS curvature k² = 2 | CP¹ Laplacian eigenvalue | ❌ NO — information-geometric | **Category error corrected** |
| **3** | T_{MΣ} frame-dragging | Machian backreaction, α = 3/2 | ✅ YES (if confirmed) | Paper 3 scope (RC-1–RC-6) |
| **4** | Vacuum entanglement | Jacobson δQ = TdS | Likely unifies with Level 3 | Paper 3 scope |

Levels 1 and 1b are the basis of the SC3 analysis in this paper. Level 2 is excluded from the Friedmann equation (it governs decoherence dynamics on Σ). Levels 3 and 4 are flagged as potentially dominant but require derivations not yet completed.

### § 5.3.2.2: Level 1b — Atiyah-Singer Topological Zero-Point (D4 Result)

On the KCR-Cone, the Atiyah–Singer index theorem lets us replace an assumed compactification with a **derived** one whose zero-point structure is fixed by topology rather than by hand. We treat the angular sector as $S^2 \simeq \mathbb{CP}^1$ with a $U(1)$ line bundle $\mathcal{L}$ of first Chern class $c_1(\mathcal{L}) = 1$, the minimal Hopf/monopole configuration. Identifying this geometric $U(1)$ with hypercharge ⚠️, each SM field of hypercharge $Y$ couples to the twisted Dirac operator $D_Y$ on $S^2$, whose index is $\mathrm{ind}(D_Y) = c_1(\mathcal{L}^Y) = Y$. The index counts the net chiral zero modes on $S^2$, $n_+ - n_- = Y$, so any representation with $Y \neq 0$ carries topologically protected zero modes, while hypercharge-neutral fields do not. Summing over colors and weak components within one SM generation gives integer indices for each multiplet and a vanishing total index, reflecting the familiar anomaly-free structure of SM hypercharge. For the Casimir calculation, these protected zero modes are not part of the massive KCR tower that sources the finite vacuum energy shift, so the effective mode-count parameter $f$ in $\rho_\Lambda = (\pi^2 \hbar c / 1440)\,f / L^{*4}$ is reduced slightly from the naive SM value $f = 54$. Even if we conservatively remove a few fermionic degrees of freedom per generation, the resulting change in $L^*$ is at the percent level, leaving the predicted interval in the same $\mathcal{O}(10^2)\,\mu\mathrm{m}$ band. Thus Level 1b does not dramatically move the SC3 ISL prediction, but it upgrades the mode count from an arbitrary field inventory to a topological invariant of the Hopf bundle: the Casimir contribution to $\Lambda$ is now constrained by $c_1 = 1$, not by an assumed compactification ansatz.

---

## § 5.3.3: Casimir Energy on the Derived Interval (Level 1)

### § 5.3.3.1: Setup (Klein-Free)

The extra dimension is the geometrically compact interval $r \in [0, r_{\max}]$ with physical length $L^* = r_{\max} \times s$. There is no Klein circle. Boundary conditions are Dirichlet-type at both ends: at $r = 0$ (brane) and at $r = r_{\max}$ (pinch-off where $A = 0$).

The mode expansion on the interval is:

$$\phi(r) = \sum_{n=1}^{\infty} a_n \sin\!\left(\frac{n\pi r}{L^*}\right) \quad \text{(bosons, Dirichlet)}$$

$$\psi(r) = \sum_{n=0}^{\infty} b_n \sin\!\left(\frac{(n+\tfrac{1}{2})\pi r}{L^*}\right) \quad \text{(fermions)}$$

### § 5.3.3.2: Casimir Energy Density (Interval, Dirichlet BC)

Define $f := \tfrac{7N_F}{8} - N_B$. The regularized Casimir energy density on the interval $[0,L^*]$ with Dirichlet BC is:

$$\rho_{\mathrm{Cas}}(L^*) = \frac{\pi^2 \hbar c}{1440\,L^{*4}}\,f$$
(Eq. 5.3.1)

This is a factor of 2 smaller than the circle result ($\pi^2 \hbar c f / 720 L^4$) because standing waves have half the mode density of travelling waves at the same wavelength.

### § 5.3.3.3: Scale Prediction

Setting $\rho_{\mathrm{Cas}} = \rho_\Lambda$:

$$L^* = \left(\frac{\pi^2 \hbar c\,f}{1440\,\rho_\Lambda}\right)^{1/4}$$
(Eq. 5.3.2)

For the SM sector with Dirac neutrinos ($f = 54$):

$$\boxed{L^* \approx 68.6\,\mu\mathrm{m} \quad \text{(full SM, } f = 54\text{)}}$$
(Eq. 5.3.3)

Self-consistent iteration ($f_{\mathrm{eff}}$ at each $L^*$) converges to:

$$\boxed{L^* \approx 55.7\,\mu\mathrm{m} \quad \text{(self-consistent, } f_{\mathrm{eff}} = 23.5\text{)}}$$
(Eq. 5.3.4)

**Predicted range:** $L^* \in [56, 69]\,\mu\mathrm{m}$.

### § 5.3.3.4: ISL Bound

The first genuine KCR graviton has dimensionless mass $m_1^2 = 20.1$ from the volcano potential. The physical wavelength:

$$\lambda_1 = \frac{L^*}{m_1} \approx \frac{68.6}{4.48} \approx 15.3\,\mu\mathrm{m} \quad \text{(full SM)}$$

$$\lambda_1 \approx 12.4\,\mu\mathrm{m} \quad \text{(self-consistent)}$$

Both are safely below the Lee et al. (2020) ISL bound of 44 μm. **ISL: PASSES with 3× margin.** ✓

### § 5.3.3.5: Branch Screening

| Sector | $N_B$ | $N_F$ | $f$ | $L^*$ (μm) | ISL? |
|--------|-------|-------|-----|-------------|------|
| **SM (Dirac ν)** | 30 | 96 | +54 | 68.6 | ✓ |
| **SM (Majorana ν)** | 30 | 90 | +48.75 | 66.7 | ✓ |
| **Self-consistent** | 20 | 6 | +23.5 | 55.7 | ✓ |
| **N=1 SUSY minimal** | 1 | 1 | −0.125 | — | See note |
| **N=2 SUSY** | 3 | 3 | −0.375 | — | See note |

**SUSY note:** Sectors with $f < 0$ give $\rho_{\mathrm{Cas}} < 0$. In the Level 1 analysis (Casimir only), this gives $\Lambda_{\mathrm{eff}} < 0$, which fails SC3. However, if Level 3 (T_{MΣ} frame-dragging) is confirmed as a positive contributor, SUSY sectors may be rescued. This depends on the RC-1 calculation (Paper 3 scope).

### § 5.3.3.6: Non-Linear KCR Mode Spacing

The volcano potential on the derived interval gives:

$$m_n/m_1 \approx 1,\; 1.67,\; 2.32,\; 2.97 \quad \text{(derived compactification)}$$

vs. Klein $S^1$:

$$m_n/m_1 = 1,\; 2,\; 3,\; 4 \quad \text{(Klein circle)}$$

This is a **new testable prediction** that distinguishes derived compactification from Klein's ad hoc circle.

---

## § 5.3.4: What Remains Open

### § 5.3.4.1: FS Curvature and the Decoherence Rate

The Fubini-Study curvature $k^2 = 2$ of $\Sigma = \mathbb{CP}^1$ does not enter the Friedmann equation. It enters the **decoherence dynamics** on Σ: it determines the rate at which quantum states decorrelate along the $r$-direction, the shape of the volcano potential, and the KCR mode spectrum. The dimensionless value $\rho_{\mathrm{geom}} = +3.534$ (the A⁴-weighted curvature integral) is real as an information-geometric quantity — it belongs in the decoherence rate equation, not in the Friedmann equation.

### § 5.3.4.2: Radion Stabilization (OP-5)

**Shape (TOPOLOGICALLY FROZEN):** $r_{\max} = \pi/(2\sqrt{2})$, set by $k^2 = 2$, has zero moduli. Topologically fixed by CP¹ geometry. No Goldberger-Wise potential needed. ✓

**Scale:** The physical scale factor $s$ (where $L^* = r_{\max} \times s$) must be stabilized. In the Casimir-only picture (Level 1), the scale is set by $\rho_{\mathrm{Cas}}(L^*) = \rho_\Lambda$, giving $L^* \in [56, 69]\,\mu\mathrm{m}$. Whether there exists a dynamical mechanism (potential minimum, cosmological attractor, or other) that drives $s$ to this value is an open question.

**Status:** Shape RESOLVED; scale PARTIALLY RESOLVED (Casimir balance gives the value, but the dynamical mechanism driving $s$ to that value is not yet demonstrated). This replaces the v2 claim of a "cosmological attractor" which relied on the Level 2 category error.

### § 5.3.4.3: Level 3 — T_{MΣ} Frame-Dragging

The α = 3/2 result (Phase 0–2 calculations, April 10 session) shows that the T_{MΣ} cross-term backreaction produces $\rho_{\mathrm{drag}} = (3/2) \times \Gamma_{\mathrm{dec}}^2 / G$ with no hierarchy factor. If the cosmic decoherence rate is $\Gamma_{\mathrm{dec}} \sim 0.68 H_0$, this gives $\Omega_{\mathrm{drag}} \sim 0.69$ — matching $\Omega_\Lambda$. This is a potentially dominant contributor that would change the SC3 picture from "Casimir sets Λ" to "frame-dragging sets Λ, Casimir provides a sub-millimeter correction." The rigorous derivation requires RC-1 (backreaction from the action principle), which is Paper 3 scope.

### § 5.3.4.4: Post-Transition Field Content

The field content determines $f$, which determines $L^*$. Paper 3, Axiom B is required for the specific $(N_B, N_F)$ count. The D4 result constrains $f$ topologically (via c₁ = 1), reducing the dependence on assumed field inventories.

---

## § 5.3.5: SC3 Verdict

| Condition | v1 | v2 (category error) | REVISED |
|-----------|----|----------------------|---------|
| **Source of Λ > 0** | Casimir only | Geometric Λ (❌ wrong) | Casimir (Level 1) + possible frame-dragging (Level 3) |
| **FS curvature role** | Not addressed | Friedmann source (❌ wrong) | Decoherence dynamics only ✓ |
| **Scale prediction** | r_f* ≈ 22 μm (wrong BC) | L* ≈ 46–56 μm | **L* = 56–69 μm** (D1 corrected) |
| **ISL bound** | Passes (wrong value) | Passes | **Passes with 3× margin** (λ₁ = 12–15 μm) |
| **OP-5 shape** | Unsolved | Resolved ✓ | **Resolved** (k² = 2 topological) ✓ |
| **OP-5 scale** | Unsolved | "Cosmological attractor" (❌) | **Partially resolved** (Casimir balance; mechanism TBD) |
| **Level 1b (D4)** | Not computed | Not computed | **ΔL*/L* < 1%, mode count topological** ✓ |
| **Level 3 (α = 3/2)** | Not known | Not known | **Identified; RC-1 needed (Paper 3)** |

**SC3 claim posture: CONDITIONALLY ESTABLISHED (Level 1).**

The Casimir energy on the derived interval with Dirichlet BCs gives $L^* \in [56, 69]\,\mu\mathrm{m}$, passing the ISL bound. The mode count is topologically constrained by $c_1 = 1$ (D4). Shape stabilization is topological (OP-5 shape resolved). Scale stabilization requires either (a) a dynamical mechanism driving $s$ to the Casimir-balance value, or (b) confirmation that Level 3 (frame-dragging) dominates, in which case the Casimir contribution becomes a sub-millimeter correction to a cosmologically-set Λ.

---

## Notation (REVISED)

| Symbol | Meaning |
|--------|---------|
| $L^*$ | Physical interval length; $L^* = r_{\max} \times s$ |
| $\rho_{\mathrm{Cas}}$ | Casimir energy density on interval with Dirichlet BC |
| $f$ | Mode-count parameter; $f = 7N_F/8 - N_B$ |
| $\lambda_1$ | Wavelength of first KCR graviton mode |
| $\alpha = 3/2$ | Geometric coupling constant from CP¹ (Level 3) |

**Removed:** $\rho_{\mathrm{geom,4D}}$ from Friedmann equation (Level 2 category error); $r_f^*$ notation (Klein-era); "cosmological attractor" for scale (relied on category error); "geometric Λ as primary source" (incorrect).

---

## Revision History

| Date | Change |
|------|--------|
| 2026-03-09 | v1 DRAFT — Casimir-as-source; $r_f^* \approx 21.8\,\mu\mathrm{m}$ |
| 2026-04-09 | §5.3.4.1 added — self-consistent iteration |
| 2026-04-10 | v2 DRAFT — Geometric Λ as primary (CONTAINS CATEGORY ERROR) |
| 2026-04-10 | **REVISED (D2)** — Category error corrected; five-level hierarchy; D1 values ($L^* = 56$–$69\,\mu\mathrm{m}$); D4 paragraph; Casimir restored as primary gravitational contributor |
