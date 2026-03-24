# §6: Geometric Dark-Matter Response

## §6.1 Framing: From Particles to Geometry

The standard cosmological paradigm addresses missing gravitational mass through particle dark matter—candidates range from WIMPs (Weakly Interacting Massive Particles) to axions to sterile neutrinos. Each invokes new matter beyond the Standard Model, with density profiles fit *a posteriori* to observations. This approach is phenomenologically successful but unsatisfying: it introduces new particles without detection and requires fitting per-system dark matter distributions that correlate mysteriously with baryonic matter.

The KK-Cone model sketches a conditional alternative framework: *if* the KK-Cone warp geometry produces a non-trivial KK mode spectrum with the properties assumed below, *then* the observed dark-matter acceleration profile may be reinterpreted as gravitational signatures of the warped extra dimension, potentially requiring no new particles. In this picture, the warp factor $A(r,z)$ that modulates the metric geometry would directly produce effective forces on brane-localized matter. Perturbations to $A(r,z)$ near the brane—sourced by baryonic matter itself—would generate an additional gravitational potential on the 3-brane. The integrated effect could mimic dark matter without postulating new particle species.

This is fundamentally different from Modified Newtonian Dynamics (MOND). MOND alters the functional form of Newton's law in the infrared limit (e.g., $F \propto a^2$ rather than $F \propto a$ for small accelerations). The KK-Cone keeps Einstein's equations intact in 5D but exploits the geometric structure of the extra dimension to produce an effective 4D gravitational correction. The mechanism is not an ad-hoc modification but a consequence of the warp geometry.

The working hypothesis explored in this section: *if* the KK-Cone warp geometry produces a non-trivial KK mode spectrum with the properties assumed below, *then* the observed dark-matter acceleration profile—particularly the flat rotation curves in galaxies and the tight radial acceleration relation (RAR)—could emerge as a geometric effect of the warped bulk, not from a population of unseen particles.

**Status**: The analysis in this section is schematic. The perturbation equations (Eqs. 6.1–6.5) assume a linearization regime that has not yet been verified against the full 5D Einstein equations on the KK-Cone background of §4. The observational predictions (§6.5) are conditional on this linearization being valid. A complete treatment requires solving the perturbation eigenvalue problem on the canonical metric of §4, which is deferred to future work.

---

## §6.2 Perturbation Setup: Linearized 5D Gravity

We linearize the 5D Einstein equations around the **canonical** KK-Cone background of §4:

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

where $\vec{a}_{\text{Newton}}$ is the Newtonian acceleration from the baryonic mass distribution, and $\delta \vec{a}_{\text{geometric}}$ is the geometric correction arising from the KK modes.

**Newtonian Contribution**

The Newtonian term comes from the zero mode:

$$\vec{a}_{\text{Newton}}(r) = -\frac{G_4 M_b(<r)}{r^2} \hat{r}$$

**(Eq. 6.7)**

where $M_b(<r)$ is the baryonic mass within radius $r$.

**Geometric Correction from KK Modes**

The massive KK modes contribute a correction:

$$\delta \vec{a}_{\text{geometric}}(r) = -\sum_{n=1}^{\infty} \nabla u_n(r) \times (\text{brane coupling})$$

**(Eq. 6.8)**

The sum is dominated by the lowest-mass KK modes ($n=1,2,\ldots$), since higher modes are increasingly suppressed. The key insight is that at large radii $r \gg R_c$, the Yukawa form of the Green's function for the massive modes leads to a different scaling:

$$u_n(r) \sim \frac{m_n}{r} \exp(-m_n r)$$

**(Eq. 6.9)**

For $r \gtrsim 1/m_n$ (i.e., $r$ comparable to or larger than the Compton wavelength of mode $n$), the exponential suppresses the contribution. However, the cumulative effect of all massive modes (which form a continuum-like tower in the limit of a large extra dimension) can produce a long-range correction that falls off more slowly than $1/r^2$.

**Schematic Form for Galaxy-Scale Dynamics**

For a galaxy-scale mass distribution (extended with scale $\sim$ kpc), numerical integration of the KK mode sum would, under the stated assumptions, yield an effective acceleration:

$$\vec{a}_{\text{eff}}(r) \approx -\frac{G_{\text{eff}}(r) M_b(<r)}{r^2} \hat{r}$$

**(Eq. 6.10 — schematic)**

where $G_{\text{eff}}(r)$ is an effective, radius-dependent gravitational coupling that varies as:

$$G_{\text{eff}}(r) = G_4 \left[1 + \alpha \frac{R_c}{r} + \mathcal{O}\left(\frac{R_c^2}{r^2}\right)\right]$$

**(Eq. 6.11 — schematic)**

Here $\\alpha$ is a dimensionless coefficient determined by the warp profile and the KK mode spectrum, and $R_c$ is the characteristic size of the extra dimension. The second term is the geometric correction. At very large radii ($r \\gg R_c/\\alpha$), the correction becomes small relative to the Newtonian term, but at intermediate radii (galactic scale, $\\sim$ 10-50 kpc), it can be substantial. These expressions are schematic, illustrating possible $G_{\\text{eff}}(r)$ behavior under an appropriate KK spectrum; they are not derived from a completed 5D eigenmode calculation. See Appendix B (`papers/02-saturation-dynamics/sections/patched/paper2_appendix_B_Geff_KK_tower_PATCHED.md`) for a compact asymptotic motivation.

**Rotation Curve Implication**

For circular orbits in a thin disk, $v_{\text{circ}}^2 = r \cdot a_{\text{eff}}(r)$. If $G_{\text{eff}}(r)$ increases with $r$ (or decreases more slowly than expected), the rotation curve becomes flatter. In the simplest schematic picture where the geometric correction grows like $1/r$ at large radii:

$$\delta a_{\text{geometric}} \sim -\frac{\beta G_4 M_b}{r}$$

**(Eq. 6.12)**

with $\beta$ a small dimensionless constant. This would produce a flat rotation curve $v_{\text{circ}} \approx \text{const}$ in the outer galaxy under the stated assumptions, without requiring a dark-matter halo. Under these assumptions, the correction would be sourced entirely by baryonic matter, with no separate dark-matter density parameter.

---

## §6.4 Distinguishing Features of the Geometric Model

### Baryon-Dark-Matter Correlation

A profound puzzle in dark-matter phenomenology is why dark matter and baryons are so tightly correlated. The Radial Acceleration Relation (RAR)—the tight correlation between total (observed) gravitational acceleration and baryonic acceleration—has no obvious explanation in the ΛCDM model, where dark matter follows from collisionless N-body dynamics independent of baryon physics.

In the geometric KK-Cone model, this correlation would be **structural** (built into the geometry rather than coincidental):

$$\delta a_{\text{geometric}}(r) = f\left(\rho_b(r), A(r,z), u_n,\chi_n(r_0)\right)$$

**(Eq. 6.13)**

The geometric correction depends directly on the baryonic density profile $\rho_b(r)$ (through the source term in Eq. 6.2) and the warp geometry. There is no separate, stochastically formed dark-matter halo—the apparent "dark matter" would be the gravitational shadow of the geometry itself. Consequently, wherever baryons are dense, the geometric response would be strongest; where baryons are sparse, the response would be weak. This explains the observed tight baryon-dark-matter coupling naturally, without fine-tuning, *if the linearization of §6.2 is valid*.

### No Free Dark-Matter Density Parameter

Traditional dark-matter models fit a dark-matter density profile (e.g., Navarro-Frenk-White or isothermal) to each galaxy. This introduces a free parameter: the dark-matter halo mass or concentration. The geometric model would, if the linearization holds, eliminate this freedom—the response would be determined entirely by:

1. The observed baryonic mass distribution
2. The warp geometry (specifically, $A(r,z)$ and the KK spectrum)
3. Physical constants ($G_5, R_c$)

Once the warp parameters are fixed by fitting one class of objects (e.g., rotation curves of a sample of spiral galaxies), the model's predictions for other observables (dwarf galaxies, elliptical galaxies, lensing, CMB) are constrained, not free to adjust.

### Deterministic Response

The geometric correction would be deterministic under the assumptions of §6.2—there is no analog of dark-matter halo scatter. Different galaxies with identical baryonic distributions (and the same warp geometry) would have identical apparent dark-matter distributions. This is in striking contrast to ΛCDM simulations, where halos with the same total mass have significant variations in substructure and spatial distribution.

Observationally, this predicts that the scatter in dark-matter properties (for fixed baryon distribution) should be very small—a specific prediction testable against high-resolution hydrodynamical simulations.

---

## §6.5 Observational Predictions

**Status**: The predictions below are conditional on the schematic linearization of §6.2. They should be treated as directional indicators, not quantitative forecasts, until the perturbation eigenvalue problem on the canonical KK-Cone metric is solved.

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
- **Halo scatter**: If hydrodynamical simulations incorporating the KK-Cone geometry show significant scatter in geometric response for identical initial baryonic profiles, the model is falsified.

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

The linearized analysis assumes the KK-Cone background is stable under small perturbations. Quantum corrections (one-loop, higher-loop) to the warp profile must be computed to ensure stability. If quantum backreaction significantly modifies $A(r,z)$, the predictions change.

### Non-Linear Regime and Cluster Dynamics

The linearization breaks down for high-contrast structures (e.g., galaxy clusters where $\delta A / A_0 \sim 0.1$ or larger). Non-linear solutions to the 5D Einstein equations are required to model clusters. This is a substantial computational challenge but necessary for precision predictions.

### Relation to MOND and TeVeS

The geometric model superficially resembles MOND (both produce flat rotation curves) but differs fundamentally in mechanism. A detailed comparison—including quantitative predictions for systems where MOND and the geometric model diverge—would clarify the relationship and may enable observational discrimination.

### Dark Energy and the Warp Sector

The cosmological constant problem and the observed accelerated expansion (typically attributed to dark energy) are not directly addressed here. The warp geometry might also contribute to dark-energy phenomena; investigating whether a unified treatment of "dark" phenomena (dark matter + dark energy) emerges from the KK-Cone is compelling.

---

## Conclusion

The geometric dark-matter response in the KK-Cone model provides an intriguing conditional alternative to particle-based dark matter. If the schematic analysis survives a full perturbation treatment on the canonical KK-Cone metric, the geometric mechanism would provide a natural explanation for:

- **Flat rotation curves** without dark-matter halos
- **Baryon-dark-matter correlation** (the tight RAR) as a geometric consequence, not a coincidence
- **Deterministic structure** with no free dark-matter density parameters

The model is falsifiable through observations of rotation curve shapes, baryon-dark-matter correlation breakdown, direct dark-matter detection, and large-scale structure surveys. Current data do not yet exclude this schematic scenario, but no quantitative global fit is claimed here; future precision measurements will provide decisive tests. If the geometric treatment holds, the geometry of the extra dimension may contribute to or account for the observations, offering a different perspective than invisible particles.

The burden of proof shifts to §7–§8, where the equations of motion on M × Σ and the full perturbation spectrum must be computed.

---

**References and Further Reading**

This section builds on the KK-Cone formalism established in §3 and §4, the perturbation theory of §5, and the linearized analysis of warp-factor dynamics. Detailed numerical results and comparisons with observational datasets will be presented in subsequent papers.
