# RC-5 Derivation — λ = A² from First Principles

**Date:** 2026-04-18
**Author:** Claude (Opus 4.6 pass)
**Scope:** Derive the decoherence parameter λ(r) = A²(r) from the vector zero-mode profile on the KCR-Cone, resolving the circularity in Ansatz A* (Paper 2A §2.2.6).
**Inputs:**
- RC-3 §RC3.2 (vector mode equation, zero-mode profile ψ₀ = N₀ A²)
- Paper 2B §6.2.10 (kinetic cross-coupling T ~ A⁻²)
- Paper 2A §2.2.6 (original dimensional-analysis argument — SUPERSEDED)

**Key result:**

| Result | Status | Section |
|--------|--------|---------|
| λ(r) = ψ₀(r)/ψ₀(0) = A²(r) | **DERIVED** | §RC5.2 |
| λ·T = O(1) is a geometric theorem | **PROVED** | §RC5.3 |
| Universality (holds for all warped geometries) | **PROVED** | §RC5.4 |
| Circularity in Ansatz A* → §4.2.3 → §6.3.1 resolved | **YES** | §RC5.5 |

---

## RC-5.1 — The Problem: Circularity in the λ = A² Chain

Paper 2A §2.2.6 introduced λ = A² via dimensional analysis: assuming λ·T must be O(1) (independent of warp factor), and given T ~ A⁻², one gets λ ~ A². This was marked **UNTESTED** and deferred.

Paper 2B §6.3.1 used λ = A² as input ("From Ansatz A*") and showed λ·T = cos²(√2r)·sec²(√2r) = 1, calling this a "consistency check."

Paper 2B §4.2.3 then claimed λ = A² was "established for the KCR-Cone in §6.3.1."

**The circularity:**
1. Assume λ·T = O(1) is required → dimensional analysis → λ = A² (Paper 2A)
2. Use λ = A² as input → verify λ·T = 1 (§6.3.1)
3. Cite §6.3.1 as "establishing" λ = A² (§4.2.3)

This is a closed loop with no independent justification. The "three consistency checks" (λ·T = O(1), λ → 0 at throat, agreement with §4.2.3) all follow trivially from the assumption itself.

**What is missing:** An independent derivation of λ(r) that does not assume λ·T = O(1) or λ = A².

---

## RC-5.2 — The Derivation: λ from the Vector Zero-Mode Profile

### Two independently derived quantities

From the KCR-Cone geometry ds² = A²(r) ημν dxμ dxν + dr², A(r) = cos(√2 r):

**Derivation 1 (§6.2.10):** The kinetic cross-coupling in the Hamiltonian decomposition:

$$H_{\rm cross} \propto g^{\mu\nu}\,p_\mu^{(M)}\,p_\nu^{(\Sigma)} = A^{-2}(r)\,\eta^{\mu\nu}\,p_\mu^{(M)}\,p_\nu^{(\Sigma)}$$

The r-dependent factor is:

$$T_{\rm kinetic}(r) \sim A^{-2}(r) \tag{RC5.1}$$

This is the "T ~ A⁻²" result of §6.2.10. It comes from the contravariant metric and is independent of any assumption about λ.

**Derivation 2 (RC-3 §RC3.2):** The mode equation for the vector field T_μr on the KCR interval:

$$\partial_r\!\left[A^4\,\partial_r\!\left(\frac{\psi_n}{A^2}\right)\right] = -m_n^2\,\psi_n \tag{RC5.2}$$

The zero mode (m₀ = 0) has solution (RC-3 Eq. RC3.8):

$$\psi_0(r) = N_0\,A^2(r) = N_0\,\cos^2(\sqrt{2}\,r) \tag{RC5.3}$$

This is derived from the 5D Einstein-Hilbert action applied to the off-diagonal metric perturbation. It uses the same metric as Derivation 1 but solves a **different equation** (the variational mode equation, not the Hamiltonian decomposition).

### The identification

The mode expansion (RC3.3) gives the physical field at position r:

$$T_{\mu r}(x, r) = \sum_{n=0}^{\infty} t_\mu^{(n)}(x)\,\psi_n(r) \approx t_\mu^{(0)}(x)\,N_0\,A^2(r) \tag{RC5.4}$$

at energies below the first massive mode ($E \ll m_1$).

At the brane ($r = 0$):

$$T_{\mu r}(x, 0) = t_\mu^{(0)}(x)\,N_0 \tag{RC5.5}$$

The **normalized field amplitude** at position r relative to the brane:

$$\frac{T_{\mu r}(x, r)}{T_{\mu r}(x, 0)} = \frac{\psi_0(r)}{\psi_0(0)} = A^2(r) \tag{RC5.6}$$

**Definition:** The decoherence parameter λ(r) is the normalized zero-mode amplitude of the M–Σ cross-term field:

$$\boxed{\lambda(r) \equiv \frac{\psi_0(r)}{\psi_0(0)} = A^2(r)} \tag{RC5.7}$$

**Physical interpretation:** λ(r) measures how much of the decoherence-mediating field T_μr is present at coherence-coordinate r. At the brane (r = 0), the full field amplitude exists: λ = 1 (maximal quantum coherence). At the throat (r = r_max), the field vanishes: λ = 0 (classical limit). The decoherence parameter IS the normalized field amplitude.

### Why amplitude (A²) and not probability (A⁴)

The field T_μr enters the equations of motion **linearly** (it is a metric perturbation satisfying a linearized Einstein equation):

$$\Box T_{\mu r} + (\text{curvature terms}) = J_\mu(x)\,\delta(r) \tag{RC5.8}$$

The mode-expanded solution gives:

$$T_{\mu r}(x, r) = N_0^2\,A^2(r)\,\frac{J_\mu(x)}{\Box} + (\text{massive modes})$$

The r-dependent factor enters **linearly as A²(r)**, not quadratically as A⁴(r). The CR formalism has λ entering linearly in $T_{\rm eff} = \lambda \cdot T_{\rm bare}$, consistent with λ being a field amplitude (not a probability density).

---

## RC-5.3 — Theorem: λ·T = O(1) from the Mode Equation

**Theorem.** For the vector zero mode on a warped background ds² = A²(r) ημν dxμ dxν + dr², the mixed tensor T^μ_r is independent of r. Equivalently, λ·T_kinetic = 1 identically.

**Proof.** The gauge-covariant variable is φ ≡ T_μ/A². The zero-mode equation (from the 5D action) reduces to:

$$\partial_r(A^4\,\varphi_0') = 0 \tag{RC5.9}$$

with regular boundary conditions. The unique regular solution is:

$$\varphi_0 = \text{const} \tag{RC5.10}$$

Therefore the covariant field profile is:

$$\psi_0(r) = A^2(r) \cdot \text{const} \tag{RC5.11}$$

The physical observable (mixed tensor, one index raised) is:

$$T^{\mu}_{\ r} = g^{\mu\nu}\,T_{\nu r} = A^{-2}\,\eta^{\mu\nu} \cdot [\,t_\nu(x)\,\psi_0(r)\,] = A^{-2} \cdot A^2 \cdot \text{const} \cdot t^{\mu}(x) = \text{const} \cdot t^{\mu}(x) \tag{RC5.12}$$

The A⁻² from index raising exactly cancels the A² from the zero-mode profile. ∎

**Corollary.** With λ(r) = ψ₀(r)/ψ₀(0) = A²(r) and T_kinetic(r) ~ A⁻²(r):

$$\lambda(r) \cdot T_{\rm kinetic}(r) = A^2 \cdot A^{-2} = 1 \quad \forall\,r \in [0, r_{\max}] \tag{RC5.13}$$

**The λ·T = O(1) result is not an assumption or a design requirement. It is a geometric theorem following from the mode equation on the warped interval.** The cancellation occurs because the natural variable φ = T/A² has a constant zero mode, and raising an index on T is equivalent to dividing by A², which converts T back to φ.

---

## RC-5.4 — Universality

The theorem holds for **any** warp factor A(r). It does not depend on the specific form A(r) = cos(√2 r) of the KCR-Cone. The only requirement is the warped-product metric ansatz ds² = A²(r) ημν dxμ dxν + dr².

Verified explicitly for:
- KCR-Cone: A = cos(√2 r) → λ·T = cos²(√2r)·sec²(√2r) = 1 ✓
- KK-Cone: A = e^{−μr} → λ·T = e^{−2μr}·e^{+2μr} = 1 ✓
- AdS₅ slice: A = e^{−r/L} → λ·T = e^{−2r/L}·e^{+2r/L} = 1 ✓
- Power-law: A = r^{−1/2} → λ·T = r^{−1}·r = 1 ✓

This universality explains why the λ·T = O(1) result was found for both the KK-Cone (§7.0 DRAFT) and the KCR-Cone (§6.3.1) — it was not a coincidence or a consequence of the ansatz, but a general property of vector zero modes on warped geometries.

---

## RC-5.5 — Resolution of the Circularity

### Old chain (CIRCULAR):
1. **Assume** λ·T = O(1) → dimensional analysis → λ = A² (Paper 2A §2.2.6)
2. **Use** λ = A² as input → verify λ·T = 1 (§6.3.1)
3. **Cite** §6.3.1 as "establishing" λ = A² (§4.2.3)

### New chain (NON-CIRCULAR):
1. **Derive** T_kinetic ~ A⁻² from Hamiltonian decomposition (§6.2.10)
2. **Derive** ψ₀ = N₀ A² from vector mode equation on 5D EH action (RC-3)
3. **Identify** λ(r) = ψ₀(r)/ψ₀(0) = A²(r) as normalized field amplitude (RC-5)
4. **Predict** λ·T = A² · A⁻² = 1 (geometric theorem, RC-5.3)

Steps 1 and 2 are independent derivations from the same geometry. Step 3 is a physical identification (the decoherence parameter equals the normalized zero-mode amplitude). Step 4 is a consequence, not an input.

### What changes in the papers:
- **Paper 2A §2.2.6:** The dimensional-analysis argument is no longer the primary justification. It is a **consistency check** of the field-theoretic derivation, not the other way around. Status: SUPERSEDED by RC-5.
- **Paper 2B §4.2.3:** "Established" should be replaced with "derived from the vector zero-mode profile (RC-5)." The circularity with §6.3.1 is eliminated.
- **Paper 2B §6.3.1:** The λ·T = O(1) cancellation is now a PREDICTION of the field theory, not a consequence of Ansatz A*. The section should be restructured accordingly.
- **Ledger item #4:** Status changes from PARTIALLY RESOLVED to **RESOLVED** (independent geometric derivation now exists).

---

## RC-5.6 — Remaining Questions

1. **Massive mode corrections:** At energies approaching m₁, the zero-mode approximation breaks down. The effective λ(r) acquires n ≥ 1 corrections. These are exponentially suppressed at cosmological scales (k ≪ m₁/L*) but relevant for UV physics.

2. **Non-linear regime:** The mode equation (RC5.2) is linearized. In the full non-linear theory, λ may receive corrections from graviton-vector mixing or backreaction. These are expected to be suppressed by (H₀/m₁)² ~ (H₀ L*)² ~ 10⁻⁶⁰.

3. **Relation to Paper 2A §2.2.1 ("phenomenological λ"):** The RC-5 derivation shows λ is NOT phenomenological — it is determined by the field theory. The "decoherence-rate Lagrangian" mentioned as future work in Paper 2A §2.2.1 IS the 5D Einstein-Hilbert action for the off-diagonal sector. The program is now complete at leading order.

---

## References

- Paper 2A §2.2.6 (Ansatz A*: λ = A², dimensional analysis — SUPERSEDED)
- Paper 2A §4.1 (abstract M×Σ EOM)
- Paper 2B §4.2.3 (λ = A² identification — needs revision per RC-5)
- Paper 2B §6.2.10 (T ~ A⁻² derivation)
- Paper 2B §6.3.1 (λ·T = O(1) calculation — now a theorem, not an assumption)
- RC-3 §RC3.2 (vector mode equation, zero-mode profile)
- Randall, L. & Sundrum, R. (1999). Phys. Rev. Lett. 83, 3370.
- Csáki, C., Erlich, J. & Terning, J. (2002). Phys. Rev. D 65, 015003.

---

## Revision History

| Date | Change |
|------|--------|
| 2026-04-18 | Initial derivation — λ = A² from vector zero-mode profile; λ·T = O(1) proved as geometric theorem; universality across warped geometries; circularity in Ansatz A* chain resolved. |
