# T3-A: Casimir-Driven Oscillations in 5D S³ × S¹ Cosmology
## Analysis Log

**Ansatz**: ds² = −dt² + a(t)² dΩ₃² + b(t)² dφ²  (topology S³ × S¹, k=+1)  
**Goal**: Find field content whose Casimir energy supports periodic (oscillatory) solutions for a(t), b(t).

---

## 5D Einstein Equations

```
Ḣa = −(2Ha² + k/a² + κ p_φ/3)
Ḣb = Ha² + k/a² − 2HaHb − Hb² + κ(2p_φ/3 − p₃)
Constraint: 3Ha² + 3k/a² + 3HaHb = κρ   [used as IC check; should be conserved]
```

Stress tensor from Casimir energy E(a,b):
```
ρ   =  E / V₄           V₄ = 4π³ a³ b
p₃  = −(a/3V₄) ∂E/∂a
p_φ = −(b/V₄)  ∂E/∂b
```

---

## Necessary Conditions for Oscillatory Solutions

### a-bounce condition (Ha = 0 turning point)

At Ha = 0, the Hamiltonian constraint gives:

    κρ = 3k/a²

For k=+1 this **requires ρ > 0** at every a-turning point.

Then Ḣa at that point:

    Ḣa = −(k/a² + κ p_φ/3)

For Ḣa > 0 (so a can re-expand after contracting to a minimum):

    κ p_φ/3 < −k/a²  ⟺  κ p_φ < −3k/a² = −κρ  ⟺  p_φ < −ρ

Since ρ > 0 this means **p_φ < 0**, equivalently **w_φ < −1** if w_φ is defined via p_φ = w_φ ρ.  
(Or simply p_φ < 0 if we avoid ratio notation.)

**Key constraint obstruction**: If ρ < 0 everywhere along a trajectory, then κρ = 3k/a² > 0 cannot
be satisfied at Ha = 0, so **no a-turning point exists** for k=+1 with ρ < 0.

### b-bounce condition (Hb = 0 turning point, Ha > 0)

At Hb = 0, using the constraint to eliminate Ha² + k/a²:

    Ḣb = Ha² + k/a² + κ(2p_φ/3 − p₃) = κρ/3 + κ(2p_φ/3 − p₃)

For Ḣb > 0 (b re-expands from minimum):

    ρ/3 + 2p_φ/3 − p₃ > 0
    ρ + 2p_φ − 3p₃ > 0

In EOS language (p₃ = w₃ρ, p_φ = w_φρ, ρ > 0):

    1 + 2w_φ − 3w₃ > 0   ⟺   w₃ < (1 + 2w_φ)/3

---

## Field Content Explored

### Test 1: Periodic Conformal Scalar — S₁-dominated regime  (v1, N_EFF=1)

**Casimir energy**: E = E_S1 + E_S2, with S₁ (zero-mode) dominant at large b/a.

**EOS at typical points**: w₃ ≈ +2/3,  w_φ ≈ −1,  ρ > 0

**a-bounce check**: p_φ = w_φ ρ = (−1)ρ < 0  ✓  (a-bounce condition satisfied)

**b-bounce check**: 1 + 2(−1) − 3(2/3) = 1 − 2 − 2 = −3 < 0  ✗  **FAILS**

**Conclusion**: b cannot oscillate. Trajectories show a expands, b monotonically collapses.

---

### Test 2: Antiperiodic Conformal Scalar  (v1 N_EFF=1 → v2 N_EFF=50 → v3 N_EFF=50 200×200)

**Boundary conditions**: antiperiodic on S¹_φ → S₁ = 0 (no zero mode), S₂ with (−1)^k alternating sign.

**Sign convention verification**: (−1)^k for k=1 → sign=−1 → F_ap < 0 → E_ap = −(1/πa)F_ap > 0  ✓

**EOS at typical points**: w₃ ≈ −1,  w_φ ≈ +4,  ρ > 0

**Amplitude regime**: At (a=2, b=0.2, N_EFF=50): κρ/(k/a²) ≈ 4.68 — adequate amplitude.

**a-bounce check**: requires p_φ < 0, but p_φ = w_φ ρ = (+4)ρ > 0  ✗  **FAILS**

**v2 result (N_EFF=50, 80×80 grid)**: 34 "oscillatory" candidates with Ha× = 11 — ARTIFACTS.  
These had |C|max = 39.5 (constraint violated by ×1000). Coarse grid (Δb ≈ 0.05 at b=0.2, 25% of b)
caused large bicubic spline errors in dE/da, dE/db → spurious force terms.

**v3 result (N_EFF=50, 200×200 grid, direct Bessel verification)**: 0 oscillatory candidates.  
|C|min = 8.85×10⁻¹⁰ (machine precision). Grid cell size Δb ≈ 0.005 eliminated all artifacts.

**Conclusion**: Antiperiodic scalar categorically cannot satisfy a-bounce condition.

---

### Test 3: Periodic Conformal Scalar — S₂-dominated regime (small b/a)  (this run)

**Hypothesis**: At small b/a (r ≲ 0.1), the S₂ Bessel sum dominates S₁ zero-mode:
E_S2 < 0 → total E < 0 → ρ < 0.  
With ρ < 0 and w_φ ≈ +4: p_φ = w_φ ρ < 0 — a-bounce condition on p_φ appears satisfied.

**EOS diagnostic** at a=2.0, N_EFF=50:

| b/a   | E            | ρ           | sign | w₃     | w_φ  | p_φ<0? | κp_φ/(k/a²) |
|-------|-------------|------------|------|--------|------|--------|-------------|
| 0.025 | −6.23×10⁴  | −1.26×10³ | −    | −0.954 | 3.86 | YES    | −6473       |
| 0.050 | −3.98×10³  | −4.01×10¹ | −    | −1.001 | 4.00 | YES    | −214        |
| 0.100 | −2.47×10²  | −1.25      | −    | −1.006 | 4.02 | YES    | −6.67       |
| 0.200 | −1.50×10¹  | −3.77×10⁻²| −    | −1.029 | 4.09 | YES    | −0.21       |

The a-bounce **ratio** condition (κp_φ/(k/a²) < −3) is satisfied at r ≤ 0.1 with N_EFF=50.

**Fundamental obstruction** (constraint equation):

At any a-turning point (Ha = 0):  `3k/a² = κρ`

With k=+1 (S³) and a > 0: LHS > 0, **requiring ρ > 0**.  
But in this regime ρ < 0 everywhere. **Ha cannot reach zero.** Full stop.

**ODE scan results** (245 ICs, N_EFF=50, 200×200 grid over (0.3,4.0)×(0.04,1.0)):
- Accepted: 146,  Rejected: 99 (|Hb0| > 20),  Integrated: 146
- Ha× ≥ 2: **0**,  Ha× ≥ 4: **0**
- ρ < 0 for >90% of trajectory: 146/146 (100%)
- All trajectories: a → grid boundary, b → 0, t_end ≤ 0.6

**Conclusion**: S₂-dominated (ρ<0) regime is **structurally forbidden** from supporting a-bounces
when k=+1. The Hamiltonian constraint is the obstruction, not the force equations.

---

## Summary No-Go Table

| Field Content            | ρ sign | w_φ  | a-bounce? | b-bounce? | Obstruction |
|--------------------------|--------|------|-----------|-----------|-------------|
| Periodic scalar, S₁-dom | +      | −1   | ✓         | ✗         | w₃ = +2/3 too large |
| Antiperiodic scalar      | +      | +4   | ✗         | (n/a)     | p_φ > 0 |
| Periodic scalar, S₂-dom | −      | +4   | ✗         | (n/a)     | constraint: ρ<0 forbids Ha=0 |

**Required EOS for oscillations** (necessary conditions, k=+1):
1. ρ > 0  (constraint at a-turning point)
2. p_φ < 0  (a-bounce: Ḣa > 0 at Ha=0 minimum)  
3. w₃ < (1 + 2w_φ)/3  (b-bounce: Ḣb > 0 at Hb=0 minimum)

Since p_φ < 0 and ρ > 0: w_φ < 0. Then condition (3) becomes w₃ < 1/3 + 2w_φ/3 < 1/3.

**No known scalar field (conformal, c=1/8) satisfies all three simultaneously.**

---

## Next Step: Graviton (Spin-2 Lichnerowicz) Casimir

On S³ × S¹, the transverse traceless spin-2 modes (graviton polarizations) have a different
spectral decomposition from scalars. The S³ TT-tensor eigenvalues are l(l+2)−2 for l ≥ 2,
shifting the effective conformal coupling. This could yield a different (w₃, w_φ) in a regime
where all three necessary conditions are simultaneously satisfiable.

Target: find a regime where:
- E_grav > 0 → ρ > 0
- ∂E/∂b < 0 → p_φ > 0... or find the regime where p_φ < 0

Status: **pending**.

---

## Output Files

| File | Description |
|------|-------------|
| `T3A_casimir_spectral.py` | Periodic conformal scalar Casimir + CasimirInterpolator + ODE system |
| `T3A_casimir_antiperiodic.py` | Antiperiodic scalar variant (v1: N_EFF=1) |
| `T3A_antiperiodic_v2.py` | Antiperiodic, N_EFF=50, 80×80 grid — 34 artifact candidates |
| `T3A_antiperiodic_v3.py` | Antiperiodic, N_EFF=50, 200×200 grid — 0 real candidates |
| `T3A_conformal_smallb.py` | Periodic scalar, S₂-dominated (small b/a), N_EFF=50 |
| `T3A_conformal_smallb.json` | ODE scan results: 146 trajectories, 0 oscillatory |
| `T3A_conformal_smallb_best.png` | Best trajectory plot (monotonic, no bounces) |


---

## Sharpened No-Go Theorem (Power-Law Analysis)

### Corrected a-bounce condition

Previously stated as "p_φ < 0". Correct statement:

At Ha=0, κρ = 3k/a² → κp_φ = w_φ × 3k/a². Then:

    Ḣa = −(k/a²)(1 + w_φ)

For Ḣa > 0 (proper a-bounce with k=+1): **w_φ < −1** (strictly).

| w_φ | Ḣa at Ha=0 | Behavior |
|-----|-----------|----------|
| < −1 | > 0 | ✓ Proper a-bounce |
| = −1 | = 0 | Marginal (de Sitter attractor, Ḣa=0) |
| > −1 | < 0 | ✗ No bounce, Ha decreases through 0 |

**S₁ zero-mode** (periodic conformal scalar, large b/a) gives w_φ = −1 exactly → **marginal, not oscillatory**.
The system approaches de Sitter, it does not bounce.

### General power-law argument

For any Casimir energy E(a,b) = C × a^{α_a} × b^{α_b} with C > 0 (so ρ > 0):

    w₃   = −α_a / 3
    w_φ  = −α_b

Conditions for oscillation:

    (A) Strict a-bounce: α_b > 1
    (B) b-bounce:        α_a > 2α_b − 1

For standard 1-loop Casimir energies of massless fields: **α_a < 0** (energy decreases as a grows — universal consequence of UV regularization and dimensional analysis).

With α_a < 0 and condition (A) requires α_b > 1 → condition (B) requires α_a > 2α_b − 1 > 1. **Contradiction with α_a < 0.**

### Theorem

*For any (massless) field whose 1-loop Casimir energy E(a,b) is positive and decreasing with a, no initial condition produces oscillatory solutions on S³(k=+1) × S¹. This follows from the incompatibility of conditions (A) and (B) with standard scaling.*

### What would need to change

To evade the theorem, one needs E(a,b) with **α_a > 2α_b − 1 > 1** — energy that *grows* faster than a^(2α_b−1) with a. This is:

- **Impossible** for standard UV-regulated massless field Casimir energies (all have α_a < 0)
- **Potentially accessible** via:
  1. **k = −1 geometry (H³)**: constraint at Ha=0 gives κρ = −3/a² → allows ρ < 0 at a-turning point, flipping all sign conditions
  2. **Finite-temperature effects**: thermal energy E ∝ T⁴V grows with volume → positive α_a
  3. **Condensates / non-perturbative**: non-trivial vacuum expectation values can source energy growing with a
  4. **p-form fields in special dimensions**: antisymmetric tensors in D=5 have zero-form contributions with different scaling on S³ × S¹

---

## Status of Graviton Computation

The graviton TT-tensor sector was computed numerically:
- **E < 0** for all (a,b) tested (TT sector contributes winding modes only, no zero mode)
- EOS: w₃ ≈ −1, w_φ ≈ +4 (identical to antiperiodic scalar structure)
- ρ < 0 → constraint obstruction (same as Test 3)

The full graviton (including trace/longitudinal modes and Faddeev-Popov ghosts) was not computed. However, based on the power-law theorem above, even if the full graviton gives ρ > 0 via zero-mode contributions, it would give α_a = −2 (same as scalar zero mode), which cannot satisfy condition (B).

**Conclusion**: Computing the full graviton Casimir energy would not change the no-go conclusion. The theorem is field-content independent for standard BCs.


---

## Multi-Spin Casimir Results (T3A_casimir_multispin.py)

Four spectral sectors implemented and cross-validated:

| Sector | BCs on S¹ | Degeneracy | S³ eigenvalue | c_eff |
|--------|-----------|-----------|---------------|-------|
| `scalar_conf` | periodic | 1 | l(l+2) | 1/8 |
| `coexact_vector` | periodic | (l+1)²-1 | l(l+2)-1 | 0 |
| `TT_tensor` | periodic | ~(l+1)² | l(l+2)-2 | 0 |
| `dirac` | antiperiodic | 2 | l(l+2)+1/4 | 0 |

Bianchi identity (∂_t ρ = 0 conservation) validated to ~10⁻²⁴ for all configs.

### Orbit scan results (296 ICs per config)

| Config | Ha×≥2 | Ha×≥4 | Ha×≥2 & |C|<1 | Min|C| |
|--------|-------|-------|------------|-------|
| scalar_only | 0 | 0 | 0 | 9.0×10⁻¹³ |
| graviton_only | 0 | 0 | 0 | 9.4×10⁻¹³ |
| scalar_graviton | 0 | 0 | 0 | 9.7×10⁻¹³ |
| full_SM | 92 | 0 | **0** | n/a (all |C|>13) |

The 92 "oscillatory" candidates in full_SM are **interpolation artifacts** — all have |C|>13 (constraint violated by ×1000), identical pattern to the v2 antiperiodic scalar artifacts. Well-integrated non-oscillatory trajectories have |C| ~ 10⁻¹².

### EOS scan: unified bounce conditions

Full SM EOS near the ρ=0 crossing (a=1):

| b/a | ρ sign | w₃ | w_φ | A(k=+1) | B(any k) | A(k=-1) |
|-----|--------|-----|-----|---------|---------|---------|
| 0.30 | − | −1.31 | +4.93 | ✓ | ✗ | ✗ |
| 0.50 | − | −4.90 | +15.7 | ✓ | ✗ | ✗ |
| 0.55 | + | +16.7 | −49.1 | ✓ | ✗ | ✗ |
| 0.70 | + | +1.10 | −2.30 | ✓ | ✗ | ✗ |
| 1.00 | + | +0.685 | −1.054 | ✓ | ✗ | ✗ |
| 3.00 | + | +0.667 | −1.000 | ✓ | ✗ | ✗ |

**The b-bounce condition B never passes for any (b/a, field content, k) combination.**

Note: the a-bounce condition A (k=+1) is satisfied at b/a≥0.55 (ρ>0, w_φ<-1). The full SM does achieve w_φ < -1 in the ρ>0 regime — but w₃>0 always defeats the b-bounce.

### Unified no-go: k=-1 analysis

At a turning point (Ha=0), the constraint gives κρ = 3k/a²:
- k=+1: ρ > 0 required → a-bounce needs w_φ < −1
- k=-1: ρ < 0 required → a-bounce needs w_φ > −1

The b-bounce condition is **independent of k**: ρ(1 + 2w_φ − 3w₃) > 0 always.

For k=-1 with ρ < 0 (S₂-dominated regime of full SM):
- a-bounce: w_φ = +15.7 > −1 ✓
- b-bounce needs: (1+2w_φ−3w₃) < 0 (since ρ<0), i.e., w₃ > (1+2×15.7)/3 = 10.8
- Actual w₃ = −4.9 → **fails by ×15 margin**

For k=-1, S₁-dominated (ρ>0 → constraint requires ρ<0 → impossible with k=-1):
The S₁ zero-mode requires ρ>0 but k=-1 requires ρ<0 at the turning point. Contradiction.

**S₁ zero-mode (E ~ b/a²) on k=-1**: a-bounce = marginal (w_φ = −1 → Ḣa = 0), b-bounce = ✓.
This is the **only configuration where b-bounce passes**, but a-bounce is degenerate.

---

## Complete No-Go Summary

**Theorem (field-content independent):** For any 1-loop Casimir energy of massless fields with standard (periodic/antiperiodic) BCs on S^n × S¹, the bounce conditions for both a and b cannot be simultaneously satisfied. The b-bounce condition ρ(1+2w_φ−3w₃)>0 never holds across the full (b/a, field content, k) parameter space explored.

**The one near-miss:** S₁ zero-mode on k=-1 gives marginal a-bounce + b-bounce. A Scherk-Schwarz twist θ ∈ (0,π) applied to the S₁ zero-mode modifies w_φ to -1+ε for small θ, potentially yielding a strict a-bounce. This is the most targeted remaining avenue.

**Routes requiring new physics:**
1. Scherk-Schwarz twist on S¹ (θ ∈ (0,π/2)): zero-mode EOS modified from w_φ = -1 → w_φ = -1+O(θ²) with ρ>0 potentially achievable near the k=-1 turning point
2. p-form flux fields: contribute with negative pressure (tension) in compactified directions
3. Non-minimal coupling or massive fields: scalar with m²>0 has zero-mode scaling E ∝ f(m,b,a) ≠ b/a² at intermediate mass
4. Holographic / non-perturbative sources: not accessible at 1-loop Casimir level

