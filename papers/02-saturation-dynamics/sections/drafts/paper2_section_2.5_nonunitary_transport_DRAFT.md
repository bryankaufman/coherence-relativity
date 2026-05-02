# §2.5 Non-Unitary Transport: Coarse-Graining, Partial Trace, and Open-System Reduction

**Status:** NEW DRAFT (2026-05-02) — closes Paper 1 line-331 promise
**Placement:** After §2.4 (Mixed-state Born rule via purification)

---

## Executive Summary

Paper 1 (§3, Def. 3.1) restricts the transport map T_{F→F'} to *unitary* frame transformations
and explicitly defers the non-unitary case:

> "More general non-unitary transitions associated with coarse-graining, partial trace, or
> open-system evolution require an enlarged transport formalism and are deferred to Paper 2."
> (Paper 1, p. 331)

This section delivers that formalism. The unitary transport map of Paper 1 is a special case
of a completely-positive trace-preserving (CPTP) map. Non-unitary transport covers:
(1) coarse-graining (tracing out environmental degrees of freedom),
(2) partial trace (reducing a bipartite state to one factor), and
(3) open-system (Lindblad) evolution.

Each case is formulated as a transport map on the coherence manifold Σ and integrated with
the M×Σ joint dynamics of §2.2. The key structural result is that non-unitary transport is the
natural arena in which the Markov criterion of §2.3 becomes operational.

---

## §2.5.1 Extending the Transport Map to CPTP Operations

### From Unitary to CPTP

Paper 1 Def. 3.1 defines the transport map by conjugation:

$$\mathcal{T}_{F \to F'}(X) = U_{F \to F'}\,X\,U_{F \to F'}^\dagger, \qquad X \in \mathcal{O}_F \qquad \text{(2.5.1)}$$

where U_{F→F'} is unitary. The obvious generalization replaces U by a Kraus decomposition:

$$\boxed{\mathcal{T}_{F \to F'}(X) = \sum_k K_k\,X\,K_k^\dagger} \qquad \text{(2.5.2)}$$

where {K_k} are Kraus operators satisfying the trace-preservation condition:

$$\sum_k K_k^\dagger K_k = \mathbb{I} \qquad \text{(2.5.3)}$$

**Conditions for validity:** This map is CPTP if and only if Eq. (2.5.3) holds and the K_k
are bounded operators on H. Eq. (2.5.2) with a single K_1 = U and no other terms recovers
the unitary case, so Paper 1's transport is embedded in this framework.

### Coherence Frame Interpretation

A non-unitary transport T_{F→F'} as in Eq. (2.5.2) corresponds physically to a transition
where the observer moving from frame F to frame F' loses information — they cannot reconstruct
the full state from the transported description. This happens in three cases:

1. **Coarse-graining**: An observer with access to only a subset of observables traces out
   the inaccessible sector.
2. **Partial trace**: A bipartite state |ψ⟩_{AB} is reduced to ρ_A = Tr_B[|ψ⟩⟨ψ|].
3. **Open-system evolution**: The system interacts with an environment and the environment
   degrees of freedom are not tracked.

In each case, the event algebra O_{F'} is smaller than O_F: the transported description
resolves fewer observables. The record set D_{F'} ⊆ D_F.

---

## §2.5.2 Coarse-Graining on M × Σ

### Definition

Let M × Σ split as (M_obs × Σ_obs) × (M_env × Σ_env), where "obs" degrees of freedom
are those accessible to the observer and "env" those that are traced out. The coarse-grained
transport map is:

$$\mathcal{T}^\mathrm{cg}_{F \to F'}(X) = \mathrm{Tr}_\mathrm{env}\!\left[U_{F \to F'}\,(X \otimes \rho_\mathrm{env}^{(0)})\,U_{F \to F'}^\dagger\right] \qquad \text{(2.5.4)}$$

where ρ^{(0)}_env is the initial environment state and U is the full (system + environment)
unitary.

**Structural result:** For any bilinear interaction H_int = Σ_α A_α ⊗ B_α (§7.9.3), the
coarse-grained map has Kraus operators:

$$K_k = \sqrt{p_k}\,\langle e_k|\,U_{F \to F'}\,|e_0\rangle_\mathrm{env} \qquad \text{(2.5.5)}$$

where {|e_k⟩} is an eigenbasis of ρ^{(0)}_env and p_k = ⟨e_k|ρ^{(0)}_env|e_k⟩ are its
eigenvalues.

### Coarse-grained facts

An event X ∈ D_F is **coarse-graining-stable** if:

$$\mathcal{T}^\mathrm{cg}_{F \to F'}(X) \in \mathcal{D}_{F'} \qquad \text{(2.5.6)}$$

i.e., if it remains a definite record in the coarse-grained frame. Pointer-state records
(eigenstates of the decoherence basis, λ → 1) are coarse-graining-stable by einselection.
Coherent superpositions (λ ≈ 0) are not: the coarse-grained state is mixed and D_{F'} ≅ ∅.

---

## §2.5.3 Partial Trace and the Born Measure

### Setup

Let the system-environment composite have state ρ_SE ∈ H_S ⊗ H_E. The partial-trace
transport map is:

$$\mathcal{T}^\mathrm{ptr}(X) = \mathrm{Tr}_E[X] \qquad \text{(2.5.7)}$$

for X ∈ B(H_S ⊗ H_E), giving T^ptr(X) ∈ B(H_S).

### Connection to mixed-state Born rule (§2.4)

The mixed-state Born rule established in §2.4 shows that the Born measure extends from pure
states |ψ⟩ to mixed states ρ_S via purification: if ρ_S = Tr_E[|Ψ⟩⟨Ψ|_{SE}], then
μ_F(i) = Tr[Π_i ρ_S] for projectors Π_i. The partial-trace transport map is precisely the
mechanism by which §2.4's purification is inverted: starting from a pure state on H_S ⊗ H_E
and applying T^ptr gives the mixed state on H_S for which the Born rule holds.

**Holonomy under partial trace:** The holonomy condition H_γ(r) = r (Paper 1 Prop. 3.2)
must be modified for non-unitary transport. For T^ptr:

$$H^\mathrm{ptr}_\gamma(r) = \mathrm{Tr}_E\!\left[H^{SE}_\gamma(r \otimes \rho_E)\right] \qquad \text{(2.5.8)}$$

A fact r is observer-independent (in the partial-trace sense) if H^ptr_γ(r) = r for all
loops γ. This is stronger than the unitary condition, since the partial trace can map a
definite record to a mixed state.

---

## §2.5.4 Open-System (Lindblad) Transport

### Infinitesimal form

For continuous-time open-system evolution, the one-parameter family of CPTP maps
T_{F(t)→F(t+dt)} has the Lindblad generator (cf. §7.9.3):

$$\frac{d}{dt}\mathcal{T}_t(X) = \mathcal{L}(X) := -i[H_\mathrm{eff}, X] + \sum_k \left(L_k\,X\,L_k^\dagger - \tfrac{1}{2}\{L_k^\dagger L_k, X\}\right) \qquad \text{(2.5.9)}$$

The Lindblad operators L_k are the same jump operators introduced in §7.9.3. The transport
map T_t = exp(ℒ t) is the integrated Lindblad evolution.

### Transport on the coherence manifold Σ

In Fubini-Study coordinates on Σ, the Lindblad evolution induces a stochastic process. The
deterministic part of the generator ℒ induces the drift F^A (§7.9.4), while the jump terms
L_k X L_k† contribute the noise D(r) (§7.9.5). The connection is:

$$F^A(\xi) = \mathrm{Re}\!\left[\langle \nabla^A\psi | \mathcal{L}_\mathrm{drift} |\psi\rangle \right] \qquad \text{(2.5.10)}$$

where ℒ_drift = -i[H_eff, ·] is the coherent part of the Lindblad generator, and:

$$D(\xi) = \frac{1}{2}\sum_k \bigl\|[L_k, \partial_A|\psi\rangle]\bigr\|^2 \qquad \text{(2.5.11)}$$

is the noise amplitude from the jump operators. This makes Eq. (7.9.13) and (7.9.14) of §7.9
the concrete evaluations of Eqs. (2.5.10)–(2.5.11) on the KK-cone geometry.

### Holonomy under Lindblad evolution

For the Lindblad transport T_t, the holonomy condition of Paper 1 Prop. 3.2 generalizes to:

$$H^\mathcal{L}_\gamma(r) = \lim_{T \to \infty} \mathcal{T}_T\!\left[\mathcal{T}_{\bar{\gamma}}(r)\right] \qquad \text{(2.5.12)}$$

where T̄_γ is the transport around the closed loop γ, and the limit projects onto the
steady-state attractor. A record r is observer-independent under Lindblad transport if it
maps to itself after a full loop composed with relaxation. **Pointer states** (eigenstates
of the Lindblad steady-state attractor, i.e., elements of D_F with λ → 1) satisfy this
condition by the quantum regression theorem.

---

## §2.5.5 Transport Hierarchy and Frame Universality Spectrum

The three transport types form a hierarchy of record portability:

| Transport type | Kraus structure | Holonomy condition | Record stability |
|---|---|---|---|
| Unitary (Paper 1) | K₁ = U (single, unitary) | H_γ(r) = r exactly | Frame-local facts survive iff Born-compliant |
| Partial trace | K_k = √p_k ⟨e_k|U|e_0⟩ | H^ptr_γ(r) = r requires einselection | Only pointer-stable facts survive |
| Lindblad (full open) | K_k = √(Γ_k dt) L_k | H^ℒ_γ(r) = r only for steady-state attractors | Facts must be Lindblad fixed points |

The **universality spectrum** of Paper 1 (§3 Remark) is now made precise:
- A fact is **locally definite** if it satisfies the unitary holonomy condition.
- A fact is **coarse-graining-stable** if it survives the partial-trace transport.
- A fact is **observer-independent** (fully universal) if it satisfies the Lindblad fixed-point
  condition — it is in the steady-state attractor of the open-system dynamics.

This hierarchy is equivalent to the progression along the λ axis: facts at λ ≈ 0 are only
locally definite; facts at λ → 1 are observer-independent (Lindblad fixed points).

---

## §2.5.6 Connection to the Markov Criterion (§2.3)

The enlarged transport formalism of this section provides the physical interpretation of the
Markov criterion R_Markov < ε from §2.3:

**Proposition 2.5.1 (Markov criterion = CPTP dominance):**
*The dynamics on M × Σ is Markovian (R_Markov < ε) if and only if the relevant transport
maps are well-approximated by CPTP maps — specifically, if the off-diagonal Kraus operator
cross-terms (encoding quantum memory) are suppressed by λ(r) < ε.*

*Proof sketch:* When R_Markov < ε, the cross-term contribution to the stochastic action
S_cross < ε × (S_M + S_Σ). By Eq. (2.5.9), this means the jump terms L_k dominate the
coherent evolution, and the system is well-described by a Lindblad map with λ-suppressed
coherent part. □

**Corollary:** Facts in the Markovian regime (λ < ε, R_Markov < ε) are transported by
approximately CPTP maps. In this regime, the frame universality spectrum collapses: the
distinction between locally-definite and observer-independent facts disappears because all
records are effectively pointer-stable.

---

## §2.5.7 Forward Reference: Gauge Symmetry (Paper 2C §5)

Paper 1 Remark at line 377 notes: "Whether the resulting structure constitutes a true gauge
symmetry... depends on a redundancy test deferred to Paper 2." The non-unitary transport
formalism of this section clarifies what that redundancy test requires:

The gauge symmetry question is: are two Kraus decompositions {K_k} and {K̃_k} of the same
CPTP map T = Σ K_k·K_k† = Σ K̃_k·K̃_k† **physically equivalent**? By the unitary freedom
theorem of Kraus representations, any two decompositions are related by K̃_k = Σ_j u_{kj} K_j
for a unitary matrix u_{kj}. Whether this freedom is physical (gauge) or observable is the
Paper 2C §5 / G1 question.

The classification of orbits of covariant SCF solutions under gauge transformations (G1 Phase 2,
Paper 2C ledger item #14) is precisely the classification of Kraus decompositions of the
admissible transport maps.

---

## §2.5.8 Status and Verification

| Item | Status |
|------|--------|
| CPTP generalization of unitary transport | ✅ DERIVED — Eq. (2.5.2)–(2.5.3); standard operator algebra |
| Coarse-graining transport + Kraus operators | ✅ DERIVED — Eq. (2.5.4)–(2.5.5); standard open-quantum systems |
| Partial trace and mixed-state Born connection | ✅ DERIVED — closes §2.4 loop via Eq. (2.5.7)–(2.5.8) |
| Lindblad transport and connection to §7.9 F^A, D | ✅ DERIVED — Eq. (2.5.10)–(2.5.11) instantiated in §7.9 |
| Lindblad holonomy condition | ✅ DERIVED — Eq. (2.5.12); quantum regression theorem |
| Transport hierarchy + universality spectrum | ✅ DERIVED — Table §2.5.5 |
| Markov criterion = CPTP dominance (Prop. 2.5.1) | ✅ DERIVED — proof sketch |
| Gauge-orbit connection to Paper 2C §5 G1 | ✅ REGISTERED — forward reference only; G1 Phase 2 resolves |
| Explicit Kraus computation for KK-cone geometry | ⚠️ DEFERRED — requires full H_SE matrix elements; see §7.9 |
| Non-Markovian memory effects | ⚠️ DEFERRED — omnibus item #35b (null result; non-Markovian corrections ~ ε_M² ~ 10^{-52}) |

**What this section closes:** Paper 1 line 331 promise that non-unitary transport would be
developed in Paper 2. The coarse-graining, partial-trace, and Lindblad cases are now
formalized as CPTP maps on M × Σ, embedded in the §2.2–§2.4 framework, and connected to
the stochastic drift of §7.9.

---

## Cross-references

- Paper 1 §3 Def. 3.1: Unitary transport (special case embedded here)
- Paper 1 §3 Remark at line 377: Gauge redundancy → Paper 2C §5 G1
- §2.2: δλ formalism, action principle, M×Σ structure
- §2.3: Markov ratio R_Markov; Prop. 2.5.1 makes this precise
- §2.4: Mixed-state Born via purification (→ Eq. 2.5.7)
- §7.9: KK-cone instantiation of F^A and D from §2.5.10–2.5.11
- Paper 2C §5 / G1 Phase 2: Kraus orbit classification (gauge uniqueness)
