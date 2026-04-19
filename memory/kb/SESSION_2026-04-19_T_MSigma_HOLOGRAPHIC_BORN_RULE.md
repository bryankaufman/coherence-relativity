# Session Archive — 2026-04-19
**KB ID**: S-20260419-001
**Agents**: Oz (Warp) + Claude Cowork (via Perplexity handoff)
**Duration**: ~12:00–12:45 UTC (Oz log-in; Cowork session earlier same day)
**Status**: ACTIVE — Born rule derivation Section 6 open for next session

---

## Session Character

This session established the T_MΣ constraint set as the foundational object for Paper 2C
holographic structure work, produced a full Related Work skeleton with verified citations,
and initiated a serious Born rule derivation on M × CP¹. The arc moved from honest status
assessment → literature triage → concrete geometry.

---

## Part 1: T_MΣ Constraint Set — Status Assessment

**Realistic overall status: ~30% complete.** The constraint set is the genuine output.
Everything downstream (derivations, formal candidate evaluation, Born rule proof) is next-phase work.

### VERIFIED constraints (established in session, logically consistent):

1. **Self-consistency / fixed-point**: T_MΣ generates M and Σ; those outputs must be
   compatible with the T_MΣ that generated them (SCF condition).
2. **Bidirectionality**: M→Σ and Σ→M influence both exist; apparent asymmetry is
   perspective-dependent (Le Châtelier framing). **CR-novel — no peer-reviewed prior art.**
3. **Depth = band**: The interior of T_MΣ IS the admissibility band — not a separate feature.
   Existence of T_MΣ is the admissibility condition. **CR-novel conceptual move.**
4. **Threshold bifurcation**: Transition completion requires crossing a bifurcation point,
   not smooth gradient traversal.
5. **φ-component**: The φ-coordinate of Σ is conjugate to transition direction θ; stores
   and releases φ-work.
6. **Type 1 vs Type 2 decoherence**: Type 1 (reversible, φ-work recoverable by spin echo
   analogy) vs Type 2 (φ-work discharged into M, irreversible). Best-supported constraint
   — multiple independent experimental systems.

### UNTESTED / PROPOSED:
- Born rule as geometry: |⟨ψ|φᵢ⟩|² corresponds to basin widths in T_MΣ admissibility band.
- Loschmidt echo identification: f(t) = ⟨ψ|U†(t)U'(t)|ψ⟩ as observable signature of T_MΣ.
- Candidate form: Connection on fiber bundle over M × Σ.

### MISSING:
- Uniqueness argument for T_MΣ
- Born rule as formal proof
- Loschmidt echo subsection for Paper 2B
- Foundational Logical Principle as numbered axiom

---

## Part 2: Literature Survey / Related Work Skeleton

**Output**: `papers/02C-holographic-structure/CR_Related_Work_19Apr2026.docx`

### Citation status (10/12 verified):

| Constraint | Best citations | Status |
|---|---|---|
| Self-consistency / fixed-point | Lahlou, Liu, Martineau arXiv:2506.17149; Chen, Gu, Wen PRB 96, 035101 (2017); Juárez-Aubry arXiv:2509.02051 | ■ VERIFIED |
| Bidirectionality | None — CR-novel axiom | LITERATURE GAP |
| Depth = band | McInnes & Ong, Nucl. Phys. B 898 (2015) 197 | ■ VERIFIED |
| Threshold bifurcation | Nat. Commun. 7, 12745 (2016) | ■ VERIFIED |
| φ-component | Gorin, Prosen, Seligman, Strunz PRA 70, 042105 (2004) | ■ VERIFIED |
| Type 1 vs Type 2 | Gorin; Cucchietti arXiv:nlin/0201038; Domínguez et al. PRB 95, 224423; de Vega, Suter, Pastawski JCP 139, 154901 | ■ VERIFIED |
| Born rule as geometry | None — most novel claim, requires internal derivation | LITERATURE GAP |

**Warning flag**: Perplexity used `CR_Session_Record_19Apr2026.docx` as source [1] in its
literature search — confirmation bias baked into the search method. Citations verified
independently on their own merits before use.

**SG landscape paragraph** (ready to drop into Paper 2C):
Uses Juárez-Aubry 2509.02051, Juárez-Aubry 2412.08402, Merz et al. 2511.01684,
Ahmed et al. 2310.16289, Lahlou–Liu–Martineau 2506.17149.

---

## Part 3: Born Rule Derivation on M × CP¹

**Output**: `papers/02C-holographic-structure/CR_Born_Derivation_Working_Draft_19Apr2026.docx`

### What was established:

**Observation 1 — Naive basin fails** (■ established):
A ψ-independent gradient flow on CP¹ divides sphere at equator → each basin area = 1/2,
independent of ψ. Cannot reproduce Born in general. **Consequence**: the T_MΣ-flow
on the fiber must be ψ-dependent (SCF condition drives this).

**Observation 2 — The right geometric fact exists** (■ established, elementary calculation):
The cap C_above(ψ) = {Ω ∈ S² : θ_Ω ≤ θ_ψ} has area:
  A(C_above(ψ)) = sin²(θ_ψ/2) = |⟨ψ|1⟩|² = P(1|ψ)

The complementary cap C_below(ψ) has area cos²(θ_ψ/2) = P(0|ψ).
**The level set θ = θ_ψ on the Bloch sphere divides it into two caps whose areas are
exactly the Born probabilities for |ψ⟩.** This is real and exact.

**The key question (■■ not yet answered)**:
What forces this level set to be the basin boundary? The level set {θ = θ_ψ} is the locus
of states equally distinguishable from |0⟩ and |1⟩ as |ψ⟩ is from |1⟩. The claim is that
T_MΣ places the basin boundary here — forced by the SCF condition, not chosen by hand.

**Frame noncontextuality argument** (■ requires proof):
For CP¹ (qubit), the ONLY continuous W(φ|ψ) on CP¹ × CP¹ satisfying:
- W ≥ 0
- Σ_i W(φᵢ|ψ) = 1 for any complete ONB {φᵢ}
- W(Uφ|Uψ) = W(φ|ψ) for all U ∈ SU(2)
is W(φ|ψ) = |⟨φ|ψ⟩|². This follows from SU(2) symmetry of CP¹ alone — Gleason not
needed for n=2.

**Central unproven claim (Section 6 — open)**:
The T_MΣ SCF fixed-point condition, applied to M × CP¹ with pointer basis {|φᵢ⟩},
forces frame noncontextuality of the basin weight function.
→ If proved, Born follows from SU(2) symmetry (qubit) or Gleason (n≥3).

### Derivation roadmap for the proof:
1. Identify a T_MΣ-flow on the band for a given initial coherent state + pointer directions.
2. Define invariant measure on band induced by T_MΣ-flow; show relative measure of
   attraction basins = |⟨ψ|φᵢ⟩|².
3. Use Gleason-type argument (frame noncontextuality for T_MΣ-projections) for uniqueness.

### Realistic status:
- ■ Geometric fact (cap areas = Born probabilities): real and exact on CP¹
- ■ Frame noncontextuality + SU(2) symmetry → Born (no Gleason needed for n=2)
- ■■ SCF condition → frame noncontextuality: gap requiring formal proof
- ■ Physical plausibility argument given; not yet a proof

---

## Artifacts Created This Session

| Artifact | Location | Status |
|---|---|---|
| CR_Session_Record_19Apr2026.docx | papers/02C-holographic-structure/ | ✅ Copied |
| CR_Related_Work_19Apr2026.docx | papers/02C-holographic-structure/ | ✅ Copied |
| CR_Born_Derivation_Working_Draft_19Apr2026.docx | papers/02C-holographic-structure/ | ✅ Copied |
| This session archive | memory/kb/ | ✅ |
| Open Items Ledger update | papers/02-saturation-dynamics/PAPER2_OPEN_ITEMS_LEDGER_2026-04-17.md | ✅ |
| COORDINATION.md update | repo root | ✅ |

---

## Why Return Here

1. **Section 6 of Born derivation draft**: The proof that T_MΣ SCF condition forces frame
   noncontextuality is the single remaining gap between the geometric fact and the derivation.
   The most productive entry point: formulate a minimal T_MΣ-flow model on M × CP¹ and
   check what invariant measure it actually generates.
2. **Related Work skeleton → paper integration**: Ten citations are verified and can be
   integrated into Paper 2C §Related Work section as-is. The two gaps (bidirectionality,
   Born geometry) should be clearly marked as CR-novel claims with no peer-reviewed prior art.
3. **Critical gap summary**: No external paper fills the four identified gaps. Next steps
   are internal derivations, not further literature mining.

---

*Session note logged 2026-04-19 12:45 UTC by Oz (Warp)*
