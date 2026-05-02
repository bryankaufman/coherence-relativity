# §4.6 Explicit Form of the Emergent Metric and Embedding Geometry

**Status:** NEW DRAFT (2026-05-02) — closes Paper 1 line-844 promise (emergent metric part)
**Placement:** After §4.5 (C¹ vs RS comparison) in Paper 2B

---

## §4.6.1 Setup

Paper 1 (line 844) defers two items to Paper 2:
1. C¹ regularity — verified in §4.4 and §4.4.8
2. **The explicit form of the emergent metric and embedding geometry** — this section

The emergent spacetime metric on M is the metric induced on the brane at r = 0 by the
5D KK-cone geometry. This is the concrete answer to the question: in what sense does
classical Minkowski spacetime *emerge* from the quantum geometry on M × Σ?

---

## §4.6.2 Induced Metric at the Brane

### State map and Fubini-Study metric

From §7.2 (Eq. 7.2.6), the Fubini-Study metric on M × Σ in the zero-mode sector is:

$$G_{\mu\nu}(r) = f_0(r)^2\,G_{\mu\nu}^{(e_0)} \qquad \text{(4.6.1)}$$

where:
- f₀(r) is the normalized KK zero-mode profile
- G^{(e₀)}_{μν} is the Fubini-Study metric of the graviton polarization state |e₀⟩

**Convention note (flagged in review):** Two normalizations are in use and must not
be conflated:

**(a) Unit-profile convention:** Define f̃₀(r) = ψ₀(r)/ψ₀(0) so that f̃₀(0) ≡ 1 by
definition. Then G_{μν}(r) = ψ₀(0)² f̃₀(r)² G^{(e₀)}_{μν}, and f̃₀(0) = 1.

**(b) Normalized-eigenfunction convention (RC-8b):** The zero-mode profile ψ₀(r) is
normalized over the interval [0, r*]:

$$\int_0^{r^*} \psi_0(r)^2\,dr = 1 \qquad \text{(4.6.2)}$$

For ψ₀(r) ∝ A(r)^{3/2} = cos^{3/2}(√2 r) (the graviton zero mode on the KK-cone,
from Paper 2B §5–6), the normalization constant is N₀² = I₆/I₂ where:

$$I_n = \int_0^{r^*} A(r)^n\,dr, \quad r^* = \frac{\pi}{2\sqrt{2}} \qquad \text{(4.6.3)}$$

From RC-8b (omnibus #23): N₀² = I₆/I₂ = 16√2/(3π) ≈ 2.404. Therefore:

$$f_0(0) = \psi_0(0) = N_0 = \sqrt{\frac{16\sqrt{2}}{3\pi}} \approx 1.550 \neq 1 \qquad \text{(4.6.4)}$$

**In this paper we use convention (b) throughout.** The factor f₀(0)² = N₀² is not 1
but is absorbed into the 4D Newton constant (§4.6.3 below). Any §7.2 equation written
with "f₀(0) = 1" should be understood as using convention (a), with N₀ pulled out.

---

## §4.6.3 The Emergent Metric: G^em = N₀² η_{μν}

### Fubini-Study pullback to M

The induced (emergent) metric on M is obtained by evaluating Eq. (4.6.1) at r = 0:

$$G^\mathrm{em}_{\mu\nu} := G_{\mu\nu}\big|_{r=0} = f_0(0)^2\,G_{\mu\nu}^{(e_0)} = N_0^2\,G_{\mu\nu}^{(e_0)} \qquad \text{(4.6.5)}$$

### Evaluating G^{(e₀)}_{μν}: symmetry argument

The graviton zero-mode polarization state |e₀⟩ on Minkowski × S³ has Fubini-Study metric:

$$G_{\mu\nu}^{(e_0)} = \eta_{\mu\nu} \qquad \text{(4.6.6)}$$

**Argument:** The brane geometry at r = 0 has exact Poincaré symmetry ISO(1,3) in the
(z, x^i) directions. The Fubini-Study metric G^{(e₀)}_{μν} is constructed from the
expectation values ⟨∂_μ e₀|∂_ν e₀⟩ of the graviton polarization state. By Poincaré
invariance, this matrix must be proportional to η_{μν} — the only ISO(1,3)-invariant
symmetric rank-2 tensor. The overall proportionality constant is fixed to 1 by the
normalization of the graviton 2-point function (in units where M_5 = 1).

**Caveat (Paper 3 grounding):** The assertion G^{(e₀)}_{μν} = η_{μν} follows at the
abstract level from Poincaré symmetry plus the normalization convention. The explicit
field-theoretic derivation — identifying |e₀⟩ as the correct zero mode of the 5D
graviton on the specific Minkowski × S³ background — requires specifying the field
content on the interval, which is Paper 3 Axiom B (interface contract P3-H3/P3-H4).
The structural result Eq. (4.6.6) holds independently of Axiom B; the grounding does not.

### Result

Combining Eqs. (4.6.5)–(4.6.6):

$$\boxed{G^\mathrm{em}_{\mu\nu} = N_0^2\,\eta_{\mu\nu}, \quad N_0^2 = \frac{16\sqrt{2}}{3\pi} \approx 2.404} \qquad \text{(4.6.7)}$$

The emergent spacetime metric is flat Minkowski, rescaled by the zero-mode normalization N₀².

---

## §4.6.4 Absorption into 4D Newton Constant

The factor N₀² is not a physical observable — it is absorbed into the 4D Newton constant
via the standard Kaluza-Klein dimensional reduction. From RC-8b:

$$\frac{1}{16\pi G_4} = \frac{N_0^2\,I_2}{16\pi G_5} \qquad \text{(4.6.8)}$$

where I₂ = ∫₀^{r*} A(r)² dr = π/(4√2) (the volume integral of the warp factor squared).
Therefore:

$$G_4 = \frac{G_5}{N_0^2\,I_2} = \frac{G_5}{\frac{16\sqrt{2}}{3\pi}\cdot\frac{\pi}{4\sqrt{2}}} = \frac{G_5}{\frac{4}{3}} = \frac{3\,G_5}{4} \qquad \text{(4.6.9)}$$

**Interpretation:** The 4D Newton constant G₄ is determined by the 5D Newton constant G₅
and the geometry of the extra dimension (r* and A(r)). In units where G₅ = 1, the
prediction is G₄ = 3/4 — a numerical consequence of A(r) = cos(√2 r) and the
KK-cone topology. The emergent 4D physics is parameterized by G₄, not by G₅ or N₀²
individually.

After substitution into the Einstein-Hilbert action in 4D, the coefficient N₀² cancels
against 1/(16πG₄) from the normalization, and the physical 4D metric is:

$$g^\mathrm{phys}_{\mu\nu} = G^\mathrm{em}_{\mu\nu}/N_0^2 = \eta_{\mu\nu} \qquad \text{(4.6.10)}$$

The emergent spacetime geometry is Minkowski, as expected for the brane at r = 0.

---

## §4.6.5 Embedding Geometry

The embedding map ι: M → M × Σ is simply the brane inclusion at r = 0:

$$\iota: (z, x^i) \longmapsto (z, x^i, r=0) \qquad \text{(4.6.11)}$$

The pullback of the 5D metric along ι reproduces Eq. (4.6.7):

$$\iota^*\bigl(G_{AB}\bigr) = G^\mathrm{em}_{\mu\nu} = N_0^2\,\eta_{\mu\nu} \qquad \text{(4.6.12)}$$

The normal direction to the brane is ∂/∂r, with induced unit normal n^A = δ^A_r (since
G_{rr} = 1). The extrinsic curvature of the brane is:

$$K_{\mu\nu} = -\frac{1}{2}\mathcal{L}_n G_{\mu\nu}\big|_{r=0} = \frac{A'(0)}{A(0)}\,G_{\mu\nu}^{(e_0)}\,\eta_{\mu\nu} = 0 \qquad \text{(4.6.13)}$$

since A'(0) = −√2 sin(0) = 0 (the warp factor has a critical point at the brane). The
brane is a **minimal surface** in M × Σ: K_{μν} = 0. This is the geometric statement
that the classical (brane) observers are not driven toward the bulk by any curvature force —
they sit at the maximum of A(r), which is a stable equilibrium in the r direction.

**Comparison with RS:** In the RS1 model, K_{μν} ≠ 0 at the brane (there is a nonzero
extrinsic curvature sourced by the brane tension). In the KK-cone, the brane is extremal
(K = 0) and sits at a warp-factor maximum — both consequences of the derived (not assumed)
compactification.

---

## §4.6.6 Summary and Status

| Result | Equation | Status |
|--------|----------|--------|
| Induced metric at brane | G^em = N₀² η_{μν} | ✅ DERIVED |
| N₀² = 16√2/(3π) from RC-8b | (4.6.4) | ✅ FROM PRIOR RESULT |
| G^{(e₀)} = η_{μν} (symmetry argument) | (4.6.6) | ✅ DERIVED (abstract level) |
| G^{(e₀)} = η_{μν} (field-theoretic grounding) | — | ⚠️ DEFERRED to Paper 3 Axiom B |
| N₀² absorbed into G₄ = 3G₅/4 | (4.6.9) | ✅ DERIVED from RC-8b |
| g^phys = η_{μν} in physical units | (4.6.10) | ✅ DERIVED |
| Embedding map ι: M → M×Σ at r=0 | (4.6.11) | ✅ DEFINED |
| Brane is minimal (K_{μν} = 0) | (4.6.13) | ✅ DERIVED (A'(0) = 0) |

**What this closes:** Paper 1 line 844 promise — "the explicit form of the emergent metric
and embedding geometry are developed in Paper 2." The structural result (flat Minkowski
emerges at r=0, brane is minimal, G₄ is determined) is fully delivered. The field-theoretic
grounding of G^{(e₀)} = η_{μν} is deferred to Paper 3, consistent with the architectural
split rule:

> *Paper 2B delivers the structural statement; Paper 3 delivers the field-theoretic grounding.*

This pattern applies identically to line 844 (emergent metric) and lines 1034/1056
(holographic connections).

---

## Cross-references

- §4.4.8: Explicit Reg1–Reg3 verification → establishes V ∈ C¹(M)
- §4.5: RS comparison → established that regularity is a prediction, not a tuned input
- §7.2.6: Fubini-Study metric components on KK-cone → G_{μν}(r) = f₀(r)² G^(e₀)_{μν}
- §7.8: A(r) = cos(√2 r) derivation from Fubini-Study Laplacian eigenvalue k²=2
- RC-8b (omnibus #23): N₀² = 16√2/(3π), I₂ = π/(4√2), α_geom = 10√2/(3π)
- Paper 3 Axiom B (P3-H3/P3-H4): field content on interval → grounds G^{(e₀)} = η_{μν}
- Paper 1 line 844: "explicit form of the emergent metric... deferred to Paper 2"
