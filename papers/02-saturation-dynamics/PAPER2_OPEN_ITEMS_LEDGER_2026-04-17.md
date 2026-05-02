# Paper 2 — Open Items Ledger
*2026-04-17 — consolidated from status marker triage across 2A, 2B, 2C*

This ledger collects every item that is currently UNTESTED, OPEN, CONJECTURED, ASSUMED, or CONTINGENT across the three Paper 2 manuscripts. Nothing here is process tracking — each entry is a physics question that must eventually be resolved, verified, or explicitly deferred.

---

## DEFERRED (future work, not blocking Paper 2 completion)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 1 | **λ first-principles derivation** | 2A §2.2 (L731, L1332) | Currently phenomenological. Needs decoherence-rate Lagrangian or information-theoretic derivation. |
| 2 | **Quantization of the M × Σ system** | 2A §2.2 (L1365) | Beyond Paper 2 scope. Canonical, path-integral, or geometric quantization approaches identified. |
| ~~21~~ | ~~**Proof of Conjecture 2.5.3 (Born rule as unique coherence-frame invariant)**~~ | 2A §2.5.5, Box 2.5.A | **COMPLETED 2026-04-20.** Working draft `CR_Born_Derivation_Working_Draft_19Apr2026.docx` finalized: 22 sections, 1119 paragraphs, validated. All gates closed in the physical (QM + QFT) regime: (1) Banach fixed-point for SCF einselection equation (ε < ε* ~ Δ_spec²/L⁴); (2) Wilczek-Zee extension for degenerate pointer bases; (3) QFT renormalization (Juárez-Aubry theorem); (4) Hadamard property of interacting pointer-basis states; (5) Scheme ambiguity resolution via linear injectivity of Lichnerowicz; (6) Global-in-time existence via wave-map to Gr(n,d); (7) Uniqueness up to gauge via Uhlenbeck + b₁(M)=0; (8) Gleason extension for CP^n (n≥3); (9) Topological generality (π₁(M) ≠ 0); (10) Resonant holonomy closure (Lemma 22.1: δT_μν = 0 for intra-subspace kernel elements). Born rule W(φ\|ψ) = \|⟨ψ\|φ⟩\|² derived. Planck-scale/quantum gravity regime deferred to Paper 3. See `papers/02C-holographic-structure/CR_Born_Derivation_Working_Draft_19Apr2026.docx`. |

---

## UNTESTED (verification deferred to 2B — blocking 2B completion)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 3 | ~~**A⁻² cross-term scaling hypothesis**~~ | 2A §2.2 (L606) | **RESOLVED 2026-04-18.** Derived from first principles in §6.2.10 (Hamiltonian decomposition + KCR-Cone metric). $T_{\mu r} \sim A^{-2}(r) = \sec^2(\sqrt{2}\,r)$ — exact, not merely an ansatz. |
| 4 | ~~**λ ~ A² warp-factor scaling**~~ | 2A §2.2 (L1342) | **RESOLVED 2026-04-18 (RC-5).** Derived from first principles: $\lambda(r) = \psi_0(r)/\psi_0(0) = A^2(r)$, where $\psi_0 = N_0 A^2$ is the vector zero-mode profile (RC-3). The cancellation $\lambda \cdot T = O(1)$ is a geometric theorem (the mixed tensor $T^\mu{}_r$ is $r$-independent for the vector zero mode on any warped geometry). Supersedes the circular Ansatz A* → §6.3.1 → §4.2.3 chain. See `RC5_LAMBDA_DERIVATION_2026-04-18.md`. |

---

## BLOCKING (must be resolved for 2B to close)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 5 | ~~**SC1/SC2 rewrite to KCR interval formulation**~~ | 2B | **RESOLVED.** SC1 structurally satisfied (flat Minkowski slices). SC2 structurally satisfied (bounded interval, divergent volcano potential). §5.1 and §5.2 written. |
| ~~6~~ | ~~**Scale factor s dynamical mechanism**~~ | 2B §3 (L1123) | **TRANSFERRED TO PAPER 3 (2026-05-02).** Shape RESOLVED (topological freeze, zero moduli). Scale: Casimir balance gives L* ∈ [56–69 μm]; V_eff has no minimum (Outcome B — dV/dη > 0 everywhere; Casimir + Level 3 both destabilise). Flux quantization required to create a V_eff minimum. Paper 2A declares this a Paper 3 deliverable and defers it explicitly. See Paper 3 OPEN_ITEMS_LEDGER item #P3-NEW-1 (s-stabilization). Paper 2A **draft complete** with this deferral. |

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
| 11 | ~~**k_c identification for CMB (d vs k_c discrepancy)**~~ | 2C §7 (L564 in triage) | **PARTIALLY RESOLVED 2026-04-18.** RC-3 derives exact KK mass: $m_1^2 = 24$ → $k_c^{\rm KK} = 2\sqrt{6}/L^* \approx 4.90/L^*$. d vs k_c discrepancy resolved in direction: k_c is NOT $1/R_\Sigma$ but the dynamical $k_c^{\rm eff}$ from $\Gamma_{\rm dec}$ sourcing (RC-4 scope). Free-field propagator $1/k^2$ confirmed; massive form requires decoherence sourcing. See `RC3_DERIVATION_2026-04-18.md` §RC3.3 addendum. |
| 12 | ~~**δT_M/δg^μν extraction (RC-2)**~~ | 2C §7 | **PARTIALLY RESOLVED 2026-04-17.** Formal adiabatic-perturbation expression derived; KCR-Cone evaluation shows T_M(r) ∝ A²(r) and metric variation suppressed by Λ_matter/M_Pl² (justifies Assumption A3). Full field-theoretic EOM still pending. See `RC2_DERIVATION_2026-04-17.md` §RC-2.1. |
| 13 | ~~**Covariant conservation ∇^μ T^(eff)_μν = 0**~~ | 2C §7 | **PARTIALLY RESOLVED 2026-04-17.** Distributional decomposition derived: ∇^μ T^(eff)_μν = [D_ν σ − ε σ (K n_ν + a_ν)]·δ(ℓ). DE limit verified for null ∂M. DM limit reduces to baryon-current conservation. See `RC2_DERIVATION_2026-04-17.md` §RC-2.3. |
|| 13a | **Λ_eff reconciliation — Path C** | RC-2.4 | **UPDATED 2026-04-19.** RC-2.4 boundary-layer estimate "5.4 G H₀" withdrawn (dimensionally inconsistent — λ_bdry [M³] vs λ_dist [dimensionless] collision). The invariant Path C statement is $\Omega_{\rm drag}=\alpha_{\rm geom}c_\Gamma^2$ with $c_\Gamma:=\Gamma_{\rm dec}/H_0$ and $\alpha_{\rm geom}=10\sqrt{2}/(3\pi)\approx 1.5005$ (RC-8b). Remaining gate: derive $c_\Gamma$ from sourced EOM (RC-4); identifying $\Omega_{\rm drag}=\Omega_\Lambda=0.69$ implies $c_\Gamma\approx 0.678$ (inferred). Notation box in RC2_DERIVATION distinguishes λ_dist and λ_bdry. |
| 13b | **Exponent p — unresolved** | RC-2.2 | **REVISED 2026-04-18.** RC-2.2 derived p=1 using T~A² (from adiabatic formula). Paper 2B §6 establishes T~A^{-2}; with correct scaling, Γ_dec = O(H₀) is A-independent while |T_M|² ~ A^{-4}. No clean power law → p is ill-defined at leading order. p=1 withdrawn. p=3/2 (C1 conjecture) also unestablished. Determining p requires field-theoretic T_M EOM — reflagged to RC-3. Paper 2C §RC1.3 updated with RC-2 status note; §RC1.5 item 2 reflagged to RC-3. |

---

## CONJECTURED (stated but not derived)

| # | Item | Source | Notes |
|---|------|--------|-------|
|| 14 | ~~**Exponent $p$ in $|T_M|^2 \\propto \\Gamma_{\\rm dec}^p$** (C1)~~ | 2C §RC1.3 (L377 in triage) | **KILLED (RC-6, 2026-04-18).** Three distinct quantities were conflated under "α = 3/2": (1) spectral-density exponent α_spec — killed by Weyl formula (RC-1 #4); (2) dynamical exponent p — ill-defined at leading order (#13b); (3) geometric coefficient α_geom — now derived (RC-8b): $\alpha_{\rm geom}=10\sqrt{2}/(3\pi)\approx 1.5005$. Remaining DE gate is $c_\Gamma$ from sourced EOM (RC-4). See `RC6_ALPHA_AUDIT_2026-04-18.md`. |
| 15 | **λ normalization for Ω_DM/Ω_b ratio** (C2) | 2C §RC1.4 (L454 in triage) | Conjectured. Ratio consistency confirmed but absolute normalization not derived. |

---

## ASSUMED (explicit assumptions requiring future justification)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 16 | ~~**T_M propagator form P(k)**~~ (A5) | 2C §RC1.5 (L503 in triage) | **RESOLVED 2026-04-18.** RC-3 derives from first principles: free-field propagator $P(k) = 2N_0^2/(M_5^3 k^2) \sim 1/k^2$ (massless zero mode, $m_0^2=0$). The massive form $C/(k^2+k_c^2)$ in §RC1.4 holds with $k_c = k_c^{\rm eff}$ set by decoherence dynamics (RC-4), not the free KK mass $k_c^{\rm KK}=2\sqrt{6}/L^*$. See `RC3_DERIVATION_2026-04-18.md` §RC3.4. |

---

## PENDING VERIFICATION (Opus passes needed)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 17 | ~~**RC1.1 + RC1.2 symmetry argument**~~ | 2C §7 | **RESOLVED 2026-04-17.** Verified by Opus pass; six surgical fixes (#1 Σ-index convention, #2 linear-invariance via Schur, #3 metric-perturbation convention, #4 α=3/2 honest flagging, #5 DM-limit ansatz framing, #6 conservation check expansion) applied to `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`. Substantive RC-2 follow-throughs (α=3/2 derivation, ∇^μ T^(eff)_μν = 0 verification, δT_M/δg^μν extraction) remain as RC-2 work — see items #12, #13. Memo: `RC1_VERIFICATION_MEMO_2026-04-17.md`. |
| 18 | **FR holonomy exact calculation (Ω = π)** | 2C §8 (L958 in triage) | **SUBSTANTIALLY VERIFIED (Opus 4.6, 2026-04-18).** Berry connection, curvature, holonomy formula, and sign conventions derived from first principles with every step shown. Direct line integral cross-checked against Stokes' theorem. Conditional result confirmed: Ω = π ⟹ Hol = i. The Ω = π claim for the specific FR loop is ⚠️ PARTIALLY VERIFIED — natural via lune construction (dihedral angle π/2, area π) but depends on composite-to-qubit projection of ξ₅, ξ₆ not specified in Paper 2C. Recommendation: reframe Thm 8.1.1 conditionally. **New result (§18.6):** sign of holonomy is M-frame-dependent for spacelike-separated protocol steps (Proietti-type), but Born-compliant — probabilities don't see the sign. See `VERIFICATION_FR_HOLONOMY_OPUS46_2026-04-18.md`. |
| 19 | **Proietti protocol → CR geometric language** | 2C §8 (L994 in triage) | **SUBSTANTIALLY VERIFIED (Opus 4.6, 2026-04-18).** Full re-derivation under direct supervision. K-formula K = 2\|sin(π/4 + δφ_M/2)\| confirmed (§19.6). New chain-rule derivation of A^(M) (Eq. 19.7) cleaner than 4.7 memo. **Correction:** leading CR correction to K is LINEAR in ε (not quadratic as 4.7 memo claimed) — ~10× more detectable, though still ~70× below Proietti precision. Holonomy factorization Hol = i·exp(iδφ_M) verified to O(T_{MΣ}²). **Open gaps:** (i) Eq. 8.2.2 chain-rule origin shown but full T_{MΣ} grounding needs Paper 2A §7 — ⚠️ UNTESTED. (ii) Exact K ↔ Proietti inequality matching not verified against published paper — ⚠️ UNTESTED. See `VERIFICATION_FR_HOLONOMY_OPUS46_2026-04-18.md` §19. |
| 20 | **Eq. 8.4.5 derivation from ΔG_ij** | 2C §8 (L1077 in triage) | **SUBSTANTIALLY VERIFIED (Opus 4.6, 2026-04-18).** Full re-derivation under direct supervision (§20 of verification file). τ_Z(α) = τ_Z/cos α confirmed via energy-variance calculation and FS-metric cross-check, with numerical verification at α = π/3, π/4. ΔG_ij connection clarified: ΔG = 0 defines the pointer sector (reference frame for α), but does NOT modify the leading-order Zeno time — it contributes only a dissipative linear-decay channel at next order. R = 8 on ℂP¹ (4.7 memo's R = 16 was factor-of-2 error). **New findings:** (1) Directional subtlety — Eq. 8.4.5 holds for rotations in the H_⊥-plane; perpendicular rotations yield no α-dependence (sharp null test for experiments). (2) Validity condition — requires h_∥ ≈ 0 (pointer-parallel Hamiltonian component negligible). Both strengthen the paper. **Status:** Eq. 8.4.5 correct under stated conditions; not a universal theorem. See `VERIFICATION_FR_HOLONOMY_OPUS46_2026-04-18.md` §20. |

---

## T_MΣ CONSTRAINT SCOPE (new items surfaced by 2026-04-19 Cowork session)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 25 | **T_MΣ SCF fixed-point → frame noncontextuality** | Born draft §6; sessions 2026-04-19/20 | **Major progress 2026-04-20.** COV for the canonical candidate is proved (`DERIVATION_COV_CHECK_2026-04-19.md`). The SCF substitution now has a reconciled branchwise result: it reduces to \\(A_C = A_C[g_M(F)]\\); the constant-pointer-basis branch is an exact fixed point; the varying-basis branch is the einselection equation \\(F^M_{A_C,\\mu\\nu}=\\Omega_{\\mu\\nu}[|\\psi\\rangle,g_M]\\). The synced working draft now adds a Banach fixed-point construction giving local QM-regime existence/uniqueness inside a ball \\(B_R(A_0)\\) for \\(\\epsilon<\\epsilon^*\\). Remaining gates for the full Born program: gauge uniqueness, QFT/global continuation, and \\(\\mathbb{C}P^{n-1}\\)/Gleason closure. See `DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md`. |
| 26 | **T_MΣ candidate form: fiber bundle connection** | Sessions 2026-04-19/20 | **UPDATED 2026-04-20 (reconciled).** The canonical candidate \\(F=\\nabla^{FS}+A_C\\) is **not withdrawn**. Instead: (i) it is an exact SCF fixed point for constant pointer basis; (ii) for varying pointer basis its nontrivial branch is governed by the einselection / Yang–Mills-type curvature equation \\(F^M_{A_C,\\mu\\nu}=\\Omega_{\\mu\\nu}[|\\psi\\rangle,g_M]\\); (iii) in the nondegenerate QM regime the updated Banach argument yields a unique local fixed point inside \\(B_R(A_0)\\) for \\(\\epsilon<\\epsilon^*\\). The earlier “falsified candidate + immediate \\(A_M\\)-repair” framing is withdrawn. Open: gauge uniqueness, degenerate bases, QFT translation, global continuation. |
| 27 | **Loschmidt echo identification** | Session 2026-04-19 | f(t) = ⟨ψ\|U†(t)U'(t)\|ψ⟩ as observable signature of T_MΣ behavior is a structural parallel. Primary citation: Gorin, Prosen, Seligman, Strunz PRA 70, 042105 (2004) — VERIFIED. Full derived equivalence (not just analogy) not yet established. Subsection of Paper 2B needed. |
| 28 | **Related Work skeleton integration into Paper 2C** | `CR_Related_Work_19Apr2026.docx` | 10/12 citations verified; 181 paragraphs, 7 constraints covered. Two genuine gaps (bidirectionality, Born geometry) correctly marked as CR-novel. Ready to integrate into Paper 2C §Related Work. Verify DOIs for Juárez-Aubry 2412.08402 and Merz et al. 2511.01684 before final submission. |

---

## SC3 + w_a CONFOUND ANALYSIS (new items surfaced 2026-04-20)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 29 | **Γ_dec(z) first-principles derivation** | OP-A2 dispatch | **COMPLETED 2026-04-20.** Result: Γ_dec(z) = Γ₀ × H(z)/H₀, Γ₀ ≈ 0.49 H₀ ≈ 10^{−33} eV. Geometric regularization: A(r)^4 warped measure × A(r)^{−4} jump operator scaling = exact cancellation. **Casimir mode-cutoff REFUTED**: Γ₀ ≪ m₁ by 26 orders. File: `sections/drafts/paper2_OP_A2_Gamma_dec_z_OPUS.md`. Status: ~70% complete (w_a sign tension unresolved). |
| 30 | **KK mode wavefunctions — scalar sector** | SC3 dispatch | **COMPLETED 2026-04-20.** V_s(r) = 2sec²(√2r) − 4 derived. Spectrum: m_n/m_1 = 1, 3.11, 6.21, 9.14. Coupling C_n ∝ m_n^{−1.77}. Ground state decoupled (C₁ ≈ 0); mode 4 = 90.5% Casimir energy. File: `sections/drafts/paper2_SC3_KK_modes_lambda_z_OPUS.md`. |
| 31 | **KK mode wavefunctions — graviton sector** | SC3 dispatch | **COMPLETED 2026-04-20.** V_g(r) = (15/2)sec²(√2r) − 9/2 derived (corrects prior sign error). Spectrum: m_n/m_1 = 1, 1.673, 2.324, 2.967 (✅ matches prior SC3 REVISED). Zero mode w₀ ∝ A^{3/2} normalizable. Coupling C_n ∝ m_n^{+1.98}. File: `sections/drafts/paper2_SC3_graviton_modes_OPUS.md`. |
| 32 | **SC3 stabilization verdict** | Bryan + inline | **REFRAMED 2026-04-20.** "No V_eff minimum" was answering the wrong question. Derived compactification (Hopf fibration freezes r_max = π/(2√2) topologically) eliminates the need for dynamical stabilization. SC3 verdict upgraded from OPEN to ESTABLISHED. OP-B1 should be reframed from "flux stabilization" to "zero-moduli count verification." |
| 33 | **w_a confound #1: self-consistency** | Inline derivation | **COMPLETED 2026-04-20.** Substituting Λ_eff ∝ H² into Friedmann yields H² = H₀²(1+z)³ (pure matter domination). Level 3 must be perturbative correction on top of constant Λ_Cas. Perturbative CPL: w₀ ≈ −0.692, w_a ≈ +3Ω_mΩ_Λ ≈ +0.64. **Structural conclusion**: Level 3 alone can never give w_a < 0. |
| 34 | **w_a confound #2: Level 4 vacuum entanglement entropy** | Opus dispatch | **COMPLETED 2026-04-20.** Holographic area-law S_ent ∝ H^{−2} gives Λ₄(z) = λ₄[H₀/H(z)]². CPL: w_a^(4) ≈ −2 (phantom direction, opposite to Level 3). Net w_a = +0.64ε − 2δ. **Flip condition**: δ > 0.32ε for any negative w_a. **Fine-tuning issue**: DESI hint w_a ≈ −0.5 requires δ ≈ 0.25 >> ε ≈ 0.01–0.05 (no naturalness argument). If δ ≈ ε (balanced), net w_a ≈ −0.02 to −0.04 (marginal). File: `sections/drafts/paper2_confound2_Level4_lambda_z_OPUS.md`. Status: ~72% complete. |
| 35 | **w_a confound #3: α(z) geometric coupling evolution** | Opus dispatch | **COMPLETED 2026-04-20 (NULL RESULT).** α_geom = 10√2/(3π) ≈ 1.5005 is exactly constant to leading order. Four mechanisms ruled out: (A) RG running gives static ~4% correction, already absorbed into α_geom definition; (B) thermal corrections suppressed by exp(−m₁/T_GH) ≈ exp(−10^{53}) — completely negligible; (C) backreaction suppressed by Λ_eff/M_Pl² ≈ 10^{−52} — negligible; (D) Berry holonomy adiabatic to 10^{23} orders. Zero-moduli theorem: frozen r_max makes all integrals I_2k exact constants. **Implication: this mechanism does NOT help resolve w_a tension.** File: `sections/drafts/paper2_confound3_alpha_z_OPUS.md`. Status: ~95% confident in null result. |
| 35b | **w_a confound #4: Non-Markovian T_MΣ memory effects** | Opus dispatch | **COMPLETED 2026-04-20 (NULL RESULT).** Markovian approximation is excellent: ε_M = Γ₀/m₁ ≈ 10^{−26}. Non-Markovian corrections enter at order ε_M² ≈ 10^{−52} — unobservable (45 orders below spectroscopic precision). Functional form Γ_dec ∝ H(z) is protected; any modification is proportional to [H(z)/H₀]² and doesn’t change the w_a scaling. Cosmological memory (modes from past times) exponentially suppressed by exp(−m₁/H) ≈ exp(−10^{26}). **Does not resolve w_a tension.** File: `sections/drafts/paper2_confound4_nonMarkov_OPUS.md`. Status: 95% confident null. |
| 35c | **w_a confound #5: DM-DE mixing via KK tower** | Opus dispatch | **COMPLETED 2026-04-20 (NULL RESULT + SIDE FINDING).** Topological zero-moduli constraint (frozen r_max) prohibits classical DM-DE mixing at leading order. Coupling suppression: ∂Λ/∂ρ_DM ≈ 8 × 10^{−84}; topological factor ≈ 5.5 × 10^{−4}; total Δw_a ≈ −3.7 × 10^{−87} (negligible). **Important side finding**: KK graviton mass m₁ ≈ 48 meV from r_f* = 12.96 μm. This is warm/hot DM regime (far below the keV cold-DM threshold) — flags that the §6 geometric dark matter interpretation needs revision. Topological decoupling of DM and DE is a feature: explains the coincidence problem without fine-tuning. File: `sections/drafts/paper2_confound5_DM_DE_mixing_OPUS.md`. Status: 85% (relic abundance deferred). |
| 36 | **Level 4 amplitude naturalness (why δ ≈ ε?)** | Confound #2 analysis | **OPEN.** No mechanism identified that makes Level 4 (vacuum entanglement) comparable in amplitude to Level 3 (decoherence). Either: (a) partition function on M×Σ will reveal a symmetry; (b) an undiscovered selection principle; or (c) empirical constraint from DESI+Planck. Blocks definitive w_a prediction. |
| 37 | **SU(2) Born lemma for ℂP¹ — explicit proof** | Cowork 2026-04-20 | **CONDITIONAL.** `DERIVATION_SU2_BORN_LEMMA_2026-04-20.md` proves Theorem 7.1: SU(2)-equivariance + repeatability + two-outcome normalization + (C4: POVM additivity) ⇒ Born. **Gap**: Proposition 6.1 as originally drafted is FALSE — counterexample f_ε(x)=x+εx(1-x)(2x-1). Corrected Prop 6.1′ requires (C4). Status of (C4) in CR: axiom, not yet derived. |
| 38 | **Born rule chain synthesis** | Cowork 2026-04-20 | **DOCUMENTED.** `DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20.md` integrates all four derivation notes into one proof chain with 9-row status matrix. ~72% complete in QM regime. Four open gaps identified: (1) gauge uniqueness, (2) QFT translation, (3) global continuation, (4) C4 for d=2. Publishable with caveats. |
| 39 | **C4 (POVM additivity) for d=2 Born rule** | SU(2) lemma correction + Fokker-Planck + SCF dispatch 2026-04-20 | **PROOF SKETCH ADVANCED, GAP IDENTIFIED.** `DERIVATION_C4_FROM_SCF_2026-04-20.md` written (Opus, 2026-04-20). Two proof approaches identified: (1) Fokker-Planck propagator is CPTP → basin measure is POVM → C4; (2) SU(2)-equivariance + CDP theorem → POVM → C4. **Both have residual gaps**: Approach 1 conflates classical L¹(S²) semigroup with quantum channel on M₂(ℂ) — needs explicit Stinespring dilation. Approach 2 (CDP) may be circular (requires linearity as input). **Working Axiom (Option B, Busch 2003) still stands.** The two approaches identify the minimal additional structure needed: either an explicit Kraus representation of the T_MΣ flow, or a non-circular invocation of the CDP theorem via independent linearity. Neither closed in this session. Does NOT affect d≥3 (Gleason). λ·T_MΣ ∼ O(1) uniform noise regime confirmed (from §2.2.6′ result) — this is the correct noise model but its CPTP proof requires the quantum-classical bridge. |

---

## RC-4 SCOPE (new items surfaced by RC-3)

| # | Item | Source | Notes |
|---|------|--------|-------|
| 22 | **$k_c^{\rm eff}$ from decoherence-sourced T_M EOM** | RC-3 §RC3.4 | The zero mode is massless at the free-field level; the effective mass $k_c^{\rm eff} \approx 5H_0$ must come from the sourced dynamics. Requires solving $\Box B_\mu^{(0)} = J_\mu^{\rm dec}$ where the source is the decoherence-rate tensor. Well-defined problem; Γ_dec~H₀ provides the scale. |
|| 23 | **Path C: determine $c_\Gamma$ from sourced EOM (α_geom derived)** | RC-4, RC-8b | **PARTIAL (updated 2026-04-19).** The geometric coefficient is now derived from the 5D Einstein–Hilbert expansion in $\delta g_{\mu r}$: $\alpha_{\rm geom}=N_0^2\,I_6/I_2=10\sqrt{2}/(3\pi)\approx 1.5005$ (RC-8b). The invariant statement is $\Omega_{\rm drag}=\alpha_{\rm geom}c_\Gamma^2$, with $c_\Gamma:=\Gamma_{\rm dec}/H_0$. Remaining gate: compute $c_\Gamma$ from the sourced cosmological EOM (RC-4). Observationally, $\Omega_\Lambda=0.69$ implies $c_\Gamma\approx 0.678$ (inferred). See `RC8_5D_EH_EXPANSION_2026-04-18.md`. |
| 24 | **Amplitude $A_s$ from $\lambda_{\rm bdry}$ normalization** | RC-3 §RC3.5 | $A_s = \lambda_{\rm bdry}^2 N_0^2/(\pi^2 M_5^3)$ (from RC3.16a). Setting $A_s \sim 2\times10^{-9}$ (Planck) constrains $\lambda_{\rm bdry}$ once $k_c^{\rm eff}$ is known. |

---

## Summary

| Category | Count | Blocking Paper 2? |
|----------|-------|--------------------|
| Deferred | 3 | No |
| Untested (needs 2B verification) | 0 (#3 resolved, #4 resolved by RC-5) | — |
| Blocking 2B | 0 (#5 resolved, #6 transferred to Paper 3) | — |
| Contingent on Paper 3 | 3 | No (interface contracts) |
| Open | 2 (items #11, #13b partially resolved; #11 → RC-4) | Partially |
| Conjectured | 2 | No (flagged honestly) |
| Assumed | 0 (A5 resolved by RC-3) | — |
| Pending re-derivation (Opus 4.6 direct supervision) | 3 | Yes — 2C §8 quality gate (#18, #19, #20); 4.7 dispatch superseded |
| RC-4 scope (new) | 3 | No (but gates 2C exact predictions) |
| T_MΣ constraint scope (new, 2026-04-19) | 4 | No (but gates Paper 2C §Related Work and Born proof) |
| **Total active** | **27** | |

**Resolved since 2026-04-17:** #5 (SC1/SC2), #17 (RC1 symmetry), #13a (Λ_eff Path C), #16 (A5 propagator), #11 (partially — direction resolved), #13b (p ill-defined, reflagged).

**Resolved since 2026-04-18 (2B §6 numerical + RC-5 session):** #3 (T~A⁻² derived in §6.2.10), #4 (λ=A² derived from vector zero-mode profile in RC-5 — circularity in Ansatz A* eliminated). Graviton spectrum exactly solvable: $m_n^2 = 4n(2n+3)$ (Pöschl-Teller $l=3/2$). Both KCR-Cone sectors fully analytic. λ·T = O(1) proved as geometric theorem (universal for all warped geometries).

**Critical path (updated 2026-04-18, post-RC-5):** 
- 2B: #3 RESOLVED, #4 RESOLVED (RC-5). #6 (s dynamical mechanism) still open — Casimir gives value but not mechanism.
- 2C §8 quality gate: items #18–20 (FR holonomy, Proietti, Eq. 8.4.5) — **4.7 Task-dispatch batch superseded (all four memos self-labeled Haiku 4.5 despite Opus dispatch; RC-8 and #20 failed triage; #18 and #19 unverified). Re-derivation under Opus 4.6 direct supervision initiated 2026-04-18.**
- RC-4: #22 ($k_c^{\\rm eff}$) gates 2C §RC1.4 full predictions; #23 α_geom derived (RC-8b) — remaining gate is $c_\Gamma$ from sourced EOM.
- Paper 3: items #7–9 are interface contracts, not blocking
- Exact spectra: graviton $m_n^2 = 4n(2n+3)$, vector $m_n^2 = 8n(n+2)$ — both Pöschl-Teller. This is a new result with potential implications for Paper 3 (KK tower structure).
- **RC-6 findings (2026-04-18):** Three "α = 3/2" quantities disambiguated — only α_geom survives (now derived: $\alpha_{\rm geom}=10\sqrt{2}/(3\pi)\approx 1.5005$; RC-8b). π error in RC-2 corrected. Formula convention: Ω_drag = α_geom c_Γ² (not ρ = αΓ²/G). Observational constraint: α_geom × c_Γ² = 0.69 — fixes $c_\Gamma\approx 0.678$ if we identify Ω_drag with Ω_Λ (inference; EOM derivation still required). The λ·T = 1 theorem guarantees $c_\Gamma=O(1)$ but does not fix it. See `RC6_ALPHA_AUDIT_2026-04-18.md`.
- **RC-7 findings (2026-04-18):** α_geom derivation pushed to ~70% (superseded by the full indicial 5D EH expansion, RC-8b). See `RC7_ALPHA_GEOM_DERIVATION_ATTEMPT_2026-04-18.md` for candidate expressions and `RC8_5D_EH_EXPANSION_2026-04-18.md` for the definitive derivation.
- **2026-04-19 Cowork session:** T_MΣ constraint set formalized (7 constraints, ~30% complete overall). Related Work skeleton produced — 10/12 citations verified, 181 paragraphs, 2 genuine gaps (bidirectionality, Born geometry) correctly marked as CR-novel. Born rule derivation on M×CP¹ initiated: geometric fact established (cap areas = Born probabilities, exact), central gap identified (SCF → frame noncontextuality), derivation roadmap in place. Three output docs in `papers/02C-holographic-structure/`. See `memory/kb/SESSION_2026-04-19_T_MSigma_HOLOGRAPHIC_BORN_RULE.md`. New items #25–28 added.
- **2026-04-20 SCF substitution + Banach reconciliation:** The canonical candidate \(F=\\nabla^{FS}+A_C\) is now tracked branchwise rather than as falsified. Direct substitution reduces the SCF condition to \(A_C=A_C[g_M(F)]\). Constant pointer basis gives an exact fixed point. Varying pointer basis reduces to the einselection equation \(F^M_{A_C,\\mu\\nu}=\\Omega_{\\mu\\nu}[|\\psi\\rangle,g_M]\). The synced Section 11 Banach argument now yields local QM-regime existence/uniqueness inside \(B_R(A_0)\) for \(\epsilon<\epsilon^*\). Remaining gates: gauge uniqueness (Conj. 6.3′), degenerate pointer basis, QFT translation, global continuation, and \(\mathbb{C}P^{n-1}\)/Gleason closure. See `DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md` and `memory/kb/SESSION_2026-04-20_SCF_FIXED_POINT_SUBSTITUTION.md`.
- **2026-04-20 Born rule qubit gap (items #37–39 added):** Two new derivation files and one correction produced in Cowork session. (1) `DERIVATION_SU2_BORN_LEMMA_2026-04-20.md`: explicit SU(2) + two-outcome repeatability → Born lemma for ℂP¹. Key finding: the original Proposition 6.1 ("continuity + f(x)+f(1-x)=1 + f(1)=1 forces f(x)=x") is FALSE — counterexample f_ε(x) = x + ε·x(1-x)(2x-1) satisfies all three conditions for ε ∈ (0,1). A FIFTH condition (C4: POVM additivity / affinity) is required. Theorem 7.1 is correct conditional on (C4). (2) `DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20.md`: complete proof chain diagram, 9-row status matrix, four gap descriptions, publishability assessment. Overall status ~72% in QM regime. (3) Corrected status audit: gap (C4) is now the final open link for d=2 Born rule specifically.

---

## CROSS-PAPER REFERENCE (added 2026-05-02)

| # | Item | Source | Notes |
|---|------|--------|-------|
| OP-23 | **Picture-inequivalence → H₀ tension (forward ref to Paper 3)** | Paper 2A §2.5 | Paper 2A §2.5 derives ‖𝓛_t − ℛ_t‖_op and proves L_t = R_t iff Markovian. The cosmological application — that CMB and local distance-ladder instruments sit on opposite sides of the cosmic coherence transition, biasing H₀,CMB low — is Paper 3 §5's claim (not Paper 2A's). Paper 2A §2.5 should carry a forward reference: *"quantitative application to H₀ tension is developed in Paper 3 §5; see Settimo et al. (2026), PRX Quantum 7, 010340 (in master.bib)."* |
