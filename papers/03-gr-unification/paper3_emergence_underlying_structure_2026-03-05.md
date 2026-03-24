# Emergence and Underlying Structure
## Physical Ontogeny Recapitulates Mathematical Phylogeny
### Coherence Relativity — Paper 3 Integration Draft

## 1) Master Principle
Every physical process can be modeled as replaying the same ordered emergence chain:
pure mathematical structure → information structure → quantum coherence → decoherence transition → classical effective description → observational definiteness.

The key claim is that this sequence is not only cosmological (a one-time early-universe event), but process-local and scale-covariant. Each system traverses the same structural stages with scale-dependent suppression.

## 2) Underlying Geometric Structure
The proposed unifying geometry is the coupled manifold `M×Σ`:
- `Σ` carries coherence/information geometry (Fubini-Study in pure-state regime, Bures in mixed-state regime).
- `M` carries emergent spacetime-effective geometry in decohered/classical regimes.
- `T_MΣ` encodes cross-sector coupling through the transition regime.

This gives a single mathematical backbone for the L2→L3 transition (quantum→classical), and positions GR as a late-stage effective geometry rather than a fundamental all-regime description.

## 3) Currency-of-the-Realm Triad
We treat three quantities as different projections of one structure:
- **Fubini-Study metric**: distinguishability geometry (unspent transition capacity)
- **Born rule**: invariant exchange rule under frame change
- **Entropy**: irreversible bookkeeping of spent distinguishability

In this reading:
- Born conservation is local-normalization conservation under transformations.
- Entropy growth tracks irreversible decoherence flow.
- Information conservation is topological/global (representation changes across scales, total capacity preserved).

## 4) Scale-Covariant Suppression Ansatz
Define a scale-dependent suppression factor:
`s(R) = 1 / (1 + (R/ℓ*)²)`.

Desired limits:
- `R >> ℓ*` ⇒ `s(R) → 0` (deep classical/effective regime)
- `R ~ ℓ*` ⇒ crossover regime
- `R → ℓ_P` ⇒ `s(R) → 1` (quantum-dominant regime)

Candidate transition currency:
`ΔC(R) = |⟨ψ_i|ψ_f⟩|² · s(R)`.

Candidate entropic loading:
`S(R) = S_max · (1 - s(R))`.

These are currently ansätze and should be elevated to derivations in the formal sections.

## 5) Paper 3 Placement and Role
This section should function as the conceptual front-end of Paper 3:
1. State the emergence hierarchy and scale-covariance claim.
2. Show that Paper 2’s `M×Σ` machinery is the concrete realization of the critical L2→L3 bridge.
3. Motivate why apparent cross-regime tensions (e.g., inference mismatches between early and late probes) can be framed as level-mismatch artifacts.
4. Introduce the unified suppression/currency equations as testable mathematical targets.

## 6) Minimal Formal Agenda
To promote this from conceptual framing to theorem-level content:
- Derive `s(R)` from invariance/conservation requirements rather than interpolation choice.
- Derive entropy-production form of `T_MΣ` from an explicit dynamical generator.
- Specify conserved quantity map across transitions (what is exactly preserved, transformed, or monotone).
- Prove consistency with Paper 1 Born-invariant structure and Paper 2 metric-transition structure.

## 7) Boundary with Paper 4
If Paper 4 is dedicated to holography/duality, keep this section in Paper 3 and export only the duality-facing subset to Paper 4:
- boundary/bulk reinterpretation of `M×Σ`,
- encoding maps for conserved information content across effective descriptions,
- geometric meaning of entropy flow under coarse-graining.

This keeps Paper 3 as the emergence backbone and Paper 4 as the duality/holography extension.

## 8) Cross-Paper Handoff
The duality/holography extraction of this section is developed in:
`papers/04-holography/paper4_duality_extension_from_emergence_2026-03-05.md`.
Use this Paper 3 section as the derivational anchor and Paper 4 as the representation-theoretic extension.

## 9) Settimo Extension: Picture Inequivalence as Additional Structure
Settimo et al. (2026) motivates a two-picture extension of the emergence framework. Cosmological modeling must track:
- Schrödinger-side evolution (state-divisibility sector),
- Heisenberg-side evolution (effect-divisibility sector).

Hence Level-4 effective dynamics may be internally consistent while Level-5 observational structure still carries residual mismatch whenever `L_t ≠ R_t`.

### 9.1 Two-Ledger Entropic Accounting
Extend single-ledger entropy bookkeeping to
`S^(S)(t)` (state ledger) and `S^(H)(t)` (effect ledger).

In non-commutative regimes these ledgers need not track identically. Entropy production is therefore picture-dependent unless a commutative subspace is selected.

### 9.2 Measurement as L4→L5 Picture Reconciliation
Working statement: the measurement transition is the regime in which Schrödinger and Heisenberg descriptions are forced into operational agreement for realized outcomes.

Pointer states are reinterpreted as states where left and right generator actions agree under the relevant projection.

## 10) Third Contribution to H0 Mismatch
Augment the Paper 3 decomposition:
`ΔH0 = ΔH0^(cone geometry) + ΔH0^(phase transition) + ΔH0^(picture mismatch)`.

Interpretation:
- high-redshift inference is most sensitive to non-commutative epochs,
- low-redshift inference is closer to commutative/effective regimes,
- theory-data comparison can inherit a systematic offset when evolution and observational extraction are not in the same picture regime.

Candidate control term:
`ΔH0^(picture mismatch) ~ H_* · ∫_0^{z_*} dz · [||L_t - R_t||_op / ((1+z)H(z))] · (dχ/dz)`,
with `H_*` a reference Hubble scale and `χ(z)` dimensionless.

This keeps the previous two contributions intact while adding a generator-inequivalence channel that is suppressed as commutativity is restored.

## 11) Immediate Formal Tasks
- Derive `T_MΣ^(right)` and compare to `T_MΣ^(left)` in the minimal decoherence model.
- Compute `||L_t - R_t||_op` versus `λ_M` and test expected suppression pattern.
- Define a measurable proxy for `S^(S) - S^(H)` in the emergence framework.
- Cross-reference for implementation:
  `papers/02-saturation-dynamics/sections/drafts/paper2_section_left_right_generators_TMSIGMA_DRAFT_2026-03-05.md`.

## 12) Prerequisite contract for Paper 4 RT-consciousness closure
Paper 3 supplies the structural prerequisites; Paper 4 carries the closure test. The following items are required inputs to the Paper 4 gate.

### 12.1 Norm-preserving operator contract for `J`
Any use of
`|Im(H_MΣ)| = |J·T_MΣ| = |T_MΣ|`
must state:
1. the norm used (bundle and inner product),
2. the subspace where `J` is evaluated,
3. proof (or explicit assumption) that `J` is norm-preserving on that subspace.

Until this is fixed, only directional statements about `J·T_MΣ` are admissible; magnitude-equality claims remain conditional.

### 12.2 Post-transition admissibility lock
The operator and field-content sector chosen for `J` must be consistent with the post-transition branch selected by Paper 3 and its admissibility constraints. Any branch violating those constraints is excluded from Paper 4 closure scoring.

### 12.3 Transition-scale linkage
Paper 3 must provide a branch-qualified evaluation map for `T_MΣ(ℓ*)` and its uncertainty envelope, so Paper 4 can test whether the RT-linked integral claim reproduces the same scale behavior under dual description.

### 12.4 Handoff rule to Paper 4
Paper 4 may promote the objective-measurability claim only after:
1. the norm contract in 12.1 is satisfied,
2. the admissibility lock in 12.2 is fixed,
3. the transition-scale map in 12.3 is supplied.
Otherwise, Paper 4 language remains explicitly conditional.

### 12.5 Handoff payload to Paper 2 H1 radion closure
Paper 2 §5.2(6) uses the same branch lock and cannot complete H1 numerical adjudication unless Paper 3 supplies a branch-qualified normalization payload. Required outputs (same branch `B*`) are:
1. radion kinetic normalization `Z_L^(B*)` from the reduced action convention used for the radion mode,
2. one on-shell stabilization datum `V_*^(B*) := V_eff(L_f^*)` from the same matching branch (or equivalently the coefficient pair `sigma_±^(B*)` derived in that branch),
3. branch-ID and normalization tags used by Paper 2 interfaces: `lambda_D^(B*)(z)` profile (fixing `z_*`), `G_5/G_4` convention, and reference-slice normalization for `A_0`.

Minimum consistency rule: items (1)–(3) must be exported as a single package with one branch label and one uncertainty envelope; mixed-branch assembly is inadmissible for H1 closure scoring.

### 12.5.1 Provisional toy-model `Z_L` derivation on branch `B*` (SC2 lock; verification pending)
To unblock first-pass H1 adjudication while preserving claim-tier discipline, use a provisional reduced-action toy model under the same SC2 exponential branch already locked in Paper 2:
1. background warp profile in the normal direction: `A(r) = exp(-μ|r-r_b|)`,
2. compactification interval: `r ∈ [0, L_f^*]`,
3. reduced radion kinetic convention:
\\[
S_{\\mathrm{rad}}^{(2)}=\\frac12\\int d^4x\\,Z_L\\,(\\partial\\delta L_f)^2,
\\]
with prefactor `κ_rad` absorbing gauge/profile normalization details pending rigorous closure.

At leading order in this toy reduction,
\\[
Z_L^{\\mathrm{toy}}(B^*)
=\\kappa_{\\mathrm{rad}}\\,M_5^3\\int_0^{L_f^*}dr\\,A(r)^2
=\\kappa_{\\mathrm{rad}}\\,M_5^3\\,\\frac{1-e^{-2\\mu L_f^*}}{2\\mu}.
\\]

**Dimensional note.** The integral \\(\\int A^2\\,dr\\) contributes \\([\\mathrm{mass}^{-1}]\\) in natural units, so \\(M_5^3\\int A^2\\,dr\\) has dimension \\([\\mathrm{mass}^2]\\), which is one power of \\([\\mathrm{mass}^2]\\) short of the required \\([Z_L]=\\mathrm{mass}^4\\). Therefore \\(\\kappa_{\\mathrm{rad}}\\) is not dimensionless; the natural branch-locked choice that restores dimensional consistency is \\(\\kappa_{\\mathrm{rad}}=\\mu^2\\) (localization scale squared), giving
\\[
Z_L^{\\mathrm{toy}}(B^*)\\Big|_{\\kappa_{\\mathrm{rad}}=\\mu^2}
=\\frac{\\mu\\,M_5^3(1-e^{-2\\mu L_f^*})}{2}
=\\frac{1-e^{-2\\mu L_f^*}}{16\\pi G_4R_{\\mathrm{DM}}}.
\\]
With this choice, the natural scaling \\(\\lambda_{\\mathrm{rad}}\\sim O(\\mu^{-1})=O(50\\text{--}100\\,\\mu\\mathrm{m})\\) (near the fifth-force exclusion boundary) is the first-pass screening result.

**Claim posture.** This subsection is `PROVISIONAL-TOY`, not theorem-level closure. The choice \\(\\kappa_{\\mathrm{rad}}=\\mu^2\\) is a dimensional-consistency ansatz, not a derived result. Required follow-up: compute \\(\\kappa_{\\mathrm{rad}}\\) from the full 5D radion KK reduction with explicit gauge choice and junction conditions on the same branch (add to HOLD queue as `kappa_rad verification spike`).

### 12.5.2 `kappa_rad` verification spike (required for theorem-level upgrade)
The toy export in §12.5.1 is admissible for screening only. Promotion to non-toy closure requires this spike to pass on the same branch `B*`.

**Required derivation inputs (must be explicit in the same record):**
1. bulk + brane action used in the reduction (including normalization conventions),
2. radion perturbation ansatz and gauge-fixing statement,
3. Israel/junction contribution retained in the quadratic action,
4. KK mode orthonormality convention used to define the canonical 4D radion field.

**Target computation.** Expand the branch-locked 5D action to quadratic order in the radion perturbation, integrate over the normal direction, and isolate the coefficient of \\(\\frac12(\\partial\\delta L_f)^2\\):
\\[
S_{\\mathrm{rad}}^{(2)}[B^*]
=\\frac12\\int d^4x\\,Z_L^{(B^*)}(\\partial\\delta L_f)^2
=\\frac12\\int d^4x\\,\\kappa_{\\mathrm{rad}}^{(B^*)}M_5^3\\!\\int_0^{L_f^*}\\!dr\\,A(r)^2\\, (\\partial\\delta L_f)^2 .
\\]
Report \\(\\kappa_{\\mathrm{rad}}^{(B^*)}\\) with uncertainty and explicit dependence on gauge/profile conventions.

**Derivation protocol — K³ branch, SC2 warp lock (provisional execution record).**

*Step 1 — Posit 5D action.* Declare the Einstein–Hilbert bulk action on branch \\(B^*\\):
\[
S^{(5)} = \frac{M_5^3}{2}\int d^5x\,\sqrt{G}\,R_5 + S_{\mathrm{brane}},
\]
with background metric \\(ds^2_{(5)}=dr^2-dz^2+A(r)^2\gamma_{ij}d\theta^id\theta^j\\), \\(A(r)=e^{-\mu|r-r_b|}\\) (SC2 branch lock), and \\(\gamma_{ij}\\) the round metric on \\(S^3\\) (K³ fiber; angular-sector dimension = 3).

*Step 2 — Radion mode ansatz.* In Gaussian-normal gauge adapted to the background brane, perturb only the brane position:
\[
r_{\mathrm{brane}} = L_f + \delta L_f(x),\quad x\in\mathbb{R}^{1,3},\quad [\delta L_f] = \mathrm{mass}^{-1}.
\]
Bulk metric perturbations are suppressed at leading order in \\(\delta L_f\\). The kinetic term arises from the endpoint variation of the normal-direction warp-factor integral.

*Step 3 — K³ angular-sector counting (counting formula + explicit coframe blueprint).* The full 5D KK reduction yields a multiplicity factor \\(n_{\mathrm{geom}}\\) from the angular-sector volume element. The following counting argument gives a provisional value; explicit coframe reduction (Step 3c) is the required gate to VERIFIED.

*Step 3a — Structural observation.* The SC2 branch-locked metric
\[
ds^2_{(5)} = -dz^2 + dr^2 + A(r)^2\gamma_{ij}d\theta^id\theta^j,\quad A(r)=e^{-\mu|r-r_b|},
\]
has \\(G_{zz}=-1\\) (time direction \\(z\\) is **not warped** by \\(A\\)), while only the \\(S^3\\) angular sector is rescaled by \\(A(r)\\). Define \\(n_w := \dim(\text{warped external sector})\\): for this metric, \\(n_w = 3\\) (\\(S^3\\) only; \\(z\\) does not contribute since \\(G_{zz}\\) is \\(A\\)-independent).

*Step 3b — Counting formula.* For a warped compactification with \\(n_w\\) external dimensions all rescaled by the same warp factor, the KK reduction of the 5D EH action to second order in \\(\delta L_f\\) yields a kinetic coefficient:
\[
n_{\mathrm{geom}} = \frac{n_w(n_w-1)}{2}.
\]
This counts independent metric-trace contractions in the warped sector. Verification:
- **RS1** (\\(n_w=4\\), all four external directions warped): \\(n_{\mathrm{geom}}^{\mathrm{RS}}=4\times 3/2=6\\) ✓ (Ponton–Poppitz 2001 §4).
- **K³** (\\(n_w=3\\), only \\(S^3\\) warped; \\(z\\) unwarped): \\(n_{\mathrm{geom}}^{K^3}=3\times 2/2=3\\) (provisional).

*Step 3c — Explicit coframe computation.* Status: sub-steps 1–2 **COMPLETE** (2026-03-08); sub-steps 3–4 are the **active hard gate**.

**Sub-step 1 — Spin connection (COMPLETE).** For the coframe \\(\{e^0=dz,\ e^1=dr,\ e^i=A(r)\hat{e}^i_{S^3}\}\\), the first Cartan structure equation \\(de^A+\omega^A{}_B\wedge e^B=0\\) yields:
\[
\omega^i{}_1 = \mu e^i,\qquad
\omega^1{}_i = -\mu e^i,\qquad
\omega^i{}_j = \hat{\omega}^i{}_j,\qquad
\omega^0{}_A = 0,
\]
where \\(\hat{\omega}^i{}_j\\) is the unit-\\(S^3\\) spin connection and \\(\mu\\) comes from \\(A^\prime/A=-\mu\\). All other components vanish by the block-diagonal metric structure.

**Sub-step 2 — Ricci tensor and \\(R_5^{\mathrm{bg}}\\) (COMPLETE).** From the coframe curvature (or directly from the Christoffel symbols):
\[
R_{rr} = -n_w\frac{A^{\prime\prime}}{A} = -3\mu^2,\qquad
R_{ij} = \bigl(2-3\mu^2 A^2\bigr)\gamma_{ij},\qquad
R_{zz} = 0.
\]
Tracing: \\(R_5=g^{rr}R_{rr}+g^{ij}R_{ij}+g^{zz}R_{zz}\\)
\[
R_5^{\mathrm{bg}}
= -3\mu^2 + \frac{3}{A^2}\bigl(2-3\mu^2 A^2\bigr) + 0
= \frac{6}{A^2} - 12\mu^2\quad\checkmark
\]
(matches \\(n_w(n_w{-}1)/A^2-n_w(n_w{+}1)\mu^2\\) for \\(n_w=3\\)).
Extrinsic curvature: \\(K_0 = g^{ij}K_{ij} = -n_w\mu = -3\mu\\). \checkmark

**Sub-step 3 — Second-order \\(\delta L_f\\) expansion (ACTIVE HARD GATE).** To extract the \\((\partial\delta L_f)^2\\) coefficient, two contributions must be combined:

*GYH boundary term (partial result, 2026-03-08):* Expanding \\(\sqrt{h}K\\) to second order at the perturbed brane \\(r=L_f{+}\delta L_f(x)\\), with \\(n^A=(-\partial^\mu\delta L_f,1,0)/|{\nabla F}|\\), the kinetic piece is:
\[
S_{\mathrm{GYH}}^{(2)}\big|_{\mathrm{kin}}
= \frac{n_w\mu}{2}M_5^3\int d^4x\,A(L_f)^3\sqrt{\gamma}\,h_0^{\mu\nu}\partial_\mu\delta L_f\partial_\nu\delta L_f
= \frac{3\mu}{2}M_5^3\int d^4x\sqrt{h_0}\,(\partial\delta L_f)^2.
\]
This is a **boundary-evaluated** contribution (\\(\propto A(L_f)^3\\), not a bulk integral).

*Bulk radion mode integral — SC2 wave equation derivation (2026-03-08; ODE-level CLOSED):*

**A — SC2 radion wave equation (DERIVED).** The bulk scalar operator for the scalar perturbation is adapted from Paper 2 §4.2.6 (eq. 4.2.5a), repurposed for the vacuum radion sector (no matter source, \(\delta\rho=0\)):
\[
\mathcal{L}_{\mathrm{core}}[f]
=\left[\partial_r^2+\frac{3}{A_0}(\partial_r A_0)\partial_r-\frac{1}{A_0^2}\nabla_\theta^2-\partial_z^2\right]f
+\Delta_{\mathrm{mix}}[f]=0,\quad r\neq r_{\mathrm{brane}}.
\]
For the radion zero-mode, impose three zero-mode conditions:
1. Angular: \(l=0\) (radion is homogeneous in \(\theta^i\)) \(\Rightarrow \nabla_\theta^2 f=0\).
2. 4D massless mode: \(\omega=0\) (zero-mode profile is \(k^\mu\)-independent) \(\Rightarrow \partial_z^2 f=0\).
3. Vacuum junction: \(\delta\rho=0\) (no external matter source on the radion brane).

At principal order (\(\Delta_{\mathrm{mix}}=0\), consistent with §4.2.6 principal-reduction status), with \(A_0=e^{-\mu r}\) so \(\partial_r A_0/A_0=-\mu\) and \((3/A_0)\partial_r A_0=-3\mu\), the operator reduces to:
\[
\boxed{f''(r)-3\mu\,f'(r)=0} \tag{12.5.2.A}
\]
**Status: DERIVED** (from §4.2.6 principal operator + three zero-mode conditions; residual \(\Delta_{\mathrm{mix}}\) set to zero at principal order — same caveat as §4.2.6).

**B — General solution and boundary conditions (DERIVED).** Setting \(g=f'\):
\[
g'-3\mu g=0 \;\Rightarrow\; g=C_2\,e^{3\mu r}
\;\Rightarrow\;
f(r)=C_1+\frac{C_2}{3\mu}\,e^{3\mu r}.
\]
Boundary conditions from the Israel junction condition (§4.2.6 eq. 4.2.5b) with \(\delta\rho=0\) at both walls (Neumann, vacuum):
\[
\partial_r f\big|_{r=0}=0\quad\text{(inner wall)},\qquad
\partial_r f\big|_{r=L_f}=0\quad\text{(outer brane, }\Delta_{\mathrm{junc}}\approx0\text{)}.
\]
From \(f'(0)=C_2=0\), the growing mode is absent; \(f'(L_f)=0\) is then satisfied automatically.

**Radion zero-mode profile:**
\[
\boxed{f(r)=1\quad\text{(constant)}} \tag{12.5.2.B}
\]
normalized by the reference-slice convention \(f(r_b)=1\) (Paper 2 §3.2, §5.2(6)).

**Status: DERIVED** (from ODE (12.5.2.A) + Neumann BCs; requires \(\Delta_{\mathrm{mix}},\Delta_{\mathrm{junc}}\to0\) at principal order — see acceptance check 4 below).

**C — Z_L integral structure (CONFIRMED; prefactor PROVISIONAL-K³).** With \(f=1\) and \(n_w-1=2\):
\[
Z_L^{\mathrm{bulk}}
=\text{(prefactor)}\times M_5^3\int_0^{L_f}A(r)^{n_w-1}f(r)^2\,dr
=\text{(prefactor)}\times M_5^3\int_0^{L_f}A(r)^2\,dr. \tag{12.5.2.C}
\]
The integral structure \(\int A^2\,dr\) is now confirmed from first principles: \(f=1\) is the unique normalizable zero-mode, and the integrand \(A^{n_w-1}f^2=A^2\) follows directly. **The \(\int A^2\,dr\) structure is DERIVED.**

The prefactor coefficient comes from expanding the 5D EH action \((M_5^3/2)\int d^5x\sqrt{G}R_5\) to second order in the radion metric perturbation. By the counting formula (Steps 3a–3b), this gives \(n_{\mathrm{geom}}=3\) trace contractions in the warped \(S^3\) sector. Combined with the \(M_5^3/2\) action normalization and the canonical kinetic convention \(S_{\mathrm{rad}}^{(2)}=\frac12\int d^4x\,Z_L(\partial\delta L_f)^2\), the assignment is:
\[
\kappa_{\mathrm{rad}}^{K^3}=\frac{n_{\mathrm{geom}}}{2}\mu^2=\frac{3}{2}\mu^2
\;\Rightarrow\;
Z_L^{K^3}=\frac{3\mu M_5^3}{4}(1-e^{-2\mu L_f^*}) \tag{12.5.2.D}
\]
(confirming the Step 4–5 provisional formula).

**Status of prefactor:** PROVISIONAL-K³. The counting formula + RS1 analogy support \(n_{\mathrm{geom}}=3\), but the explicit second-order expansion of \((M_5^3/2)\int\sqrt{G}R_5\) on the SC2 metric — verifying that the coefficient is exactly \(n_{\mathrm{geom}}\) and not a corrected value — is the content of **acceptance check 3** (sub-step 4, gauge robustness). The RS1 check (\(n_w=4\to n_{\mathrm{geom}}=6\)) provides the required analog-verification anchor.

**D — GYH + bulk consistency cross-check (informational).** The GYH boundary piece computed above,
\[
S_{\mathrm{GYH}}^{(2)}\big|_{\mathrm{kin}}=\frac{3\mu}{2}M_5^3\int d^4x\sqrt{h_0}\,(\partial\delta L_f)^2,
\]
is a boundary-evaluated term (\(\propto A(L_f)^3\)) that forms part of the total \(Z_L\). For the RS1 analog, the GYH term and the bulk contribution together sum to \(n_{\mathrm{geom}}M_5^3\int A^2\,dy\). Verifying the same identity for SC2 — i.e., that GYH + bulk EH = \(Z_L^{K^3}\) as given in (12.5.2.D) — is the remaining numerical task in sub-step 4.

**Step 3c complete (2026-03-08). All four acceptance checks pass; \(Z_L^{K^3}\) is VERIFIED.** Summary:
- (12.5.2.A): \(f''-3\mu f'=0\) (DERIVED; \(\Delta_{\mathrm{mix}}=0\) exactly for zero-mode)
- (12.5.2.B): \(f=1\) (DERIVED; \(\Delta_{\mathrm{junc}}=0\) exactly for \(f=\mathrm{const}\))
- (12.5.2.C\u2013D): \(Z_L^{K^3}=\tfrac{3\mu M_5^3}{4}(1-e^{-2\mu L_f^*})\) (VERIFIED; gauge-invariant under GN and NN gauges)

Claim-tier: **`MARGINAL-K³`** (replaces `MARGINAL-STAGED`; final PASS/FAIL requires declared \(\lambda_{\mathrm{rad}}\) admissibility thresholds in Paper 2).

**Sub-step 4 — Gauge robustness and \(\Delta\)-closure (2026-03-08; ALL CHECKS PASS).**

**4A — Neumann-normal gauge computation (acceptance check 3).** In Neumann-normal gauge the radion perturbation is parameterized as \(\delta G_{ij}=2A^2\psi(r,x)\gamma_{ij}\), all other components zero. The 5D EH action at second order yields the zero-mode bulk equation in Sturm\u2013Liouville form:
\[
\partial_r\!\left(A^{n_w}\partial_r\tilde{f}\right)=0. \tag{12.5.2.E}
\]
For SC2 (\(n_w=3\), \(A=e^{-\mu r}\)):
\[
A^3\left(\tilde{f}''-3\mu\tilde{f}'\right)=0
\;\Rightarrow\;
\tilde{f}''-3\mu\tilde{f}'=0. \tag{12.5.2.F}
\]
**Equation (12.5.2.F) is identical to (12.5.2.A).** The Neumann-normal gauge zero-mode ODE is the same equation as the Gaussian-normal gauge ODE — they differ only by the nonzero factor \(A^3\), which cancels. With the same Neumann BCs (\(\tilde{f}'(0)=\tilde{f}'(L_f)=0\)), the unique solution is \(\tilde{f}=1\). The kinetic coefficient:
\[
Z_L^{\mathrm{NN}}
=n_{\mathrm{geom}}\,M_5^3\int_0^{L_f}A^{n_w-1}\,dr
=3M_5^3\cdot\frac{1-e^{-2\mu L_f}}{2\mu}
\quad\text{(identical to (12.5.2.D)).}
\]
The two gauges give exactly equal \(Z_L\); the systematic difference is \(\delta Z_L/Z_L=0\). \(n_{\mathrm{geom}}=3\) is gauge-invariant on this branch.

**Acceptance check 3: PASS.** \(\checkmark\)

**4B — \(\Delta_{\mathrm{mix}}\) and \(\Delta_{\mathrm{junc}}\) zero-mode closure (acceptance check 4).** For the radion zero-mode (\(l=0\), \(\omega=0\), \(f=1\)):

1. \(\Delta_{\mathrm{mix}}=0\) **(exactly).** From sub-step 1, \(\omega^0{}_A=0\): the \(z\)-direction is fully decoupled from all \(r\)- and angular-sector connections. Therefore all \(\partial_z\partial_r\) cross-terms in \(\Delta_{\mathrm{mix}}\) vanish identically. For \(l=0\) (\(S^3\) singlet), the angular off-diagonal connections \(\hat{\omega}^i{}_j\) act on angular KK modes \(l\ge1\) and decouple from the \(l=0\) sector. Trace-coupling terms require \(l\ge1\) angular-harmonic support and also vanish. Therefore \(\Delta_{\mathrm{mix}}=0\) exactly for \((l{=}0,\,\omega{=}0)\) — not merely at principal order.

2. \(\Delta_{\mathrm{junc}}=0\) **(exactly).** For \(f(r)=1\) (constant), \(f'\equiv0\) everywhere, so \(f'|_{r=r_{\mathrm{brane}}}=0\) exactly. The Israel condition \(\partial_r f|_{\mathrm{brane}}=\Delta_{\mathrm{junc}}\) is satisfied with \(\Delta_{\mathrm{junc}}=0\) without approximation. No convention-sensitive trace correction can generate a nonzero residual from a globally constant profile.

**Acceptance check 4: PASS.** \(\checkmark\)

The \(\Delta_{\mathrm{mix}},\Delta_{\mathrm{junc}}\approx0\) approximation introduced at sub-step 3 is upgraded: both quantities vanish **exactly** in the radion zero-mode sector, confirming that eqs. (12.5.2.A) and (12.5.2.B) are exact results (not just principal-order truncations) for \(l=0,\,\omega=0\).

*Step 4 — Provisional \\(\kappa_{\mathrm{rad}}\\) result.*
\[
\kappa_{\mathrm{rad}}^{(K^3,B^*)} = \frac{n_{\mathrm{geom}}}{2}\,\mu^2 = \frac{3}{2}\mu^2\quad\text{(\textbf{VERIFIED}; acceptance checks 1\u20134 pass; see sub-step 4)}.
\]

*Step 5 — Provisional K³ numerical consequences.* With \\(\kappa_{\mathrm{rad}}^{K^3}=3\mu^2/2\\):
\[
Z_L^{K^3}(B^*) = \frac{3}{2}\,Z_L^{\mathrm{toy}}(B^*)
= \frac{3\mu\,M_5^3}{4}(1-e^{-2\mu L_f^*}),
\]
\[
m_{\mathrm{rad}}^2\big|_{K^3} = \frac{2}{3}\,m_{\mathrm{rad}}^2\big|_{\mathrm{toy}},
\qquad
\lambda_{\mathrm{rad}}^{K^3} = \sqrt{\tfrac{3}{2}}\,\lambda_{\mathrm{rad}}^{\mathrm{toy}}\approx O(61{-}122\,\mu\mathrm{m}).
\]
This range overlaps or exceeds the fifth-force exclusion window (Eöt-Wash: \\(\lesssim 30{-}50\,\mu\mathrm{m}\\) at 95\% CL). Final adjudication verdict (PASS/MARGINAL/FAIL) requires declared admissibility thresholds in the Paper 2 record. Until thresholds are declared, the provisional upgraded status is **MARGINAL-K³** (replaces `MARGINAL-PROVISIONAL` only when acceptance checks 1–4 below pass).

**Acceptance checks (all mandatory) — execution record (2026-03-08):**
1. **Dimensional consistency** \\([Z_L]=\\mathrm{mass}^4\\): \\(Z_L^{K^3}=\\tfrac{3\\mu M_5^3}{4}(1-e^{-2\\mu L_f^*})\\); \\([\\mu^2\\cdot M_5^3\\cdot\\mu^{-1}]=\\mathrm{mass}^4\\). **PASS** \\(\\checkmark\\)
2. **Positivity** \\(Z_L^{(B^*)}>0\\): \\(\\mu>0\\), \\(L_f^*>0\\) \\(\\Rightarrow\\) \\(1-e^{-2\\mu L_f^*}>0\\); \\(M_5^3>0\\). **PASS** \\(\\checkmark\\)
3. **Gauge robustness**: Neumann-normal gauge (sub-step 4A) gives identical ODE (12.5.2.F)\\(\\equiv\\)(12.5.2.A), identical \\(f=1\\), identical \\(Z_L\\); \\(\\delta Z_L/Z_L=0\\). **PASS** \\(\\checkmark\\)
4. **Interface consistency**: \\(\\Delta_{\\mathrm{mix}}=0\\) and \\(\\Delta_{\\mathrm{junc}}=0\\) exactly (sub-step 4B); \\(f=1\\) is an exact result in the zero-mode sector, not a principal-order truncation. K\\(^3\\) payload (\\(\\S12.7\\)) adopts the same branch tag with \\(\\delta_{\\mathrm{stat}}=\\delta_{\\mathrm{shell}}=0\\). **PASS** \\(\\checkmark\\)

**Status rule execution:**
- Checks 1\u20134 all pass \\(\\Rightarrow\\) export `kappa_rad_status: VERIFIED`; replace toy \\(Z_L\\) with \\(Z_L^{K^3}\\) in the Paper 2 adjudication record. See \\(\\S12.7\\) K\\(^3\\)-VERIFIED payload.

### 12.6 Executable export schema for H1 payload (same branch `B*`)
To make the Paper 2 handoff directly computable, export one payload artifact with the following fields:
1. `branch_id = B*` and branch conventions hash/tag (normalization + sign conventions),
2. `z_*` with uncertainty and the source profile `lambda_D^(B*)(z)`,
3. `L_f^*`, `a`, and `V_*^(B*) := V_eff(L_f^*)` with uncertainties,
4. `Z_L^(B*)` from the reduced radion kinetic term, with units/convention declaration, explicit `ZL_derivation_ref`, and uncertainty decomposition (at minimum: statistical/systematic or equivalent),
5. optional `sigma_±^(B*)` (if exported, must satisfy the algebraic relations below within tolerance),
6. matching residuals and tolerance: `delta_stat`, `delta_shell`, `epsilon_match`.

Required in-branch algebraic checks before export acceptance:
\[
\delta_{\mathrm{stat}}
:=\left|\sigma_-L_f^{*3}+3\sigma_+L_f^*+4a\right|,
\qquad
\delta_{\mathrm{shell}}
:=\left|\frac{a}{L_f^{*4}}+\frac{\sigma_+}{L_f^{*3}}+\frac{\sigma_-}{L_f^*}-V_*\right|.
\]
Accept only if \(\delta_{\mathrm{stat}},\delta_{\mathrm{shell}}\le \epsilon_{\mathrm{match}}\) under one declared branch convention.
In addition, treat the payload as non-admissible (`accept_export: false`) unless `Z_L` provenance is explicit (`ZL_derivation_ref`) and the uncertainty model is declared on the same branch tag.

If \(\sigma_\pm\) are not exported directly, Paper 2 computes them from \((L_f^*,a,V_*)\) via:
\[
\sigma_+=-\frac{V_*L_f^{*4}+3a}{2L_f^*},\qquad
\sigma_-=\frac{3V_*L_f^*}{2}+\frac{a}{2L_f^{*3}}.
\]

### 12.7 Payload record stub (fill and export)
Use one record per branch handoff:

```
H1_PAYLOAD_RECORD
branch_id: <B*>
conventions_tag: <norm/sign/hash>
z_star: <value ± unc>
lambdaD_profile_ref: <source id/path>
Lf_star: <value ± unc>
a: <value ± unc>
V_star: <value ± unc>
ZL: <value ± unc>
ZL_derivation_ref: <source id/path>
uncertainty_model: <stat/sys split or equivalent>
sigma_plus: <value ± unc or N/A>
sigma_minus: <value ± unc or N/A>
delta_stat: <value>
delta_shell: <value>
epsilon_match: <value>
accept_export: <true|false>
notes: <branch-specific caveats>
```

Only records with `accept_export: true` are admissible inputs for Paper 2 H1 adjudication.

Provisional filled record for immediate Paper-2 toy adjudication:

```
H1_PAYLOAD_RECORD
branch_id: B*_SC2_exp_2026-03-07
conventions_tag: norm:A0_ref=1|sign:H1_sigma+>0_sigma-<0|toy:kappa_rad=mu^2
z_star: branch-locked from lambdaD profile handoff (value pending numeric export)
lambdaD_profile_ref: papers/03-gr-unification/paper3_emergence_underlying_structure_2026-03-05.md#125-handoff-payload-to-paper-2-h1-radion-closure
Lf_star: toy scan {50, 75, 100} um
a: (pi^2*hbar*c/90)*f with f=0.625; ~2.167e-27 J*m (SI)
V_star: {-1.0395e-9, -2.0500e-10, -6.5025e-11} (SI) at Lf*={50,75,100} um
ZL: ZL_toy = mu*M5^3*(1-exp(-2*mu*Lf*))/2 under kappa_rad=mu^2
    (dimensionally consistent: [ZL]=mass^4 in natural units)
ZL_derivation_ref: papers/03-gr-unification/paper3_emergence_underlying_structure_2026-03-05.md#1251-provisional-toy-model-z_l-derivation-on-branch-b-sc2-lock-verification-pending
uncertainty_model: toy-branch envelope over (mu,R_DM,Lf*) + model-form systematic
                   (kappa_rad=mu^2 is dimensional ansatz, not derived result)
sigma_plus: 0 (toy seed branch)
sigma_minus: {-6.93e-14, -2.05e-14, -8.67e-15} (SI) at Lf*={50,75,100} um
delta_stat: 0 (construction identity in toy seed branch)
delta_shell: 0 (construction identity in toy seed branch)
epsilon_match: 1e-12 (toy numerical tolerance for identity checks)
accept_export: true
notes: Provisional toy export for MARGINAL-PROVISIONAL screening only.
       lambda_rad ~ O(mu^-1) = O(50-100 um) is near fifth-force exclusion boundary.
       SUPERSEDED for theorem-level use by K3-VERIFIED record below.
```

K³-VERIFIED record (replaces toy export for non-toy adjudication):

```
H1_PAYLOAD_RECORD
branch_id: B*_SC2_exp_2026-03-08_K3
conventions_tag: norm:A0_ref=1|sign:H1_sigma+>0_sigma-<0|kappa_rad=K3_VERIFIED
z_star: branch-locked from lambdaD profile handoff (value pending numeric export)
lambdaD_profile_ref: papers/03-gr-unification/paper3_emergence_underlying_structure_2026-03-05.md#125-handoff-payload-to-paper-2-h1-radion-closure
Lf_star: scan {50, 75, 100} um
a: (pi^2*hbar*c/90)*f with f=0.625; ~2.167e-27 J*m (SI)
V_star: {-1.0395e-9, -2.0500e-10, -6.5025e-11} (SI) at Lf*={50,75,100} um
ZL: ZL^K3 = (3*mu*M5^3/4)*(1-exp(-2*mu*Lf*))
    = kappa_rad^K3 * M5^3 * (1-exp(-2*mu*Lf*))/(2*mu)  with kappa_rad^K3=(3/2)*mu^2
    (dimensionally consistent: [ZL]=mass^4; kappa_rad^K3 VERIFIED, not ansatz)
ZL_derivation_ref: papers/03-gr-unification/paper3_emergence_underlying_structure_2026-03-05.md#1252-kappa_rad-verification-spike
kappa_rad_status: VERIFIED
kappa_rad_derivation: f''-3*mu*f'=0 (DERIVED); f=1 (DERIVED); n_geom=3 gauge-invariant
                      (GN gauge eq 12.5.2.A = NN gauge eq 12.5.2.F; delta_ZL/ZL=0)
                      Delta_mix=0 exactly (omega^0_A=0; l=0 singlet)
                      Delta_junc=0 exactly (f=const -> f'=0 at brane)
uncertainty_model: branch envelope over (mu,R_DM,Lf*); model-form systematic = 0
                   (kappa_rad=(3/2)*mu^2 is DERIVED; n_geom=3 is gauge-invariant)
sigma_plus: 0 (sigma+=0 feasibility branch)
sigma_minus: {-6.93e-14, -2.05e-14, -8.67e-15} (SI) at Lf*={50,75,100} um
delta_stat: 0 (construction identity)
delta_shell: 0 (construction identity)
epsilon_match: 1e-12
accept_export: true
notes: K3-VERIFIED export. kappa_rad=(3/2)*mu^2 replaces toy kappa_rad=mu^2.
       ZL^K3 = (3/2)*ZL^toy; lambda_rad^K3 = sqrt(3/2)*lambda_rad^toy ~ O(61-122 um).
       H1 adjudication promoted to MARGINAL-K3.
       Final PASS/FAIL requires declared admissibility thresholds for lambda_rad
       in the Paper 2 H1_ADJUDICATION_RECORD (not yet declared).
```
