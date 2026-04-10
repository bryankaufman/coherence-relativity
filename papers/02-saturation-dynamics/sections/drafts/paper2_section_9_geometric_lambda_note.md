# §9 Discussion — Geometric Λ Insert
**Date:** 2026-04-09
**Status:** ADDENDUM — insert into §9.1 (Summary of Results) and §9.4 (What Remains Open)
**Target file:** paper2_section_9_discussion_UPDATED.md
**Action for Warp:** Splice these two blocks into the §9 UPDATED draft at the locations marked below.

---

## Insert 1: Into §9.1 after the SC3 paragraph

*Location:* After the sentence "...a falsifiable, not-yet-falsified prediction accessible to near-future short-range gravity experiments." in §9.1 Summary of Results.

---

**Geometric origin of the cosmological constant (§5.3, OP-24 resolution).** A structural finding that emerged from the Klein-removal analysis (OP-24, resolved 2026-04-09) shifts the interpretation of SC3. The 5D Einstein equations for the derived metric $\mathrm{d}s^2 = A^2(r)\eta_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu + \mathrm{d}r^2$ with warp factor $A(r) = \cos(\sqrt{2}\,r)$ contribute a positive effective 4D energy density directly from the $A^4$-weighted curvature integral:

$$\rho_\mathrm{geom}^{(4D)} = \frac{3M_5^3 k^2}{s} \int_0^{r_\mathrm{max}} A^4(r)\,\mathrm{d}r = +\frac{3.534\,M_5^3 k^2}{s} > 0 \tag{9.1.*}$$

where $s$ is the cosmological scale factor and $k^2 = 2$ is the Fubini-Study eigenvalue. The Gibbons-Hawking-York boundary term at the pinch-off ($r = r_\mathrm{max}$, where $A = 0$) vanishes. This is a classical result: no quantum fields are required. The cosmological constant therefore has a geometric origin in the warp-factor curvature energy, and the Casimir vacuum energy on the derived interval $[0, L]$ is a subleading quantum correction:

$$\rho_\Lambda = \underbrace{\rho_\mathrm{geom}(s)}_{\text{geometric (primary)}} + \underbrace{\rho_\mathrm{Cas}(s)}_{\text{quantum correction}} \tag{9.1.**}$$

The Friedmann equation $H^2 = (8\pi G_4/3)[\rho_\mathrm{geom}(s) + \rho_\mathrm{Cas}(s)]$ then determines the physical scale $s$ dynamically. Non-traversability ($\dot{r} \geq 0$, Proposition 4.2) ensures $s$ is monotonically non-decreasing, recovering cosmological expansion without fine-tuning.

Three consequences follow from this reordering:

1. **OP-5 resolved.** The radion stabilization problem — no $V_\mathrm{eff}$ minimum demonstrated — is dissolved by recognizing that the shape modulus has zero modes (topologically frozen by $k^2=2$, a Fubini-Study eigenvalue condition) and the scale is set by the Friedmann balance rather than a separate potential. Neither Paper 3 species inputs nor Goldberger-Wise tuning is required at leading order.

2. **SUSY sectors now allowed.** The earlier sign condition $f = 7N_F/8 - N_B > 0$ was required to make the Casimir energy positive. With geometric Λ as the primary source (positive by construction), the Casimir correction can be negative ($f < 0$, SUSY sectors) and still leave $\rho_\Lambda > 0$ net. The field-content selection from SC3 changes from a hard exclusion of SUSY to a quantitative comparison of Casimir corrections.

3. **Casimir scale reinterpreted.** The earlier radius prediction $r_f^* \approx 21.82\,\mu\mathrm{m}$ (from $\rho_\mathrm{Cas} = \rho_\Lambda^\mathrm{obs}$) is reinterpreted as the scale at which the quantum Casimir correction saturates the observed dark energy density. This remains a falsifiable prediction at the $10$–$50\,\mu\mathrm{m}$ scale; it is now a correction-level rather than leading-order prediction.

---

## Insert 2: Into §9.4 (What Remains Open)

*Location:* Replace the paragraph beginning "The most critical open problem is radion stabilization (OP-5)..." with the following.

---

**OP-5 (radion stabilization) — resolved.** The radion stabilization problem (no $V_\mathrm{eff}$ minimum demonstrated) is resolved by the geometric Λ analysis (§5.3, OP-24). The resolution has two parts. First, the shape modulus of the derived interval is topologically frozen: $k^2 = 2$ is a Fubini-Study eigenvalue condition, not a free parameter, so there are zero shape moduli and no shape instability. Second, the scale degree of freedom (the cosmological scale factor $s$) is stabilized dynamically by the Friedmann balance $H^2 = (8\pi G_4/3)\rho_\mathrm{geom}(s)$, which has $s$ as a cosmological attractor rather than a runaway. No Goldberger-Wise mechanism, no Paper 3 species input, and no tuned potential are needed. OP-5 is closed.

The field-content question from SC3 remains open in a weaker form: the Casimir correction $\rho_\mathrm{Cas}$ depends on the post-transition species count $f = 7N_F/8 - N_B$, which is determined by Paper 3 boundary conditions. This no longer blocks the SC3 result but does affect the subleading prediction for the Casimir correction scale $L_\mathrm{Cas}^*$.

The most testable near-term prediction is now the non-linear KK graviton spectrum: $m_n/m_1 \approx 1, 1.67, 2.32, 2.97$ from the volcano potential on the derived interval, versus Klein's linear spacing $1, 2, 3, 4$ from the circle harmonics. The first genuine KK graviton has $\lambda_1 \approx 13.3\,\mu\mathrm{m}$, safely below the Lee et al.\ (2020) ISL bound of $44\,\mu\mathrm{m}$. Short-range gravity experiments at the $10$–$50\,\mu\mathrm{m}$ scale can distinguish these spectra; any observed non-linearity would directly confirm the derived-interval picture over Klein's ad hoc circle.

---

## Revision Note

The §9.1 SC3 paragraph and the §9.4 OP-5 paragraph in `paper2_section_9_discussion_UPDATED.md` should be replaced/supplemented with the above inserts. No other changes to §9 are required by this dispatch.

**Verification:** §9.1 insert references Eq. (9.1.*) and (9.1.**) — these should be renumbered to fit the assembled equation sequence. The numerical values ($3.534$, $21.82\,\mu\mathrm{m}$, $13.3\,\mu\mathrm{m}$, $44\,\mu\mathrm{m}$) are sourced from OP-24 resolution (COORDINATION.md, 2026-04-09) and SC3 v2 numerics.
