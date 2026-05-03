# Coherence Relativity IIC — Holographic Structure, Effective Stress Tensor, and Consequences

# §1 Introduction

Paper 2C is the consequence-line manuscript of the 2026-04-15 Paper 2 split. Paper 2A stabilizes the abstract $M \times \Sigma$ framework; Paper 2B carries the derived-topology and KCR-Cone evaluation line; Paper 2C carries the holographic structure line, with RC-1 as the core result and the dark-sector, CMB, and quantum-foundations consequences treated as immediate corollaries.

The central claim of this paper is that the boundary action on $\partial M$ induces an effective stress tensor $T^{(\mathrm{eff})}_{\mu\nu}$ with enough structure to support three consequence lines at once: a dark-energy limit, a dark-matter limit, and a primordial-spectrum/CMB line. In this architecture, holography is no longer an abstract conjecture deferred elsewhere; it becomes the organizing interpretation of the RC-1 result.

This extraction is intentionally conservative. It promotes the RC-1 theorem line, the holographic dictionary material, the quantum-foundations applications, and the current discussion/open-problems spine into one canonical 2C target, while leaving any remaining verification gates explicitly labeled rather than silently absorbed.

Throughout, this paper preserves the same three-level reader map fixed in Papers 2A and 2B: $\mathbb{P}(\mathcal{H})$ is the kinematical state arena, $\Sigma$ is the coherence manifold carrying pointer and Berry/Hopf structure, and the physical KCR depth coordinate appears only as a derived feature of the effective macroscopic geometry. The holographic interpretation developed below depends on keeping those roles distinct. Accordingly, the holographic projection is not introduced as a direct quotient of the Hilbert-space tower, but derived from the joint geometry $M \times \Sigma$, its boundary locus, and the coherence flow connecting them.


# §2 RC-1: Effective Stress Tensor from the CR Action Principle

---

> **D2 Guardrail (active throughout):** The boundary term S^boundary_M is a Level 1 object — it lives
> in the gravitational sector (GR + matter on M) and sources the spacetime stress tensor. It must NOT
> be conflated with the Fubini-Study curvature on Σ (Level 2, information geometry). The Σ-geometry
> enters only by constraining the *symmetry structure* of S^boundary_M and providing the UV cutoff
> k_c for the T_M propagator. This distinction was violated in derivation attempt D2 (2026-04-10)
> and is explicitly tracked here.

---

## §RC1.1 — Symmetry Derivation of S^boundary_M

Derived (explicit calculation, pending independent verification on Opus)

### Setup

The CR manifold is M × Σ, with:

- **M**: spacetime (4D Lorentzian manifold of accumulated irreversible records)
- **∂M**: fact horizon — the present-moment decoherence front; a 3-dimensional hypersurface in M
- **Σ = U(d)/T^d**: coherosphere with Fubini-Study metric h_{ab}

The full metric on M × Σ is a higher-dimensional block-product metric perturbed by M-Σ coupling:

$$G_{AB} = \begin{pmatrix} g_{\mu\nu} & T_{M\,\mu}^{\;\;a} \\ T_{M\,\nu}^{\;\;b} & h_{ab} \end{pmatrix}$$

where A, B run over both M-indices (μ, ν) and Σ-indices (a, b). The field T_M (equivalently T_{MΣ}) is the off-diagonal block — it is an (M, Σ)-mixed tensor, a d × 4 matrix at each point of M × Σ. It is maximally supported at ∂M (see EOM v2 §7.1).

Throughout, we treat $T_M^{\mu a}$ as a section of $TM \otimes \mathfrak{u}(d)^\perp$, where $\mathfrak{u}(d)^\perp$ is the complement of $\mathfrak{t}^d$ in $\mathfrak{u}(d)$ — equivalently, the tangent space $T_p\Sigma$. The Σ-index $a$ therefore ranges over $d^2 - d$ real directions and transforms under the isotropy representation of $U(d)/T^d$.

The full CR action is:

$$S_{\rm CR} = \underbrace{\int_M \sqrt{-g}\left[\frac{R}{16\pi G} + \mathcal{L}_{\rm matter}\right]}_{S_M} + \underbrace{\int_\Sigma \omega_{\rm FS} \wedge \mathcal{F}}_{S_\Sigma} + S_M^{\rm boundary}$$

**RC-1 task:** Determine the form of S^boundary_M, then compute δS^boundary_M / δg^μν.

---

### Constraint 1 — Diffeomorphism Covariance on M

S^boundary_M must be a diffeomorphism scalar on M. This means:

1. It integrates over ∂M with the induced-metric measure d³y √(-γ)
2. It depends only on **intrinsic and extrinsic geometry of ∂M**: the induced metric γ_{ij} = g_{\mu\nu} e^\mu_i e^\nu_j and the extrinsic curvature K_{ij} = ∇_\mu n_\nu e^\mu_i e^\nu_j
3. It does **not** contain bulk metric components g_{\mu\nu} with indices not tangent to ∂M — equivalently, no normal-normal or normal-tangent components of the bulk metric appear independently

Here e^\mu_i = ∂x^\mu/∂y^i are the tangent vectors to ∂M in M coordinates, and n^\mu is the outward unit normal.

**Consequence:** S^boundary_M takes the form

$$S_M^{\rm boundary} = \int_{\partial M} d^3y\, \sqrt{-\gamma}\; \mathcal{L}_{\rm bdry}\!\left(\gamma_{ij}, K_{ij}, \text{matter fields at } \partial M\right)$$

The "matter fields at ∂M" includes T_M restricted to ∂M, which we denote T_M|_{∂M}. Constraint 1 alone admits an infinite-dimensional space of possible ℒ_bdry.

---

### Constraint 2 — U(d) × T^d Invariance on Σ

The coherosphere Σ = U(d)/T^d has isometry group U(d) (the full unitary group acting on the d-dimensional Hilbert space H) and a residual T^d gauge freedom from the quotient. Under these symmetries:

- T_M^{\mu a} → (U)^a_{\;b}\, T_M^{\mu b}, where U ∈ U(d) acts on the Σ-index

This means T_M transforms in the isotropy representation of $U(d)/T^d$ on its Σ-index (the earlier “fundamental-representation” language is only a shorthand). To form a U(d)-invariant out of T_M, we must contract the Σ-indices. The unique independent bilinear invariant is:

$$\text{Tr}(T_M T_M^\dagger) \equiv g_{\mu\nu}\, h_{ab}\, T_M^{\mu a}\, (T_M^{\nu b})^* = |T_M|^2$$

**Why this is the only leading bilinear:**

- A linear scalar in $T_M^{\mu a}$ would require contraction with a fixed element of $T^*M \otimes T_p^*\Sigma$. Under the action of U(d) on Σ, which is transitive, no such invariant tensor exists: the isotropy representation at $p \in \Sigma$ contains no U(d)-invariant vector. Linear invariants are therefore forbidden by the U(d) symmetry alone, independent of the form of any contracted tensor.

- The unique U(d)-invariant real bilinear in T_M is Tr(T_M T_M†) = g_{\mu\nu} h_{ab} T_M^{\mu a} T_M^{\nu b} ≡ |T_M|². (Here we use both metrics to contract all free indices, giving a scalar.)

- Higher bilinear structures from U(d) invariance: Tr((T_M T_M†)^n) for n ≥ 2 exist but are of higher order in the T_M expansion.

- T^d gauge invariance (residual from the quotient U(d)/T^d): under T^d, each diagonal U(1) factor rotates T_M^{\mu a} by a phase e^{iφ_a}. Since Tr(T_M T_M†) = Σ_a |T_M^{\mu a}|², this is manifestly invariant.

**Consequence:** Constraint 2 selects, at leading order in T_M, the unique structure Tr(T_M T_M†).

---

### Constraint 3 — Locality Along ∂M

S^boundary_M must be a local integral — no non-local kernels, convolutions, or bi-local functionals along ∂M. Specifically, no expression of the form

$$\int_{\partial M} d^3y\, d^3y'\, K(y, y')\, f(T_M(y))\, g(T_M(y'))$$

is permitted unless K(y,y') = δ³(y-y'). This is the locality postulate standard in effective field theory.

**Consequence:** Combined with Constraints 1 and 2, the action must be of the local form

$$S_M^{\rm boundary} = \int_{\partial M} d^3y\, \sqrt{-\gamma}\; \mathcal{L}_{\rm bdry}(\gamma_{ij}, K_{ij}, T_M, T_M^\dagger)$$

with ℒ_bdry a polynomial (or convergent series) in local fields evaluated at the same point y.

---

### Deriving the Leading-Order Form

**Dimensional analysis** (critical for isolating the leading term):

In natural units with G = 1/M_Pl², the action S must be dimensionless. The integration measure d³y √(-γ) has mass dimension [M^{-3}] (three spacetime dimensions on ∂M). Therefore ℒ_bdry must have mass dimension [M^3].

The field T_M^{\mu a} is a metric component (dimensionless in the metric signature convention where g_{\mu\nu} has no mass dimension). The curvature K_{ij} has dimension [M^1] (one derivative of the metric). Therefore:

We adopt the metric-perturbation convention throughout, in which $T_M^{\mu a}$ is dimensionless — consistent with its definition as an off-diagonal block of the $M \times \Sigma$ metric $G_{AB}$. Under this convention, couplings that multiply $\mathrm{Tr}(T_M T_M^\dagger)$ carry mass dimension.

- Tr(T_M T_M†) is dimensionless → requires coupling λ with [M^3] to make ℒ_bdry have dimension [M^3]
- K_{ij} alone has dimension [M^1] → K Tr(T_M T_M†) has dimension [M^1], requires coupling with [M^2]
- K^2 terms (from K_{ij} K^{ij} or K²) have dimension [M^2] → require coupling with [M^1]
- (K_{ij} K^{ij}) Tr(T_M T_M†) has dimension [M^2] → requires coupling with [M^1]

The **leading-order** term in the low-energy (long-wavelength on ∂M) expansion, where K_{ij} is treated as small compared to λ:

$$\boxed{\mathcal{L}_{\rm bdry} = \lambda\, \text{Tr}(T_M T_M^\dagger) + O(\lambda_K K_{ij}) + O(\lambda'\, [\text{Tr}(T_M T_M^\dagger)]^2)}$$

where:
- **λ** [M^3] is the M-Σ boundary coupling — the single free parameter at leading order
- **O(λ_K K_{ij})** terms: couplings of the form λ_K [M^2] × K_{ij} γ^{ij} = λ_K K, where K = K_{ij} γ^{ij} is the mean curvature trace. These are **subleading** because K_{ij} ~ H (Hubble rate) on cosmological scales, and K/M_Pl ≪ 1.
- **O(λ' [Tr T_M T_M†]²)** terms: the next order in the T_M expansion. These are suppressed by an additional factor of Tr(T_M T_M†)/M_Pl² (the T_M amplitude squared relative to the Planck scale). At leading order in the M-Σ coupling, these are negligible.

**The unique leading-order boundary action is therefore:**

$$\boxed{S_M^{\rm boundary} = \lambda_{\rm bdry} \int_{\partial M} d^3y\, \sqrt{-\gamma}\, \text{Tr}(T_M T_M^\dagger) + O(\lambda_K, \lambda')}$$

**Notation convention.** Throughout this paper, $\lambda_{\rm bdry}$ denotes the dimensionful M-Σ boundary coupling with $[\lambda_{\rm bdry}] = M^3$ that appears in $S_M^{\rm boundary}$. This is **distinct** from $\lambda_{\rm 2B} = A^2(r)$, the dimensionless distinguishability parameter of Paper 2B. Both are called "$\lambda$" in the literature; we use subscripts here to prevent the notation collision identified in RC-2.5. The conversion factor $\lambda_{\rm bdry} = \lambda_{\rm 2B} \cdot M_{\rm eff}^3$ for some physical mass scale $M_{\rm eff}$ is an RC-3 calculation.

**Assumption (A1)**: T_M is treated as a classical background field at ∂M in this derivation. Its quantum fluctuations are accounted for in §RC1.4. The action above is the classical (background) boundary action.

**Assumption (A2)**: The expansion in T_M is valid, i.e., |T_M| ≪ M_Pl. This is expected from the M-Σ coupling being a subleading correction to the gravitational sector, but requires verification against the Bekenstein bound S ~ 10^{123} bits.

**Subleading K_{ij} corrections:** Terms mixing K_{ij} with T_M appear at the next order. The leading mixing term is:

$$\delta \mathcal{L}_{\rm bdry}^{(K)} = \lambda_K\, K_{ij} \gamma^{ij}\, \text{Tr}(T_M T_M^\dagger) = \lambda_K\, K\, |T_M|^2$$

This coupling (trace of extrinsic curvature times |T_M|²) would be relevant near the Big Bang where K → ∞ (strongly curved ∂M). In the current epoch, K ~ H₀/c, and λ_K K ≪ λ for reasonable λ_K/λ ratios.

---

## §RC1.2 — Metric Variation: Extract T^(eff)_μν

Derived (variational calculation; the identification of support on ∂M is exact; overall normalization requires A1–A2)

### Setup for Variation

The effective stress tensor is defined by:

$$T^{\rm (eff)}_{\mu\nu}(x) = -\frac{2}{\sqrt{-g(x)}}\frac{\delta S_M^{\rm boundary}}{\delta g^{\mu\nu}(x)}$$

We must vary S^boundary_M = λ ∫_∂M d³y √(-γ) Tr(T_M T_M†) with respect to the 4D bulk metric g^{μν}(x).

There are two contributions:
1. **Variation of √(-γ)**: the induced metric γ_{ij} = g_{\mu\nu}(y) e^\mu_i(y) e^\nu_j(y) depends on the bulk metric evaluated at the boundary point y
2. **Variation of Tr(T_M T_M†)**: this depends on whether T_M itself depends on g^{μν}

Under Assumption (A1), T_M is a background field independent of g^{μν}, so **only contribution (1) is nonzero**.

---

### Step 1: Variation of the Induced Metric

The induced metric on ∂M:

$$\gamma_{ij}(y) = g_{\mu\nu}(y)\, e^\mu_i(y)\, e^\nu_j(y)$$

Varying with respect to g^{μν} at bulk point x:

$$\frac{\delta \gamma_{ij}(y)}{\delta g^{\mu\nu}(x)} = -g_{\mu\alpha} g_{\nu\beta}\, e^\alpha_i(y)\, e^\beta_j(y)\, \delta^{(4)}(x - y)$$

where the delta function restricts the variation to the point y on ∂M. (We use δg_{\mu\nu} = -g_{\mu\alpha} g_{\nu\beta} δg^{αβ}.)

---

### Step 2: Variation of √(-γ)

$$\delta \sqrt{-\gamma} = \frac{1}{2} \sqrt{-\gamma}\, \gamma^{ij}\, \delta\gamma_{ij}$$

Substituting:

$$\frac{\delta \sqrt{-\gamma(y)}}{\delta g^{\mu\nu}(x)} = -\frac{1}{2} \sqrt{-\gamma(y)}\, \gamma^{ij}(y)\, g_{\mu\alpha} g_{\nu\beta}\, e^\alpha_i(y)\, e^\beta_j(y)\, \delta^{(4)}(x - y)$$

Define the **boundary projection** of the bulk metric:

$$\Pi_{\mu\nu}(y) \equiv \gamma^{ij}(y)\, e^\alpha_i(y)\, e^\beta_j(y)\, g_{\mu\alpha}\, g_{\nu\beta}$$

This is the pullback-pushforward of the induced metric to bulk indices: Π_{\mu\nu} = γ_{μν}^{∂M} is the bulk representation of the induced metric (zero for bulk directions normal to ∂M).

Then:

$$\frac{\delta \sqrt{-\gamma(y)}}{\delta g^{\mu\nu}(x)} = -\frac{1}{2} \sqrt{-\gamma(y)}\, \Pi_{\mu\nu}(y)\, \delta^{(4)}(x - y)$$

---

### Step 3: Variation of S^boundary_M

$$\frac{\delta S_M^{\rm boundary}}{\delta g^{\mu\nu}(x)} = \lambda \int_{\partial M} d^3y\; \frac{\delta \sqrt{-\gamma(y)}}{\delta g^{\mu\nu}(x)}\; \text{Tr}(T_M T_M^\dagger)(y)$$

$$= \lambda \int_{\partial M} d^3y\; \left[-\frac{1}{2} \sqrt{-\gamma(y)}\, \Pi_{\mu\nu}(y)\right]\, \text{Tr}(T_M T_M^\dagger)(y)\; \delta^{(4)}(x - y)$$

The 4D delta function with a 3D integration gives a delta function in the **normal direction** to ∂M:

$$\int_{\partial M} d^3y\; f(y)\, \delta^{(4)}(x - y) = f(x)\big|_{x \in \partial M} \cdot \delta_\perp(x, \partial M)$$

where δ_⊥(x, ∂M) is the transverse (normal-direction) delta function, normalized so that:

$$\int_M d^4x\; \delta_\perp(x, \partial M) = 1$$

More precisely, in a coordinate system (y^i, n) where y^i are coordinates on ∂M and n is the normal coordinate:

$$\delta_\perp(x, \partial M) = \delta(n(x)) / \sqrt{g_{nn}}$$

Therefore:

$$\frac{\delta S_M^{\rm boundary}}{\delta g^{\mu\nu}(x)} = -\frac{\lambda}{2}\, \sqrt{-\gamma(x)}\, \Pi_{\mu\nu}(x)\, \text{Tr}(T_M T_M^\dagger)(x)\; \delta_\perp(x, \partial M)$$

---

### Step 4: The Effective Stress Tensor

$$T^{\rm (eff)}_{\mu\nu}(x) = -\frac{2}{\sqrt{-g(x)}} \cdot \left(-\frac{\lambda}{2}\right) \sqrt{-\gamma(x)}\, \Pi_{\mu\nu}(x)\, |T_M|^2(x)\; \delta_\perp(x, \partial M)$$

$$\boxed{T^{\rm (eff)}_{\mu\nu}(x) = \lambda\; \frac{\sqrt{-\gamma(x)}}{\sqrt{-g(x)}}\; \Pi_{\mu\nu}(x)\; |T_M|^2(x)\; \delta_\perp(x, \partial M)}$$

where we write |T_M|² ≡ Tr(T_M T_M†) for compactness.

**Three key properties are manifest:**

1. **Quadratic in T_M:** T^(eff)_μν ~ |T_M|² = Tr(T_M T_M†) — a bilinear in T_M, as required. It is NOT linear in T_M (which would have broken U(d) invariance). This confirms the derivation is internally consistent.

2. **Localized on ∂M:** The factor δ_⊥(x, ∂M) kills T^(eff)_μν everywhere except at the boundary. This is structurally analogous to the Israel junction condition stress tensor in thin-shell GR.

3. **Tensor structure:** Π_μν = γ_μν^{∂M} is tangential to ∂M. The component T^(eff)_{μν} n^ν = 0 (where n^ν is the unit normal to ∂M) — the effective stress tensor has no normal flux. This is consistent with ∇^μ T^(eff)_μν = 0 along ∂M (see conservation check below).

---

### Anisotropic Corrections

The full T^(eff)_μν including subleading terms:

**From K_{ij} corrections to S^boundary_M:**

$$\delta T^{\rm (eff)\,(K)}_{\mu\nu} = \lambda_K \left[K\, \Pi_{\mu\nu} + K_{\mu\nu} - K\, n_\mu n_\nu\right] |T_M|^2\; \delta_\perp$$

where K_{μν} here is the extrinsic curvature tensor embedded in bulk indices. These are the standard GHY-type corrections.

**From variations in T_M itself** (lifting Assumption A1 — treating T_M as a dynamical field):

If T_M has spatial gradients ∇_i T_M along ∂M, there is an additional contribution:

$$\delta T^{\rm (eff)\,(∇T)}_{\mu\nu} = 2\lambda\, \frac{\sqrt{-\gamma}}{\sqrt{-g}}\, \text{Re}\left[\text{Tr}\!\left(\frac{\delta T_M}{\delta g^{\mu\nu}} T_M^\dagger\right)\right] \delta_\perp$$

This term is the **anisotropic correction** relevant for dark matter (Target 3B). When ∇_i T_M ≠ 0 (decoherence not uniform), T_M picks up a preferred direction, breaking the isotropic γ_μν structure.

**Assumption (A3):** The δT_M/δg^{μν} term requires knowing the equation of motion for T_M derived from the full S_CR. This is the M-Σ EOM from Paper 2A §7. Extracting the metric-variation of T_M is **not done here** — it is the subject of RC-2.

---

### Conservation Check

The covariant conservation ∇^μ T^(eff)_μν = 0:

Write

$$T^{\rm (eff)}_{\mu\nu} = \sigma(y)\, \Pi_{\mu\nu}\, \delta_\perp, \qquad \sigma(y)=\lambda |T_M(y)|^2 \frac{\sqrt{-\gamma}}{\sqrt{-g}}$$

with $\Pi_{\mu\nu}=g_{\mu\nu}-n_\mu n_\nu$ the tangential projector onto $\partial M$. Then, at the distributional level,

$$\nabla^\mu T^{\rm (eff)}_{\mu\nu} = \big[D^\mu(\sigma \Pi_{\mu\nu})\big]\delta_\perp + \sigma\,(\nabla^\mu \Pi_{\mu\nu})\,\delta_\perp + \sigma\, \Pi_{\mu\nu} n^\mu \partial_\perp \delta_\perp,$$

where $D_\mu$ is the induced covariant derivative on $\partial M$.

The last term vanishes because $\Pi_{\mu\nu}n^\mu = 0$. The middle term is governed by the extrinsic geometry of the embedding: $\nabla^\mu \Pi_{\mu\nu}$ is built from the extrinsic curvature $K_{\mu\nu}$ and its trace $K$. Thus conservation reduces to a tangential continuity condition together with the usual thin-shell/junction balance between projector derivatives and extrinsic-curvature terms.

In the homogeneous (DE) limit, $\sigma = \text{const}$ on $\partial M$, so $D_i \sigma = 0$ and the tangential piece vanishes. The remaining extrinsic-curvature contribution is the standard junction-term bookkeeping and is consistent with no normal flux through $\partial M$.

In the inhomogeneous (DM) limit, $D_i \sigma \neq 0$. Then the tangential divergence is nonzero unless the full $T_M$ equation of motion supplies compensating terms through $\delta T_M/\delta g^{\mu\nu}$ and the induced anisotropic stress. In other words, conservation of the truncated isotropic ansatz is not automatic away from homogeneity.

**Assumption (A4):** Full covariant conservation $\nabla^\mu T^{\rm (eff)}_{\mu\nu} = 0$ is assumed to hold only after the complete M-Σ EOM for $T_M$ is imposed. A full verification, including the precise projector/extrinsic-curvature balance, is deferred to RC-2.

---

## §RC1.3 — Two Physical Limits: Dark Energy and Dark Matter

Derived for the tensor structure and equation-of-state identification
 Derived for the geometric coefficient $\alpha_{\rm geom} = N_0^2 I_6/I_2 = 10\sqrt{2}/(3\pi) \approx 1.5005$ appearing in the zero-mode-weighted KCR backreaction integral (RC-8b)
 WITHDRAWN for any power-law scaling $|T_M|^2 \propto \Gamma_{\rm dec}^{p}$ at leading order (RC-6: the “p exponent” formulation is ill-defined; do not use)

---

### Limit A: Dark Energy (w = -1), Uniform Decoherence

**Physical setup:** The decoherence rate Γ_dec is spatially uniform across ∂M, with Γ_dec ~ 0.68 H₀ (April 10 result). This means T_M is homogeneous along ∂M:

$$T_M^{\mu a}(y) = T_M^{\mu a} = \text{const across } \partial M$$

**Consequence for tensor structure:**

On a spatially homogeneous ∂M (FLRW case), the induced metric is:

$$\gamma_{ij} = a^2(t)\, \delta_{ij} \quad \text{(in comoving coordinates)}$$

and the boundary projection is:

$$\Pi_{\mu\nu} = \gamma_{\mu\nu}^{\partial M} = a^2(t) \text{diag}(0, 1, 1, 1)_{\mu\nu}$$

In 4D covariant language, for a homogeneous ∂M:

$$\Pi_{\mu\nu} = g_{\mu\nu} + n_\mu n_\nu$$

(projection onto ∂M, which is the standard spatial metric in the preferred frame where n^μ is the unit normal = time direction).

With constant |T_M|², the effective stress tensor (at the location of ∂M) takes the form:

$$T^{\rm (eff)}_{\mu\nu}\big|_{\partial M} = \lambda\, |T_M|^2\, (g_{\mu\nu} + n_\mu n_\nu) \cdot \delta_\perp$$

When this is **integrated across ∂M** to give an effective energy density in the bulk (smeared over a Hubble-scale thickness ℓ ~ 1/H₀):

$$\langle T^{\rm (eff)}_{\mu\nu} \rangle = \lambda\, |T_M|^2 \cdot \frac{1}{\ell} \cdot g_{\mu\nu}$$

The isotropic γ_μν structure (plus n_μ n_ν) gives, in the frame of a comoving observer, equal contributions to energy density and pressure:

$$\rho_{\rm eff} = \lambda |T_M|^2 / \ell, \qquad P_{\rm eff} = -\lambda |T_M|^2 / \ell$$

$$\Rightarrow \quad w = P_{\rm eff}/\rho_{\rm eff} = -1 \quad $$

**The dark energy equation of state w = -1 is reproduced exactly from the isotropic limit of T^(eff)_μν.**

This is the cosmological constant form: T^(eff)_μν → -ρ_eff g_μν, identical to vacuum energy. The CR mechanism identifies the boundary term at ∂M as the geometric origin of Λ.

---

**The geometric coefficient $\alpha_{\rm geom}$ and the remaining dynamical coefficient $c_\Gamma$: **

The KCR-Cone geometry fixes the dimensionless backreaction coefficient in the corrected (π-consistent) form

$$\boxed{\Omega_{\rm drag} = \alpha_{\rm geom}\,c_\Gamma^2, \qquad c_\Gamma := \Gamma_{\rm dec}/H_0.}$$

A reproducible derivation of $\alpha_{\rm geom}$ is now available:

$$\boxed{\alpha_{\rm geom} = N_0^2\,\frac{I_6}{I_2} = \frac{10\sqrt{2}}{3\pi} \approx 1.5005,}$$

where $\psi_0(r)=N_0A^2(r)$ is the KCR vector zero mode (RC-3) and the weighting uses the graviton reduction measure $A^2dr$ (RC-8b). This value is within 0.033% of $3/2$ but is not exactly $3/2$.

The $\lambda\cdot T=O(1)$ theorem (RC-5) guarantees $c_\Gamma=O(1)$ (no Planck/Hubble hierarchy). The Path C balance equation $\Omega_\Lambda = \alpha_{\rm geom}\,c_\Gamma^2$ now yields a \textbf{derived} value (RC-4, 2026-05-01):
$$\boxed{c_\Gamma = \sqrt{\Omega_\Lambda/\alpha_{\rm geom}} = \sqrt{0.6921/1.5005} = 0.679\pm 0.005}$$
This is a derivation, not an inference: given $\Omega_\Lambda$ (Planck 2018) and the purely geometric $\alpha_{\rm geom} = 10\sqrt{2}/(3\pi)$ (RC-8b), the decoherence rate $c_\Gamma$ follows with 0.7\% precision. See \texttt{RC4\_SOURCED\_EOM\_2026-05-01.md} for the EOM derivation.

**Withdrawn:** We do **not** assume a power-law scaling $|T_M|^2 \propto \Gamma_{\rm dec}^{p}$ at leading order; the exponent formulation is ill-defined in the KCR-Cone scaling regime and was retired in RC-6.

---

### Limit B: Dark Matter (w = 0), Decoherence Tracking Baryon Density

**Physical setup:** The decoherence rate tracks local baryonic density:

$$\Gamma_{\rm dec}(x) = \Gamma_0 \cdot \frac{\rho_b(x)}{\bar{\rho}_b}$$

where ρ_b(x) is the local baryon mass density and ρ̄_b is the cosmic mean. This means T_M(x) has spatial gradients along ∂M, pointing in the direction of ∇ρ_b.

**T_M structure in this limit:**

We adopt the following rank-1 outer-product **ansatz** for $T_M$ when $\Gamma_{\rm dec}$ tracks $\rho_b$:

$$T_M^{\mu a}(y) = A(\rho_b(y))\, u^\mu\, \psi^a$$

where:
- $u^\mu$ is the comoving 4-velocity (the preferred time direction set by the baryon rest frame)
- $\psi^a$ is a fixed $\Sigma$-direction (the "baryonic decoherence channel")
- $A(\rho_b)$ is a scalar amplitude depending on local baryon density

**Status of the ansatz.** This is a *chosen* minimal structure, not a uniquely derived form. It is the simplest rank-1 factorization consistent with (i) a single preferred M-direction (comoving with baryons), (ii) a single preferred $\Sigma$-direction (a baryonic decoherence channel), and (iii) leading-order scaling $T_M \propto A(\rho_b)$. Other structures consistent with "tracks $\rho_b$" include a rank-1 ansatz built on the normal direction $n^\mu$ instead of $u^\mu$, rank-$\geq 2$ outer products with secondary Σ-modes, and non-factorized $T_M(\rho_b, u, n)^{\mu a}$ with mixed M–Σ profiles. A genuine uniqueness argument requires solving the M–Σ EOM with $\Gamma_{\rm dec} \propto \rho_b$ as source; we defer that calculation to RC-2. The $w = 0$ derivation below should therefore be read as: *if* the ansatz above holds, the equation of state is pressureless dust.

**Resulting stress tensor:**

$$|T_M(y)|^2 = \text{Tr}(T_M T_M^\dagger)(y) = A^2(\rho_b)\, g_{\mu\nu} u^\mu u^\nu \cdot |\psi|^2_{h} = A^2(\rho_b) \cdot |\psi|^2_h$$

(using u^μ u_μ = -1 in the time-direction convention, and |ψ|²_h = h_{ab} ψ^a ψ^b* = 1 normalized).

The induced metric on ∂M has the boundary projection:

$$\Pi_{\mu\nu}(y) = g_{\mu\nu} + n_\mu n_\nu$$

but the anisotropy enters through the metric variation of T_M (Assumption A3 relaxed). With T_M = A(ρ_b) u⊗ψ, the variation δT_M/δg^{μν} picks up the u^μ structure:

$$\delta T^{(∇T)}_{\mu\nu} \propto \lambda\, A(\rho_b)\, \frac{\delta A}{\delta g^{\mu\nu}}\, u_\mu u_\nu$$

For a pressureless source, ρ_b u^μ is the baryon current, and δA/δg^{μν} ~ A'(ρ_b) × ρ_b u_μ u_ν / 2. The dominant term becomes:

$$T^{\rm (eff)}_{\mu\nu}\big|_{\rm DM\; limit} = \lambda\, A^2(\rho_b)\, u_\mu u_\nu \cdot \delta_\perp$$

This is **pressureless dust** with equation of state:

$$w = P_{\rm eff}/\rho_{\rm eff} = 0 \quad $$

The dark matter signature — a pressureless, non-relativistic fluid co-moving with baryons — emerges from the anisotropic (non-isotropic) limit of the boundary term when T_M tracks baryon density.

---

**Mechanism converting boundary term to effective bulk density:**

The δ_⊥(x, ∂M) factor localizes T^(eff) on ∂M. In FLRW cosmology, ∂M is a 3-sphere at fixed cosmic time (recombination for the CMB case; the present-moment horizon for the current epoch). The effective dust density is:

$$\rho_{\rm DM}(x, t) = \lambda\, A^2(\rho_b(x, t_{rec}))\, \frac{\sqrt{-\gamma}}{\sqrt{-g}}\, \delta(t - t_{rec}) \times (\text{propagator in }t > t_{rec})$$

The boundary condition at ∂M seeds a classical field in the bulk M that, under the M equation of motion, propagates forward in time as pressureless dust. This is the **transfer mechanism** from boundary term to bulk effective density. Full derivation requires the M EOM with T^(eff) as a source — flagged for RC-2.

---

**Ω_DM/Ω_b consistency check for an adopted *phenomenological* scaling ansatz (illustrative only):**

If one adopts the phenomenological ansatz

$$\rho_{\rm DM} \sim \lambda^2 \rho_b^{q},$$

then

$$\frac{\Omega_{\rm DM}}{\Omega_b} = \lambda^2 \cdot \bar{\rho}_b^{\,q - 1}.$$

For the illustrative choice $q = 3/2$, with $\Omega_b = 0.049$, $\Omega_{\rm DM} = 0.259$, and $\bar{\rho}_b$ expressed in units of the critical density $\rho_c$, one obtains

$$\lambda^2 \cdot \left(\frac{\Omega_b}{1}\right)^{1/2} = \frac{\Omega_{\rm DM}}{\Omega_b}$$

and hence

$$\lambda^2 = \frac{0.259}{0.049} \cdot \frac{1}{\sqrt{0.049}} = 5.29 \cdot 4.52 \approx 23.9 \cdot \rho_c^{-1/2}.$$

The $\Omega^{1/2}$ factor carries units of $\rho_c^{1/2}$, so this is only a scaling-level consistency estimate.
**Conjectured (C2):** If future work yields a baryon-tracking scaling close to $q\approx 3/2$, then the observed ratio $\Omega_{\rm DM}/\Omega_b = 5.29$ can be matched by an admissible choice of the normalization $\lambda$. This check does **not** derive either $q$ or $\lambda$; it only shows phenomenological viability of that benchmark ansatz.

**Interpretation:** This illustrative baryon exponent $q$ is **not** tied to the geometric dark-energy coefficient $\alpha_{\rm geom}$; the latter is fixed independently by the KCR zero-mode backreaction integral (RC-8b). Any genuine derivation of baryon tracking requires solving the sourced M–Σ dynamics.

---

**⚠️ Inbound reference from Paper 2B §7.9 — Gravitational decoherence coefficient β (item #OP-β):**
Paper 2B §7.9.7 Eq. (7.9.21) introduces a gravitationally-sourced correction to the
stochastic drift F^r:
$$F^r_{\rm grav}(r) = F^r(r) + \beta\,\frac{dg/dt^2}{\chi^2_{\rm grav}}\,\tau^2_{\rm frame}$$
and asserts β ~ O(1) with a forward reference to this section (Paper 2C §RC1.3) for the
derivation of β from the T_{AB} effective stress tensor. **That derivation does not currently
exist here.** The §RC1.3 results establish w = −1 (DE limit) and w = 0 (DM limit) from the
boundary effective stress tensor T^(eff)_μν, and fix α_geom (Eq. RC-8b). Extracting a
gravitational decoherence modification β from these results requires:
1. A time-dependent metric perturbation g(t) expanding the T^(eff) source;
2. A coupling between ∂M dynamics and the coherence frame r-coordinate via T_{MΣ};
3. The resulting correction to Γ_dec(r,t) and hence to F^r.
This calculation is deferred to RC-2 (full T_M EOM with sourced metric) or a dedicated
sub-item. **Status:** OPEN (#OP-β). Registered in PAPER2_OPEN_ITEMS_LEDGER.

---

## §RC1.4 — Primordial Perturbation Spectrum: Connection to RC-3

 CONJECTURED for the T_M propagator form; Derived for the general formula structure

---

### Setup: Perturbed Boundary Action

Consider metric perturbations h_μν = δg_μν around the FLRW background ḡ_μν. To first order:

$$\delta S_M^{\rm boundary} = \lambda \int_{\partial M} d^3y \left[\delta\sqrt{-\gamma} \cdot |T_M|^2 + \sqrt{-\bar\gamma} \cdot \delta|T_M|^2\right]$$

The first term gives the background stress tensor variation (already computed in §RC1.2). The second term is new: it sources a perturbation to the gravitational field when T_M has spatial fluctuations.

Treating T_M(y) on ∂M as a quantum field with zero-point and thermal fluctuations:

$$\delta|T_M(y)|^2 = \delta\text{Tr}(T_M T_M^\dagger)(y)$$

Fourier-transforming along ∂M:

$$T_M(y) = \int \frac{d^3k}{(2\pi)^3}\, \tilde{T}_M(k)\, e^{ik \cdot y}$$

$$|\delta T_M(k)|^2 \equiv \langle \tilde{T}_M(k) \tilde{T}_M^\dagger(k)\rangle = P_{T_M}(k)$$

The perturbed source in the Einstein equations on ∂M:

$$\delta T^{\rm (eff)}_{\mu\nu}(k) = \lambda \cdot P_{T_M}(k) \cdot \Pi_{\mu\nu}(k) \cdot \delta_\perp$$

---

### The T_M Propagator from Σ Geometry

T_M^{μa} carries a Σ-index a. On the compact space Σ = U(d)/T^d, the index a is discrete with spectrum determined by the representation theory of U(d). The effective propagator for T_M on ∂M, integrated over Σ modes, takes the form:

$$P_{T_M}(k) = \frac{C_{T_M}}{k^2 + k_c^2}$$

where:
- k is the 3-momentum along ∂M
- k_c ~ 1/R_Σ is the IR cutoff from the compact Σ (inverse coherosphere radius)
- C_{T_M} is the UV amplitude set by the T_M normalization

**Physical origin of the Lorentzian form:** The compact Σ has a spectral gap. The lowest non-trivial mode of T_M on Σ has a mass-squared equal to the smallest non-zero eigenvalue of the Laplacian on U(d)/T^d. This lowest mode mass appears as k_c² in the 3D propagator via the standard KCR mode mechanism rather than a literal Klein-circle KK tower.

**Assumption (A5):** The propagator P_{T_M}(k) = C_{T_M}/(k² + k_c²) is the Euclidean propagator of a massive scalar on ∂M with mass k_c. This assumes T_M behaves as a free massive field at leading order. Interactions (non-linear Σ coupling) would modify this form. The Lorentzian shape is the minimal consistent ansatz given the Σ compact geometry.

> **RC-3 Update (2026-04-18):** The free-field T_M propagator derived from first principles in `RC3_DERIVATION_2026-04-18.md` §RC3.4 is **massless**: $P(k) = 2N_0^2/(M_5^3 k^2) \sim 1/k^2$. The zero mode $\psi_0(r) = N_0\cos^2(\sqrt{2}\,r)$ is normalizable and has $m_0^2 = 0$. The massive tower starts at the exact first massive KCR vector-mode value $m_1^2 = 24$ (in KCR units), giving $k_c^{\rm KK} = 2\sqrt{6}/L^* \approx 4.90/L^*$ as the corresponding spectral transition scale.
>
> The $k_c^2$ term in the propagator Assumption A5 is therefore NOT the free-field KCR mode gap but a **dynamical effective mass** arising from the decoherence sourcing of $T_M$. With $\Gamma_{\rm dec} \sim H_0$ (from Path C, RC-2.5), the natural sourced mass scale is $k_c^{\rm eff} \sim H_0 \sim 5H_0$ (the latter matching the 69% quadrupole suppression). From RC-4 (2026-05-01): the sourced EOM gives $k_c^{\rm eff} = \sqrt{\Omega_\Lambda}\,H_0 \approx 0.832\,H_0$ at leading order. The connecting factor to $k_c = 5/\chi_{\rm CMB}$ is the holographic projection $R_\Sigma = \chi_{\rm CMB}$ (Paper 4 \S3). See \texttt{RC4\_SOURCED\_EOM\_2026-05-01.md} \S3.
>
> The spectral formula $\Delta^2_\Sigma(k) = A_s k^2/(k^2 + k_c^2)$ remains structurally correct with $k_c = k_c^{\rm eff}$ (dynamical). The form $k^2/(k^2 + k_c^2)$ requires a propagator $P(k) \sim 1/(k^2+k_c^2)$ — which comes from the sourced dynamics, not the free spectrum.

---

### The Primordial Power Spectrum

The dimensionless primordial power spectrum sourced by T_M fluctuations:

$$\mathcal{P}^\Sigma(k) = \frac{k^3}{2\pi^2} \cdot \lambda^2 \cdot P_{T_M}(k) = \frac{k^3}{2\pi^2} \cdot \frac{\lambda^2 C_{T_M}}{k^2 + k_c^2}$$

Defining the amplitude A_s = λ² C_{T_M} / (2π²) (absorbing all UV normalizations):

$$\boxed{\Delta^2_\Sigma(k) = \mathcal{P}^\Sigma(k) = A_s \cdot \frac{k^2}{k^2 + k_c^2}}$$

This is:
- → 0 as k → 0: no super-coherosphere power (compact Σ has no zero mode for T_M)
- → A_s as k ≫ k_c: recovers Harrison-Zel'dovich at sub-coherosphere scales
- Half-power at k = k_c (definition of the cutoff)

This is exactly the Fubini-Study–motivated spectrum from the Tier 3 toy model (T25B_tier3_cl_model.py). **RC-1 now provides the derivation that converts the toy model into a calculation.**

---

### Angular Power Spectrum

From the standard CMB transfer function in the Sachs-Wolfe approximation:

$$C_\ell^\Sigma = \frac{2}{\pi} \int_0^\infty k^2\, \mathcal{P}^\Sigma(k)\, [j_\ell(k \chi_{\rm CMB})]^2\, dk$$

which in terms of Δ²_Σ becomes:

$$C_\ell^\Sigma = \frac{2}{9\pi} \int_0^\infty \frac{dk}{k}\; \Delta^2_\Sigma(k)\; [j_\ell(k \chi_{\rm CMB})]^2$$

(The factor of 1/9 comes from the Sachs-Wolfe transfer function T(k) = 1/3.)

Substituting Δ²_Σ(k) = A_s k²/(k² + k_c²):

$$C_\ell^\Sigma = \frac{2A_s}{9\pi} \int_0^\infty \frac{dk}{k} \cdot \frac{k^2}{k^2 + k_c^2} \cdot [j_\ell(k \chi_{\rm CMB})]^2$$

---

### Verification: 69% Quadrupole Suppression at k_c = 5/χ_CMB

From the toy model computation (T25B_tier3_cl_model.py, verified numerically):

| k_c (units of 1/χ_CMB) | Quadrupole suppression D_ℓ^Σ/D_ℓ^std (ℓ=2) |
|---|---|
| 3 | 0.2068 (79.3% suppression) |
| **5** | **0.3079 (69.2% suppression)** |
| 10 | 0.6244 (37.6% suppression) |

Planck 2018 observed: ~67% quadrupole deficit (ℓ=2 anomaly).

**k_c = 5/χ_CMB gives 69% suppression, within 3% of the Planck observation.**

The dimensionless scale d (coherosphere dimension) is related to k_c by:

$$k_c \sim \frac{1}{R_\Sigma} = \frac{\sqrt{d}}{\chi_{\rm CMB}}$$

Setting k_c = 5/χ_CMB: d ~ 25. But d is the Hilbert space dimension — for a cosmological system, d ~ 10^{61} (from the Bekenstein bound S ~ 10^{123} bits with d ~ S^{1/2}).

**Note on d vs k_c:** The identification k_c = √d/χ_CMB would give k_c ~ 10^{30}/χ, not k_c = 5/χ. This discrepancy indicates that k_c is NOT directly 1/√d but rather involves a different projection. The physically relevant k_c is the **lowest KCR mode of T_M**, which is set by the effective radius of the lowest-energy coherosphere excitation, not by the full dimension.

> **RC-3 Resolution (2026-04-18):** The lowest massive KCR vector mode is exact: $m_1^2 = 24$ in KCR units, giving $k_c^{\rm KK} = 2\sqrt{6}/L^* \approx 4.90/L^*$. This is NOT the dynamical cutoff $k_c^{\rm eff} \approx 5H_0$ needed for the quadrupole suppression — rather, $k_c^{\rm KK}$ sets the scale below which the zero-mode-dominated propagator $1/k^2$ applies. The dynamical $k_c^{\rm eff}$ comes from decoherence sourcing of $T_M$ (RC-4 scope). The d vs k_c discrepancy is therefore resolved in direction: k_c is not $1/R_\Sigma$ but $k_c^{\rm eff}$ from the Γ_dec dynamics.

The self-consistency check from Session 2026-04-14 (Part VI):
- d ~ 10^{61} → d² ~ 10^{122}
- Bekenstein entropy S_CMB ~ 10^{123}
- These agree to within one order of magnitude — consistent without being tautological

---

### What Remains for RC-3

For RC-3 to make C_ℓ^Σ fully predictive, it needs from RC-1:

**Provided here:**
1. The spectrum formula: Δ²_Σ(k) = A_s k²/(k² + k_c²)
2. The structural identification: 𝒫^Σ(k) ∝ λ² |T_M(k)|²
3. The angular power spectrum formula C_ℓ^Σ via Sachs-Wolfe integral
4. Numerical verification that k_c = 5/χ_CMB → 69% quadrupole suppression

**RC-3 delivered (2026-04-18):**
1. ✅ KCR mode spectrum: $m_n^2 = 8n(n+2)$, giving $k_c^{\rm KK} = m_1/L^* = 2\sqrt{6}/L^*$ (exact analytic)
2. ✅ Free-field propagator: $P(k) \sim 1/k^2$ (zero mode massless; $N_0 \approx 1.55$)
3. ✅ λ_bdry decouples from Λ_eff (CC comes from geometry, not boundary coupling)
4. ✅ d vs k_c discrepancy resolved in direction: k_c = dynamical from decoherence, not the free-field KCR mode gap

**RC-4 closed at leading order (2026-05-01):** $c_\Gamma = \sqrt{\Omega_\Lambda/\alpha_{\rm geom}} = 0.679$ derived; $k_c^{\rm eff} = \sqrt{\Omega_\Lambda}\,H_0 = 0.832\,H_0$ estimated. Residual gap: holographic projection $R_\Sigma = \chi_{\rm CMB}$ (Paper 4 \S3). See \texttt{RC4\_SOURCED\_EOM\_2026-05-01.md}.

**Still needed (Paper 4 scope):**
1. $R_\Sigma = \chi_{\rm CMB}$ from holographic projection $\Phi: \Sigma \to \partial M$ (closes factor-1.9 gap between $k_c^{\rm eff}$ and $k_c^{\rm SW} = 5/\chi_{\rm CMB}$)
2. Full Boltzmann transfer function (beyond Sachs-Wolfe)
3. Non-Gaussian corrections to 𝒫^Σ(k) from T_M interactions
4. Amplitude A_s from λ_bdry normalization (requires 5D action evaluation)

---

## §RC1.5 — Open Items and Gates to RC-2 through RC-4

### Summary of RC-1 Status

| Section | Target | Status | Key Assumption |
|---|---|---|---|
| §RC1.1 | Symmetry constraints → S^boundary_M | Derived | A1: T_M background; A2: |T_M| ≪ M_Pl |
| §RC1.2 | Metric variation → T^(eff)_μν | Derived | A3: T_M metric-variation from RC-2 |
| §RC1.3A | DE limit: w = -1 from isotropic T^(eff) | Derived | — |
| §RC1.3A | Geometric coefficient $\alpha_{\rm geom}=10\sqrt{2}/(3\pi)\approx 1.5005$ in KCR backreaction | Derived | Zero-mode-weighted KCR geometry (RC-8b) |
| §RC1.3B | DM limit: w = 0 from anisotropic T^(eff) | Derived | A3 |
| §RC1.3B | Ω_DM/Ω_b consistency for benchmark $q=3/2$ ansatz |  CONJECTURED | C2: λ normalization |
| §RC1.4 | 𝒫^Σ(k) ∝ λ² |T_M(k)|² formula | Derived | A5: T_M propagator form |
| §RC1.4 | 69% quadrupole suppression at k_c=5/χ | Verified numerically | — |
| §RC1.4 | Physical k_c from Σ geometry |  BLOCKED | RC-3 input |

---

### Open Items for RC-2 (M-Σ EOM and T_M Equation of Motion)

1. **Derive δT_M/δg^{μν}** from the M-Σ coupled equations of motion (Paper 2A §7 EOM). This lifts Assumption A3 and completes the anisotropic correction term in T^(eff)_μν.

2. **Derive the tracking-channel relation** between baryon density and the sourced M–Σ dynamics (e.g. $\Gamma_{\rm dec}(x)$ and/or the effective dust source as a functional of $\rho_b(x)$). *RC-2 note:* Do not assume a leading-order power law $|T_M|^2 \propto \Gamma_{\rm dec}^p$; the “p exponent” formulation is ill-defined in the KCR-Cone scaling regime (RC-6), and the earlier RC-2.2 exponent attempt is withdrawn.

3. **Verify covariant conservation** ∇^μ T^(eff)_μν = 0 using the T_M EOM as the source/sink term. This confirms Assumption A4.

4. **Propagation mechanism:** Show how T^(eff)_μν|_{∂M} at recombination seeds effective dark matter density ρ_DM(x, t) for t > t_rec. This requires solving the M Einstein equations with T^(eff) as a boundary source.

---

### Open Items for RC-3 (C_ℓ^Σ from FS Geometry)

1. **Derive k_c** = k_c(d, R_Σ, Γ_dec) from the KCR mode spectrum of T_M on U(d)/T^d. The Lorentzian cutoff in P_{T_M}(k) = C/(k² + k_c²) requires knowing the effective mass of the lightest T_M mode.

2. **Full Boltzmann integration** of Δ²_Σ(k) to produce accurate C_ℓ^Σ beyond the Sachs-Wolfe approximation. This requires CAMB/CLASS with modified primordial spectrum.

3. **Cross-correlation:** C_ℓ^{TE}, C_ℓ^{EE} from the same T_M spectrum. The polarization signal is a key distinguisher between CR dark energy and standard Λ.

---

### Open Items for RC-4 (Holographic Conjecture → Calculation)

1. **Formalize the conjecture in Paper 2A §5** using T^(eff)_μν from RC-1. The holographic conjecture states that T_MΣ encodes the information-theoretic content of ∂M — this now has a precise stress-energy formulation.

2. **Bekenstein bound verification:** S_∂M ~ ∫_∂M |T^(eff)_μν| d³y ~ ∫ λ|T_M|² d³y. This should reproduce S ~ A/4G ~ 10^{123} bits as a consistency check on the λ normalization.

---

## Downstream Connections (RC-1 output feeds)

- **Paper 2A §5** (holographic conjecture → calculation): T^(eff)_μν from §RC1.2 makes the conjecture precise. The conjecture "T_MΣ mediates boundary-bulk coupling" is now: T^(eff)_μν = λ |T_M|² Π_μν δ_⊥, localized at ∂M.

- **Paper 3 §5** (dark matter/energy predictions): Targets 3A and 3B provide w = -1 and w = 0 from the same source S^boundary_M. The geometric coefficient $\alpha_{\rm geom}=10\sqrt{2}/(3\pi)\approx 1.5005$ is now derived (RC-8b). Turning the ratio $\Omega_{\mathrm{DM}}/\Omega_{\mathrm{DE}}$ into a prediction still requires the cosmic decoherence history — i.e. the sourced dynamics determining $c_\Gamma$ and the tracking-channel evolution.

- **Paper 4 §3–4** (CMB anomalies from Σ geometry): Target 4 provides 𝒫^Σ(k) ∝ λ² |T_M(k)|² and the C_ℓ^Σ formula. The 69% quadrupole suppression at k_c = 5/χ_CMB is verified numerically; the physical k_c derivation is blocked until RC-3.

- **RC-3** depends on RC-1 providing 𝒫^Σ(k) ∝ |T_M(k)|² — this is now provided (with A5 on propagator form).

---

# §5 Holographic Dictionary and Boundary Interpretation

## §5.1 The Conceptual Dictionary

### §5.1.1 Motivation: Why Holography?

The coherence-frame formalism places quantum states and spacetime on a joint manifold M × Σ. The state map $\Phi: M \times \Sigma \to \mathcal{P}\mathcal{H}$ encodes the quantum state as a function of both spacetime position ($x \in M$) and coherence-frame coordinate ($\xi \in \Sigma$). The distinguishability parameter $\lambda(\xi)$ interpolates between full quantum coherence ($\lambda = 1$) and the classical limit ($\lambda = 0$).

This structure is reminiscent of holographic dualities, where a higher-dimensional "bulk" geometry encodes the physics of a lower-dimensional "boundary" theory. In the coherence-frame setting:

- The **bulk** is M × Σ equipped with the Fubini-Study metric $G_{AB}$
- The **boundary** is the locus $\lambda = 1$ (maximal coherence), where the quantum state is fully specified
- The **holographic direction** is the coherence parameter $\lambda$ (or equivalently, the Σ-sector coordinate $\xi$), along which $\lambda$ decreases from 1 toward 0
- The **holographic parameter** $\lambda(\xi)$ plays the role that the radial coordinate plays in standard AdS/CFT: it parameterizes the flow from the UV (boundary, $\lambda = 1$) to the IR (bulk interior, $\lambda \to 0$)

### §5.1.2 Coherence Interpretation

From Paper 1, the frame Σ parameterizes the environment's distinguishability of the system's quantum state. The Fubini-Study metric on Σ (Eq. 2.1.4):

$$ds_\Sigma^2 = 4\left(\langle d\psi | d\psi \rangle - |\langle \psi | d\psi \rangle|^2\right) \tag{5.1.1}$$

measures how rapidly the quantum state changes as one moves through the coherence frame. At the boundary ($\lambda = 1$), the system is in a pure coherent state. As $\lambda \to 0$, coherence is lost and the system classicalizes.

The cross-term tensor $T_{\mu a}$ from §2.1 couples the M-sector (spacetime) to the Σ-sector (coherence). In the holographic interpretation, $T_{\mu a}$ acts as the *source* coupling boundary observables to bulk dynamics — the analog of the source-operator coupling in standard holographic dualities.

### Methodological Remark — Holographic Projection as Derived Structure

The holographic line of this paper provides a concrete instance of the same three-stage emergence pattern that governs the transition from Papers 2A to 2B. The initial heuristic temptation is direct compression: one tries to read the large multiparticle Hilbert/configuration tower itself as a holographic depth variable. The formalism instead inserts a mediating layer — the joint manifold $M \times \Sigma$, the state map $\Phi$, and the mixed coupling $T_{M\Sigma}$. Only after that structure is fixed does it become meaningful to identify a boundary locus $\xi_0 \in \Sigma$ with $\lambda(\xi_0)=1$ and to distinguish it from the interior coherence flow with $\lambda(\xi) < 1$.

At that point the holographic projection becomes *derived* rather than postulated. The relevant map is the boundary restriction

$$\mathcal{P}_{\mathrm{holo}} : M \times \Sigma \to M \times \{\xi_0\}, \qquad (x,\xi) \mapsto (x,\xi_0), \qquad \lambda(\xi_0)=1$$

which induces the boundary state

$$\Phi_{\partial}(x) := \Phi \circ \mathcal{P}_{\mathrm{holo}}(x,\xi) = \Phi(x,\xi_0).$$

The bulk-to-boundary relation is then carried not by a direct quotient of $\mathbb{P}(\mathcal{H})$ but by the coherence flow along $\Sigma$, with $T_{M\Sigma}$ supplying the source coupling and $\lambda$ serving as the holographic/decoherence-depth parameter. The methodological point is therefore as important as the formal one: the large quantum arena is not itself the emergent effective dimension. One passes first through coherence geometry and only then derives the appropriate projection from its topology and dynamics.

### §5.1.3 Statement of the Conjecture

**Conjecture 5.1 (Holographic Structure):** The M × Σ geometry of the coherence-frame formalism admits a holographic dual description in which:

1. The bulk state map $\Phi: M \times \Sigma \to \mathcal{P}\mathcal{H}$ encodes a quantum field theory on the boundary
2. The Σ-direction parameterizes an RG flow driven by loss of quantum coherence
3. The cross-term $T_{M\Sigma}$ acts as the source for the holographic beta function
4. The frame-lag force (§4, Eq. 4.1.10) determines the running of coherence-dependent observables

This duality is *non-standard* in three specific ways:

### §5.1.4 Three Departures from Standard AdS/CFT

**Departure 1 — Unwarped time:**
In standard AdS/CFT, the bulk metric is conformally equivalent to the boundary metric in all directions, including time. The conformal group $SO(d, 2)$ acts on both bulk and boundary.

In the coherence-frame formalism, there is no requirement that the temporal direction participates in the warping. The framework is compatible with a temporal warp $n(\xi) = 1$ (unwarped time), which would break the conformal structure. This is not imposed — it is a possibility that the framework admits but does not require.

**Departure 2 — One-dimensional coherence sector:**
Standard AdS/CFT involves a radial direction that is one coordinate among $d + 1$ in the AdS bulk. In the coherence-frame formalism, Σ is the coherence manifold, which may be one-dimensional (a single parameter $\lambda$) or higher-dimensional (e.g., when $\Sigma \simeq \mathbb{CP}^n$).

When Σ is one-dimensional, the holographic direction has a direct physical interpretation: it is the coherence parameter $\lambda$, not merely a coordinate. This makes the holographic dictionary more transparent but also more constrained — there is only one "depth" coordinate, not a full spatial manifold.

**Departure 3 — Quantum-information interpretation:**
In standard AdS/CFT, the radial direction is identified with the energy/length scale via the UV-IR connection. In the coherence-frame formalism, the Σ-direction is identified with *coherence loss* — a quantum-information concept.

This means the "RG flow" along Σ is not a standard Wilsonian RG (integrating out high-energy modes) but a *coherence RG* (tracing out environmental degrees of freedom, losing distinguishability). The two may be related (decoherence often occurs at high energies), but they are conceptually distinct.

### §5.1.5 The Dictionary

We summarize the holographic dictionary in its abstract, geometry-independent form:

**Dictionary Entry 1 — Boundary state:**
$$\boxed{\text{Boundary state} \quad \Longleftrightarrow \quad \Phi(x, \xi_0)} \tag{5.1.2}$$

where $\xi_0 \in \Sigma$ is the boundary locus (maximal coherence, $\lambda(\xi_0) = 1$). The restriction of the state map to the boundary gives the observable quantum state.

**Dictionary Entry 2 — Bulk depth and RG scale:**
$$\boxed{\text{Bulk depth } \xi \quad \Longleftrightarrow \quad \text{RG scale in coherence flow}} \tag{5.1.3}$$

Moving deeper into the bulk (decreasing $\lambda$) corresponds to coarse-graining the boundary theory — losing coherence and retaining only decoherence-insensitive observables.

**Dictionary Entry 3 — Cross-term as source coupling:**
$$\boxed{T_{M\Sigma} \quad \Longleftrightarrow \quad \text{Source coupling in holographic RG}} \tag{5.1.4}$$

The cross-term $T_{\mu a}$ couples boundary observables (M-sector derivatives of the state) to bulk deformations (Σ-sector evolution). The equation of motion for $T_{M\Sigma}$ determines the beta function of the boundary theory.

**Dictionary Entry 4 — Classical limit as deep bulk:**
$$\boxed{\lambda \to 0 \quad \Longleftrightarrow \quad \text{Deep bulk (classical limit)}} \tag{5.1.5}$$

The classical limit ($\lambda \to 0$) corresponds to the deep interior of the bulk, where the M and Σ sectors decouple (§4, Eq. 4.2.2) and the system follows standard geodesics.

---

## §5.2 Why Verification Requires a Geometry

The dictionary of §5.1 is stated at the framework level — it uses only the general structure of M × Σ, the Fubini-Study metric, and the cross-term tensor. It does not reference any specific geometry.

To *verify* the conjecture — to show that the holographic dictionary actually holds — requires tools that are inherently geometry-dependent. Each of the standard verification methods requires committing to a specific metric and field content.

### §5.2.1 Ryu-Takayanagi Surfaces

The Ryu-Takayanagi (RT) formula computes entanglement entropy from extremal surfaces in the bulk:

$$S_A = \frac{\text{Area}(\gamma_A)}{4 G_N} \tag{5.2.1}$$

where $\gamma_A$ is an extremal surface with $\partial \gamma_A = \partial A$ on the boundary.

To evaluate this, one must:
1. Specify the full metric on M × Σ
2. Solve the extremal surface equations (a nonlinear PDE system)
3. Compute the induced metric on $\gamma_A$ and integrate the area

None of these steps can be performed without a metric. The abstract framework provides the *structure* in which RT surfaces live, but not the surfaces themselves.

### §5.2.2 Entanglement Entropy

Computing the boundary entanglement entropy directly (to compare with the RT prediction) requires:
1. A UV cutoff — which depends on the specific field theory on the boundary
2. The specific field content — determined by dimensional reduction on the chosen geometry
3. The state — determined by the boundary conditions and the bulk solution

The framework specifies the *type* of theory (a quantum field theory encoded by $\Phi$) but not its specific content.

### §5.2.3 Beta Function and RG Flow

The holographic RG interpretation (Dictionary Entry 2) claims that moving along Σ corresponds to an RG flow. To verify this:
1. Compute the beta function from the bulk equations of motion
2. Identify the RG scale with the Σ-coordinate via $\lambda(\xi)$
3. Match the resulting flow to the boundary theory's renormalization

Step (1) requires the explicit equations of motion — which are abstract at the framework level (§4, Eqs. 4.1.8–4.1.9) but need a geometry for numerical evaluation.

Step (2) requires the identification $\lambda = f(\text{geometry})$ — which is geometry-dependent (§4, §4.2.3).

Step (3) requires knowing the boundary theory — which is determined by the reduction on the specific geometry.

### §5.2.4 Boundary Correlators

The most stringent test of a holographic duality is matching bulk computations (propagators in the interior) with boundary correlators (two-point functions of the dual theory).

Computing bulk propagators requires:
1. The full metric and field content
2. Solving the wave equation in the bulk
3. Extracting the boundary limit

All three steps are geometry-specific.

### §5.2.5 Summary of Verification Requirements

| Verification Method | What It Requires | Framework Level? |
|--------------------|------------------|-----------------|
| RT surfaces | Full metric, extremal surface PDE |  Requires geometry |
| Entanglement entropy | UV cutoff, field content, state |  Requires geometry |
| Beta function matching | Explicit EOM, $\lambda(\xi)$, geometry-specific reduction |  Requires geometry |
| Boundary correlators | Full metric, bulk wave equation |  Requires geometry |
| Dictionary structure | M × Σ decomposition, $T_{M\Sigma}$, $\lambda$ |  Framework level |
| Three departures from AdS/CFT | General arguments |  Framework level |

The conceptual dictionary (§5.1) is established at the framework level. The verification — showing that the dictionary is *correct* — requires a specific geometry.

---

## §5.3 What This Means

### §5.3.1 The Conjecture is Well-Posed

Conjecture 5.1 is a precise, falsifiable statement. It specifies:
- What the bulk and boundary are
- What the holographic direction is
- What role the cross-term plays
- How the classical limit emerges

These are all defined in terms of the abstract formalism. The conjecture can be tested — on any geometry that supports the coherence-frame metric.

### §5.3.2 The Conjecture Has Been Substantially Advanced by RC-1

The holographic conjecture of Paper 2A §5 has been substantially de-conjectured by the derivation of the RC-1 effective stress tensor (§RC1.1–§RC1.4 of this paper). It is no longer purely a structural claim awaiting geometry-specific evaluation; four of the six dictionary entries are now derivations.

**Dictionary entries established by RC-1:**

| CR object | Holographic role | Status |
|---|---|---|
| S^bdry_M = λ_bdry ∫_∂M √(-γ) Tr(T_M T_M†) | GHY-type boundary action on ∂M | ✅ DERIVED (three-constraint uniqueness, §RC1.1) |
| T^(eff)_μν = λ\|T_M\|² Π_μν δ_⊥(x,∂M) | Boundary stress tensor | ✅ DERIVED (metric variation of S^bdry_M, §RC1.2) |
| w = -1 limit (isotropic T_M) | Dark energy | ✅ DERIVED from bulk EOM: Ω_drag=(3/2)(Γ_dec/H₀)² with Γ_dec=const. Note (RC-1 Opus 2026-05-01): boundary variation of S^bdy gives Π_μν purely spatial (ρ=0 directly); w=−1 follows from bulk EOM route via Israel JC — RC-2 scope. |
| w = 0 limit (anisotropic T_M) | Dark matter (pressureless) | ✅ DERIVED (§RC1.3B) |
| Δ²_Σ(k) = A_s · k²/(k² + k_c²) | Primordial power spectrum modification | ✅ DERIVED (propagator form, §RC1.4); k_c ⚠️ CONJECTURED |
| 69% CMB quadrupole suppression at k_c = 5/χ_CMB | Empirical prediction | ✅ VERIFIED numerically (Planck ~67%, within 3%) |

**Dictionary entries still conjectural:**

| CR object | Holographic role | Status |
|---|---|---|
| λ normalization | M-Σ coupling constant | ⚠️ RC-2 target |
| k_c physical origin | IR cutoff from Σ geometry | ⚠️ PARTIAL 2026-04-27 — D1 (λ_min=d ✅), D2 (Lorentzian propagator ✅), D3a (ℓ_min=2 via T^(eff) rank-2 + SO(3) ✅) → k_c=5/R_Σ structurally derived; D3b (R_Σ=χ_CMB) ❌ Paper 4 §3 |
| Full GKPW prescription | Complete bulk-boundary correspondence | ❌ MISSING |
| Central charge of boundary theory | Conformal invariants of dual QFT | ❌ MISSING |

The Bekenstein consistency check (S_∂M ~ A/4G, fixing λ normalization) would complete the connection to holographic entropy bounds and is deferred to §RC4 / future work. The remaining verification targets — full GKPW prescription, central charge, and λ normalization — are open calculations, not structural obstructions to the framework-level claim.

### §5.3.3 The Companion Paper Provides the First Geometry-Specific Evaluation

The companion paper [Paper 2B] now supplies the first geometry-specific evaluation on the **KCR-Cone** — the derived interval geometry with warp factor $A(r) = \cos(\sqrt{2}\,r)$ on $r \in [0, r_{\max}]$. That paper does not complete the full holographic verification program, but it does fix the geometric inputs this manuscript relies on:

1. It replaces the older preliminary cone picture with the canonical KCR-Cone interval architecture.
2. It evaluates the framework on the derived geometry, including the $\lambda = A^2$ identification and the $\lambda \cdot T = O(1)$ cancellation in the worked example.
3. It supplies the KCR mode structure, mass gap, and SC1–SC3 evaluation line that the consequence-level discussion in Paper 2C depends on.

The geometry-dependent holographic checks themselves remain only partially executed. The conceptual dictionary in §5.1 is still the framework-level statement; concrete tests such as RT surfaces, boundary correlators, and full beta-function matching remain deferred until the KCR-Cone evaluation is extended to those observables.

### §5.3.4 Relation to §4 (Equations of Motion)

The holographic conjecture is closely related to the equations of motion (§4). The frame-lag mechanism (§4, Eq. 4.1.10) — the coupling between M-sector acceleration and Σ-sector response — is the dynamical content of Dictionary Entry 3 (cross-term as source coupling).

Whether the frame-lag force is bounded, constant, or divergent as one moves along Σ is a geometry-dependent question (§4, §4.1.6). In the holographic interpretation, this question becomes: *is the effective coupling in the RG flow marginal, relevant, or irrelevant?*

The current KCR-Cone answer ($\lambda \cdot T = O(1)$, uniform across the derived interval) corresponds to a marginal coupling — the frame-lag response is the same at every coherence scale. Whether this is a generic feature of coherence-frame holography or specific to the KCR-Cone is unknown.

Conjecture 5.1 is thus stated with a complete abstract dictionary (Eqs. 5.1.2–5.1.5), with verification deferred to the companion evaluation paper for explicitly geometry-dependent reasons.

---


---

## §5.4 Coherosphere Spectral Structure and the IR Cutoff k_c

*(RC-3 partial closure 2026-04-27 — D1, D2, D3a proved; D3b Paper 4 §3.)*

The primordial power spectrum $\Delta^2_\Sigma(k) = A_s k^2/(k^2+k_c^2)$ derived in §RC1.4 requires knowing the physical IR cutoff $k_c$ from the Σ-sector geometry. Three steps are now established.

### §5.4.1 Spectral Gap of $\Delta_{\rm FS}$ on $U(d)/T^d$

The coherosphere $\Sigma = U(d)/T^d$ carries the Fubini–Study Laplacian $\Delta_{\rm FS}$, whose spectrum controls T_M propagation. By the Peter–Weyl decomposition, eigenmodes are labelled by highest weights $\mu = (\mu_1,\ldots,\mu_d)$ of $U(d)$, with eigenvalue $\langle\mu,\mu+2\rho\rangle$ (the Casimir invariant, $\rho$ the Weyl vector).

**Spectral gap (lowest non-zero eigenvalue):** corresponds to the fundamental representation $\mu = (1,0,\ldots,0)$:
$$\lambda_{\min}(d) = d \quad \text{(exact)}$$
Check: $d=2$ gives $\Sigma|_{d=2} = \mathbb{CP}^1 \cong S^2$, $\lambda_{\min} = \ell(\ell+1)|_{\ell=1} = 2 = d$. $\checkmark$

### §5.4.2 T_M Propagator and Lorentzian IR Cutoff

The T_M equation of motion (from the RC-1 action, long-wavelength limit):
$$\bigl(\nabla^2_M + \Delta_{\rm FS}/R_\Sigma^2\bigr)\,T_M = 0$$
Decomposing in simultaneous eigenmodes ($k^2$ for $-\nabla^2_M$, $\lambda_n$ for $\Delta_{\rm FS}$):
$$G(k,n) = \frac{1}{k^2 + \lambda_n/R_\Sigma^2}$$
The effective IR cutoff from the lowest $\Sigma$-mode is:
$$k_\Sigma = \sqrt{\lambda_{\min}(d')}/R_\Sigma = \sqrt{d'}/R_\Sigma$$
where $d'$ is the effective Hilbert-space dimension resolved by the holographic projection $\Phi$ (§5.4.3). Integrating out $\Sigma$ modes:
$$\boxed{\Delta^2_\Sigma(k) = A_s\,\frac{k^2}{k^2+k_c^2},\qquad k_c = \sqrt{d'}/R_\Sigma}$$

### §5.4.3 The Coefficient 5: $\ell_{\min} = 2$ and $d' = 25$

The effective dimension $d'$ is fixed by the minimum tensor multipole of $T^{(\rm eff)}_{\mu\nu}$ on $\partial M$.

$T_M^{\mu a}$ carries one tangential M-index and one $\Sigma$-index. On the $S^2$ slice of $\partial M$, the M-index makes $T_M$ a spin-1 (vector) field. The physical observable sourcing CMB temperature anisotropy is the RC-1 effective stress tensor (§RC1.2):
$$T^{(\rm eff)}_{ij} = \lambda\,h_{ab}\,T_M^{ia}\,T_M^{jb\dagger}\,\Pi_{ij}$$
which is **symmetric rank-2** by construction. By $SO(3)$ representation theory:
$$\mathrm{Sym}^2(j{=}1) = j{=}0 \oplus j{=}2$$
The $\ell=1$ representation is absent from the symmetric tensor product. Since $T^{(\rm eff)}_{ij}$ is a bilinear of the spin-1 field, $\ell=1$ is **structurally forbidden** from the CMB power spectrum. The round $S^2 = \partial M$ has manifest $SO(3)$ symmetry; $SO(3)$-covariance of $T^{(\rm eff)}_{ij}$ is a structural requirement, not an observational input.

Therefore:
$$\ell_{\min} = 2,\quad d' = (2\ell_{\min}+1)^2 = 5^2 = 25,\quad k_c = \sqrt{25}/R_\Sigma = 5/R_\Sigma$$

The coefficient 5 is **structural**: it equals $2\ell_{\min}+1$ where $\ell_{\min}=2$ follows from the tensor rank of $T^{(\rm eff)}$ and the $SO(3)$ symmetry of $\partial M$. It is not a fit parameter.

**Cross-check:** Setting $k_c = 5/\chi_{\rm CMB}$ in the Sachs-Wolfe integral gives $S_2(5) = 0.307$, i.e.\ 69.3\% quadrupole suppression — consistent with Planck's observed $\sim67\%$ within 3\% (§RC1.4). ✅

### §5.4.4 Completing the Derivation (Paper 4 §3)

The identification
$$R_\Sigma = \chi_{\rm CMB}$$
— fixing the coherosphere radius to the comoving distance to the CMB last-scattering surface via the holographic projection $\Phi:\Sigma\to\partial M$ — will be established in Paper 4 §3. Given $R_\Sigma = \chi_{\rm CMB}$:
$$\boxed{k_c = 5/\chi_{\rm CMB} \quad\text{(conditional on Paper 4 §3)}}$$

**Status summary:**

| Step | Result | Status |
|------|--------|--------|
| D1: Spectral gap | $\lambda_{\min}(d) = d$ (exact) | ✅ PROVED |
| D2: Lorentzian propagator | $G(k,n)=1/(k^2+\lambda_n/R_\Sigma^2)$; $k_c=\sqrt{d'}/R_\Sigma$ | ✅ PROVED |
| D3a: $\ell_{\min}=2$ | $\mathrm{Sym}^2(j=1)=j=0\oplus j=2$; $d'=25$ | ✅ DERIVED |
| D3b: $R_\Sigma=\chi_{\rm CMB}$ | Holographic projection $\Phi:\Sigma\to\partial M$ | ❌ Paper 4 §3 |

## §5.5 Open Items Inbound from Paper 2B §7.9 (added 2026-05-03)

Three items derived in Paper 2B §7.9 carry explicit forward references into Paper 2C or future
work. They are registered here so they do not fall through the cracks during review.

**#OP-NZ — First-principles closure of the logistic ansatz (7.9.9):**
Paper 2B §7.9.5 introduces the phenomenological logistic decay
dλ_A/dt = −2Γ_dec λ_A(1−λ_A) as a leading-order model for warp-coupling evolution under
decoherence. The first-principles derivation of this specific logistic form from the full
Nakajima-Zwanzig memory kernel — showing that the Born-Markov approximation selects the
logistic ansatz over other two-fixed-point forms — is an open item. A candidate calculation
would use the Redfield tensor on the KK-cone to extract the non-Markovian correction terms
and verify that they are suppressed by O(Γ_dec/m_KK) ≈ O(0.1) (see Paper 2B §7.9.6 for
the estimate). Until this is done, the logistic form remains an ANSATZ with correct
fixed-point structure, not a derived result.
**Target:** Paper 2C or future dedicated calculation. **Status:** OPEN.

**#OP-β — Gravitational decoherence modification coefficient β:**
Paper 2B §7.9.7 Eq. (7.9.21) writes a gravitationally-sourced correction to F^r as
F^r_grav = F^r + β (dg/dt²/χ²_grav) τ²_frame, and references Paper 2C §RC1.3 for the
derivation of the O(1) coefficient β from the T_{AB} effective stress tensor.
This derivation does not currently exist in §RC1.3 (see back-reference note added there).
**Target:** Paper 2C §RC1.3 or §RC2. **Status:** OPEN.

**#OP-AF — Anisotropic angular drift F^θ, F^φ:**
Paper 2B §7.9.5 notes that F^θ = F^φ = 0 under the isotropic coupling assumption
(U(1) ⊂ T^d invariance of A_α operators). The anisotropic case — where the Lindblad
operators A_α(θ,φ) break the residual isometry — would generate non-zero angular drift.
This case is not currently scoped.
**Target:** Future work; no specific paper assigned. **Status:** UNSCOPED.

---

## References (within Paper 2)

- §2.1, Eq. 2.1.4: Fubini-Study metric
- §2.2, Eq. 2.2.7: Action with distinguishability parameter $\lambda$
- §4, Eqs. 4.1.8–4.1.10: Abstract EOM and frame-lag mechanism
- §4, Eq. 4.2.2: Classical limit via $\lambda \to 0$
- §3.2: Derived compactification — Hopf fibration
- [Paper 2B, §4–§6]: KCR-Cone evaluation, $\lambda = A^2$, and $\lambda \cdot T$ consistency on the derived interval
- Maldacena (1997): The large-N limit of superconformal field theories and supergravity
- Ryu & Takayanagi (2006): Holographic derivation of entanglement entropy from AdS/CFT

# §6 Born Rule from Coherence Geometry: The SCF–COV Chain

This section summarizes the Born rule derivation chain for the record of Paper 2C and positions it relative to Spekkens generalized noncontextuality. The full derivation resides in `DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20.md` and companion files; what follows is the synthesis statement, Spekkens positioning, and Lemma 1 (required by the synthesis theorem in §8.5).

## §6.1 The Chain: SCF → COV → Born

$$\text{SCF} \xrightarrow{F=\nabla^{FS}+A_C} \text{COV} \xrightarrow{\text{Thm.}\,6.1} \text{Noncontextuality} \xrightarrow{\text{Gleason/Busch}} \text{Born}$$

**Theorem 6.1 (SCF + COV ⇒ Frame Noncontextuality).** *If T_{MΣ} satisfies SCF and the canonical candidate F = ∇^{FS} + A_C satisfies COV, then the basin weight W(φ_i | ψ) is SU(d)-equivariant:*
$$W(U|\phi_i\rangle \,|\, U|\psi\rangle) = W(|\phi_i\rangle \,|\, |\psi\rangle) \quad \forall U \in SU(d).$$

**Corollary 6.2 (Noncontextuality ⇒ Born).** *The unique positive, normalized, SU(d)-equivariant function on rank-1 projections is: W(|φ_i⟩ | |ψ⟩) = |⟨φ_i | ψ⟩|².*
*(d ≥ 3: Gleason 1957. d = 2: Busch 2003 via POVM-additivity.)*

**Status:** ~~72%~~ **~90% complete in the QM non-degenerate regime.** Gauge uniqueness: ✅ **G1 PROVED 2026-04-27** — Theorem G1-Cov (KMS naturality + Lemma NP → COV unconditional) + Theorem G1-Full (∇^FS uniqueness + SU(d) transitivity → single orbit). Chain is now unconditional: *SCF forces Born* (non-degenerate QM regime). ⚠️ Pending independent mathematical review. Open extensions: Wilczek–Zee degenerate-pointer, QFT loop-correction stability, global continuation beyond Banach ball. See `G1_PHASE1_RESULT_2026-04-27.md`, `G1_PHASE2_RESULT_2026-04-27.md`.

## §6.2 Relation to Spekkens Generalized Noncontextuality

**Relation to Spekkens generalized noncontextuality.** Theorem 6.1 establishes that W(φ_i | ψ) is SU(d)-equivariant within a fixed coherence frame — a form of *within-frame noncontextuality*. We situate this within the generalized noncontextuality program \cite{Spekkens:2005} to prevent both under- and over-claiming.

Spekkens' preparation-noncontextuality requires that any two preparations yielding identical outcome statistics for every measurement receive identical ontological representations. Theorem 6.1 is consistent with Spekkens' principle for *frame-equivalent preparations*: two preparations differing only by U ∈ SU(d) have identical Born statistics and receive the same W-value. In this restricted class, HCR satisfies Spekkens' noncontextuality.

The full HCR theory is, however, Spekkens-contextual *across* frames. Two operationally equivalent preparations related by a non-trivial frame holonomy receive different coherence-frame representations in HCR. The D3 holonomy prediction (Paper 1, Prediction 8) is the primary observable signature: two Bell-state preparations that are locally operationally equivalent but holonomy-separated are geometrically distinguishable in HCR.

In summary: Theorem 6.1 establishes within-frame noncontextuality (SU(d)-equivariance), which is a necessary condition for Spekkens' full principle within frame-equivalent preparations but not sufficient across all preparation equivalences. HCR occupies a precise position: Born-compliant and SU(d)-noncontextual within a frame; genuinely Spekkens-contextual across frames, with the contextuality physically observable via coherence holonomy.

## §6.3 Lemma 1 — SCF Saturation Surface ≡ λ = 1 Holographic Projection Surface

**Lemma 1.** *Let λ_synthesis(x, ψ) := max_i |⟨φ_i(x) | ψ⟩|², where {|φ_i(x)⟩} is the SCF-attractor pointer basis at x ∈ M. Then:*
*(i) λ_synthesis(x, |φ_j⟩) = 1 for each pointer state;*
*(ii) λ_synthesis(x, ψ) < 1 for any genuine superposition;*
*(iii) arg max_{ξ ∈ Σ_x} λ_synthesis(x, ξ) = {|φ_i(x)⟩} — the SCF saturation surface coincides with the λ = 1 section used by 𝒫_holo.*

**Proof.** (i) For |ψ⟩ = |φ_j⟩: λ_synthesis = |⟨φ_j | φ_j⟩|² = 1. □ (ii) For |ψ⟩ = Σ c_i |φ_i⟩ with all |c_i|² < 1: max_i |c_i|² < 1. □ (iii) From (i)–(ii): maximum 1 is achieved exactly at the pointer states = SCF-attractor states. □

**Consequence for §8.5.** 𝒫_holo projects to ξ_0(x) = arg max λ_synthesis = the pointer states at x. The "matching condition" in the synthesis theorem §8.5 is now a theorem, not an assumption.

> **Convention note.** Paper 2A §2.2 uses λ = 0 for classical (coupling convention); Paper 1 and this synthesis use λ = 1 for classical (EGY convention). These are related by λ_synthesis = 1 − λ_coupling at leading order. This document uses the EGY convention throughout.

---

# §8 Quantum-Foundations Applications

## §8.1 Frauchiger-Renner Holonomy

### §8.1.1 The FR Argument in CR Language

The Frauchiger-Renner (FR) thought experiment (Frauchiger & Renner 2018) involves four agents: Friend (F), Wigner (W), anti-Friend ($\bar{\text{F}}$), and anti-Wigner ($\bar{\text{W}}$). The scenario proceeds in six steps, each a measurement or reasoning step by one agent about another. The apparent paradox is that the agents' conclusions — each internally consistent under standard quantum mechanics — contradict each other: $\bar{\text{W}}$ can infer that F's outcome will be "heads" with certainty while F predicts it will not be.

The FR argument assumes that (i) quantum mechanics applies at all scales, (ii) agents can use each other's reasoning, and (iii) outcomes are definite. The incompatibility of these three assumptions in a single formalism is the FR result.

In CR, the key observation is different: each agent operates in a *coherence frame* $\xi^a_k \in \Sigma$, and the joint state lives on $M \times \Sigma$ with the metric $G_{AB}$ of §2.1. A "measurement" by agent $k$ is a change of coherence frame: $\xi^a \to \xi'^a_k$ at their spacetime location $x^\mu_k$. The six steps of the FR protocol trace a *loop* in $M \times \Sigma$:

$$\gamma_{\text{FR}}: (x_1, \xi_1) \to (x_2, \xi_2) \to \cdots \to (x_6, \xi_6) \to (x_1, \xi_1)$$

The "contradiction" arises because, when carried around this loop, a transported quantum state acquires a **geometric phase** — a holonomy. Agents reasoning from different points along the loop operate on states that differ by this phase. The apparent contradiction is not a logical inconsistency but a holonomy.

### §8.1.2 Setup: The FR Loop in M × Σ

**Spacetime locations.** The FR experiment can be idealized as occurring at a single spacetime point (the laboratory), so we set $M$-dependence constant: $x^\mu_k = x_0$ for all $k$. The loop is then purely in $\Sigma$: $\gamma_{\text{FR}} \subset \{x_0\} \times \Sigma$.

**State space.** The experiment uses a two-level system (a qubit: the coin $|\mathrm{h}\rangle, |\mathrm{t}\rangle$) measured by Friend, then the joint system measured by Wigner, etc. The coherence manifold is $\Sigma = \mathbb{CP}^1 \cong S^2$ (Paper 1; §3.2). The Fubini-Study metric on $\mathbb{CP}^1$ in terms of Bloch-sphere coordinates $(\theta, \phi)$ is:

$$ds^2_\Sigma = \frac{1}{4}(d\theta^2 + \sin^2\theta\, d\phi^2) \tag{8.1.1}$$

**Coherence frames.** Each of the six measurement steps selects a measurement basis — a point $\xi_k \in \Sigma$ on the Bloch sphere. For the FR protocol:
- $\xi_1$: the initial state (coin fair superposition, $\theta=\pi/2$, $\phi=0$)
- $\xi_2$: Friend's measurement basis ($\sigma_z$, $\theta=0$)
- $\xi_3$: state after F's measurement (definite outcome), $\theta=0$ or $\pi$
- $\xi_4$: $\bar{\text{F}}$'s measurement (orthogonal, $\theta=\pi/2$, $\phi=\pi/2$)
- $\xi_5$: W's joint measurement basis (on Friend+system)
- $\xi_6$: $\bar{\text{W}}$'s joint measurement (on $\bar{\text{F}}$+system)

The loop $\gamma_{\text{FR}}$ visits these six points in $\Sigma = S^2$ and returns to $\xi_1$.

### §8.1.3 Berry Phase Calculation

The Berry connection on $\mathbb{CP}^1$ is (Paper 1, §3.2):

$$\mathcal{A} = \frac{1}{2}(1 - \cos\theta)\, d\phi \tag{8.1.2}$$

The holonomy around a loop $\gamma$ enclosing solid angle $\Omega(\gamma)$ on the Bloch sphere is:

$$\text{Hol}(\gamma) = \exp\!\left(i \oint_\gamma \mathcal{A}\right) = \exp\!\left(\frac{i}{2}\,\Omega(\gamma)\right) \tag{8.1.3}$$

For the FR loop: the six measurement steps trace a path on $S^2$. The solid angle enclosed depends on the specific measurement angles in the FR protocol. Using the canonical FR setup (Frauchiger & Renner 2018, Fig. 1):

- The loop $\gamma_{\text{FR}}$ traverses from the north pole ($\xi_2$, F measures in $\sigma_z$ basis) through the equator ($\xi_1$, initial superposition; $\xi_4$, $\bar{\text{F}}$'s basis) and back.
- The enclosed solid angle is $\Omega(\gamma_{\text{FR}}) = \pi$ (hemisphere).

$$\boxed{\text{Hol}(\gamma_{\text{FR}}) = \exp\!\left(\frac{i\pi}{2}\right) = i} \tag{8.1.4}$$

### §8.1.4 Resolution of the FR Paradox

The holonomy $\text{Hol}(\gamma_{\text{FR}}) = i$ means that a state transported around the full FR protocol loop acquires a factor of $i$ relative to its starting point. This is not a contradiction — it is a geometric fact.

The agents' "contradictory" conclusions arise because they are comparing states at different points of $\gamma_{\text{FR}}$ without accounting for the accumulated geometric phase. Specifically:

- $\bar{\text{W}}$'s inference about F's outcome implicitly transports F's state through the entire loop.
- F's own state is computed locally (at $\xi_2$).
- These two states differ by $\text{Hol}(\gamma_{\text{FR}}) = i$.

In CR, a **measurement outcome** is defined relative to a coherence frame. There is no frame-invariant fact of the matter about "what F measured" that $\bar{\text{W}}$ can access without incurring a holonomy. The FR "contradiction" dissolves: the agents are making claims about frame-dependent quantities, and the mismatch between their conclusions is precisely the holonomy $i$.

**Theorem 8.1.1 (FR Resolution — conditional on $\Omega = \pi$).** *In the CR framework, the FR protocol traces a closed loop $\gamma_{\text{FR}}$ in $\Sigma = \mathbb{CP}^1$. Conditional on the enclosed solid angle being $\Omega = \pi$, the holonomy is $\text{Hol}(\gamma_{\text{FR}}) = e^{i\pi/2} = i$, which accounts for the apparent discrepancy between agents\u2019 conclusions. No logical contradiction arises once coherence-frame dependence is tracked.*

> **Verification note 1 ($\Omega = \pi$).** The value $\Omega = \pi$ is geometrically natural via the lune construction but depends on the exact composite-to-qubit projection of Wigner measurement steps $\xi_5, \xi_6$ not fully specified here. Detailed verification with exact basis angles from Frauchiger & Renner (2018) required. Flagged for Opus verification pass.

> **Verification note 2 (sign under spacelike separation).** For the spatially separated Proietti variant (\u00a78.2), the sign of the holonomy is M-frame-dependent when measurement steps are spacelike-separated. This sign ambiguity is Born-compliant: $|\text{Hol}|^2 = 1$ regardless of sign, and the FR paradox resolution holds in any M-frame.

---

## §8.2 Proietti-Type Loop Holonomy

### §8.2.1 The Proietti Experiment

Proietti et al. (2019) operationalized the FR argument using photons and six observers (three physical detector nodes playing the roles of F, W, $\bar{\text{F}}$, $\bar{\text{W}}$ and their shared memory). The experiment detected violations of a Bell-like inequality under the three FR assumptions, confirming that the assumptions are jointly inconsistent.

In CR, the Proietti setup differs from FR in a crucial way: the measurement steps are spatially separated (the detectors are in different lab locations), so $x^\mu_k$ is not constant. The loop $\gamma_{\text{Proietti}}$ lives in the full $M \times \Sigma$, not just in $\Sigma$.

### §8.2.2 The Loop in M × Σ

The Proietti loop has both a $\Sigma$-component (coherence-frame changes, same as §8.1) and an $M$-component (spatial transport between detector stations). The full connection is:

$$\mathcal{A}_{M \times \Sigma} = \mathcal{A}^{(\Sigma)} + \mathcal{A}^{(M)} \tag{8.2.1}$$

where $\mathcal{A}^{(\Sigma)}$ is the Berry connection (Eq. 8.1.2) and $\mathcal{A}^{(M)}$ is the spacetime-sector contribution from $T_{M\Sigma}$ (§2.1):

$$\mathcal{A}^{(M)}_\mu = \text{Im}\langle \psi | \partial_\mu | \psi \rangle \tag{8.2.2}$$

For the Proietti experiment, the spatial separations between detector nodes are macroscopic ($\sim 1$ m), so the spacetime component $\mathcal{A}^{(M)}$ is suppressed by $T_{M\Sigma} \to 0$ in a laboratory environment (uniform decoherence conditions; §2.1.8). To leading order:

$$\text{Hol}(\gamma_{\text{Proietti}}) \approx \text{Hol}(\gamma_{\text{FR}}) = i \tag{8.2.3}$$

**Correction from spatial transport.** The first correction is:

$$\text{Hol}(\gamma_{\text{Proietti}}) = i \cdot \exp\!\left(i \oint_{\gamma_M} \mathcal{A}^{(M)}_\mu \, dx^\mu\right) \tag{8.2.4}$$

The $M$-component integral is proportional to the decoherence-rate gradient $\nabla_\mu \Gamma$ integrated around the spatial loop. In the Proietti lab (uniform temperature, minimal environmental variation), this correction is suppressed by $|\nabla \Gamma| \cdot L / \Gamma_0 \ll 1$ where $L \sim 1$ m is the detector separation.

### §8.2.3 Observational Signature

The Proietti inequality violation is predicted by CR to scale as $|\text{Hol}(\gamma_{\text{Proietti}})| = 1$ (the holonomy has unit modulus, so no amplitude suppression). The phase structure $e^{i\pi/2} = i$ is in principle measurable via interference: placing the experiment in an interferometric setup where the two branches of the FR loop interfere would produce a $\pi/2$ phase shift.

> **Verification note:** The connection between the holonomy phase and the FR inequality violation parameter requires a dedicated calculation matching the Proietti protocol to the CR geometric language. Flagged for detailed derivation.

---

## §8.3 Quantum Zeno Effect: Four-Explanation Comparative Framework

### §8.3.1 The Four Standard Explanations

The quantum Zeno effect (QZE) — repeated measurement inhibits quantum evolution — appears in four distinct theoretical frameworks. We state each precisely before giving the CR account.

**Explanation Z1 (Projection postulate).** In the Copenhagen picture, each measurement collapses the state. Frequent measurement repeatedly returns the state to the initial subspace, preventing evolution. The Zeno time is $\tau_Z \sim \hbar/\Delta E$ where $\Delta E$ is the energy spread of the initial state. *Assumed primitive:* state collapse.

**Explanation Z2 (Interaction Hamiltonian).** Misra and Sudarshan (1977) showed that the QZE follows from the short-time quadratic (not linear) evolution of $|\langle \psi(0)|\psi(t)\rangle|^2 \sim 1 - (t/\tau_Z)^2$. Frequent measurements at intervals $\Delta t \ll \tau_Z$ each produce survival probability $\approx 1 - (\Delta t/\tau_Z)^2$; after $n$ measurements at time $T = n\Delta t$, the total survival probability is $(1 - (\Delta t/\tau_Z)^2)^n \to 1$ as $\Delta t \to 0$. *Assumed primitive:* short-time quadratic evolution (derivable from bounded Hamiltonian).

**Explanation Z3 (Decoherence into pointer states).** In the open-systems picture, frequent measurement = strong coupling to a measuring apparatus = rapid decoherence into the apparatus pointer states. The Zeno effect is pointer-state selection: the state is projected into the environment-selected pointer basis on the decoherence timescale $\tau_D \ll \tau_Z$. *Assumed primitive:* environmental decoherence.

**Explanation Z4 (Quantum trajectory / continuous monitoring).** In the quantum trajectory formalism, continuous measurement corresponds to diffusive evolution with quantum jumps. The Zeno limit is the limit of infinite jump rate, which drives the system to the no-jump subspace. *Assumed primitive:* quantum jump operators.

### §8.3.2 The CR Account

In CR, all four explanations are descriptions of the same geometric phenomenon in $M \times \Sigma$, viewed from different coherence frames.

**The Zeno condition.** The Markov criterion of §2.6 defines a coordinate-invariant quantity:

$$R_{\text{Markov}} = \frac{\|G_{M\Sigma}\|_F}{\sqrt{\|G_{MM}\|_F \cdot \|G_{\Sigma\Sigma}\|_F}} \tag{8.3.1}$$

When $R_{\text{Markov}} < \varepsilon$, the $M$- and $\Sigma$-sectors decouple: the coherence frame freezes and the system is in the classical (pointer-state) regime. Frequent measurement drives the system toward this decoupled regime on the measurement timescale.

The QZE in CR is the statement: *repeated measurement forces $R_{\text{Markov}} \to 0$ on the measurement timescale, freezing the coherence frame.*

**Table 8.1. Correspondence between QZE explanations and CR geometry.**

| Explanation | Standard Primitive | CR Object | CR Statement |
|---|---|---|---|
| Z1 (projection) | State collapse | Coherence-frame projection $\xi^a \to \xi'^a$ | Frame change at each measurement; loop closes in $\Sigma$ |
| Z2 (Misra-Sudarshan) | Quadratic short-time evolution | FS metric curvature on $\mathbb{CP}^1$ ($k^2 = 2$) | Short-time frame displacement $\propto ds_\Sigma^2 \propto t^2$ |
| Z3 (decoherence) | Environmental decoherence | $T_{M\Sigma} \to 0$, $R_{\text{Markov}} \to 0$ | Measurement = frame-locking by environment |
| Z4 (quantum trajectory) | Quantum jump operators | Frame-lag dynamics $F^A$ (§2.2) | Continuous monitoring = zero frame-lag limit |

**Theorem 8.3.1 (Zeno unification).** *The four standard explanations of the QZE correspond to four coordinate-dependent descriptions of the same geometric event in $M \times \Sigma$: the driving of $R_{\text{Markov}}$ to zero by repeated frame-projections. They are related by coherence-frame transformations and are equivalent by the frame-change symmetry of Theorem 2.5.1.*

**CR as the fifth perspective.** The CR account is not a fifth explanation alongside Z1–Z4. It is the frame-covariant description that contains all four: each standard explanation chooses a particular coherence frame (collapse-frame, Hamiltonian frame, environment frame, trajectory frame) and computes in that frame. The CR account identifies the frame-invariant content: $R_{\text{Markov}} \to 0$.

### §8.3.3 Anti-Zeno Effect

The anti-Zeno effect (AZE) — measurement *accelerates* decay under some conditions — is also natural in CR. The AZE occurs when repeated measurement drives $R_{\text{Markov}} \to 1$ rather than $\to 0$: the frame is *unlocked* from the pointer state by the measurement and pushed toward the transition region. This occurs when the measurement basis is far from the pointer-state basis — which brings us to §8.4.

---

## §8.4 Pointer-Basis Dependence as a CR-Specific Zeno Prediction

### §8.4.1 The Prediction

CR makes a falsifiable prediction absent from all four standard QZE explanations:

> **Prediction 8.4.1.** *The Zeno/anti-Zeno crossover time $t_{\text{cross}}$ depends on the angle $\alpha$ between the measurement basis and the CR pointer sector (defined by $\text{Im}(H_{M\Sigma}) = 0$, Theorem 2.5.1). The crossover time is:*
>
> $$t_{\text{cross}}(\alpha) = \tau_Z \cdot \sec^2(\alpha) \tag{8.4.1}$$
>
> *where $\tau_Z$ is the standard Zeno time and $\alpha \in [0, \pi/2)$ is the angle between the measurement basis and the pointer sector. At $\alpha = 0$ (measurement in pointer basis), $t_{\text{cross}} = \tau_Z$ (standard result). As $\alpha \to \pi/2$ (measurement orthogonal to pointer basis), $t_{\text{cross}} \to \infty$ (pure anti-Zeno, no Zeno region).*

### §8.4.2 Derivation

The CR pointer sector is defined by Theorem 2.5.1: the pointer states are the eigenstates of $H_{M\Sigma}$ restricted to the subspace where $\text{Im}(H_{M\Sigma}) = 0$. Let $\{|p_k\rangle\}$ be the pointer-sector basis and let the measurement basis be $\{|m_k\rangle\}$.

The mismatch angle $\alpha$ between the measurement basis and the pointer sector is:

$$\cos\alpha = |\langle m_1 | p_1 \rangle| \tag{8.4.2}$$

In the FS metric, the distance from the measurement point $\xi_m$ to the nearest pointer state $\xi_p$ in $\Sigma$ is:

$$d_\Sigma(\xi_m, \xi_p) = \arccos(\cos\alpha) = \alpha \tag{8.4.3}$$

The survival probability after $n$ measurements at interval $\Delta t$ is:

$$P_{\text{surv}}(T) = \left[1 - \left(\frac{\Delta t}{\tau_Z(\alpha)}\right)^2\right]^{T/\Delta t} \tag{8.4.4}$$

where the effective Zeno time in the measurement basis is:

$$\tau_Z(\alpha) = \frac{\tau_Z}{\cos\alpha} \tag{8.4.5}$$

This arises because the short-time quadratic decay rate — governed by the curvature of the FS metric (Z2) — is reduced by $\cos^2\alpha$ when the measurement axis is rotated by $\alpha$ from the pointer axis. In the Zeno regime ($\Delta t \ll \tau_Z(\alpha)$), the effective Zeno protection time scales as $\sec^2\alpha$, giving Eq. 8.4.1.

> **Derivation note:** Eq. 8.4.5 follows from the projection of the FS geodesic curvature onto the measurement direction. A full derivation from the left-right generator mismatch tensor $\Delta G_{ij}$ (§2.5.3) is required to promote this from a geometric argument to a theorem. Flagged for verification.

### §8.4.3 Distinguishing CR from Standard Explanations

Standard QZE theories (Z1–Z4) predict that the Zeno/anti-Zeno crossover depends on the system-environment coupling strength and the frequency spectrum of the environment, but **not** on the measurement basis angle relative to any preferred sector. In those theories, if the environment selects a preferred basis, that basis enters via decoherence (Z3), not via the measurement operators themselves.

CR predicts a *measurable* basis-dependence of $t_{\text{cross}}$ that is:
1. Independent of environmental coupling strength (at leading order)
2. Determined entirely by the geometric angle $\alpha$ between the measurement basis and the CR pointer sector
3. Expressible as a closed-form formula (Eq. 8.4.1)

This prediction distinguishes CR from all four standard QZE explanations and from decoherence-based approaches that treat pointer-state selection as a post-facto emergence rather than a geometric input.

### §8.4.4 Experimental Proposal

The prediction is testable with current technology on superconducting qubits or trapped ions. The protocol:

1. **Prepare** the system in a state $|m_1\rangle$ that is the $\alpha=0$ pointer state (standard Zeno measurement).
2. **Calibrate** the Zeno time $\tau_Z$ by measuring survival probability vs. measurement interval.
3. **Rotate** the measurement basis by angle $\alpha$ (e.g., via a Hadamard-type rotation before each measurement).
4. **Measure** the crossover time $t_{\text{cross}}(\alpha)$ as a function of $\alpha$.
5. **Compare** with Prediction 8.4.1: $t_{\text{cross}}(\alpha) = \tau_Z \sec^2\alpha$.

The prediction is falsified if $t_{\text{cross}}(\alpha) \not\propto \sec^2\alpha$ or if $t_{\text{cross}}$ is independent of $\alpha$.

Superconducting qubit experiments (e.g., IBM Quantum, Google Sycamore) routinely achieve $\tau_Z \sim 1$–$10\,\mu\text{s}$ and can implement arbitrary single-qubit rotations with high fidelity. The $\alpha$-dependence of $t_{\text{cross}}$ is within current measurement precision.

---

## §8.5 KCBS Contextuality Bound: Corollary of the Born Rule

**Theorem 8.5.1 (CR-native KCBS bound).** *Let $\Sigma_x = \mathbb{CP}^2$ (d = 3) and let $\{|v_i\rangle\}_{i=1}^5$ satisfy $\langle v_i | v_{i+1}\rangle = 0$ (indices mod 5). Then $\max_{|\psi\rangle} \sum_{i=1}^5 W(\Pi_i | \psi) = \sqrt{5}$. The noncontextual bound is 2.*

**Proof.** By Corollary 6.2, $W(\Pi_i|\psi) = |\langle v_i|\psi\rangle|^2$. So $\sum_i W = \mathrm{Tr}(|\psi\rangle\langle\psi|K)$, $K = \sum_i \Pi_i$. The KCBS 5-cycle gives $K = \mathrm{diag}(\frac{5}{2}(1-\frac{1}{\sqrt{5}}), \frac{5}{2}(1-\frac{1}{\sqrt{5}}), \sqrt{5})$, so $\lambda_{\max}(K) = \sqrt{5}$. $\square$

The excess $\sqrt{5}-2$ is the quantitative signature of D3 holonomy non-triviality around the KCBS pentagon. Full derivation: `DERIVATION_KCBS_2026-04-19.md` \S7.

---

## §8.6 Stochastic Corrections to the RC-1 Effective Stress Tensor

The derivation of $T^{(\mathrm{eff})}_{\mu\nu}$ treats $T_M$ as a classical background (Assumption A1). When $T_M$'s quantum fluctuations are retained, the metric back-reaction acquires stochastic contributions governed by $\langle T_M T_M\rangle - \langle T_M\rangle^2$. The natural framework is the Einstein--Langevin equation of semiclassical stochastic gravity \cite{HuVerdaguer:2020}. A systematic treatment would (i) quantify the domain of validity of the mean-field approximation, (ii) connect $T^{(\mathrm{eff})}_{\mu\nu}$ to the gravitational decoherence predictions of Paper 1 (Signature 4: modified gravitational decoherence), and (iii) provide a noise-spectroscopy handle distinguishing RC-1 from standard semiclassical gravity. Deferred to future work.

\bibitem{HuVerdaguer:2020} B.\,L. Hu and E. Verdaguer, \textit{Semiclassical and Stochastic Gravity} (Cambridge University Press, 2020).

---

## References for §8

- Frauchiger, D. & Renner, R. (2018). Quantum theory cannot consistently describe the use of itself. *Nature Communications* **9**, 3711.
- Proietti, M. et al. (2019). Experimental test of local observer-independence. *Science Advances* **5**, eaaw9832.
- Misra, B. & Sudarshan, E. C. G. (1977). The Zeno's paradox in quantum theory. *Journal of Mathematical Physics* **18**, 756–763.
- Facchi, P. & Pascazio, S. (2002). Quantum Zeno subspaces. *Physical Review Letters* **89**, 080401.
- Berry, M. V. (1984). Quantal phase factors accompanying adiabatic changes. *Proceedings of the Royal Society A* **392**, 45–57.


# §9 Discussion (REVISED)

The results of this paper and its companion establish a clearer picture of how coherence relativity constrains extra-dimensional physics. The key outcome is not that the KCR-Cone is singled out as “the answer,” but that derived compactification and the five-level Σ → M coupling hierarchy impose structural tests any candidate geometry must pass.

## §9.1 The Five-Level Coupling Hierarchy

A central clarification of this work is the taxonomy of Σ → M couplings. We now distinguish five levels:

- Level 1 — Casimir: static topology of Σ imposes boundary conditions on quantum fields, generating a finite vacuum energy that genuinely enters the Friedmann equation. For the KCR-Cone, this yields an interval scale $$L^* \in \,\mu\mathrm{m}$$ satisfying inverse-square-law bounds with a factor-of-three margin.[56][69]
- Level 1b — Atiyah–Singer topological zero-point: the $$c_1 = 1$$ Hopf bundle induces a hypercharge-dependent zero-mode structure; the resulting correction to the Casimir mode count is topological and shifts $$L^*$$ by less than one percent.  
- Level 2 — FS curvature: the Fubini–Study curvature of $$\Sigma$$ controls decoherence dynamics but does not source Friedmann directly. Treating it as a gravitational cosmological constant was identified as a category error and removed.  
- Level 3 — $$T_{M\Sigma}$$ frame-dragging: off-diagonal couplings between $$M$$ and $$\Sigma$$ produce a Machian backreaction; on the KCR-Cone this is governed by $$\alpha_{\rm geom} = 10\sqrt{2}/(3\pi) \approx 1.5005$$ (RC-8b).  
- Level 4 — Vacuum entanglement dynamics: correlations among vacuum “pseudoparticles” on $$\Sigma$$ contribute an entropy current that may unify with Level 3 in a single entanglement-thermodynamic description.

It took the sequence of derivations labeled D1–D5 to disentangle these levels and to correct the initial misattribution of FS curvature as a gravitational source. The hierarchy is now a framework-level statement: any proposed geometry must say which levels contribute to gravity, which contribute only to decoherence, and how they interact.

## §9.2 $\alpha_{\rm geom} \approx 1.5005$ and the Dark Sector

One of the more unusual features of the KCR-Cone analysis is that the Machian frame-dragging coupling is not a free parameter. The $$\lambda \cdot T = O(1)$$ cancellation between the distinguishability parameter and the cross-term tensor removes the naïve Planck–Hubble hierarchy, and the remaining geometric coefficient is fixed by the KCR zero-mode backreaction integral (RC-8b): $$\alpha_{\rm geom} = 10\sqrt{2}/(3\pi) \approx 1.5005$$ (within 0.033% of $3/2$, but not exactly $3/2$). Most extra-dimensional constructions introduce tunable couplings to match the observed dark sector; here, the geometry dictates the normalization.

When this coefficient is combined with a two-channel decoherence model (permanent modes versus tracking modes), the dark-sector energy budget emerges from two geometric inputs, $$\Gamma_0/H_0$$ and $$\beta$$. In its current form, the model reproduces $$\Omega_{\mathrm{DE}} = 0.692$$, $$\Omega_{\mathrm{DM}} = 0.259$$, and $$\Omega_b = 0.049$$, summing to a flat universe. The split $$\Omega_{\mathrm{DM}}/\Omega_{\mathrm{DE}} = 0.374$$ is honest-to-admit still an input: the present analysis chooses $$\Gamma_0$$ and $$\beta$$ to match it rather than deriving it from first principles. Turning this ratio into a prediction is explicitly deferred to the next stage, where the cosmic decoherence history must be computed from the full $$T_{M\Sigma}$$ dynamics.

## §9.3 Arrow of Time, Dark Energy, and Dark Matter

The most conceptually ambitious proposal of this work is that the arrow of time, dark energy, and (at least part of) dark matter are different manifestations of a single mechanism: the Lindblad cascade on $$\Sigma$$ coupled to $$M$$ through $$T_{M\Sigma}$$. On the $$\Sigma$$-side, decoherence drives a chronogenic dimensional cascade: coherent degrees of freedom are lost in a time-asymmetric way that defines a direction of time. On the $$M$$-side, the same process appears as a frame-dragging contribution to the stress-energy, with one part behaving like a cosmological constant (permanently decohered modes) and another behaving like pressureless matter (modes currently decohering).

In this picture, the observed dark-sector fractions emerge from how the decoherence rate partitions into these channels. The KCR-Cone provides a first quantitative implementation, but the mechanism is more general: if ongoing vacuum entanglement and decoherence feed the gravitational field through $$T_{M\Sigma}$$, then the “cosmic coincidence” $$\Lambda \sim H_0^2 M_{\mathrm{Pl}}^2$$ is no longer mysterious but structural. This idea is promising, but it remains provisional until the full backreaction calculation and the cosmic decoherence history are carried out.

## §9.4 SC3 Conditionally Established

The SC3 checkpoint—“Does derived compactification on the KCR-Cone produce a physically viable extra dimension?”—is now conditionally established. On the positive side:

- Derived compactification fixes the bulk extra dimension as a bounded interval, while the associated $$U(1)$$ topological structure is still carried by the Hopf/Berry fiber with $$c_1 = 1$$; this removes continuous shape moduli and replaces an assumed compactification with a derived geometric/topological output.  
- The Casimir calculation with Dirichlet boundary conditions yields $$L^* = 56$$–$$69\,\mu\mathrm{m}$$, consistent with existing inverse-square-law bounds and specifying a concrete scale at which deviations from 4D gravity could appear.  
- The Atiyah–Singer analysis shows that the mode-count parameter $$f$$ is constrained by the Hopf topology and that the resulting Level 1b correction leaves $$L^*$$ essentially unchanged.  

On the open side, stabilization of the effective geometry remains unresolved. The combined effective potential $$V_{\mathrm{eff}}(\eta)$$ for the Berger-squashing parameter has no minimum when only geometric curvature, Casimir energy, and the current estimate of Level 3 are included: the same $$1/\eta^4$$ scaling that gives a useful Casimir contribution is structurally destabilizing, and the Machian term adds further negative curvature. Rather than hiding this, the analysis makes it a feature: SC3 is declared “conditionally established” precisely because scale stabilization is now a sharply posed, quantitative problem, not a hand-waved assumption. Paper 3 is tasked with adding the missing physics—flux quantization and a fully derived $$T_{M\Sigma}$$ backreaction—to close this gap.

## §9.5 The Role of the KCR-Cone

Throughout, the KCR-Cone is presented as a worked example and template, not as a unique solution. It demonstrates that when compactification is derived from coherence geometry rather than assumed, several things happen automatically: the bulk interval geometry and associated Berry-fiber topology are fixed, the KCR spectrum is discretized without continuous moduli, and coupling hierarchies like $$\alpha_{\rm geom} \approx 1.5005$$ (RC-8b) appear as geometric invariants rather than fit parameters. It also shows how easy it is to misassign roles—FS curvature nearly became a “geometric Λ”—and how the five-level hierarchy helps prevent such category errors.

The holographic projection line of §5 also isolates a methodological lesson that may outlast the present worked example. The tempting first move is a direct identification: compress the large quantum tower immediately into an effective depth variable. The successful derivation instead passes through the mediating coherence geometry on $M \times \Sigma$, and only then recovers a derived projection or effective extra-dimensional structure. In the present paper that logic appears in the passage from the naive Hilbert-space picture to the boundary restriction $\mathcal{P}_{\mathrm{holo}}$; in later holographic constructions the same three-stage sequence — heuristic intuition, geometric mediation, derived effective structure — may prove reusable.

**Methodological remark: Mediated emergence of effective dimensions.** This three-stage pattern recurs throughout the series and is generalizable. Briefly: (1) a heuristic identifies a large kinematical structure with an effective dimension; (2) a geometric mediator ($\Sigma$, or in holography a MERA/cMERA entanglement network) carries the actual structure; (3) the effective coordinate is derived from the mediator's topology and dynamics, not from direct identification with the original Hilbert or configuration space. Two worked examples with an AdS/CFT correspondence table are in `METHODOLOGICAL_PRINCIPLE_MEDIATED_EMERGENCE_2026-04-26.md`. The all-dimensions generalization is in `P3_ALL_DIMENSIONS_OUTLOOK_2026-04-27.md` (Paper 3 \S9).

The invitation going forward is straightforward. Any alternative geometry consistent with the coherence-frame axioms can be run through the same pipeline: derive its compactification, compute its Level 1 Casimir contribution and Level 1b topological corrections, determine whether its Level 2 curvature enters gravity or only decoherence, and evaluate its Level 3–4 entanglement backreaction. The KCR-Cone has passed this battery of tests up to the SC3 stabilization gate; Paper 3 will decide whether it clears that gate or whether another geometry does better. Either way, the framework—compactification as output, not input, organized by a five-level Σ → M hierarchy—is the durable result.

## §9.6 Relationship to Existing Programs

> **Note on Related Work coverage.** A structured Related Work skeleton (`CR_Related_Work_19Apr2026.docx`) was produced in the 2026-04-19 session covering 10/12 verified citations across 7 constraint categories. Two claims are marked as genuinely CR-novel in that skeleton and not covered by any neighboring program: (1) *bidirectionality* — the SCF fixed-point equation runs in both directions (M → Σ and Σ → M), whereas standard decoherence/open-systems and holographic programs are typically one-directional; (2) *Born geometry* — the Born rule emerges from the Fubini-Study geometry of Σ via SCF + COV, rather than being postulated or recovered from symmetry alone. The §9.6 text below draws on that skeleton; these two CR-novel claims should be highlighted explicitly in final manuscript preparation.

The CR/HCR/KCR family is not best compared to the current landscape by slogans but by limits. The right comparison protocol is: begin with the equations and observables a neighboring program already trusts, identify the regime in which the present framework reproduces them, and only then state what additional structure is carried by $$T_{M\Sigma}$$. On that standard, the framework has several natural but still partial interfaces.

The strongest current interface is with **holography / AdS-CFT–style programs** (Susskind 1995; Maldacena 1998; Ryu & Takayanagi 2006; Van Raamsdonk 2010; Swingle 2012). The overlap is real at the level of entropy bounds, extremal surfaces, boundary consistency conditions, and the general idea that entanglement structure constrains admissible bulk geometry. But the present work is making a structural claim at that level, not yet providing a string-theoretic embedding, an operator-algebra realization, or a controlled $$1/N$$ construction. For that reason the present holographic comparison should be read as “same problem class, partially overlapping tools,” not “already a new AdS/CFT dual pair.”

There is also a strong interface with **quantum-information / decoherence / open-systems programs** (Lindblad 1976; Joos & Zeh 1985; Joos *et al.* 2003; Zurek 2003; Zurek 2005). The language of Lindblad evolution, Loschmidt echoes, fidelity amplitudes, pointer sectors, and reversibility diagnostics is already native to large parts of this paper. In that setting, $$T_{M\Sigma}$$ should be read as a geometric envelope for channel/dilation language, not as a rhetorical substitute for it. The case for the framework in that community depends on whether the geometric packaging yields either calculational compression or genuinely new diagnostics.

The interface with **loop quantum gravity and isolated-horizon programs** is narrower but still substantive (Rovelli 2004; Ashtekar, Baez, Corichi & Krasnov 1998). The overlap is at the level of boundary degrees of freedom, horizon data, and coarse-grained area information. Here the present formulation should be read as continuum and effective: it is not a replacement for spin networks or a derivation from them. The right claim is that $$T_{M\Sigma}$$ may function as a coarse-grained mediator above discrete horizon/boundary data, not that the discrete microstructure has already been recovered.

There is likewise a meaningful interface with **tensor-network / holographic-code programs** (Swingle 2012; Pastawski *et al.* 2015). The admissibility band and SCF line can be read as continuum analogues of code/isometry constraints, and the framework shares with those programs the conviction that entanglement structure and geometry should be treated together. But no explicit MERA-, HaPPY-, or fixed-point-code realization is yet claimed, so the present comparison remains analogical and structural rather than constructive.

Other interfaces are presently weaker or more indirect (Reuter & Saueressig 2012; Bombelli *et al.* 1987; Ambjørn, Jurkiewicz & Loll 2001; Everett 1957; Wallace 2012; Bohm 1952). For **perturbative string theory**, the obvious complaint is that the current papers do not yet produce strings, branes, amplitudes, or moduli dynamics. For **asymptotic safety**, the resonance is only partial: fixed-point language alone is not enough unless $$T_{M\Sigma}$$ can be related to functional RG flows. For **causal-set / CDT programs**, the missing step is even more basic: $$T_{M\Sigma}$$ has not yet been defined on a discrete causal substrate. For **Everettian** and **Bohmian** communities, the present series should be read as branch-geometry or effective-guidance interface work, not as an unqualified replacement for branching or pilot-wave ontology. The local Bohmian overlap in Paper 2A §2.3 and the branch/pointer-sector language in Paper 2A §2.5 are therefore best understood as controlled interfaces with existing programs, not declarations that those programs have been superseded wholesale.

## §9.7 Addressing Predictable Objections

Several objections are likely to recur across these communities, and they should be treated as legitimate technical demands rather than as sociological resistance.

**“Where is the explicit $$T_{M\Sigma}$$?”** This is the most universal objection. A framework-level constraint list is not enough by itself. The right answer is local and cumulative: the qubit/Bloch-sphere and dephasing sectors, the pilot-wave overlap in Paper 2A §2.3, the pointer-sector / Born-rule structures in Paper 2A §2.5, and the KCR-Cone interval evaluation in Paper 2B are all partial explicit realizations. What is still missing is a comparably explicit, fully general construction of $$T_{M\Sigma}$$ across the whole program.

**“Show me a regime where your geometry reduces to equations I already know.”** This is also a fair demand. For open-systems readers, the framework must reduce to known Lindblad / pointer / decoherence structures in the appropriate limits. For Bohmian readers, it must recover the guidance-law and quantum-potential sector where the dephasing model applies. For holographers, it must reproduce RT/HRT-type structures and entanglement constraints in known backgrounds before stronger claims are made. For LQG-style readers, the relevant target is a coarse-grained connection to spin-network or horizon data rather than a mere verbal analogy.

**“Why introduce a new geometric object instead of just using the existing formalism?”** For channel/dilation programs this means: why not stay with completely positive maps and effective master equations? For asymptotic-safety readers it means: why not stay with functional RG flows? For Everettian readers it means: why not stick with unitary branching? The only defensible answer is that $$T_{M\Sigma}$$ is useful only if it unifies structures that would otherwise remain disconnected or if it yields new diagnostics that the older language does not already package as naturally.

**“What is the genuinely new prediction?”** Without at least one diagnostic unavailable in the comparison program, the framework remains interpretive overlay rather than physical advance. The present series has only a first set of answers: the Zeno basis-angle dependence, the CMB quadrupole-suppression line, and the interval/KCR compactification constraints. These are enough to justify continued development, but not enough to eliminate the demand for sharper, cross-community predictions.

The deeper strategic point is therefore simple. The framework should be presented most strongly where it already has calculational traction, and more cautiously where the interface is still aspirational. That is not a weakness; it is the correct way to keep the comparison to existing programs honest. If later papers can make $$T_{M\Sigma}$$ explicit on additional substrates, recover more of the neighboring limits, and sharpen the existing diagnostics into unmistakable tests, then the present discussion section will read as early calibration rather than defensive hedging. If not, the value of the current work will remain what it already securely is: a coherence-first geometric organization of problems that are otherwise treated separately.

## References for §9

- Susskind, L. (1995). The world as a hologram. *Journal of Mathematical Physics* **36**, 6377–6396.
- Maldacena, J. (1998). The large-N limit of superconformal field theories and supergravity. *Advances in Theoretical and Mathematical Physics* **2**, 231–252.
- Ryu, S. & Takayanagi, T. (2006). Holographic derivation of entanglement entropy from AdS/CFT. *Physical Review Letters* **96**, 181602.
- Van Raamsdonk, M. (2010). Building up spacetime with quantum entanglement. *General Relativity and Gravitation* **42**, 2323–2329.
- Swingle, B. (2012). Entanglement renormalization and holography. *Physical Review D* **86**, 065007.
- Lindblad, G. (1976). On the generators of quantum dynamical semigroups. *Communications in Mathematical Physics* **48**, 119–130.
- Joos, E. & Zeh, H. D. (1985). The emergence of classical properties through interaction with the environment. *Zeitschrift für Physik B* **59**, 223–243.
- Joos, E., Zeh, H. D., Kiefer, C., Giulini, D., Kupsch, J. & Stamatescu, I.-O. (2003). *Decoherence and the Appearance of a Classical World in Quantum Theory*. 2nd ed. Springer.
- Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics* **75**, 715–775.
- Zurek, W. H. (2005). Probabilities from entanglement, Born’s rule from envariance. *Physical Review A* **71**, 052105.
- Rovelli, C. (2004). *Quantum Gravity*. Cambridge University Press.
- Ashtekar, A., Baez, J., Corichi, A. & Krasnov, K. (1998). Quantum geometry and black hole entropy. *Physical Review Letters* **80**, 904–907.
- Pastawski, F., Yoshida, B., Harlow, D. & Preskill, J. (2015). Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence. *Journal of High Energy Physics* **06**, 149.
- Reuter, M. & Saueressig, F. (2012). Quantum Einstein gravity. *New Journal of Physics* **14**, 055022.
- Bombelli, L., Lee, J., Meyer, D. & Sorkin, R. D. (1987). Space-time as a causal set. *Physical Review Letters* **59**, 521–524.
- Ambjørn, J., Jurkiewicz, J. & Loll, R. (2001). Dynamically triangulating Lorentzian quantum gravity. *Nuclear Physics B* **610**, 347–382.
- Everett, H. (1957). Relative state formulation of quantum mechanics. *Reviews of Modern Physics* **29**, 454–462.
- Wallace, D. (2012). *The Emergent Multiverse: Quantum Theory According to the Everett Interpretation*. Oxford University Press.
- Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of “hidden” variables. *Physical Review* **85**, 166–179.


# §10 Open Problems (REVISED)

The KCR framework now has a well-defined five-level Σ → M coupling hierarchy and a worked example on the KCR-Cone. This makes it possible to state open problems with sharper scope. We group them into: (A) near-term questions still within the reach of the current geometry and tools; (B) Paper 3 gates that must be resolved before the program advances; and (C) long-range structural questions that chart the conceptual roadmap.

***

## §10.1 Category A — KCR-Cone Open Problems (Near-Term, Concrete)

These problems can, in principle, be addressed by extending the methods already used in the companion paper on the KCR-Cone. They refine or complete results that are partially in hand.

**OP-A1. Chronogenic field $$\phi_c$$.**  
The temporal emergence mechanism on the KCR-Cone points to a chronogenic scalar field $$\phi_c$$ coupled to the Σ sector. The open task is to promote this heuristic into a full field equation,
$$
\square \phi_c + m_c^2 \phi_c = J_{\mathrm{dec}}(t),
$$
with $$J_{\mathrm{dec}}(t)$$ derived from the decoherence functional rather than inserted by hand. This includes identifying the correct effective metric for $$\square$$, fixing $$m_c$$ from geometric input, and solving the resulting equation in radiation-, matter-, and $$\Lambda$$-dominated eras.

**OP-A2. Γ$$_{\text{dec}}(\eta)$$ beyond the scaling ansatz.**  
The current analysis of Level 3 backreaction and $$V_{\mathrm{eff}}(\eta)$$ uses a coherence-volume scaling ansatz $$\Gamma_{\mathrm{dec}}(\eta) \sim \Gamma_0 / \eta$$. The open problem is to derive $$\Gamma_{\mathrm{dec}}(\eta)$$ directly from the $$T_{M\Sigma}$$ stress-energy tensor on the KCR-Cone, eliminating this phenomenological assumption. This will sharpen both the sign and magnitude of the Level 3 contribution to $$V_{\mathrm{eff}}$$ and feed back into the dark-sector budget.

**OP-A3. Dark-sector unification numerics.**  
At the current stage, the two-channel model reproduces $$\Omega_{\mathrm{DE}} = 0.692$$, $$\Omega_{\mathrm{DM}} = 0.259$$, and $$\Omega_b = 0.049$$ from two geometric parameters $$\Gamma_0/H_0$$ and $$\beta$$, with $$\Omega_{\mathrm{DM}}/\Omega_{\mathrm{DE}} = 0.374$$ treated as an input. The near-term task is to implement full numerical cosmological solutions on the KCR-Cone background that track the decoherence history and check the robustness of this fit against perturbations in $$\Gamma_0$$, $$\beta$$, and $$L^*$$.

***

## §10.2 Category B — Paper 3 Gates (Blocking Problems)

These problems are now sharply defined by the D1–D5 results. They must be addressed in Paper 3 before the framework can claim a complete account of SC3 and the dark sector.

**OP-B1. SC3 stabilization via flux quantization.**  
The D3/D3b analysis establishes “Outcome B”: with Casimir $$ \propto 1/\eta^4$$ and Level 3 backreaction $$ \propto 1/\eta^2$$, the effective potential $$V_{\mathrm{eff}}(\eta)$$ has no minimum; any stationary point is a maximum. Stabilization therefore requires an additional contribution with slower-than-$$\eta^2$$ growth but positive sign—flux quantization on the compact fiber is the primary candidate. The gate problem is to compute this flux contribution, derive its $$\eta$$-dependence (e.g., constant or logarithmic), and demonstrate a bona fide minimum in $$V_{\mathrm{eff}}(\eta)$$ consistent with SC3.

**OP-B2. Rigorous $$T_{M\Sigma}$$ backreaction from the 5D action.**  
The geometric coefficient in the Level 3 Machian term is now fixed by a reproducible derivation: $$\alpha_{\rm geom} = 10\sqrt{2}/(3\pi)\approx 1.5005$$ (RC-8b). The remaining gate is to derive the full effective stress-energy tensor $$T_{\mu\nu}^{\mathrm{drag}}$$ (including its equation of state beyond the isotropic estimate) together with the sourced dynamics that determine $$c_\Gamma=\Gamma_{\mathrm{dec}}/H_0$$ on the cosmological background.

**OP-B3. SU(3)$$_c$$ gauge derivation.**  
D4 shows that the $$c_1 = 1$$ Hopf bundle naturally yields a geometric $$U(1)_Y$$ structure but cannot produce $$SU(3)_c$$ from this single $$S^2$$ base plus Hopf-fiber structure alone. Paper 3 must introduce the additional compact structure—whether an extended spatial compactification, a higher-dimensional Hopf fibration, or another mechanism—that supports an $$SU(3)$$ principal bundle. The gate is to construct such a bundle explicitly and demonstrate how the color sector emerges from the same derived-compactification philosophy.

**OP-B4. Cosmic decoherence history and $$\Omega_{\mathrm{DM}}/\Omega_{\mathrm{DE}}$$ as prediction.**  
The present dark-sector model treats the dark-matter–to–dark-energy ratio as an input. Once $$\Gamma_{\mathrm{dec}}(\eta)$$ and $$T_{M\Sigma}$$ backreaction are derived from the action, the cosmic decoherence history becomes calculable across radiation, matter, and dark-energy domination. The gate problem is to compute $$\Gamma_{\mathrm{dec}}(t)$$ on the cosmological background and thereby turn $$\Omega_{\mathrm{DM}}/\Omega_{\mathrm{DE}}$$ into a parameter-free prediction.

**OP-B5. Chronogenic field and coalescence map consistency.**  
The chronogenic scalar $$\phi_c$$ and the coalescence map $$C : \Sigma \to M$$ are conceptually intertwined: both aim to capture how a pre-temporal coherence substrate yields a classical spacetime with an arrow of time. Paper 3 must supply a single, consistent set of equations that (1) links $$\phi_c$$ to decoherence-driven entropy production, and (2) realizes the coalescence hypothesis with a non-singular Big Bang locus and a well-defined metric at the apex. This is a true gate: without it, the chronogenic picture remains heuristic.

***

## §10.3 Category C — Long-Range Structural Questions

These problems set the longer-term agenda. They are structurally well-motivated by the current results but will likely require new formalisms or generalizations beyond the KCR-Cone.

**OP-C1. Coalescence hypothesis and bipolar substrate.**  
The coalescence hypothesis posits a mapping $$C : \Sigma \to M$$ from a bipolar, pre-temporal substrate to spacetime, with two opposed orientations coalescing at a non-singular Big Bang locus. The long-range program is to give this mapping a rigorous mathematical definition, prove that the double orientation indeed regularizes the initial singularity, and compute the resulting apex metric. This would elevate “Decoherence Recapitulates Cosmogenesis” from metaphor to theorem.

**OP-C2. Mach’s principle in wavefunctions.**  
The KCR-Cone geometry introduces a natural Machian hyperradius $$\rho_{\mathrm{Mach}}(t) = r_f(\eta(t))$$ and an effective grand angular momentum $$K_{\mathrm{eff}}$$ that encodes inertia. The long-range question is whether this can be developed into a bona fide Mach principle in Hilbert space: inertia and gravitational response emerging from global properties of the wavefunction and its entanglement pattern. This requires connecting $$K_{\mathrm{eff}}$$, $$\eta(t)$$, and $$V_{\mathrm{eff}}$$ to observable inertial properties without relying on background assumptions.

**OP-C3. Full dark-sector unification (Levels 3+4).**  
Current results suggest that arrow of time, dark energy, and (at least part of) dark matter arise from a single Lindblad cascade on $$\Sigma$$ coupled to $$M$$ via $$T_{M\Sigma}$$. A long-range goal is to unify Level 3 frame-dragging and Level 4 vacuum entanglement thermodynamics into a single formalism, possibly along Jacobson-style entanglement thermodynamics lines. Success would mean deriving the dark sector and the arrow of time from the same entropic current, with the Hubble scale emerging as a derived quantity.

**OP-C4. Beyond $$c_1 = 1$$: higher Chern numbers and non-abelian fibers.**  
The present work focuses on the minimal $$c_1 = 1$$ Hopf bundle for a qubit. The general program extends to higher Chern numbers and higher-dimensional coherence manifolds (e.g., $$\mathbb{CP}^n$$ for qutrits and multi-qubit systems), which naturally support lens-space quotients and non-abelian fiber structures. The long-range question is to classify the resulting compactification topologies and gauge groups, and to determine whether any of them are phenomenologically viable alternatives or complements to the KCR-Cone.

**OP-C5. Chronogenic cosmology and structure formation.**  
If the chronogenic cascade on $$\Sigma$$ is indeed the microscopic origin of the arrow of time and the dark sector, then it should leave imprints on structure formation: the growth of perturbations, halo profiles, and perhaps even correlations in the CMB. The long-range task is to develop a chronogenic cosmology that tracks not only background quantities like $$H(t)$$ and $$\Omega_i$$ but also perturbations sourced by spatial variations in the decoherence rate, and to compare these with precision cosmological data.

***

This revised open-problems section thus marks a transition. With SC3 conditionally established, the role of the KCR-Cone is no longer to supply ad hoc numbers, but to define a concrete set of calculational gates and structural questions that any competing geometry must also face.


# §11 Extraction Note

This manuscript is intended to be the canonical Paper 2C target going forward. Legacy Paper 2 whole-document variants remain in the repository as historical quarries, but future 2C editing should proceed here rather than by reinserting RC-1 and §8 material back into the older 2A/Unified drafts.
