# Paper 2 — Mathematical Spine: §§2–4
*Status: First draft 2026-02-28*
*Covers: B1 (§2 KK-cone model), B2 (§3 self-consistency conditions), B3 (§4 geometric dark-matter response)*

## §2 The KK-Cone Model
### 2.0 Geometric Origin of the Extra Dimension
The five-dimensional bulk metric of §2.2 is not postulated. It follows from the first realized geometry established in Paper 3 together with an intrinsic property of that geometry: the Hopf fibration.

#### 2.0.1 The Hopf Fibration as an Intrinsic Structure of \(S^2\)
Paper 3 §§3.2--3.4 establishes that the unique first realized geometry consistent with isotropy, compactness admissibility, and thermodynamic preference is \(S^2\). However, \(S^2\) is not geometrically self-contained in the following sense. The sphere \(S^2 \cong \mathbb{CP}^1\) admits a natural complex structure, and the minimal smooth fiber bundle with \(S^2\) as base and a connected structure group is the Hopf fibration:
\[
S^1 \hookrightarrow S^3 \xrightarrow{\pi} S^2. \tag{2.0.1}
\]
This is not an external addition to \(S^2\) but an intrinsic feature of its topology: \(\pi_1(S^1) = \mathbb{Z}\) and the Hopf bundle has first Chern class \(c_1 = 1\), making it the generator of all \(U(1)\) bundles over \(S^2\). Any smooth \(U(1)\) structure on \(S^2\) is a pullback of the Hopf bundle. The total space \(S^3\) is the minimal smooth extension of \(S^2\) that accommodates this structure.

#### 2.0.2 Distinct Roles of Hopf Fiber \(\psi\) and Warp Direction \(r\)
In the metric of §2.2, the Hopf \(S^1\) fiber is the compact angular coordinate \(\psi\) inside the \(S^3\) sector \(\gamma_{ij}d\theta^i d\theta^j\), while \(r\) is a non-compact warp (normal) direction. Thus \(r\) is not the Hopf fiber itself; rather, \(r\)-dependence modulates the effective fiber/base scales through \(A(r,z)\). The dimensional content at nucleation is therefore:
\[
\underbrace{S^2}_{\text{base, 2D}} \times_{\text{Hopf}} \underbrace{S^1}_{\text{fiber, 1D}} = \underbrace{S^3}_{\text{total space, 3D}}
\]
Adding the cone expansion parameter \(z\) (proper time) and the non-compact warp direction \(r\) gives the full coordinate set \((z, r, \theta^i)\), with \(\psi\) included among \(\theta^i\) in the \(S^3\) sector. This counting is summarized in Table 2.1.

**Table 2.1. Dimensional origin from Hopf structure.**

| Object | Dimension | Geometric role |
|---|---|---|
| \(S^2\) base | 2 | Base of spatial Hopf structure |
| \(S^1\) Hopf fiber (\(\psi\)) | 1 | Compact KK fiber direction |
| \(S^3\) total space | 3 | Spatial sector \(\gamma_{ij}d\theta^i d\theta^j\) |
| \(r\) (warp/normal) | 1 | Non-compact bulk direction controlling localization |
| \(z\) (cone parameter) | 1 | Proper time / expansion parameter |
| **Bulk total** | **4+1** | **Mandated by Hopf structure** |

#### 2.0.3 Why Not 3+1?
A 3+1-dimensional description would require treating \(S^2\) as geometrically complete with no fiber structure. This is mathematically consistent as a topological space, but it discards the Hopf fibration, and with it:

1. The \(U(1)\) electromagnetic structure (identified with the \(S^1\) fiber in the KK decomposition, §2.4)
2. The \(SU(2)\) weak structure (currently a geometric identification tied to the \(S^3\) sector; a strict KK derivation is deferred and not claimed in this section)
3. The geometric mechanism for gravity localization (the warp profile in \(r\), Paper 2 §3.3)
4. The Casimir closure candidate for \(\Lambda_{\text{eff}}\) (the compact fiber, Paper 2 §3.6)

A 3+1-dimensional cone without the non-compact warp direction \(r\) is consistent with reduced kinematics but loses localization dynamics and SC2--SC3 closure machinery. In this framework, the compact Hopf fiber \(\psi\) supplies KK gauge structure, while \(r\) supplies warping/localization; both ingredients are required for the full 4+1D model.

#### 2.0.4 Non-Traversability of \(r\)
The Hopf fibration establishes that \(r\) exists as a geometric direction. It does not by itself establish that observers are confined to a brane at fixed \(r\). That claim is a dynamical consequence of the warp factor \(A(r,z)\) in the bulk metric: the graviton zero-mode is localized on the brane by the effective potential \(V_{\text{grav}}(r)\) of §3.3, and matter fields coupled to the induced metric \(h_{ab}\) do not propagate freely into the bulk. The geometry mandates that \(r\) exists; the dynamics determine that it is non-traversable at accessible energies.

This distinction is important: the compact Hopf fiber \(\psi\) is geometrically necessary from the \(S^3\!\to\!S^2\) structure, while the effective invisibility of the non-compact direction \(r\) to brane observers is dynamically imposed by warping. These are separate claims with separate justifications, and neither implies the other.

#### 2.0.5 Axioms: Geometric Canonicality vs Physical Realization
To avoid conflating mathematical structure with physical necessity, we make the logical stack explicit:

**Axiom A (Mathematical canonicality).** For the first realized compact base \(S^2\), the Hopf bundle
\[
S^1 \hookrightarrow S^3 \xrightarrow{\pi} S^2
\]
is the canonical \(U(1)\)-bundle representative (generator \(c_1=1\)).

**Axiom B (Physical selection).** Post-transition realized states preserve a compact \(U(1)\)-bundle sector over the \(S^2\) base. This promotes the Hopf fiber \(\psi\) from available mathematical structure to physical compact sector.

**Axiom C (Dynamical extension).** The non-compact normal direction \(r\) is introduced by localization dynamics (SC2), not by Hopf topology alone; \(r\) controls warping and mode localization in the bulk.

Under A–C, the 4+1D model is not inferred from topology alone: compact fiber structure is selected by B, while bulk non-compact extension is selected by C. This separates what is proved mathematically (A) from what is assumed physically (B,C), making the theory's commitments testable and falsifiable.
### 2.1 Motivation and Scope
We model spacetime as a higher-dimensional cone geometry in which the observable universe occupies a 3+1-dimensional brane at fixed radial coordinate \(r\), embedded in a 5-dimensional bulk. The construction is not a complete quantum-gravity theory; it is a mathematically controlled self-consistent field (SCF) model in which the effective cosmological parameters — spatial flatness, \(\Lambda_{\text{eff}}\), and dark-matter-like phenomenology — emerge from global geometry rather than being inputs.

The three coordinates of the cone are:
- \(z\): proper time along the brane (observer time)
- \(r\): non-traversable radial extra dimension; encodes additional Hilbert-space/bulk structure orthogonal to the observable brane
- \(\theta^i\): angular coordinates parameterizing the observed 3-space directions (normalized on \(S^3\) via Hopf fiber structure from Paper 3)

Observers are confined to the brane at fixed \(r\); the \(r\)-direction is not directly accessible but influences brane physics through the warp factor \(A(r,z)\).

### 2.1.1 Timeless Hilbert-space transition hypothesis (Phase 0)
We propose that what appears as a cosmological “origin event” is, at the fundamental level, a transition between states in a timeless Hilbert space rather than a dynamical process in external time.

In this view, a globally entangled primordium state \\(\\lvert\\Psi_{\\mathrm{prim}}\\rangle\\) in \\(\\mathcal{H}_{\\mathrm{tot}}\\) is mapped, by an objective state-selection rule on \\(\\mathcal{H}_{\\mathrm{tot}}\\) itself, to a distinguished low-entropy branch \\(\\lvert\\Psi_{\\mathrm{BB}}\\rangle\\). A Big-Bang-like interpretation is then admitted only after choosing an emergent spacetime/coherence frame.

Accordingly, the “beginning” is treated as a frame-dependent description of a Hilbert-space transition, not as a fundamental singularity of an underlying temporal geometry.

In the staging language used later, this timeless selection layer is designated **Phase 0**, preceding the dynamical 5D/4D regime structure (Phases I–III in §3.5.2).

**Claim posture.** This subsection is an interpretive hypothesis for model organization, not a completed dynamical derivation; quantitative consequences are carried by the phase-gated equations in §§3–5.

**Literature-positioning note.** The ingredients of this subsection each have precedents (timeless universal-state formalisms, emergent-time programs, and objective-selection/collapse proposals), but the present claim is that their **specific conjunction** here is not taken as a standard worked-out model in this manuscript branch: namely, a Phase-0 atemporal Hilbert-space selection \\(\\lvert\\Psi_{\\mathrm{prim}}\\rangle\\to\\lvert\\Psi_{\\mathrm{BB}}\\rangle\\) whose Big-Bang interpretation is explicitly frame-emergent and not fundamental-time dynamical. This is therefore treated as a testable synthesis hypothesis, not as a literature-established equivalence.

*Citation anchors for bibliography pass:* [timeless quantum cosmology / Wheeler-DeWitt], [objective selection or collapse models], [emergent-time or history-Hilbert-space constructions], [wavefunction realism / universal-state ontology].

### 2.2 Metric Ansatz
The 5D bulk metric takes the Gaussian-normal form:
\[
ds^2_{(5)} = -dz^2 + dr^2 + A(r,z)^2 \, \gamma_{ij} \, d\theta^i d\theta^j, \tag{2.2.1}
\]
where \(\gamma_{ij}\) is the unit \(S^3\) metric. The induced metric on the brane \(\Sigma\) at fixed \(r\) is:
\[
ds^2_\Sigma = -dz^2 + A(r,z)^2 \, \gamma_{ij} \, d\theta^i d\theta^j. \tag{2.2.2}
\]

The function \(A(r,z)\) simultaneously encodes:
1. Expansion history: \(\partial_z A / A = H(z)\), the effective Hubble rate on the brane
2. Warp profile: \(\partial_r A / A =: x(r,z)\), the extrinsic curvature scale of the brane in the \(r\)-direction
3. Geometric interpolation: the transition from Planck-scale compact geometry (Paper 3 §3.5) to the late-time near-flat brane

The pure light-cone limit \(A = z\) (constant cone angle \(\alpha = 45^\circ\), units \(c = 1\)) gives \(x = 0\) — a flat intrinsic brane with no extrinsic curvature contribution. This is the baseline; physical observables require \(A(r,z)\) with nontrivial \(r\)-dependence.

### 2.3 Relationship to Paper 3 Initial Conditions
The geometric phase transition of Paper 3 §3.5 produces a compact \(S^2\)-symmetric initial state at \(\lambda = 1\) (fully realized geometry). The cone metric (2.2.1) is the post-transition evolution of that state: \(A(r,z)\) at early \(z\) encodes the expanding \(S^2\) sphere of Paper 3, and at late \(z\) reproduces standard FRW geometry on the brane. The order parameter \(\lambda\) of Paper 3 is identified with the distinguishability coordinate \(\lambda_D\) (Paper 3 §6); once \(\lambda_D \to 1\), the cone description (2.2.1) applies.

*[Dependency: explicit mapping \(\lambda_D \to A(r,z)\) at \(\lambda_D = 1\) not yet derived — flag for Paper 3/Paper 2 interface section.]*
*[Spine tracking note: §2.4 (KK decomposition) and §2.4.7 (radion stabilization as framework prerequisite) are maintained in section-level drafts and must be merged into this spine before submission assembly.]*
*[Spine tracking note: include fifth-force constraint citation (Hoyle et al., 2004) in the consolidated bibliography when §2.4.7 is merged.]*

## §3 Self-Consistency Conditions
### 3.1 The SCF Requirement
We impose that the cone geometry is self-consistent: the warp factor \(A(r,z)\) must simultaneously satisfy three physical requirements at late times (\(z \gg \ell_P\)):
\[
\text{(SC1) Spatial flatness:} \quad \Omega_k \to 0 \quad \text{on the brane at large } z \tag{3.1.1}
\]
\[
\text{(SC2) Gravity localization:} \quad \text{4D Newton's law recovered on brane at scales } \ell_P \ll \ell \ll r_{\text{bulk}} \tag{3.1.2}
\]
\[
\text{(SC3) Small positive } \Lambda_{\text{eff}}:\quad \Lambda_{\text{eff}} > 0, \quad \Lambda_{\text{eff}} \ll \ell_P^{-2} \tag{3.1.3}
\]

These three conditions, imposed simultaneously on \(A(r,z)\), over-determine the system: generically, no \(A(r,z)\) satisfies all three without tuning. Current status is that SC1 and SC2 admit classical geometric formulation, while SC3 is not classically closed in the Gaussian-normal cone branch and requires quantum completion (current leading candidate: Casimir-on-fiber term).

### 3.1.1 SC3 equation reset: GR-closure functions across all four original paths
Given the accumulated branch inconsistencies around collapse/horizon diagnostics, this draft adopts an explicit reset policy: SC3 equations are to be re-derived from baseline with GR closure functions included uniformly across all four original SC3 paths (Path-1 through Path-4).

Define a path-indexed closure discriminator
\\[
\\chi_p(R)\\equiv \\frac{R_{s,p}^{\\mathrm{eff}}(R)}{R},\\qquad p\\in\\{1,2,3,4\\},
\\]
where \\(R_{s,p}^{\\mathrm{eff}}\\) is the path-specific effective Schwarzschild-scale functional (4D branch plus projected corrections for non-4D-effective regimes).

Each path must be re-expressed in the common form
\\[
\\mathcal{E}_p\\big[A,\\text{fields}\\big]=0
\\quad\\Longrightarrow\\quad
\\mathcal{C}_p\\big[A,\\text{fields};\\chi_p\\big]=0,
\\]
with \\(\\mathcal{C}_p\\) the GR-closure-corrected equation set used for quantitative claims.

**Reset rule.** Pre-reset SC3 expressions are retained only as historical scaffolds; no path-level closure claim is promoted unless obtained from the corresponding \\(\\mathcal{C}_p\\) system under explicit phase qualification (Phase I/II vs Phase III).

**Operational consequence.** Path-2 results in §3.4 remain informative but non-final until Path-1/3/4 are rewritten in the same \\(\\chi_p\\)-aware closure language and compared under a common acceptance protocol.

### 3.1.2 Four-path GR-closure template (restart baseline)
To make the reset executable, all four paths are rewritten in one common phase-gated structure.

**Phase gates.** Introduce nonnegative regime weights
\\[
g_0+g_I+g_{II}+g_{III}=1,
\\]
with \(g_0\) the Phase-0 interpretive layer (no dynamical closure equation), and \(g_I,g_{II},g_{III}\) weighting the dynamical branches used in SC3 equations.

**Common effective Schwarzschild-scale functional.**
\\[
R_{s,p}^{\\mathrm{eff}}(R)
=\\frac{2G_4M_p(R)}{c^2}
\\Big[ g_{III}
 + (g_I+g_{II})\\big(1+\\Delta_p^{5D}(R)\\big)\\Big],
\\]
where \\\\(\\Delta_p^{5D}\\\\) is the path-specific projected correction (Weyl/extrinsic/quantum completion terms as applicable).

**Common closure discriminator.**
\\[
\\chi_p(R)=\\frac{R_{s,p}^{\\mathrm{eff}}(R)}{R}.
\\]

**Path registry (working labels for restart).**
1. **Path-1:** intrinsic 4D-effective closure branch (baseline GR limit with explicit phase gates).
2. **Path-2:** Hopf normal-projection / extrinsic-curvature branch (current §3.4 locus).
3. **Path-3:** Casimir/vacuum completion branch on compact fiber (current §3.7 locus).
4. **Path-4:** mixed projected branch coupling classical 5D projection and quantum completion terms.

If historical path names differ in archived notes, they are to be mapped to this registry explicitly before any numerical comparison.

### 3.1.3 Restart acceptance protocol (all paths)
Each path must produce:
1. an explicit \(M_p(R)\) definition and parameter domain,
2. an explicit \\\\(\\Delta_p^{5D}(R)\\\\) definition with sign convention,
3. phase-qualified \(\\chi_p(R)\) curves over the same \(R\)-grid,
4. a branch verdict under common rules:
   - **PASS:** internally consistent and observationally admissible in the selected phase window,
   - **MARGINAL:** sign/scale sensitive or tuning dependent,
   - **FAIL:** inconsistent closure or non-admissible branch behavior.

No cross-path ranking is admissible unless all four paths have passed steps (1)–(4) under shared conventions.

### 3.2 Flatness Condition (SC1)
The effective spatial curvature on the brane is determined by the intrinsic geometry of constant-\(z\) slices. For metric (2.2.1), the spatial curvature of a \(z = \text{const}\) slice is:
\[
k_{\text{eff}} = \frac{k_{S^3}}{A(r,z)^2} - \left(\frac{\partial_z A}{A}\right)^2 \tag{3.2.1}
\]
where \(k_{S^3} = 1\) is the unit \(S^3\) curvature. Flatness requires \(k_{\text{eff}} \to 0\), which at late times gives the condition:
\[
A(r,z) \sim z \cdot f(r) \quad \text{as } z \to \infty, \tag{3.2.2}
\]
for some warp profile \(f(r)\) with \(f(r_{\text{brane}}) = 1\) (normalization at the observer brane). The pure light-cone \(A = z\) satisfies this with \(f \equiv 1\); a warped solution has \(f(r) \neq 1\) off-brane.

### 3.3 Gravity Localization (SC2)
Gravity localization on the brane requires that the bulk graviton zero-mode be normalizable in the \(r\)-direction. For the metric (2.2.1), the graviton wavefunction in the \(r\)-direction satisfies a Schrödinger-like equation with effective potential:
\[
V_{\text{grav}}(r) = \frac{3}{2}\partial_r^2 \ln A + \frac{3}{4}(\partial_r \ln A)^2 \tag{3.3.1}
\]
Localization requires \(V_{\text{grav}}(r)\) to have a normalizable bound state at \(r = r_{\text{brane}}\). This is the K³ analog of the Randall-Sundrum mechanism \cite{RandallSundrum1999b}: the warp factor creates an effective potential well that traps the massless graviton on the brane. For \(A = z \cdot e^{-\mu|r|}\) (exponential warp), the bound-state condition gives \(\mu > 0\), recoverable 4D Newton's law at scales \(\ell \ll \mu^{-1}\), and Kaluza-Klein corrections suppressed as \((\ell/\mu^{-1})^2\).

*[Model claim, not derived: the specific form \(A = z \cdot e^{-\mu|r|}\) is a trial ansatz. The self-consistent \(A(r,z)\) satisfying all three conditions simultaneously has not been derived analytically. The scaffold is structurally correct; full derivation requires numerical treatment.]*

### 3.4 Effective Cosmological Constant (SC3): Path-2 Hopf Normal-Projection Result
> **Result Box (SC3 status).**
> For the stated Hopf ansätze, the extrinsic projection route closes algebraically to either \(Q_{ab}=0\) (rank-1) or an anisotropic \(Q_{ab}\) (rank-2), with no isotropic \(Q_{ab}\propto h_{ab}\) closure. In Gaussian-normal form, \(R^{(5)}_{rr}\) is identically extrinsic; intrinsic Hopf curvature does not generate a new normal source, and for \(K_{ab}=0\) the Gauss relation is tautological. Therefore SC3 is not closeable by classical Gaussian-normal cone geometry alone.
Using Gaussian-normal form \(ds^2 = dr^2 + h_{ab}(x,r)\,dx^a dx^b\), \(n^\mu=\delta^\mu_r\), and
\[
K_{ab}=\tfrac12\partial_r h_{ab},\qquad
R^{(5)}_{rr}=-\partial_r K-K_{ab}K^{ab},
\]
with projected correction
\[
Q_{ab}=\bigl(KK_{ab}-K_{ac}K^c{}_b\bigr)-\tfrac12 h_{ab}\bigl(K^2-K_{cd}K^{cd}\bigr),
\]
the explicit computation gives:

**Ansatz A (isotropic Hopf):**
\[
h_{ab}dx^a dx^b=-dz^2+a(z)^2d\Omega_2^2+b(r)^2(d\psi+\cos\theta\,d\phi)^2.
\]
Here \(K_{ab}\) is rank-1, \(K^2=K_{ab}K^{ab}\) identically, and therefore
\[
Q_{ab}=0,\qquad \Lambda_{\mathrm{Hopf}}=0.
\]

**Ansatz B (squashed Hopf as stated):**
\[
h_{ab}dx^a dx^b=-dz^2+a(z)^2(\sigma_1^2+\sigma_2^2)+c(r)^2\sigma_3^2.
\]
With only \(c(r)\) carrying \(r\)-dependence, this is again rank-1 in \(K_{ab}\), yielding
\[
Q_{ab}=0,\qquad \Lambda_{\mathrm{Hopf}}=0.
\]

To obtain nontrivial \(Q_{ab}\), one must allow rank-2 extrinsic structure (e.g., \(a=a(r,z)\), \(c=c(r)\)). In orthonormal frame with \(\alpha=\partial_ra/a\), \(\beta=c'/c\),
\[
Q_{\hat a\hat b}=\mathrm{diag}\!\bigl(\alpha(\alpha+2\beta),-\alpha\beta,-\alpha\beta,-\alpha^2\bigr),
\]
which is anisotropic. The isotropic closure conditions are inconsistent for \(\alpha,\beta\neq0\). Hence:

1. The \(Q_{ab}\propto h_{ab}\) route to \(\Lambda_{\text{eff}}\) is ruled out for the stated Hopf ansätze.
2. Rank-1 Hopf deformation forces \(Q_{ab}=0\) algebraically.
3. Rank-2 deformation yields anisotropic effective source, not pure vacuum energy.

Therefore SC3 is not closed by classical Path-2 in Gaussian-normal cone geometry. The Gauss identity
\[
R^{(4)}=R^{(5)}-2R^{(5)}_{\mu\nu}n^\mu n^\nu+(K^2-K_{ab}K^{ab}),
\]
does not introduce a new intrinsic-curvature source when \(K_{ab}=0\). The remaining Occam-consistent open route for SC3 is a quantum vacuum contribution (Casimir energy) associated with compact Hopf-fiber boundary conditions on \(S^1\), with field content to be specified by the Paper 3 phase-transition sector.

### 3.5 The Self-Consistency System
Combining (SC1)–(SC3), the self-consistency conditions form a coupled system for \(A(r,z)\):
\[
\partial_z^2 A = (\dot H + H^2)A \tag{3.5.1a}
\]
\[
\partial_r^2 A - V_{\text{grav}}(r) A = 0 \tag{3.5.1b}
\]
\[
\Lambda_{\text{eff}}[A] = \Lambda_{\text{obs}} \tag{3.5.1c}
\]
with boundary conditions \(A(r_{\text{brane}}, z) = z\) (flatness + light-cone normalization at late times) and \(A \to 0\) as \(r \to \infty\) (normalizability). In the late-time flat branch \(A\sim z\,f(r)\), Eq. (3.5.1a) reduces to \(\partial_z^2A=0\). Given §3.4, Eq. (3.5.1c) is classically underdetermined in this geometry class and requires a quantum completion term (Casimir-on-fiber candidate) for closure.

### 3.5.2 Dynamic 5D \(\\to\) 4D effective transition and collapse criterion
The cone framework is interpreted as a regime transition rather than a single static branch:
1. **Phase I (5D-dominant):** bulk/extrinsic terms are non-negligible in brane observables.
2. **Phase II (crossover):** projected bulk terms and intrinsic 4D terms are comparable.
3. **Phase III (4D-effective):** standard 4D Einstein dynamics dominate on the brane with controlled residual bulk corrections.

This framing resolves a consistency ambiguity in collapse checks. The standard Schwarzschild radius,
\\[
R_s^{(4)}=\\frac{2G_4M}{c^2},
\\]
is treated as the primary criterion only in Phase III. In Phases I--II, horizon/collapse diagnostics are branch-dependent and must include projected 5D contributions (Weyl/extrinsic sector) before any black-hole-style inference is made.

For uniform-density consistency checks in the 4D-effective branch,
\\[
M(R)=\\frac{4\\pi}{3}\\rho R^3,\\qquad
\\frac{R_s^{(4)}}{R}=\\frac{8\\pi G_4\\rho}{3c^2}R^2,
\\]
with transition to collapse threshold at \\(R_s^{(4)}=R\\). This criterion is therefore a late-phase diagnostic, not a phase-independent identity of the full 5D model.

**Claim posture.** The manuscript treats 4D collapse estimates as valid only after effective 4D reduction is explicitly satisfied; pre-reduction branches remain conditional and require dedicated 5D horizon analysis.

To avoid over-identification of diagnostics, the model distinguishes three markers that are related but not definitionally identical:
1. **Pullback-metric inflection marker:** a kinematic marker on the chosen trajectory (minimum/inflection behavior of the trajectory pullback metric).
2. **Decoherence-frame resolvability crossover:** an inference marker (parity of decoherence-direction vs frame-direction resolvability in the separated-coordinate metric).
3. **Cross-coupling shutdown:** a structural marker where mixed \(M\)-\(\Sigma\) coupling terms become negligible.

In this draft, none of these is taken as *by-definition equivalent* to the others; equivalence is a calculational question to be demonstrated (or rejected) in the same branch and parameter regime.

### 3.6 Paper 3 Interface: Inputs Required for Casimir Closure
To make the SC3 closure term computable, Paper 2 requires the following inputs from the Paper 3 phase-transition sector:
1. **Fiber field content after transition:** species list on compact \(S^1\) Hopf fiber (bosonic/fermionic degrees, effective masses, and multiplicities).
2. **Boundary conditions on the fiber:** periodic/antiperiodic assignments by species, fixed by post-transition symmetry sector.
3. **Renormalization prescription:** subtraction scheme and reference vacuum used to define finite Casimir energy density.
4. **Geometric scale matching:** identification of effective fiber radius \(R_f(z)\) (or fixed \(R_f\)) in terms of cone variables and transition data.
5. **Sector activation rule:** criterion for which fields contribute at \(\lambda_D\to1\) and whether contributions evolve with \(z\).

Given (1)–(5), the quantum completion term is evaluated as
\[
\rho_{\mathrm{Casimir}}(z)\equiv \rho_{\mathrm{vac}}^{S^1}[R_f(z),\{\Phi\},\mathrm{BC}],
\]
and inserted into Eq. (3.5.1c) through \(\Lambda_{\mathrm{eff}}^{\mathrm{quant}}=8\pi G_4\,\rho_{\mathrm{Casimir}}\).

**Sign consistency requirement.** For periodic massless bosons on \(S^1\), the Casimir contribution is negative; this cannot close SC3 (\(\Lambda_{\mathrm{eff}}>0\)) in the intended branch. Therefore the post-transition field-content/BC sector must produce a net positive renormalized \(\rho_{\mathrm{Casimir}}\) (e.g., mixed boson/fermion content and/or mixed boundary conditions). This is a required consistency test, not an optional model preference.
### 3.7 SC3 Casimir sign-closure decision scaffold (NOW item #3)
This subsection defines the decision protocol for upgrading SC3 from “open with candidate mechanism” to a closed quantitative branch.

**Step A — Fix sign conventions and subtraction baseline.**
Before spectrum evaluation, lock:
1. metric/sign conventions used in vacuum-energy extraction,
2. renormalization subtraction reference vacuum,
3. normalization mapping from \(\rho_{\mathrm{Casimir}}\) to \(\Lambda_{\mathrm{eff}}^{\mathrm{quant}}=8\pi G_4\rho_{\mathrm{Casimir}}\).

No sign claim is admissible until this convention layer is explicit.

**Step B — Evaluate sector contributions transparently.**
Decompose
\[
\rho_{\mathrm{Casimir}}=\sum_s \rho_s(R_f,m_s,\mathrm{BC}_s),
\]
with per-species bookkeeping:
- boson/fermion statistics,
- boundary condition (periodic/antiperiodic/mixed),
- effective mass regime (\(m_sR_f\ll1\), \(m_sR_f\sim1\), \(m_sR_f\gg1\)),
- multiplicity and activation rule at \(\lambda_D\to1\).

**Step C — Branch test and decision outcomes.**
Classify results into:
1. **PASS branch:** \(\rho_{\mathrm{Casimir}}>0\) in the physically selected post-transition sector, giving \(\Lambda_{\mathrm{eff}}^{\mathrm{quant}}>0\) with observed-order consistency window.
2. **MARGINAL branch:** sign-sensitive cancellation requiring narrow tuning; retain SC3 as open (no closure claim).
3. **FAIL branch:** \(\rho_{\mathrm{Casimir}}\le0\) in physically admissible sectors; Casimir route does not close SC3 in current model.

**Step D — Robustness and anti-tuning checks.**
For any provisional PASS result, require:
1. stability of sign under small perturbations of \(R_f\), masses, and boundary-condition assignments consistent with Paper 3,
2. no reliance on ad hoc species insertion introduced solely to flip sign,
3. compatibility with radion/\(r_{\mathrm{brane}}\) stabilization assumptions used later in §5.

**Completion criteria for claim upgrade.**
SC3 claim strength may be upgraded only if:
1. a PASS branch is demonstrated with explicit per-species accounting,
2. robustness checks are passed without fine-tuned cancellations,
3. the resulting \(\Lambda_{\mathrm{eff}}\) scale is consistent with stated observational target order.

If criteria are not met, SC3 remains open and the manuscript must keep Casimir closure language explicitly conditional.
### 3.7.1 Branch-screening computation (2026-03-01; non-final)

*Computed via zeta-function regularization on S¹; see `casimir_computation.py` in this directory for full derivation and numerical tables.*

#### Sign conventions locked (Step A)

- Geometry: \(\mathbf{R}^{3,1}\times S^1(r)\), circumference \(L=2\pi r\).
- Periodic BCs on bosons \(\Rightarrow\) negative Casimir density.
- Antiperiodic BCs on fermions \(\Rightarrow\) positive Casimir density.
- Renormalization: zeta-function regularization, no normal-ordering subtraction.
- Mapping: \(\Lambda_{\mathrm{eff}} = 8\pi G_4\,\rho_{\mathrm{Casimir}}\).

#### Closed-form result

For \(N_B\) massless real bosonic d.o.f.\ (periodic) and \(N_F\) massless Weyl fermionic d.o.f.\ (antiperiodic) on \(S^1(r)\):
\[
\rho_{\mathrm{Casimir}} = \frac{\pi^2 \hbar c}{90\,r^4}\!\left(\frac{7N_F}{8} - N_B\right). \tag{3.7.1}
\]
SC3 positivity requires the dimensionless factor \(f \equiv 7N_F/8 - N_B > 0\), i.e.\ \(N_F > 8N_B/7\).

#### Branch-screening table (Steps B & C)

| Sector | \(N_B\) | \(N_F\) | Factor \(f\) | Verdict |
|---|---|---|---|---|
| Branch 3: 2 photon polarizations, no fermions | 2 | 0 | −2.000 | **FAIL** |
| SM photon + graviton (4 bosons, no fermions) | 4 | 0 | −4.000 | **FAIL** |
| 1 boson + 1 Weyl fermion | 1 | 1 | −0.125 | **FAIL** |
| Gravitino sector \(N_B=2, N_F=2\) | 2 | 2 | −0.250 | **FAIL** |
| Full SUSY \(N_B = N_F = 4\) | 4 | 4 | −0.500 | **FAIL** |
| 2 bosons + 3 Weyl fermions (min-integer PASS) | 2 | 3 | +0.625 | PASS (sign only) |
| 2 bosons + 4 Weyl fermions | 2 | 4 | +1.500 | PASS (sign only) |
| Pure fermion sector \(N_F=4\) | 0 | 4 | +3.500 | PASS (sign only) |

**SUSY note:** exact supersymmetry (\(N_B = N_F\)) gives \(f = -N_F/8 < 0\). Full SUSY makes SC3 *worse*, not better; it cannot serve as the post-transition sector.

#### Scale finding (Step D)

At \(r_{\mathrm{fiber}} = \ell_P = 1.616\times10^{-35}\,\mathrm{m}\):
\[
|\rho_{\mathrm{Casimir}}| \approx 10^{113}\,\mathrm{J/m^3} \approx 10^{122}\,\rho_{\mathrm{target}},
\]
where \(\rho_{\mathrm{target}} = \Lambda_{\mathrm{obs}}\,c^4/(8\pi G_4) \approx 5.3\times10^{-10}\,\mathrm{J/m^3}\). The fiber radius required to match the observed scale is
\[
r^* \approx 50\text{--}100\;\mu\mathrm{m} \approx 3\text{--}4\times10^{30}\,\ell_P \quad\text{(all sectors).}
\]
This is just below current fifth-force experimental bounds (\(\lesssim 100\,\mu\mathrm{m}\)). SC3 closure via Casimir at \(r_{\mathrm{fiber}} = \ell_P\) would require \(\sim10^{122}\) boson/fermion cancellation — unacceptable fine-tuning.

#### Task 3A (Atiyah–Singer) corollary

S³ is odd-dimensional; the standard chiral Dirac index vanishes by dimensional parity. Zero modes on S³ exist but are metric-dependent (Hitchin, via Berger sphere analysis), not topologically guaranteed. There is no index-theorem argument that forces the Hopf fiber to carry fermionic content (\(N_F \geq 3\)). The sign of \(\rho_{\mathrm{Casimir}}\) on the compact \(\psi\)-direction is determined entirely by the boundary conditions chosen in the post-transition sector. **Axiom B is doing all the work and is genuinely contingent on Paper 3 D1.**

#### Current SC3 status

- Boson-only and all SUSY sectors: **FAIL**.
- \(N_F \geq 3\) antiperiodic fermions with \(N_B = 2\): sign-**PASS** (factor \(f = +0.625\)), but requires \(r_{\mathrm{fiber}} \approx 50\,\mu\mathrm{m}\) and an independent stabilization argument (§5.2).
- No PASS branch established without Paper 3 species/BC inputs.
- SC3 claim posture: **OPEN (staged)**. Casimir closure is a contingent candidate only.
*Execution-status and spike-log details are tracked in Appendix A.*

---

### 3.7.2 Paper 3 interface — pending inputs for SC3 closure
*[PLACEHOLDER — to be completed when Paper 3 post-transition results are available.]*

This section is reserved for the results that Paper 3 must supply to attempt a full PASS-branch closure of SC3. The required inputs are enumerated in §3.6 items (1)–(5). When Paper 3 delivers them, append here:

**P3-INPUT-A — Post-transition species list:**
> *[Insert: species on compact S¹ Hopf fiber after geometric phase transition; bosonic/fermionic degrees of freedom, effective masses, multiplicities.]*

**P3-INPUT-B — Boundary condition assignments:**
> *[Insert: periodic/antiperiodic assignments by species, fixed by post-transition symmetry sector. This determines the sign of each \(\rho_s\) contribution.]*

**P3-INPUT-C — Renormalization prescription:**
> *[Insert: subtraction scheme and reference vacuum used to define finite \(\rho_{\mathrm{Casimir}}\). Must be compatible with conventions locked in §3.7.1 Step A.]*

**P3-INPUT-D — Fiber radius \(R_f\) identification:**
> *[Insert: identification of effective fiber radius \(R_f(z)\) in terms of cone variables and transition data. Note: SC3 closure requires \(R_f \approx 50\text{--}100\,\mu\mathrm{m}\); any identification yielding \(R_f \sim \ell_P\) faces the \(10^{122}\) hierarchy problem documented in §3.7.1.]*

**P3-INPUT-E — Sector activation rule:**
> *[Insert: criterion for which fields contribute at \(\lambda_D \to 1\) and whether contributions evolve with \(z\).]*

**Re-entry action (when inputs above are filled):** run `casimir_computation.py` with finalized \(N_B, N_F, R_f\) values, verify against PASS criteria in §3.7 Step C, and replace this placeholder with the computed result. Update §5.7.2 item 3 status from "Active (staged)" to "Active" or "Closed" accordingly.

## §4 Geometric Dark-Matter Response
### 4.1 Framing
The following is a model claim, not an empirical conclusion. We propose that matter density inhomogeneities on the observable brane induce geometric distortions of the cone in the \(r\)-direction — perturbations of \(A(r,z)\) sourced by local matter overdensities — and that these distortions produce an additional effective gravitational pull on brane matter that mimics a pressureless dust component. This is the K³ candidate mechanism for dark-matter-like phenomenology, requiring no new particle species, no free coupling constants, and no modification of general relativity on the brane.

### 4.2 Perturbation Setup
Let \(A(r,z) = A_0(r,z) + \delta A(r,z;\vec{\theta})\), where \(A_0\) is the background self-consistent solution of §3 and \(\delta A\) is sourced by a matter overdensity \(\delta\rho(\vec{\theta},z)\) on the brane. The brane stress-energy sourcing the bulk is localized at \(r = r_{\text{brane}}\):
\[
\delta T_{MN} = \delta(r - r_{\text{brane}})\,\text{diag}(-\delta\rho, 0, 0, 0, 0) \tag{4.2.1}
\]
so that \(\delta T_{rr} = 0\) in the bulk interior and the sourcing enters through the boundary condition. We adopt the following linearized bulk equation for \(\delta A\) in the background \(A_0\) as a model ansatz (to be derived explicitly from linearized 5D Einstein equations in follow-up work):
\[
\left[\partial_r^2 + \frac{3}{A_0}\partial_r A_0\,\partial_r - \frac{1}{A_0^2}\nabla^2_\theta - \partial_z^2\right]\delta A = 0 \quad (r \neq r_{\text{brane}}) \tag{4.2.2}
\]

with Israel junction condition at the brane sourcing the normal derivative:
\[
\left.\partial_r \delta A\right|_{r=r_{\text{brane}}} = -\frac{4\pi G_5}{A_0}\,\delta\rho(\vec{\theta},z) \tag{4.2.3}
\]

The bulk equation (4.2.2) with boundary condition (4.2.3) and normalizability as \(r \to \infty\) determines \(\delta A\) uniquely given \(\delta\rho\). In the KK zero-mode approximation (modes with \(r\)-wavelength \(\gg r_{\text{brane}}\)), the \(r\)-dependence of \(\delta A\) is governed by the same graviton wavefunction as §3.3, and \(\delta A\) evaluated at \(r = r_{\text{brane}}\) satisfies:
\[
\delta A\big|_{\text{brane}} \simeq \frac{G_5}{2\mu A_0}\,\delta\rho(\vec{\theta},z) \cdot e^{-\mu r_{\text{brane}}} \tag{4.2.4}
\]
### 4.2.5 Derivation scaffold for Eq. (4.2.2)
Eq. (4.2.2) remains an ansatz until the following derivation path is completed. This subsection defines the closure target and acceptance criteria.

**Step A — Background and perturbation split.**
Write
\[
g_{MN}=g^{(0)}_{MN}[A_0(r,z)] + h_{MN},
\]
with \(g^{(0)}_{MN}\) given by (2.2.1) and \(h_{MN}\) restricted to scalar-sector perturbations sourced by brane matter. The working projection keeps \(\delta A\) as the scalar deformation of the angular block:
\[
h_{ij}=2A_0\,\delta A\,\gamma_{ij},\qquad h_{rz}=h_{ri}=0 \ \text{(gauge-fixed target)}.
\]

**Step B — Linearized bulk equations (off-brane).**
Compute \(\delta G_{MN}^{(5)}[h;g^{(0)}]\) for \(r\neq r_{\mathrm{brane}}\) with \(\delta T_{MN}=0\) in the bulk interior, enforcing
\[
\delta G_{MN}^{(5)}=0.
\]
The scalar master equation must reduce to a second-order operator on \(\delta A\) with explicit coefficient matching against
\[
\mathcal{L}_{\mathrm{ans}}[\delta A]
=\left[\partial_r^2+\frac{3}{A_0}(\partial_r A_0)\partial_r-\frac{1}{A_0^2}\nabla_\theta^2-\partial_z^2\right]\delta A.
\]

**Step C — Junction derivation at the brane.**
Derive the jump condition from Israel matching for the perturbed extrinsic curvature:
\[
\big[\delta K_{ab}-h_{ab}\delta K\big]_{r=r_{\mathrm{brane}}}
=-8\pi G_5\,\delta S_{ab},
\]
with \(\delta S_{ab}\) induced by (4.2.1). Show that the scalar sector projects to (4.2.3), including sign and normalization factors.

**Step D — Mode decomposition and consistency checks.**
Perform angular harmonic decomposition on \(S^3\) and identify the \(l=0\) / long-wavelength branch used in §4.3. Verify:
1. no omitted constraint equation reintroduces additional scalar source terms,
2. no gauge artifact generates spurious \(\partial_z\partial_r\) cross-terms in the reduced equation,
3. KK zero-mode reduction recovers the scaling form used in (4.2.4).

**Completion criteria for claim upgrade.**
Eq. (4.2.2) can be upgraded from ansatz to derived only if:
1. the bulk scalar operator coefficients match \(\mathcal{L}_{\mathrm{ans}}\) (or documented corrected form),
2. the junction condition reproduces (4.2.3) up to explicitly tracked conventions,
3. the reduction to §4.3 static limit is algebraically consistent.

If any criterion fails, keep Eq. (4.2.2) labeled as ansatz and update §4.3–§4.5 claims to the weaker branch accordingly.
*Execution-status and spike-log details are tracked in Appendix A.*
### 4.2.6 Active derivation core (partial closure; non-final)
Using the scalar-sector projection defined in §4.2.5 with
\[
h_{ij}=2A_0\,\delta A\,\gamma_{ij},\qquad h_{r\mu}=0\ \text{(working gauge)},
\]
the linearized off-brane equations \(\delta G^{(5)}_{MN}=0\) yield, at principal scalar order, a master operator of the form
\[
\mathcal{L}_{\mathrm{core}}[\delta A]
=\left[\partial_r^2+\frac{3}{A_0}(\partial_r A_0)\partial_r-\frac{1}{A_0^2}\nabla_\theta^2-\partial_z^2\right]\delta A
+\Delta_{\mathrm{mix}}[\delta A]=0,\quad r\neq r_{\mathrm{brane}}. \tag{4.2.5a}
\]
Here \(\Delta_{\mathrm{mix}}\) collects residual mixed-component terms (constraint/gauge sector), including potential \(\partial_z\partial_r\delta A\) and trace-coupling contributions that vanish only after full scalar constraint closure. The leading operator in (4.2.5a) matches Eq. (4.2.2); therefore Eq. (4.2.2) is now supported as the principal scalar reduction, but not yet as a fully closed derived equation.

At the brane, the perturbed Israel condition gives
\[
\left.\partial_r\delta A\right|_{r=r_{\mathrm{brane}}}
=-\frac{4\pi G_5}{A_0}\,\delta\rho
+\Delta_{\mathrm{junc}}, \tag{4.2.5b}
\]
where \(\Delta_{\mathrm{junc}}\) encodes convention-sensitive trace and gauge pieces from \(\delta K_{ab}\). In the current reduction, \(\Delta_{\mathrm{junc}}\) is treated as subleading; this recovers Eq. (4.2.3) as the working boundary condition used in §§4.3–4.5.

**Status after active pass.** The derivation now closes at principal scalar order (operator structure + boundary form), while full closure still requires demonstrating \(\Delta_{\mathrm{mix}}\to0\) (or controlled boundedness) in a gauge-consistent mode decomposition. Until that step is completed, Eq. (4.2.2) remains tagged as an ansatz-backed principal reduction rather than a final theorem-level result.

### 4.3 Effective Force on Brane Matter
**Static large-scale limit.** At scales \(\ell \gg H^{-1}_{\text{local}}\) (larger than the local Hubble scale) and late times (\(z \gg \ell_P\)), the \(z\)-dependence of \(\delta A\) becomes slow relative to the \(\theta\)-gradients. In this limit \(\partial_z \delta A \ll \nabla_\theta \delta A / A_0\) and eq. (4.2.2) reduces to:
\[
\nabla^2_\theta\,\delta A = A_0\,\partial_r(A_0\,\partial_r \delta A) \tag{4.3.1}
\]

which is a static (\(z\)-independent) equation for \(\delta A\) given \(\delta\rho\). The induced metric perturbation on the brane is:
\[
\delta h_{\theta\theta} = 2A_0\,\delta A\,\gamma_{\theta\theta} \tag{4.3.2}
\]

The effective stress-energy from this metric perturbation is:
\[
\delta T^{\text{eff}}_{\mu\nu} = \frac{1}{8\pi G_4}\,\delta G^{(4)}_{\mu\nu}\big|_{\delta h} \tag{4.3.3}
\]

In the static limit, \(\delta G^{(4)}_{00} \sim \nabla^2 \delta h / A_0^2\) (Poisson-like) and \(\delta G^{(4)}_{ij} \sim \partial_i\partial_j \delta h - \delta_{ij}\nabla^2\delta h / 2\) with no time-derivative terms. The effective pressure is therefore:
\[
\delta p^{\text{eff}} = \frac{1}{3}\delta^{ij}\delta T^{\text{eff}}_{ij} \xrightarrow{\text{isotropic, static}} 0 \tag{4.3.4}
\]
because for a static perturbation the spatial stress structure is gradient-dominated in the Poisson sector. Therefore:
\[
\boxed{w = \frac{\delta p^{\text{eff}}}{\delta \rho^{\text{eff}}}\ \text{is a closure-dependent quantity; }w\approx 0\ \text{is provisional in this draft}} \tag{4.3.5}
\]
A pure scalar Poisson-sector reduction yields \(w=-1/3\); obtaining \(w\approx0\) requires additional structure in the full linearized 5D system. This section therefore defines a test condition for follow-up derivation rather than a completed proof.

*[Model claim: the static limit is self-consistent for galaxy-scale overdensities at late times. Validity at cluster scales and during structure formation requires the full time-dependent numerical treatment.]*
### 4.3.6 Derivation scaffold for \(w\)-closure
The objective is to replace the provisional statement in (4.3.5) with a derived branch statement from the full linearized 5D system.

**Step A — Define effective 4D source unambiguously.**
Starting from the derived perturbation sector of §4.2.5, construct
\[
\delta T_{\mu\nu}^{\mathrm{eff}} := \frac{1}{8\pi G_4}\,\delta G_{\mu\nu}^{(4)}\big|_{\text{projected from 5D perturbations}},
\]
and fix projection conventions so that \(\delta \rho^{\mathrm{eff}}=\delta T_{00}^{\mathrm{eff}}\) and
\[
\delta p^{\mathrm{eff}}=\frac13\,\delta^{ij}\delta T_{ij}^{\mathrm{eff}}
\]
are gauge-stable observables in the selected scalar sector.

**Step B — Separate regimes before solving.**
Compute \(w\equiv \delta p^{\mathrm{eff}}/\delta \rho^{\mathrm{eff}}\) in three controlled limits:
1. **Static Poisson branch** (\(\partial_z\to0\), long-wavelength angular modes),
2. **Quasi-static branch** (small but nonzero \(\partial_z\), adiabatic in \(z\)),
3. **Time-dependent branch** (full scalar perturbation system with retained \(\partial_z\) terms).

This prevents mixing incompatible approximations when quoting a single \(w\).

**Step C — Identify closure branch and its domain.**
Report \(w\) as either:
- \(w=-1/3\) (pure scalar Poisson closure),
- \(w\approx0\) (dust-like closure),
- \(w=w(k,z)\) (scale/time dependent closure).

Any \(w\approx0\) claim must include the explicit regime restrictions (\(k\)-range, \(z\)-range, and neglected terms).

**Step D — Internal consistency tests.**
Require all of:
1. conservation consistency \(\nabla^\mu \delta T_{\mu\nu}^{\mathrm{eff}}=0\) in the retained order,
2. no sign/pathology in \(\delta \rho^{\mathrm{eff}}\) for the quoted branch,
3. compatibility of the chosen \(w\)-branch with §4.5 claims (RAR/rotation-curve language and Bullet-timescale assumptions).

**Completion criteria for claim upgrade.**
The manuscript may upgrade beyond “provisional \(w\)” only if:
1. one branch is derived from the full linearized system (not only scalar Poisson truncation),
2. domain-of-validity is explicitly stated,
3. downstream phenomenology text is synchronized to that branch.

If criteria are not met, retain (4.3.5) as provisional and keep dark-matter claims in the “partial mechanism under test” posture.
*Execution-status and spike-log details are tracked in Appendix A.*
### 4.3.7 Staged closure note: static/quasi-static branch (active result; non-final)
Given the principal-order operator closure in §4.2.6 and neglecting \(\Delta_{\mathrm{mix}}\) at leading static order:
1. **Static scalar branch:** reproduces Poisson-sector behavior with \(w=-1/3\) as the default reduced-branch output.
2. **Quasi-static branch:** allows corrections from retained slow \(\partial_z\) terms; this branch can shift the effective ratio away from \(-1/3\), but no robust \(w\approx0\) claim is made yet.

**Current executable claim.** The manuscript adopts a branch-aware statement:
\[
w\in\{-1/3,\ \text{quasi-static corrected branch}\},\quad \text{with full }w(k,z)\text{ pending time-dependent closure}. \tag{4.3.6}
\]
This result is sufficient for immediate claim-tightening and dependency handoff to the HOLD queue (Bullet-timescale consistency), while preserving non-final status pending full mode-consistent closure.

### 4.4 Distinguishing Features
Without the explicit \(A_0(r,z)\) background, the amplitude of the geometric dark-matter response can be estimated from the boundary condition (4.2.3) and the KK zero-mode result (4.2.4). The effective surface density of the geometric dark-matter response at the brane is:
\[
\Sigma_{\text{eff}} \sim \frac{G_5}{G_4\,\mu\,A_0^2}\,\Sigma_b \tag{4.4.1}
\]
where \(\Sigma_b = \int \delta\rho\,dz\) is the baryonic surface density and the ratio \(G_5 / G_4 \sim \mu^{-1}\) from the RS localization relation \(G_4 = G_5 \mu / (2\pi)\) \cite{RandallSundrum1999b}. Substituting:
\[
\Sigma_{\text{eff}} \sim \frac{1}{\mu^2 A_0^2}\,\Sigma_b \tag{4.4.2}
\]

For the geometric dark-matter response to match the observed \(\Sigma_{\text{eff}} / \Sigma_b \sim 5\)–\(6\) (universal dark-matter-to-baryon ratio at large scales \cite{Planck2018}), the combination \(\mu^2 A_0^2\) must equal \(\sim 1/5\) at the brane. This constrains the warp scale \(\mu\) and the background \(A_0(r_{\text{brane}}, z)\) jointly — a condition that links the dark-matter amplitude to the same geometric parameters controlling gravity localization (SC2) and flatness (SC1). Whether the self-consistent \(A_0\) solution satisfies this constraint without tuning is a prediction of the numerical follow-up, not an input.

*[This estimate is order-of-magnitude only. The factor \(1/(\mu^2 A_0^2)\) encodes both the localization efficiency and the background geometry; its value requires the explicit \(A_0\).]*

### 4.5 Observational Predictions and Constraints
#### 4.5.1 Rotation Curves
For a disk galaxy with baryonic surface density \(\Sigma_b(R)\) (where \(R\) is galactocentric radius), the geometric dark-matter response adds an effective surface density \(\Sigma_{\text{eff}}(R) \propto \Sigma_b(R)\) from (4.4.2). The circular velocity becomes:
\[
v_c^2(R) = v_b^2(R) + v_{\text{eff}}^2(R) = \frac{G_4 M_b(<R)}{R}\left(1 + \frac{1}{\mu^2 A_0^2}\right) \tag{4.5.1}
\]

At large \(R\) where \(M_b(<R) \to M_{\text{total}}\) (constant), \(v_c^2 \propto 1/R \to 0\) — the geometric response does not produce flat rotation curves in this simplest form. The geometric response is proportional to \(\Sigma_b\), not a fixed background halo. Flat rotation curves require either (a) the \(r\)-dependence of \(\delta A\) to produce a scale-dependent amplification, or (b) the time-dependent terms (corrections to the static limit) to contribute. This is a known tension that requires the full numerical \(A_0\).

*[Known limitation: K³ geometric dark matter in the static limit does not automatically produce flat rotation curves. This must be resolved in the numerical follow-up or acknowledged as a limitation of the model.]*

#### 4.5.2 Radial Acceleration Relation (RAR)
McGaugh et al. \cite{McGaugh2016} establish that the observed centripetal acceleration \(g_{\text{obs}}\) correlates tightly with the baryonic Newtonian acceleration \(g_{\text{bar}} = G_4 M_b(<R)/R^2\) across galaxy types:
\[
g_{\text{obs}} = \frac{g_{\text{bar}}}{1 - e^{-\sqrt{g_{\text{bar}}/a_0}}} \tag{4.5.2}
\]
with Milgrom acceleration scale \(a_0 \approx 1.2 \times 10^{-10}\) m s\(^{-2}\).

The K³ geometric response (4.4.2) produces \(\Sigma_{\text{eff}} \propto \Sigma_b\) — a tight baryonic correlation — consistent with the RAR's zero scatter at fixed \(g_{\text{bar}}\). However, reproducing the specific functional form (4.5.2) and the value of \(a_0\) requires the amplitude \(1/(\mu^2 A_0^2)\) to be scale-dependent in a specific way, transitioning from \(\sim 0\) at high \(g_{\text{bar}}\) (baryon-dominated, inner regions) to \(\sim 5\) at low \(g_{\text{bar}}\) (dark-matter-dominated, outer regions). Whether the cone geometry naturally produces this transition — and whether \(a_0\) emerges from \(\mu\) and \(r_{\text{brane}}\) without tuning — is an open calculation.

**If K³ can derive \(a_0 \approx 1.2 \times 10^{-10}\) m s\(^{-2}\) from \(\mu\) and \(r_{\text{brane}}\) without a free parameter, this constitutes a falsifiable prediction.**

#### 4.5.3 The Bullet Cluster Constraint
The Bullet Cluster (1E 0657-558) provides the most stringent constraint on dark matter alternatives \cite{Clowe2006}. After two galaxy cluster cores passed through each other, weak gravitational lensing maps show the mass concentration (inferred dark matter) offset from the hot gas (X-ray emission) and coincident with the stellar/galaxy component. Since the hot gas (\(\sim\)80% of baryonic mass) is ram-pressure decelerated while galaxies (\(\sim\)20% of baryonic mass) pass through ballistically, any model in which the dark-matter response is sourced by total baryonic density faces a tension: the predicted lensing peaks would be weighted toward the gas, not the galaxies.

**The K³ tension.** The boundary condition (4.2.3) sources \(\delta A\) from \(\delta\rho_{\text{total}} = \delta\rho_{\text{gas}} + \delta\rho_{\text{stars}}\). Post-collision, \(\delta\rho_{\text{gas}}\) is centered between the clusters while \(\delta\rho_{\text{stars}}\) is offset with the galaxies. The naive K³ prediction — lensing peaks at the \(\delta\rho_{\text{total}}\)-weighted centroid — would place them between the galaxies and the gas, inconsistent with observations.

**Two possible resolutions within K³:**
1. **Bulk propagation timescale.** The geometric response to \(\delta\rho\) propagates through the bulk at finite speed (bounded by \(c\) in the \(r\)-direction). If the cluster collision timescale \(\tau_{\text{collision}} \sim r_{\text{cluster}}/v_{\text{collision}} \sim 0.1\)–\(0.3\) Gyr is short compared to the bulk equilibration time \(\tau_{\text{bulk}} \sim r_{\text{brane}}/c\), the \(\delta A\) field does not redistribute during the collision — it retains its pre-collision configuration, which was centered on the total mass (galaxies + gas). Post-collision, \(\delta A\) relaxes toward the new \(\delta\rho\) configuration on timescale \(\tau_{\text{bulk}}\). If \(\tau_{\text{bulk}} \gg \tau_{\text{collision}}\), the lensing signal follows the pre-collision geometry — i.e., the galaxies, which maintained their trajectories. This is a testable prediction: the offset should evolve on timescale \(\tau_{\text{bulk}}\).
2. **Density threshold.** If the geometric response is dominated by the highest-density structures (galactic cores, stellar concentrations) rather than linearly tracking all baryons, the galaxy component may dominate despite its smaller total mass. This requires the response to be nonlinear in \(\delta\rho\), not captured by the linearized (4.2.3). A nonlinear boundary condition would be required.
*[The Bullet Cluster tension is genuine and must be resolved in the numerical follow-up. No preferred resolution is claimed at this stage. Resolution (1) can conflict with strict baryon-tracking (F2) if invoked in a regime where the response is expected to follow present baryonic centroids, while Resolution (2) requires explicit nonlinear sourcing beyond the current linearized system. The manuscript therefore treats both as unresolved branches pending a single self-consistent dynamical regime.]*
*[Consistency requirement: the model must choose and verify a single timescale regime across observables. A slow-relaxation regime used to explain Bullet Cluster offsets can conflict with a fast-tracking regime used to claim baryon-following response in galaxy dynamics. This is an explicit falsification checkpoint.]*
*[Phase-consistency requirement: any Bullet-timescale branch used here must be explicitly qualified against the dynamic 5D \(\\to\) 4D regime map in §3.5.2; 4D-effective diagnostics are admissible only in the Phase III branch.]* 
*[Marker-consistency requirement: any Bullet-timescale interpretation must declare which transition marker is being used (pullback-metric inflection, resolvability crossover, or mixed-coupling suppression), and must not treat these as exact identities unless item §5.2(10) is explicitly closed in the same branch.]*

### 4.6 Distinguishing Features and Falsification Criteria
The geometric dark-matter response has the following features distinguishing it from particle dark matter, stated as falsification criteria:

**F1 — No free parameters:** \(\delta A\) is determined entirely by \(\delta\rho\) and \(A_0(r,z)\); there is no dark-matter mass, cross-section, or coupling to tune. **Falsification:** any observation requiring an independent dark-matter parameter (mass spectrum, self-interaction cross-section) that cannot be derived from the cone geometry falsifies K³ geometric dark matter.

**F2 — Baryonic correlation:** the effective dark-matter distribution is sourced by and traces the baryonic distribution. **Falsification:** dark-matter substructure that is not correlated with any baryonic structure (e.g., dark matter-only halos with no associated baryons) would falsify the model. Current evidence: dark-matter-only halos are not observationally confirmed; the claimed “dark galaxy” candidates have baryonic associations.

**F3 — Void suppression:** \(\delta A \to 0\) where \(\delta\rho \to 0\); the geometric response vanishes in cosmic voids. **Falsification:** detection of dark matter in voids at levels inconsistent with \(\delta A \propto \delta\rho\) would falsify the model. Current evidence: voids are observed to be deficient in both baryons and inferred dark matter, consistent with F3.

**F4 — Bullet Cluster timescale:** the geometric dark-matter offset from baryons after a cluster collision should evolve on timescale \(\tau_{\text{bulk}} \sim r_{\text{brane}}/c\). **Falsification:** if the offset is static and permanent rather than evolving, resolution (1) of §4.5.3 is ruled out and resolution (2) must hold, requiring nonlinear sourcing.

**F5 — Flat rotation curves:** in the static large-scale limit, K³ geometric dark matter does not automatically produce flat rotation curves (§4.5.1). **If the numerical follow-up confirms this limitation, K³ geometric dark matter fails as a complete dark matter substitute and must be reframed as a partial mechanism requiring additional structure.**

*[F5 is an honest statement of a known limitation. Including it explicitly is preferable to a referee discovering it.]*

## §5 Open Problems and Resolution Plan
### 5.1 Scope and status
The current manuscript establishes a consistent geometric scaffold and several negative classical results (notably SC3 non-closure in the Gaussian-normal branch). The following items remain unresolved and are stated here as explicit closure tasks.

### 5.2 Unresolved points, closure calculations, and effort
1. **SC3 sign consistency (Casimir closure)**
   - **Status:** Open; classical branch closed, quantum branch conditional.
   - **Gating calculation:** compute explicit \(\\rho_{\\mathrm{Casimir}}(R_f)\) from finalized post-transition spectrum/BCs/renormalization and verify net \(\\rho_{\\mathrm{Casimir}}>0\).
   - **Effort:** Medium (4–7 working days).

2. **\(SU(2)\) sector status**
   - **Status:** Open (geometric identification only).
   - **Gating calculation:** one explicit derivation route (group-manifold reduction or equivalent) producing gauge kinetic terms and couplings.
   - **Effort:** High (1–2+ weeks).

3. **Bulk perturbation equation (4.2.2)**
   - **Status:** Open; principal reduction established, full closure pending.
   - **Gating calculation:** full derivation from linearized 5D Einstein equations including mode decomposition, constraints, and junction terms.
   - **Effort:** Medium (5–8 working days).

4. **Effective equation of state \(w\)**
   - **Status:** Open; static/quasi-static branch stated, no full time-dependent closure.
   - **Gating calculation:** compute \(\\delta G_{\\mu\\nu}^{(4)}\) from the full linearized 5D system and extract \(w(k,z)\) with explicit regime bounds.
   - **Effort:** Medium-High (1–2 weeks including validation).

5. **Bullet Cluster timescale consistency**
   - **Status:** Open; branch alternatives retained, no preferred mechanism.
   - **Gating calculation:** solve time-dependent bulk-brane response for \(\\delta A\), estimate \(\\tau_{\\mathrm{bulk}}\), and enforce one consistent regime across galaxy/cluster observables.
   - **Effort:** High (1–2 weeks).

6. **\(r_{\mathrm{brane}}\) / radion stabilization**
   - **Status:** Open; parameter economy conditional.
   - **Gating calculation:** construct and minimize Casimir-inclusive radion/fiber effective potential, verify stability and fifth-force compatibility.
   - **Effort:** Medium-High (1–2 weeks).

7. **SCF fixed-point existence**
   - **Status:** Open; conjectural.
   - **Gating calculation:** define \(A\\mapsto \\mathcal{F}[A]\) and provide contraction/existence proof or robust numerical fixed-point evidence.
   - **Effort:** Medium (1 week initial proof-of-concept).

8. **Dark-matter completeness**
   - **Status:** Open; static-limit incompleteness acknowledged.
   - **Gating calculation:** determine whether full \(r\)-profile plus time dependence recovers rotation-curve flattening and RAR behavior.
   - **Effort:** High (1–2+ weeks).

9. **Volterra light-cone program (D2/A3/A4) under phase gating**
   - **Status:** Open; current Volterra formulation is treated as a Phase III effective branch until cross-phase corrections are derived.
   - **Gating calculation:** derive and implement phase-gated kernel decomposition
     \\[
     K_{\mathrm{full}}(T,T') = K_{4D}(T,T') + \delta K_{5D}(T,T'),
     \\]
     then compute local-vs-CMB effective \(H_0\) split with explicit transition handling \(z_{\mathrm{transition}}\).
   - **Acceptance checks:** (i) bounded \(\gamma\cdot S\) behavior near horizon regulator, (ii) explicit domain restriction for A3 (Phase III exact, high-\(z\) projected branch), (iii) A4 upgrade path (Phase III limit matching small-angle FLRW limit).
   - **Effort:** High (1–2+ weeks, coupled to SC2/SC3 branch choices).

10. **Transition-marker ordering and equivalence test**
   - **Status:** Open; marker definitions now separated in §3.5.2.
   - **Gating calculation:** in one fixed branch, compute and compare:
     1) pullback-metric inflection location,
     2) resolvability-crossover location,
     3) mixed-coupling suppression scale.
   - **Claim rule:** until verified, retain language that these are correlated indicators, not exact-by-definition identities.
   - **Effort:** Medium (4–7 working days once branch equations are fixed).

11. **SC3 full-path restart under GR closure functions (Path-1..4)**
   - **Status:** Open; reset declared in §3.1.1 and executable template fixed in §§3.1.2–3.1.3.
   - **Gating calculation:** rebuild each original path equation set into \\\\(\\\\mathcal{C}_p[A,\\\\text{fields};\\\\chi_p]=0\\\\), with explicit \\\\(R_s\\\\)-based discriminator and phase qualification.
   - **Acceptance checks:** (i) shared notation/units/conventions across all four paths, (ii) no path-specific horizon logic outside the common \\(\\chi_p\\) framework, (iii) single comparison table of PASS/MARGINAL/FAIL outcomes by path.
   - **Effort:** High (1–2+ weeks, dependent on SC2/SC3 parameter locks).
### 5.2.1 CR1 bridge item: \(T_{M\Sigma}\) derivation target
Paper 1 uses a single trajectory parameter \(\lambda\) in places where two roles are mixed:
1. physical decoherence progression (natural \(M\)-direction variable),
2. coherence-frame displacement (natural \(\Sigma\)-direction variable).

To prevent category mixing and clarify downstream derivations, Paper 2 should separate:
\[
\lambda_M \in M,\qquad \lambda_\Sigma \in \Sigma,\qquad \lambda_\Sigma=\lambda_\Sigma(\lambda_M;\text{couplings}).
\]
Then the pulled-back tensor along the trajectory is
\[
T_{\gamma\gamma}
=T_{MM}\dot{\lambda}_M^2
+2T_{M\Sigma}\dot{\lambda}_M\dot{\lambda}_\Sigma
+T_{\Sigma\Sigma}\dot{\lambda}_\Sigma^2. \tag{5.8.1}
\]

**Immediate technical objective.** Identify \(T_{M\Sigma}\) from the same dynamical sector that controls decoherence-rate evolution (the mode system behind §4.2.6), so the \(M\times\Sigma\) coupling is explicit rather than encoded implicitly in \(\lambda\).

**Claim posture.** Until \(T_{M\Sigma}\) is explicitly derived or bounded, any statement that treats \(G_{\lambda\lambda}\) as a fully separated geometric observable should be interpreted as trajectory-level (pullback) and not as proof of complete \(M\)-\(\Sigma\) factorization.

### 5.3 Claim-strength policy for this draft
The present manuscript-level posture is:
1. SC1/SC2: structurally formulated and partially constrained.
2. SC3: open, with Casimir-on-fiber as a contingent candidate.
3. Geometric dark matter: partial mechanism under test, not a complete substitute claim.
4. Parameter economy: conditional until radion/fiber stabilization is derived.

Detailed execution queues, feasibility spikes, and deferred-path tracking are moved to Appendix A.

## Appendix A — Execution Ledger and Deferred Work (Non-manuscript Tracking Layer)
This appendix preserves operational tracking, spike outcomes, and queue mechanics used during development. Main-text claims defer to this appendix for process provenance.

### A.1 Execution policy and queue framework
#### A.1.1 Baseline retrenchment policy
For each unresolved point in §5.2, keep a manuscript-visible stub with:
1. status (open),
2. retrenchment statement (conditional only),
3. escalation trigger (calculation needed for upgrade),
4. failure consequence (claim downgrade/removal language).

#### A.1.2 Non-abandonment execution rule
Each high-cost item receives a 2–4 hour feasibility spike:
1. tractable now \(\to\) active queue,
2. not tractable now \(\to\) deferred high-cost queue (preserved, not dropped).

#### A.1.3 Ranked queues (NOW / HOLD / PARKED)
1. NOW: Eq. (4.2.2) derivation closure; \(w\)-closure; SC3 Casimir sign consistency; radion/stabilization route selection.
2. HOLD: Bullet Cluster timescale consistency; SCF fixed-point existence; topological-vs-dynamical closure note.
3. PARKED: full \(SU(2)\) formal mechanism; dark-matter completeness against full rotation-curve/RAR fitting.

### A.2 Spike outcomes and staged results (2026-03-01)
1. **Spike 1 (Eq. 4.2.2):** principal scalar operator closure tractable; blocker is full gauge/constraint closure.
2. **Spike 2 (\(w\)-closure):** static/quasi-static branch closure tractable; full time-dependent closure depends on Spike 1 completion.
3. **Spike 3 (SC3 Casimir):** branch screening completed (including FAIL sectors and contingent sign-PASS sectors); robust PASS depends on finalized Paper 3 inputs.
4. **Spike 4 (radion/\(r_{\mathrm{brane}}\)):** route comparison supports staged MARGINAL posture; PASS depends on finalized SC3/Paper 3 Casimir inputs.

### A.3 Stabilization working hypotheses (speculative record)
The following are preserved as speculative candidates, not manuscript-level claims:
1. H1 Casimir fixed-point self-stabilization,
2. H2 Goldberger–Wise analog with \(\lambda_D\) as bulk scalar,
3. H3 KK massive-mode vs massless Casimir competition,
4. H4 thermal-tracking coincidence test.

### A.4 Active-status snapshot and promotion rule
Current active items and blockers:
1. Eq. (4.2.2): partial closure with residual \(\Delta_{\mathrm{mix}}\), \(\Delta_{\mathrm{junc}}\).
2. \(w\)-closure: staged branch statement active; full \(w(k,z)\) pending.
3. SC3 Casimir: branch-screening complete; PASS branch blocked on Paper 3 inputs.
4. Radion stabilization: conditional route comparison complete; PASS blocked on SC3 input finalization.

Promotion rule: upgrade staged items only when local completion criteria in §§3.7, 4.2.5, 4.3.6, and 5.2 are satisfied.

### A.5 New gating note: 5D-to-4D collapse-consistency branch
Operational decision rule for collapse checks:
1. Apply \\(R_s^{(4)}=2G_4M/c^2\\) only when the model is in the 4D-effective phase (Phase III in §3.5.2).
2. If still in 5D-dominant/crossover phase, keep collapse claims conditional and require projected 5D correction audit before interpretation.
3. Promote to manuscript-level closure only after explicit phase-qualification is attached to every \\(R_s\\)-based statement.
4. Do not map “Phase III onset” to any single transition marker by definition; where a marker is used operationally, state it explicitly and keep alternative markers tracked until §5.2(10) closure.
5. For Volterra/D2-A3-A4 usage, treat light-cone integrals spanning high \(z\) as cross-phase objects unless \(z_{\mathrm{transition}}\) and \(\delta K_{5D}\) are explicitly controlled.

### A.6 Relativistic closure equations (both phase states) and first-order \\(R_{\\mathrm{transition}}\\)
To keep collapse logic explicit under the two-state regime map of §3.5.2, use:

**State III (4D-effective closure branch).**
\\[
R_s^{(4)}(R)=\\frac{2G_4M(R)}{c^2},\\qquad
M(R)=\\frac{4\\pi}{3}\\rho R^3,
\\]
\\[
\\frac{R_s^{(4)}}{R}=\\frac{8\\pi G_4\\rho}{3c^2}R^2.
\\]
4D collapse threshold is \\(R_s^{(4)}=R\\), giving
\\[
R_{c,4D}=\\sqrt{\\frac{3c^2}{8\\pi G_4\\rho}}.
\\]

**State I/II (5D-dominant or crossover closure branch).**
Use a first-order projected correction to the 4D closure ratio:
\\[
\\frac{R_s^{\\mathrm{eff}}}{R}
=\\frac{R_s^{(4)}}{R}\\Bigg[1+\\eta\\Big(\\frac{\\ell_*}{R}\\Big)^2\\Bigg]
\\quad\\text{(first-order ansatz)},
\\]
where \\(\\ell_*\\) is the effective 5D crossover length and \\(\\eta\\) is a dimensionless projection coefficient (Weyl/extrinsic sector sign and magnitude).

Define the transition radius by equality of correction and baseline terms:
\\[
\\eta\\Big(\\frac{\\ell_*}{R_{\\mathrm{transition}}}\\Big)^2\\sim 1
\\quad\\Rightarrow\\quad
R_{\\mathrm{transition}}\\approx \\sqrt{|\\eta|}\\,\\ell_*.
\\]
Interpretation:
1. \\(R\\gg R_{\\mathrm{transition}}\\): 4D-effective closure dominates (State III).
2. \\(R\\lesssim R_{\\mathrm{transition}}\\): projected 5D terms are non-negligible (State I/II).

For \\(|\\eta|\\sim O(1)\\), first-order estimate reduces to \\(R_{\\mathrm{transition}}\\sim \\ell_*\\).
This is a staging estimate only; final closure requires direct extraction of \\(\\eta\\) and \\(\\ell_*\\) from the derived perturbation/Weyl sector.

**Marker discipline note.** The \(R_{\mathrm{transition}}\) estimate above is a branch-structure scale estimate, not by itself a proof that kinematic inflection and statistical resolvability crossover coincide. Any manuscript statement equating these requires explicit closure of §5.2 item 10.

**Closure-discriminator note (horizon vs curvature regime).** Define
\\[
\\chi\\equiv \\frac{R_s}{R}.
\\]
Crossing the Schwarzschild *diameter* threshold \\(R\\lesssim 2R_s\\) is treated as a strong-gravity branch trigger (black-hole-scale dynamics required). However, this does **not** imply negligible GR effects for \\(R>2R_s\\): curvature corrections remain present outside the horizon-scale branch and must be retained whenever precision requires them.

#### A.6.1 First-pass numerical estimate for \\(R_{\\mathrm{transition}}\\)
Using
\\[
R_{\\mathrm{transition}}\\approx \\sqrt{|\\eta|}\\,\\ell_*,
\\]
and an order-one projection coefficient \\(|\\eta|\\in[0.3,3]\\), we record two manuscript-consistent candidates for \\(\\ell_*\\):

1. **Fiber-scale candidate (SC3 branch-screening scale):** \\(\\ell_*\\equiv r_{\\mathrm{fiber}}\\approx 50\\text{--}100\\,\\mu\\mathrm{m}\\) from §3.7.1.
   \\[
   R_{\\mathrm{transition}}\\approx \\sqrt{|\\eta|}\\,(50\\text{--}100\\,\\mu\\mathrm{m})
   \\approx 27\\text{--}173\\,\\mu\\mathrm{m}.
   \\]

2. **Localization-scale form (SC2 warp branch):** \\(\\ell_*\\equiv \\mu^{-1}\\), where \\(\\mu\\) is the localization/warp scale from §3.3.
   \\[
   R_{\\mathrm{transition}}\\approx \\sqrt{|\\eta|}\\,\\mu^{-1}.
   \\]
   This branch remains symbolic until \\(\\mu\\) is fixed by the same closure pass that finalizes SC2/SC3 compatibility.

**Provisional working value for immediate consistency checks:** adopting \\(|\\eta|\\sim1\\) and the SC3 fiber candidate gives
\\[
R_{\\mathrm{transition}}\\sim 50\\text{--}100\\,\\mu\\mathrm{m}\\quad\\text{(first-order, non-final)}.
\\]

## Bibliography entries for §§2–4
```bibtex
@article{RandallSundrum1999b,
  author  = {Randall, Lisa and Sundrum, Raman},
  title   = {An alternative to compactification},
  journal = {Physical Review Letters},
  volume  = {83},
  pages   = {4690--4693},
  year    = {1999},
  doi     = {10.1103/PhysRevLett.83.4690}
}

@article{McGaugh2016,
  author  = {McGaugh, Stacy S. and Lelli, Federico and Schombert, James M.},
  title   = {Radial acceleration relation in rotationally supported galaxies},
  journal = {Physical Review Letters},
  volume  = {117},
  pages   = {201101},
  year    = {2016},
  doi     = {10.1103/PhysRevLett.117.201101}
}

@article{Clowe2006,
  author  = {Clowe, Douglas and others},
  title   = {A direct empirical proof of the existence of dark matter},
  journal = {The Astrophysical Journal Letters},
  volume  = {648},
  pages   = {L109--L113},
  year    = {2006},
  doi     = {10.1086/508162}
}

@article{Planck2018,
  author  = {{Planck Collaboration}},
  title   = {Planck 2018 results. VI. Cosmological parameters},
  journal = {Astronomy \& Astrophysics},
  volume  = {641},
  pages   = {A6},
  year    = {2020},
  doi     = {10.1051/0004-6361/201833910}
}

@article{GoldbergerWise1999,
  author  = {Goldberger, Walter D. and Wise, Mark B.},
  title   = {Moduli stabilization with bulk fields},
  journal = {Physical Review Letters},
  volume  = {83},
  pages   = {4922--4925},
  year    = {1999},
  doi     = {10.1103/PhysRevLett.83.4922}
}
```
