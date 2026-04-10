# § 5.3: SC3 — Effective Cosmological Constant from Derived Geometry

**Status:** v2 DRAFT — 2026-04-10. Major revision: geometric Λ as primary source, Casimir as correction.
**Supersedes:** `paper2_section_5.3_SC3_Casimir_DRAFT.md` (2026-03-09)
**Changes from v1:** (1) Λ_classical ≠ 0: warp curvature gives Λ_geom > 0 classically. (2) Casimir relabeled as quantum correction. (3) Sign condition secondary. (4) SUSY sectors allowed. (5) OP-5 resolved. (6) Notation: r_fiber/S¹/ψ → interval [0,L] with Dirichlet BC.

---

## § 5.3.1: The SC3 Condition and Its Geometric Resolution

The third self-consistency condition (SC3) requires that the observed cosmological constant,

$$\Lambda_{\mathrm{obs}} \approx 1.1 \times 10^{-52} \, \mathrm{m}^{-2},$$

emerges from the KCR-Cone geometry. Previous drafts required **quantum closure**: the classical Einstein tensor of the $S^3$ Hopf fiber geometry gives $\Lambda_{\mathrm{classical}} = 0$ (spine §3.4), so SC3 appeared to require Casimir energy as the sole source of $\Lambda_{\mathrm{obs}} > 0$.

This framing is superseded by the following result.

### § 5.3.1.1: Geometric Λ from Warp Curvature

The 5D metric of the KCR-Cone is

$$\mathrm{d}s^2_{5\mathrm{D}} = A^2(r)\,\eta_{\mu\nu}\,\mathrm{d}x^\mu \mathrm{d}x^\nu + \mathrm{d}r^2$$
(Eq. 5.3.0)

with warp factor $A(r) = \cos(\sqrt{2}\,r)$, $r \in [0, r_{\max}]$, $r_{\max} = \pi/(2\sqrt{2})$. The theory is genuinely 5D: four spacetime coordinates $(x^\mu)$ plus one geometrically compact decoherence-depth coordinate $r$. There is no separate Hopf-fiber spatial coordinate; the U(1) gauge structure emerges from the Berry phase of the coherence manifold $\Sigma = \mathbb{CP}^1$ (§3.2).

The 5D Einstein equations for (5.3.0) produce an effective 4D energy density when integrated over the interval with $A^4$ weighting (the standard Kaluza-Klein dimensional reduction weight):

$$\rho_{\mathrm{geom}}(r) = 3k^2\bigl[1 - \tan^2(kr)\bigr] \times \frac{M_5^3}{\mathrm{vol}}$$
(Eq. 5.3.1a)

where $k = \sqrt{2}$ (fixed by the Fubini-Study eigenvalue, §7). This expression is:
- **Positive** near the brane ($r \ll r_{\max}$, where $\tan^2(kr) < 1$)
- **Negative** near the pinch-off ($r \to r_{\max}$, where $\tan^2(kr) \to \infty$)

The $A^4$-weighted integral over the interval gives the effective 4D geometric energy density:

$$\int_0^{r_{\max}} A^4(r)\,\rho_{\mathrm{geom}}(r)\,\mathrm{d}r = +1.666 \quad \text{(dimensionless)}$$
(Eq. 5.3.1b)

The volume factor is:

$$I_{A^3} = \int_0^{r_{\max}} A^3(r)\,\mathrm{d}r = 0.471$$
(Eq. 5.3.1c)

giving

$$\rho_{\mathrm{geom,4D}} = \frac{+1.666}{0.471} \times \frac{M_5^3 k^2}{s} = +3.534 \times \frac{M_5^3 k^2}{s} > 0$$
(Eq. 5.3.1d)

where $s$ is the physical scale factor mapping dimensionless $r$ to meters ($s = L/r_{\max}$).

**This is positive.** The $A^4$ weighting strongly suppresses the negative contribution near the pinch-off (since $A^4 \to 0$ faster than $\tan^2 \to \infty$), leaving a net positive 4D vacuum energy from pure geometry.

The Gibbons-Hawking-York boundary term at the pinch-off vanishes:

$$K \times A^3 \Big|_{r = r_{\max}} = 0$$

since $A(r_{\max}) = 0$. The geometry is self-consistent at the boundary.

### § 5.3.1.2: Revised SC3 Narrative

**Old (v1) narrative:** Classical geometry gives $\Lambda_{\mathrm{classical}} = 0$. SC3 requires quantum closure via Casimir energy. Sign condition $f > 0$ is the primary constraint. SUSY sectors excluded.

**New (v2) narrative:** The classical $\cos(\sqrt{2}\,r)$ warp factor has intrinsic positive curvature energy. When the extra dimension is integrated out, this yields $\Lambda_{\mathrm{geom}} > 0$ classically — no quantum fields required for the sign. The Casimir energy on the derived interval is a **quantum correction** to $\Lambda_{\mathrm{geom}}$, not its source. The sign of $\Lambda$ is geometrically guaranteed. The sign condition $f > 0$ on the field content affects the correction, not the leading term. SUSY sectors are no longer excluded.

**SC3 revised claim:** The KCR-Cone with warp factor $A(r) = \cos(\sqrt{2}\,r)$ produces $\Lambda_{\mathrm{eff}} > 0$ from classical geometry, with Casimir energy providing a subleading quantum correction whose magnitude determines the physical scale $s$ (and hence the interval length $L = r_{\max} \times s$).

---

## § 5.3.2: Geometric Λ — The Primary Contribution

### § 5.3.2.1: Physical Interpretation

The $\cos(\sqrt{2}\,r)$ warp factor is not a flat extra dimension — it has intrinsic curvature that costs energy. The geometric origin is the Fubini-Study eigenvalue $k^2 = 2$ (Proposition 4.2, §7): the warp factor is an eigenfunction of the Laplacian on $\Sigma = \mathbb{CP}^1$ with eigenvalue 2. The same curvature that pins $k^2 = 2$ also produces the positive effective cosmological constant.

Physically: the extra dimension is not a free direction. It is geometrically compressed by the coherence manifold's curvature. This compression costs energy, appearing in 4D as $\Lambda_{\mathrm{geom}} > 0$.

### § 5.3.2.2: Scale from Friedmann Balance

The physical scale factor $s$ (mapping dimensionless $r$ to meters) is determined by the Friedmann equation at the current epoch:

$$H^2 = \frac{8\pi G_4}{3}\bigl[\rho_{\mathrm{geom}}(s) + \rho_{\mathrm{Cas}}(s)\bigr]$$
(Eq. 5.3.2)

At leading order ($\rho_{\mathrm{geom}} \gg \rho_{\mathrm{Cas}}$):

$$H_0^2 \approx \frac{8\pi G_4}{3} \times \frac{3.534 \, M_5^3 k^2}{s}$$

This determines $s_{\mathrm{now}}$ from $H_0 \approx 67.4 \,\mathrm{km/s/Mpc}$. The scale $s$ evolves cosmologically (it increases with cosmic expansion) at the Hubble rate $\dot{s}/s \sim H_0$. This is a cosmological scale — the decoherence depth of the observable universe has been growing for 13.8 Gyr.

The cosmological constant is not a parameter to be tuned; it is the energy density of the geometrically curved extra dimension at the current epoch.

### § 5.3.2.3: OP-5 Resolution — Radion Stabilization

The geometric Λ result resolves the radion stabilization problem (OP-5) in two parts.

**Shape (TOPOLOGICALLY FROZEN):** The dimensionless shape of the interval — $r_{\max} = \pi/(2\sqrt{2})$, set by $k^2 = 2$ from the Fubini-Study Laplacian eigenvalue — has zero moduli. The shape cannot be continuously perturbed without changing $k^2$, which is topologically fixed by the geometry of $\mathbb{CP}^1$. No Goldberger-Wise potential is needed to stabilize the shape.

**Scale (COSMOLOGICAL ATTRACTOR):** The physical scale factor $s$ is determined by the Friedmann balance (Eq. 5.3.2). At the current epoch, $H = H_0$ determines $s = s_{\mathrm{now}}$. The scale cannot decrease (non-traversability: $\dot{r} \geq 0$ from Lindblad contractivity, Proposition 4.2) and increases at the Hubble rate. This is a cosmological attractor, not a potential minimum in the traditional sense.

**No Goldberger-Wise scalar required. No KKLT potential required.** The stabilization uses:
- Topology ($k^2 = 2$ from $\mathbb{CP}^1$ curvature)
- Classical geometry (warp-factor curvature energy, Eq. 5.3.1d)
- Cosmology (Friedmann balance, Eq. 5.3.2)
- Thermodynamics (non-traversability as one-way constraint)

**Status: OP-5 RESOLVED (2026-04-10).**

---

## § 5.3.3: Quantum Correction — Casimir Energy on the Derived Interval

### § 5.3.3.1: Setup (Klein-Free)

The extra dimension is the geometrically compact interval $r \in [0, r_{\max}]$ with physical length $L = r_{\max} \times s$. There is no Klein circle. Boundary conditions are Dirichlet-type at both ends: at $r = 0$ (brane) and at $r = r_{\max}$ (pinch-off where $A = 0$).

The mode expansion on the interval is:

$$\phi(r) = \sum_{n=1}^{\infty} a_n \sin\!\left(\frac{n\pi r}{L}\right) \quad \text{(bosons, Dirichlet)}$$

$$\psi(r) = \sum_{n=0}^{\infty} b_n \sin\!\left(\frac{(n+\tfrac{1}{2})\pi r}{L}\right) \quad \text{(fermions)}$$

This differs from the Klein circle (which uses $e^{iny/R}$ with periodic/antiperiodic BC) by a factor of 2 in the Casimir energy density: standing waves on a bounded interval contribute half the energy of travelling waves on a circle of the same length.

### § 5.3.3.2: Casimir Energy Density (Interval, Dirichlet BC)

Define $f := \tfrac{7N_F}{8} - N_B$ as before. The regularized Casimir energy density on the interval $[0,L]$ with Dirichlet BC is:

$$\rho_{\mathrm{Cas}}(L) = \frac{\pi^2 \hbar c}{1440\,L^4}\,f$$
(Eq. 5.3.3)

This is a factor of 2 smaller than the circle result ($\pi^2 \hbar c f / 720 L^4$) because standing waves have half the mode density of travelling waves at the same wavelength. Equivalently, using $L = r_{\max} \times s$:

$$\rho_{\mathrm{Cas}}(s) = \frac{\pi^2 \hbar c}{1440\,(r_{\max} s)^4}\,f$$
(Eq. 5.3.3a)

**Sign convention:** The sign of $\rho_{\mathrm{Cas}}$ depends on $f = \tfrac{7N_F}{8} - N_B$:
- $f > 0$: Casimir correction is positive (adds to $\Lambda_{\mathrm{geom}}$)
- $f < 0$: Casimir correction is negative (partially cancels $\Lambda_{\mathrm{geom}}$)
- $f = 0$: No quantum correction (pure geometric $\Lambda$)

Because $\Lambda_{\mathrm{geom}} > 0$ is geometrically guaranteed, the sign condition $f > 0$ is **no longer the primary SC3 constraint**. It affects only the magnitude of the quantum correction.

### § 5.3.3.3: Branch Screening — Updated

The branch screening table is retained, but the framing changes: sectors are no longer screened for whether they can produce $\Lambda > 0$ (geometry already guarantees this), but rather for whether their Casimir correction is consistent with the observed magnitude.

**Status: CHECKED (sector enumeration)**

| Sector | $N_B$ | $N_F$ | $f$ | Casimir correction sign | SC3 compatibility |
|--------|-------|-------|-----|------------------------|-------------------|
| **Scalar only** | 1 | 0 | −1 | Negative (partial cancellation) | ✓ ALLOWED (geometric Λ still positive) |
| **Weyl pair** | 0 | 2 | +1.75 | Positive | ✓ ALLOWED |
| **N=1 SUSY minimal** | 1 | 1 | −0.125 | Small negative | ✓ ALLOWED (previously excluded — now admitted) |
| **N=2 SUSY** | 3 | 3 | −0.375 | Negative | ✓ ALLOWED (previously excluded — now admitted) |
| **SM (Dirac ν)** | 30 | 96 | +54 | Positive | ✓ ALLOWED (preferred) |
| **SM (Majorana ν)** | 30 | 90 | +48.75 | Positive | ✓ ALLOWED |

**Key changes from v1:**
1. SUSY sectors are **no longer excluded**. The $f < 0$ condition previously failed SC3 because it gave $\Lambda_{\mathrm{Cas}} < 0$ which was interpreted as the total $\Lambda < 0$. Now $\Lambda_{\mathrm{geom}} > 0$ is established classically; SUSY sectors give a small negative correction that does not flip the sign.
2. The relevant constraint is whether the magnitude $|\rho_{\mathrm{Cas}}|$ is consistent with the total $\Lambda_{\mathrm{obs}}$ after the geometric contribution is accounted for. This requires the full Friedmann balance, not just the Casimir balance alone.
3. Sector selection is still contingent on Paper 3, Axiom B.

---

## § 5.3.4: Scale Analysis

### § 5.3.4.1: Casimir Correction Scale

The scale at which the Casimir correction equals $\rho_\Lambda$ (i.e., the scale where Casimir energy alone would match $\Lambda_{\mathrm{obs}}$) is:

$$L_{\mathrm{Cas}}^* = \left(\frac{\pi^2 \hbar c\,f}{1440\,\rho_\Lambda}\right)^{1/4}, \quad \rho_\Lambda = \frac{\Lambda_{\mathrm{obs}} c^4}{8\pi G_4}$$
(Eq. 5.3.4)

For the SM sector with Dirac neutrinos ($f = 54$):

$$\boxed{L_{\mathrm{Cas}}^* \approx 55.6\,\mu\mathrm{m}, \quad \Rightarrow s^* \approx \frac{L_{\mathrm{Cas}}^*}{r_{\max}} \approx 50\,\mu\mathrm{m}}$$

This is the scale at which the Casimir quantum correction is of order $\Lambda_{\mathrm{obs}}$. It is **not** the primary prediction for the physical scale (which comes from the Friedmann balance, §5.3.2.2), but it sets the scale at which quantum corrections become important.

**Comparison with v1 ($r_{\mathrm{fiber}}^*$ notation):** The v1 prediction $r_{\mathrm{fiber}}^* \approx 21.8\,\mu\mathrm{m}$ was the Casimir-balance scale using the wrong formula (circle rather than interval Dirichlet). The corrected interval formula gives $L_{\mathrm{Cas}}^*/r_{\max} \approx 50\,\mu\mathrm{m}$ as the equivalent scale. In any case, this is now interpreted as the **Casimir correction scale**, not the primary cosmological prediction.

### § 5.3.4.2: Self-Consistency of the Massless-Field Approximation

At $L \sim 55\,\mu\mathrm{m}$, the KCR energy scale is $E_{\mathrm{KK}} = \hbar c / L \approx 3.5\,\mathrm{meV}$. Self-consistent iteration (computing $f_{\mathrm{eff}}$ at each $L^*$ and re-solving) converges to:

| Quantity | Full SM ($f = 54$) | Self-consistent |
|---|---|---|
| Effective massless bosonic DOF | 30 | 20 ($\gamma$, graviton, 8 gluons) |
| Effective massless fermionic DOF | 96 | 6 (3 Dirac $\nu$, marginal) |
| $f_{\mathrm{eff}}$ | 54 | 23.5 |
| $L_{\mathrm{Cas}}^*$ | 55.6 μm | ~46 μm |
| ISL margin (vs. 44 μm Lee 2020 bound) | 1.3× | ~1.05× |

Three open subtleties remain: (1) gluon confinement, (2) neutrino mass hierarchy, (3) finite-mass corrections. Conservative range: $L_{\mathrm{Cas}}^* \in [37, 56]\,\mu\mathrm{m}$.

### § 5.3.4.3: ISL Bound Comparison (Klein-Free)

The gravitational ISL comparison for the derived interval geometry uses the first genuine KCR graviton, not a Yukawa correction from a Klein circle. The graviton Schrödinger equation on $[0, r_{\max}]$ with volcano potential

$$V(r) = -3 + \tfrac{3}{2}\tan^2(\sqrt{2}\,r)$$

gives the KCR mode spectrum:

| Mode | $m^2$ (dimless) | Identity | $\lambda$ (μm) at $s \sim 50\,\mu\mathrm{m}$ |
|------|-----------------|----------|----------------------------------------------|
| 0 | 0 | Graviton zero mode | $\infty$ (massless) |
| ~0 | 0.01 | Radion (OP-5, resolved) | ~2600 |
| 1 | 20.1 | First KCR graviton | **13.3 μm** |
| 2 | 56.2 | Second KCR graviton | 7.9 μm |

The near-zero mode (71% overlap with radion wavefunction) is the breathing mode of $r_{\max}$ — it is OP-5's stabilized radion appearing in the spectrum, not a KCR graviton. The first genuine KCR graviton is at $\lambda_1 \approx 13.3\,\mu\mathrm{m}$, safely below the 44 μm ISL bound (Lee et al. 2020). ✓

**Non-linear mode spacing:** $m_n/m_1 \approx 1, 1.67, 2.32, 2.97$ (non-linear). This distinguishes derived compactification from Klein's $S^1$ (which gives exactly linear spacing $1, 2, 3, 4$). This is a **new testable prediction**.

---

## § 5.3.5: Open Issues

### § 5.3.5.1: Radion Stabilization

**Status: RESOLVED (2026-04-10) — see §5.3.2.3 above.**

Shape is topologically frozen ($k^2 = 2$ from $\mathbb{CP}^1$ curvature). Scale is a cosmological attractor (Friedmann balance at each epoch). No $V_{\mathrm{eff}}$ minimum required.

The $Z_L$ correction from Spike 11 (radion kinetic normalization $A^3$-weighted, radion mass ~48% lighter) remains valid. The lighter radion has a larger Yukawa range but does not affect the primary SC3 result (geometric $\Lambda$), which is independent of $Z_L$.

### § 5.3.5.2: Post-Transition Field Content

**Status: CONTINGENT (depends on Paper 3)**

The field content determines the sign and magnitude of the Casimir correction. In the new picture, a negative correction ($f < 0$) does not fail SC3 — it reduces $\Lambda_{\mathrm{eff}}$ from the geometric value. Whether the resulting $\Lambda_{\mathrm{eff}}$ matches $\Lambda_{\mathrm{obs}}$ exactly depends on both the geometric contribution and the Casimir correction in combination. Paper 3, Axiom B is required for the specific $(N_B, N_F)$ count.

### § 5.3.5.3: Atiyah-Patodi-Singer Index on the Interval

The compact space is now $[0, r_{\max}] \times S^2$ (interval times sphere base), not $S^3$ (Klein compact). The index theorem applicable to a manifold with boundary is the Atiyah-Patodi-Singer (APS) theorem:

$$\mathrm{ind}(D) = \int_X \hat{A}(TX) - \tfrac{1}{2}\eta(\partial X)$$

For the interval geometry $[0, r_{\max}] \times S^2$:
- The $\hat{A}$-genus is zero (3-dimensional; $\hat{A}$ is non-trivial only in dimensions $4k$)
- The $\eta$-invariant at the $S^2$ boundary vanishes by the $S^2$ symmetry

**Result:** $\mathrm{ind}(D) = 0$, same as the Klein $S^3$ result. No fermion-content obstruction from the index theorem. The sign condition ($f > 0$ for Casimir; now secondary) is the only constraint on $N_F$.

**Status: VERIFIED (analytically).**

### § 5.3.5.4: Warp/Interval Decoupling Assumption

The Casimir formula (Eq. 5.3.3) assumes the interval modes decouple from the transverse $S^2$ geometry. The full coupled analysis requires solving mode equations in the complete 5D background. Corrections are expected to be $O(1)$ factors, not parametrically large or small.

**Status: UNTESTED.** Corrections could shift $L_{\mathrm{Cas}}^*$ by order-unity factors.

### § 5.3.5.5: Higher-Order Quantum Corrections

Massive modes, loop corrections, finite-temperature effects, and cubic interactions are all deferred. These are subleading relative to both the geometric $\Lambda$ and the leading Casimir correction.

**Status: UNKNOWN.**

---

## § 5.3.6: SC3 Verdict — Geometric Λ with Quantum Corrections

### Summary of Findings

| Condition | v1 Status | v2 Status |
|-----------|-----------|-----------|
| **Source of $\Lambda > 0$** | Quantum (Casimir) — required | Classical (warp curvature) — derived ✓ |
| **Sign condition $f > 0$** | Primary constraint | Secondary (affects correction only) |
| **SUSY sectors** | Excluded ($f < 0$ failed) | Allowed (geometric Λ survives) |
| **Scale prediction** | $r_f^* \approx 21.8\,\mu\mathrm{m}$ (Casimir-primary) | $L_{\mathrm{Cas}}^* \approx 46\text{–}56\,\mu\mathrm{m}$ (correction scale) |
| **Radion shape** | Unsolved | Topologically frozen ($k^2 = 2$) ✓ |
| **Radion scale** | Unsolved | Cosmological attractor ✓ |
| **ISL bound** | $r^* = 21.8\,\mu\mathrm{m} < 44\,\mu\mathrm{m}$ ✓ | $\lambda_1^{\mathrm{KK}} = 13.3\,\mu\mathrm{m} < 44\,\mu\mathrm{m}$ ✓ |
| **APS index** | $\mathrm{ind} = 0$ on $S^3$ ✓ | $\mathrm{ind} = 0$ on $[0,r_{\max}] \times S^2$ ✓ |
| **OP-5** | Critical — OPEN | **RESOLVED** |

### Claim Posture: GEOMETRIC Λ (Conditionally Established)

**SC3 in v2:** The KCR-Cone with $A(r) = \cos(\sqrt{2}\,r)$ produces a positive cosmological constant from classical geometry. The magnitude is set by the Friedmann balance at the current epoch (cosmological attractor). The Casimir energy on the derived interval provides a quantum correction whose scale is $L_{\mathrm{Cas}}^* \sim 46\text{–}56\,\mu\mathrm{m}$.

Remaining open items:
1. **Post-transition field content** (Paper 3): determines the sign and magnitude of the Casimir correction
2. **Warp/interval decoupling** (untested): $O(1)$ corrections to $\rho_{\mathrm{Cas}}$ expected
3. **Quantitative Friedmann balance**: explicit computation of $s_{\mathrm{now}}$ from $H_0$ requires the 5D–4D reduction factor (deferred to Paper 2B)

---

## § 5.3.7: Connection to SC1 and SC2

- **SC1** (§5.1): Requires $A(r,z) \sim z \cdot f(r)$ for late-time acceleration. The geometric $\Lambda > 0$ from the warp factor is consistent with late-time acceleration; the Casimir correction adds to this.
- **SC2** (§5.2): Requires normalizable graviton zero mode. The volcano potential $V(r) = -3 + \tfrac{3}{2}\tan^2(\sqrt{2}\,r)$ gives a normalizable zero mode with half-weight at $r/r_{\max} \approx 22.6\%$. ✓
- **SC3** (this section): $\Lambda_{\mathrm{eff}} > 0$ from geometry + quantum correction.

All three conditions are mutually consistent in the Klein-free picture.

---

## § 5.3.8: Paper 3 Interface Hooks (updated)

1. **P3-SC3-1: Realized post-transition branch** — Specify $(N_B, N_F)$ from Axiom B. This determines the magnitude and sign of the Casimir correction. The sign of $\Lambda$ is no longer contingent on this outcome (geometry guarantees it); only the correction magnitude depends on Paper 3.

2. **P3-SC3-2: Phase-transition gate** — Provide the transition scale/redshift where 4D effective formulas are valid. The geometric Λ derivation (Eq. 5.3.1d) is a 4D effective result; its 5D validity requires this gate.

3. **P3-SC3-3: High-z correction channel** — Provide projection rule for phase-coupling corrections. Sign conventions must be fixed relative to the geometric Λ contribution (which is now the leading term).

4. **P3-SC3-4: Stabilization** — OP-5 is resolved at the topological/cosmological level. Paper 3 may provide a more detailed dynamical picture, but no new mechanism is required.

**Status**: INTERFACE-CONTRACT ONLY (1–3 remain forward dependencies; 4 resolved).

---

## § 5.3.9: New Testable Prediction — Non-Linear KK Mode Spacing

The Klein-free derived compactification predicts non-linear KCR graviton mass ratios:

$$m_n/m_1 \approx 1,\; 1.67,\; 2.32,\; 2.97 \quad \text{(derived compactification)}$$

vs. Klein $S^1$:

$$m_n/m_1 = 1,\; 2,\; 3,\; 4 \quad \text{(Klein circle)}$$

If KCR graviton resonances are detected in future experiments, the spacing pattern distinguishes CR's derived compactification from Klein's ad hoc circle. This is a clean, model-independent prediction.

---

## Notation and Conventions (v2)

| Symbol | Meaning |
|--------|---------| 
| $\Lambda_{\mathrm{obs}}$ | Observed cosmological constant; $\approx 1.1 \times 10^{-52}\,\mathrm{m}^{-2}$ |
| $r$ | Decoherence-depth coordinate; $r \in [0, r_{\max}]$, $r_{\max} = \pi/(2\sqrt{2})$ |
| $L = r_{\max} \times s$ | Physical interval length; $s$ = physical scale factor |
| $A(r) = \cos(\sqrt{2}\,r)$ | Warp factor; exact solution from Fubini-Study eigenvalue $k^2 = 2$ |
| $s$ | Physical scale factor (maps dimensionless $r$ to meters); determined by Friedmann balance |
| $N_B$ | Massless bosonic DOF (Dirichlet BC on interval) |
| $N_F$ | Massless fermionic DOF (mixed BC on interval) |
| $f = \tfrac{7N_F}{8} - N_B$ | Sign factor for Casimir correction |
| $\rho_{\mathrm{geom,4D}}$ | Geometric energy density from warp curvature; $= +3.534 \times M_5^3 k^2 / s > 0$ |
| $\rho_{\mathrm{Cas}}$ | Casimir correction on interval with Dirichlet BC |
| $G_4$ | 4D Newton constant |
| $L_{\mathrm{Cas}}^*$ | Casimir-balance scale (not the primary physical prediction) |

**Removed from v1:** $r_{\mathrm{fiber}}$, $r_f^*$ (Casimir-primary), $L = 2\pi r_{\mathrm{fiber}}$ (Klein circumference), $\psi \in [0,2\pi)$ (Klein coordinate), periodic/antiperiodic BC on $S^1$.

---

## Revision History

| Date | Change |
|------|--------|
| 2026-03-09 | v1 DRAFT — Casimir-as-source narrative; $r_f^* \approx 21.8\,\mu\mathrm{m}$; Z_L correction |
| 2026-04-09 | §5.3.4.1 added — self-consistent Casimir iteration; $r_f^* = 17.72\,\mu\mathrm{m}$ |
| 2026-04-10 | **v2 DRAFT** — Geometric Λ as primary; Casimir as correction; OP-5 resolved; Klein/S¹/ψ notation removed; SUSY sectors admitted; APS updated to interval; non-linear KK spacing added |

---

**End of § 5.3 v2**
