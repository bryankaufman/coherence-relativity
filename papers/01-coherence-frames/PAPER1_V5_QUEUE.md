# Paper 1 v5 Improvement Queue

**Baseline**: v4 (Zenodo concept DOI: 10.5281/zenodo.18675342; prepared 2026-04-04)
**v4 additions**: §5.6 Sleeping Beauty, §5.5 Zeno D_f completion, §5.0 meta-theorem, Prediction 7, 21 pages

Items below are queued for v5. Each carries a status, source, and the section it affects in main.tex.

---

## 1. §5.6 Sleeping Beauty — Remaining Formal Items

**Status**: §5.6 content 95% complete (draft April 5, Claude review April 5). Two items not yet integrated into main.tex.

**Item 1a** — Definition 2 addendum:
> Add one sentence: "Information never received by a system is excluded from its accessible sector on the same footing as information decohered to the bath."
Source: Claude review 2026-04-05 01:31. Addresses the gap that makes the amnestic-drug = decoherence argument explicit in the formal definitions.

**Item 1b** — Axiom numbering: RESOLVED (Warp, 2026-04-08). EQUATIONS_REFERENCE.md reconciled to main.tex numbering A1-A4. main.tex already correct.

**Target section**: §II (Coherence Frames, Definition 2) + §V.F (Sleeping Beauty)

---

## 2. §5.6 Sleeping Beauty — Strengthened Preferred-Basis Formulation

**Status**: NEW — from decoherence video analysis (2026-04-13)

**Content**: The current §5.6 states that F_wake uses the Born measure over centered alternatives. The sharper formulation from the analysis:

> **Preferred Basis Criterion**: A basis is preferred iff self-locating propositions can be consistently assigned truth values within that basis.

This is a theorem-level sharpening: the pointer basis selected by decoherence is exactly the basis in which an observer can coherently ask "which outcome am I in?" The Sleeping Beauty setup illustrates this — the coin outcome was never in Beauty's accessible sector, so the three centered alternatives {H_Mon, T_Mon, T_Tue} are all in the accessible basis at F_wake.

**Connection to main.tex**: Strengthens the claim that A3 (Dependence) applied to the accessible sector gives the thirder answer without Elga's counterfactual. Also connects §5.6 directly to §2 (Definition 2 gap above).

**Target section**: §V.F (add remark after the Step 2 derivation)

---

## 3. §5.6 — Records as the Only Past (Temporal Self-Location)

**Status**: NEW — from decoherence video analysis (2026-04-13)

**Content**: Beauty's amnesia is the destruction of a temporal record — decoherence of the temporal self-location degree of freedom. This is not merely analogical: in the CR framework, "the past" is the structure of present records, and records are stable precisely because decoherence has acted. The amnestic drug protocol introduces self-locating degrees of freedom into Σ_full by *destroying* record structure, not by creating new information.

**Formal statement**: The transition F_pre → F_wake removes the "which awakening" record from the accessible sector of Σ, increasing the self-locating uncertainty. This is the decoherence of a temporal DOF, handled by T_AB in the same way as any other bath-coupling.

**Target section**: §V.F (could be a parenthetical remark or footnote connecting to §V.E Zeno and to Paper 2A §2.1 T_MΣ)

---

## 4. Empirical Anchoring from Decoherence Video

**Status**: NEW — from YouTube extraction of Faultlines Studio video "Decoherence Was Discovered in 1970..." (video ID: D0DWgD7Tvx8, extracted 2026-04-12; 51 concepts, 26 facts)

**Content**: The following empirical facts from Joos & Zeh (1985) and subsequent work provide concrete grounding for claims already in Paper 1:

| Fact | Paper 1 connection |
|------|-------------------|
| Dust grain in air: decoherence time ~ 10⁻³¹ s | Quantifies what "effectively instantaneous" means for macroscopic objects; anchors Discussion claim that classicality is manufactured collision-by-collision |
| Best laboratory vacuum: ~ 10⁻¹⁴ s | Shows decoherence is environment-relative, supporting the frame-relative coherence claim |
| Intergalactic void (CMB only): ~ 1 s | Extreme limit; illustrates that coherence is always relative to the environment |
| Hyperion (Saturn moon): would be in 57° superposition without decoherence | Concrete macroscopic example for the Discussion; supports CR's claim that classicality is not inherent |
| 26 years from Zeh (1970) to Haroche experimental confirmation (1996) | Historical framing for the Introduction: sociological resistance parallels CR's own interpretive shift |

**Target section**: §V.D (Schrödinger's Cat resolution) and/or Discussion (§VI); also Introduction if a historical framing paragraph is added. These are empirical citations to Joos & Zeh (1985) and Haroche & Wineland (2012 Nobel lecture).

**Required bib entries**: Joos & Zeh (1985) Z. Phys. B 59:223; Haroche (2012) Nobel lecture; Zurek & Paz (1995) Phys. Rev. D 52:2508.

---

## 5. Prediction 8 (New) — No Preferred Basis Without Observer Constitution

**Status**: NEW — from decoherence video analysis (2026-04-13)

**Content**: If the preferred basis is the basis in which self-location is possible (§2 above), then systems incapable of supporting observer-structures should have no privileged basis. Specifically:

> **Prediction 8**: For quantum systems in which decoherence is prevented and no observer-structure can be maintained, no basis should emerge as preferred. Attempts to impose measurement-like interactions on such systems should fail to produce definite outcomes in any basis.

**Experimental approach**: Sophisticated interferometry with decoherence-protected systems (superconducting qubits in engineered environments). Compare outcome statistics with and without observer-structure coupling. CR predicts: without observer-structure coupling, no preferred basis → no definite outcomes in any fixed basis. Hidden-variable theories predict definite outcomes regardless.

**Distinguishing feature**: This is different from Predictions 1–7 in that it targets the *absence* of preferred basis selection rather than its rate or hysteresis. It does not require access to the τ_transform timescale (Prediction 5).

**Target section**: §VI (Experimental Predictions, after Prediction 7)

---

## 6. Referee Response Integration

**Status**: Check — the paper1_referee_response.tex was prepared but referee comments may have suggested specific edits that haven't been integrated into main.tex.

**Action**: Review `papers/01-coherence-frames/paper1_referee_response.tex` for any accepted corrections that should be incorporated into main.tex before v5.

---

## 7. §5.5 Zeno — MIPT Connection (Collapse as Phase Transition on Σ)

**Status**: NEW — from Perplexity string/CR session (undated, pre-2026-04-13)

**Content**: The D_f completion framing of §5.5 (Zeno measurement completes D_f classicalization) now has an explicit connection to the MIPT literature. The MIPT critical point p_c is the same phenomenon as the D_f completion threshold τ_meas ≈ τ_transform from Prediction 7. Specifically:
- Below p_c: stationary distribution on Σ weights coherent frames → superpositions persist
- Above p_c: distribution concentrates near pointer frames → collapse stabilizes
- The CR quasipotential V(F) develops non-analytic behavior at p_c, matching the MIPT entanglement transition

The key MIPT citations to add: Li et al. (2018) PRB 101:104301; Bao et al. (2020) PRB; Google Quantum AI MIPT experiment (PhysRevX 14, 041012, 2024).

**Target section**: §V.E (add 2-3 sentences connecting D_f completion to MIPT literature; this upgrades Prediction 7 from a standalone CR claim to a connection with an experimental literature)

---

## 8. Notation Clarification: Σ Overloading

**Status**: NEW — from Perplexity string/CR session

**Content**: The session identified that Σ is overloaded across different contexts. Paper 1 should explicitly state:
> *Throughout this paper, Σ ≡ Σ_coh(H) = U(d)/T^d denotes the coherence manifold (flag manifold) of a Hilbert space H. This is distinct from the string worldsheet Σ_ws used in string theory and from configuration spaces Map(Σ_ws, M). The notation Σ_coh(H) will be adopted in Papers 2+ to prevent ambiguity.*

This one-sentence clarification in §II (Definitions) prevents a category error that confused even a sustained Perplexity session.

**Target section**: §II footnote or Definition 1

---

## 9. Causal Direction Disambiguation (Discussion §VI)

**Status**: NEW — from conceptual review 2026-04-13

**Content**: The frame-lag language in Paper 2A (§2.2) risked reading as if M drives Σ, inverting the ontological hierarchy. The clarification — now added to Paper 2A §2.2 Executive Summary — should also appear in Paper 1’s Discussion or Implications section, where T_AB is introduced and the M × Σ arena is first described.

**Precise point**: The Discussion should explicitly state that M × Σ dynamics are **bidirectional within the constituted space**; neither sector drives the other ontologically. T_AB couples M and Σ in both directions simultaneously. The ontological direction (H ↠ Σ ↠ M) is constitution, not dynamical causation. When the Discussion uses language like "the environment drives decoherence," add a parenthetical: "(where the environment is itself a projection of H onto M coordinates)."

**Target section**: Paper 1 §VI Discussion, paragraph on T_AB and emergent spacetime.

---

## 10. Bloch Sphere Dual-Role Remark (§II — Coherence Frames)

**Status**: NEW — pedagogical necessity, 2026-04-15

**Problem**: The Bloch sphere appears in quantum mechanics both as the space of pure qubit states (PH = CP¹) AND as the coherence frame space (Σ = U(2)/T² ≅ CP¹). For d=2 these are the same manifold. Anyone not already steeped in quantum information will conflate them — and even experts may not immediately see that CR is working in the *frame* interpretation, not the *state* interpretation. This must be made explicit.

**Where**: §II (Coherence Frames), as a Remark immediately after Definition 1 (Coherence Space) or Definition 2 (Coherence Frame).

**Draft Remark**:

> **Remark 2.1 (Bloch Sphere: Two Roles).** For a qubit ($d=2$), the coherence space $\Sigma = U(2)/T^2 \cong \mathbb{CP}^1 \cong S^2$ is geometrically the same manifold as the space of pure qubit states $\mathcal{PH} = \mathbb{CP}^1$. This coincidence can cause confusion: the Bloch sphere plays two conceptually distinct roles.
>
> *As state space $\mathcal{PH}$*: each point represents a quantum state $|\psi\rangle$ — where the qubit *is*. A state $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\varphi}\sin(\theta/2)|1\rangle$ is a location on the sphere.
>
> *As coherence frame space $\Sigma$*: each point represents an orthonormal basis $\{|e_1\rangle, |e_2\rangle\}$ of $\mathbb{C}^2$ (up to T² phase factors) — which direction the observer calls "definite." A frame is not a state; it is a choice of measurement axis.
>
> In the coherence-relativity framework, $\Sigma$ is always the frame space. A qubit state $|\psi\rangle$ is represented *in* a frame $F = \{|e_1\rangle, |e_2\rangle\}$ as amplitudes $c_1, c_2$ where $|\psi\rangle = c_1|e_1\rangle + c_2|e_2\rangle$; the Born probabilities $\mu_F(i) = |c_i|^2$ are frame-invariant (the central result of §IV). For $d > 2$, state space $\mathcal{PH} = \mathbb{CP}^{d-1}$ and frame space $\Sigma = U(d)/T^d$ are different manifolds, and the distinction becomes unavoidable.

**Why this matters**: Without this remark, a reader familiar with the Bloch sphere will automatically read every statement about Σ as being about states, missing that CR is about the observer's perspective (frames), not the system's location (states).

**Target section**: §II, immediately after Definition 2 (Coherence Frame).

---

## Priority Order for v5

1. **Item 1a** — Definition 2 addendum (small, formal, already reviewed)
2. **Item 2** — Preferred basis criterion sharpening in §5.6 (strengthens existing content)
3. **Item 3** — Records/past remark in §5.6 (closes the amnestic argument formally)
4. **Item 4** — Empirical anchoring citations (requires bib additions, non-trivial but high value)
5. **Item 5** — Prediction 8 (new section, requires careful drafting)
6. **Item 6** — Referee response check (diagnostic first)

---

## v5 Rebuild Checklist (when ready)

- [ ] All main.tex edits integrated
- [ ] master.bib updated with new entries
- [ ] LaTeX build clean (zero errors, zero undefined refs)
- [ ] PDF verified (section numbers, cross-refs, figure labels)
- [ ] Zenodo new version upload
- [ ] OSF metadata updated
- [ ] COORDINATION.md log entry
