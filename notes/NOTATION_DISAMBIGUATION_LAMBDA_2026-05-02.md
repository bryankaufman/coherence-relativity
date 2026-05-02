# HCR Series — Notation Disambiguation: All λ Symbols
*Created 2026-05-02 after systematic verification revealed direction-inversion conflict*
*Status: AUTHORITATIVE — all papers must adopt this scheme in their next editorial pass*

---

## The Core Conflict

Two principal uses of λ go in OPPOSITE directions:

| Symbol in use | At coherent endpoint | At classical/pointer endpoint | Conflict |
|---|---|---|---|
| Paper 1 EGY λ | λ = 0 (coherent, open future) | λ = 1 (pointer/past, rigid) | ← PRIMARY definition |
| Paper 2B λ = A(r)² | λ = 1 (brane, r=0) | λ = 0 (throat, r=r*) | ← INVERTED vs. EGY |

"Ansatz A*: λ = A(r)²" conflates these. The correct mapping is:

$$\lambda_{\rm EGY} = \sin(\sqrt{2}\,r), \quad A(r) = \cos(\sqrt{2}\,r) = \sqrt{1 - \lambda_{\rm EGY}^2}$$

**Ansatz A* corrected statement:** The EGY distinguishability coordinate λ satisfies
λ = sin(√2 r) in KK-cone coordinates, or equivalently λ_A = A(r)² = 1 − λ².
The warp coupling λ_A and the EGY parameter λ are COMPLEMENTARY, not equal.

---

## Complete λ Symbol Inventory

### λ — PRIMARY (retained, NO subscript in Papers 1–2A)

**Definition:** EGY distinguishability = √(1 − |⟨W_L|W_R⟩|²)

**Range:** [0, 1]

**Direction:** 0 = fully coherent (open future), 1 = classical pointer state (fixed past)

**Papers:** P1, P2A, P2C (in T^(eff) coupling see λ_bdry below)

**Metric:** G_λλ = 1/[2(1−λ²)]; G_λλ(0) = 1/2 finite; G_λλ → ∞ as λ → 1 ✓

**In KK-cone coordinates:** λ = sin(√2 r); ranges 0 at r=0 to 1 at r=r*=π/(2√2)

---

### λ_D — DECOHERENCE DISTINGUISHABILITY (Paper 1 §5, already subscripted)

**Definition:** λ_D = 1 − |⟨E_i|E_j⟩| (off-diagonal environment overlap decay)

**Range:** [0, 1], same direction as λ

**Paper 1 states:** "we work in the gauge λ ≡ λ_D" — so bare λ is used for λ_D in P1

**Action:** No change needed; Paper 1 is correct. Keep λ_D as the explicit form and λ as the gauge-fixed shorthand.

---

### λ_A — WARP-FACTOR AMPLITUDE SQUARED (renamed from bare λ in Paper 2B §7)

**Definition:** λ_A = A(r)² = cos²(√2 r)

**Range:** [1, 0] — OPPOSITE to EGY λ

**Direction:** 1 at brane (coherent), 0 at throat (classical). Decreases as decoherence proceeds.

**Relationship to EGY λ:** λ_A = 1 − λ² (single-mode KK-cone); equivalently, A(r) = √(1−λ²)

**Role in Paper 2B:** Warp-factor coupling strength in the frame-lag force F_lag = λ_A · T_μr · G^μν a_ν. The key result λ_A · T_μr = O(1) (frame-lag force is warp-independent) comes from λ_A ~ A² and T_μr ~ A^{-2}.

**Papers:** P2B §7.3, §7.9; formerly called "λ" or "λ(r)" in these sections

**Required change:** Replace λ → λ_A everywhere in Paper 2B §7 derivations. Update Ansatz A*:
> OLD: "Ansatz A*: λ = A(r)² = cos²(√2 r)"
> NEW: "Ansatz A*: λ_A = A(r)² = 1 − λ², where λ is the EGY coordinate sin(√2 r)"

---

### λ_w — WARP-FACTOR COUPLING IN H_int (Paper 2B §7.9, formerly λ(r) in H_int)

**Definition:** The coupling coefficient in H_int = λ_w Σ A_α ⊗ B_α

**Note:** After the §7.9 verification pass (2026-05-02), the decision was to write H_int WITHOUT an explicit warp-factor coupling, absorbing it into Γ_dec. If H_int carries an explicit coupling, that coupling should be labeled λ_w (or λ_A if the coupling equals A(r)²). If no explicit coupling, λ_w does not appear.

**Papers:** P2B §7.9 (optional, depending on revision)

---

### λ_bdry — BOUNDARY LAYER AMPLITUDE (Paper 2C, already partially labeled)

**Definition:** The λ coefficient in T^(eff)_μν = λ_bdry (√-γ/√-g) Π_μν |T_M|² δ_⊥(x, ∂M)

**Role:** Holographic source normalization; λ_bdry · |T_M|² has units of stress-energy.

**Distinct from:** EGY λ (coherence parameter) and λ_A (warp coupling)

**Papers:** P2C §RC1.1–§RC1.3; RC-2 resolution document

**Note:** Already partially labeled in omnibus #13a: "λ_bdry [M³] vs λ_dist [dimensionless] collision."

---

### λ_dist — DISTRIBUTED DISTINGUISHABILITY (Paper 2C, already partially labeled)

**Definition:** Dimensionless distributed decoherence parameter in the bulk EOM

**Distinct from:** λ_bdry (dimensional boundary quantity)

**Papers:** P2C §RC1.3; RC-2 notation box

---

### λ_K, λ_n — KK MODE EIGENVALUES (Paper 2C, already labeled)

**Definition:** λ_K = KK eigenvalue index; λ_n = nth KK mode eigenvalue

**No change needed** — already subscripted and distinct.

---

### δλ — FRAME-LAG DISPLACEMENT (Paper 2A §2.2)

**Definition:** Separation between observed λ and equilibrium λ; measures frame-lag vs. decoherence progress

**No change needed** — already distinct via δ prefix.

---

### λ_ptr — POINTER-STATE NON-OCCUPANCY (Paper 2B §7.9, new label)

**Definition:** 1 − ⟨ψ_ptr|ρ_S|ψ_ptr⟩, where |ψ_ptr⟩ is the pointer state

**Range:** [0, 1]; 1 = fully coherent (not in pointer state), 0 = fully in pointer state

**Direction:** OPPOSITE to EGY λ

**Problem:** §7.9 line 94 was using bare λ for this quantity. Since it decreases to 0 at the pointer state, it is NOT the EGY λ. Must be relabeled λ_ptr.

**Note:** The Lindblad (7.9.8) preserves populations (dρ₁₁/dt = 0 for pointer-basis dephasing), so λ_ptr does NOT evolve under (7.9.8). This confirms the §7.9 derivation error: the logistic dλ/dt = −Γ_dec λ(1−λ) cannot come from (7.9.8) if λ ≡ λ_ptr.

**Papers:** P2B §7.9 (draft only); must be replaced in the §7.9 rewrite.

---

## The Ansatz A* Correction

The statement "Ansatz A*: λ = A(r)²" is the source of all conflicts. The correct formulation in Papers 2A/2B is:

**Ansatz A* (corrected):** In the KK-cone geometry, the EGY coherence parameter λ satisfies:
$$\lambda = \sin(\sqrt{2}\,r), \qquad A(r) = \cos(\sqrt{2}\,r) = \sqrt{1-\lambda^2}$$

Equivalently: $\lambda_A := A(r)^2 = 1 - \lambda^2$ is the warp coupling, NOT the EGY parameter.

The frame-lag invariance result (λ_A · T_μr = O(1)) becomes:
$$(1-\lambda^2) \cdot T_{\mu r} \sim A^{-2} \cdot A^2 = O(1) \checkmark$$

---

## Summary: What Changes Where

| Paper | Section | Old notation | New notation | Note |
|---|---|---|---|---|
| P1 | All | λ (EGY) | **λ** (KEEP) | No change |
| P1 | §5 initiation | λ_D | **λ_D** (KEEP) | Already subscripted |
| P2A | §2.2 | λ, δλ | **λ, δλ** (KEEP) | No change |
| P2A | §2.2 action | λ G_{AB}^{(cross)} | **λ_A G_{AB}^{(cross)}** | coupling = λ_A |
| P2B | §7.3, §7.4 | λ(r) = A²(r) | **λ_A** | critical rename |
| P2B | §7.9 line 94 | λ = 1−⟨ptr\|ρ\|ptr⟩ | **λ_ptr** | opposite direction |
| P2B | §7.9 H_int | λ(r) coupling | **no explicit λ** (absorbed into Γ_dec) | per §7.9 revision |
| P2B | Ansatz A* | λ = A(r)² | **λ_A = 1−λ²; λ = sin(√2 r)** | direction fix |
| P2C | §RC1 T^(eff) | λ (boundary) | **λ_bdry** | already partially done |
| P2C | RC-2 | λ_dist | **λ_dist** (KEEP) | already distinct |
| P2C | §7, §8 | λ_K, λ_n | **λ_K, λ_n** (KEEP) | already distinct |

---

## Editorial Pass Required (NOT a §7.9 quick fix — full manuscript pass)

The Ansatz A* correction propagates through:
1. Paper 2B §7 entire section: replace λ → λ_A where it means A(r)²
2. Paper 2A §2.2 action: the cross-term coupling coefficient λ G_{AB}^{(cross)} — should it be λ or λ_A?
3. Paper 2B §5 SC1/SC2: use of λ in Markov ratio R_Markov
4. All OPEN_ITEMS_LEDGER entries referencing "λ = A²"
5. Paper 2B §7.9: full rewrite needed (separate task)

**Scope estimate:** ~2–3 editorial sessions. Not a patch job.

---

## Session Log

- 2026-05-02: Disambiguation document created after §7.9 adversarial verification revealed: (1) direction inversion between EGY λ and KK-cone λ_A = A(r)²; (2) §7.9 line-94 λ_ptr conflated with EGY λ; (3) logistic dλ/dt inconsistent with Lindblad when λ = λ_ptr. Root cause: "Ansatz A*: λ = A(r)²" was stated as an identification, not a complementarity (λ_A = 1−λ²).
