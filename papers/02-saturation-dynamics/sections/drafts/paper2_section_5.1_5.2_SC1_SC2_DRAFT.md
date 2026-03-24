# §5 Self-Consistency Conditions: SC1 (Flatness) and SC2 (Gravity Localization)

## Overview

Having established in §4 the canonical KK-Cone metric with Hopf-fibered internal space, we now examine what it means for this geometry to be **self-consistent** with observed physics. This section develops two of the three self-consistency conditions that the warp factor $A(r,z)$ must satisfy simultaneously:

1. **SC1 (Flatness Condition):** The observed universe is spatially flat ($\Omega_k \to 0$) as measured at late cosmological times.
2. **SC2 (Gravity Localization):** Standard 4D Newton's law holds at accessible scales, with no detectable fifth force.

These conditions do not determine $A(r,z)$ uniquely; rather, they define a **class** of admissible warp profiles. The combined system SC1 + SC2 further constrains this class, but does not close it completely—a third condition, SC3 (effective cosmological constant), is required. The present section establishes the mathematical structure of SC1 and SC2 and shows how their interplay restricts the radial profile $f(r)$ in the asymptotic form $A \sim z \cdot f(r)$.

---

### Notation Convention: Warp Factor

In §4, the KK-Cone metric was written using the Randall–Sundrum convention $e^{2\mathcal{A}(r,z)}$, where $\mathcal{A}$ is the warp *exponent*. Beginning in this section and continuing through §7–§8, we adopt a simplified notation in which $A(r,z)$ denotes the warp *factor* (scale factor) directly:

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

In the limit of high precision, we take $\Omega_k \to 0$, meaning that the spatial sections of the universe are **flat** to observable accuracy. On the KK-Cone, the brane observers at fixed $r = r_{\text{brane}}$ measure curvature through the intrinsic metric of constant-$z$ slices. For the universe to appear flat to these observers, the effective spatial curvature must vanish.

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

The first term is the standard Newtonian result. The second term represents KK corrections—modifications due to the excitation of massive KK graviton modes in the bulk. These corrections are suppressed as $(\ell/\mu^{-1})^2$, which for $\ell \ll \mu^{-1}$ is very small.

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
- The existence of a mass gap: the first excited graviton KK mode has a mass $m_1 \sim \mu$, which suppresses its production at low energies.

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

The effective 4D Planck mass is determined by the Gauss-Codazzi KK reduction:

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

The massive KK graviton modes satisfy the Sturm-Liouville equation:

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

**Physical interpretation:** The non-conformal SC2 metric produces a *smaller* self-consistent $\mu L_*$ than the conformal case would, which pushes the KK mass gap *higher* and the Yukawa range *shorter*. This is the mechanism by which $p = 1$ (seemingly "less localized" than $p = 2$) actually produces a *stronger* fifth-force suppression. The key is that small $p$ demands small $\mu L_*$ for self-consistency, and small $\mu L_*$ means heavy KK modes.

### §5.2.8.5 Radion Normalization

The radion kinetic normalization integral is:

$$
Z_L = 6 M_5^3 \mu^2 \int_0^{L_*} n(r) \cdot a(r)^3 \, \mathrm{d}r = 2 M_5^3 \mu \left(1 - e^{-3\mu L_*}\right)
\tag{5.2.8.9}
$$

The weight is $n \cdot a^3 = 1 \cdot A^3 = A^3$ (not $A^2$ as would follow from a naive conformal generalization; see the Radion Z_L Correction assessment). The RS1 cross-check gives $Z_L^{\text{RS1}} = \tfrac{3}{2} M_5^3 \mu (1 - e^{-4\mu L_*})$, matching the Goldberger-Wise result.

The radion contributes a tier-2 fifth force with Planck-suppressed coupling ($\alpha_{\text{rad}} \sim 10^{-58}$), which is negligible compared to the tier-1 KK graviton contribution and far below experimental sensitivity.

### §5.2.8.6 Summary of Quantitative SC2 Results

| Quantity | SC2 Value | RS1 Value (cross-check) |
|----------|-----------|------------------------|
| Graviton weight $p$ | 1 | 2 |
| Self-consistent $\mu L_*$ | 0.2007 | (depends on $R_{\text{DM}}$) |
| Extra-dimension size $L_*$ | $\sim 13 \, \mu\mathrm{m}$ | $\sim$ mm-scale |
| First KK mass $m_1/\mu$ | $\approx 15.7$ | $\approx 3.83$ |
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
- Is consistent with the topological structure of the KK-Cone.
- Satisfies the necessary conditions SC1 and SC2.
- Admits numerical evaluation to test SC3 compatibility.

It is **not justified** by an a-priori analytical derivation from first principles. The "true" self-consistent $A(r,z)$, if it exists, may have a different form—or may not exist at all for generic parameter values, in which case the KK-Cone model itself would be ruled out.

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

- **§4:** The KK-Cone metric ansatz and coordinate structure.
- **§3:** Topological derivation of the Hopf fibration and its role in the coherence frame (from Paper 3).
- **§5.3 (upcoming):** SC3, the effective cosmological constant, and the closure of the full system.

---

*Word count: ~4,800 words | Status: DRAFT | Equations: 5.1.1–5.2.7.5 | Claims: SC1 & SC2 structurally closed; SC1+SC2 combined leaves one degree of freedom; full analytical derivation unsolved.*
