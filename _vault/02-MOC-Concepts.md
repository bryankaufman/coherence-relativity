# MOC — HCR Key Concepts
*Core theoretical objects of the HCR research program. Each concept links to its primary definition and the papers that develop it.*

---

## Foundational Structures

### Coherence Frame (F_λ)
A coherence frame is a choice of basis in Hilbert space that defines which-path distinguishability λ ∈ [0,1].
- Primary definition: [[notes/EQUATIONS_REFERENCE]] (Def 2.1)
- Introduced: [[papers/01-coherence-frames/main]] Sec. II
- λ = 0 → fully coherent (quantum); λ = 1 → fully classical (pointer basis)

### Coherence Parameter λ
- EGY parameterization: λ ≡ √(1 − |⟨W_L|W_R⟩|²)
- N=1 metric: G_λλ = 1/[2(1−λ²)]; N=10 multi-mode: U-shaped with min at λ ≈ 0.41
- Physical meaning: degree of which-path distinguishability
- See: [[notes/EQUATIONS_REFERENCE]], [[analysis/T3A_analysis]]

### Frame Transformations
- Group/groupoid structure on coherence frame space Σ
- Non-factorizability = quantum (indivisible); factorizability = classical (Markov)
- Maps to Barandes indivisible stochastic processes
- See: [[papers/01-coherence-frames/main]] Sec. III

### Born Rule as Frame Invariant
- Theorem 4.1 in P1: unique frame-invariant probability measure on Σ
- Derived from frame-splitting, not postulated
- Extension to mixed states via purification (Paper 2A Sec 4)
- See: [[notes/EQUATIONS_REFERENCE]] (Theorem 4.1), [[papers/01-coherence-frames/BORN_RULE_DERIVATION]]

---

## The Joint Manifold M × Σ

### T_AB Tensor Field
The full metric tensor on M × Σ (spacetime × coherence space):
```
T_AB = | G_μν       T_μα |
       | T_αμ    G_αβ   |
```
- G_μν: spacetime metric (GR or emergent)
- G_αβ: Fubini-Study metric on Σ
- T_μα: cross-term (spacetime-coherence coupling)
- Defined in P1 Sec. II.3; fully derived in P2A
- See: [[notes/EQUATIONS_REFERENCE]], [[papers/02-saturation-dynamics/DERIVATION_BORN_CHAIN_SYNTHESIS_2026-04-20]]

### T_{MΣ} Cross-Term
- Physical meaning: motion through spacetime induces motion through coherence space
- T_{μα} = Re[⟨∂_μΨ|∂_αΨ⟩ − ⟨∂_μΨ|Ψ⟩⟨Ψ|∂_αΨ⟩] (mixed Fubini-Study pullback)
- Vanishes for states with no spacetime dependence
- Non-zero for spatially separated measurement apparatus
- See: [[papers/02-saturation-dynamics/sections/paper2_section_2.1_T_MSigma]]

### Quasipotential V(λ)
- V(λ) = accumulated Fubini-Study distance to classical frame
- Gradient flow limit: d x^α/dt = −G^{αβ} ∂V/∂x^β
- Attractors = pointer states (classical frames)
- See: [[notes/EQUATIONS_REFERENCE]], [[code/calculate_v_lambda]]

---

## Dynamics

### δ-λ Formalism (Frame Lag)
- λ(t): actual distinguishability; λ_eq(t): equilibrium from environment
- δ-λ(t) = λ(t) − λ_eq(t): frame lag
- Relaxation: d(δ-λ)/dt = −κ(λ)·δ-λ + ξ(t)
- κ minimal at crossover λ* ≈ 0.41 — lag persists longest here
- See: [[papers/02-saturation-dynamics/paper2_mathematical_spine_2026-02-28]]

### Saturation / SCF (Saturation Coherence Frame)
- The fixed point of the frame-lag dynamics
- SCF = configuration where frame evolution saturates
- Key active research area; see G1 phase results
- See: [[papers/02-saturation-dynamics/G1_PHASE1_RESULT_2026-04-27]], [[memory/kb/SESSION_2026-04-19_COV_CHECK_CANDIDATE_SCF]]

### Coordinate-Invariant Markov Criterion
- Transition ratio: G_MM^new(λ*) / G_λλ(λ*) = 1
- Below: reversible (quantum); above: irreversible (Markov/classical)
- Independent of coordinate choice and coupling strength
- See: [[papers/02-saturation-dynamics/RC2_DERIVATION_2026-04-17]]

---

## Numerical / Computational Objects

### T3A Casimir Spectral Analysis
- 5D compactified Casimir vacuum energy landscape
- Scripts: [[code/calculate_g_lambda]], [[analysis/T3A_casimir_spectral]]
- Results: [[analysis/T3A_analysis]], [[analysis/T3A_multispin_full_SM]]
- Latest: antiperiodic boundary conditions, v3 stage 1+2 JSON outputs

### G_λλ(λ) Metric
- Fubini-Study metric component for coherence space
- N=10 multi-mode: U-shaped, min at λ ≈ 0.41
- Computed by: [[code/calculate_g_lambda]]
- Figure: [[figures/fig1_g_lambda]]

---

## Holographic & Cosmological Connections

### Holographic Principle in HCR
- Vol(Σ_accessible) ~ exp(S(ρ_A)) — Ryu-Takayanagi structure from Σ geometry
- Emergent spacetime conjecture: G_μν = ∫_Σ G_αβ projected onto M
- Primary paper: P2C [[papers/02C-holographic-structure/paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17]]
- Session: [[memory/kb/SESSION_2026-04-19_T_MSigma_HOLOGRAPHIC_BORN_RULE]]

### Geometric Dark Matter (Sec 6)
- Dark matter as geometric effect of coherence frame structure
- See: [[papers/02-saturation-dynamics/sections/paper2_section_6_geometric_dark_matter]]

### KK Cone Model (Sec 4.0)
- Kaluza-Klein cone compactification in HCR framework
- See: [[papers/02-saturation-dynamics/sections/paper2_section_4.0_KK_Cone_model]]

### Topology as Output (Sec 3.2)
- Spacetime topology emerges from coherence frame structure
- See: [[papers/02-saturation-dynamics/sections/paper2_section_3.2_topology_as_output]]

---

## External Connections

### Barandes Indivisible Stochastic Processes
- Barandes (2309.03085): indivisible process ↔ unitary quantum evolution
- Mapping: Σ = Barandes stochastic configuration space; indivisibility = non-factorizability of frame transforms
- See: [[notes/EQUATIONS_REFERENCE]], [[papers/02-saturation-dynamics/paper2_mathematical_spine_2026-02-28]]

### Neighboring Programs
- See: [[papers/03-gr-unification/AXIS8_NEIGHBORING_PROGRAMS_DRAFT_2026-04-26]]
- Everett, QBism, RQM, GRW, Penrose, Zurek envariance, Deutsch-Wallace
- Reference notes: [[literature/LITERATURE_REVIEW]]
