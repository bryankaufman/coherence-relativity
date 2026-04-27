# Coherence Relativity IIB — KCR-Cone Evaluation

*Companion paper to Coherence Relativity IIA.*
*Status: Working manuscript — structure pass pending*

---

# §1 Introduction

Notation and conventions throughout this paper follow Paper 2A §1.6. The cross-paper symbol
correspondence (Table 1), object-type conventions (Table 2), and causal/ontological direction
notation (Table 3) are not reproduced here. KCR-Cone-specific symbols are defined at first use
in the text; all others refer to Paper 2A.

This paper evaluates the abstract framework of Paper 2A on the first physically motivated
geometry arising from derived compactification: the KCR-Cone, whose warp factor
$A(r) = \cos(\sqrt{2}\,r)$ is derived — not fitted — from the Fubini-Study Laplacian eigenvalue
$k^2 = 2$, a topological invariant of $\mathbb{CP}^1$. The paper passes two self-consistency
tests (SC1, SC2), conditionally establishes a third (SC3), resolves the norm convention
ambiguity identified in Paper 2A §4.2, and partially verifies the holographic conjecture.

---

<!-- ===== SECTION: §5.1-5.2 SC1 and SC2 ===== -->
<!-- Source: sections/drafts/paper2_section_5.1_5.2_SC1_SC2_DRAFT.md -->

# §5 Self-Consistency Conditions: SC1 (Flatness) and SC2 (Gravity Localization)

## Overview

Having established in §4 the canonical KCR-Cone metric with Hopf-fibered internal space, we now examine what it means for this geometry to be **self-consistent** with observed physics. This section develops two of the three self-consistency conditions that the warp factor $A(r,z)$ must satisfy simultaneously:

1. **SC1 (Flatness Condition):** The observed universe is spatially flat ($\Omega_k \to 0$) as measured at late cosmological times.
2. **SC2 (Gravity Localization):** Standard 4D Newton's law holds at accessible scales, with no detectable fifth force.

These conditions do not determine $A(r,z)$ uniquely; rather, they define a **class** of admissible warp profiles. The combined system SC1 + SC2 further constrains this class, but does not close it completely—a third condition, SC3 (effective cosmological constant), is required. The present section establishes the mathematical structure of SC1 and SC2 and shows how their interplay restricts the radial profile $f(r)$ in the asymptotic form $A \sim z \cdot f(r)$.

---

### Notation Convention: Warp Factor

In §4, the KCR-Cone metric was written using the Randall–Sundrum convention $e^{2\mathcal{A}(r,z)}$, where $\mathcal{A}$ is the warp *exponent*. Beginning in this section and continuing through §7–§8, we adopt a simplified notation in which $A(r,z)$ denotes the warp *factor* (scale factor) directly:

$$
A(r,z) \;\equiv\; e^{\mathcal{A}(r,z)}, \qquad \text{so that} \quad e^{2\mathcal{A}} = A^2.
$$

For the explicit profile used throughout: $\mathcal{A}(r) = -\mu r$, giving $A(r) = e^{-\mu r}$, so the metric coefficient $e^{-2\mu r} = A(r)^2$.

This convention ensures:

- $A = 1$ at the brane ($r = 0$): no warping.
- $A \to 0$ as $r \to \infty$: maximal warping in the deep bulk.
- The 5D metric takes the compact form $\mathrm{d}s^2_{(5)} = -\mathrm{d}z^2 + \mathrm{d}r^2 + A(r,z)^2 \gamma_{ij} \mathrm{d}\theta^i \mathrm{d}\theta^j$.

All subsequent references to "the warp factor $A$" denote the scale factor (not its logarithm).

---

## §5.1 The Flatness Condition (SC1)

### §5.1.1 Physical Requirement

Observations from the cosmic microwave background (CMB) and baryon acoustic oscillations (BAO) constrain the spatial curvature parameter to extraordinary precision:

$$
\Omega_k = -\frac{k_{\text{eff}}}{H_0^2} = 0.0005 \pm 0.0019 \quad \text{(Planck 2018)}
$$

In the limit of high precision, we take $\Omega_k \to 0$, meaning that the spatial sections of the universe are **flat** to observable accuracy. On the KCR-Cone, the brane observers at fixed $r = r_{\text{brane}}$ measure curvature through the intrinsic metric of constant-$z$ slices. For the universe to appear flat to these observers, the effective spatial curvature must vanish.

### §5.1.2 Derivation of the Effective Curvature

The 5D metric from §4 is:

$$
\mathrm{d}s^2_{(5)} = -\mathrm{d}z^2 + \mathrm{d}r^2 + A(r,z)^2 \, \gamma_{ij} \, \mathrm{d}\theta^i \mathrm{d}\theta^j
\tag{5.1.1}
$$

At fixed $r = r_{\text{brane}}$, the induced brane metric is:

$$
\mathrm{d}s^2_{\text{(brane)}} = -\mathrm{d}z^2 + A(r_{\text{brane}}, z)^2 \, \gamma_{ij} \, \mathrm{d}\theta^i \mathrm{d}\theta^j
\tag{5.1.2}
$$

The constant-$z$ spatial sections have metric:

$$
\mathrm{d}\sigma^2 = A(r_{\text{brane}}, z)^2 \, \gamma_{ij} \, \mathrm{d}\theta^i \mathrm{d}\theta^j
\tag{5.1.3}
$$

The unit round metric $\gamma_{ij}$ on $S^3$ has constant intrinsic curvature $k_{S^3} = 1$ (in the units where the 3-sphere has radius 1). When scaled by the warp factor squared, the curvature scales inversely as the square of the scale factor. The Ricci scalar of a 3D space with metric $A^2 \gamma_{ij}$ is:

$$
R^{(3)} = \frac{1}{A^2} R^{(3)}_{\gamma} = \frac{6}{A^2}
$$

so the scalar curvature per unit area is effectively $k_{\text{eff}} \sim 1/A^2$ from this term alone. However, the $z$-dependence of $A$ introduces a second curvature component: the warping of the slices in the $z$-direction acts like a negative-curvature deformation. The complete expression, derived from the Gauss-Codazzi equations, is:

$$
k_{\text{eff}} = \frac{k_{S^3}}{A(r,z)^2} - \left(\frac{\partial_z A}{A}\right)^2
\tag{5.1.4}
$$

**Interpretation:** The first term, $k_{S^3}/A^2$, represents the intrinsic curvature of the internal sphere, suppressed by the inverse square of the warp factor. The second term, $-(\partial_z A / A)^2$, is negative and represents the curvature deficit from the rapid expansion or contraction in the $z$-direction. For the spatial sections to be flat, these two contributions must cancel.

### §5.1.3 Flatness Condition and Asymptotic Profile

For flatness, we require:

$$
k_{\text{eff}} \to 0 \quad \text{as } z \to \infty
\tag{5.1.5}
$$

At late times, the universe becomes close to a de Sitter or matter-dominated FRW model. In these limits, the Hubble parameter $H(z) := \partial_z A / A$ becomes small and slowly varying. Let us assume an asymptotic form:

$$
A(r,z) \sim z \cdot f(r) \quad \text{as } z \to \infty
\tag{5.1.6}
$$

where $f(r)$ is a profile function that does not depend on $z$ at late times. Then:

$$
\frac{\partial_z A}{A} = \frac{\partial_z(z f(r))}{z f(r)} = \frac{f(r)}{z f(r)} = \frac{1}{z} \to 0 \quad \text{as } z \to \infty
$$

so the second term in Eq. (5.1.4) vanishes. The first term gives:

$$
k_{\text{eff}} \to \frac{k_{S^3}}{(z f(r))^2} \sim \frac{1}{z^2} \to 0 \quad \text{as } z \to \infty
$$

Thus, **the asymptotic form $A \sim z \cdot f(r)$ is sufficient to enforce flatness at late times**, provided $f(r)$ does not blow up faster than logarithmically in $z$.

**Normalization:** At the observer brane $r = r_{\text{brane}}$, we set $f(r_{\text{brane}}) = 1$ so that:

$$
A(r_{\text{brane}}, z) \sim z \quad \text{as } z \to \infty
\tag{5.1.7}
$$

This is the light-cone normalization: brane observers at fixed $r_{\text{brane}}$ see the warp factor approach the pure light-cone form at late times, recovering approximately flat spacetime geometry.

### §5.1.4 Pure Light-Cone Limit: Explicit Verification

The simplest case is the pure light-cone metric $A = z$ everywhere:

$$
\mathrm{d}s^2 = -\mathrm{d}z^2 + \mathrm{d}r^2 + z^2 \, \gamma_{ij} \, \mathrm{d}\theta^i \mathrm{d}\theta^j
\tag{5.1.8}
$$

Then:
- $\partial_z A / A = 1/z \to 0$ as $z \to \infty$
- $k_{\text{eff}} = 1/z^2 - 1/z^2 = 0$ **exactly**

**Result (example):** The pure light-cone is an explicit profile that satisfies SC1 exactly for all $z > 0$. This is consistent with the fact that each constant-$r$ slice is conformal to Minkowski × $S^3$, which has zero curvature in 4D up to conformal factors.

### §5.1.5 What SC1 Constrains (and What It Does Not)

**What SC1 determines:**
- The late-time asymptotic form of $A(r,z)$ must be $A \sim z \cdot f(r)$ for any function $f(r)$.
- The function $f(r)$ must satisfy $f(r_{\text{brane}}) = 1$ to match observations.

**What SC1 does not determine:**
- The form of $f(r)$ at other radii (e.g., off-brane).
- Whether $f(r)$ increases, decreases, or oscillates as $r$ moves away from $r_{\text{brane}}$.
- The early-time (small $z$) behavior of $A(r,z)$, which may deviate significantly from the light-cone form near the Planck scale.
- The functional form of $A(r,z)$ at intermediate times; only the late-time behavior is constrained.

**Key insight:** SC1 defines a **necessary condition** that any physically realistic $A(r,z)$ must satisfy. It rules out, for example, any warp profile where the internal space $S^3$ remains finite in "proper size" at late times. However, SC1 is **not sufficient** to determine a unique metric; many warp profiles consistent with different choices of $f(r)$ will satisfy SC1. Additional constraints from SC2 and SC3 are required to further restrict $f(r)$.

---

## §5.2 The Gravity Localization Condition (SC2)

### §5.2.1 Physical Requirement

Experiments searching for deviations from Newton's law at submillimeter scales (fifth-force experiments, Yukawa-potential tests) place stringent limits on Yukawa-like corrections to gravity. A useful benchmark scale is the tens-of-microns regime:

$$
\\lambda_{\\text{test}} \\sim 44 \\, \\mu\\mathrm{m} \\quad (\\alpha \\sim 1\\ \\text{benchmark})
\\tag{5.2.1}
$$

In the context of extra dimensions, such constraints translate to bounds on the localization scale of gravity to the brane. If gravity "leaked" into the bulk, the 4D gravitational potential would be modified at sub-millimeter scales. Observations show that standard 4D gravity holds down to submicron scales, implying that the graviton must be tightly bound to the brane.

**SC2 requirement:** The massless graviton (the 4D graviton zero mode) must be normalizable in the radial direction, with KK corrections suppressed at currently tested scales (order tens of microns for order-one Yukawa strength). This ensures that the effective gravitational constant $G_4$ measured on the brane matches the known value, and no significant modifications to Newton's law appear at observed scales.

### §5.2.2 The Schrödinger Equation for Graviton Localization

In the KK decomposition of the 5D graviton in the presence of the warp factor, the radial profile of the zero mode satisfies a Schrödinger-like equation. Working in the Gaussian-normal frame (where $r$ is the normal coordinate to the brane), the condition for a normalizable graviton wavefunction $\psi(r)$ in the $r$-direction is:

$$
\left[ -\frac{\mathrm{d}^2}{\mathrm{d}r^2} + V_{\text{grav}}(r) \right] \psi(r) = 0
\tag{5.2.2}
$$

where the potential is:

$$
V_{\text{grav}}(r) = \frac{3}{2} \partial_r^2 \ln A + \frac{3}{4} (\partial_r \ln A)^2
\tag{5.2.3}
$$

**Interpretation:** The factor of 3 appears because the internal space is 3-dimensional ($S^3$ in Hopf parameterization). The first term is proportional to the curvature of the logarithm of the warp factor, and the second is the squared gradient. Together, they form an effective potential that arises from the kinetic energy of fluctuations in the warp direction.

### §5.2.3 Localization Condition

A normalizable bound state $\psi(r)$ decaying as $r \to \infty$ requires:

1. $\psi(r)$ is finite and nonzero at $r = r_{\text{brane}}$ (the brane location).
2. $\psi(r) \to 0$ as $r \to \infty$ (normalizability in the bulk).
3. The potential $V_{\text{grav}}(r)$ has a minimum near $r = r_{\text{brane}}$ and grows monotonically as $|r - r_{\text{brane}}| \to \infty$.

Condition 3 ensures that the wavefunction is trapped in a potential well centered on the brane, analogous to the quantum-mechanical confinement of a particle in a box.

**Equivalently:** The potential $V_{\text{grav}}(r)$ must be positive-definite for $r \neq r_{\text{brane}}$ and have a zero or negative dip near $r = r_{\text{brane}}$. The boundary of the potential well, where $V(r) = 0$, defines an effective "edge" beyond which graviton fluctuations are evanescent and exponentially suppressed.

### §5.2.4 Example: Exponential Warp

To make SC2 concrete, consider the trial ansatz:

$$
A(r,z) = z \cdot e^{-\mu |r|}
\tag{5.2.4}
$$

where $\mu > 0$ is the localization scale (inverse length). This separates cleanly into a late-time light-cone piece ($z$) and an exponential radial warp ($e^{-\mu|r|}$).

**Computing the potential:**

$$
\ln A = \ln z - \mu |r|
$$

$$
\partial_r \ln A = -\mu \, \mathrm{sgn}(r)
$$

where $\mathrm{sgn}(r)$ is the sign function. For $r > 0$:

$$
\partial_r \ln A = -\mu
$$

$$
\\partial_r^2 \\ln A = -2\\mu\\,\\delta(r)
$$

Thus:

$$
V_{\\text{grav}}(r) = -3\\mu\\,\\delta(r) + \\frac{3\\mu^2}{4}
\\tag{5.2.5}
$$

**Result:** The potential consists of an attractive brane-localized delta well plus a positive bulk plateau. This is the standard localization structure: a normalizable zero mode is trapped near the brane and decays into the bulk.

**Normalizability check:**

$$
\int_0^\infty \mathrm{d}r \, |\psi(r)|^2 \sim \int_0^\infty \mathrm{d}r \, e^{-2\kappa r} < \infty \quad \text{for } \kappa > 0
$$

The integral converges, confirming that a normalizable bound state exists. The confinement length scale is $\ell_* = 1/\mu = \mu^{-1}$, which measures how far the graviton wavefunction extends from the brane into the bulk.

### §5.2.5 Recovery of 4D Newton's Law

At scales much smaller than the localization length, $\ell \ll \mu^{-1}$, the graviton does not sense the extra dimension—it behaves as a 4D particle. The effective 4D Newtonian potential at distances $\ell < \mu^{-1}$ is:

$$
V_{\text{Newton}}(\ell) = -\frac{G_4 M}{\ell} + O\left(\left(\frac{\ell}{\mu^{-1}}\right)^2\right)
\tag{5.2.6}
$$

The first term is the standard Newtonian result. The second term represents KK corrections—modifications due to the excitation of massive KCR graviton modes in the bulk. These corrections are suppressed as $(\ell/\mu^{-1})^2$, which for $\ell \ll \mu^{-1}$ is very small.

**Observational constraint (benchmark form):** At distances where fifth-force experiments are most sensitive (tens of microns), KK corrections must remain below current exclusion limits.

For order-one Yukawa strength, this is commonly summarized as:

$$
\\mu^{-1} \\lesssim \\mathcal{O}(10\\text{–}40)\\,\\mu\\mathrm{m}
\\tag{5.2.7}
$$

(equivalently, $\\mu \\gtrsim \\mathcal{O}(10^{-2})\\,\\mu\\mathrm{m}^{-1}$). The exact numerical bound is model-dependent through the Yukawa amplitude and should be extracted from a full exclusion-curve fit.

### §5.2.6 What SC2 Constrains (and What It Does Not)

**What SC2 determines:**
- The warp profile $f(r)$ must create an effective potential well that traps the graviton zero mode. For the exponential form $f(r) = e^{-\\mu|r|}$, the parameter $\\mu$ is constrained by fifth-force tests at the tens-of-microns scale (for order-one Yukawa strength).
- The existence of a mass gap: the first excited graviton KCR mode has a mass $m_1 \sim \mu$, which suppresses its production at low energies.

**What SC2 does not determine:**
- The specific functional form of $f(r)$; while $f(r) = e^{-\mu|r|}$ is a concrete example, other localization profiles (Gaussian, power-law with exponent $> 1$, etc.) can also satisfy SC2.
- The relationship between $\mu$ and other parameters of the model (e.g., the early-time geometry, the Planck scale, the size of the internal space).
- Whether SC2 is compatible with SC1 and SC3 simultaneously—this requires checking the coupled system.

**Key insight:** SC2 is a **stability and recovery condition**. It ensures that the warp factor does not allow gravity to spread into the bulk, and it guarantees that 4D gravity is recovered at scales below the localization length. Like SC1, it is **necessary but not sufficient** to uniquely determine the metric.

---

## §5.2.7 The Combined SC1 + SC2 System

### §5.2.7.1 Coupled Constraints on $f(r)$

The two conditions SC1 and SC2 impose a coupled system of constraints:

**From SC1:**
$$
A(r,z) \sim z \cdot f(r) \quad \text{at late times} \quad \Rightarrow \quad f(r_{\text{brane}}) = 1
\\tag{5.2.7.1}
$$

**From SC2:**
$$
V_{\text{grav}}(r) = \frac{3}{2} \partial_r^2 \ln f(r) + \frac{3}{4} (\partial_r \ln f(r))^2 > 0 \quad \text{(for } r \neq r_{\text{brane}}\text{)}
\\tag{5.2.7.2}
$$

must support a normalizable bound state at $r = r_{\text{brane}}$.

**Interpretation:** Equation (5.2.1.1) fixes the value of $f$ at the brane by the flatness requirement. Equation (5.2.1.2) constrains its **shape** (derivatives) to create a confining potential. These are not independent—the profile that satisfies (5.2.1.2) must be such that it approaches 1 at $r = r_{\text{brane}}$ without violating the localization condition.

### §5.2.7.2 Restrictions on the Warp Profile

For the exponential ansatz $f(r) = e^{-\mu|r-r_{\text{brane}}|}$ (placing the brane at $r = r_{\text{brane}}$ for simplicity):

$$
A(r,z) = z \cdot e^{-\mu|r-r_{\text{brane}}|}
\\tag{5.2.7.3}
$$

**SC1 check:**
- At $r = r_{\text{brane}}$: $A = z$ ✓
- As $z \to \infty$: $\partial_z A / A = 1/z \to 0$ ✓
- Flatness: $k_{\text{eff}} \to 0$ ✓

**SC2 check:**
- Away from the brane: $V_{\text{grav}} = \frac{3\mu^2}{4} > 0$ ✓
- Normalizable zero mode exists ✓
- 4D Newton's law recovered for $\ell \ll \mu^{-1}$ ✓

**Conclusion:** The exponential warp simultaneously satisfies the stated forms of SC1 and SC2. However, this alone does not prove that it is the **self-consistent** solution, because:

1. Many other profiles also satisfy SC1 and SC2 (e.g., $f(r) = 1 + (e^{-\mu|r|} - 1)$, which is a smoothed exponential).
2. The combined system SC1 + SC2 + SC3 is **over-determined** (three equations for one unknown function $f(r)$), generically having no solution without fine-tuning.

### §5.2.7.3 The Pure Light-Cone Does Not Satisfy SC2

An important negative result: the pure light-cone metric $A = z$ (i.e., $f(r) \equiv 1$) **fails SC2**.

**Proof:**

$$
f(r) = 1 \quad \Rightarrow \quad \partial_r \ln f = 0, \quad \partial_r^2 \ln f = 0
$$

$$
V_{\text{grav}}(r) = \frac{3}{2} \cdot 0 + \frac{3}{4} \cdot 0 = 0
\\tag{5.2.7.4}
$$

The potential vanishes everywhere. This means the radial direction is completely transparent to the graviton; there is no confining potential well. The graviton wavefunction is a plane wave in the radial direction, which does not decay at infinity. Hence:

$$
\int_0^\infty \mathrm{d}r \, |\psi(r)|^2 = \infty
$$

The zero mode is **not normalizable**, and 4D gravity does not localize on the brane.

**Physical interpretation:** Without any radial warp in $f(r)$, the extra dimension remains accessible at all scales. The geometry is too "open"—observers on the brane would detect a modified gravitational law, with effects growing at large distances due to the leakage of graviton amplitude into the bulk. This contradicts observations.

**Conclusion:** **Warping in the radial direction is essential** for gravity localization. The pure 5D cone is topologically consistent (it realizes the Hopf structure) but dynamically inconsistent with observation. A nontrivial warp profile $f(r) \neq 1$ is required to satisfy SC2.

### §5.2.7.4 Statement of the Combined System

The self-consistency conditions SC1 and SC2 together imply:

$$
\boxed{
\begin{align}
\text{(SC1)} & : \quad A(r,z) \sim z \cdot f(r) \text{ as } z \to \infty, \quad f(r_{\text{brane}}) = 1 \\
\text{(SC2)} & : \quad f(r) \text{ creates a normalizable graviton bound state at } r = r_{\text{brane}} \\
\text{Combination} & : \quad f(r) \text{ must provide a confining profile for the graviton (for example, a monotonically decaying function from } f(r_{\text{brane}}) = 1\text{)}
\end{align}
}
\\tag{5.2.7.5}
$$

This rules out:
- The pure light-cone ($f \equiv 1$).
- Profiles that increase from the brane ($f(r) > 1$ for all $r > r_{\text{brane}}$), which would create a repulsive barrier instead of an attractive well.
- Non-monotonic or oscillating profiles that do not confine the graviton.

The **class of admissible profiles** includes:
- Exponential: $f(r) = e^{-\mu|r - r_{\text{brane}}|}$
- Gaussian: $f(r) = e^{-(r-r_{\text{brane}})^2/\ell_*^2}$
- Power-law: $f(r) = [1 + (r/r_*)^n]^{-1}$ for $n > 1$

Each choice of $f(r)$ within this class represents a different model of the bulk geometry. Which one is actually realized depends on the full self-consistency system including SC3.

---

## §5.2.8 Quantitative SC2 Results for the Non-Conformal Metric

The preceding subsections establish the *structure* of gravity localization. We now present the *quantitative* results, derived from first principles for the SC2 metric with unwarped time.

### §5.2.8.1 The SC2 Metric Convention

The SC2 metric takes the non-conformal form:

$$
\mathrm{d}s^2 = -\mathrm{d}z^2 + A(r)^2 \, \gamma_{ij} \, \mathrm{d}\theta^i \mathrm{d}\theta^j + \mathrm{d}r^2
\tag{5.2.8.1}
$$

with $A(r) = e^{-\mu r}$ for $r \in [0, L_*]$. Unlike the Randall-Sundrum conformal metric ($\mathrm{d}s^2 = A^2(-\mathrm{d}z^2 + \mathrm{d}x^2) + \mathrm{d}r^2$), the time direction is **not warped**: the lapse function is $n(r) = 1$, while the spatial scale factor is $a(r) = A(r)$.

⚠️ **Convention note:** The choice $n(r) = 1$ is adopted as an ansatz within the one-parameter family $n(r) = C_1 + C_2 e^{-\mu r}$ satisfying the compatibility condition $n'' + \mu n' = 0$. This choice does not follow from the vacuum 5D Einstein equations with a simple cosmological constant (which uniquely select the conformal case $n = a$), and requires anisotropic bulk matter for exact self-consistency. The ansatz is motivated by the physical requirement of universal decoherence rates and is treated as one frame of reference within the allowed family. See the SC2 Convention Lock document for alternative formulations and retrenchment criteria.

### §5.2.8.2 Graviton Zero-Mode Normalization

The effective 4D Planck mass is determined by the Gauss-Codazzi KCR reduction:

$$
M_{\text{Pl}}^2 = M_5^3 \int_0^{L_*} n(r) \cdot a(r) \, \mathrm{d}r = M_5^3 \int_0^{L_*} A(r) \, \mathrm{d}r
\tag{5.2.8.2}
$$

The integrand weight is $n \cdot a = 1 \cdot A = A^1$, giving $p = 1$ (compared to $p = 2$ for the conformal RS1 case where $n = a = A$). The graviton zero-mode profile is $f_0(r) = 1$ (constant), which is universal for any weight function — a consequence of Neumann boundary conditions on the Sturm-Liouville equation $-(W f')' = m^2 W f$.

### §5.2.8.3 Self-Consistent Extra-Dimension Size

The branch-lock condition $M_{\text{Pl}}^2 = R_{\text{DM}} \cdot M_5^3 \cdot \mu^{-1}$ (linking the dark matter ratio to the hierarchy) combined with the normalization integral yields the self-consistency equation:

$$
p = R_{\text{DM}}(1 - e^{-p \mu L_*})
\tag{5.2.8.3}
$$

For $p = 1$ and $R_{\text{DM}} = 5.5$, this gives:

$$
\mu L_* = 0.2007
\tag{5.2.8.4}
$$

This is a *small* value, meaning the extra dimension is only $\sim$20% of a single e-folding. The physical size is $L_* = \mu L_* / \mu \approx 13 \, \mu\mathrm{m}$ for typical $\mu$ values.

### §5.2.8.4 KK Graviton Spectrum and Fifth-Force Bound

The massive KCR graviton modes satisfy the Sturm-Liouville equation:

$$
-(A^3 f')' = m^2 A^3 f
\tag{5.2.8.5}
$$

(with $n = 1$ for SC2). In dimensionless variables $\rho = \mu r$, $\nu = m/\mu$, and $F(\rho) = e^{3\rho/2} f(\rho)$, this becomes:

$$
F'' - F' + \nu^2 F = 0
\tag{5.2.8.6}
$$

with Neumann boundary conditions $F'(0) = \tfrac{3}{2} F(0)$ and $F'(\mu L_*) = \tfrac{3}{2} F(\mu L_*)$. The first excited mode has $\nu_1 = m_1/\mu \approx 15.7$ for $\mu L_* = 0.2$, giving a Yukawa range:

$$
\lambda_1 = \frac{1}{m_1} = \frac{1}{\nu_1 \mu} \approx 4.3 \, \mu\mathrm{m}
\tag{5.2.8.7}
$$

This is well below the Eöt-Wash experimental bound of $\sim 44 \, \mu\mathrm{m}$ for order-one Yukawa strength:

$$
\lambda_1 \approx 4.3 \, \mu\mathrm{m} \ll 44 \, \mu\mathrm{m} \quad \Rightarrow \quad \textbf{H1 PASSES}
\tag{5.2.8.8}
$$

**Physical interpretation:** The non-conformal SC2 metric produces a *smaller* self-consistent $\mu L_*$ than the conformal case would, which pushes the KCR mass gap *higher* and the Yukawa range *shorter*. This is the mechanism by which $p = 1$ (seemingly "less localized" than $p = 2$) actually produces a *stronger* fifth-force suppression. The key is that small $p$ demands small $\mu L_*$ for self-consistency, and small $\mu L_*$ means heavy KCR modes.

### §5.2.8.5 Radion Normalization

The radion kinetic normalization integral is:

$$
Z_L = 6 M_5^3 \mu^2 \int_0^{L_*} n(r) \cdot a(r)^3 \, \mathrm{d}r = 2 M_5^3 \mu \left(1 - e^{-3\mu L_*}\right)
\tag{5.2.8.9}
$$

The weight is $n \cdot a^3 = 1 \cdot A^3 = A^3$ (not $A^2$ as would follow from a naive conformal generalization; see the Radion Z_L Correction assessment). The RS1 cross-check gives $Z_L^{\text{RS1}} = \tfrac{3}{2} M_5^3 \mu (1 - e^{-4\mu L_*})$, matching the Goldberger-Wise result.

The radion contributes a tier-2 fifth force with Planck-suppressed coupling ($\alpha_{\text{rad}} \sim 10^{-58}$), which is negligible compared to the tier-1 KCR graviton contribution and far below experimental sensitivity.

### §5.2.8.6 Summary of Quantitative SC2 Results

| Quantity | SC2 Value | RS1 Value (cross-check) |
|----------|-----------|------------------------|
| Graviton weight $p$ | 1 | 2 |
| Self-consistent $\mu L_*$ | 0.2007 | (depends on $R_{\text{DM}}$) |
| Extra-dimension size $L_*$ | $\sim 13 \, \mu\mathrm{m}$ | $\sim$ mm-scale |
| First KCR mass $m_1/\mu$ | $\approx 15.7$ | $\approx 3.83$ |
| First KK Yukawa range | $\approx 4.3 \, \mu\mathrm{m}$ | $\sim 100 \, \mu\mathrm{m}$ |
| H1 verdict | **PASS** | (would need checking) |
| Radion weight | $A^3$ | $A^4$ |
| Radion coupling | $\alpha \sim 10^{-58}$ (negligible) | Similar |

---

## §5.2.9 Open Problem: Analytic Derivation of the Self-Consistent $A(r,z)$

### Status

The flatness condition SC1 and the localization condition SC2 are both **structurally clear** and **individually satisfiable**. However, the **simultaneous derivation** of a single $A(r,z)$ that satisfies SC1 and SC2 and also SC3 (to be discussed in §5.3 onward) remains **unsolved analytically**.

### Why the Problem is Hard

1. **SC1 is a constraint on late-time asymptotics** (as $z \to \infty$), specifying the form $A \sim z \cdot f(r)$.
2. **SC2 is a constraint on the radial direction**, requiring $f(r)$ to create a confining potential.
3. **SC3 (effective cosmological constant)** is a global constraint linking the geometry to the observed dark energy, equivalent to an additional differential equation for $A$.

Together, these form an **over-determined system**: three conditions for one function $A(r,z)$ of two variables. Over-determined systems generically have no solution, unless special structure or fine-tuning is present.

### Current Approach: Trial Ansätze vs. Derivation

Until now, the approach has been:

$$
\text{Propose a trial form for } A(r,z) \, \Rightarrow \, \text{Check if SC1, SC2, SC3 are satisfied}
$$

Example: $A = z \cdot e^{-\mu|r|}$ satisfies SC1 and SC2 (Sections 5.1–5.2), but its compatibility with SC3 requires further analysis (§5.3 onward).

⚠️ **Claim posture:** The trial-ansatz approach is **pragmatic but not fundamental**. The exponential warp $A = z \cdot e^{-\mu|r|}$ is a **hypothesis**, not a derived solution. It is justified insofar as it:
- Is consistent with the topological structure of the KCR-Cone.
- Satisfies the necessary conditions SC1 and SC2.
- Admits numerical evaluation to test SC3 compatibility.

It is **not justified** by an a-priori analytical derivation from first principles. The "true" self-consistent $A(r,z)$, if it exists, may have a different form—or may not exist at all for generic parameter values, in which case the KCR-Cone model itself would be ruled out.

### Next Steps

To resolve this, one must:

1. **Numerically solve the SC1–SC3 system** for a family of trial ansätze.
2. **Identify which ansätze (if any) achieve closure** to within acceptable error.
3. **Characterize the remaining parameter freedom** (e.g., how many degrees of freedom remain even after all three conditions are imposed?).
4. **Link to Paper 3 initial conditions** to determine the boundary conditions on $A$ near the Planck scale, which constrains the early-time behavior.

This is deferred to a dedicated numerical study (cf. WARP.md for the computational roadmap).

---

## Summary and Synthesis

**SC1 (Flatness):**
- **Requirement:** $\Omega_k \to 0$ at late times.
- **Implication:** $A(r,z) \sim z \cdot f(r)$ with $f(r_{\text{brane}}) = 1$.
- **Status:** Algebraically closed; satisfied by a **class** of profiles.

**SC2 (Gravity Localization):**
- **Requirement:** 4D Newton's law holds; fifth force suppressed to observational limits.
- **Implication:** $f(r)$ must decay as $r$ increases, creating a confining potential $V_{\text{grav}} > 0$ in the bulk.
- **Status:** Algebraically closed; satisfied by exponential, Gaussian, power-law, and other monotone-decreasing profiles.

**SC1 + SC2 Combined:**
- **Jointly, they eliminate:** the pure light-cone, any increasing profile, any non-monotone profile.
- **Jointly, they leave open:** a one-parameter family of profiles (parameterized by the localization scale $\mu$ or equivalent).
- **Remaining degree of freedom:** The form of $f(r)$ is constrained but not determined. SC3 is needed to pin down the unique solution.

**Claim posture:**
- SC1 and SC2 are **derived from physical observation** and are structurally sound.
- The exponential ansatz $A = z \cdot e^{-\mu|r|}$ is a **trial hypothesis**, not a proven solution.
- **No analytical derivation of the fully self-consistent $A(r,z)$ exists yet.** This is an open problem.
- Solving it requires the full SC1–SC3 system, likely through numerical methods.

---

## References to Earlier Sections

- **§4:** The KCR-Cone metric ansatz and coordinate structure.
- **§3:** Topological derivation of the Hopf fibration and its role in the coherence frame (from Paper 3).
- **§5.3 (upcoming):** SC3, the effective cosmological constant, and the closure of the full system.

---

*Word count: ~4,800 words | Status: DRAFT | Equations: 5.1.1–5.2.7.5 | Claims: SC1 & SC2 structurally closed; SC1+SC2 combined leaves one degree of freedom; full analytical derivation unsolved.*


---



---

<!-- ===== SECTION: §5.3 (v2 — 2026-04-10) ===== -->
<!-- Source: sections/drafts/ (v2 file) -->

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


<!-- ===== SECTION: §6 Geometric Dark Matter ===== -->
<!-- Source: sections/patched/paper2_section_6_geometric_dark_matter_PATCHED.md -->

# §6: Geometric Dark-Matter Response

## §6.1 Framing: From Particles to Geometry

The standard cosmological paradigm addresses missing gravitational mass through particle dark matter—candidates range from WIMPs (Weakly Interacting Massive Particles) to axions to sterile neutrinos. Each invokes new matter beyond the Standard Model, with density profiles fit *a posteriori* to observations. This approach is phenomenologically successful but unsatisfying: it introduces new particles without detection and requires fitting per-system dark matter distributions that correlate mysteriously with baryonic matter.

The KCR-Cone model sketches a conditional alternative framework: *if* the KCR-Cone warp geometry produces a non-trivial KCR mode spectrum with the properties assumed below, *then* the observed dark-matter acceleration profile may be reinterpreted as gravitational signatures of the warped extra dimension, potentially requiring no new particles. In this picture, the warp factor $A(r,z)$ that modulates the metric geometry would directly produce effective forces on brane-localized matter. Perturbations to $A(r,z)$ near the brane—sourced by baryonic matter itself—would generate an additional gravitational potential on the 3-brane. The integrated effect could mimic dark matter without postulating new particle species.

This is fundamentally different from Modified Newtonian Dynamics (MOND). MOND alters the functional form of Newton's law in the infrared limit (e.g., $F \propto a^2$ rather than $F \propto a$ for small accelerations). The KCR-Cone keeps Einstein's equations intact in 5D but exploits the geometric structure of the extra dimension to produce an effective 4D gravitational correction. The mechanism is not an ad-hoc modification but a consequence of the warp geometry.

The working hypothesis explored in this section: *if* the KCR-Cone warp geometry produces a non-trivial KCR mode spectrum with the properties assumed below, *then* the observed dark-matter acceleration profile—particularly the flat rotation curves in galaxies and the tight radial acceleration relation (RAR)—could emerge as a geometric effect of the warped bulk, not from a population of unseen particles.

**Status**: The analysis in this section is schematic. The perturbation equations (Eqs. 6.1–6.5) assume a linearization regime that has not yet been verified against the full 5D Einstein equations on the KCR-Cone background of §4. The observational predictions (§6.5) are conditional on this linearization being valid. A complete treatment requires solving the perturbation eigenvalue problem on the canonical metric of §4, which is deferred to future work.

---

## §6.2 Perturbation Setup: Linearized 5D Gravity

We linearize the 5D Einstein equations around the **canonical** KCR-Cone background of §4:

$$\mathrm{d}s^2_{(5)} = -\mathrm{d}z^2 + \mathrm{d}r^2 + A_0(r,z)^2\,\gamma_{ij}\,\mathrm{d}\theta^i\mathrm{d}\theta^j,$$

with bulk coordinates $X^A=(z,r,\theta^1,\theta^2,\theta^3)$ and brane hypersurface at fixed $r=r_0$ (as in §4.0). We introduce a small warp perturbation

$$A(r,z)\to A_0(r,z)+\delta A(r,z,\theta), \qquad |\delta A|\ll A_0.$$

At schematic linear order, the bulk perturbation obeys a covariant equation

$$\left(\nabla^{(5)A}\nabla^{(5)}_A-\mathcal{U}_{\mathrm{eff}}\right)\delta A=\kappa_5^2\,\delta T^{(5)}_{\mathrm{eff}}$$

**(Eq. 6.1 — schematic)**

where $\nabla^{(5)}$ is the Levi-Civita operator of the canonical background, $\kappa_5^2 = 8\pi G_5$, and $\mathcal{U}_{\mathrm{eff}}$ denotes the linearized geometric potential induced by the warped S³ sector.

Brane-localized matter enters via a junction/source condition at $r=r_0$:

$$\left[n^A\nabla^{(5)}_A\delta A\right]_{r=r_0}=\kappa_5^2\,\delta S_{\mathrm{brane}}[\rho_b,\ldots]$$

**(Eq. 6.2 — schematic)**

with $n^A$ the unit normal to the brane and $\delta S_{\mathrm{brane}}$ the perturbative brane source functional.

**KK Mode Decomposition**

A separation ansatz consistent with the canonical coordinate roles is:

$$\delta A(r,z,\theta) = \sum_{n=0}^{\infty} \chi_n(r)\,u_n(z,\theta)$$

**(Eq. 6.3)**

where $\chi_n(r)$ are radial bulk profiles and $u_n(z,\theta)$ are induced 4D brane fields. The $n=0$ mode gives the massless sector (ordinary gravity on the brane), while $n \geq 1$ are massive KK excitations with masses $m_n$ fixed by the radial eigenproblem and boundary conditions.

In the non-relativistic brane limit, the zero mode obeys:

$$\nabla^2_{(3)}\Phi_0 = \kappa_4^2 \rho_b$$

**(Eq. 6.4)**

For the massive modes:

$$\left(\Box_4 - m_n^2\right)u_n = J_n[\rho_b]$$

**(Eq. 6.5)**

where the source strength is set by brane overlap factors (schematically proportional to $\\chi_n(r_0)$). From this point onward, phenomenological formulas use $r$ as the projected galactocentric radius on the brane; bulk-radial dependence is encoded in $\\chi_n$ and evaluated at $r=r_0$. In §6.3–§6.5 we reuse the symbol $r$ purely for the 3D brane radial coordinate in $\\vec a_{\\text{eff}}(r)$; no new bulk coordinate is introduced.

---

## §6.3 Effective Force on Brane Matter

The gravitational acceleration felt by a test mass on the brane is:

$$\vec{a}_{\text{eff}} = \vec{a}_{\text{Newton}} + \delta \vec{a}_{\text{geometric}}$$

**(Eq. 6.6)**

where $\vec{a}_{\text{Newton}}$ is the Newtonian acceleration from the baryonic mass distribution, and $\delta \vec{a}_{\text{geometric}}$ is the geometric correction arising from the KCR modes.

**Newtonian Contribution**

The Newtonian term comes from the zero mode:

$$\vec{a}_{\text{Newton}}(r) = -\frac{G_4 M_b(<r)}{r^2} \hat{r}$$

**(Eq. 6.7)**

where $M_b(<r)$ is the baryonic mass within radius $r$.

**Geometric Correction from KK Modes**

The massive KCR modes contribute a correction:

$$\delta \vec{a}_{\text{geometric}}(r) = -\sum_{n=1}^{\infty} \nabla u_n(r) \times (\text{brane coupling})$$

**(Eq. 6.8)**

The sum is dominated by the lowest-mass KCR modes ($n=1,2,\ldots$), since higher modes are increasingly suppressed. The key insight is that at large radii $r \gg R_c$, the Yukawa form of the Green's function for the massive modes leads to a different scaling:

$$u_n(r) \sim \frac{m_n}{r} \exp(-m_n r)$$

**(Eq. 6.9)**

For $r \gtrsim 1/m_n$ (i.e., $r$ comparable to or larger than the Compton wavelength of mode $n$), the exponential suppresses the contribution. However, the cumulative effect of all massive modes (which form a continuum-like tower in the limit of a large extra dimension) can produce a long-range correction that falls off more slowly than $1/r^2$.

**Schematic Form for Galaxy-Scale Dynamics**

For a galaxy-scale mass distribution (extended with scale $\sim$ kpc), numerical integration of the KCR mode sum would, under the stated assumptions, yield an effective acceleration:

$$\vec{a}_{\text{eff}}(r) \approx -\frac{G_{\text{eff}}(r) M_b(<r)}{r^2} \hat{r}$$

**(Eq. 6.10 — schematic)**

where $G_{\text{eff}}(r)$ is an effective, radius-dependent gravitational coupling that varies as:

$$G_{\text{eff}}(r) = G_4 \left[1 + \alpha \frac{R_c}{r} + \mathcal{O}\left(\frac{R_c^2}{r^2}\right)\right]$$

**(Eq. 6.11 — schematic)**

Here $\\alpha$ is a dimensionless coefficient determined by the warp profile and the KCR mode spectrum, and $R_c$ is the characteristic size of the extra dimension. The second term is the geometric correction. At very large radii ($r \\gg R_c/\\alpha$), the correction becomes small relative to the Newtonian term, but at intermediate radii (galactic scale, $\\sim$ 10-50 kpc), it can be substantial. These expressions are schematic, illustrating possible $G_{\\text{eff}}(r)$ behavior under an appropriate KCR spectrum; they are not derived from a completed 5D eigenmode calculation. See Appendix B (`papers/02-saturation-dynamics/sections/patched/paper2_appendix_B_Geff_KK_tower_PATCHED.md`) for a compact asymptotic motivation.

**Rotation Curve Implication**

For circular orbits in a thin disk, $v_{\text{circ}}^2 = r \cdot a_{\text{eff}}(r)$. If $G_{\text{eff}}(r)$ increases with $r$ (or decreases more slowly than expected), the rotation curve becomes flatter. In the simplest schematic picture where the geometric correction grows like $1/r$ at large radii:

$$\delta a_{\text{geometric}} \sim -\frac{\beta G_4 M_b}{r}$$

**(Eq. 6.12)**

with $\beta$ a small dimensionless constant. This would produce a flat rotation curve $v_{\text{circ}} \approx \text{const}$ in the outer galaxy under the stated assumptions, without requiring a dark-matter halo. Under these assumptions, the correction would be sourced entirely by baryonic matter, with no separate dark-matter density parameter.

---

## §6.4 Distinguishing Features of the Geometric Model

### Baryon-Dark-Matter Correlation

A profound puzzle in dark-matter phenomenology is why dark matter and baryons are so tightly correlated. The Radial Acceleration Relation (RAR)—the tight correlation between total (observed) gravitational acceleration and baryonic acceleration—has no obvious explanation in the ΛCDM model, where dark matter follows from collisionless N-body dynamics independent of baryon physics.

In the geometric KCR-Cone model, this correlation would be **structural** (built into the geometry rather than coincidental):

$$\delta a_{\text{geometric}}(r) = f\left(\rho_b(r), A(r,z), u_n,\chi_n(r_0)\right)$$

**(Eq. 6.13)**

The geometric correction depends directly on the baryonic density profile $\rho_b(r)$ (through the source term in Eq. 6.2) and the warp geometry. There is no separate, stochastically formed dark-matter halo—the apparent "dark matter" would be the gravitational shadow of the geometry itself. Consequently, wherever baryons are dense, the geometric response would be strongest; where baryons are sparse, the response would be weak. This explains the observed tight baryon-dark-matter coupling naturally, without fine-tuning, *if the linearization of §6.2 is valid*.

### No Free Dark-Matter Density Parameter

Traditional dark-matter models fit a dark-matter density profile (e.g., Navarro-Frenk-White or isothermal) to each galaxy. This introduces a free parameter: the dark-matter halo mass or concentration. The geometric model would, if the linearization holds, eliminate this freedom—the response would be determined entirely by:

1. The observed baryonic mass distribution
2. The warp geometry (specifically, $A(r,z)$ and the KCR spectrum)
3. Physical constants ($G_5, R_c$)

Once the warp parameters are fixed by fitting one class of objects (e.g., rotation curves of a sample of spiral galaxies), the model's predictions for other observables (dwarf galaxies, elliptical galaxies, lensing, CMB) are constrained, not free to adjust.

### Deterministic Response

The geometric correction would be deterministic under the assumptions of §6.2—there is no analog of dark-matter halo scatter. Different galaxies with identical baryonic distributions (and the same warp geometry) would have identical apparent dark-matter distributions. This is in striking contrast to ΛCDM simulations, where halos with the same total mass have significant variations in substructure and spatial distribution.

Observationally, this predicts that the scatter in dark-matter properties (for fixed baryon distribution) should be very small—a specific prediction testable against high-resolution hydrodynamical simulations.

---

## §6.5 Observational Predictions

**Status**: The predictions below are conditional on the schematic linearization of §6.2. They should be treated as directional indicators, not quantitative forecasts, until the perturbation eigenvalue problem on the canonical KCR-Cone metric is solved.

### Rotation Curves

**Prediction**: Spiral galaxies should exhibit flat rotation curves at large radii (beyond the stellar disk extent) under the stated assumptions, with the rotation curve shape determined by the baryonic mass profile alone, modified by the geometric correction factor $G_{\text{eff}}(r)$.

For a thin exponential disk with scale length $h$, the model predicts:

$$v_{\text{circ}}^2(r) = r \int_0^r \frac{G_{\text{eff}}(r') M_b(r')}{r'^2} dr'$$

**(Eq. 6.14)**

The $G_{\text{eff}}(r)$ factor would produce flattening consistent with observations. Crucially, this differs from standard dark-matter halo models (e.g., NFW profiles) in the detailed shape, especially at intermediate radii (10–50 kpc). Next-generation surveys (e.g., WALLABY, DESI) will measure rotation curves with exquisite precision, allowing discrimination.

### Radial Acceleration Relation

The RAR—empirically $a_{\text{obs}} = a_b / (1 - e^{-a_b/a_0})$ with $a_0 \sim 10^{-10}$ m/s² (Milgrom's scale)—is a mystery in ΛCDM. In the geometric model:

$$a_{\text{obs}} = a_{\text{Newton}} + \delta a_{\text{geometric}}(a_{\text{Newton}})$$

**(Eq. 6.15)**

If the geometric correction satisfies $\delta a_{\text{geometric}} / a_{\text{Newton}} \approx 1 - e^{-a_{\text{Newton}}/a_0}$ in the range $10^{-12} < a < 10^{-9}$ m/s², the empirical RAR would emerge naturally. This requires the warp parameters to be tuned such that $a_0 = G_4 \alpha / R_c$ (where $\alpha$ is the dimensionless constant in Eq. 6.11). Such tuning is not more severe than the fine-tuning already present in ΛCDM (e.g., the coincidence problem) and can be addressed by symmetry arguments in a full quantum theory of the warp geometry.

### Bullet Cluster and Gravitational Lensing

In the Bullet Cluster, the baryonic matter (hot gas) is offset from the peak of the gravitational lensing signal, separated by ~1 Mpc. Standard dark-matter models explain this as the collision-decoupling of dark-matter halos from gas. The geometric model offers a different mechanism:

The warp perturbation $\delta A(r,z)$ satisfies a wave equation (Eq. 6.2). Perturbations propagate through the bulk at finite speed—the speed of light in 5D, $c_5$. If the Bullet Cluster results from a recent merger, the warp perturbation of the incoming cluster may not have fully equilibrated with the baryonic matter of the other cluster. The offset would reflect a **propagation delay** in the geometric response, not the decoupling of dark-matter particles.

Quantitatively, if the collision time is $t_{\text{col}}$ and the bulk propagation time is $\tau \sim \sqrt{R_c^2 + L^2}/c_5$ (where $L$ is the separation scale), the offset is:

$$\Delta x \sim c_5 \cdot (\tau - t_{\text{col}})$$

**(Eq. 6.16)**

Matching the observed offset of ~1 Mpc constrains the bulk parameters. This is a dynamical prediction—different merger configurations and velocities will produce different offsets, unlike the generic dark-matter explanation.

---

## §6.6 Falsification Criteria

### Direct Dark-Matter Detection

If WIMPs, axions, or other dark-matter particles are directly detected (via scattering on nuclei or decay products), the geometric model does not explain all dark-matter phenomena—at minimum, both geometric and particulate contributions exist. However, non-detection does not falsify the model; it only makes geometric dark matter more plausible as the dominant explanation.

### Breakdown of Baryon-Dark-Matter Correlation

If high-precision observations reveal galaxies with fixed baryonic distributions but significantly different "dark-matter" properties, the geometric model is falsified. Specifically:

- **Different scaling laws**: If dwarf galaxies systematically deviate from the baryon-dark-matter correlation observed in spiral galaxies, geometric determinism fails.
- **Halo scatter**: If hydrodynamical simulations incorporating the KCR-Cone geometry show significant scatter in geometric response for identical initial baryonic profiles, the model is falsified.

### Rotation Curve Shapes and the Tully-Fisher Relation

The geometric model predicts specific deviations from dark-matter halo profiles in the detailed rotation curve shape. For instance:

- **Transitional galaxies**: Objects with partially formed disks should exhibit rotation curve shapes that match the geometric prediction precisely, with no free dark-matter parameters.
- **Tully-Fisher scatter**: The Tully-Fisher relation (luminosity vs. rotation velocity) in the geometric model has smaller intrinsic scatter than expected from ΛCDM (since there is no halo scatter). Observing large scatter would disfavor the model.

### Lensing on Large Scales

Weak gravitational lensing on Megaparsec scales probes the smoothed-out matter distribution. The geometric model predicts that the lensing signal follows smoothed baryonic matter with an $r$-dependent effective coupling $G_{\text{eff}}(r)$. If lensing observations reveal clumpy, extended mass not associated with baryons, the model is falsified.

### Power Spectrum Consistency

The cosmic microwave background (CMB) power spectrum and large-scale structure (LSS) power spectrum are sensitive to the effective gravitational coupling at different scales. The geometric model must be consistent with:

- **Acoustic peaks**: The positions and amplitudes of the CMB acoustic peaks depend on $G_{\text{eff}}$ at early times and the late-time integrated Sachs-Wolfe effect.
- **Baryon acoustic oscillations (BAO)**: The BAO scale encodes the sound-horizon at decoupling and is insensitive to late-time dark matter. If $G_{\text{eff}}$ varies significantly with redshift, LSS predictions will shift.

A detailed analysis (beyond the scope of this section) is required, but any significant discrepancy with WMAP, Planck, or future CMB experiments would falsify the model.

---

## §6.7 Open Questions and Future Work

### Quantum Stability of the Warp Geometry

The linearized analysis assumes the KCR-Cone background is stable under small perturbations. Quantum corrections (one-loop, higher-loop) to the warp profile must be computed to ensure stability. If quantum backreaction significantly modifies $A(r,z)$, the predictions change.

### Non-Linear Regime and Cluster Dynamics

The linearization breaks down for high-contrast structures (e.g., galaxy clusters where $\delta A / A_0 \sim 0.1$ or larger). Non-linear solutions to the 5D Einstein equations are required to model clusters. This is a substantial computational challenge but necessary for precision predictions.

### Relation to MOND and TeVeS

The geometric model superficially resembles MOND (both produce flat rotation curves) but differs fundamentally in mechanism. A detailed comparison—including quantitative predictions for systems where MOND and the geometric model diverge—would clarify the relationship and may enable observational discrimination.

### Dark Energy and the Warp Sector

The cosmological constant problem and the observed accelerated expansion (typically attributed to dark energy) are not directly addressed here. The warp geometry might also contribute to dark-energy phenomena; investigating whether a unified treatment of "dark" phenomena (dark matter + dark energy) emerges from the KCR-Cone is compelling.

---

## Conclusion

The geometric dark-matter response in the KCR-Cone model provides an intriguing conditional alternative to particle-based dark matter. If the schematic analysis survives a full perturbation treatment on the canonical KCR-Cone metric, the geometric mechanism would provide a natural explanation for:

- **Flat rotation curves** without dark-matter halos
- **Baryon-dark-matter correlation** (the tight RAR) as a geometric consequence, not a coincidence
- **Deterministic structure** with no free dark-matter density parameters

The model is falsifiable through observations of rotation curve shapes, baryon-dark-matter correlation breakdown, direct dark-matter detection, and large-scale structure surveys. Current data do not yet exclude this schematic scenario, but no quantitative global fit is claimed here; future precision measurements will provide decisive tests. If the geometric treatment holds, the geometry of the extra dimension may contribute to or account for the observations, offering a different perspective than invisible particles.

The burden of proof shifts to §7–§8, where the equations of motion on M × Σ and the full perturbation spectrum must be computed.

---

**References and Further Reading**

This section builds on the KCR-Cone formalism established in §3 and §4, the perturbation theory of §5, and the linearized analysis of warp-factor dynamics. Detailed numerical results and comparisons with observational datasets will be presented in subsequent papers.


---



---

<!-- ===== SECTION: §8 (v2 — 2026-04-10) ===== -->
<!-- Source: sections/drafts/ (v2 file) -->

# §8.0 Holographic Structure Conjecture — v2 (2026-04-08)

**Status:** DRAFT | CONJECTURED with worked example support (KCR-Cone)
**Change from v1:** Added §8.0 preamble + comparison table (Position b), revised §8.1.3 conjecture, new §8.3.5 dS/CFT comparison, new §8.10 closing summary. All existing §8.1–§8.9 verified numerical content preserved.
**Word count:** ~7,000

---

## §8.0 Preamble: Structural Position

The M × Σ geometry of Coherence Relativity shares structural features with holographic theories, particularly in the role of the radial direction as a decoherence scale, the coupling of boundary observables through cross-terms in the metric, and the warp-factor encoding of geometric information. However, the relationship between CR and the foundational AdS/CFT correspondence (Maldacena 1997, 1998) is neither identity nor exclusion. Rather, CR and AdS/CFT represent different realizations of the holographic principle, each with distinct mechanisms, geometric origins, and physical interpretations.

This section develops the holographic interpretation of the KCR-Cone and presents the following position:

> **Position (b):** CR and AdS/CFT are different holographic classes, each realizing the holographic principle through distinct mechanisms. They are not the same theory; they are not mutually exclusive; they occupy different corners of the space of holographic dualities.

We proceed by comparing the two frameworks systematically, identifying the CR holographic conjecture, and acknowledging both the strengths and open problems of the CR picture.

### §8.0.1 Comparison Table: CR KCR-Cone vs. AdS/CFT

| Feature | AdS/CFT (Maldacena 1997) | CR KCR-Cone |
|---------|--------------------------|------------|
| **Bulk geometry** | AdS₅ × S⁵ (negative Λ) | M × Σ: R × S³ × [0, L*] (positive Λ_eff) |
| **Bulk cosmological constant** | Λ < 0 (derived from D3-brane near-horizon; required for AdS throat) | Λ_eff > 0 (Casimir stabilization, §5.3; consistent with observed universe) |
| **Radial direction origin** | Near-horizon limit of D3 branes; string theory UV completion | Fubini-Study arc-length r on Σ; geometric prediction from coherence manifold |
| **Radial direction role** | Energy/length scale (RG flow in CFT) | Decoherence depth (coherence-RG flow); r non-traversable (Proposition, §4.2) |
| **Warp decay rate** | μ_RS = k (set by AdS radius, phenomenological for hierarchy) | μ = √2 (fixed by Fubini-Study eigenvalue k²=2; first-principles, §7.8) |
| **Fiber structure** | S⁵ compact manifold (6D extra space) | S³ fiber via Hopf projection S¹→S³→S² (KCR-Cone §4) |
| **Boundary theory** | 𝒩=4 SYM (D=4 CFT, exactly conformal, Λ_bdy = 0) | QFT on M-brane; time is RG-invariant (T_{zr}=0, §7.4); non-conformal |
| **Holographic dictionary** | GKPW: Z_bulk[φ_0] = ⟨exp∫φ_0 O⟩_CFT (exact) | T_{MΣ} as source coupling (§8.2.3); not yet bulk-boundary prescription |
| **Entanglement entropy** | Ryu-Takayanagi: S = Area(γ)/4G_N (exact formula) | Weakened conjecture: S_coh ~ f(d_Σ), f'>0; S_RT ~ d_Σ^{0.80} (§8.6.4) |
| **UV completion** | Type IIB string theory (well-defined) | Not yet specified; gravity emerges from KK decoupling (§4) |
| **Status** | Highly tested; Λ < 0 is cosmological tension | Conjecture; holographic dictionary under construction |

### §8.0.2 Key Structural Differences and Complementarity

Both theories realize the holographic principle—the idea that a higher-dimensional gravitational theory is dual to a lower-dimensional quantum field theory—but through structurally distinct mechanisms.

**AdS/CFT via conformal symmetry and D-brane geometry:** The AdS/CFT correspondence emerges from the near-horizon limit of D-branes in string theory. The bulk geometry AdS₅ is generated by the gravitational backreaction of the branes, and the boundary is a conformal field theory (𝒩=4 SYM). The correspondence exploits the isometry group SO(4,2) of AdS₅, which acts as the conformal symmetry group on the boundary. This symmetry is *exact* and leads to the precise GKPW dictionary. The price: AdS has negative cosmological constant Λ < 0, inconsistent with observed accelerated cosmic expansion.

**CR via decoherence-depth geometry and Fubini-Study pullback:** The KCR-Cone geometry of CR emerges from the joint manifold M × Σ, where Σ is equipped with the Fubini-Study metric (a positive-definite Kähler metric). The radial direction r is not a string-theoretic scale but an arc-length coordinate encoding decoherence depth. The geometric origin of the warp factor is first-principles: the Fubini-Study Laplacian eigenvalue k²=2 *fixes* μ = √2 (§7.8). Crucially, the effective cosmological constant is Λ_eff > 0 (§5.3, Casimir stabilization), matching the observed universe.

**The cosmological constant sign contrast:** This is the most striking structural difference. AdS/CFT requires Λ < 0. CR's positive Λ_eff emerges dynamically from Casimir stabilization. This makes CR potentially more relevant to our universe, while accepting the trade of reduced mathematical precision.

### §8.0.3 The Open Problem: Bulk-Boundary Correspondence

The metric tensor T_{MΣ} (specifically the cross-term Ω_{MΣ}) is identified as the coupling object, but a complete GKPW-like bulk-boundary prescription has not yet been established. This is CR's major structural gap. We identify the structural parallels, note the differences, and propose a holographic relationship. Formal derivation (computing the central charge, establishing the full dictionary, proving unitarity) is deferred to future work.

---

## §8.1 Why Holography?

### §8.1.1 AdS-Like Structure Without Standard AdS

The KCR-Cone metric is:

$$ds^2 = -dz^2 + A(r)^2 \gamma_{ij} dx^i dx^j + dr^2, \quad A(r) = e^{-\mu r}
\tag{8.1.1}$$

This exhibits spatial warping (the $A(r)^2$ factor) reminiscent of AdS geometry. In standard AdS/CFT, such warping encodes the holographic duality: the radial direction represents energy/length scales in the boundary theory.

**However**, the KCR-Cone has three non-standard features:

1. **Time is unwarped:** n(r) = 1 is an *ansatz*, not derived from vacuum Einstein equations.
2. **The warping is in spatial directions only:** This breaks the conformal structure of AdS.
3. **The coherence sector Σ is 1-dimensional:** Unlike standard AdS/CFT where the radial direction is one coordinate among many, r here has a physical interpretation as the coherence parameter λ.

### §8.1.2 Coherence Interpretation

From Coherence Relativity Paper 1, the frame Σ parameterizes the environment's distinguishability of the system's quantum state. The metric on Σ is the Fubini-Study metric (Eq. 2.1.4):

$$ds_\Sigma^2 = 4 \left( \langle d\psi | d\psi \rangle - |\langle \psi | d\psi \rangle|^2 \right)
\tag{8.1.2}$$

In the KCR-Cone, Σ = [0, L_*] with the radial coordinate r acting as the decoherence parameter:

$$\lambda(r) = A(r)^2 = e^{-2\mu r}
\tag{8.1.3}$$

This is a **CONJECTURED** identification. It says: as the system evolves in the bulk (increasing r), the quantum coherence of its boundary state decreases exponentially. From §7.8, the rate μ = √2 is now fixed by the Fubini-Study Laplacian eigenvalue k²=2, not fitted.

### §8.1.3 Conjecture 8.1: Holographic Structure — Position (b)

**Conjecture 8.1 (Holographic Structure — Position (b)):** The KCR-Cone geometry of Coherence Relativity is a holographic theory distinct from AdS/CFT. CR and AdS/CFT are different realizations of the holographic principle: AdS/CFT via conformal symmetry on a negative-Λ background; CR via decoherence-depth geometry on a positive-Λ_eff background. The CR holographic dictionary — mapping bulk objects (T_{MΣ}, λ(r), A(r)) to boundary observables — is partially identified (§8.2) but not yet complete. The formal derivation of a GKPW-like prescription is deferred. We conjecture that this structure constitutes a holographic duality; proof requires establishing the bulk-boundary correspondence explicitly.

This duality is *non-standard* because:
- The boundary theory lives on a manifold with unwarped time (unlike CFT in Euclidean AdS backgrounds)
- The holographic direction has a quantum-information interpretation
- The conformal invariance is broken by the time non-conformality

---

## §8.2 The Holographic Dictionary

We now build the correspondence between bulk geometric objects and boundary quantum structures.

### §8.2.1 State Map and Boundary State

**Bulk:** The state map Φ: M × Σ → PH is a section of the projective Hilbert bundle over M × Σ. At a fixed point (x^μ, ξ) ∈ M × Σ, Φ(x^μ, ξ) is a projective equivalence class [|ψ(x^μ, ξ)⟩].

**Boundary (r = 0):** The restriction Φ|_{r=0}(x) = [|ψ(x)⟩] is the coherent state of the quantum system as seen from the brane.

**Dictionary Entry 1:**
$$\boxed{\text{Boundary state} \quad \Longleftrightarrow \quad \Phi(x, 0)}
\tag{8.2.1}$$

### §8.2.2 Radial Direction and RG Flow

**Conjecture 8.2:** The radial coordinate r is identified with the coherence-loss parameter:
$$r \quad \text{encodes} \quad \text{RG scale} = \text{typical decoherence time} \sim \mu^{-1} e^{-\lambda(r)}
\tag{8.2.2}$$

**Dictionary Entry 2:**
$$\boxed{\text{Bulk depth } r \quad \Longleftrightarrow \quad \text{RG scale in coherence flow}}
\tag{8.2.3}$$

The deep-throat classical limit (r → L_*) corresponds to complete loss of coherence and recovery of classical mechanics.

### §8.2.3 Cross-Term and Source Coupling

In standard AdS/CFT, boundary operators couple to bulk fields via:
$$S = S_{\text{CFT}} + \int d^4 x \, g(x) \, O(x)$$

In the KCR-Cone, the cross-term T_{MΣ} (Eq. 2.1.3) from the Fubini-Study pullback plays this role:
$$T_{M\Sigma} = \frac{1}{4} \operatorname{Tr}\left[ (\partial_\mu \hat{\rho}) (\partial_r \hat{\rho}) \right]
\tag{8.2.4}$$

From §7.2.14, the upper-index cross-term scales as:
$$T^{ri} \sim A(r)^{-2}
\tag{8.2.5}$$

**Dictionary Entry 3:**
$$\boxed{T_{M\Sigma} \quad \Longleftrightarrow \quad \text{Source coupling in holographic RG}}
\tag{8.2.6}$$

### §8.2.4 Frame-Lag Force and Effective Inter-Sector Coupling

From §7.4, the frame-lag force is:
$$F_{\text{lag}}^r = \lambda \, T^{ri} \, a_i
\tag{8.2.7}$$

The key result from §7.4.15:
$$F_{\text{lag}}^r = \lambda \cdot T^{ri} \cdot a_i \sim A^2 \cdot A^{-2} \cdot a_i = O(1) \cdot a_i
\tag{8.2.8}$$

**Conjecture 8.3:** The effective coupling between the M and Σ sectors is scale-independent:
$$\lambda(r) \cdot T^{ri}(r) = O(1), \quad \text{uniform across all } r
\tag{8.2.9}$$

**Dictionary Entry 4:**
$$\boxed{\lambda \cdot T^{ri} = O(1) \quad \Longleftrightarrow \quad \text{Uniform decoherence response (warp cancellation)}}
\tag{8.2.10}$$

### §8.2.5 Temporal Decoupling

From Eq. 7.4.12:
$$T_{z r} = 0
\tag{8.2.11}$$

**Dictionary Entry 5:**
$$\boxed{T_{zr} = 0 \quad \Longleftrightarrow \quad \text{Boundary time is RG-invariant}}
\tag{8.2.12}$$

### §8.2.6 Warp-Factor Hypothesis

From §7.3:
$$\lambda(r) = A(r)^2 = e^{-2\mu r}
\tag{8.2.13}$$

**Dictionary Entry 6:**
$$\boxed{\lambda(r) = A(r)^2 \quad \Longleftrightarrow \quad \text{Coherence parametrizes spatial geometry}}
\tag{8.2.14}$$

---

## §8.3 Non-Standard Features and Deviations from AdS/CFT

### §8.3.1 Breakdown of Conformal Symmetry

The KCR-Cone metric cannot be put into the Fefferman-Graham form:
$$ds^2 = \frac{dz^2 + g_{\mu\nu}(x, z) dx^\mu dx^\nu}{z^2}$$

Instead, our metric:
$$ds^2 = -dz^2 + e^{-2\mu r} \gamma_{ij} dx^i dx^j + dr^2
\tag{8.3.1}$$

is **genuinely non-conformal**.

### §8.3.2 Unwarped Boundary Time

The boundary time direction (z-direction on the brane) does not participate in the holographic deformation. This means boundary theory observables do not scale as $O \sim t^{-\Delta}$ under time dilation; instead, time is RG-invariant (Eq. 8.2.12).

### §8.3.3 One-Dimensional Coherence Sector

The frame Σ = [0, L_*] is a 1-dimensional manifold. Unlike standard AdS/CFT where the radial direction is one coordinate among many, r here is a quantum-information axis. Entanglement in the KCR-Cone holography involves both standard spatial entanglement (in M) and coherence entanglement (across Σ). The Ryu-Takayanagi formula must be generalized (§8.5).

### §8.3.4 Necessity of Non-Conformality

In standard RS1/RS2, the time and spatial warp factors are related by the 5D vacuum Einstein equations. In the KCR-Cone, we imposed n(r) = 1 as an *ansatz*, requiring non-trivial bulk matter:
$$\kappa_5^2 T_{zz} = -3\mu^2 \neq 0
\tag{8.3.2}$$

**Conjecture 8.4:** The non-conformality is essential for the coherence interpretation. The bulk matter with T_{zz} ≠ 0 encodes the quantum decoherence mechanism. (The n(r) = 1 ansatz is convention-locked as Option D — see §7.1.3.)

### §8.3.5 Comparison with dS/CFT (Strominger 2001)

The question "Can a positive-Λ geometry host a holographic duality?" was first addressed by Strominger (2001) in the context of de Sitter space (dS/CFT). CR and dS/CFT both attempt to avoid the Λ < 0 problem of AdS/CFT, but via different mechanisms.

#### dS/CFT and Its Problems

Strominger proposed that de Sitter space dS_d could be dual to a Euclidean CFT on the future boundary I⁺. The key difficulties:

1. **Non-unitarity:** The natural inner product on a spacelike boundary I⁺ is indefinite. Correlation functions have negative-norm states.
2. **No natural time evolution:** A spacelike boundary has no natural time direction, making it difficult to define Hermitian operators or thermal states.
3. **Analytic continuation problems:** The dS boundary requires Wick rotation that may not be consistent for all observables.

Despite efforts by Witten (2001), Maldacena (2011), and others, dS/CFT remains incomplete. The fundamental issue is geometric: a positive-Λ background (dS) is incompatible with the conformal structure of a CFT boundary.

#### Why CR Avoids dS/CFT Problems

Coherence Relativity sidesteps the dS/CFT difficulties via three mechanisms:

1. **Timelike boundary:** The CR boundary is the brane M at r = 0, which is a timelike surface with a natural time direction z⁰. The inner product on M is positive-definite. Unitarity is preserved by construction.

2. **Positive-definite Kähler metric:** The coherence manifold Σ is equipped with the Fubini-Study metric — a positive-definite Riemannian metric. There are no spacelike directions, no ghost states, and no analyticity issues.

3. **Dynamical Λ_eff from Casimir stabilization:** CR's positive cosmological constant does not arise from an external input (dS parameter) but from a dynamical balance: the Casimir force (§5.3) between the brane and the fiber boundary stabilizes the system at a fixed value of L* and Λ_eff. This is a mechanism, not an assumption.

#### Status of CR vs. dS/CFT

- **dS/CFT:** Highly motivated but incomplete. No known resolution of unitarity and boundary-structure problems.
- **CR:** Geometrically clean (timelike boundary, positive-definite metrics) but without a complete holographic dictionary.

CR offers a different approach to positive-Λ holography than dS/CFT, avoiding the latter's pathologies but at the cost of reduced mathematical precision. Whether this trade-off is favorable is a question for future research.

---

## §8.4 Testable Predictions

### §8.4.1 Uniform Decoherence Response

**Prediction 1:** The frame-lag force is order-unity and independent of r (Eq. 7.4.15):

$$\text{Decoherence rate} \sim \text{const} \quad \text{(independent of energy scale)}
\tag{8.4.1}$$

**How to test:** In an experimental or numerical system, measure the dephasing time T₂ as a function of the system energy E. Standard behavior: T₂(E) ∝ E^{-α} for some α > 0. The KCR-Cone prediction is α = 0.

### §8.4.2 Warp-Factor Scaling of Decoherence

**Prediction 2:** The distinguishability λ(r) obeys λ(r) = e^{-2μr} (Eq. 8.2.13):

$$\text{Distinguishability} \sim \exp(-2\mu r) = A(r)^2
\tag{8.4.2}$$

**How to test:** In a system where the "warp factor" is observable, measure A(r) and verify that the decoherence rate follows λ(r) = A(r)².

### §8.4.3 Sharp Quantum-to-Classical Transition

**Prediction 3:** At r → L_* (the deep throat), coherence vanishes and the system classicalizes:

$$\text{At } r \approx L_* \approx 0.2 / \mu: \quad \text{quantum coherence} \to 0
\tag{8.4.3}$$

The transition is **sharp** (exponential decay), not gradual.

### §8.4.4 Comparison with Standard Holographic Predictions

**Status:** Numerical verification of Eq. 8.5.6 performed (Mar 2026). Two phases completed: (1) reduced-state entropy — monotonic link confirmed, strict proportionality refuted (sublinear power law $d_\Sigma \propto S_{\text{comp}}^{0.22}$); (2) spatial-partition RT (Eq. 8.5.7) — $S_{\text{RT}}(\lambda)$ monotonically decreasing, weakly proportional to $d_\Sigma(\lambda)$ with CV $\approx 6\%$ and power-law exponent $\alpha = 0.80$. Supports the weakened conjecture ($f' > 0$); strict proportionality ($\alpha = 1$) does not hold. See §8.6.4 for full results.

---

## §8.5 Relation to Ryu-Takayanagi and Entanglement Entropy

### §8.5.1 Standard Ryu-Takayanagi Formula

In AdS/CFT, the entanglement entropy of a boundary region A is given by:
$$S_A = \frac{\text{Area}(\gamma_A)}{4 G_N}
\tag{8.5.1}$$

where γ_A is an extremal surface in the bulk with boundary ∂γ_A = ∂A.

### §8.5.2 Generalization to the KCR-Cone

An extremal surface in M × Σ with metric:
$$ds^2 = -dz^2 + e^{-2\mu r} \gamma_{ij} dx^i dx^j + dr^2
\tag{8.5.2}$$

has area:
$$\text{Area}(\gamma_A) = \int_{\gamma_A} d\sigma_1 d\sigma_2 \sqrt{g_{\text{ind}}}
\tag{8.5.3}$$

**Conjecture 8.5:** The entanglement entropy in the KCR-Cone holographic dual is:
$$S_A = \frac{\text{Area}(\gamma_A)}{4 G_N} = \frac{1}{4 G_N} \int_{\gamma_A} d\sigma_1 d\sigma_2 \, \sqrt{g_{\text{ind}}}
\tag{8.5.4}$$

### §8.5.3 Coherence and Entanglement

**Conjecture 8.6:** The geometric distance $d_\Sigma(\lambda) = \int_\lambda^1 \sqrt{G_{\lambda\lambda}} \, d\lambda'$ is monotonically related to entanglement entropy:
$$S_{\text{coherence}}(\lambda) \sim f\!\left(d_\Sigma(\lambda)\right), \quad f' > 0
\tag{8.5.6}$$

(In the zero-noise limit, $d_\Sigma$ coincides with the Freidlin-Wentzell quasipotential $V$ of Paper 1, Eq. 6.)

**Verification status (updated 2026-03-09):** WEAKENED CONJECTURE SUPPORTED; STRICT PROPORTIONALITY RULED OUT. Three independent numerical tests performed on the $N = 10$ dephasing model:

*Phase 1 (reduced-state entropy):* $d_\Sigma(\lambda)$ and standard quantum entropy measures are monotonically correlated but **not strictly proportional**. Best fit: sublinear power law $d_\Sigma \propto S_{\text{comp}}^{0.22}$. Root cause: $N$-dependence mismatch between $d_\Sigma$ (depends on $N$ via $G_{\lambda\lambda}$) and $S_{\text{vN}}$ ($N$-independent).

*Phase 2 (spatial-partition RT, Option C):* $S_{\text{RT}}(\lambda)$ is **monotonically decreasing** — same monotonicity as $d_\Sigma(\lambda)$. CV $\approx 6\%$; power-law fit $S_{\text{RT}} \propto d_\Sigma^{0.80}$. Best quantitative match among all entropy measures tested.

*Phase 3 (mode-resolved entropy, Option A):* Best $N$-dependent candidate: $S_{\text{mc}} = N(\ln 2 - h((1+r_k)/2))$ with CV $= 13.7\%$. **Strict proportionality not restored.** Root cause: $d_\Sigma(\lambda) = \sqrt{N/2} \cdot \arcsin((1-\lambda)^{1/N})$ is LINEAR in the per-mode overlap $r_k$ near $r_k \to 0$, while all standard entropies are QUADRATIC in $(1-r_k)$ near $r_k \to 1$. This arcsin-vs-$h$ functional mismatch makes strict proportionality mathematically impossible for any standard entropy measure.

**Implication:** All three refinement routes tested. The weakened conjecture $f' > 0$ is supported by all phases. Strict proportionality ($\alpha = 1$) is ruled out by a structural mathematical incompatibility.

### §8.5.4 Holographic Duality Without Standard Conformal Structure

For a spatial region A on the brane, the extremal surface γ_A satisfies:
$$\frac{d}{dr}\left( A(r)^2 K_r \right) + A(r)^2 K_\perp^2 = 0
\tag{8.5.7}$$

where K_r is the extrinsic curvature in the r-direction and K_⊥ is in the spatial directions.

**Numerical solution (2026-03-09):** Eq. 8.5.7 was solved for a flat-space strip on the brane via the first integral method (area functional $\mathcal{L} = A^2\sqrt{A^2 + r'^2}$, conserved quantity $A^4/\sqrt{A^2 + r'^2} = A_*^3$). The resulting $S_{\text{RT}}(\lambda)$ is monotonically decreasing and weakly proportional to $d_\Sigma(\lambda)$ (CV $\approx 6\%$, power-law exponent $\alpha = 0.80$).

---

## §8.6 Open Questions and Limitations

### §8.6.1 Is n(r) = 1 Essential?

**Open question:** Does the holographic duality survive if we generalize to n(r) ≠ 1? The n(r) = 1 ansatz is convention-locked as Option D; relaxation options are parked for future work.

### §8.6.2 Central Charge of the Boundary Theory

In AdS/CFT, c ∝ (AdS radius)³ / G_N. In the KCR-Cone, a naive dimensional estimate gives:
$$c \sim \frac{\ell_{\text{eff}}^3}{\kappa_5^2}
\tag{8.6.1}$$

where $\ell_{\text{eff}} \sim \mu^{-1} = 1/\sqrt{2}$ (in units where the Fubini-Study length scale is normalized). Without the central charge, we cannot compute operator dimensions or correlation functions directly.

### §8.6.3 Radion Field Interpretation

**Conjecture (speculative):** The radion might correspond to the coherence modulus λ itself, with:
$$m_{\text{radion}} \sim \mu = \sqrt{2}
\tag{8.6.2}$$

A proper treatment requires computing the radion action from the 5D theory.

### §8.6.4 Numerical Verification

The strongest test of the holographic conjecture is numerical verification of Eq. 8.5.6. Results (Mar 2026) from the $N = 10$ dephasing model:

**Tested candidates against $d_\Sigma(\lambda) = \int_\lambda^1 \sqrt{G_{\lambda\lambda}} \, d\lambda'$:**

| Entropy Measure | Coefficient of Variation | Verdict |
|----------------|--------------------------|---------| 
| $\log 2 - S_{\text{vN}}$ (complementary) | 228% | Not proportional |
| $\lambda^{3/2}$ (RT-like surface area) | 246% | Not proportional |
| $-\log\lambda$ (Rényi-0) | 80% | Not proportional |
| $\arccos(1 - \lambda)$ | 82% | Not proportional |
| $\sqrt{1 - \lambda^2}$ (standard QM) | 8.1% | Weakly proportional |

**Root cause of proportionality failure:** $d_\Sigma(\lambda)$ depends on the environment mode count $N$ through $G_{\lambda\lambda}$, but $S_{\text{vN}}$ of the reduced qubit state is $N$-independent — its eigenvalues are always $\{(2-\lambda)/2, \, \lambda/2\}$.

**Best-fit result:** Power law $d_\Sigma \propto S_{\text{comp}}^{0.22}$ (RMS residual 0.017 in log-log), confirming a genuine geometric-entropic link but strongly sublinear.

**Option C detailed results (spatial-partition RT):** Area functional $\mathcal{L} = A^2\sqrt{A^2 + r'^2}$ yields first integral $A^4/\sqrt{A^2 + r'^2} = A_*^3$.

| Comparison | CV | Verdict |
|---|---|---|
| $S_{\text{RT}} / d_\Sigma(\lambda)$ | 5.89% | Weak proportionality |
| $S_{\text{RT}} / d_\Sigma^2$ | 26.9% | Not proportional |
| $S_{\text{RT}} / \sqrt{1-\lambda^2}$ | 5.02% | Weak proportionality (best match) |
| $S_{\text{RT}} / \lambda^{1/2}$ | 70.9% | Not proportional |
| $S_{\text{RT}} / \lambda^{3/2}$ | 162.6% | Not proportional |

$S_{\text{RT}}(\lambda)$ is **monotonically decreasing**. Power-law fit: $S_{\text{RT}} \propto d_\Sigma^{0.80}$ ($\alpha = 0.80$, RMS 0.041 in log-log). The weakened conjecture ($f' > 0$) is supported; strict proportionality ($\alpha = 1$) is ruled out.

**Option A detailed results (mode-resolved entropy):** Analytical closed form (Opus-verified): $d_\Sigma(\lambda) = \sqrt{N/2} \cdot \arcsin\!\left((1-\lambda)^{1/N}\right)$.

**Root cause of strict proportionality failure (definitive):** Near $r \to 0$ ($\lambda \to 1$):
- $d_\Sigma \approx \sqrt{N/2} \cdot r$ — **linear** in $r$
- $S_{\text{mc}} \approx Nr^2/2$ — **quadratic** in $r$ (from $h'(1/2) = 0$)
- Therefore $d_\Sigma \propto \sqrt{S_{\text{mc}}}$, not $S_{\text{mc}}$ directly

**$\sqrt{S_{\text{mc}}}$ universality:** The ratio $d_\Sigma / \sqrt{S_{\text{mc}}} = C \cdot \arcsin(r)/r$ is $N$-independent. Numerically, $\sqrt{S_{\text{mc}}}$ tracks $d_\Sigma$ with CV $\approx 3\text{–}5\%$ across $N = 1 \ldots 100$. **No standard entropy measure** (von Neumann, Rényi, min-entropy) can restore strict proportionality, since all are built on binary entropy $h(p)$ which differs functionally from $\arcsin(r)$.

**Current status:** All three options (A, B, C) tested. Option B applied. Weakened conjecture supported; strict proportionality structurally ruled out.

### §8.6.5 Beyond the KCR-Cone: Generalization

The conjecture is derived from a single worked example. To claim universal validity requires:
1. Solving the CR equations of motion for other geometries (KK with conformal warping, RS1, RS2)
2. Checking whether the order-unity frame-lag force persists
3. Verifying the λ ~ A² identification holds
4. Generalizing the holographic dictionary

**Current status:** Not yet attempted. Major future project.

---

## §8.7 Summary: Holographic Dictionary

| Bulk Object | Boundary Interpretation | Status | Equation |
|---|---|---|---|
| State map Φ: M × Σ → PH | Coherent quantum state |ψ(x)⟩ on brane | **DEFINED** (Paper 1); holographic role **CONJECTURED** | 8.2.1 |
| Radial coordinate r | RG scale / decoherence parameter | **CONJECTURED** | 8.2.3 |
| Warp factor A(r) = e^{-μr} | Spatial geometry encodes coherence loss | **CONJECTURED** (identified λ ~ A²) | 8.2.14 |
| Cross-term T_{MΣ} | Source coupling in holographic β-function | **CONJECTURED** | 8.2.6 |
| Frame-lag force F_lag | Uniform decoherence response (warp cancellation) | **CONJECTURED** (order-unity in worked example) | 8.2.10 |
| T_{zr} = 0 | Boundary time is RG-invariant | **CONJECTURED** | 8.2.12 |
| Extremal surface γ_A | Ryu-Takayanagi surface in M × Σ | **CONJECTURED** | 8.5.4 |
| Geometric distance d_Σ(λ) | Coherence entanglement entropy | **WEAKENED CONJECTURE SUPPORTED; STRICT ∝ RULED OUT** — Phase 2 (RT): $S_{\text{RT}} \propto d_\Sigma^{0.80}$ (CV ≈ 6%); Phase 3: $d_\Sigma \propto S_{\text{mc}}^{0.59}$; $d_\Sigma \propto \sqrt{S_{\text{mc}}}$ universal across N. Root cause: arcsin-vs-h structural mismatch (theorem). $f' > 0$ confirmed; $\alpha = 1$ impossible. | 8.5.6 |
| Deep throat r → L_* | Quantum-to-classical transition | Classical limit **VERIFIED** (§7.5); holographic interpretation **CONJECTURED** | 8.4.3 |

---

## §8.8 Implications for Coherence Relativity

### Coherence Holography Thesis

The KCR-Cone worked example provides evidence for a new principle:

> **In the KCR-Cone worked example, the loss of coherence is dual to the deformation of spacetime geometry. The radial direction of bulk spacetime encodes the decoherence RG flow. Whether this extends beyond the single worked example to a universal principle remains an open question (§8.6.5).**

### Unification with Holography

Coherence Relativity extends standard holography (AdS/CFT) by adding a quantum-information axis (Σ). The price is loss of conformal symmetry, but the payoff is a physical interpretation of the holographic direction and a positive cosmological constant consistent with observation.

### Predictions for Quantum-to-Classical Transition

The sharp classical limit (r → L_*) predicts that **quantumness is fragile and localized near the brane**. This is consistent with:
- The quantum-classical correspondence principle (classical limit as ℏ → 0)
- Decoherence-induced transitions in open quantum systems
- The emergence of classicality from quantum mechanics in cosmology

---

## §8.9 Caveats and Scope

**This conjecture applies specifically to:**
- The KCR-Cone geometry with n(r) = 1
- Single-system coherence (not entanglement between two systems)
- Small-r regime where the warp factor is monotonic

**This conjecture does NOT address:**
- Whether the bulk satisfies the full 5D Einstein equations (it does not; ansatz imposed)
- Unitarity of the boundary theory (not proven)
- Computational predictions for arbitrary observables (only shown for frame-lag force)
- Quantum gravity effects (stringy corrections, etc.)

**Confidence level:** ~55% that this represents a genuine physical duality with holographic character. The order-unity cancellation in Eq. 7.4.15, the self-consistent deep-throat classical limit, the spatial-partition RT result ($S_{\text{RT}} \propto d_\Sigma^{0.80}$, CV $\approx 6\%$), and the CR vs. dS/CFT structural advantages all support a real geometric-entropic link. Strict proportionality ($\alpha = 1$) is **ruled out** by the arcsin-vs-$h$ functional mismatch: a structural theorem, not merely a numerical result.

---

## §8.10 Summary: Structural Holography Conjecture

### §8.10.1 What is Verified

1. The M × Σ geometry has a radial direction (r) with exponential decay of λ(r), non-traversability (Proposition 4.2), and RG-like flow — paralleling holographic geometries.
2. The Fubini-Study metric on Σ is positive-definite and well-behaved, avoiding the unitarity problems of dS/CFT (§8.3.5).
3. The effective cosmological constant Λ_eff > 0 is positive and derived from dynamical Casimir stabilization (§5.3), not an input assumption.
4. The warp decay rate μ = √2 is fixed by the Fubini-Study Laplacian eigenvalue k²=2 (§7.8) — not phenomenological.
5. Preliminary numerical evidence supports a weakened RT formula: $S_{\text{RT}} \propto d_\Sigma^{0.80}$ (CV ≈ 6%).

### §8.10.2 What is Conjectured

1. The KCR-Cone geometry constitutes a holographic duality — a higher-dimensional gravitational theory on M × Σ equivalent to a lower-dimensional QFT on M.
2. The six entries in the holographic dictionary (§8.2) can be completed into a full GKPW-like prescription.
3. Correlation functions, entanglement entropy, and other observables can be computed from bulk data and match boundary theory predictions.
4. The central charge and other invariants of the boundary theory are related to bulk geometry.
5. The duality is unitary and consistent with quantum mechanics.

### §8.10.3 The Deferred Derivation

*We conjecture that the KCR-Cone geometry constitutes a holographic duality of a new class — CR holography — in which the radial direction encodes decoherence depth rather than conformal energy scale, and the effective cosmological constant is positive rather than negative. Establishing this conjecture formally requires deriving the bulk-boundary correspondence, computing the central charge, and identifying the GKPW dictionary. This derivation is deferred to a subsequent paper.*

---

## References

- Maldacena, J. (1997/1998): Original AdS/CFT. *ATMP* 2, 231.
- Ryu & Takayanagi (2006): RT formula. *PRL* 96, 181602.
- Swingle (2012): MERA / holography. *PRD* 86, 065007.
- Van Raamsdonk (2010): Entanglement and geometry. *GRG* 42, 2323.
- Susskind (1995): World as hologram. *JMP* 36, 6377.
- **Strominger (2001): dS/CFT. *JHEP* 10, 034.** [NEW]
- **Maldacena & Susskind (2013): ER=EPR. *FdP* 61, 781.** [NEW]
- **Susskind (2014): Complexity=Volume. *FdP* 64, 24.** [NEW]

