# CR Series — Complete Concept Registry
**Date**: 2026-04-11
**Purpose**: Canonical map of every concept across the series. Use this before any editorial pass to resolve misassignments and cross-paper tensions.
**Papers covered**: P1, P2, P2B, P3, P4, Post-Series

Legend:
- ✅ = correctly assigned and contained in its paper
- ⚠️ = appears in wrong paper, needs relocation
- 🔀 = legitimately spans multiple papers (must be linked, not duplicated)
- ❌ = currently unassigned or at risk of loss
- 🚧 = partially developed, needs completion

---

## LAYER 0: Foundations (Paper 1)

These are primitives and first results. Everything downstream inherits them.

### Primitives (undefined in CR, taken as given)
| Concept | Symbol | P1 Status | Notes |
|---|---|---|---|
| Hilbert space | H | ✅ | dimension d |
| Physical reality | ℛ | ✅ | primitive — NOT a ray in H alone |
| Emergent spacetime | M, 𝓜 | ✅ | primitive in P1; derived in P3/P4 |
| Quantum state (frame-dependent) | \|ψ⟩_F | ✅ | |

### Core Objects (Paper 1 introduces)
| Concept | Symbol | P1 Status | Downstream |
|---|---|---|---|
| Coherence space (flag manifold) | Σ = U(d)/T^d | ✅ | Foundational for all papers |
| Coherence frame | F ∈ Σ | ✅ | |
| Frame transformation | U_{F→F'} | ✅ | |
| Joint manifold | M × Σ | ✅ introduced, P2 develops | |
| Coherence tensor field | T_AB = G_AB + Ω_AB | ✅ on Σ alone | ⚠️ NAMING CONFLICT with T_MΣ in P2 below |
| Pointer states / pointer observable | | ✅ conceptually | P2 §2.5 formalizes |

### Geometry (Paper 1)
| Concept | Symbol | P1 Status | Notes |
|---|---|---|---|
| Fubini-Study metric | G_λλ, G_AB | ✅ | Pullback from projective H |
| Berry curvature 2-form | Ω_AB | ✅ | Antisymmetric part of T_AB |
| EGY distinguishability parameter | λ = √(1−\|⟨W_L\|W_R⟩\|²) | ✅ | Coordinate on decoherence trajectory in Σ |
| Visibility | V = √(1−λ²) | ✅ | V²+λ²=1 |
| FS metric value at λ=0 | G_λλ(0) = 1/2 | ✅ | Universal; coherent end accessible |
| FS metric divergence at λ→1 | G_λλ → ∞ | ✅ | Classical records rigid |
| Ricci scalar of Σ | K_Σ | ✅ | Curvature effects (Signature 3) |

### Dynamics on Σ (Paper 1)
| Concept | Symbol | P1 Status | Notes |
|---|---|---|---|
| Arc-length along decoherence trajectory | s(λ) | ✅ | Accumulated geometric entropy |
| Geometric quasipotential | V(λ) = s(1)−s(λ) | ✅ | |
| Freidlin-Wentzell action | S[γ] | ✅ | |
| Drift field on Σ | F^A (not frame F) | ✅ ⚠️ NOTATION CLASH with frame F | |
| Full stochastic quasipotential | V_stoch | ✅ | |

### Main Results (Paper 1)
| Concept | Symbol | P1 Status | Notes |
|---|---|---|---|
| Born rule derivation | μ_F(i) = \|c_i^(F)\|² | ✅ | From axioms A1–A4 + frame invariance + additivity + continuity |
| Axioms A1–A4 | | ✅ | |
| Frame invariants | Born measures, inner products, spectra, entanglement entropy | ✅ | Theorem of invariants |
| Collapse as frame transformation | | ✅ | Central interpretive claim |
| Decoherence as trajectory in Σ | | ✅ | Geometric reframing |

### Experimental Signatures (Paper 1 — all 7)
| Signature | P1 Status | Current Testability |
|---|---|---|
| S1: Non-linear visibility scaling | ✅ | Superconducting qubits, trapped ions |
| S2: Frame-transformation hysteresis (erasure hysteresis) | ✅ | Most accessible |
| S3: Coherence-space curvature effects | ✅ | Via K_Σ |
| S4: Modified gravitational decoherence | ✅ | |
| S5: Measurable frame-change timescales | ✅ | Most accessible |
| S6: Coherence revival | ✅ | |
| S7: Zeno/anti-Zeno crossover | ✅ | |

### Paradox Resolutions (Paper 1)
| Paradox | Framing | P1 Status |
|---|---|---|
| Double slit | Two coherence frames (interference vs which-path) | ✅ |
| Wigner's Friend | Frame transformation between observers | ✅ |
| EPR/Bell | Frame-dependent entanglement; frame-invariant correlations | ✅ |
| Schrödinger's Cat | Coherence frame of macroscopic apparatus | ✅ |

### Relations to Prior Work (Paper 1)
| Framework | CR Relation | P1 Status |
|---|---|---|
| Gleason's theorem | Non-contextuality → Born, but CR explains geometric why | ✅ |
| Zurek envariance | Entanglement symmetry → Born; CR unifies geometrically | ✅ |
| Deutsch-Wallace | Rationality axioms + Everett; CR: geometry not many worlds | ✅ |
| Relational QM (Rovelli) | Observer-relative; CR: geometric language + Born derivation | ✅ |
| QBism | Operationalist; CR: frame-invariant realism | ✅ |

---

## LAYER 1: Joint Geometry Formalism (Paper 2 — Abstract Framework)

These concepts require the M × Σ arena but NOT any specific geometry (KCR-Cone).

### New Geometric Objects
| Concept | Symbol | Assigned | Location in Draft | Notes |
|---|---|---|---|---|
| Extended state map | Φ: M × Σ → PH | P2 §2.1 | ✅ | State depends on (x,ξ) |
| Full metric on M × Σ | G_AB (3-block) | P2 §2.1 | ✅ | |
| Cross-term tensor | T_MΣ = G_μa | P2 §2.1 | ✅ | ⚠️ NAME COLLISION with T_AB from P1 |
| Quantum geometric tensor | Q_AB = G_AB + i F_AB | P2 §2.1 | ✅ | Real part = G, imaginary = Berry curvature |
| Berry connection | A_x = i⟨η\|∂_xη⟩ | P2 §2.3 | ✅ | Vanishes for real dephasing |
| Bures-Kähler metric | H_MΣ = G_MΣ + iΩ_MΣ | P2 §2.5 | ✅ | Complex extension |

### δλ Formalism
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| λ as scalar field on M × Σ | λ(x,ξ) ∈ [0,1] | P2 §2.2 | 🔀 λ also used in P1 as EGY coord — same concept, different view |
| Effective cross-term | T_μa^eff = λ · T_μa^FS | P2 §2.2 | |
| Separated pullback metric | G_AB(λ) | P2 §2.2 | |
| Frame-lag equations of motion | | P2 §2.2 | |
| Frame-lag force | F_lag | P2 §2.2, §4 | |

### Markov Transition (abstract)
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| Markov ratio | R_Markov | P2 §2.3 | Abstract; norm convention unresolved → P2B |
| Markov transition criterion | R_Markov < ε | P2 §2.3 | ✅ |
| Geometric classicality | λ → 0, not ℏ → 0 | P2 §2.3 | ✅ |
| Semiclassical gravity as EFT | | P2 §2.3 | ✅ When R_Markov → 0 |
| Local classicality | | P2 §2.3 | ✅ System can be Q in one region, classical in another |

### Mixed-State Extension (Paper 2)
| Concept | Assigned | Notes |
|---|---|---|
| Mixed-state Born rule | P2 §2.4 | ✅ Via purification + Naimark dilation |
| POVM formalism P(a\|ρ) = Tr(ρM_a) | P2 §2.4 | ✅ |
| Purification of mixed states | P2 §2.4 | ✅ |

### Left-Right Generator Decomposition
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| Schrödinger picture generator | L_t | P2 §2.5 | ✅ |
| Heisenberg picture generator | R_t = Φ_t^{-1}∘L_t∘Φ_t | P2 §2.5 | ✅ |
| Divergence condition | L_t ≠ R_t when Ω_MΣ ≠ 0 | P2 §2.5 | ✅ |
| Pointer-sector criterion | L_t = R_t (pointer states) | P2 §2.5 | ✅ |
| Theorem 2.5.1 | Im(H_MΣ) = 0 iff pointer sector | P2 §2.5 | ✅ Domain: det ρ > 0 |
| Born as exchange rate between L and R | | P2 §2.4 | 🔀 bridges §2.4 and §2.5 |

### Derived Compactification (Paper 2, Part II)
| Concept | Assigned | Location | Notes |
|---|---|---|---|
| Century of assumed compactification | P2 §3.1 | ✅ | Historical narrative |
| S² as qubit coherence manifold | P2 §3.2 | ✅ | From axioms on d=2 |
| Hopf fibration S¹ → S³ → S² | P2 §3.2 | ✅ | Minimal c_1=1 bundle |
| Topology as output (not input) | P2 §3.2 | ✅ | Central result |
| First Chern number c_1 ∈ ℤ | P2 §3.2 | ✅ | Landscape selector |
| Landscape collapse 10^500 → countable | P2 §3.2 | ✅ | |
| What derived compactification constrains | P2 §3.3 | ✅ | Moduli, KK spectrum, Λ |
| Warp profile regularity from topology | P2 §3.3, §4.5 | ✅ | |
| Radion field (breathing mode) | P2 §3.3 | 🔀 P2B evaluates | |

### Abstract EOM and Holographic Conjecture (Paper 2, Part III)
| Concept | Assigned | Notes |
|---|---|---|
| Abstract EOM on M × Σ (Euler-Lagrange) | P2 §4 | ✅ |
| Frame-lag as universal mechanism | P2 §4 | ✅ |
| λ·T boundedness requirement | P2 §4 | ✅ |
| Where evaluation hits walls (norm conventions) | P2 §4.2 | ✅ Pedagogical |
| C¹ regularity from topology vs RS junction conditions | P2 §4.5 | ✅ |
| Holographic structure conjecture (abstract) | P2 §5 | ✅ Conjecture only |
| Holographic dictionary (4 entries) | P2 §5.1 | ✅ Abstract form |
| Coherence RG flow | P2 §5.1 | 🔀 Full treatment in P4 |
| Three departures from AdS/CFT | P2 §5.1 | ✅ Framework level |
| Why verification requires a geometry | P2 §5.2 | ✅ Pedagogical device |

### Pilot Wave Connection
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| Q_Bohm from Born-Oppenheimer reduction | Q = Q_BODC + Q_geom | P2 §2.3 | ✅ Algebraically exact in 1D dephasing |
| BODC (adiabatic frame-following cost) | V_BODC = (ħ²/2m)\|∂_xη\|²_Σ | P2 §2.3 | ✅ |
| KK measure term (geometric potential) | V_geom = −(ħ²/2m)∂_x²R/R | P2 §2.3 | ✅ |
| Guidance equation from BO phase | ẋ = (1/m)(∂_xS − ħA_x) | P2 §2.3 | ✅ |
| Two-slit model (1D exact) | | P2 §2.3 | ✅ SymPy verified |
| Berry phase correction to guidance | | P2 §2.3 | ✅ Vanishes for real dephasing |

---

## LAYER 2: KCR-Cone Evaluation (Paper 2B)

These concepts require the specific KCR-Cone geometry. They live in Paper 2B.

### Geometry
| Concept | Symbol | Notes |
|---|---|---|
| KCR-Cone metric | ds² = −dz² + A(r)²γ_ij dx^idx^j + dr² | |
| Exact warp factor | A(r) = cos(√2 r) | From FS Laplacian eigenvalue k²=2 |
| Eigenvalue k²=2 | | Topological invariant of CP¹ |
| WKB range | r < 0.08 r_max | |
| μ = √2 | | Geometric prediction, not fit |
| Maximal radius | r_max = π/(2√2) | Topologically frozen |
| Volcano potential | V(r) = −3 + (3/2)tan²(√2 r) | For graviton mode equation |
| Radion near-zero mode | m² ≈ 0.01 | 71% wavefunction overlap with breathing mode |

### Self-Consistency Conditions
| Concept | Symbol | Status |
|---|---|---|
| SC1: Spatial flatness | | CLOSE |
| SC2: Gravity localization | H1 PASS via B2 | PASS |
| Fifth-force coupling | α_eff = 0 exactly | |
| SC3: Cosmological constant | | RESOLVED |
| Geometric Λ from warp curvature | ρ_geom,4D = +3.534 × M_5³ k²/s | Primary source (v2) |
| Casimir energy on compact fiber | ρ_Cas | Quantum correction only |
| Self-consistent Casimir iteration | r_f* = 17.72 μm | |
| Casimir correction scale | L_Cas* ≈ 46–56 μm | Not primary prediction |
| OP-5 resolved | Topological freeze + cosmological attractor | |

### KK Spectrum and Experimental Predictions
| Concept | Symbol | Notes |
|---|---|---|
| Non-linear KK mode spacing | m_n/m_1 ≈ 1, 1.67, 2.32, 2.97 | vs Klein linear 1,2,3,4 |
| First KCR graviton | λ_1 ≈ 13.3 μm < 44 μm ISL bound | |
| Klein independence | | Derived interval replaces Klein S¹ |
| APS index | ind = 0 on [0,r_max]×S² | |
| Charge quantization via Berry phase | c_1 = 1 on CP¹ | Klein-independent |

### Holographic Verification (partial)
| Concept | Symbol | Status |
|---|---|---|
| RT formula (weakened) | S_RT ∝ d_Σ^0.80 | CV ≈ 6%; numerical |
| Proportionality α=1 | | RULED OUT (functional mismatch) |
| Confidence level | ~55% genuine duality | |

### Dark Matter (geometric)
| Concept | Notes |
|---|---|
| Geometric dark matter mechanism | Schematic; linearization unverified |
| Baryon-DM correlation as geometric consequence | |
| Flat rotation curves from KK modes | |
| Bullet Cluster offset prediction | |
| Radial acceleration relation (RAR) | |
| Tully-Fisher prediction | |

### Resolution of Abstract Ambiguities
| Concept | Notes |
|---|---|
| Norm convention lock (asymmetric) | Appendix A of 2B |
| R_Markov ~ A² in throat | |
| λ = A² identification | |
| Frame-lag F_lag = O(1), r-independent | |
| Temporal decoupling T_zr = 0 | |
| Non-traversability (Proposition 4.2) | |

---

## LAYER 3: Emergence and GR Unification (Paper 3)

### Master Principle
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| Physical Ontogeny Recapitulates Mathematical Phylogeny | | P3 §1 | |
| Level sequence L0→L1→L2→L3→L4→L5 | | P3 §1 | L0=math, L5=consciousness |

### Emergence Equation
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| Scale-covariant emergence function | s(R) = 1/(1+(R/ℓ*)²) | P3 §3 | |
| Decoherence regime | s ~ (ℓ*/R)² | P3 §3 | |
| Scale covariance group | | P3 §3 | ❌ Needs derivation |
| Born as conserved quantity across transitions | | P3 | |

### Applications to Open Problems
| Concept | Assigned | Notes |
|---|---|---|
| Measurement problem as L_t ≠ R_t (pointer states) | P3 §5 | 🔀 Pointer criterion in P2 §2.5 |
| H₀ tension as level-mismatch artifact | P3 §5 | CMB (Phase I) vs local (Phase III) calibrated differently |
| Arrow of time as L_t ≠ R_t | P3 §5 | Thermodynamic and cosmic same asymmetry |

### Thermodynamic Geometry
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| FS/Bures/Born/Entropy triangle | | P3 | |
| FS metric = geometry of unspent currency | | P3 | |
| Born rule = exchange rate | | P3 | |
| Entropy = accumulated debt | | P3 | |
| Thermodynamic uncertainty relation | dS/dλ_M ≤ ½√(F_Q^{MM}) | P3 | |

### Σ Below Planck Scale
| Concept | Assigned | Notes |
|---|---|---|
| FS/Bures has no intrinsic minimal length | P3 §3/§12 | 🔀 P2 §3.3 introduces; P3 develops |
| Planck scale = resolution limit of Φ: Σ→M | P3 | |
| Sub-Planckian structure in Σ | P3 | |

### Bridges
| Concept | Assigned | Notes |
|---|---|---|
| Decoherence Recapitulates Cosmogenesis (formal) | P3 §9 | ❌ Currently only in P2 §10 as OP-22 |
| e^{-λ_M} ~ (ℓ*/R)² scale covariance | P3 | ❌ Formal derivation missing |
| ℓ* = S(ℓ*) = S_max/2 | P3/P2B | ⚠️ Currently in P2 idea assignments only |

---

## LAYER 4: Holographic Extensions (Paper 4)

### Holographic Embedding
| Concept | Assigned | Notes |
|---|---|---|
| Σ as Susskind's 2D holographic boundary | P4 §1–2 | |
| KK-cone as emergent 3+1D bulk | P4 §1–2 | |
| Optical hologram analogy for Σ | P4 §2 | |
| FS/Bures area on Σ → entropy / information capacity | P4 §2 | |
| FS/Bures geodesic → boundary entanglement | P4 §2 | |
| Focal length f of Φ: Σ→M → Planck scale / G | P4 §3 | |
| G as restricted focal length (not free parameter) | P4 §3 | |
| Σ as Postulate (Σ-screen), with Theorem A + B | P4 §2–3 | |

### ER=EPR via Σ
| Concept | Assigned | Notes |
|---|---|---|
| S_sep (separable submanifold) → no ER bridge | P4 §4 | |
| Bell orbit (EPR locus) → ER bridge | P4 §4 | |
| ER=EPR as geometric position on Σ | P4 §4 | |

### Mach's Principle
| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| Σ-sum over entanglement sectors | g_μν^eff = F_μν[Σ_α w_α ∫ K_α(x;ψ)dμ_α(ψ)] | P4 §4–5 | |
| Inertia from global entanglement (not just mass) | | P4 §4–5 | |
| Mach as special case (coarse-grained matter only) | | P4 §5 | |

### Rosetta Stone (CR as universal wrapper)
| Concept | Assigned | Notes |
|---|---|---|
| CR ↔ holographic/AdS-CFT translation | P4 §5 | |
| CR ↔ tensor-network models | P4 §5 | |
| CR ↔ relational QM | P4 §5 | |
| CR ↔ LQG / spin networks | P4 §5 | |
| CR ↔ causal set theory | P4 §5 | |
| CR ↔ NC geometry / spectral action | P4 §5 | |
| CR ↔ string theory emergent spacetime | P4 §5 | |
| CR ↔ configuration-space relativity (Pavšič) | P4 §5 | |
| 8-framework emergent-spacetime survey (Perplexity 2026-04-11) | P4 §5 | ❌ New material, not yet in draft |

### Translatable Anlage (new 2026-04-11)
| Concept | Assigned | Notes |
|---|---|---|
| CR-string anlage 𝔄 = (H, Σ_coh(H), {Φ_str↔CR}) | P4 §5.1 | ❌ Not yet in draft |
| String → CR map Φ_str→CR | P4 §5.1 | ❌ |
| CR → String map Φ_CR→str | P4 §5.1 | ❌ |
| Two charts on X(H): CR-native + string-native | P4 §5.1 | ❌ |
| Σ_coh(H) notation standardization | P2/P4 | ⚠️ Needed in P2 notation table |
| ℓ_s ~ k ℓ_P resolution hierarchy connection | P4 | ❌ From Perplexity session |
| Casimir / vacuum energy / 120-orders in CR | P4 §3 | ❌ |

### Retrocausality
| Concept | Assigned | Notes |
|---|---|---|
| Time-symmetric at Σ, causal in M | P4 §6 | |
| TSVF: pre-selected state = early branch condition on Σ | P4 §6 | |
| Post-selected state = late-branch decohered KK-cone records | P4 §6 | |
| Two-boundary constrained point in Σ | P4 §6 | |

### Speculative / Appendix
| Concept | Assigned | Notes |
|---|---|---|
| α (fine structure constant) as information-geometric time scale | P4 appendix | |
| Frame dragging / quantum foam Σ-sum corrections | P4 §5 or P3 FD | ⚠️ Currently in P2 idea assignments |

---

## LAYER 5: Post-Series Program (Not Physics Papers 1–4)

| Concept | Venue | Notes |
|---|---|---|
| Im(H_MΣ) / Re(H_MΣ) as consciousness measure | JCS or Mind & Matter | One sentence in P4 only |
| Geometric panpsychism | Post-series | |
| Pointer states (Im=0) = zero consciousness | Post-series | |
| Markov transition = boundary of consciousness | Post-series | |
| Decoherence Recapitulates Cosmogenesis (theological depth) | Post-series | |
| Big Bang as first decoherence event | Post-series | |
| CMB as first pointer-state selection | Post-series | |
| Seraphim field framing (Isaiah 6 correspondence) | Zygon / Theology & Science | Never in physics papers |
| Full book: The Real Slice | Book | |

---

## CROSS-PAPER TENSIONS AND MISASSIGNMENTS

### Critical Notation Conflicts
| Conflict | Papers | Resolution |
|---|---|---|
| T_AB in P1 = G_AB + Ω_AB (on Σ); T_MΣ in P2 = off-diagonal block G_μa | P1 vs P2 | Adopt T_MΣ or T_{μa} for the cross-term; keep T_AB as the full tensor |
| λ in P1 = EGY coordinate (distinguishability along a trajectory); λ in P2 = scalar field on M×Σ (coupling strength) | P1 vs P2 | Same physical concept, different mathematical realization. Add notation note in P2 §1.6 |
| F as frame F ∈ Σ AND as drift field F^A on Σ | P1 | Resolved by calligraphic notation; keep as-is |
| Σ as coherence space vs Σ_ws as worldsheet (if strings) | P2/P4 | Adopt Σ_coh(H) in contexts where string notation appears |
| X(H) := M × Σ_coh(H) vs plain M × Σ | P4 idea vs P1/P2 | Use X(H) only when H-dependency is being emphasized |

### Content in Wrong Paper
| Concept | Currently In | Should Be In | Action |
|---|---|---|---|
| SC1/SC2/SC3 self-consistency checks | P2 assembled §5.1–5.3 | P2B | Extract |
| Geometric dark matter (§6) | P2 assembled §6 | P2B | Extract |
| §7 EOM KCR-Cone-specific content (~60%) | P2 assembled §7 | P2B | Separate abstract from specific |
| §8 Holographic v2 KCR-Cone content (~70%) | P2 assembled §8 | P2B | Separate |
| Decoherence Recapitulates Cosmogenesis (formal derivation) | P2 §10 as OP-22 | P3 §9 | Promote; keep pointer in P2 OP |
| ℓ* = S(ℓ*) = S_max/2 | P2 idea assignments | P3 | Move |
| Scale covariance e^{-λ_M} ~ (ℓ*/R)² | P2 idea assignments | P3 | Move |
| Casimir + Frame Dragging (Σ-sum corrections) | P2 idea assignments | P4 §5 or P3 FD | Move |
| T_MΣ^(right) dual derivation | P2 idea assignments §7 | P3 or standalone | Pending |

### Concepts at Risk of Loss (not currently in any file)
| Concept | Action |
|---|---|
| Translatable anlage (from Perplexity 2026-04-11) | Captured in perplexity_string_CR_anlage_2026-04-11.md; move to P4 draft |
| 8-framework CR survey | Same file; P4 §5 |
| Σ_coh(H) notation standardization | Add to P2 §1.6 notation table |
| Born as exchange rate between L and R geometries | In P2 idea assignments; ensure in §2.4/§2.5 |
| TSVF connection (OP-25) | In P2 §10; verify content is there |
| Three-box paradox via Berry phase (OP-26) | In P2 §10; verify content is there |
| ℓ* = S_max/2 numerical check | Needed; assign to Paper 3 |
| Formal scale covariance derivation | Needed; assign to Paper 3 |

### Concepts Legitimately Spanning Multiple Papers (require explicit linking, not duplication)
| Concept | Papers | How to Link |
|---|---|---|
| Holographic conjecture | P2 §5 (abstract), P2B §8 (evaluated), P4 (extended) | P2→P2B: "evaluated in companion paper"; P2B→P4: "extended to all frameworks" |
| Σ below Planck scale | P2 §3.3 (states principle), P3 (derives s(R)) | P2 refers to P3 |
| Decoherence Recapitulates Cosmogenesis | P2 §9/§10 (gesture), P3 §9 (formal), Post-series (depth) | P2 names it; P3 proves it |
| Casimir mechanism | P2B §5.3 (SC3 on KCR-Cone), P4 §L (extended to all frameworks) | P4 cites P2B |
| Pointer states | P1 (conceptual), P2 §2.5 Thm 2.5.1 (geometric criterion), P3 (L_t=R_t application) | Explicit theorem upgrade chain |
| Emergent spacetime M | P1 (primitive), P3 (derived from H via coherence), P4 (CR tenet: H fundamental, M emergent) | Explicit escalation of M's status |

---

## PAPER ASSIGNMENT SUMMARY

| Paper | Primary Concepts | Word Budget |
|---|---|---|
| P1 | Coherence frames, Σ geometry, Born rule derivation, 7 signatures, paradox resolutions | 15 pages, done |
| P2 | T_MΣ, δλ, Markov criterion, mixed-state Born, left-right generators, derived compactification, abstract EOM, abstract holographic conjecture, pilot wave BO | 15–20k words journal target |
| P2B | KCR-Cone evaluation: SC1/SC2/SC3, geometric Λ, Casimir correction, dark matter, holographic verification, R_Markov ~ A², exact warp factor | Companion paper |
| P3 | Emergence equation s(R), level sequence, H₀ tension, arrow of time, thermodynamic geometry, Decoherence Recapitulates Cosmogenesis (formal), ℓ*=S_max/2 | ~20k words |
| P4 | Holographic embedding of all frameworks, ER=EPR via Σ, Mach via Σ-sum, Rosetta Stone (8 frameworks), retrocausality, translatable anlage | ~20k words |
| Post | Consciousness, Seraphim, geometric panpsychism | Separate venues |
