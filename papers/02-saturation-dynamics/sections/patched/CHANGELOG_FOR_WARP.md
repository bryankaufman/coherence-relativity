# Wave 1 Surgical Patch — Changelog for Warp Review

**Date**: 2026-03-04
**Patches applied by**: Claude Cowork (Opus subagents)
**Patch script source**: Warp's surgical review (sections A–F)

---

## Addendum (2026-03-05) — Appendix A Reference Asset

- Added patched appendix asset for future reuse:
  - `papers/02-saturation-dynamics/sections/patched/paper2_appendix_A_block_inverse_PATCHED.md`
- Draft source retained:
  - `papers/02-saturation-dynamics/sections/drafts/paper2_appendix_A_block_inverse_DRAFT.md`
- Linked from §2.2 draft inverse-metric note:
  - `papers/02-saturation-dynamics/sections/drafts/paper2_section_2.2_delta_lambda_DRAFT.md`

---

## §4.0 — KK-Cone Model (B1–B4)

### Equations Removed → Replaced

| Old | New | Change |
|-----|-----|--------|
| Eq. 4.1: `ds² = e^{2A(r,z)}(−dt² + dx₁² + dx₂² + dx₃²) + dr² + r²(dθ² + sin²θ dφ²) + L²(dψ + cosθ dφ)²` | Eq. 4.1: `ds²₍₅₎ = −dz² + dr² + A(r,z)² γᵢⱼ dθⁱ dθʲ` + Eq. 4.1b (Hopf parameterization of γᵢⱼ) | 8 coords → 5 coords. z replaces {t, x₁, x₂, x₃}. S³ metric γᵢⱼ encodes Hopf internally. |
| Eq. 4.2: 4-part decomposition (4D Mink + radial + S² + Hopf) | Eq. 4.2: 3-part decomposition (brane-normal + radial + warped S³) + Eq. 4.3: brane-induced metric | Correct dimensional splitting. Brane = 4D (z + S³). |
| "4 + 1 + 3 = 5" arithmetic | Two coordinate registry tables (bulk 5D, brane 4D) | Unambiguous dimension count. |
| Cone-tip: Minkowski prefactor at r=0 | Cone-tip: S³ pinch-off with A(r,z) case analysis (smooth/singular/quantum) | Matches new metric. |

### Topology Line
- **Old**: R^{1,3} × R₊ × (S² × S¹)
- **New**: R × R₊ × S³

### Surviving References to Old Coordinates
- One mention of {t, x₁, x₂, x₃} in clarifying context only ("z replaces the old..."). Not used as coordinates.

---

## §2.4 — Mixed-State Born Rule (C1–C5)

### Equations Removed → Replaced

| Old | New | Change |
|-----|-----|--------|
| Eq. 2.4.2: `G_{AB} = ∂_A ∂_B [log⟨Ψ\|Ψ⟩]` | Direct invocation of Paper 1 result: `P(a\|Ψ) = ⟨Ψ\|(Πₐ ⊗ I_E)\|Ψ⟩` | Removed invalid log-of-scalar. No FS metric computation needed at this step. |
| §2.4.4 derivation: `P(a\|ρ) = Tr_E[⟨Ψ\|(Πₐ ⊗ I_E)\|Ψ⟩]` (trace of scalar) | 5-step chain: sandwich → Tr_{SE} → partial trace → purification → Tr(ρ Mₐ) | Each step justified individually. Key: convert ⟨Ψ\|·\|Ψ⟩ to full trace first. |
| Eq. 2.4.5: `Mₐ = Tr_A(Π̃ₐ)` | `Mₐ = V† Π̃ₐ V` (isometry form) | Standard Naimark. |
| §2.4.6 POVM derivation (double-trace, unjustified \|0_A⟩) | Clean 3-line: `Tr_S(ρ V† Π̃ₐ V) = Tr_{SA}[(V ρ V†) Π̃ₐ]` | No ancilla state needed explicitly. |
| `dim(H_A) ≤ dim(H_S)` | `dim(H_A) ≤ \|X\| · dim(H_S)` (or "finite-dimensional ancilla exists") | Correct general bound. |

### Sections Preserved (no changes needed)
- §2.4.1 Introduction ✓
- §2.4.2 Purification Theorem (Theorem 2.4.1) ✓
- §2.4.5 Purification Independence (Theorem 2.4.2) ✓
- §2.4.7 Circularity Check (updated references to corrected derivation steps) ✓

---

## §2.1 — T_{MΣ} Cross-Term (D1–D8)

### Equations Removed → Replaced

| Old | New | Change |
|-----|-----|--------|
| T_AB used for both full tensor and cross-term | Q_AB = G_AB + i F_AB (quantum geometric tensor); T_{MΣ} reserved for cross-term G_{μa} only | Symbol overload eliminated. |
| Eq. 2.1.15: Ω_AB (conflated connection + curvature) | A_A = i⟨ψ\|∂_Aψ⟩ (connection); F_AB = ∂_A A_B − ∂_B A_A (curvature) | Berry connection vs. curvature now distinct. |
| Eq. 2.1.19: Φ_Berry = ∮ Ω_AB dX^A | Φ_Berry = ∮ A_A dX^A = ∫∫ F_AB dX^A ∧ dX^B (by Stokes) | Line integral of connection, not curvature. |
| Eq. 2.1.25: Ω'_AB = Ω_AB + ∂_Aα ∂_Bα | A_A → A_A + ∂_Aα; F_AB → F_AB (gauge-invariant) | Correct gauge transformation. |
| Eq. 2.1.22: T^{μa} = G^{μν} G^{ab} T_{νb} | T^{μa} = G^{μB} G^{aC} T_{BC} (full inverse metric) | Non-block-diagonal metric requires full G^{AB}. |
| §2.1.9: Kähler potential K = log⟨ψ\|ψ⟩, G_AB = ∂_A ∂_B K (Eqs. 2.1.39–2.1.42) | Brief note: Kähler descent to real M×Σ not assumed; deferred to future work | Removed invalid claim for real manifold. |
| §2.1.7 toy model: γ(t) variable but γt in exponent (inconsistent) | γ₀ constant; T_{tξ} = 0 in uniform case. Position-dependent case deferred to §2.2. | Honest about what the toy model shows. |
| Eq. 2.1.45: T_{μa} ∝ A^{-2} T^{(0)}_{μa} (stated as derived) | Reframed as hypothesis: "Under the ansatz that ∂_μ → A^{-1} ∂_μ..." Verification deferred to §7. | Honest epistemic status. |

### Sections Preserved (no changes needed)
- §2.1.1–2.1.3 (state map, derivatives, metric computation) ✓
- §2.1.4 (physical interpretation) ✓
- §2.1.8 (inverse metric, action principle) ✓ (notation updated)
- Summary and Outlook ✓ (updated for Q_AB)

---

## Unresolved Math Blockers Remaining After Patch

| Item | Status | Notes |
|------|--------|-------|
| §4.0 Eq. 4.1b: Hopf parameterization convention | ⚠️ NEEDS VERIFICATION | Standard form used but should cross-check against Paper 3's convention |
| §2.1 Warp scaling A^{-2} | ⚠️ HYPOTHESIS | Stated as ansatz, deferred to §7. Cannot be resolved until EoM (§2.2) written. |
| §2.1 Kähler descent | ⚠️ DEFERRED | Open question; not blocking for Paper 2 core. |
| §2.1 Toy model (position-dependent γ) | ⚠️ DEFERRED to §2.2 | The interesting physics (T_{tξ} ≠ 0) requires the position-dependent case. |
| §2.4 Naimark ancilla bound | ✅ FIXED | Correct general bound stated. |
| §4.0 Cone-tip resolution | ⚠️ DEFERRED | Requires quantum gravity input. Correctly marked as open. |

---

## Numbering Collisions Introduced

**None detected.** All three files use independent equation namespaces:
- §4.0: Eq. 4.1, 4.1b, 4.2, 4.3
- §2.4: Eq. 2.4.1 through 2.4.6
- §2.1: Eq. 2.1.1 through 2.1.43

No cross-section numbering conflicts.

---

## File Sizes (Pre vs. Post Patch)

| File | Original | Patched | Delta |
|------|----------|---------|-------|
| §4.0 KK-Cone | 14,959 bytes | 16,255 bytes | +1,296 (coord tables, clarifications) |
| §2.4 Born Rule | 14,953 bytes | 9,509 bytes | −5,444 (removed malformed derivations, tightened) |
| §2.1 T_{MΣ} | 24,407 bytes | 27,738 bytes | +3,331 (Q_AB intro, corrected gauge, deferred notes) |

---

## Next Steps for Warp

1. **Review patched files** — all three in `/sessions/clever-vibrant-cray/patch-outputs/`
2. **Verify Hopf parameterization convention** (§4.0 Eq. 4.1b) against Paper 3
3. **Clear §4.0 and §2.1 from draft_blocked → draft** if satisfied
4. **Medium fixes still pending**: §3.1 (quantum Navier-Stokes), §3.2 (uniqueness overclaim)
5. **Downstream blockers**: §4.4 and §6.0 inherit from §4.0 — can now be re-evaluated
6. **Wave 2 gate**: §2.2 now unblocked if §2.1 clears review
