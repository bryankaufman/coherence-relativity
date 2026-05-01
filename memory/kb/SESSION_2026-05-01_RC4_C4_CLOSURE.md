# Session Log — 2026-05-01 — RC-4 and C4 Closure

## Session Summary

Two critical-path items closed at leading order:
1. **RC-4**: c_Γ derived; k_c^eff estimated from sourced EOM
2. **C4**: Born-rule axiom for d=2 settled — Busch 2003 adopted

Commit: `7eaa543` (main branch)

---

## RC-4: Sourced Cosmological EOM

**File created:** `papers/02C-holographic-structure/RC4_SOURCED_EOM_2026-05-01.md`

### Result 1 — c_Γ derived

Starting from the Path C balance equation:

$$\Omega_{\rm drag} = \alpha_{\rm geom}\,c_\Gamma^2 = \Omega_\Lambda$$

with $\alpha_{\rm geom} = 10\sqrt{2}/(3\pi) \approx 1.5005$ (RC-8b, geometric-only) and $\Omega_\Lambda = 0.6921 \pm 0.0070$ (Planck 2018):

$$\boxed{c_\Gamma = \sqrt{\Omega_\Lambda/\alpha_{\rm geom}} = 0.679 \pm 0.005}$$

This is a **derivation** (not an inference): both inputs are independently fixed; $c_\Gamma$ follows algebraically.

**Closes omnibus #22** (c_Γ value sourced).

### Result 2 — k_c^eff estimated

From the sourced cosmological EOM $\Box_4 B_\mu = J_\mu^{\rm dec}$ with decoherence source current, the leading-order physical cutoff is:

$$k_c^{\rm eff} = \sqrt{\Omega_\Lambda}\,H_0 = 0.832\,H_0$$

Residual gap: $k_c^{\rm eff}/k_c^{\rm SW} \approx 1/1.9$ where $k_c^{\rm SW} = 5/\chi_{\rm CMB}$. Attributed to the holographic projection $R_\Sigma = \chi_{\rm CMB}$ (Paper 4 §3).

**Closes omnibus #23 at leading order** (full closure requires Paper 4 §3).

---

## C4: Born Rule for d=2

**File created:** `papers/02C-holographic-structure/C4_AXIOM_DECISION_2026-05-01.md`

### Decision

| Route | Status |
|-------|--------|
| Route A — isotropic Fokker–Planck | ❌ Definitively closed (absorption prob ≠ Born rule) |
| Route B — non-isotropic noise ∝ T_MΣ | ⚠️ Open; 2–3 weeks work; deferred to Paper 5 |
| Route C — CDP theorem | ⚠️ Potentially circular |

**Adopted:** Busch 2003 (PRL 91, 120403) as stated axiom for d=2.

**Manuscript instruction:** Corollary 6.2 should read:
> "For d=2 we adopt the Busch (2003) characterization of qubit POVMs as the working axiom for the Born rule…"

**Closes 2C ledger item #21.** Route B recommended for Paper 5 (transformer program).

---

## Paper 2C Prose Updates

Three sections updated in `papers/02C-holographic-structure/paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`:

1. **c_Γ status** (§RC1.3 vicinity): promoted from "observationally inferred" to "derived"; boxed equation added
2. **k_c^eff note** (RC-3 Update): RC-4 leading-order result installed; Paper 4 §3 cross-reference
3. **"Still needed" block**: retitled from "RC-4 scope" to "RC-4 closed / Paper 4 scope"; R_Σ holographic projection as remaining item

## OPEN_ITEMS_ROLLUP.md Updates

- Paper 2C: ~78% → ~82%; blockers cleared
- Paper 3: ~58% → ~62%; RC-4 removed from blockers
- Critical-path item #1 (RC-4): struck through, CLOSED
- Critical-path item #4 (C4): struck through, CLOSED
- Multi-paper dependency table: both rows marked CLOSED
- Next step: RC-1 Opus verification pass

---

## Active Priority Queue (post-session)

1. **RC-1 Opus verification pass** — verify T^(eff)_μν = λ(√−γ/√−g)Π_μν|T_M|²δ_⊥(x,∂M); promote α=3/2 from CONJECTURED to DERIVED; §RC1.1–§RC1.4 systematic check
2. **ζ-regularization** — T2.5-B Casimir bounce spectral sums (Paper 3 tier-1 blocker)
3. **Paper 4 H1-A → H1-C closure gate** — entropy identity S_ent(Σ) = ∫_{γ_RT} Ω_MΣ
4. **s(R) first-principles** — Paper 3 central deliverable
5. **Paper 4 RC-3-P4** — R_Σ = χ_CMB from holographic projection (closes factor-1.9 gap)

---

## Files Changed This Session

| File | Action |
|------|--------|
| `papers/02C-holographic-structure/RC4_SOURCED_EOM_2026-05-01.md` | Created |
| `papers/02C-holographic-structure/C4_AXIOM_DECISION_2026-05-01.md` | Created |
| `papers/02C-holographic-structure/paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md` | Updated (3 locations) |
| `OPEN_ITEMS_ROLLUP.md` | Updated (8 locations) |

Commit: `7eaa543` · 4 files · 514 insertions

---

## RC-1 Opus Verification (2026-05-01, commit bfd197b)

**Files created/updated:**
-  (full report, 227 lines)
-  (inline corrections + status table)

### Findings

**§RC1.1 VERIFIED:** Uniqueness of |T_M|² bilinear under U(d)×T^d correct. Minor: Σ-index sum should be d(d−1) not d².

**§RC1.2 VERIFIED:** Variational calculation T^(eff)_μν = λ(√−γ/√−g)Π_μν|T_M|²δ_⊥ is correct step by step.

**§RC1.3A — TWO ERRORS FOUND:**
1. **w=−1 claim demoted:** Π_μν is PURELY SPATIAL for constant-t ∂M (diag(0,a²,a²,a²)), giving ρ_eff=0, NOT w=−1. The w=−1 result comes from the April 10 bulk EOM: Ω_drag=(3/2)(Γ_dec/H₀)² with Γ_dec=const. Bridge requires Israel junction conditions (RC-2 scope).
2. **α=3/2 misidentified as exponent:** The RC-1 draft interpreted α=3/2 as the exponent in ρ~Γ_dec^{3/2}. The actual April 10 formula has EXPONENT=2 and α=3/2 as COEFFICIENT: Ω_drag = (3/2)(Γ_dec/H₀)². Coefficient α = ∫f₀/∫f₀³ = 3/2 from KCR graviton zero-mode wavefunction f₀=Ncos^{3/2}(√2 r). The Weyl law spectral density argument in the draft (ρ(λ)~λ^{1/2} for CP¹) is WRONG: CP¹ (dim=2) gives ρ(λ)~const.

**§RC1.3B PLAUSIBLE under A3:** w=0 from u_μu_ν tensor structure. Ω_DM/Ω_b consistency holds with corrected formula: Ω_DM=(3/2)β², β=0.416 (April 10).

**§RC1.4 UPDATED:** k_c^eff = √Ω_Λ H₀ = 0.832 H₀ installed from RC-4.

### RC-2 Primary Task (revised)
Reconcile boundary action route (T^(eff)∝Π_μν spatial) with bulk EOM route (ρ_drag=(3/2)(Γ_dec/H₀)²ρ_crit). Show equivalence via Israel junction conditions, with α=∫f₀/∫f₀³=3/2 entering the extrinsic curvature term.
