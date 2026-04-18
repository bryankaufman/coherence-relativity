# Paper 2 — Open Items Ledger
*2026-04-17 — consolidated from status marker triage across 2A, 2B, 2C*

This ledger collects every item that is currently UNTESTED, OPEN, CONJECTURED, ASSUMED, or CONTINGENT across the three Paper 2 manuscripts. Nothing here is process tracking — each entry is a physics question that must eventually be resolved, verified, or explicitly deferred.

---

## DEFERRED (future work, not blocking Paper 2 completion)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 1 | **λ first-principles derivation** | 2A §2.2 (L731, L1332) | Currently phenomenological. Needs decoherence-rate Lagrangian or information-theoretic derivation. |
| 2 | **Quantization of the M × Σ system** | 2A §2.2 (L1365) | Beyond Paper 2 scope. Canonical, path-integral, or geometric quantization approaches identified. |
| 21 | **Proof of Conjecture 2.5.3 (Born rule as unique coherence-frame invariant)** | 2A §2.5.5, Box 2.5.A | *Paper N candidate.* Three requirements identified in Box 2.5.A: (1) precise definition of coherence-frame symmetry group $\mathcal{G}_{\text{CR}}$ and its orbit structure; (2) noncontextuality and regularity assumptions translated into HCR language; (3) uniqueness lemma (Gleason/envariance-type, adapted to $\mathcal{G}_{\text{CR}}$). Most direct path: map the pointer-sector swap symmetry (§2.5.6) onto Zurek's envariance construction (2003) and extend from qubit to general $\mathcal{H}$. Model verification complete (dephasing + amplitude-damping). Pursue as standalone paper if not resolved by existing literature. |

---

## UNTESTED (verification deferred to 2B — blocking 2B completion)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 3 | **A⁻² cross-term scaling hypothesis** | 2A §2.2 (L606) | Ansatz follows dimensionally from A⁻¹ derivative scaling. Needs EOM verification in 2B. |
| 4 | **λ ~ A² warp-factor scaling** | 2A §2.2 (L1342) | Key verification point — does KK-Cone metric confirm this? Deferred to 2B. |

---

## BLOCKING (must be resolved for 2B to close)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 5 | ~~**SC1/SC2 rewrite to KCR interval formulation**~~ | 2B | **RESOLVED.** SC1 structurally satisfied (flat Minkowski slices). SC2 structurally satisfied (bounded interval, divergent volcano potential). §5.1 and §5.2 written. |
| 6 | **Scale factor s dynamical mechanism** | 2B §3 (L1123) | Shape RESOLVED. Scale PARTIALLY RESOLVED — Casimir gives the value but the dynamical mechanism driving s to that value is not yet demonstrated. |

---

## CONTINGENT ON PAPER 3

| # | Item | Source | Notes |
|---|------|--------|-------|
| 7 | **Field content on interval** | 2B §3 (L523) | Determined by Paper 3 phase transition (Axiom B) and symmetry. |
| 8 | **P3-H3: Bundle-selection statement** | 2B §4 (L613) | Interface contract — Paper 3 must clarify whether only c₁=1 Hopf fiber is dynamically selected. |
| 9 | **P3-H4: Effective-source projection rule** | 2B §4 (L615) | Interface contract — projection map from M × Σ dynamics to 4D effective source terms. |

---

## OPEN (no resolution path yet)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 10 | **c₁ = 1 uniqueness** | 2B §3 (L525) | Minimality argument unchanged; higher-c₁ bundles possible at higher energies. |
| 11 | **k_c identification for CMB (d vs k_c discrepancy)** | 2C §7 (L564 in triage) | RC-3 scope. The cutoff scale identification doesn't match between derivations. |
| 12 | ~~**δT_M/δg^μν extraction (RC-2)**~~ | 2C §7 | **PARTIALLY RESOLVED 2026-04-17.** Formal adiabatic-perturbation expression derived; KCR-Cone evaluation shows T_M(r) ∝ A²(r) and metric variation suppressed by Λ_matter/M_Pl² (justifies Assumption A3). Full field-theoretic EOM still pending. See `RC2_DERIVATION_2026-04-17.md` §RC-2.1. |
| 13 | ~~**Covariant conservation ∇^μ T^(eff)_μν = 0**~~ | 2C §7 | **PARTIALLY RESOLVED 2026-04-17.** Distributional decomposition derived: ∇^μ T^(eff)_μν = [D_ν σ − ε σ (K n_ν + a_ν)]·δ(ℓ). DE limit verified for null ∂M. DM limit reduces to baryon-current conservation. See `RC2_DERIVATION_2026-04-17.md` §RC-2.3. |
| 13a | **Λ_eff boundary-layer estimate vs. SC3** | RC-2.4 | **NEW 2026-04-17.** Naive Israel-junction estimate gives Λ_eff ~ 5.4 G H_0, which is ~10⁻⁸⁹ of H_0². Discrepancy with Paper 2B §5.3 SC3 calculation must be reconciled. Single most important unresolved item from RC-2. |
| 13b | **Exponent p = 1 vs. p = 3/2 narrative** | RC-2.2 | **NEW 2026-04-17.** RC-2 warp-factor argument gives p = 1 on KCR interval, not p = 3/2. α_geom = 3/2 is a separate geometric coefficient (graviton zero-mode). If accepted, Paper 2C §RC1.3 Limit B needs rewrite parallel to fix #4. Awaiting user decision. |

---

## CONJECTURED (stated but not derived)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 14 | **Exponent $p$ in $|T_M|^2 \propto \Gamma_{\rm dec}^p$** (C1) | 2C §RC1.3 (L377 in triage) | Unresolved. The naive CP¹ spectral-density route was withdrawn; if $p = 3/2$, it must be derived from the full M-Σ dynamics. |
| 15 | **λ normalization for Ω_DM/Ω_b ratio** (C2) | 2C §RC1.4 (L454 in triage) | Conjectured. Ratio consistency confirmed but absolute normalization not derived. |

---

## ASSUMED (explicit assumptions requiring future justification)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 16 | **T_M propagator form P(k)** (A5) | 2C §RC1.5 (L503 in triage) | Assumed functional form for the matter-sector propagator. |

---

## PENDING VERIFICATION (Opus passes needed)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 17 | ~~**RC1.1 + RC1.2 symmetry argument**~~ | 2C §7 | **RESOLVED 2026-04-17.** Verified by Opus pass; six surgical fixes (#1 Σ-index convention, #2 linear-invariance via Schur, #3 metric-perturbation convention, #4 α=3/2 honest flagging, #5 DM-limit ansatz framing, #6 conservation check expansion) applied to `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`. Substantive RC-2 follow-throughs (α=3/2 derivation, ∇^μ T^(eff)_μν = 0 verification, δT_M/δg^μν extraction) remain as RC-2 work — see items #12, #13. Memo: `RC1_VERIFICATION_MEMO_2026-04-17.md`. |
| 18 | **FR holonomy exact calculation (Ω = π)** | 2C §8 (L958 in triage) | Flagged for Opus verification. |
| 19 | **Proietti protocol → CR geometric language** | 2C §8 (L994 in triage) | Flagged for derivation, not just translation. |
| 20 | **Eq. 8.4.5 derivation from ΔG_ij** | 2C §8 (L1077 in triage) | Flagged for verification. |

---

## Summary

| Category | Count | Blocking Paper 2? |
|----------|-------|--------------------|
| Deferred | 3 | No |
| Untested (needs 2B verification) | 2 | Yes — 2B |
| Blocking 2B | 2 | Yes — 2B |
| Contingent on Paper 3 | 3 | No (interface contracts) |
| Open | 4 | Partially (RC-2 items gate 2C closure) |
| Conjectured | 2 | No (flagged honestly in manuscript) |
| Assumed | 1 | No (flagged honestly in manuscript) |
| Pending Opus verification | 3 | Yes — 2C quality gate (items #18, #19, #20) |
| **Total** | **21** (20 active, 1 resolved) | |

**Critical path:** ~~SC1/SC2 rewrite (#5)~~ **DONE** → 2B unblocked for items #3, #4, #6 verification → 2B closes. ~~RC1.1/RC1.2 verification (#17)~~ **DONE 2026-04-17** → items #18–20 remain as the 2C §8 quality gate (FR holonomy, Proietti, Eq. 8.4.5). ~~Items #12, #13 (RC-2 work)~~ **PARTIALLY DONE 2026-04-17** — RC-2 derivation framework complete (~60%); two new blockers surfaced: **#13a Λ_eff boundary-layer vs. SC3 reconciliation** (most important) and **#13b p = 1 vs. p = 3/2 narrative decision**. Items #7–9 are Paper 3's problem.
