# § 5.3: SC3 — Effective Cosmological Constant via Casimir Energy on the Hopf Fiber

## § 5.3.1: The SC3 Condition

The third self-consistency condition (SC3) requires that the observed cosmological constant,

$$\Lambda_{\mathrm{obs}} \approx 1.1 \times 10^{-52} \, \mathrm{m}^{-2},$$

emerges naturally from the KK-Cone geometry with a single classical solution valid at all scales.

In the canonical metric of § 4.0,

$$\mathrm{d}s^2_{\mathrm{5D}} = -\mathrm{d}z^2 + \mathrm{d}r^2 + A(r,z)^2 \, \gamma_{ij} \, \mathrm{d}\theta^i \mathrm{d}\theta^j,$$

the four-dimensional effective metric (after dimensional reduction via Kaluza-Klein on $S^2$) is

$$\mathrm{d}s^2_{\mathrm{4D}} \approx g_{\mu\nu}^{\mathrm{eff}} \, \mathrm{d}x^\mu \mathrm{d}x^\nu + \ell_{\mathrm{eff}}^2(r, z) \, \mathrm{d}\psi^2,$$

where the Hopf fiber is parameterized by $\psi \in [0, 2\pi)$.

**Status: CHECKED (classical analysis in spine §3.4)**. The classical Einstein tensor $G^{\mathrm{(5D)}}$ computed from § 3.4 (spine reference) yields

$$\lambda_{\mathrm{classical}} = 0,$$

i.e., the *classical* Ricci scalar on $S^3$ vanishes, and the extrinsic curvature of the Hopf fiber within $S^3$ satisfies $K_{ab}^2 \equiv K_{ab} K^{ab}$ with $Q_{ab} = 0$ identically. Thus $\Lambda_{\mathrm{eff}}^{\mathrm{classical}} = 0$.

**SC3 therefore requires QUANTUM CLOSURE**: A non-zero contribution from vacuum quantum effects must be added to the classical geometry to match the observed $\Lambda_{\mathrm{obs}}$.

The most natural candidate is **Casimir energy** in the compact Hopf direction, arising from the quantization of massless fields with boundary conditions determined by the post-transition field content (see Paper 3, Axiom B).

---

## § 5.3.2: Casimir Energy on the Hopf Fiber

### Derivation Outline and Sign Conventions

Consider the quantum scalar field (and fermion) content propagating on the five-dimensional KK-Cone background, restricted to the Hopf fiber $S^1$ of circumference

$$L = 2\pi r_{\mathrm{fiber}}.$$

**Status: UNTESTED (full mode expansion)**. The calculation derives from zeta-function regularization of the vacuum energy density. The field-theoretic setup assumes:

1. Massless free fields on $S^1$ (intra-fiber modes only; couplings to warp direction deferred to higher order). **Scale caveat:** At $r_{\mathrm{fiber}} \sim 22\,\mu\mathrm{m}$, the KK energy scale is $\sim 1/r \sim 10\,\mathrm{meV}$. At this scale, only photons (2 d.o.f.), gravitons (2 d.o.f.), and possibly neutrinos contribute as effectively massless; all other SM particles ($m_W, m_Z, m_H$, quarks, charged leptons) have $m \gg 10\,\mathrm{meV}$ and are exponentially suppressed. The full $N_B = 30, N_F = 96$ counting assumes all fields are massless, which is self-consistent only if the relevant energy is set by the compactification scale (the KK tower), not by $1/r_{\mathrm{fiber}}$ directly. This tension is unresolved and could modify $f$ significantly.
2. **Periodic boundary conditions** on real bosons: $\phi(0) = \phi(L)$.
3. **Antiperiodic boundary conditions** on Weyl fermions: $\psi(0) = -\psi(L)$.
4. Minkowski metric in the internal $S^1$ (flat-space limit; curvature corrections suppressed at leading order).

The mode decomposition of a canonically quantized field on $S^1$ is

$$\phi(s) = \sum_{n \in \mathbb{Z}} a_n e^{2\pi i n s / L}, \quad \text{(boson)}$$

$$\psi(s) = \sum_{n \in \mathbb{Z} + 1/2} b_n e^{2\pi i (n + 1/2) s / L}, \quad \text{(fermion)}.$$

The zero-point energy of mode $n$ (per species) is $\hbar \omega_n = \hbar \cdot |2\pi n / L|$ for bosons and $\hbar |2\pi (n + 1/2) / L|$ for fermions.

Define

$$f := \frac{7N_F}{8} - N_B.$$

In the fixed convention used in this manuscript (massless modes, periodic bosons, antiperiodic fermions), the regularized Casimir **energy density** is

$$\rho_{\mathrm{Casimir}}(L) = \frac{\pi^2 \hbar c}{90\,L^4}\,f.$$

Using $L=2\pi r_{\mathrm{fiber}}$, this is equivalently

$$\rho_{\mathrm{Casimir}}(r_{\mathrm{fiber}}) = \frac{\hbar c}{1440\pi^2\,r_{\mathrm{fiber}}^4}\,f.$$

In this section, $\rho_{\mathrm{Casimir}}$ is always the 4D effective vacuum energy **density** after dimensional reduction on the fiber; 1D energy-per-length expressions $E\propto L^{-1}$ are not used without explicit volume factors.

The zeta-function values controlling the sign are

$$\zeta_B(s) = \sum_{n=1}^\infty n^{-s}, \quad \zeta_F(s) = \sum_{n=0}^\infty (n+1/2)^{-s},$$

with analytic continuation values $\zeta_B(-1)=-1/12$ and $\zeta_F(-1)=-1/24$.

**Equation 5.3.1:**

$$\rho_{\mathrm{Casimir}} = \frac{\hbar c}{1440\pi^2\,r_{\mathrm{fiber}}^4}\left(\frac{7N_F}{8} - N_B\right).$$

**Status: SCHEMATIC**. The numerical coefficient is locked to the Eq. 5.3.1 convention above; the full derivation from the five-dimensional stress-energy tensor is deferred.

### Sign Convention and Physical Interpretation

**Positive $\rho_{\mathrm{Casimir}}$ (repulsive vacuum energy)**:

The sign of Eq. 5.3.1 depends on the balance $f := 7N_F/8 - N_B$:

- If $f > 0$ (more fermion d.o.f. than bosons, weighted), then $\rho_{\mathrm{Casimir}} > 0$, contributing **positive** vacuum energy density (DE-like, repulsive).
- If $f < 0$, then $\rho_{\mathrm{Casimir}} < 0$, contributing **negative** vacuum energy density (attractive, unphysical for our context).

Within the sign convention of Eq. 5.3.1 (and neglecting additional vacuum contributions), SC3 requires $f > 0$ for a positive effective $\Lambda$, i.e.,

$$\boxed{N_F > \frac{8 N_B}{7} \approx 1.14 \, N_B.}$$

In this sense, this acts as a **selection rule** on the field content. Sectors with too many boson d.o.f. relative to fermions are excluded from producing the observed Λ.

---

## § 5.3.3: Branch Screening — Field Content Analysis

The post-transition sector field content is determined by Paper 3 (Axiom B phase transition). We screen candidate sectors against the sign condition.

**Status: CHECKED (sector enumeration)**. The table below summarizes closed-form results for $f = 7N_F/8 - N_B$ across representative sectors:

| Sector | Description | $N_B$ | $N_F$ | $f$ | SC3 Pass? | Notes |
|--------|-------------|-------|-------|-----|-----------|-------|
| **Scalar only** | Real scalar d.o.f. (massless) | 1 | 0 | −1 | ✗ FAIL | Negative $f$; purely bosonic. |
| **Weyl pair** | 2 Weyl fermions, 0 bosons | 0 | 2 | +1.75 | ✓ PASS | Minimal fermionic sector; cf. Table entry (3). |
| **N=1 SUSY minimal** | Chiral multiplet: 1 scalar + 1 Weyl | 1 | 1 | −0.125 | ✗ FAIL | Equal bosons ↔ fermions; SUSY makes $f$ worse. |
| **N=2 SUSY** | 2 chiral multiplets + vector | 3 | 3 | −0.375 | ✗ FAIL | Equal d.o.f.; $f < 0$ always. |
| **SM (Dirac ν)** | 30 boson d.o.f. (incl. Higgs, photon, gluons); 96 fermion d.o.f. (Dirac neutrinos) | 30 | 96 | +54 | ✓ PASS | Realistic; strong positive $f$. |
| **SM (Majorana ν)** | 30 bosons; 90 fermionic d.o.f. (Majorana neutrinos) | 30 | 90 | +48.75 | ✓ PASS | Also viable; slightly weaker $f$. |
| **Minimal fermionic** | $N_B = 2, N_F = 3$ | 2 | 3 | +0.625 | ✓ PASS | Minimal integer sector; marginal $f > 0$. |
| **GUT-extended** | SU(5) unification (∼150 bosons, ∼200 fermions) | 150 | 200 | +25 | ✓ PASS | Positive but roughly half SM value; heavier boson sector reduces $f$. |

**Key findings**:

1. **Boson-only sectors FAIL**: Any $N_F = 0$ gives $f = -N_B < 0$.

2. **SUSY sectors FAIL**: For $N_B = N_F$ (standard SUSY multiplet structure), $f = 7N_F/8 - N_F = -N_F/8 < 0$ always. **SUSY makes SC3 worse** — not worse in the usual UV-divergence sense, but in matching $\Lambda_{\mathrm{obs}}$. This is a non-trivial constraint: the simplest supersymmetric extensions are ruled out.

3. **SM with Dirac neutrinos PASSES**: With 96 Weyl fermions and 30 bosons, $f = 54$. This is a substantial, positive contribution.

4. **Minimal integer sector**: $N_B = 2, N_F = 3$ (e.g., 2 scalars + 3 Weyl fermions) gives $f = +0.625$, barely passing. This is a toy model; the scale is too large (see § 5.3.4).

**Status: CONTINGENT**. Which sector is realized depends on the outcome of the Paper 3 phase transition (Axiom B). The present analysis assumes one of the PASSING sectors emerges; the specific sector is NOT determined by SC3 alone.

---

## § 5.3.4: Scale Analysis — Fiber Radius Prediction

Matching the Casimir energy density to the observed cosmological constant:

$$\rho_{\mathrm{Casimir}} = \frac{\Lambda_{\mathrm{obs}}c^4}{8\pi G_4},$$

where $G_4$ is the 4D Newton constant (related to 5D Planck scale via dimensional reduction).

**Status: SCHEMATIC (dimensional reduction)**. Solving for $r_{\mathrm{fiber}}^*$ in the **SM sector with Dirac neutrinos** ($f = 54$):

$$r_{\mathrm{fiber}}^* = \left(\frac{\hbar c \cdot 54}{1440\pi^2\,\rho_{\mathrm{target}}}\right)^{1/4}, \qquad \rho_{\mathrm{target}}:=\frac{\Lambda_{\mathrm{obs}}c^4}{8\pi G_4}.$$

Substituting $\rho_{\mathrm{target}} \approx 5.32 \times 10^{-10} \, \mathrm{J/m^3}$ (equivalently $\Lambda_{\mathrm{obs}} \approx 1.1 \times 10^{-52} \, \mathrm{m}^{-2}$):

$$\boxed{r_{\mathrm{fiber}}^* \approx 21.8 \, \mu\mathrm{m} \quad (L^* = 2\pi r^* \approx 137 \, \mu\mathrm{m}).}$$

**Equation 5.3.2:**

$$r_{\mathrm{fiber}}^* \approx \left(\frac{\hbar c \cdot f}{1440\pi^2\,\rho_{\mathrm{target}}}\right)^{1/4}, \quad f = \frac{7N_F}{8} - N_B.$$

### Comparison with Experimental Bounds

**Inter-Space Length (ISL) bounds** (Lee et al. 2020; Chiaverini et al. 2006) probe the submillimeter-to-micron regime and strongly constrain extra-dimensional gravity corrections at tens-of-microns scales. Our prediction,

$$r_{\mathrm{fiber}}^* \approx 21.8 \, \mu\mathrm{m},$$

lies in the **actively testable ISL regime** (order $10^1$ μm). The KK Yukawa range is set by the fiber radius $r_{\mathrm{fiber}}$, not the circumference $L^*$. Whether it is allowed/excluded depends on the detailed coupling model and should be checked against full exclusion curves rather than a single-threshold inequality.

**Status: CONDITIONAL (fit against full exclusion curves pending)**. This is a quantitative prediction, not a parameter fit.

### Comparison with Planck Scale — Fine-Tuning Assessment

**Planck length**: $\ell_P \approx 1.6 \times 10^{-35} \, \mathrm{m}$.

**Ratio**: 

$$\frac{r_{\mathrm{fiber}}^*}{\ell_P} \approx \frac{21.8 \times 10^{-6}}{1.6 \times 10^{-35}} \approx 1.4\times 10^{30} \sim 10^{30}.$$

In logarithmic terms, the fiber radius is *about 30 orders of magnitude* larger than the Planck length. This is a large hierarchy in the classical sense: the fundamental scale ($\ell_P$) is vastly smaller than the predicted fiber scale.

**Status: HIGHLY UNNATURAL by conventional standards**. However, this comparison applies only if one assumes the 5D Planck scale sets the fundamental short-distance cutoff. In the coherence-frame axioms (§ 3.2), the scale separation emerges from the *geometry itself* (Hopf structure, not input); whether this legitimately avoids \"fine-tuning\" is an open question deferred to the Discussion.

---

## § 5.3.5: Open Issues and Deferred Problems

### 5.3.5.1 Radion Stabilization

The fiber radius $r_{\mathrm{fiber}}$ appears as a dynamical scalar field ("radion") in the 4D effective action. SC3 predicts a *value*, $r^* \approx 21.8 \, \mu\mathrm{m}$ (circumference $L^* \approx 137 \, \mu\mathrm{m}$), but provides **no mechanism for stabilizing** it.

**Status: MISSING**. A complete scenario requires:

- A potential $V_{\mathrm{eff}}(r_{\mathrm{fiber}})$ with a minimum at $r^*$.
- Computation of the stabilization scale (warp factor modulus, higher-dimensional fluxes, etc.).
- Proof that the minimum is stable against small perturbations.

None of this is provided here. Stabilization is a **standard problem in dimensional reduction** (cf. Randall-Sundrum, string theory moduli stabilization) but is NOT solved in the present paper.

**Corrected radion kinetic normalization (Spike 11 audit):** The radion kinetic term $Z_L$ in the 4D effective action was corrected from $A^2$-weighted (Spike 10) to $A^3$-weighted:

$$Z_L^{\mathrm{SC2}} = 2M_5^3 \mu \left(1 - e^{-3\mu L_*}\right) \quad \text{(Eq. 5.3.5.1a — corrected)}$$

This represents a factor $\sim 3.65\times$ increase in $Z_L$ relative to the Spike 10 value. The consequences for radion phenomenology are:

- **Radion mass** ($m_\phi \propto Z_L^{-1/2}$): decreases by $\sim 48\%$ relative to the Spike 10 estimate. A lighter radion is *harder* to stabilize, as the potential must be correspondingly shallower.
- **Radion Yukawa range** ($\lambda_\phi \propto m_\phi^{-1}$): increases by $\sim 91\%$. The radion's fifth-force contribution extends to larger distances, potentially affecting ISL bounds at scales comparable to $r_{\mathrm{fiber}}^*$.
- **Radion-matter coupling** ($\kappa_\mathrm{rad} = \frac{3}{2}\mu^2$): **unchanged** (independent of $Z_L$).

The RS1 cross-check gives $Z_L^{\mathrm{RS1}} = \frac{3}{2}M_5^3 \mu (1 - e^{-4\mu L_*})$ with $A^4$ weight, consistent with Goldberger and Wise (PRD 60, 107505).

**Impact on SC3 scale prediction:** The Casimir energy formula (Eq. 5.3.1) and the fiber radius prediction $r^* \approx 21.8\,\mu\mathrm{m}$ are **independent of $Z_L$** — they depend only on the field content ($N_B, N_F$) and the vacuum energy density. However, the lighter radion mass means that the stabilization mechanism (when constructed) must account for a broader radion potential well. This is a quantitative shift, not a qualitative one.

**Status: VERIFIED** (Z_L correction). **MISSING** (stabilization mechanism).

### 5.3.5.2 Post-Transition Field Content

The branch screening (§ 5.3.3) assumes one of the PASSING sectors ($N_F > 8N_B/7$) is realized. **Which sector?** This is determined by Paper 3, Axiom B — the phase transition from the pre-transition geometric phase to the post-transition field-theoretic phase.

**Status: CONTINGENT (depends on Paper 3)**. If Paper 3 predicts a post-transition sector that FAILS the SC3 sign condition, SC3 FAILS entirely. The present work cannot stand alone.

### 5.3.5.3 Atiyah-Singer Topological Index

$S^3$ is odd-dimensional. The Atiyah-Singer chiral Dirac index theorem, applied to spinors on $S^3$, yields

$$\mathrm{index}(D) = 0.$$

This means **there is no topological obstruction** to having $N_F < 3$. In fact, $N_F = 0$ (purely bosonic) is topologically consistent; it simply fails SC3 (sign condition). By contrast, in even dimensions, the index is non-trivial and restricts fermion content.

**Status: VERIFIED (index calculation)**. **Implication**: The sign condition ($f > 0$) is the ONLY constraint on $N_F$; no topological protection exists.

### 5.3.5.4 Warp/Fiber Decoupling Assumption

The Casimir energy formula, Eq. 5.3.1, assumes that the Hopf fiber $S^1$ (parameterized by $\psi$) is **independent** of the radial warp direction $r$. In other words, the mode expansion on $S^1$ decouples from the geometry in the $(z, r, \theta^i)$ directions.

**Status: UNTESTED (full coupled analysis)**. A rigorous treatment requires solving the coupled wave equations for the entire 5D background, not a factorized product geometry. Corrections from warp-fiber coupling likely modify the numerical coefficient in Eq. 5.3.1 and could affect the scale $r^*$ by factors of order unity.

### 5.3.5.5 Higher-Order Corrections

The Casimir energy derived here is a **tree-level, zero-temperature calculation** in free-field QFT. Corrections include:

- **Massive mode contributions**: If any field in the post-transition sector is massive, the Casimir energy shifts.
- **Loop corrections**: Quantum loops modify the effective potential.
- **Finite-temperature effects**: At cosmic scales, "temperature" is set by the Hubble parameter; its contribution is non-negligible in some models.
- **Cubic and higher interactions**: The present calculation assumes free massless fields.

**Status: UNKNOWN**. None of these are computed.

---

## § 5.3.6: SC3 Verdict — Status and Posture

### Summary of Findings

| Condition | Status | Notes |
|-----------|--------|-------|
| **Sign condition ($f > 0$)** | PASS (conditional) | Satisfied in SM sector ($f = 54$), GUT sector, and minimal fermionic sector. SUSY sectors fail. |
| **Scale prediction ($r^*$)** | CONDITIONAL (schematic) | Gives $r^* \approx 21.8 \, \mu\mathrm{m}$ ($L^* \approx 137 \, \mu\mathrm{m}$) for SM; compare to full ISL exclusion curves and allow for $O(1)$ shifts from warp-fiber coupling corrections. |
| **Classical closure** | FAIL | Classical geometry alone gives $\Lambda_{\mathrm{eff}} = 0$. Quantum correction required. |
| **Stabilization** | MISSING | No potential with minimum at $r^*$; radion stabilization unaddressed. |
| **Post-transition content** | CONTINGENT | Depends on Paper 3 outcome (Axiom B). |
| **Atiyah-Singer constraint** | NONE | No topological obstruction; $N_F$ is unrestricted by index theorem. |
| **Decoupling assumption** | UNTESTED | Warp-fiber coupling not computed; corrections unknown. |

### Claim Posture: OPEN (Staged)

**SC3 is NOT closed.** The present section establishes SC3 as a **conditional candidate mechanism** for the cosmological constant:

1. **Necessary condition satisfied**: If the post-transition sector has $N_F > 8N_B/7$, then Casimir energy produces $\rho > 0$, and the magnitude can be matched to $\Lambda_{\mathrm{obs}}$.

2. **Quantitative prediction in place**: For the SM sector, $r^* \approx 21.8 \, \mu\mathrm{m}$ (circumference $L^* \approx 137 \, \mu\mathrm{m}$), a macroscopic scale accessible to future experiments. This is a **falsifiable prediction**, not a parameter fit.

3. **Sufficient condition NOT established**: 
   - Stabilization mechanism is missing.
   - Post-transition sector is not derived here.
   - Warp/fiber coupling is unchecked.
   - Large hierarchy (~30 orders of magnitude relative to $\ell_P$) is not resolved.

### Staged Closure Path

Full closure of SC3 requires (in order):

1. **Paper 3 completion**: Derive the post-transition field content via Axiom B phase transition. Verify that $N_F > 8N_B/7$ holds.

2. **Radion stabilization**: Construct a potential $V_{\mathrm{eff}}(r_{\mathrm{fiber}})$ (via flux, non-perturbative effects, or other mechanism) with a minimum at $r^*$. Demonstrate stability.

3. **Decoupling verification**: Solve the coupled 5D wave equations for the Hopf fiber in the warp background. Quantify corrections to Eq. 5.3.1.

4. **Experimental tests**: Search for deviations from Newton's law at scales $\lesssim \mathcal{O}(10^1) \, \mu\mathrm{m}$ (ISL improvements or graviton resonance signatures at the fiber radius scale).

**Until these are complete, SC3 remains a necessary but conditional candidate.**

---

## § 5.3.7: Connection to SC1 and SC2

Recall:

- **SC1** (§ 5.1): Requires $A(r, z) \sim z \cdot f(r)$ at late times to achieve late-time acceleration.
- **SC2** (§ 5.2): Requires $f(r)$ to create a normalizable graviton bound state (spectral support for isotropic perturbations).
- **SC3**: Requires Casimir energy in the post-transition sector to match $\Lambda_{\mathrm{obs}}$.

These three conditions are **mutually constraining**:

- SC1 and SC2 determine the *functional form* of the warp metric.
- SC3 determines the *scale* of the fiber and (contingently) the field content.
- The field content (from SC3 screening) constrains the phase transition outcome (Paper 3, Axiom B).

In principle, if Paper 3 predicts a post-transition sector that FAILS the SC3 sign condition, then SC1 and SC2 cannot both hold in a self-consistent manner. This is a **consistency check** on the entire framework, not resolved until all three papers are complete.

---

## § 5.3.8: Paper 3 Interface Hooks (SC3 closure + phase-gated interpretation)
The following hooks define what Paper 3 must provide so that SC3 can move from "conditional candidate" to staged closure.
1. **P3-SC3-1: Realized post-transition branch**  
   Specify the realized field-content branch and explicit $(N_B,N_F)$ counting after Axiom B. This determines whether the SC3 sign condition $f>0$ is satisfied by derivation rather than by assumption.
2. **P3-SC3-2: Phase-transition gate for effective formulas**  
   Provide a transition scale/redshift that marks where 4D effective formulas are valid versus where 5D-coupled corrections are required. This prevents phase-mixing in downstream phenomenology.
3. **P3-SC3-3: High-z correction channel to observables**  
   Provide the projection rule for phase-coupling corrections entering high-redshift kernels/observables, with sign conventions fixed so additive versus partially cancelling effects are unambiguous.
4. **P3-SC3-4: Stabilization link to Axiom B dynamics**  
   Provide a concrete stabilization pathway connecting post-transition dynamics to a radion potential with a controlled minimum at the SC3 target scale.
**Status**: INTERFACE-CONTRACT ONLY. These hooks are forward dependencies and are not asserted as completed in this section.

## References (Internal)

- § 3.2: Coherence-frame axioms and derived Hopf structure.
- § 3.4 (spine): Classical Einstein tensor; proof that $\Lambda_{\mathrm{classical}} = 0$.
- § 3.7 (spine): Casimir energy computation (zeta-function regularization).
- § 4.0: Canonical KK-Cone metric.
- § 5.1: SC1 condition and late-time acceleration.
- § 5.2: SC2 condition and graviton bound state.
- **Paper 3, Axiom B**: Phase transition dynamics (not yet written).

---

## Notation and Conventions

| Symbol | Meaning |
|--------|---------|
| $\Lambda_{\mathrm{obs}}$ | Observed cosmological constant; $\approx 1.1 \times 10^{-52} \, \mathrm{m}^{-2}$ or $5.32 \times 10^{-10} \, \mathrm{J/m^3}$ |
| $r_{\mathrm{fiber}}$ | Geometric radius of Hopf fiber $S^1$ (circumference $L = 2\pi r_{\mathrm{fiber}}$); dynamical (radion) in 4D effective theory |
| $\psi$ | Angular coordinate on Hopf fiber; period $2\pi$ |
| $N_B$ | Massless real bosonic d.o.f. (counted with periodic BC in Casimir formula) |
| $N_F$ | Massless Weyl fermionic d.o.f. (counted with antiperiodic BC) |
| $f$ | Sign factor; $f := 7N_F/8 - N_B$ |
| $\rho_{\mathrm{Casimir}}$ | Vacuum energy density on Hopf fiber |
| $G_4$ | 4D Newton constant |

---

**End of § 5.3**

---

## Metadata and Status Log

**Last Updated**: 2026-03-09
**Status**: **DRAFT** — Revised per Warp formal review: B1 (r/L 2π factor corrected, r*≈22μm), N1-N2 (f arithmetic fixed), N3 (massless field scale caveat added), N4 (LaTeX escaping cleaned). Z_L A³ correction (§5.3.5.1) from prior session.
**Next Steps**:
1. Cross-check numerical factor in Eq. 5.3.1 against spine § 3.7 zeta-function tables.
2. Verify ISL bound comparison with Lee et al. 2020 and Chiaverini et al. 2006.
3. Add fine-tuning discussion to main text or Discussion section.
4. Link to Paper 3 (Axiom B phase transition) once Paper 3 structure is finalized.
5. Quantify impact of lighter radion (Z_L correction) on ISL bounds at r ~ 22 μm.
