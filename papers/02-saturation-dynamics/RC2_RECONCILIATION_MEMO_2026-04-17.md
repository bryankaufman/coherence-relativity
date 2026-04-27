# RC-2 Reconciliation Memo — RC2_DERIVATION vs. Paper 2B §5.3 (SC3)

**Date:** 2026-04-17
**Author:** Claude (Opus pass — reconciliation audit)
**Scope:** Audit RC2_DERIVATION_2026-04-17.md against paper2B_KCR_EVALUATION_2026-04-17.md §5.3 / SC3 to determine (a) whether the p = 1 result is robust or a normalization artifact, and (b) where the Λ_eff mismatch enters.

---

## TL;DR (one-paragraph verdict)

The p = 1 result is structurally correct **given Paper 2B's λ = A² identification and |T_M| ∼ A² scaling**, but those two identifications are themselves cited to a §7.3.3 / §7.4.15 of "the companion paper Paper 2B" that does not exist in the current split — they are stale pre-split references. So p = 1 is correctly *derived from the inputs as stated*, but the inputs are unverified within the current manuscript set. The Λ_eff mismatch is **not a physics discrepancy**; it is a notation collision: Paper 2B uses λ as a *dimensionless* distinguishability parameter (0 ≤ λ ≤ 1, λ = A² on KCR), while Paper 2C §RC1.1 uses λ as a *dimensionful* boundary coupling with [M³]. RC-2.4 silently substituted the dimensionful Paper 2C λ into a formula and then set its dimensionless number to 1, producing a result that is dimensionally inconsistent. The correct way to estimate Λ_eff in the SC3 framework is the Path C / Level 3 frame-dragging integral with α_geom = 3/2, not the naive boundary-layer integral in RC-2.4.

**Bottom line:** Neither manuscript needs to be rewritten yet. RC-2.4 needs to be **withdrawn or rederived**, and a notation fix is needed to reconcile "λ" between Paper 2B and Paper 2C before any further dimensional estimates are made.

---

## 1. p = 1 robustness audit

### 1.1 The derivation chain in RC-2.2

The p = 1 result derives from three inputs, combined as:

| Input | Value | Source | Status |
|---|---|---|---|
| λ(r) on KCR-Cone | A²(r) | Paper 2B §4.2.3, citing "Eq. 7.3.3" | **STALE REFERENCE** — §7 doesn't exist in current Paper 2B |
| \|T_{μa}(r)\| from adiabatic formula | A²(r) | Paper 2B §4.1.3 Eq. 4.1.7 + RC-2.1 | ⚠️ Derived from W ∼ A⁻² ansatz; consistent but not independently verified |
| Σ-metric scale \|G_ab\| | O(1) | FS metric on CP¹ | ✅ Standard |

Combination: Γ_dec ∼ λ·\|T\|·\|a^μ_M\|/\|G_ab\| ∼ A²·A²·H₀ = A⁴ H₀, and \|T_M\|² ∼ A⁴, so \|T_M\|² ∼ Γ_dec / H₀ → **p = 1**.

### 1.2 Sensitivity to inputs

The p = 1 result is **exquisitely sensitive** to the λ(r) scaling:

| If λ(r) ∼ … | Then Γ_dec ∼ … | And \|T_M\|² ∼ … | Implied p |
|---|---|---|---|
| A⁰ (constant) | A² H₀ | A⁴ | **p = 2** |
| A¹ | A³ H₀ | A⁴ | **p = 4/3** |
| **A² (RC-2.2)** | **A⁴ H₀** | **A⁴** | **p = 1** |
| A³ | A⁵ H₀ | A⁴ | **p = 4/5** |
| A⁴ | A⁶ H₀ | A⁴ | **p = 2/3** |

So **p = 1 is the answer if and only if λ ∝ A² exactly**. Any deviation rescales p. Since the λ = A² identification is sourced to a §7.3.3 that no longer exists in the split papers, the p = 1 result is conditional on a citation that cannot currently be verified.

### 1.3 Independent plausibility check

The qualitative requirements stated in §4.2.3 (λ → 1 at brane, λ → 0 at pinch-off, λ·T finite) **uniquely fix λ ∝ A^β with β > 0** but do **not** uniquely fix β = 2:

- λ = A^β → 1 at r = 0 (where A = 1) ✓ for any β
- λ = A^β → 0 at r = r_max (where A = 0) ✓ for any β > 0
- λ·\|T\| = A^β · A² = A^(β+2), bounded for any β ≥ −2

The **stronger** condition (constant λ·T, i.e., A^(β+2) = const) requires β = −2, i.e., λ ∝ A⁻². This is the *opposite* of what §4.2.3 claims. The text of §4.2.3 explicitly says "the corrected identification λ = A² (not A⁻²)" — citing Eq. 7.3.3 — so the corrected sign comes from a physical-interpretation argument (λ → 0 in classical limit) that overrides the constant-λT requirement.

⚠️ **There is therefore an internal inconsistency in 2B between §4.1.6 ("constant λ·T = O(1) on KCR") and §4.2.3 (λ = A², which gives λ·T = A⁴, not constant).** Both are cited to §7. This needs to be reconciled inside Paper 2B before p = 1 can be considered settled.

### 1.4 Verdict on p = 1

✅ **Mechanically correct** given inputs as stated.
⚠️ **Inputs unverified** in the current manuscript set (stale §7.3.3 / §7.4.15 references).
🤔 **Internal 2B inconsistency** between §4.1.6 (λ·T constant) and §4.2.3 (λ = A², which makes λ·T = A⁴ ≠ constant).

**Recommendation:** Do not propagate p = 1 into Paper 2C until the §4.1.6 vs. §4.2.3 inconsistency in 2B is resolved. The right next step is to recover the §7.3.3 derivation from the pre-split draft (presumably the original monolithic Paper 2 or the Paper 2A pre-split file) and either restore it as a referenced derivation or supersede it.

---

## 2. Λ_eff mismatch audit

### 2.1 What RC-2.4 wrote

```
Λ_eff = 8πG · λ · |T_M|² / ℓ_bdry
      = 8πG · 1 · 0.68 · H₀
      = 5.4 G H₀
      → Λ_eff / H₀² ∼ 10⁻⁸⁹
```

### 2.2 What SC3 Level 3 says

```
ρ_drag = α_geom · Γ_dec² / G,    α_geom = 3/2
       ∼ H₀² / G                  (for Γ_dec ∼ H₀)
       → Ω_drag ∼ 0.69            (matches Ω_Λ)
```

The two answers differ by a factor of ∼ 10⁸⁹. This is not a small discrepancy — it spans the full "cosmological constant problem" hierarchy.

### 2.3 The notation collision

The single most important finding from this audit:

| Symbol | Paper 2B usage | Paper 2C usage |
|---|---|---|
| λ | Dimensionless distinguishability parameter, 0 ≤ λ ≤ 1; equals A²(r) on KCR | Dimensionful boundary coupling with [M³] (Paper 2C §RC1.1 line 131) |

These are **different objects** sharing a symbol. Paper 2B's λ is a profile function whose values are pure numbers between 0 and 1. Paper 2C's λ is a coupling constant in a Lagrangian density that must carry mass dimension 3 for the action to be dimensionless.

### 2.4 Why RC-2.4 is dimensionally inconsistent

Take RC-2.4's formula at face value:

```
Λ_eff = 8πG · λ · |T_M|² / ℓ_bdry
[Λ_eff] = M⁻² · M³ · 1 · M¹ = M²    ✓ (using Paper 2C λ with [M³])
```

So the formula is dimensionally correct **only if λ has [M³]**. But the substitution "λ = 1" in RC-2.4 then implicitly treats λ as a pure number, conflating the two conventions. With λ_2C properly dimensioned as λ_natural × M³ for some characteristic mass M, the result becomes:

```
Λ_eff = 8π · λ_natural · M³ · 0.68 · H₀ / M_Pl²
      = 17 · λ_natural · M³ · H₀ / M_Pl²
```

For this to match Λ_obs ∼ H₀², one needs M³ ∼ M_Pl² · H₀, i.e., M ∼ (M_Pl² H₀)^(1/3) ∼ 50 MeV (the "GUT-of-Λ" scale). This is the cosmological constant problem in its standard form: λ must be tuned to a specific non-natural value.

### 2.5 Why SC3 Level 3 avoids the hierarchy

The SC3 Level 3 calculation does **not** use the boundary-action λ at all. Instead it uses:

1. The §4.1.6 statement λ·T = O(1) on KCR (the dimensionless Paper 2B λ).
2. The frame-dragging backreaction integral ρ_drag = α_geom · Γ_dec² / G with α_geom = 3/2 derived from CP¹ geometry.

The trick is that **λ·T appearing as a dimensionless O(1) combination eliminates the Planck-scale dependence** that plagues the naive boundary-layer integral. The α_geom = 3/2 number is the dimensionless residue after all the dimensionful stuff (G, H₀, etc.) has been pulled out.

**The two calculations are different physics, not different numerical approximations of the same physics.**

- RC-2.4: integrate the boundary action S_bdry = λ ∫ √(-γ) Tr(T_M T_M†) as an Israel-junction source.
- SC3 Level 3: compute the frame-dragging backreaction from the M-Σ EOM directly, using the §4.1.6 λ·T cancellation.

The boundary action formulation (Paper 2C §RC1.1) and the M-Σ frame-dragging formulation (Paper 2B §5.3.4.3) are **two different approaches to the same Λ_eff**, and they should agree once both are properly derived. They do not currently agree because:

- Paper 2C §RC1.1 has the boundary action with a free coupling λ_2C ∼ [M³] whose value is not fixed.
- Paper 2B §4.1.6 / §5.3 has the frame-dragging calculation with an O(1) dimensionless combination λ_2B · T, whose value comes from the cited §7.3.3 / §7.4.15 (stale).

### 2.6 Verdict on Λ_eff mismatch

🤔 **Not a physics discrepancy — it is two unfinished and uncoordinated calculations.**

- RC-2.4's "Λ_eff = 5.4 G H₀" is **wrong** (dimensionally inconsistent — requires λ_2C to be dimensionless when it must carry [M³]).
- SC3 Level 3's "ρ_drag ∼ ρ_Λ" is **right at the order-of-magnitude level** but rests on a stale §7.3.3 derivation.

**Recommendation:**
1. **Withdraw the RC-2.4 numerical estimate** for Λ_eff. The structural result (Israel-junction propagation) stands; the numerical "5.4 G H₀" should be deleted or marked incorrect.
2. **Reconcile the two λ's.** Either (a) introduce distinct symbols (e.g., λ_dist for Paper 2B's distinguishability parameter, λ_bdry for Paper 2C's boundary coupling), or (b) explicitly relate them via a conversion factor (e.g., λ_bdry = λ_dist · M_eff³ for some M_eff).
3. **Recover §7.3.3 / §7.4.15** from pre-split material before claiming λ = A² on KCR.

---

## 3. Decision matrix for Bryan

| Question | Answer | Action implied |
|---|---|---|
| Is p = 1 the genuine implication of the current KCR analysis? | Conditionally yes — given λ = A² and \|T_M\| ∼ A² | Don't patch 2C yet; verify §4.2.3 chain first |
| Can the Λ_eff boundary-layer estimate be reconciled with SC3? | No — they are computing different things, and the boundary-layer estimate is dimensionally inconsistent as written | Withdraw RC-2.4's numerical estimate; note the structural framework but not the number |
| Does 2C need a rewrite? | **Not yet.** The §RC1.3 narrative still works as written (Conjecture C1 = honest flag). Premature rewrite to "p = 1, derived" would propagate an unverified input | Keep §RC1.3 in its current "C1 = conjectured" state |
| Does 2B/RC-2 normalization need work? | **Yes.** Three issues: (a) stale §7.3.3 / §7.4.15 references, (b) §4.1.6 vs. §4.2.3 internal inconsistency, (c) λ-symbol collision between 2B and 2C | This is the next gating calculation |

---

## 4. Concrete next steps (in priority order)

1. **Recover §7.3.3 and §7.4.15** from pre-split Paper 2 material. Without these, both p = 1 and the SC3 Level 3 estimate are uncited.
2. **Resolve the λ-symbol collision.** Pick one of:
   - (a) Rename Paper 2C's coupling to λ_bdry [M³] and Paper 2B's distinguishability parameter to λ_dist [dimensionless].
   - (b) Express λ_bdry = λ_dist · M³ explicitly with a chosen mass scale M.
3. **Resolve the §4.1.6 vs. §4.2.3 internal inconsistency in Paper 2B.** Either λ·T is constant (requires λ ∝ A⁻²) or λ ∝ A² (gives λ·T ∝ A⁴, not constant). Both cannot be true simultaneously on the KCR interval.
4. **Withdraw RC-2.4's numerical Λ_eff estimate.** Replace with a statement that the boundary-action and frame-dragging calculations need to be reconciled before any number can be quoted.
5. **Defer the p = 1 propagation into Paper 2C** until items 1–3 are resolved.

---

## Realistic Status

✅ **VERIFIED:** Reconciliation diagnosis is complete. The Λ_eff mismatch is not a physics problem; it is a notation collision plus a stale-reference problem.

⚠️ **UNTESTED:** None of the three items in §4 (recover §7.3.3, resolve λ-collision, resolve 2B internal inconsistency) has been worked through here — they are flagged for next-session work.

❌ **MISSING:** A single self-consistent derivation of λ(r) on the KCR interval from the action principle. The current chain is broken by stale references.

🤔 **UNKNOWN:** Whether the §7.3.3 derivation in the pre-split material survives modern scrutiny. Until recovered, all downstream identifications (λ = A², λ·T = O(1), p = 1) inherit its uncertainty.

**Next Steps:**
1. Recover §7.3.3 / §7.4.15 from the pre-split Paper 2 monolithic draft (or wherever they live).
2. Resolve the λ-symbol collision between Paper 2B and Paper 2C explicitly.
3. Resolve the §4.1.6 vs. §4.2.3 internal inconsistency.
4. Withdraw RC-2.4's Λ_eff = 5.4 G H₀ numerical claim; mark as "structural framework correct, numerical estimate retracted pending reconciliation."
5. Hold off on Paper 2C §RC1.3 patches until items 1–3 close.

**Realistic Status:** Reconciliation diagnosis complete. **2C does not need a rewrite yet; 2B and RC-2 need the source-derivation work recovered before any further estimates can be taken seriously.**
