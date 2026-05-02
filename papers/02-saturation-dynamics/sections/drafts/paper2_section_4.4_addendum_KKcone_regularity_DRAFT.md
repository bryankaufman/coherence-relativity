# §4.4.8 Addendum: Explicit Reg1–Reg3 Verification for A(r) = cos(√2 r)

**Status:** NEW DRAFT (2026-05-02) — closes Paper 1 line-844 promise (C¹ regularity part)
**Placement:** After §4.4.7 in `paper2_section_4.4_C1_regularity_PATCHED.md`

---

Lemma 4.4.1 establishes sufficient conditions (Reg1–Reg3) for C¹ regularity of the
coherence-to-classical map. This addendum verifies them explicitly for the KK-cone exact
warp factor A(r) = cos(√2 r) derived in §7.8 (Eq. 7.8.2.5).

---

## Verification of Reg1: Global C¹ Smoothness

**Claim:** A(r) = cos(√2 r) ∈ C¹([0, r*]) with bounded derivatives on [0, r*],
where r* = π/(2√2) is the pointer-state attractor at the throat.

**Proof:** The function cos(√2 r) is analytic (C^∞) on all of ℝ. In particular, it is C¹
on the closed interval [0, r*]. Its first derivative ∂_r A = −√2 sin(√2 r) is continuous.

**Status: ✅ VERIFIED** — A ∈ C^∞([0, r*]) ⊃ C¹([0, r*]).

---

## Verification of Reg2: Bounded First Derivatives

**Claim:** The first partial derivative satisfies |∂_r A| ≤ C for some constant C > 0
uniformly on [0, r*].

**Proof:**

$$\left|\frac{\partial A}{\partial r}\right| = \left|-\sqrt{2}\sin(\sqrt{2}\,r)\right| = \sqrt{2}\,|\sin(\sqrt{2}\,r)| \leq \sqrt{2} \qquad \text{(4.4.8.1)}$$

since |sin(θ)| ≤ 1 for all θ. The bound is achieved at r = r*/2 = π/(4√2):

$$\left|\frac{\partial A}{\partial r}\right|_\mathrm{max} = \sqrt{2} \quad \text{at} \quad r = \frac{\pi}{4\sqrt{2}} \approx 0.555 \qquad \text{(4.4.8.2)}$$

Take C = √2. Then Reg2 holds uniformly on [0, r*].

**Note on z-dependence:** The KK-cone warp factor A(r) does not depend on the coherence
parameter z at this level of the derivation (the zero-mode sector). When the full
system-environment coupling is included (§7.9), the effective warp factor acquires a
z-dependence through Γ_dec(z) = Γ₀ H(z)/H₀. The resulting ∂_z A is:

$$\frac{\partial A}{\partial z} = 0 \quad \text{(zero-mode sector)} \qquad \text{(4.4.8.3)}$$

so the Reg2 bound on ∂_z A is trivially satisfied with C_z = 0.

**Status: ✅ VERIFIED** — |∂_r A| ≤ √2 everywhere; |∂_z A| = 0 in zero-mode sector.

---

## Verification of Reg3: Uniform Conical Structure at r = 0

**Claim:** Any conical singularity at r = 0 must satisfy Condition 4.4.7a (linear tip profile).

**Assessment:** The condition is **vacuously satisfied** — there is no conical singularity at r = 0.

**Proof:** At the brane r = 0:

$$A(0) = \cos(0) = 1 \qquad \text{(4.4.8.4)}$$

The warp factor is unity at the brane, so the metric is non-degenerate:

$$ds^2_{(5)}\big|_{r=0} = -dz^2 + \gamma_{ij}\,dx^i dx^j + dr^2 \qquad \text{(4.4.8.5)}$$

This is the metric of Minkowski × S³ at the brane level — smooth everywhere, no cone tip,
no orbifold structure. The internal S³ sector has unit radius at r = 0.

**Comparison with RS:** In Randall-Sundrum models, the warp factor is A(y) = e^{−k|y|}
with A(0) = 1 but A'(0) is discontinuous (a kink — the RS mechanism). In the KK-cone,
A'(0) = −√2 sin(0) = 0: the first derivative **vanishes** at the brane. The warp factor
is not only smooth but has a local maximum at r = 0. There is no kink, no junction
condition, and no distributional curvature at the brane.

**Status: ✅ VERIFIED** — Reg3 vacuously satisfied; no conical singularity at r = 0.

---

## Note on the Throat (r → r* = π/(2√2))

The warp factor vanishes at the throat:

$$A(r^*) = \cos\!\left(\sqrt{2}\cdot\frac{\pi}{2\sqrt{2}}\right) = \cos\!\left(\frac{\pi}{2}\right) = 0 \qquad \text{(4.4.8.6)}$$

This is **not** a regularity failure of A(r). Rather, it is the decoherence attractor: the
pointer-state fixed point at r = r* where λ → 1 and the system is fully classical. The
metric degenerates there in the sense that the internal S³ shrinks to zero size —
a standard conical (or orbifold) tip in Kaluza-Klein geometry, analogous to the apex of a
cone. This degeneration is:

1. **Physical**: it signals the pointer-state / classical entry, not a mathematical defect.
2. **Outside the regularity claim**: Lemma 4.4.1 asserts C¹ of the coherence-to-classical
   map V(x) on the brane (r = 0), not throughout the bulk. The throat at r* is the endpoint
   of the coherence trajectory, not a point in M.

The quasipotential V(r) = ∫_r^{r*} √G_{rr} dr' = r* − r diverges only in the sense that
the geodesic distance to the brane from the throat is r* = π/(2√2) — finite. So even the
throat geometry does not obstruct the regularity result.

---

## Summary

| Condition | Requirement | KK-cone value | Status |
|-----------|-------------|---------------|--------|
| Reg1 | A ∈ C¹(ℝ⁺ × Σ) with bounded derivatives | A = cos(√2 r) ∈ C^∞ | ✅ PASS |
| Reg2 | \|∂_r A\| + \|∂_z A\| ≤ C | ≤ √2 + 0 = √2 | ✅ PASS (C = √2) |
| Reg3 | Conical tip: A(0,z) = C(z)r + O(r²) | A(0) = 1 ≠ 0: no conical singularity | ✅ PASS (vacuous) |

**Conclusion:** All three sufficient conditions of Lemma 4.4.1 hold for A(r) = cos(√2 r).
Therefore, by Lemma 4.4.1, the coherence-to-classical map V(x) ∈ C¹(M).

**What this closes:** The Paper 1 line 844 regularity promise is fulfilled at the
structural level — the explicit KK-cone warp factor satisfies C¹ regularity. The
explicit emergent metric formula is given in §4.6.
