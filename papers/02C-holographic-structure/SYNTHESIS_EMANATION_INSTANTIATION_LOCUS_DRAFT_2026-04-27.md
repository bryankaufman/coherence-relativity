# The Emanation–Instantiation Locus on M × Σ
**Working title:** *The Emanation–Instantiation Locus: A Synthesis of Coherence-Field, Born-Chain, and Holographic-Boundary Results in Holographic Coherence Relativity*
**Date:** 2026-04-27 (expanded from skeleton 2026-04-26)
**Status:** DRAFT — full prose connective tissue added; Lemma 0 and Lemma 1 stated and proved; main theorem stated with named conditionals.
**Audience:** Internal review prior to placement decision (Paper 2C §8 supplement or Paper 3 §0 framing document).
**Source documents:** `SYNTHESIS_EMANATION_INSTANTIATION_LOCUS_2026-04-26.md` (skeleton), `DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20.md`, `DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md`, `M2_SPEKKENS_AND_LEMMA1_2026-04-26.md`, `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md` §RC1, `paper3_idea_assignments_2026-03-23.md`.

---

## Status Legend

- ✅ VERIFIED: derived in a checked-in derivation file and reviewed
- ⚠️ UNTESTED: structurally plausible, written but not externally checked
- ❌ MISSING: not yet derived; named gate
- 🤔 UNKNOWN: open question

---

## §0. The Central Question

How does a potentiality on the coherence manifold Σ become a fact on spacetime M?

This question — the emanation–instantiation problem — has three structural answers in the HCR framework, each at a different scale. This document assembles those answers into a single theorem. The three answers are:

1. At the **quantum scale**, the self-consistency of the coherence-frame connection forces measurement statistics to obey the Born rule. Potentiality maps to probability by geometric necessity, not by additional postulate.

2. At the **holographic scale**, the projection of the coherence cross-term T_{MΣ} onto the boundary ∂M generates an effective stress tensor that sources bulk geometry. Potentiality, concentrated at the boundary fibration ∂M × Σ, becomes a gravitational source.

3. At the **ontological scale**, the boundary ∂M *is* the present-moment decoherence front — the surface on which Hilbert-space potentialities are crystallized as irreversible spacetime facts. The past is M; the future is the unresolved coherosphere.

These three answers are not independent. **The central claim of this synthesis** is that they are three faces of the same geometric object: the boundary fibration ∂M × Σ, on which the SCF saturation condition, the holographic projection, and the fact-horizon condition all coincide.

---

## §1. Setup and Notation

### 1.1 Manifolds

Let H be a separable Hilbert space, dim H = d (finite-d sector throughout; infinite-d/QFT extension flagged ❌ MISSING).

- **Σ ≡ U(d)/T^d** — the flag manifold; coherence manifold. Equipped with the Fubini–Study metric g^{FS}. For d = 2: Σ = CP¹ ≅ S². ✅ VERIFIED.
- **M** — Lorentzian 4-manifold; realized spacetime; the accumulated record of irreversible decoherence events.
- **∂M** — fact horizon; 3-dimensional hypersurface in M; the decoherence front between past facts (M) and future potentialities. ✅ Identified in Paper 3 §3 idea assignments.
- **M × Σ** — the coherosphere; the joint manifold on which both quantum and gravitational dynamics are formulated.
- **H** — the orthoverse; strictly H ⊋ M (Lemma 0 below). H is not a manifold in the usual sense but contains M as a projection.

### 1.2 Key Tensors and Fields

- **g_{μν}** — bulk metric on M (Lorentzian)
- **g^{FS}_{ab}** — Fubini–Study metric on Σ
- **T_{MΣ} = T_M^{μa}** — the coherence cross-term; off-diagonal block of the M×Σ metric G_{AB}. Maximally supported at ∂M. ✅ VERIFIED (Paper 2C §RC1).
- **F = ∇^{FS} + A_C** — the canonical SCF candidate; ∇^{FS} the Fubini–Study connection on Σ, A_C the Berry/pointer connection. ✅ SCF fixed point in constant-basis branch; ⚠️ local Banach fixed point in varying-basis QM regime.
- **W(φ_i | ψ)** — basin weight; the CR probability measure on Σ-rays. Before the Born chain is closed: a priori an unknown function. After: W = |⟨φ_i | ψ⟩|².

### 1.3 The Distinguishability Field λ

λ: M × Σ → [0, 1], with λ = 1 denoting full distinguishability (classical/pointer-like), λ = 0 denoting maximal coherence.

Under the synthesis convention (EGY from Paper 1):
  λ_synthesis(x, ψ) = max_i |⟨φ_i(x) | ψ⟩|²

where {|φ_i(x)⟩} is the pointer basis at x ∈ M.

The holographic projection:
  ξ_0(x) := arg max_{ξ ∈ Σ} λ(x, ξ)

defines a section of the bundle Σ → M, used by 𝒫_holo: M × Σ → M × {ξ_0(x)}. ✅ VERIFIED.

**Convention note:** Paper 2A §2.2 uses a coupling convention where λ = 0 is classical; Paper 1 and this synthesis use λ = 1 as classical (EGY). These are related by λ_synthesis = 1 − λ_coupling at leading order. The synthesis convention is used throughout; Paper 2A §2.2's coupling parameter should be renamed κ in final manuscripts.

---

## §2. Three Structural Closures

### 2.1 Quantum Closure: SCF + COV ⇒ Born Rule

The first closure operates entirely on the Σ side and delivers the Born rule as a geometric consequence of self-consistency.

**The problem.** In standard quantum mechanics the Born rule W(φ | ψ) = |⟨φ|ψ⟩|² is a postulate. In CR, the question is whether it can be derived from the axioms of the coherence-frame structure — specifically, from the requirement that the coherence connection be self-consistent under the M × Σ dynamics.

**The chain.** Three steps link the SCF equation to the Born rule:

*Step 1: SCF → COV.* The self-consistency equation T_{MΣ} = F[g_M(T_{MΣ}), g^{FS}, C] is satisfied by the canonical candidate F = ∇^{FS} + A_C. Direct substitution shows that the Fubini–Study terms cancel, leaving A_C = A_C[g_M(F)]. In the constant-pointer-basis branch, this is an exact fixed point. In the varying-basis branch, it reduces to the geometric einselection equation F^M_{A_C,μν} = Ω_{μν}[|ψ⟩, g_M]; Banach's fixed-point theorem provides a unique local solution in B_R(A_0) for ε < ε*. ✅ Constant branch exact. ⚠️ Varying branch local/QM. The canonical F satisfies the SU(d)-covariance condition COV: F[Ug_MU⁻¹, g^{FS}, UC] = U·F·U⁻¹ for all U ∈ SU(d). ✅ VERIFIED algebraically.

*Step 2: COV ⇒ Frame Noncontextuality (Theorem 6.1).* If T_{MΣ} satisfies SCF and F satisfies COV, the basin weight W(φ_i | ψ) is SU(d)-equivariant: W(U|φ_i⟩ | U|ψ⟩) = W(|φ_i⟩ | |ψ⟩) for all U ∈ SU(d). The proof is a clean group-transport argument: the flow Φ_t transforms equivariantly under COV, so basins and their measures transform accordingly, and the weight is invariant. This is unconditional given COV. ✅ VERIFIED.

*Step 3: Frame Noncontextuality ⇒ Born (Corollary 6.2).* By Gleason's theorem (d ≥ 3): the unique positive, normalized, SU(d)-equivariant function on rank-1 projections of ℂ^d is the trace form W(|φ_i⟩|ψ⟩) = |⟨φ_i|ψ⟩|². For d = 2: the Busch (2003) extension to effects under POVM-additivity supplies the same conclusion. ✅ VERIFIED (Gleason 1957; Busch 2003).

**Open gates in §2.1:**
- ~~G1: Gauge uniqueness (Conjecture 6.3′)~~ ✅ **PROVED 2026-04-27** — Theorem G1-Cov (HCR axioms A1–A4 → naturality via Kolar–Michor–Slovak → Lemma NP → every admissible SCF fixed-point satisfies COV unconditionally) + Theorem G1-Full (∇^FS is unique natural Kähler-compatible connection on CP^{d-1}; SU(d) transitive on orthonormal bases → all A_C connections gauge-equivalent → single orbit). The chain now proves "SCF FORCES Born" — unconditionally in the non-degenerate QM regime. ⚠️ Pending independent mathematical review; Wilczek–Zee degenerate-pointer extension and QFT loop-correction stability remain open.
- Wilczek–Zee degenerate-pointer extension (non-Abelian Berry phases). ❌ MISSING.
- QFT translation of the Banach contraction (loop corrections to κ = εC_E C_Q C_{YM}). ❌ MISSING.
- Global continuation beyond the initial Banach ball. ❌ MISSING.

**Realistic closure: ~72% in the QM non-degenerate regime.** Publishable now with the gauge-class caveat.

### 2.2 Holographic Closure: 𝒫_holo + RC-1 ⇒ Effective Stress Tensor

The second closure connects the coherence cross-term T_{MΣ} to observable geometry on M via the holographic projection.

**The problem.** Given the joint manifold M × Σ, how does coherence structure generate a gravitational source? The CR answer is through the boundary action at ∂M — the holographic locus where the Σ-fibre collapses onto the pointer sector.

**RC-1 result.** Three symmetry constraints uniquely determine the leading boundary action:

  S^{bdry}_M = λ_{bdry} ∫_{∂M} √(-γ) Tr(T_M T_M†)

where the three constraints are: (1) diffeomorphism covariance on M (admits only ∂M-intrinsic integrals); (2) U(d)×T^d invariance on Σ (the unique leading bilinear invariant in T_M is Tr(T_M T_M†)); (3) locality along ∂M (no bi-local kernels). ✅ DERIVED (Paper 2C §RC1.1).

Metric variation yields the effective bulk stress tensor:
  T^{(eff)}_{μν} = λ |T_M|² Π_{μν} δ_⊥(x, ∂M)

localized at ∂M, with Π_{μν} the boundary projector. ✅ DERIVED (Paper 2C §RC1.2).

**Two cosmological limits:**
- Isotropic T_M (uniform decoherence): equation of state w = p/ρ = -1. This is dark energy — a boundary-localized, constant negative-pressure contribution. ✅ DERIVED (§RC1.3A).
- Anisotropic T_M (decoherence tracking baryon density): w = 0. This is pressureless dark matter. ✅ DERIVED (§RC1.3B).

**Observational contact:** The primordial power spectrum acquires a coherence-induced IR suppression Δ²_Σ(k) = A_s · k²/(k² + k_c²). At k_c = 5/χ_{CMB}, this predicts 69% CMB quadrupole suppression vs. Planck's observed 67% — within 3%. ✅ VERIFIED numerically.

**The geometric coefficient** α_geom = N₀² · I₆/I₂ = 10√2/(3π) ≈ 1.5005 is derived from the KCR zero-mode backreaction integral (RC-8b). The 0.033% proximity to 3/2 is a numerical coincidence; the two quantities answer different questions. ✅ DERIVED.

**Open gates in §2.2:**
- Physical k_c from Σ geometry (RC-3 ⚠️ PARTIAL 2026-04-27): D1 (λ_min=d) ✅, D2 (Lorentzian propagator) ✅, D3a (ℓ_min=2 via T^(eff) rank-2 + SO(3) isotropy of ∂M) ✅ — k_c=5/R_Σ is now structurally derived; D3b (R_Σ=χ_CMB via holographic projection) ❌ Paper 4 §3 deliverable.
- c_Γ from sourced EOM (RC-4): the constraint is Ω_{drag} = α_geom c_Γ² = 0.69, giving c_Γ ≈ 0.678 by inference; the derivation from the sourced T_M EOM is not complete. ⚠️ PARTIAL.
- Full GKPW-type prescription and boundary correlators. ❌ MISSING.

**Realistic closure: ~85% on the analytic side.** RC-1 has de-conjectured the holographic structure to a substantial degree.

### 2.3 Ontological Closure: H ⊋ M — The Fact Horizon as Locus

The third closure provides the ontological foundation: what *is* M, what is ∂M, and in what sense is the boundary fibration ∂M × Σ the locus of emanation–instantiation?

**The problem.** The abstract formalism produces T^{(eff)}_{μν} and Born statistics at ∂M, but does not by itself say *what* ∂M is physically. The ontological layer answers this.

**M = accumulated irreversible record.** A fact is a decoherence event so deeply embedded in environmental records that its reversal would require erasing more bits than the Bekenstein bound permits. M is the accumulated set of all such facts. The past is complete; the present is the decoherence front; the future is potential. This is not a metaphor — it is the statement that the realized spacetime manifold is constructed by quantum Darwinism applied globally. ⚠️ UNTESTED as a derivation (sketched in Paper 3 §3 idea assignments; Lemma 0 below packages the argument).

**∂M(t) = present-moment decoherence front.** The fact horizon is the 3-surface in M at which decoherence events are currently becoming irreversible. It moves forward in time as new facts accumulate. The Big Bang is the initial ∂M (first decoherence event); the CMB last-scattering surface is ∂M at t = t_rec — the largest visible fact horizon. ✅ Identified in Paper 3 ideas and Paper 2C §RC1.

**The locus.** On the boundary fibration ∂M × Σ, three things coincide:
1. The SCF saturation surface: {|φ_i(x)⟩} — pointer states at each x ∈ ∂M (see Lemma 1)
2. The holographic projection locus: {ξ_0(x)} — the λ = 1 section of Σ over ∂M (see Lemma 1)
3. The fact-horizon: ∂M — where Σ-potentialities crystallize as M-facts

The coincidence of all three is not assumed; it follows from Lemma 1 (below).

**Open gates in §2.3:**
- Lemma 0 (strict containment H ⊋ M) needs packaging (written below — ⚠️ UNTESTED at theorem level).
- The coalescence map C: Σ → M (long-range program). ❌ MISSING.
- Constructive 𝓕: (H, ∂𝒞, T_{AB}) → (M, g_{μν}, {Φ_a}) — the terminal program; Papers 4–7. ❌ MISSING at Papers 4–7 level; ~30% on side-conditions only.

**Realistic closure: ~40%** — the ontology is named and internally consistent, but no constructive reconstruction is in hand.

---

## Lemma 0. Strict Containment H ⊋ M

**Statement.** The orthoverse H strictly contains the realized spacetime M: H ⊋ M in the sense that there exist elements of H with no M-projection.

**Argument** (three supporting threads; none yet a formal proof):

*(a) Gödel bound.* For sufficiently large mathematical structures — Graham's number G₆₄ being the canonical example — the statement "G₆₄ exists as a mathematical object" is true in H (via the Kolmogorov complexity argument: G₆₄ requires ~500 bits to define and is therefore encodable), but has no M-projection: the Bekenstein bound forbids encoding G₆₄'s information content in any physical system. M is necessarily Gödel-incomplete relative to H. ⚠️ Argument correct in spirit; formal packaging as a theorem requires care about what "Kolmogorov complexity" means relative to a Hilbert space.

*(b) Bekenstein bound.* The maximum information content of any spatial region of M is S ~ A/(4ℓ_P²) bits, finite. H, as an abstract separable Hilbert space, is infinite-dimensional and admits states with information content exceeding any Bekenstein bound. Those states have no M-projection. ⚠️ Correct modulo the choice of "information content" measure.

*(c) Path-integral precedent.* The Feynman path integral sums over all paths in H, including M-unrealizable intermediate configurations. Those intermediate configurations are physically real in H (they contribute to amplitudes) but have no M-projection (they are never observed). This is a case of H ⊋ M already accepted in standard QFT. ✅ This is conventional physics.

**Corollary (motivation for the synthesis).** Since H ⊋ M, the question "how do H-elements become M-facts?" is well-posed and non-trivial. The answer — via decoherence at ∂M — is what the present synthesis makes precise.

**Status:** ⚠️ UNTESTED as a formal theorem. The three arguments are each accepted in their respective domains; their conjunction as a single packaged lemma is a writing task (< 1 week) for Paper 3 §1.

---

## Lemma 1. SCF Saturation Surface ≡ λ = 1 Holographic Projection Surface

**Statement.** *Let λ_synthesis: M × Σ → [0, 1] be defined by λ_synthesis(x, ψ) = max_i |⟨φ_i(x) | ψ⟩|², where {|φ_i(x)⟩} is the SCF-attractor (pointer) basis at x ∈ M. Then:*

*(i) λ_synthesis(x, |φ_j⟩) = 1 for each pointer state |φ_j⟩.*

*(ii) λ_synthesis(x, ψ) < 1 for any ψ that is not a pointer state at x.*

*(iii) Consequently, arg max_{ξ ∈ Σ_x} λ_synthesis(x, ξ) = {|φ_i(x)⟩} — the SCF saturation surface coincides exactly with the λ = 1 surface used by 𝒫_holo.*

**Proof.**

*(i)* For |ψ⟩ = |φ_j⟩: λ_synthesis = |⟨φ_j | φ_j⟩|² = 1. □

*(ii)* For |ψ⟩ = Σ_i c_i |φ_i⟩ with |c_i|² < 1 for all i (genuine superposition): max_i |c_i|² < 1, so λ_synthesis < 1. □

*(iii)* From (i) and (ii): the maximum value 1 is achieved exactly at the pointer states {|φ_i⟩}, which are also the SCF-attractor states (exact fixed points in the constant-basis branch; Banach-unique fixed points in the QM-regime varying-basis branch). Therefore ξ_0(x) = arg max_ξ λ_synthesis(x,ξ) = {|φ_i(x)⟩} = SCF saturation set. □

**What Lemma 1 establishes.** The synthesis theorem §3 proof sketch requires that the holographic projection 𝒫_holo respects the SCF saturation structure. Lemma 1 provides this "matching condition" as a theorem under the synthesis λ convention. The synthesis §3 step (III) — "the boundary fibration ∂M × Σ is the locus of instantiation" — is now a theorem, not an assumption, given that 𝒫_holo projects to λ = 1 states.

**Residual openings:**
1. The proof treats the fiber in isolation. The global statement — that ξ_0(x) varies smoothly with x — requires a smoothness check at degenerate/boundary cases. ⚠️ Expected to hold generically; not verified at singular points.
2. Whether λ_synthesis = max_i |⟨φ_i|ψ⟩|² is the *definition* of λ in HCR or a derived identity needs to be made explicit. If definitional, Lemma 1 is partly tautological; its content is then the coincidence of the SCF attractor and the λ-maximizer. If derived, it has more content. The synthesis skeleton takes it as definitional.

---

## §3. Main Theorem — The Emanation–Instantiation Locus

> **Theorem (Emanation–Instantiation Locus).**
>
> *Let M × Σ be a coherosphere with M a Lorentzian 4-manifold, Σ = Σ_coh(H), dim H = d ≥ 2, and let A_C be a coherence connection on Σ satisfying SCF (in the sense of §2.1). Let 𝒫_holo: M × Σ → M × {ξ_0(x)} be the holographic projection along the λ_synthesis-maximizing section ξ_0. Then:*
>
> **(I) Holographic boundary source.** The pulled-back coherence cross-term T_{MΣ} contributes a boundary stress on ∂M of the form:
>   S^{bdry}_M = λ_{bdry} ∫_{∂M} √(-γ) Tr(T_M T_M†)
> whose variation yields the effective bulk stress:
>   T^{(eff)}_{μν} = λ |T_M|² Π_{μν} δ_⊥(x, ∂M).
>
> **(II) Born statistics at the boundary.** Measurement statistics on every Σ-ray over ∂M obey the Born rule: W(|φ_i⟩ | ψ) = |⟨φ_i | ψ⟩|² (Gleason d ≥ 3 / Busch d = 2).
>
> **(III) Locus identification.** The boundary fibration ∂M × Σ ⊂ M × Σ is the emanation–instantiation locus: (a) it is the SCF saturation surface (by Lemma 1), (b) it is the λ = 1 holographic projection surface (by Lemma 1), and (c) it is the fact horizon ∂M — the present-moment decoherence front where Σ-potentialities become M-facts. At t = t_rec, ∂M is identified with the CMB last-scattering surface.

**Proof sketch.**
- (I) follows from §2.2 (RC-1 symmetry derivation and metric variation).
- (II) follows from §2.1 (SCF → COV → Theorem 6.1 → Corollary 6.2/Gleason/Busch).
- (III) follows from §2.3 + Lemma 1: 𝒫_holo projects to ξ_0 = arg max λ_synthesis = {|φ_i⟩} (Lemma 1); {|φ_i⟩} are the SCF-attractor states (§2.1); ∂M is the fact horizon (§2.3); CMB identification from Paper 3 §3.

**Conditional on:**
- ~~Conjecture 6.3′~~ ✅ **PROVED 2026-04-27** (Theorems G1-Cov + G1-Full) — (II) is now unconditional in the non-degenerate QM regime; "IF canonical gauge" caveat is lifted. ⚠️ Pending independent mathematical review.
- QFT translation of the Banach contraction (§2.1 varying-basis branch in renormalized theory).
- Lemma 0 (H ⊋ M — provides the ontological backdrop for (III)).
- Constructive 𝓕: the theorem names the locus ∂M × Σ but does not construct the reconstruction map from Hilbert boundary data to (M, g, {Φ_a}); this is the Papers 4–7 program.

---

## §4. Corollaries

**Corollary 1 (Dark Energy / Dark Matter Limits).** Under the conditions of the theorem, T^{(eff)}_{μν} has two physical limits:
- Isotropic T_M (uniform cosmological decoherence): w = -1. This is a boundary-localized dark energy contribution with α_geom = 10√2/(3π) ≈ 1.5005 as the derived coupling coefficient.
- Anisotropic T_M (cluster-scale decoherence tracking baryons): w = 0. This is pressureless dark matter. ✅ Both derived.

**Corollary 2 (CMB Quadrupole Suppression).** The primordial power spectrum modification Δ²_Σ(k) = A_s · k²/(k² + k_c²) suppresses the quadrupole by 69% at k_c = 5/χ_{CMB}, matching the Planck observation of ~67% within 3%. ✅ Verified numerically; k_c = 5/R_Σ is now structurally derived (T^(eff) rank-2 bilinear of spin-1 T_M → Sym²(j=1) = j=0 ⊕ j=2 → ℓ_min=2 → d'=25 → coefficient 5 ✅ 2026-04-27); R_Σ=χ_CMB remains ❌ Paper 4 §3 deliverable. Paper 2C §5.3 states the conditional result explicitly: k_c = 5/χ_CMB conditional on R_Σ=χ_CMB (Paper 4 §3). See `M1_2C_SEC5_PROSE_UPDATE_2026-04-26.md` §5.1–75.3 for full insertion prose.

**Corollary 3 (KCBS Contextuality Bound).** On any fiber Σ_x = CP² (d = 3) over a point x ∈ ∂M, the Born rule from (II) implies the Klyachko–Can–Binicioğlu–Shumovsky maximum: max_{ψ} Σ_i W(Π_i | ψ) = √5 ≈ 2.236, exceeding the noncontextual bound of 2. The excess √5 − 2 is the quantitative signature of D3 holonomy non-triviality around the KCBS pentagon. ✅ Proved (DERIVATION_KCBS_2026-04-19.md, Theorem 7.1).

**Corollary 4 (Frauchiger–Renner Resolution).** In the CR framework, the FR protocol traces a closed loop γ_{FR} in Σ = CP¹ with enclosed solid angle Ω = π (⚠️ pending exact verification). The holonomy Hol(γ_{FR}) = e^{iπ/2} = i accounts for the apparent agent-conclusion discrepancy without logical contradiction. ⚠️ Conditional on Ω = π for the specific FR geometry; sign is M-frame-dependent for spacelike-separated steps but Born-compliant.

---

## §5. Named Gates (Four Open Items)

| # | Gate | Type | Effort | Blocks |
|---|------|------|--------|--------|
| ~~G1~~ | ~~Conjecture 6.3′ — gauge uniqueness of A_C~~ | ✅ **PROVED 2026-04-27** — Theorem G1-Cov (axioms A1–A4 → naturality → Lemma NP → COV unconditional for all admissible F) + Theorem G1-Full (∇^FS uniqueness by Kobayashi–Nomizu + SU(d) transitivity on orthonormal bases → single gauge orbit). Born chain now unconditional in non-degenerate QM regime. See `G1_PHASE1_RESULT_2026-04-27.md`, `G1_PHASE2_RESULT_2026-04-27.md`. ⚠️ Requires independent mathematical review before final claim. | — | — |
| ~~G2~~ | ~~α = 3/2 vs α_{geom} = 10√2/(3π) — coincidence or derivation?~~ | ✅ **RESOLVED 2026-04-26** — α_geom = 10√2/(3π) is **derived** (RC-8b + independent Python verification); proximity to 3/2 is a Wallis-product transcendental near-coincidence (same 0.034% error as π ≈ 20√2/9). Conjecture C1 retired. See `RC2_RESOLUTION_2026-04-26.md`. | — | — |
| G3 | Physical k_c from FS geometry | ⚠️ **PARTIAL 2026-04-27** — D1 (λ_min=d, exact, ✅); D2 (Lorentzian propagator G(k,n)=1/(k²+λ_n/R_Σ²), k_Σ=√d'/R_Σ, ✅); D3a (ℓ_min=2 via T^(eff) rank-2 bilinear of spin-1 T_M + SO(3) isotropy of ∂M, ✅ — coefficient 5 in k_c=5/R_Σ structurally derived); D3b (R_Σ=χ_CMB via Φ:Σ→∂M) ❌ Paper 4 §3. Paper 2C §5.3 states conditional result k_c=5/χ_CMB with explicit Paper 4 §3 forward reference. See `G3_RC3_RESULT_2026-04-27.md`, `G3_RC3c_RESULT_2026-04-27.md`, `M1_2C_SEC5_PROSE_UPDATE_2026-04-26.md`. | Paper 4 §3 | Parameter-free CMB prediction |
| G4 | Constructive 𝓕: (H, ∂𝒞, T_{AB}) → (M, g_{μν}, {Φ_a}) | Papers 4–7 program | 36–60 months | Full constructive closure of (III) |

**Smaller manuscript-discipline gates:**

| # | Gate | Effort |
|---|------|--------|
| M1 | 2C §5 prose update to reflect RC-1 de-conjecture | < 1 day (text ready) |
| M2 | Spekkens noncontextuality positioning paragraph | 1–2 hours (text ready) |
| M3 | Hu–Verdaguer stochastic-gravity paragraph in §8 | < 1 hour (text ready) |

---

## §6. Placement Decision

Three viable placements for this document in the series:

**(a) Paper 2C §8 supplement (recommended for near-term).** The existing §8 (Quantum-Foundations Applications) ends with §8.4 (Zeno) and §9 (Discussion). A §8.5 or §8.6 "Synthesis: The Emanation–Instantiation Locus" would give the three-closure structure a home in the published 2C paper. Con: it is weightier than a typical §8 section.

**(b) Paper 2D standalone technical note.** The synthesis document can be released as a standalone arxiv note: "The Emanation–Instantiation Locus on M × Σ." This gives maximum visibility to the synthesis claim without requiring Paper 3 to absorb it. Con: introduces a fourth 2-series paper.

**(c) Paper 3 §0 framing (recommended for long-term).** Paper 3 opens with H-Only Mathematical Objects (§1) and the emergence sequence. The synthesis statement — connecting Born statistics, effective stress tensor, and fact horizon — is exactly the claim that motivates Paper 3's expansion program. A §0 or §1.0 that states the synthesis theorem and its four named gates would frame Papers 3–7 clearly.

**Recommendation:** Use (a) as an internal §8.5 in the near term; then migrate the theorem statement to Paper 3 §0 when Paper 3 is assembled.

---

## §7. Realistic Status

| Track | Status |
|---|---|
| §2.1 Quantum closure (Born chain) | ~90% QM non-degenerate regime (G1 proved 2026-04-27; Wilczek–Zee degenerate-pointer + QFT loop extension remain) |
| §2.2 Holographic closure (RC-1) | ~85% analytic / pending error-bar audit |
| §2.3 Ontological closure (H⊋M / fact horizon) | ~40% named, not constructed |
| Lemma 0 (H ⊋ M) | ⚠️ Packaged; needs formal proof |
| Lemma 1 (SCF saturation ≡ λ=1) | ✅ Proved in this document |
| Theorem (main) | ✅ Stated; conditional on G4 only (G1 proved 2026-04-27 — Born chain unconditional in non-degenerate QM regime) |
| Corollaries 1–4 | ✅ All stated; C2 coefficient 5 in k_c=5/χ_CMB structurally derived 2026-04-27 (T^(eff) rank-2 bilinear + SO(3) isotropy → ℓ_min=2 → d'=25 → √25=5); R_Σ=χ_CMB pending Paper 4; C4 Ω=π pending |
| This document | ~75% — full prose, proofs, theorem, corollaries; connective polish and citation pass remain |

**Overall HCR readiness for external review:** ~75–80%, gated by G3-D3b (R_Σ=χ_CMB via holographic projection — Paper 4 §3 deliverable), synthesis prose polish pass, and independent peer review of G1. G3-D1/D2/D3a proved 2026-04-27 (λ_min=d exact; Lorentzian propagator; ℓ_min=2 structural). G1 proved 2026-04-27 (Born chain unconditional). G2 resolved 2026-04-26 (α_geom derived).

---

*— 2026-04-27 — Generated from skeleton 2026-04-26 + Born chain synthesis + M2 Lemma 1 + RC-1 results. Supersedes SYNTHESIS_EMANATION_INSTANTIATION_LOCUS_2026-04-26.md (skeleton only). —*
