# The Emanation-Instantiation Locus on M × Σ

**Working title:** *The Emanation–Instantiation Locus: A Synthesis of Coherence-Field, Born-Chain, and Holographic-Boundary Results in Holographic Coherence Relativity*
**Date:** 2026-04-26
**Status:** ⚠️ DRAFT — skeleton with theorem statement and chain; prose connective tissue not yet written
**Scope:** Single-document synthesis tying SCF/COV/Born chain + RC-1 boundary action + H⊋M ontology (fact horizon, coherosphere, realized multiverse) into one theorem-and-corollaries statement.
**Audience:** Internal review (Bryan + Oz/Warp) prior to placement decision (Paper 2D appendix? Paper 3 §0? standalone tech note?).
**Supersedes:** none. **Depends on:** `paper2_ABC_OMNIBUS_AUDIT_2026-04-22.md`, `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`, `DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20.md`, `DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md`, `paper3_idea_assignments_2026-03-23.md`.

---

## Status Legend

- ✅ VERIFIED: derived in a checked-in derivation file and reviewed
- ⚠️ UNTESTED: stated, structurally plausible, calculation written but not externally checked
- ❌ MISSING: not yet derived; named gate
- 🤔 UNKNOWN: open question, no committed direction yet

---

## §0. Frame and Claim

The emanation–instantiation question — *how* potentialities on Σ become facts on M — is, in the HCR framework, decomposed across three scales:

1. **Quantum scale (Σ-internal closure).** The coherence manifold Σ = U(d)/T^d, equipped with the Fubini–Study metric and the Berry/pointer connection, supports a self-consistent fixed-point equation whose solutions force the Born rule on every measured ray. *(Source: SCF / COV / Born-chain derivations.)*

2. **Holographic projection (Σ → ∂M boundary action).** The coherence cross-term T_{MΣ} pulled back along the projection 𝒫_holo: M × Σ → M × {ξ_0} reduces to a boundary stress contribution S^bdry_M = λ_bdry ∫_∂M √(-γ) Tr(T_M T_M†), generating w = -1 (dark energy) and w = 0 (dark matter) limits and the 69% CMB quadrupole suppression. *(Source: Paper 2C RC-1.)*

3. **Ontological scale (H ⊋ M, fact horizon).** The orthoverse H strictly contains the realized manifold M; the boundary ∂M *is* the present-moment decoherence front; the past = M; the singularity = sub-Planck dissolution of M. Σ is the dual source of Q and the spacetime fabric. *(Source: Paper 3 idea assignments + omnibus audit Σ-characterization sections.)*

**Central claim of this synthesis:**

> The *locus* of emanation–instantiation in HCR is the boundary fibration ∂M × Σ ⊂ M × Σ, on which (i) the SCF/COV-pinned coherence connection A_C is rigid up to the open Conjecture 6.3′ gauge, (ii) the holographic projection 𝒫_holo collapses Σ-fibres onto λ = 1 rays, and (iii) the projected stress tensor T^(eff)_μν = λ |T_M|² Π_μν δ_⊥(x, ∂M) realizes the emanation as a boundary source for the bulk metric on M.

This is not three results in parallel; it is one chain. The synthesis document's job is to make that chain visible as a single theorem with corollaries — and to mark the four named gates (gauge uniqueness, α-reconciliation, k_c, constructive 𝓕) cleanly so reviewers see what is and isn't claimed.

---

## §1. Setup and Notation

### 1.1 Manifolds

Let H be a separable Hilbert space, dim H = d (finite-d sector; infinite-d extension flagged ❌ MISSING for the QFT translation).

- **Σ ≡ Σ_coh(H) := U(d)/T^d** — the flag manifold of H; coherence/pointer manifold. Equipped with the Fubini–Study metric g^{FS} and the canonical Berry/pointer connection A_C. ✅ VERIFIED (standard).
- **M** — Lorentzian 4-manifold (the realized spacetime). Metric g_M dynamic.
- **M × Σ** — the joint manifold; the *coherosphere* (Paper 3 terminology). ✅ VERIFIED in audit.
- **H** — *orthoverse*; H ⊋ M strictly. *(See §1.4.)* ⚠️ UNTESTED at theorem level (Gödel/Bekenstein/path-integral argument is sketched in Paper 3 ideas but not yet packaged as a lemma.)

### 1.2 Tensors and Connections

- **g_{μν}** — bulk metric on M
- **g^{FS}_{ab}** — Fubini–Study on Σ
- **T_{MΣ}** — cross-block of the joint metric/coupling tensor; component-wise G_{μa} ✅ VERIFIED in 2C §RC1.
- **A_C** — Berry/pointer connection on Σ (and, in the varying-basis branch, on M as well). ✅ VERIFIED.
- **F = ∇^{FS} + A_C** — the canonical SCF candidate. ✅ exact fixed point in constant-basis branch (Section §3 of `DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md`); ⚠️ varying-basis branch ≡ einselection equation, locally closed in QM regime by Banach.

### 1.3 The Distinguishability Field λ

λ: M × Σ → [0, 1], with λ = 1 = full distinguishability/classicality and λ = 0 = full coherence. The locus

  ξ_0(x) := arg max_{ξ ∈ Σ} λ(x, ξ)        — boundary ray on Σ over each x ∈ M

defines a section of the bundle Σ → M × Σ → M used by 𝒫_holo. ✅ VERIFIED (defined consistently across audit and 2C).

### 1.4 H ⊋ M (Ontological Layer)

The argument that H strictly extends M (not merely "H = M plus extra fibres"):

(a) **Gödel:** the formal-systems closure of M is incomplete relative to H. ⚠️ UNTESTED at theorem level.
(b) **Bekenstein:** the area-bound on M is finite; the orthoverse content is not. ⚠️ UNTESTED.
(c) **Path integral:** the realized M is one ⊂ a multi-history ensemble in H. ⚠️ UNTESTED.

→ **Pending:** consolidate (a)–(c) into a single Lemma 0 ("Strict Containment") so the synthesis can cite it cleanly. ❌ MISSING (writing task, not calculation).

---

## §2. The Three Closures

This synthesis claims that emanation–instantiation closes via the *conjunction* of three already-derived (or partially-derived) closure results, plus one ontological backdrop.

### 2.1 Quantum Closure (Σ-side: SCF + COV ⇒ Born)

> **Theorem [Born Chain, restated — see `DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20.md`].**
>
> Let A_C be a coherence connection on Σ_coh(H) satisfying:
> (i) **SCF**: F = ∇^{FS} + A_C is a fixed point of the self-consistency map T_{MΣ} = F[g_M(T_{MΣ}), g^{FS}, C];
> (ii) **COV**: A_C is SU(d)-covariant in the sense of `DERIVATION_COV_CHECK_2026-04-19.md`.
>
> Then for d ≥ 3, the induced measurement statistics on every ray of Σ obey the Born rule (via Theorem 6.1 + Gleason). For d = 2, the same holds via Busch's POVM extension.

**Status of premises:**
- (i) Constant-basis branch: ✅ VERIFIED.
- (i) Varying-basis branch: ⚠️ ≡ einselection equation; locally closed in QM regime by Banach contraction (`DERIVATION_SCF_FIXED_POINT_SUBSTITUTION_2026-04-20.md` §6).
- (ii) ✅ VERIFIED.
- Theorem 6.1 (SCF + COV ⇒ frame noncontextuality): ✅ VERIFIED in `DERIVATION_SCF_NONCONTEXTUALITY_2026-04-19.md`. ⚠️ Position relative to Spekkens generalized noncontextuality is a presentation gate (see §4 below), not a derivation gate.
- Gleason (d ≥ 3) / Busch (d = 2): ✅ standard.

**Open gates inside §2.1:**
- Gauge uniqueness — Conjecture 6.3′ (uniqueness of A_C up to gauge). ❌ MISSING.
- Wilczek–Zee / degenerate-pointer extension. ❌ MISSING.
- QFT (renormalized semiclassical) translation of the Banach argument. ❌ MISSING.
- Global continuation beyond initial Banach ball. ❌ MISSING.

→ **Realistic closure of §2.1: ~72% in the QM regime (per Born-chain synthesis).**

### 2.2 Holographic Closure (M-side: 𝒫_holo + RC-1 ⇒ effective stress tensor)

> **Result [RC-1, restated — see `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md` §RC1.1–§RC1.4].**
>
> Let 𝒫_holo: M × Σ → M × {ξ_0} be the holographic projection along ξ_0(x). The pulled-back coherence cross-term T_{MΣ} contributes a boundary stress
>
>   S^{bdry}_M = λ_{bdry} ∫_{∂M} √(-γ) Tr(T_M T_M†)
>
> whose variation yields an effective bulk stress
>
>   T^{(eff)}_{μν} = λ |T_M|² Π_{μν} δ_⊥(x, ∂M).
>
> Two cosmological corollaries follow:
> (a) **Dark energy limit:** w = -1 in the λ → 1 saturation regime. ✅ DERIVED.
> (b) **Dark matter limit:** w = 0 in the λ → 0 cluster regime. ✅ DERIVED.
>
> One observational hand-off:
> (c) **CMB quadrupole suppression:** 69% (HCR prediction) vs. 67% (Planck observation). ⚠️ UNTESTED at error-bar level — the comparison framework is correct; the propagation of uncertainty has not been audited.

**Open gates inside §2.2:**
- α = 3/2 vs α_geom = 10√2/(3π) ≈ 1.5005 reconciliation (0.03% discrepancy). 🤔 UNKNOWN — coincidence vs. derivation. **Sharpest open issue.**
- Physical k_c selection (currently CONJECTURED in 2C status table). ❌ MISSING.
- 2C §5 prose still framed as "unverified at framework level," inconsistent with the §RC1 results that close it. ⚠️ Lowest-effort highest-visibility fix.

→ **Realistic closure of §2.2: ~80% on the analytic side; observational hand-off pending error-bar audit.**

### 2.3 Ontological Closure (H ⊋ M: fact horizon as the locus)

> **Identification [Paper 3 idea assignments, formalized here for first time].**
>
> The fact horizon ∂M is the dynamical front on which Σ-side potentialities are instantiated as M-side facts. Equivalently:
>
>   ∂M(t) = { x ∈ M : λ(x, ξ_0(x)) achieves the SCF saturation condition at time t }.
>
> Cosmological identification: ∂M at t = t_rec is the CMB last-scattering surface. ✅ identified in audit / Paper 3 ideas; ⚠️ UNTESTED as a derivation (currently a definitional identification, not an outcome of an equation of motion).

**Open gates inside §2.3:**
- Lemma 0 (strict containment H ⊋ M): packaging task. ❌ MISSING (writing).
- Singularity = sub-Planck M dissolution: framing. ⚠️ UNTESTED.
- Coalescence map C: Σ → M: long-range program; not blocking this synthesis. ❌ MISSING.
- Constructive reconstruction map 𝓕: (H, ∂𝒞, T_{AB}) → (M, g_{μν}, {Φ_a}). ❌ MISSING — this is the long-range gap (G4). The synthesis claims an *existence-and-uniqueness shape* for 𝓕 via the boundary fibration ∂M × Σ as data, but does not construct it. 𝓕 is the terminal paper of a six-paper arc (Papers 2–7); the program is scoped in `PAPER7_SCOPE_CONSTRUCTIVE_F_2026-04-26.md`. Realistic horizon: 3–5 years.

→ **Realistic closure of §2.3: ~40% — the ontology is named, the fact horizon is identified, but no constructive reconstruction is in hand.**

---

## §3. Main Theorem (Synthesis Statement)

> **Theorem [Emanation–Instantiation Locus — proposed].**
>
> Let M × Σ be a coherosphere with M a Lorentzian 4-manifold, Σ = Σ_coh(H), dim H = d ≥ 3, and let A_C be an SCF/COV coherence connection (per §2.1). Let 𝒫_holo: M × Σ → M × {ξ_0(x)} be the holographic projection along the distinguishability boundary section ξ_0. Then:
>
> **(I)** The pulled-back coherence cross-term induces a boundary stress on ∂M of the form S^{bdry}_M = λ_{bdry} ∫_{∂M} √(-γ) Tr(T_M T_M†), with effective bulk source T^{(eff)}_{μν} = λ |T_M|² Π_{μν} δ_⊥(x, ∂M).
>
> **(II)** Measurement statistics on every Σ-ray over ∂M obey the Born rule (Gleason d ≥ 3 / Busch d = 2).
>
> **(III)** The boundary fibration ∂M × Σ ⊂ M × Σ is the locus on which Σ-potentialities are instantiated as M-facts; ∂M is identified with the present-moment decoherence front, and at t = t_rec with the CMB last-scattering surface.
>
> **Conditional on:** Conjecture 6.3′ (gauge uniqueness), QFT translation of the Banach contraction, and a constructive realization of 𝓕 from boundary data.

→ **Skeleton complete.** Proof = "(I) follows from §2.2; (II) follows from §2.1; (III) follows from §2.3 + the matching condition that 𝒫_holo respects ξ_0 = arg max λ."

⚠️ The "matching condition" is currently stated, not separately verified. ❌ MISSING: explicit lemma showing that the SCF saturation surface and the λ = 1 holographic-projection surface coincide. This is a candidate for **Lemma 1 of the synthesis document** and probably needs ½–1 page of Σ-side argument that has not yet been written down.

---

## §4. Named Gates (the Four Open Items)

| # | Gate | Type | Effort | Blocks |
|---|------|------|--------|--------|
| G1 | Conjecture 6.3′ — gauge uniqueness of A_C | calculation | 4–6 weeks | full closure of §2.1 |
| G2 | α = 3/2 vs α_{geom} = 10√2/(3π) reconciliation | calculation/coincidence | uncertain — could be 1 week or could be 6 months | sharpness of §2.2 numerical claim |
| G3 | Physical k_c selection in primordial spectrum | calculation | 2–4 weeks | observational predictions in §RC1.4 |
| G4 | Constructive reconstruction map 𝓕 | long-range program (Papers 4→5→6→7) | 36–60 months | full closure of §2.3; scoped in PAPER7_SCOPE_CONSTRUCTIVE_F_2026-04-26.md |

Plus three smaller manuscript-discipline gates:

| # | Gate | Type | Effort |
|---|------|------|--------|
| M1 | 2C §5 prose update to reflect RC-1 closure | writing | < 1 day |
| M2 | Spekkens generalized-noncontextuality positioning paragraph | writing + 1–2 days reading | 1–2 days |
| M3 | Hu–Verdaguer stochastic-gravity paragraph in 2C §8 Discussion | writing | < 1 day |

→ M1, M2, M3 are the highest-leverage work the synthesis can absorb in the next session.

---

## §5. Placement Decision (Where Does This Document Live?)

Three candidates, in increasing order of editorial commitment:

**(a) Paper 2D appendix.** Pro: keeps the synthesis with the RC-1 / Born-chain results that are its premises. Con: 2D doesn't exist yet; would need to scaffold a paper around the appendix.

**(b) Paper 3 §0 (Introduction).** Pro: Paper 3 is the natural home for the H ⊋ M layer; this synthesis frames the rest of Paper 3. Con: §0 is normally a *summary* not a *theorem statement*; the synthesis is too technical for §0.

**(c) Standalone technical note (recommended).** Title: "The Emanation–Instantiation Locus on M × Σ: A Synthesis of HCR Closure Results." Status: internal; cited by both 2C §8 and Paper 3 §0. Con: doesn't get archive-visible directly; a stripped-down version still needs to land in 2C §5 (per M1).

🤔 UNKNOWN: which placement Bryan prefers. Default for now: **(c)**, with the understanding that the M1 prose update will surface the same chain in 2C §5 in 2C-appropriate compressed form.

---

## §6. Realistic Status

- **Skeleton (this document):** ✅ written, reviewable.
- **Theorem statement (§3):** ✅ stated; ⚠️ Lemma 1 (matching condition between SCF saturation and λ = 1 surface) is the one new piece of mathematical work this synthesis needs.
- **Proof connective tissue:** ❌ not yet written. Each of the three closures cites its own derivation file; the synthesis itself is currently three pointers + a theorem statement, not a self-contained proof.
- **Prose:** ⚠️ §0–§4 are draft prose; §5 is a placement memo; §6 is meta.
- **Citations / bibliography:** ❌ not yet inserted (Cao–Carroll–Michalakis, Van Raamsdonk, Swingle, Spekkens, Hu–Verdaguer, Maldacena–Susskind 1306.0533, etc., per the Axis 8 draft `AXIS8_NEIGHBORING_PROGRAMS_DRAFT_2026-04-26.md`).

**Realistic completion:** ~25% of a finished synthesis document. The skeleton is the load-bearing 25%; the next 50% is filling the connective tissue (§§2.1–2.3 prose expansion + Lemma 1 proof); the final 25% is polishing, citations, and editorial pass.

---

## Next Steps

In recommended order of attack — each is a self-contained turn-sized task:

1. **Lemma 1 (matching condition):** SCF saturation surface ≡ λ = 1 holographic-projection surface. ½–1 page of math. *This is the single new mathematical contribution the synthesis needs to be self-contained.*

2. **§§2.1–2.3 prose expansion:** turn each of the three closure subsections from "premise list + status table" into ~1 page of expository prose with theorem-statement framing. ~3 pages total.

3. **Lemma 0 (strict containment H ⊋ M):** consolidate the Gödel / Bekenstein / path-integral arguments into a packaged statement, even if the proof remains "see Paper 3 ideas." ~½ page.

4. **M1 — 2C §5 prose update** (parallel track, lowest-effort highest-visibility): rewrite 2C §5 to reflect that the holographic dictionary is now derived at framework level via §RC1. < 1 day.

5. **M2 — Spekkens positioning paragraph:** insert before/around Theorem 6.1 statement to clarify HCR's frame-noncontextuality vs. Spekkens preparation-noncontextuality. 1–2 days including targeted reading.

6. **G2 — α reconciliation:** treat the 0.03% gap as a real research question; first pass is a ½-day sanity check (do the two derivations actually agree to higher order, or do they diverge?). If they diverge, escalate to G2 as a multi-week item.

7. **G1 — Conjecture 6.3′:** the calculation that closes §2.1 fully. Multi-week.

## Realistic Status of the Overall HCR Synthesis (post-skeleton)

- **§2.1 Quantum closure:** ~72% (per Born-chain synthesis).
- **§2.2 Holographic closure:** ~80% analytic / pending observational error-bar audit.
- **§2.3 Ontological closure:** ~40% (named, not constructed).
- **Synthesis-as-document:** ~25% (this skeleton).
- **Overall HCR readiness for external review:** ~65–70%, gated by G1, G2, M1, M2 in that order of leverage.

---

*— end of skeleton —*
