# MOC — HCR Derivations & Equations
*Index of all derivation documents, equation references, and verification memos.*

---

## Primary Reference
- [[notes/EQUATIONS_REFERENCE]] — master equation list with LaTeX labels (start here)
- [[notes/key-insights]] — accumulated key insights
- [[notes/REVIEW_CROSS_REFERENCE]] — cross-reference to reviewer comments
- [[notes/derivations/kappa_rad_verification_spike_log]] — kappa_rad verification

---

## Paper 1 Derivations
- [[papers/01-coherence-frames/BORN_RULE_DERIVATION]] — Born rule via frame-splitting
- [[papers/01-coherence-frames/main]] Sec. IV — primary derivation
- Key result: Theorem 4.1 — Born rule as unique frame-invariant measure

---

## Paper 2A Derivation Chain (active)

### G1 Phase Results (2026-04-27)
- [[papers/02-saturation-dynamics/G1_SCOPING_BRIEF_2026-04-27]] — scoping
- [[papers/02-saturation-dynamics/G1_SCOPING_RESULT_2026-04-27]]
- [[papers/02-saturation-dynamics/G1_PHASE1_TASK_2026-04-27]]
- [[papers/02-saturation-dynamics/G1_PHASE1_RESULT_2026-04-27]]
- [[papers/02-saturation-dynamics/G1_PHASE2_TASK_2026-04-27]]
- [[papers/02-saturation-dynamics/G1_PHASE2_RESULT_2026-04-27]]
- [[papers/02-saturation-dynamics/G3_RC3_TASK_2026-04-27]]
- [[papers/02-saturation-dynamics/G3_RC3_RESULT_2026-04-27]]
- [[papers/02-saturation-dynamics/G3_RC3b_RESULT_2026-04-27]]
- [[papers/02-saturation-dynamics/G3_RC3c_RESULT_2026-04-27]]

### RC Series (Rigorous Computation series)
- [[papers/02-saturation-dynamics/RC1_VERIFICATION_MEMO_2026-04-17]]
- [[papers/02-saturation-dynamics/RC2_DERIVATION_2026-04-17]] — coordinate-invariant Markov criterion
- [[papers/02-saturation-dynamics/RC2_RECONCILIATION_MEMO_2026-04-17]]
- [[papers/02-saturation-dynamics/RC2_RESOLUTION_2026-04-26]]
- [[papers/02-saturation-dynamics/RC3_DERIVATION_2026-04-18]]
- [[papers/02-saturation-dynamics/RC5_LAMBDA_DERIVATION_2026-04-18]]
- [[papers/02-saturation-dynamics/RC6_ALPHA_AUDIT_2026-04-18]]
- [[papers/02-saturation-dynamics/RC7_ALPHA_GEOM_DERIVATION_ATTEMPT_2026-04-18]]
- [[papers/02-saturation-dynamics/RC8_5D_EH_EXPANSION_2026-04-18]]

### Derivation Documents
- [[papers/02-saturation-dynamics/DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20]] — synthesis
- [[papers/02-saturation-dynamics/DERIVATION_C4_FOKKER_PLANCK_2026-04-20]] — C4 Fokker-Planck
- [[papers/02-saturation-dynamics/DERIVATION_C4_FROM_SCF_2026-04-20]] — C4 from SCF
- [[papers/02-saturation-dynamics/DERIVATION_COV_CHECK_2026-04-19]] — covariance check
- [[papers/02-saturation-dynamics/DERIVATION_EQ_8_4_5_2026-04-18]] — Eq 8.4.5
- [[papers/02-saturation-dynamics/DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20]] — SCF fixed point
- [[papers/02-saturation-dynamics/DERIVATION_SCF_NONCONTEXTUALITY_2026-04-19]] — SCF non-contextuality
- [[papers/02-saturation-dynamics/DERIVATION_SU2_BORN_LEMMA_2026-04-20]] — SU(2) Born lemma

### Synthesis & Reconciliation
- [[papers/02-saturation-dynamics/SYNTHESIS_EMANATION_INSTANTIATION_LOCUS_2026-04-26]]
- [[papers/02-saturation-dynamics/SYNTHESIS_EMANATION_INSTANTIATION_LOCUS_DRAFT_2026-04-27]]
- [[papers/02-saturation-dynamics/M1_2C_SEC5_PROSE_UPDATE_2026-04-26]]
- [[papers/02-saturation-dynamics/M2_SPEKKENS_AND_LEMMA1_2026-04-26]]
- [[papers/02-saturation-dynamics/M3_HU_VERDAGUER_PARA_2026-04-26]]
- [[papers/02-saturation-dynamics/METHODOLOGICAL_PRINCIPLE_MEDIATED_EMERGENCE_2026-04-26]]

---

## Paper 2C Derivations
- [[papers/02C-holographic-structure/DERIVATION_KCBS_2026-04-19]] — KCBS contextuality
- [[papers/02C-holographic-structure/DERIVATION_PROIETTI_CR_2026-04-18]] — Proietti CR
- [[papers/02C-holographic-structure/DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20]]
- [[papers/02C-holographic-structure/DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20]]
- [[papers/02C-holographic-structure/VERIFICATION_FR_HOLONOMY_2026-04-18]] — FR holonomy
- [[papers/02C-holographic-structure/VERIFICATION_FR_HOLONOMY_OPUS46_2026-04-18]]

---

## Session-Level Derivation Notes
Quick derivation work from agent sessions (in `memory/kb/`):
- [[memory/kb/SESSION_2026-04-19_COV_CHECK_CANDIDATE_SCF]]
- [[memory/kb/SESSION_2026-04-19_T_MSigma_HOLOGRAPHIC_BORN_RULE]]
- [[memory/kb/SESSION_2026-04-20_SCF_FIXED_POINT_SUBSTITUTION]]
- [[memory/kb/SESSION_2026-04-10_GEOMETRIC_LAMBDA_ANALYSIS]]
- [[memory/kb/SESSION_2026-02-07_FIGURE_AUDIT]] — U-shape metric, figure audit
- [[memory/kb/SESSION_2026-02-12_ESTIMATE_AUDIT]] — R_Σ=8, s*=0.72

---

## Key Equations Quick Reference
(From [[notes/EQUATIONS_REFERENCE]])

| Label | Equation | Where |
|-------|----------|-------|
| EGY | λ ≡ √(1−\|⟨W_L\|W_R⟩\|²) | P1 Sec II |
| G_λλ N=1 | G_λλ = 1/[2(1−λ²)] | P1 Sec II |
| Born | p_i = \|⟨ψ_i\|Ψ⟩\|² (frame-invariant) | P1 Thm 4.1 |
| T_AB | full block matrix on M×Σ | P2A Sec 2 |
| V(λ) | quasipotential = ∫ √G_λλ dλ | P1 Eq. 11 |
| δ-λ | d(δ-λ)/dt = −κ(λ)·δ-λ + ξ(t) | P2A Sec 3 |
| Markov | G_MM^new/G_λλ = 1 at λ* | P2A Sec 3.3 |
