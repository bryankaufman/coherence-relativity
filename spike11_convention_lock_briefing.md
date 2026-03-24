# Spike 11 — Convention Lock Decision Required
## Team Briefing: H1 Fifth-Force Gate BLOCKED

**Date:** 2026-03-08  
**Status:** BLOCKED — awaiting author/collaborator convention declaration  
**Gate:** H1 fifth-force constraint (Eöt-Wash), Tier-2 (coupling-explicit) closure  
**Impact:** Spike 11 closes immediately once the decision is declared. Both options lead to **H1: PASS**.

---

## 1. Context: Where We Are

The *coherence-relativity* manuscript develops a braneworld cosmology (the "SC2" geometry) in which
ordinary matter is localized on a 4D brane embedded in a 5D spacetime. The SC2 metric is:

```
ds² = -dz² + A(r)² γ_{ij} dx^i dx^j + dr²
```

where `A(r) = e^{-μr}` is the warp factor, `z` is the **unwarped** time direction, and the three
spatial directions `x^i` are warped. This makes SC2 structurally distinct from Randall-Sundrum RS1
(which has four warped directions, `n_w = 4`); SC2 has `n_w = 3`.

The radion field `δL_f` — the fluctuation of the brane separation `L_f` — is the scalar degree of
freedom most likely to mediate a fifth force. Hypothesis **H1** requires that this fifth force not
exceed Eöt-Wash torsion-balance experimental limits.

### H1 current status: `MARGINAL-FINAL`

| Tier | Assumption | Result |
|------|-----------|--------|
| Tier-1 | `α_eff = 1` (conservative, full gravitational coupling) | FAIL — `λ_rad ~ 61–122 μm` lies above the Hoyle et al. 2004 exclusion boundary (`~44 μm` at 95% CL) |
| Tier-2 | `α_eff` derived explicitly from the K³ 4D effective action | Provisional PASS — estimate `α_eff ~ O(10⁻⁵⁸)`, approximately `10⁵⁵×` below Eöt-Wash sensitivity |

**Tier-2 is the decisive gate.** It requires a *formally derived* `α_eff`, not just an estimate.
That derivation is **Spike 11**.

---

## 2. What Has Already Been Established (Spikes 8–10)

These results are fully verified and not in dispute:

- **Radion zero-mode** `f(r) = 1` — derived from the SC2 bulk ODE and Neumann boundary conditions
  (Paper 3 §12.5.2 eq. 12.5.2.A–B).

- **Kinetic normalization integral:**
  ```
  Z_L^{K³} = (3μ M₅³ / 4)(1 − e^{−2μL_f*})
  ```
  with `κ_rad^{K³} = (3/2)μ²` — derived from first principles, gauge-robust, `Δ_mix = 0` exactly
  (Spike 10 acceptance checks 3–4: both PASS). K³ payload exported from Paper 3 §12.7
  (`accept_export: true`).

- **`λ_rad^{K³} ~ O(61–122 μm)`** — above the Eöt-Wash exclusion boundary under the Tier-1
  conservative assumption, but this only matters if `α_eff` is not negligibly small.

---

## 3. Spike 11: The Derivation and the Blocker

The Eöt-Wash coupling parameter `α_eff` is defined by the radion's coupling to matter:

```
Fifth-force potential:  V(r) = −(α_eff G_N M₁ M₂ / r) × e^{−r/λ_rad}
```

The radion-matter coupling `g_rad` has two contributions from the 4D effective action:

```
g_rad = g_J  +  g_W
```

### Step A — CLOSED (exact, no ambiguity)

**`g_J^{NR} = 0` exactly.**

Proof: In the Jordan frame, the radion couples to `T^μ_μ (induced)`. For the SC2 metric, the
induced 4D metric on the brane is:

```
h_{μν} dx^μ dx^ν = −dz² + A(L_f)² γ_{ij} dx^i dx^j
```

The `h_{00} = −1` component is **independent of `L_f`** (the time direction is unwarped). Therefore:

```
d(ln√|h|)/dL_f = (3/2) × d(ln A²)/dL_f = −3μ   [from 3 spatial directions only]
```

The Jordan-frame coupling to NR matter is to `T^j_j = 3p ≈ 0` (pressure ≈ 0 for torsion-balance
test masses). This is a structural zero — it follows from the SC2 symmetry, not from any
approximation or convention. `g_J^{NR} = 0` **exactly**.

### Step B — BLOCKED

The Weyl-rescaling (Einstein-frame conformal) coupling is:

```
g_W = (1 / 2M_Pl²) × dM_Pl^{eff²}/dL_f |_{L_f*}
```

This couples to the full trace `T ≈ −ρ` for NR matter (the dominant term). Computing `g_W`
requires knowing `M_Pl^{eff²}(L_f)` — how the 4D effective Planck mass depends on the brane
separation.

`M_Pl^{eff²}` comes from reducing the 5D Einstein-Hilbert action to 4D:

```
S_5D ⊃ M₅³ ∫d⁵x √G  R₅  →  M_Pl^{eff²}(L_f) ∫d⁴x √h  R₄
```

The key question is: **what power of the warp factor `A(r)` appears in the graviton kinetic
normalization integral for the SC2 background?**

The radion integral (now established) uses:

```
Z_L = n_geom × M₅³ × ∫₀^{L_f} A(r)^{n_w−1} dr = M₅³ × ∫ A² dr   [n_w−1 = 2]
```

The graviton EH reduction uses a *different* contraction structure and may give a different power.

---

## 4. The Two Options

### Option B1 — Explicit Dynamic Reduction

Derive `M_Pl^{eff²}(L_f)` from the SC2 5D EH action explicitly:

```
M_Pl^{eff²}(L_f) = M₅³ × ∫₀^{L_f} A(r)^p dr
```

The exponent `p` is **not currently declared** in the SC2 derivations. Candidate values:

| Candidate | Argument |
|-----------|----------|
| `p = 1` | SC2-specific: `n_w = 3` warped directions, graviton EH contraction `√G × G^{μα}G^{νβ}` gives net power `n_w − 2 = 1` |
| `p = 2` | RS1 analogy (but RS1 has `n_w = 4`, giving `n_w − 2 = 2`; this may not transfer directly to SC2) |
| `p = 2` | By analogy with the radion integral (`n_w − 1 = 2`), but the graviton uses a different EH contraction |

Under the most structurally natural SC2 choice (`p = 1`):

```
M_Pl^{eff²}(L_f) = M₅³ × (1 − e^{−μL_f}) / μ          [A₀ = 1]
dM_Pl^{eff²}/dL_f |_{L_f*} = M₅³ × e^{−μL_f*}
```

Using the branch lock `M₅³ = M_Pl² / (R_DM μ)` (Paper 2 §5.2(6)):

```
g_W = e^{−μL_f*} / (2 R_DM μ)   ~   O(μ/M_Pl)² × O(1)
α_eff ~ O(10⁻⁶¹ – 10⁻⁵⁸)   [both estimates << α_Eöt-Wash ~ 10⁻³]
```

**B1 result → H1: PASS** (with explicit closed-form `α_eff`)

### Option B2 — Locked Ratio as Primary Normalization

The branch lock in Paper 2 §5.2(6) declares:

```
G₅/G₄ = C_loc / μ   with   C_loc = R_DM μ²
```

Under B2, this lock is the *primary* normalization at adjudication order, meaning `M_Pl` is treated
as `L_f`-independent at the stated closure level:

```
dM_Pl^{eff²}/dL_f |_{L_f*} = 0   (at adjudication order)
g_W = 0
α_eff = 0   (exactly)
```

Secondary observation: the Entry 8 estimate formula

```
g_rad = d(ln√|h|)/dL_f / √Z_L = −3μ / √Z_L^{K³}
```

was derived from the `d(ln√|h|)/dL_f = −3μ` variation (three warped spatial directions). Under B2,
this formula already represents the *complete* coupling (Jordan + Weyl both zero), and the `−3μ`
factor is purely the spatial volume element variation — not a `M_Pl` shift.

**B2 result → H1: PASS** (unconditional — no fifth-force coupling at any order within declared closure)

---

## 5. Why Both Paths Lead to PASS

For B1: The fifth-force strength scales as `α_eff × (G_N / r²) × e^{−r/λ_rad}`. Even with
`λ_rad ~ 100 μm` in the Eöt-Wash exclusion zone, a coupling `α_eff ~ 10⁻⁵⁸` is completely
undetectable — Eöt-Wash sensitivity is `α_eff ≳ O(10⁻³)` at those scales. The margin is `~10⁵⁵`.

For B2: `α_eff = 0` exactly means no fifth-force signal at all.

**The choice between B1 and B2 is a convention/normalization-scheme declaration, not a question
about whether the theory survives the H1 constraint.**

---

## 6. Relevant Source Documents

All paths are relative to the project root `coherence-relativity/`:

| File | Relevant Section | Content |
|------|-----------------|---------|
| `notes/derivations/kappa_rad_verification_spike_log.md` | Entry 9 (Spike 11 protocol), Entry 10 (blocker) | Full Steps A–D protocol; B1/B2 definitions and tentative formulas |
| `papers/02-saturation-dynamics/paper2_mathematical_spine_2026-02-28.md` | A.2 item 11, A.4 item 5 | Spike 11 BLOCKED status record |
| `papers/02-saturation-dynamics/paper2_mathematical_spine_2026-02-28.md` | §5.2(6) branch-lock package | `G₅/G₄ = C_loc/μ` lock; `M₅³ = M_Pl²/(R_DM μ)` fixed |
| `papers/02-saturation-dynamics/paper2_mathematical_spine_2026-02-28.md` | `H1_ADJUDICATION_RECORD_UPDATE_K3` | Current `MARGINAL-FINAL` record; `alpha_eff_estimate: O(10^-58) [formal derivation pending]` |
| `papers/03-gr-unification/paper3_emergence_underlying_structure_2026-03-05.md` | §12.5.2 (eqs. 12.5.2.A–D), §12.7 | Radion ODE, zero-mode, `Z_L = n_geom M₅³ ∫A² dr`; K³-VERIFIED payload |

---

## 7. What Happens After the Decision

Once B1 or B2 is declared, the following close in a single pass:

| Gate | Description | Depends on |
|------|-------------|-----------|
| AC-S11-2 | Closed-form `g_W` formula | B1/B2 declaration |
| AC-S11-3 | Closed-form `α_eff` expression | AC-S11-2 |
| AC-S11-4 | Eöt-Wash numerical comparison (explicit margin) | AC-S11-3 |
| AC-S11-5 | Update `H1_ADJUDICATION_RECORD_UPDATE_K3`; promote H1 from `MARGINAL-FINAL` to `PASS` | AC-S11-4 |

**Spike 11 closes. H1 is finalized.**

---

## 8. Questions for the Team

**Primary question (required):**

> **Declare B1 or B2.**
>
> - **B2:** Confirm that the `G₅/G₄` branch lock in §5.2(6) is intended to fix `M_Pl` as
>   `L_f`-independent at adjudication-level closure, making `dM_Pl^{eff²}/dL_f = 0` a valid
>   declaration at this order.
>
> - **B1:** Declare the exponent `p` in `∫₀^{L_f} A(r)^p dr` for the SC2 graviton KE reduction
>   (not the radion). Specifically: does the graviton EH contraction in SC2 give `p = n_w − 2 = 1`
>   (from the `n_w = 3` SC2 structure) or `p = 2` (by RS1 analogy or by matching the radion
>   integral), and on what grounds?

**Secondary question (optional but helpful):**

> Does the Entry 8 formula `g_rad = −3μ / √Z_L^{K³}` already implicitly encode the full (Jordan +
> Weyl) coupling — i.e., is the `d(ln√|h|)/dL_f = −3μ` variation in that formula the complete
> variation of the brane action including the conformal sector? If so, this would independently
> validate B2 from the existing derivation record.

---

*Document prepared by derivation tracking agent, 2026-03-08.*  
*For project history, see `notes/derivations/kappa_rad_verification_spike_log.md` Entries 9–10.*
