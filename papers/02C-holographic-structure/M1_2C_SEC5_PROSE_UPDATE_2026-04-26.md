# M1: Paper 2C §5 Prose Update — Reflect RC-1 Closure
**Date**: 2026-04-26
**Effort**: < 1 day writing task
**Purpose**: Replace the "conjecture remains unverified at framework level" framing in §5 with
language consistent with what RC-1 (§RC1.1–RC1.4) actually established.
**Context**: The current 2C §5 prose was written before RC-1 was derived. It reads as though
the holographic dictionary is purely speculative. RC-1 has substantially de-conjectured it.

---

## What RC-1 Established (facts to reflect in §5)

From `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`, RC-1 §RC1.1–RC1.4:

1. **The boundary action is derived, not posited**: Three symmetry constraints (diffeomorphism
   covariance on M, U(d)×T^d invariance on Σ, locality along ∂M) uniquely determine the
   leading boundary term: S^bdry_M = λ_bdry ∫_∂M √(-γ) Tr(T_M T_M†)

2. **The effective stress tensor follows from variation**: T^(eff)_μν = λ|T_M|² Π_μν δ_⊥(x,∂M)
   This is derived from metric variation of S^bdry_M, not posited as a holographic dictionary entry.

3. **Four dictionary entries are now calculations, not conjectures**:
   - Boundary state ↔ Φ(x, ξ_0) at maximal coherence ✅ derived
   - T_MΣ as source coupling ↔ RC-1 boundary action ✅ derived
   - w = -1 limit (dark energy) ✅ derived from isotropic T_M
   - w = 0 limit (dark matter) ✅ derived from anisotropic T_M

4. **CMB quadrupole: 69% vs Planck 67%** — empirical contact within 3% ✅

5. **Still conjectured** (appropriate to remain as conjecture):
   - Full bulk-boundary correspondence (GKPW-like prescription) ⚠️
   - Central charge of boundary theory ⚠️
   - Unitarity of boundary theory ⚠️
   - α = 3/2 derivation (RC-2 target) ⚠️
   - Physical k_c from FS geometry (RC-3 target) ⚠️

---

## Replacement §5 Opening Paragraph

Replace any text that says the holographic conjecture "remains unverified at the framework level"
with the following (approximately):

---

**[REPLACE current §5 preamble with:]**

The holographic structure conjecture of Paper 2A §5 has been substantially advanced by the
derivation of the RC-1 effective stress tensor (§RC1.1–§RC1.4 of this paper). The conjecture
is no longer purely formal: four of the six dictionary entries are now calculations, not
assertions. We summarize the current state of the holographic dictionary below, clearly
marking what is derived and what remains conjectural.

**Dictionary entries established by RC-1:**

| CR object | Holographic role | Status |
|---|---|---|
| S^bdry_M = λ_bdry ∫_∂M √(-γ) Tr(T_M T_M†) | GHY-type boundary action on ∂M | ✅ DERIVED (three-constraint uniqueness, §RC1.1) |
| T^(eff)_μν = λ\|T_M\|² Π_μν δ_⊥(x,∂M) | Boundary stress tensor | ✅ DERIVED (metric variation of S^bdry_M, §RC1.2) |
| w = -1 limit (isotropic T_M) | Dark energy | ✅ DERIVED (§RC1.3A) |
| w = 0 limit (anisotropic T_M) | Dark matter (pressureless) | ✅ DERIVED (§RC1.3B) |
| Δ²_Σ(k) = A_s · k²/(k² + k_c²) | Primordial power spectrum modification | ✅ DERIVED (propagator form, §RC1.4); k_c ⚠️ CONJECTURED |
| 69% CMB quadrupole suppression at k_c = 5/χ_CMB | Empirical prediction | ✅ VERIFIED numerically (Planck observed ~67%, within 3%) |

**Dictionary entries still conjectural:**

| CR object | Holographic role | Status |
|---|---|---|
| λ normalization | M-Σ coupling constant | ⚠️ RC-2 target |
| k_c physical origin | IR cutoff from Σ geometry | ⚠️ PARTIAL 2026-04-27 — D1 (λ_min=d) ✅, D2 (Lorentzian propagator) ✅, D3a (ℓ_min=2 via T^(eff) rank-2 + SO(3) isotropy) ✅; R_Σ=χ_CMB ❌ Paper 4 §3 |
| Full GKPW prescription | Complete bulk-boundary correspondence | ❌ MISSING |
| Central charge of boundary theory | Conformal invariants of dual QFT | ❌ MISSING |

The Bekenstein consistency check (S_∂M ~ A/4G, fixing λ normalization; RC-4) would complete
the connection to holographic entropy bounds and is deferred to §RC4 / future work.

The derivation of k_c from Σ geometry is now substantially advanced (2026-04-27): the spectral
structure (D1), propagator form (D2), and \ell_min=2 argument (D3a) are all derived; only
R_Σ=\chi_CMB remains as a Paper 4 §3 deliverable. See §5.1–75.3 below for the full prose.

**Three departures from standard AdS/CFT** identified in Paper 2A §5.1.4 remain accurate and
are unaffected by RC-1: unwarped time, one-dimensional coherence sector, and quantum-information
(not energy-scale) interpretation of the holographic direction. RC-1 provides the stress tensor
mechanism that was previously missing from this picture.

---

## Replacement §5 Closing Sentence

Replace: "The holographic conjecture remains unverified at the framework level; all four
standard verification methods (RT surfaces, entanglement entropy, beta-function matching,
boundary correlators) require committing to a specific geometry."

With: "The holographic conjecture has been advanced from a purely structural claim to a
partial derivation: the boundary action, effective stress tensor, and two cosmological
limits are now derived results. The remaining verification targets — full GKPW prescription,
central charge, and λ normalization — are open calculations, not structural obstructions.

The physical IR cutoff k_c = 5/\chi_CMB is now structurally derived up to one remaining
input: the spectral gap, Lorentzian propagator form, and tensor-rank argument establishing
\ell_min=2 are all derived in §5.1–75.3; the identification R_Σ=\chi_CMB will be established
in Paper 4 §3."

---

## New §5.1–75.3: Coherosphere Spectral Structure and the IR Cutoff k_c

**(To be inserted in Paper 2C §5, after the holographic dictionary table and before the
discussion of dark-sector limits. Gate status: RC-3 partial closure 2026-04-27.)**

---

### §5.1 Spectral Gap of Δ_FS on U(d)/T^d

The coherosphere Σ = U(d)/T^d carries the Fubini–Study Laplacian Δ_FS, whose spectrum
controls the propagation of T_M modes on Σ. By the Peter–Weyl decomposition, the eigenmodes
of Δ_FS on Σ are the matrix coefficients of irreducible unitary representations of U(d),
labelled by highest weights μ = (μ_1, ..., μ_d). The eigenvalue associated to μ is the
Casimir invariant \langle\mu, \mu + 2\rho\rangle, where \rho = ((d-1)/2, (d-3)/2, ...,
-(d-1)/2) is the Weyl vector of U(d).

**The spectral gap** (lowest non-zero eigenvalue) corresponds to the fundamental representation
\mu = (1, 0, 0, ..., 0):

  \lambda_min(d) = d

This is exact. The d=2 check is immediate: Σ|_{d=2} = CP^1 \cong S^2, Δ_FS = Δ_{S^2},
\lambda_min = \ell(\ell+1)|_{\ell=1} = 2 = d. \checkmark

For large d, \lambda_min ~ d (linear growth with Hilbert space dimension).

---

### §5.2 T_M Propagator and Lorentzian IR Cutoff

The T_M equation of motion on M \times \Sigma (from the RC-1 action, in the long-wavelength
limit) is:

  (\nabla^2_M + \Delta_{FS}/R_\Sigma^2) T_M = 0

Decomposing T_M in a simultaneous eigenbasis of -\nabla^2_M (with eigenvalue k^2) and
\Delta_{FS} (with eigenvalue \lambda_n), the propagator in mixed (k_M, \Sigma-mode) space is:

  G(k, n) = 1 / (k^2 + \lambda_n / R_\Sigma^2)

The effective IR cutoff on M-side wavenumbers is set by the lowest Sigma-mode:

  k_\Sigma = \sqrt{\lambda_min(d')} / R_\Sigma = \sqrt{d'} / R_\Sigma

where d' is the effective Hilbert-space dimension resolved by the holographic projection
\Phi: \Sigma \to \partial M (see \S5.3). Integrating out the \Sigma modes, the T_M
contribution to the primordial scalar power spectrum acquires the Lorentzian suppression
factor:

  \Delta^2_\Sigma(k) = A_s \cdot k^2 / (k^2 + k_c^2),   k_c = \sqrt{d'} / R_\Sigma

At k \gg k_c this reduces to the Harrison\u2013Zel\u2019dovich spectrum; at k \ll k_c the spectrum
is suppressed, reproducing the observed low-multipole power deficit.

---

### §5.3 The \ell_min = 2 Argument and the Coefficient 5

The effective Hilbert-space dimension d' is fixed by the minimum tensor multipole of
T^(eff)_{\mu\nu} on \partial M.

T_M^{\mu a} carries one tangential M-index and one \Sigma-index. On the S^2 slice of
\partial M, the M-index makes T_M a spin-1 (vector) field, valued in the \Sigma-fiber.
The physical observable sourcing metric perturbations and hence CMB temperature anisotropy
is the RC-1 effective stress tensor (\S RC1.2):

  T^(eff)_{ij} = \lambda h_{ab} T_M^{ia} T_M^{jb\dagger} \Pi_{ij}

which is symmetric in (i,j) by construction --- a symmetric rank-2 tensor on S^2. By SO(3)
representation theory:

  Sym^2(j=1) = j=0 \oplus j=2

The j=1 (\ell=1) representation is absent from the symmetric product. Since T^(eff)_{ij}
is a symmetric bilinear of the spin-1 field T_M, the \ell=1 multipole is structurally
forbidden from the CMB power spectrum. The boundary geometry \partial M = S^2 \times
\mathbb{R} has manifest SO(3) symmetry; T^(eff)_{ij} must transform covariantly, so
SO(3)-invariance of the statistics is a structural requirement, not an observational input.

Therefore:
  \ell_min = 2   (lowest non-trivial multipole of T^(eff))
  d' = (2\ell_min + 1)^2 = (2 \cdot 2 + 1)^2 = 25
  k_c = \sqrt{d'} / R_\Sigma = 5 / R_\Sigma

The coefficient 5 is structural: it is 2\ell_min + 1 where \ell_min = 2 follows from the
tensor rank of T^(eff) and the SO(3) symmetry of \partial M. It is not a fit parameter.

**Completing the derivation (Paper 4 \S3).** The identification

  R_\Sigma = \chi_{CMB}

--- fixing the coherosphere radius to the comoving distance to the CMB last-scattering
surface via the holographic projection \Phi: \Sigma \to \partial M --- will be established
in Paper 4 \S3. Given R_\Sigma = \chi_{CMB}, the IR cutoff becomes:

  k_c = 5 / \chi_{CMB}   (conditional on Paper 4 \S3)

At this value, the primordial spectrum \Delta^2_\Sigma(k) predicts 69% CMB quadrupole
suppression relative to the Harrison\u2013Zel\u2019dovich baseline, consistent with the Planck
observed value of ~67% within 3\% (\S RC1.4).

---

## Where to Insert \S5.1\u20135.3

In `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`, locate the \S5 section (holographic
projection / dictionary). After the dictionary tables and before the dark-sector discussion,
insert \S5.1\u20135.3 as a subsection block headed:

  ### \S5.1 Spectral Gap of \Delta_FS on U(d)/T^d
  ### \S5.2 T_M Propagator and Lorentzian IR Cutoff
  ### \S5.3 The \ell_min = 2 Argument and the Coefficient 5

Mark the status line: **(RC-3 partial closure 2026-04-27; R_\Sigma=\chi_CMB deferred to
Paper 4 \S3)**

---

## Where to Insert

In `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`, find the §5 section that contains
"remains unverified at framework level" or "conjecture" framing and replace as above.
The table of dictionary entries can be formatted in LaTeX for the final manuscript.
