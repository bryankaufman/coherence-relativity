# Paper 1 v6 — Cross-Paper Conflict Audit
**Date**: 2026-04-26
**Scope**: All known notation/framing conflicts spanning Papers 1 through 2C
**Action**: Resolve all conflicts in Paper 1 v6 before arXiv submission

---

## Severity levels
- 🔴 CRITICAL: Affects fundamental notation throughout; reader will be confused in Paper 2
- 🟡 SIGNIFICANT: Affects cross-paper reading; needs explicit resolution
- 🟢 MINOR: Already partially addressed or low impact

---

## Issue 1 — λ Orientation Flip 🔴 CRITICAL

**What Paper 1 (v4) says:**
- λ = EGY distinguishability = √(1 - |⟨W_L|W_R⟩|²)
- λ=0: coherent (paths indistinguishable, double-slit open) — "fully coherent endpoint"
- λ=1: classical (pointer state reached, which-path information complete) — "rigidity of classical records"
- Confirmed: line 207 "metric diverges as λ→1 expresses the rigidity of fully established classical records"
- Confirmed: line 361 "Frames near the pointer limit (λ→1) carry stable records"

**What Paper 2A §2.2 says:**
- λ = "distinguishability parameter" / coupling strength
- λ=0: "classical limit — sectors completely distinguishable (separable), T_MΣ effectively zero"
- λ=1: "quantum regime — sectors maximally coupled"

**Conflict:** Paper 1 says λ=1 classical; Paper 2A §2.2 says λ=0 classical. OPPOSITE orientations.

**Root cause:** Two physically distinct quantities share the symbol:
- Paper 1 λ: path-distinguishability (0=coherent, 1=classical) — EGY convention
- Paper 2A §2.2 λ: sector-coupling strength (0=decoupled/classical, 1=coupled/quantum)

**Resolution (v6):**
- Keep Paper 1's EGY convention as the canonical definition throughout the series.
- Paper 2A §2.2 must rename its coupling parameter to μ or κ_coupling.
- Paper 2A §1.6 cross-paper table should note: "Paper 2A §2.2 coupling parameter κ(x,ξ) satisfies κ = 1 - λ in the pure-state limit; λ throughout this series follows the EGY convention."
- Paper 1 v6: add one sentence to the λ definition (§metric) noting the coupling-convention usage in Paper 2A §2.2 is renamed.
- **Paper 1 change needed:** Add footnote or parenthetical: "Note: Paper 2A introduces a derived coupling parameter κ(x,ξ) related by κ = f(λ); throughout this series, λ always refers to the EGY distinguishability with λ=0 coherent, λ=1 classical."

---

## Issue 2 — T_AB → Q_AB Promotion 🟡 SIGNIFICANT

**What Paper 1 says:**
- T_AB = G_AB + Ω_AB on Σ alone (Definition 4)
- Forward pointer to Paper 2 for the M × Σ extension (line 247)

**What Paper 2A introduces:**
- Q_AB = G_AB + iF_AB on M × Σ (the "true promotion" of T_AB)
- T_MΣ = G_μa (cross-term, new object, no P1 analog)
- Paper 2A §2.1 line 384 says "Q_AB replaces the previous ambiguous use of T_AB"

**Conflict:** Paper 1 defines T_AB; Paper 2A says it's been replaced. A reader going P1→P2A needs to understand the T_AB→Q_AB promotion explicitly.

**Resolution (v6):**
- Paper 1 §T_AB definition: add sentence "In Paper 2, T_AB is promoted to Q_AB = G_AB + iF_AB on M × Σ, where the antisymmetric part Ω_AB is reinterpreted as the imaginary component iF_AB of the quantum geometric tensor; see Paper 2 §1.6 for the precise correspondence."
- Paper 1 §conclusion or discussion: brief note that T_AB is the Σ-restricted version of Q_AB.

---

## Issue 3 — Ω_AB vs Berry Curvature Framing 🟡 SIGNIFICANT

**What Paper 1 says:**
- Line 236: "Ω_AB is NOT the Berry curvature of the state. Berry curvature... lives on the external parameter manifold. Ω_AB is instead the curvature of the frame bundle over Σ."
- But line 240–243: the formula for Ω_AB = 2 Im[⟨∂_Aψ|∂_Bψ⟩] IS the Berry curvature formula, and Paper 1 acknowledges it: "which is the Berry curvature two-form on projective Hilbert space when restricted to a single state; its role here as frame-bundle curvature is distinct."

**What Paper 2A does:**
- Introduces F_AB with the same formula: F_AB = Im[⟨∂_Aψ|∂_Bψ⟩] and calls it "Berry curvature" without the distinction Paper 1 makes.
- Q_AB = G_AB + iF_AB, where F_AB is the Berry curvature.

**Conflict:** Paper 1 says Ω_AB ≠ Berry curvature (different role: frame-bundle vs state-vector holonomy). Paper 2A calls F_AB the Berry curvature using the same formula. The distinction Paper 1 draws is real but subtle; a reader may think P1's Ω_AB and P2A's F_AB are different objects when they're the same formula with a reinterpretation.

**Resolution (v6):**
- Paper 1 should reframe: instead of "Ω_AB is NOT the Berry curvature," say "Ω_AB has the same algebraic form as the Berry curvature two-form (Eq. X), but its geometric interpretation differs: here it encodes frame-bundle holonomy (pointer-observable transport) rather than state-vector holonomy."
- Add: "In Paper 2, this object is reidentified as the F_AB component of the quantum geometric tensor Q_AB = G_AB + iF_AB; the distinction between pointer-transport holonomy (Paper 1) and state-vector holonomy (standard Berry curvature) is addressed in Paper 2 §2.1."
- This resolves the confusion without requiring Paper 1 to be fully wrong.

---

## Issue 4 — M as Primitive (P1) vs M as Derived (P3, P4) 🟡 SIGNIFICANT

**What Paper 1 says:**
- Notation table: "𝓜 — Emergent spacetime (primitive)" (line 101)
- Abstract: "Physical reality is described on a joint manifold 𝓜 × Σ, where 𝓜 is emergent spacetime"

**What later papers do:**
- Papers 3–4 derive M from (H, ∂𝒞, T_AB): H is fundamental, M is reconstructed
- The H ⊋ M ontological claim makes M strictly derived, not primitive

**Conflict:** "Primitive" in Paper 1 is inconsistent with the later program where M is derived from H.

**Resolution (v6):**
- Change "𝓜 — Emergent spacetime (primitive)" to "𝓜 — Emergent spacetime (treated as a primitive input in this paper; derived from Hilbert-space data in the full HCR program, see Paper 3)"
- Add one sentence in §introduction: "We treat 𝓜 as given in this paper; later papers in the series will derive the manifold structure from the coherence geometry of H."
- This is a one-sentence clarification, not a structural change.

---

## Issue 5 — CR vs HCR Naming 🟡 SIGNIFICANT

**What Paper 1 v4 says:**
- Abstract: "We call the broader framework Holographic Coherence Relativity (HCR), while using 'coherence relativity' for the frame-relativity principle developed in this paper"
- Command `\CR{}` = "Coherence Relativity" (line 25); `\HCRname{}` and `\HCR{}` also defined
- Mixed usage throughout: some places say "CR" or "coherence relativity", others say "HCR"

**What Papers 2A–2C use:**
- Consistently use "HCR" (Holographic Coherence Relativity) and "KCR" (Kaluza-Coherence Relativity cone)
- Paper 2A v4 says "Paper 2A of the Holographic Coherence Relativity (HCR) series"

**Resolution (v6):**
- Settle on "HCR" throughout. The abstract framing in v4 ("we call the broader framework HCR") is correct.
- Check all `\CR{}` instances and replace with `\HCR{}` or "HCR" where appropriate.
- Define `\HCR{}` as the primary macro; keep `\CR{}` only for historical references to "coherence relativity" as the frame-relativity principle.
- Ensure `\newcommand{\HCR}{Holographic Coherence Relativity}` and `\newcommand{\CR}{coherence relativity}` are both defined clearly.

---

## Issue 6 — Born Rule Derivation Reconciliation 🟡 SIGNIFICANT

**What Paper 1 derives:**
- Born rule via A1–A4 + frame-invariance + additivity + continuity
- Independent of SCF, COV, Gleason/Busch in Paper 2C

**What Paper 2C derives:**
- Born rule via SCF → COV → frame-noncontextuality → Gleason/Busch (Theorem 6.1, Corollary 6.2)

**Potential confusion:** Two derivation routes exist. Are they two independent proofs of the same theorem, or is one strictly stronger?

**Resolution (v6):**
- These are complementary, not competing. Paper 1's derivation establishes Born at the coherence-frame level (axioms A1–A4 on Σ alone). Paper 2C's derivation establishes it from the dynamical SCF condition (on M × Σ). The Paper 2C chain implies Paper 1's result in the SCF-saturated sector.
- Paper 1 needs one sentence: "A dynamical derivation of the Born rule from the self-consistency fixed-point condition on M × Σ, recovering the present axiomatic result as a consequence, is given in Paper 2C §6."

---

## Issue 7 — Signature Count (7 vs 8) 🟢 MINOR

**Paper 1 v4 abstract:** "eight experimentally testable signatures"
**Paper 1 v4 WARP.md:** "seven deliverables" (old WARP.md, may be outdated)
**Paper 2A §1.2:** "Eight Deliverables"

**Resolution:** Count is 8 (the Frauchiger-Renner/Proietti signature was added as the eighth). Confirm the abstract, predictions section, and WARP.md all say 8. This is likely already correct in v4.

---

## Issue 8 — Σ Disambiguation 🟢 ALREADY IN V4

Paper 1 v4 line 157 already says: "Throughout this paper, Σ ≡ Σ_coh(H) = U(d)/T^d... distinct from a string worldsheet Σ_ws... later papers will use the more explicit notation Σ_coh(H) whenever multiple meanings of Σ appear at once."

✅ No change needed for v6.

---

## Issue 9 — F (drift field) vs F (frame) Disambiguation 🟢 ALREADY IN V4

Paper 1 v4 Table 1 line 128: "F^A — Drift field on Σ (distinct from frame F)"

✅ No change needed for v6.

---

## Issue 10 — s (arc length) vs σ (path parameter) 🟢 ALREADY IN V4

Paper 1 v4 Table 1 line 130: "σ — Action path parameter (distinct from arc s)"

✅ No change needed for v6.

---

## Summary of v6 Changes Required

| Issue | Type | Change location | Effort |
|---|---|---|---|
| 1. λ orientation | 🔴 CRITICAL | §metric λ definition + notation table | 2–3 sentences |
| 2. T_AB → Q_AB | 🟡 SIGNIFICANT | §T_AB definition (§frames) + §discussion | 1 sentence each |
| 3. Ω_AB framing | 🟡 SIGNIFICANT | §T_AB antisymmetric part | Reframe 2 sentences |
| 4. M as primitive | 🟡 SIGNIFICANT | Notation table + 1 intro sentence | 2 sentences total |
| 5. CR vs HCR | 🟡 SIGNIFICANT | Macros + throughout | Macro fix + scan |
| 6. Born derivation | 🟡 SIGNIFICANT | §conclusion or §discussion | 1 sentence |
| 7. Signature count | 🟢 MINOR | Abstract + predictions table | Verify only |
| 8–10 | 🟢 DONE | — | No change |

**Total new text for v6:** ~10–15 sentences across 5–6 locations. This is a precision revision, not a restructuring.

---

## Proposed v6 Changelog (for commit message)

```
Paper 1 v6 — Cross-paper notation reconciliation

Critical fixes:
- λ: clarify EGY convention (λ=0 coherent, λ=1 classical) is canonical
  throughout the HCR series; Paper 2A §2.2 coupling parameter renamed κ
- T_AB: add forward pointer to Q_AB = G_AB + iF_AB in Paper 2 §1.6
- Ω_AB: reframe as "same formula as Berry curvature but distinct geometric
  role"; resolution in Paper 2 §2.1

Significant fixes:
- 𝓜: "primitive in this paper; derived from H in Paper 3" (one sentence)
- HCR/CR: establish HCR as primary name throughout; standardize macros
- Born: one sentence pointing to Paper 2C §6 dynamical derivation

Minor:
- Verify signature count = 8 throughout
- No changes to Σ, F^A, s/σ disambiguations (already correct in v4)
```
