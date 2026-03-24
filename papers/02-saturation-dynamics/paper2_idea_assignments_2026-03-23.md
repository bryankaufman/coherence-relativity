# Paper 2 — Idea Assignments & Section Backlog
**Compiled**: 2026-03-23
**Target file**: papers/02-saturation-dynamics/paper2_idea_assignments_2026-03-23.md
**Sources**: CR_loose_ideas_abstracts_2026-03-23.md + CR_PDF_ideas_abstracts_2026-03-23.md

---

## 🔴 IMMEDIATE — Spike 11 B2 Decision (Unblocks H1)

**Section**: Appendix A (H1 entry in A.2/A.4) + §5.26 H1ADJUDICATIONRECORD

Both B1 and B2 give H1 PASS. Adopt **Option B2 (locked ratio)** — cleaner at
adjudication order, no half-baked graviton KE derivation needed now.

**Paste into Appendix A:**

> For the purposes of the H1 fifth-force gate at adjudication order, we adopt
> Option B2 (locked ratio). The SC2 branch lock and the associated normalization
> package in Paper 2 §5.26 are taken as the primary definition of the 4D Einstein
> sector on branch B. Under this convention, the effective 4D Planck mass is treated
> as independent of L_f at this order, i.e. dMP_eff/dL_f = 0, and the Weyl-rescaling
> coupling of L_f to NR matter vanishes, g_W = 0. Together with the structurally exact
> Jordan-frame result g_{J,NR} = 0 on SC2, this gives ε_eff = 0 exactly at this
> closure level. H1 therefore upgrades from MARGINAL-FINAL to PASS: the
> radion-mediated fifth force is absent at this order, and any subleading corrections
> from a future explicit graviton KE reduction are bounded by the existing estimate
> ~10^{-5}, far below Et-Wash sensitivity.

**Update §5.26 H1ADJUDICATIONRECORD:**
Replace "Tier-2 verdict provisional PASS, formal ε_eff derivation pending" with:
"Tier-2 verdict PASS under B2; ε_eff = 0 at adjudication order; optional B1
refinement spike left open."

---

## §2.1 / §2.3 — Born-Oppenheimer Derivation of Q_Bohm

**Idea A** | Priority: Very High | Status: Structurally complete

The quantum potential Q of pilot-wave theory is not postulated — it emerges as
the Born-Oppenheimer effective potential from integrating out Σ on M × Σ.

**Q_Bohm = V_BODC + V_geom**

- **V_BODC** (adiabatic frame-following cost): When x moves through varying Γ(x),
  maintaining adiabatic following costs energy ∝ |∇Γ|². Under Γ = −2 ln R, gives
  (∇R/R)² — first piece of Q_Bohm.
- **V_geom** (KK measure effect): x-dependent Σ volume det G_{ab} ∝ η(x).
  Weyl transformation absorbing this measure factor generates ∇²Γ — second piece.

Both pieces are scalar potentials (velocity-independent), both vanish at λ → 0,
both require mixed states.

**✅ VERIFIED**: Structural match. Both derivative structures arise from BO decomposition.
**⚠️ UNTESTED**: Exact coefficient match (requires γ < 0, case-by-case verification).
**❌ NOT SHOWN**: Multi-particle extension, guidance equation part.

**Placement**: §2.1 main text (~1200 words) + new §2.3 + Appendix (~2000 words full computation).

---

## §2.3 — Two-Slit Pilot Wave as Explicit BO Reduction

**Idea B** | Priority: High | Status: Pipeline defined, needs execution

Derive the two-slit pilot wave explicitly within CR:

1. M × Σ model: 1D config space on M; Σ as mixed-state sector with Γ(x).
2. BO Ansatz across both slits: Ψ(x) = Σ_k φ_k(x) ⊗ χ_k(Σ).
3. BO reduction for two-channel superposition → recover Q_Bohm and guidance
   equation ∇S/m from BO wave function phase.
4. Show Q = ℏ²/2m · ∇²R/R as a theorem, not a postulate.

**Notation box for §2.1** (paste near first appearance of Q):

> Notation: decomposition of the quantum potential
> Q = Q_BODC + Q_geom
> Q_BODC: Born-Oppenheimer diagonal correction (adiabatic frame-following cost).
>   Encodes kinetic cost of transporting optimal coherence frame over M;
>   geometrically = squared FS/Bures norm of ∇_x χ on Σ.
> Q_geom: geometric measure term. Arises from x-dependence of Σ volume element
>   det G_{ab}(x); scalar correction from FS/Bures volume form under M × Σ → M
>   reduction. Both terms vanish in classical limit λ → 0.

**Cross-reference for "Relation to Quantum Foundations" subsection:**

> In the 1D two-slit toy model developed in Appendix X, this decomposition
> reproduces the standard Bohmian quantum potential: when the Σ-sector is
> instantiated with the FS/Bures geometry and reduced via the BO procedure, the
> combined term Q_BODC + Q_geom coincides with the familiar expression
> −ℏ²/2m · ∇²R/R for effective configuration-space amplitude R.

---

## §2.4 — Born Rule as Exchange Rate Between Two Geometries

**Idea from loose_ideas** | Priority: Write | Status: Conceptually complete

Born rule is not merely a frame-invariant within one picture — it is invariant
across both Schrödinger and Heisenberg pictures simultaneously.

|⟨ψ|φ⟩|² = invariant of |H|, not just G

where H = G + iΩ = G(1 + iJ) is the full complex Hermitian metric.

- D₁ (trace distance) = Schrödinger currency
- D∞ (operator norm) = Heisenberg currency
- Born rule = exchange rate between them

Add to §2.4 write-up. No new derivation needed — reframing of existing result.

---

## §7 (EOM on M × Σ) — T_MΣ Right-Generator Dual

**Idea from loose_ideas** | Priority: High | Status: Needs derivation

T_MΣ^(left) is derived from L_t (Schrödinger). There is a dual
T_MΣ^(right) from R_t = Φ_t^{-1} ∘ L_t ∘ Φ_t (Heisenberg).

They diverge when Ω_MΣ ≠ 0 (multi-qubit, non-Markovian case).

**TODO**: Derive T_MΣ^(right) in single-qubit case. Confirm T_MΣ^(left) =
T_MΣ^(right) iff pointer state condition (L_t = R_t at pointer states).

**Cite**: Settimo et al. (2026), PRX Quantum 7, 010340. DOI: 10.1103/6dt2-sq44

---

## §7 — Full Complex Metric H = G + iΩ

**Idea from loose_ideas** | Priority: High | Status: Conceptual, needs EOM rewrite

Paper 2 currently works only with Re(H). Full theory requires H.

H_ij = G_ij + iΩ_ij = G_ij(1 + iJ)

Rewrite §7 EOM throughout using H rather than G. No equations wrong —
all need promotion to complex versions.

Fiber bundle structure:
- arg(H_MΣ) ∈ [0, π/2] parametrizes U(1) fiber
- Coherence frame transformations act on |H_MΣ| (base)
- J acts on arg(H_MΣ) (fiber)

---

## §5.3 / §10 — ℓ* = S(ℓ*) = S_max/2 Prediction

**Idea from loose_ideas** | Priority: High if confirmed | Status: Needs numerical check

If ℓ* ~ 12.96 μm (Casimir result), and Born rule is conserved currency across
all level transitions, then ℓ* should mark the entropic watershed:

S(ℓ*) = S_max / 2

**TODO**: Compute S_max for observable universe. Compute S(ℓ*) from Casimir
result. Check ratio. If not 1/2, determine what ratio it gives.

Note: Hopf fiber density n_fiber = 1/4 at r = ℓ* provides independent geometric
grounding for the S_max/2 claim (already derived in §4.5.6).

---

## §5.3 / §9 Discussion — Decoherence Recapitulates Cosmogenesis

**Idea from loose_ideas** | Priority: High — in chat only, at risk of loss

Every quantum decoherence event enacts the same three-phase sequence the
universe traversed cosmologically. Scale covariance:

e^{−λ_M} ~ (ℓ*/R)²

The cosmic transition happened once. Every measurement enacts it continuously.
Born rule is the conserved "genetic code" across both.

**Arrow of time**: thermodynamic irreversibility and cosmological expansion are
the same asymmetry at different scales.

**TODO**: Formal derivation of scale covariance. Explicit map from e^{−λ_M} to
(ℓ*/R)² with proportionality constant. Verify Born rule is the correct conserved
quantity across both transitions.

---

## Future Directions (§10 or §9 Discussion)

### Casimir + Frame Dragging (paste-ready for §5.3 Casimir section)

> Future direction. The Casimir-completed sector in the present KK-cone model is
> introduced solely to close SC3 at the level of the effective cosmological term.
> However, in the broader CR framework, the same Σ-sum over vacuum (Casimir)
> fields and non-local entanglement in the quantum foam could, in principle, feed
> into the off-diagonal components of the emergent brane metric, leading to small
> corrections to rotational and frame-dragging observables. Quantifying whether
> such effects exist, and if so whether they are observationally relevant, is outside
> the scope of this paper and is reserved as a direction for future work.
