# §7.9 Stochastic Drift F^A from the System-Environment Hamiltonian

**Status:** REVISED DRAFT (2026-05-02 original → corrected 2026-05-02 → editorial 2026-05-03)
**Closes:** Paper 1 line-778 promise (Predictions 2, 3, 4, 6)
**Placement:** Appended to `paper2_section_7.0_EoM_MxSigma_DRAFT.md` after §7.8
**Status note:** F^r formula (Eq. 7.9.13) is correct; derivation is from a phenomenological
logistic ansatz (§7.9.5), NOT a first-principles Lindblad derivation. See §7.9.5 and §7.9.9.
**2026-05-03 editorial pass:** Fixed m_KK numerical value in §7.9.8 (8·1·(1+2)=24, not √48);
added angular F^θ, F^φ scope statement at end of §7.9.5; tightened D subleading estimate in
§7.9.6; added N-mode independent-channels justification for Prediction 3 in §7.9.7.

---

## §7.9.1 Motivation: From Geodesics to Stochastic Dynamics

Sections §7.1–§7.8 establish the *deterministic* equations of motion on M × Σ and verify the
warp-factor structure A(r) = cos(√2 r). However, Paper 1 (§6.F, Eq. 6.2) introduces the
stochastic action

$$\mathcal{S}[\gamma] = \frac{1}{4D}\int_0^1\bigl(\dot{x}^A - F^A\bigr)G_{AB}\bigl(\dot{x}^B - F^B\bigr)\,d\sigma \qquad \text{(7.9.1)}$$

and notes that the order-of-magnitude estimates for Predictions 2 (hysteresis δV), 3 (curvature
scaling), 4 (gravitational decoherence), and 6 (coherence revival) "additionally invoke the
stochastic action S[γ] and drift F^A, whose explicit derivation from system–environment coupling
is deferred to Paper 2." This section delivers the derivation on the KK-cone geometry.

---

## §7.9.2 Notation and λ-Symbol Disambiguation

> **Mandatory notation note** — this section uses multiple λ symbols in distinct roles.
> Canonical definitions follow `notes/NOTATION_DISAMBIGUATION_LAMBDA_2026-05-02.md`.

| Symbol | Definition | Range | Direction |
|--------|-----------|-------|----------|
| **λ** | EGY distinguishability: √(1 − \|⟨W_L\|W_R⟩\|²) | [0, 1] | 0 = coherent, 1 = pointer |
| **λ_A** | Warp-factor amplitude squared: A(r)² = cos²(√2 r) | [1, 0] | **inverted** vs. λ |
| **λ_ptr** | Pointer non-occupancy: 1 − ⟨ψ_ptr\|ρ_S\|ψ_ptr⟩ | [1, 0] | inverted vs. λ |

**Corrected Ansatz A*:** In KK-cone coordinates, the EGY parameter and warp coupling satisfy:
$$\lambda = \sin(\sqrt{2}\,r), \qquad
  \lambda_A := A(r)^2 = \cos^2(\!\sqrt{2}\,r) = 1 - \lambda^2 \qquad \text{(7.9.2)}$$

These are COMPLEMENTARY, not equal. Previous drafts (pre-2026-05-02) incorrectly identified
λ = λ_A; this is the root of the algebraic conflicts resolved below.

---

## §7.9.3 System-Environment Hamiltonian on M × Σ

### Decomposition

Let the total Hamiltonian on M × Σ be:

$$H_{SE} = H_S \otimes \mathbb{I}_E \;+\; \mathbb{I}_S \otimes H_E \;+\; H_\mathrm{int} \qquad \text{(7.9.3)}$$

with interaction Hamiltonian:

$$H_\mathrm{int} = \sum_{\alpha} A_\alpha \otimes B_\alpha \qquad \text{(7.9.4)}$$

where A_α are system (Σ-sector) operators and B_α are environment (M-sector) operators.
**No explicit λ or λ_A coupling is written in H_int.** The r-dependence of the effective
decoherence rate is absorbed into Γ_dec (see §7.9.4), consistent with the renormalized
coupling convention of §7.3. Writing an explicit λ_A coefficient in H_int (as in the
pre-2026-05-02 draft) double-counts the warp-factor suppression already present in Γ_dec(r).

### Environment Correlation Function

Define the two-time environment correlation function in the interaction picture:

$$C_{\alpha\beta}(\tau) = \mathrm{Tr}_E\bigl[B_\alpha(\tau)\,B_\beta(0)\,\rho_E^{(0)}\bigr] \qquad \text{(7.9.5)}$$

where ρ_E^{(0)} is the initial (thermal bath) environment state. Under the Markov approximation,
C_αβ(τ) decays on environment correlation time τ_E ≪ 1/Γ_dec. The spectral density at the
decoherence frequency ω ~ Γ_dec determines the effective rate:

$$\tilde{C}_{\alpha\beta}(\Gamma_\mathrm{dec}) = \int_0^\infty e^{i\Gamma_\mathrm{dec}\tau}\,C_{\alpha\beta}(\tau)\,d\tau \qquad \text{(7.9.6)}$$

From Paper 2 omnibus item #29 (COMPLETED 2026-04-20): Γ_dec(z) = Γ₀ × H(z)/H₀, Γ₀ ≈ 0.49 H₀.

---

## §7.9.4 Born-Markov Master Equation on Σ

### Lindblad form

Under the Born-Markov approximation (system-environment factorization + memoryless replacement
of the memory kernel), the reduced dynamics on the system Hilbert space H_S is:

$$\frac{d\rho_S}{dt} = -i[H_\mathrm{eff},\rho_S] + \sum_{\alpha\beta}\tilde{C}_{\alpha\beta}\!\left(A_\beta\rho_S A_\alpha^\dagger - \tfrac{1}{2}\{A_\alpha^\dagger A_\beta,\rho_S\}\right) \qquad \text{(7.9.7)}$$

For pointer-basis dephasing, the dominant Lindblad operator is L = √Γ_eff P̂_ptr
(pointer projector), reducing to a pure-dephasing master equation:

$$\frac{d\rho_S}{dt} = \Gamma_\mathrm{eff}\!\left(\hat{P}_\mathrm{ptr}\rho_S\hat{P}_\mathrm{ptr} - \tfrac{1}{2}\{\hat{P}_\mathrm{ptr}^2,\rho_S\}\right) \qquad \text{(7.9.8)}$$

### What Eq. (7.9.8) does — and does NOT — give

Pure-dephasing Lindblad (7.9.8) has two consequences:
1. **Off-diagonal decay:** d⟨L|ρ_S|R⟩/dt = −Γ_eff ⟨L|ρ_S|R⟩ (exponential decoherence)
2. **Population preservation:** d⟨i|ρ_S|i⟩/dt = 0 (diagonal elements fixed)

The pointer non-occupancy λ_ptr = 1 − ⟨ψ_ptr|ρ_S|ψ_ptr⟩ is a **population**, so it does
**not** evolve under Eq. (7.9.8). Therefore:

> **Key correction vs. pre-2026-05-02 draft:**
> The equation dλ/dt = −2Γ_dec λ(1−λ) (Eq. 7.9.9 of the old draft) **cannot** be derived from
> the pointer-basis Lindblad alone, regardless of whether λ is identified with λ_ptr, λ_A, or
> the EGY parameter. The logistic evolution equation is a phenomenological ansatz (§7.9.5).

Equation (7.9.8) establishes the correct Born-Markov framework, the form of the jump operators,
and the validity regime (§7.9.8). The ansatz in §7.9.5 is *consistent with* (7.9.8) in that it
respects the pointer-state attractor structure mandated by Lindblad decoherence, but it is not
derived from it.

---

## §7.9.5 Phenomenological Logistic Ansatz and Drift F^r

### Motivation for the logistic ansatz

The warp coupling λ_A = A(r)² = cos²(√2 r) decreases from 1 (brane, coherent endpoint) to 0
(throat, pointer endpoint) as decoherence proceeds. A natural model for this evolution is the
logistic decay:

$$\frac{d\lambda_A}{dt} = -2\,\Gamma_\mathrm{dec}\,\lambda_A\,(1-\lambda_A) \qquad \text{(7.9.9) [ANSATZ]}$$

Physical motivation for this specific form:
- **Two fixed points:** λ_A = 1 (coherent endpoint, repelling) and λ_A = 0 (pointer endpoint,
  attracting); each has zero rate, consistent with no spurious drift at extremes.
- **Maximum rate at λ_A = 1/2**, corresponding to r = π/(4√2) ≈ 0.555 — mid-way between
  brane and throat, where the decoherence drive is strongest.
- **Small-λ_A linearization:** (7.9.9) reduces to dλ_A/dt ≈ −2Γ_dec λ_A, consistent with
  the standard exponential decoherence prediction λ_A(t) ~ e^{−2Γ_dec t} near t = 0 (onset
  of decoherence from the fully coherent brane).
- The factor of 2 normalizes the peak rate to Γ_dec/2, matching the dephasing rate from
  Eq. (7.9.8) at the half-decoherence point.

> **Scope statement:** Ansatz (7.9.9) is a leading-order phenomenological model capturing the
> key fixed-point structure and rate normalization. It is consistent with — but not uniquely
> determined by — the Born-Markov Lindblad framework of §7.9.4. First-principles derivation
> of the logistic form from the Nakajima-Zwanzig memory kernel is deferred to future work;
> registered as #OP-NZ in PAPER2_OPEN_ITEMS_LEDGER; stub in Paper 2C §5.5.

### Derivation of F^r from the logistic ansatz

From Ansatz (7.9.9) and the chain rule for r-coordinates:

$$\frac{d\lambda_A}{dr} = \frac{d}{dr}\cos^2(\!\sqrt{2}\,r) = -\sqrt{2}\,\sin(2\sqrt{2}\,r) \qquad \text{(7.9.10)}$$

The drift velocity in the r-direction is:

$$F^r(r) = \frac{dr}{dt}\bigg|_\mathrm{drift} = \frac{d\lambda_A/dt}{d\lambda_A/dr}
= \frac{-2\,\Gamma_\mathrm{dec}\,\cos^2(\!\sqrt{2}\,r)\sin^2(\!\sqrt{2}\,r)}{-\sqrt{2}\,\sin(2\sqrt{2}\,r)} \qquad \text{(7.9.11)}$$

Using sin(2√2 r) = 2 sin(√2 r) cos(√2 r):

$$F^r(r) = \frac{2\,\Gamma_\mathrm{dec}\,\cos^2(\!\sqrt{2}\,r)\,\sin^2(\!\sqrt{2}\,r)}{\sqrt{2}\cdot 2\,\sin(\!\sqrt{2}\,r)\cos(\!\sqrt{2}\,r)}
= \frac{\Gamma_\mathrm{dec}}{\sqrt{2}}\,\cos(\!\sqrt{2}\,r)\,\sin(\!\sqrt{2}\,r) \qquad \text{(7.9.12)}$$

$$\boxed{F^r(r) = \frac{\Gamma_\mathrm{dec}}{2\sqrt{2}}\,\sin(2\sqrt{2}\,r)} \qquad \text{(7.9.13)}$$

### Fixed-point analysis

- **r = 0 (brane, λ = 0, λ_A = 1):** F^r(0) = 0. Repelling fixed point:
  dF^r/dr|₀ = Γ_dec cos(0)·1 = Γ_dec > 0 → perturbations δr > 0 grow.
- **r ≈ π/(4√2) ≈ 0.555:** Maximum drift F^r = Γ_dec/(2√2).
- **r = r* = π/(2√2) ≈ 1.11 (throat, λ = 1, λ_A = 0):** F^r(r*) = 0. Attracting fixed
  point: dF^r/dr|_{r*} = −Γ_dec < 0 → perturbations return to r*.

The drift is smooth and finite everywhere, consistent with regularity (§4.4.8).

### Scope: angular components F^θ, F^φ

The present derivation gives only the radial drift F^r on the KK-cone. For pointer-basis
decoherence with isotropic environment coupling — H_int = Σ_α A_α ⊗ B_α with the A_α
operators invariant under the residual U(1) ⊂ T^d isometry of Σ — the angular components
F^θ, F^φ vanish identically: there is no preferred angular direction in the dissipator and
no angular bias is induced. Anisotropic coupling (A_α(θ, φ) breaking the U(1)) would generate
non-zero angular drift; the anisotropic case is outside §7.9 scope and deferred to future work
(future work; not currently scoped to a specific paper — registered as #OP-AF in PAPER2_OPEN_ITEMS_LEDGER).
All Predictions 2, 3, 6 evaluated below depend only on F^r.

---

## §7.9.6 Diffusion Coefficient D

### Corrected form

With H_int written as Eq. (7.9.4) (no explicit λ_A factor), the noise kernel evaluated
at the Markov frequency is O(Γ₀), independent of r at leading order. In arc-length
parameterization (G_{rr} = 1), the diffusion coefficient is:

$$D = \Gamma_0 \qquad \text{(7.9.14)}$$

**Correction vs. pre-2026-05-02 draft:** The old formula D(r) = cos⁴(√2 r) Γ₀ arose from
including an explicit λ_A coupling in H_int and squaring under the Born approximation.
Absorbing λ_A into Γ_dec (§7.9.3) removes this double-counting; D is constant at leading
order. Subleading r-dependence enters from the spectral-density evaluation at the system
Bohr frequency rather than at the bare Hubble scale, and is estimated O(Γ_dec/m_KK) ≈ O(0.1)
at present cosmological epoch (using m_KK ≈ 4.90 H₀ from §7.9.8 and Γ_dec ≈ 0.49 H₀); this
correction is not derived in §7.9.

### Consequences for stochastic action

The noise-to-signal ratio (F^r)²/(4D) evaluates to:

$$\frac{(F^r)^2}{4D} = \frac{\Gamma_\mathrm{dec}^2\,\sin^2(2\sqrt{2}\,r)}{32\,\Gamma_0} \qquad \text{(7.9.15)}$$

This is **finite everywhere** on [0, r*], including at the pointer-state throat r = r*. The
old formula gave (F^r)²/(4D) ∝ tan²(√2 r), which diverged at r → r* (unphysical).

**Geometric rigidity** (G_λλ → ∞ as λ → 1 in Paper 1) is the correct signature of the
attractor, coming from the **geometric** potential V_geom, not from V_stoch. Separating
these two contributions is an important clarification over the pre-2026-05-02 draft.

---

## §7.9.7 Stochastic Action and Prediction Estimates

### Explicit stochastic action

With F^r from Eq. (7.9.13) and D = Γ₀ from Eq. (7.9.14):

$$\mathcal{S}[\gamma] = \frac{1}{4\,\Gamma_0}\int_0^1\!\!\left(\dot{r} - \frac{\Gamma_\mathrm{dec}}{2\sqrt{2}}\sin(2\sqrt{2}\,r)\right)^{\!2} d\sigma \qquad \text{(7.9.16)}$$

### Quasipotential depth

The action cost of the reverse path (coherence revival, ṙ = −F^r) is:

$$V_\mathrm{stoch}(0) = \int_0^{r_*}\!\frac{(F^r)^2}{4\,\Gamma_0}\,dr
= \frac{\Gamma_\mathrm{dec}^2}{32\,\Gamma_0}\int_0^{\pi/(2\sqrt{2})}\!\!\!\sin^2(2\sqrt{2}\,r)\,dr \qquad \text{(7.9.17)}$$

Substituting u = 2√2 r (du = 2√2 dr, limits 0 → π):

$$V_\mathrm{stoch}(0) = \frac{\Gamma_\mathrm{dec}^2}{32\,\Gamma_0}\cdot\frac{1}{2\sqrt{2}}\int_0^{\pi}\sin^2(u)\,du
= \frac{\Gamma_\mathrm{dec}^2}{64\sqrt{2}\,\Gamma_0}\cdot\frac{\pi}{2}
= \frac{\pi\,\Gamma_\mathrm{dec}^2}{128\sqrt{2}\,\Gamma_0} \qquad \text{(7.9.18)}$$

This is **finite**. The old tan²-formula gave V_stoch(0) = ∞, which was unphysical.

### Application to Predictions

**Prediction 2 (Frame-transformation hysteresis):** Visibility deficit for an erasure-revival
loop λ: 0 → λ_max → 0:

$$\delta\mathcal{V} \approx \Delta\mathcal{S} = \frac{\Gamma_\mathrm{dec}^2}{32\,\Gamma_0}\int_0^{r_\mathrm{max}}\!\!\sin^2(2\sqrt{2}\,r)\,dr \qquad \text{(7.9.19)}$$

For a half-loop to r_max = π/(4√2) (peak drift), Δ𝒮 = πΓ_dec²/(256√2 Γ₀). This predicts
a measurable hysteresis coefficient of order Γ_dec²/Γ₀ per erasure-revival cycle.

**Prediction 3 (Coherence-space curvature, N-body):** The N-mode generalization of F^r
follows from the N-mode warp factor A_N(r). At leading order in 1/N, the logistic
Ansatz (7.9.9) generalizes with Γ_dec → Γ_dec × N (each of N independent decoherence
channels contributes additively to the dissipator under the standard product-environment
Born-Markov assumption; cross-channel correlations are subleading in 1/N). This gives
δV ∝ N² from (Γ_dec × N)² in the stochastic-action prefactor. D^(N) = Γ₀ remains constant
at leading order. Full N-mode generalization is Paper 2C scope.

**Prediction 6 (Coherence revival time):** The Poincaré recurrence time for escape from
the pointer attractor back to r = 0 scales as:

$$T_\mathrm{rev} \sim \exp\!\left(\frac{V_\mathrm{stoch}(0)}{\Gamma_0}\right)
= \exp\!\left(\frac{\pi\,\Gamma_\mathrm{dec}^2}{128\sqrt{2}\,\Gamma_0^2}\right) \qquad \text{(7.9.20)}$$

This is finite and frame-relative, as required by Paper 1 Prediction 6.

**Prediction 4 (Gravitational decoherence modification):**

$$F^r_\mathrm{grav}(r) = F^r(r) + \beta\,\frac{dg/dt^2}{\chi^2_\mathrm{grav}}\,\tau_\mathrm{frame}^2 \qquad \text{(7.9.21)}$$

where β is the T_{AB} coefficient from Paper 2C §RC1.3. Full derivation of β is Paper 2C scope.

---

## §7.9.8 Born-Markov Approximation Validity

The Born approximation requires |H_int| ≪ |H_S| in the interaction picture (weak
system-environment coupling). With H_int = Σ A_α ⊗ B_α and no explicit warp-factor coefficient:

- **At r = 0 (λ_A = 1):** Maximum KK environment coupling. Born holds when Γ_dec ≪ ω_S
  (system Bohr frequency), satisfied in the regime of interest (Γ_dec ~ 0.49 H₀ ≪ ω_S
  for atomic / qubit systems).
- **At intermediate r (λ_A ~ 1/2):** Half-strength coupling; Born most reliable here, and
  this is where F^r is maximal, so the Born regime governs the dominant dynamics.
- **At r → r* (λ_A → 0):** System approaches the pointer state; H_int effectively vanishes
  by warp suppression, Born excellent. Markov is also self-consistent here: F^r → 0 so the
  system dynamics slow to zero, and the Markov condition τ_E ≪ 1/Γ_system is not violated.

**Markov validity:** The Markov approximation requires τ_E ≪ 1/Γ_dec. For the KK bath
(environment = KK bulk modes, §2.3), this reads m_KK ≫ Γ_dec. Using the first
KK vector mode with spectrum m_n² = 8n(n+2) (Paper 2B §RC3.3 addendum), so
m_1² = 8·1·(1+2) = 24 and m_1 = 2√6 H₀ ≈ 4.90 H₀, vs. Γ_dec ~ 0.49 H₀,
the Markov condition m_KK/Γ_dec ≈ 10 ≫ 1 is satisfied.

---

## §7.9.9 Summary and Status

| Result | Equation | Status |
|--------|----------|---------|
| H_SE decomposition on M × Σ (no λ_A in H_int) | 7.9.3–7.9.4 | ✅ DERIVED |
| Lindblad pure-dephasing master equation | 7.9.7–7.9.8 | ✅ DERIVED |
| Logistic ansatz for warp coupling decay | 7.9.9 | ⚠️ ANSATZ (phenomenological) |
| Drift F^r = Γ_dec sin(2√2 r) / (2√2) | 7.9.13 | ✅ DERIVED from ansatz (7.9.9) |
| Diffusion D = Γ₀ (constant) | 7.9.14 | ✅ CORRECTED (coupling absorbed into Γ_dec) |
| Stochastic action (finite everywhere) | 7.9.16 | ✅ CORRECTED |
| Quasipotential depth V_stoch(0) = πΓ_dec²/(128√2 Γ₀) | 7.9.18 | ✅ DERIVED (FINITE) |
| Prediction 2 hysteresis Δ𝒮 estimate | 7.9.19 | ✅ CORRECTED |
| Prediction 6 revival time T_rev | 7.9.20 | ✅ CORRECTED (finite, well-defined) |
| Prediction 3 N-body scaling | §7.9.7 | ⚠️ SKETCH (N-mode generalization stated) |
| Prediction 4 gravitational correction β | 7.9.21 | ⚠️ DEFERRED to Paper 2C |
| Born/Markov validity in KK environment | §7.9.8 | ✅ VERIFIED (m_1 = 2√6 H₀ ≈ 4.90 H₀; m_KK/Γ_dec ≈ 10) |

**What this section closes:** Paper 1 line 778 promise that F^A would be derived from H_SE
in Paper 2. F^r = Γ_dec sin(2√2 r)/(2√2) is the result; derived from the logistic Ansatz
(7.9.9) on the warp coupling λ_A, motivated by Born-Markov Lindblad decoherence physics.
The ansatz status is explicit; first-principles closure of (7.9.9) is deferred to future work (registered as #OP-NZ in PAPER2_OPEN_ITEMS_LEDGER).

**Key corrections over pre-2026-05-02 draft:**
1. λ_A notation disambiguated from EGY λ throughout; see §7.9.2.
2. Logistic evolution is a phenomenological ansatz (7.9.9), not derivable from pointer-basis
   Lindblad alone (§7.9.4 explains why).
3. D = Γ₀ constant (no r-dependent cos⁴ factor); stochastic action is finite everywhere.
4. Tan² divergence removed; V_stoch(0) = πΓ_dec²/(128√2 Γ₀) is finite and analytically derived.

---

## References within Paper 2

- §7.1–§7.8: KK-cone metric, warp factor A(r) = cos(√2 r), frame-lag force
- §2.3: Markov ratio R_Markov; decoherence timescale τ_D; KK mass spectrum m_KK
- §2.4: Mixed-state Born rule via purification
- §4.4.8: Regularity (Reg1–Reg3) verification for A(r) = cos(√2 r)
- Omnibus #29: Γ_dec(z) = Γ₀ H(z)/H₀ (COMPLETED 2026-04-20)
- `notes/NOTATION_DISAMBIGUATION_LAMBDA_2026-05-02.md`: Authoritative λ symbol list
- Paper 2C §RC1.3: T_{AB} gravitational coupling coefficient β
- **N-Z closure of Ansatz (7.9.9):** First-principles derivation via Nakajima-Zwanzig memory kernel not yet scoped to a specific section; registered as #OP-NZ in PAPER2_OPEN_ITEMS_LEDGER
- Paper 1 §6.F Eq. (6.2): Stochastic action S[γ]
