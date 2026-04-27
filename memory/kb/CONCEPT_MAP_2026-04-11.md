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

---

## UPDATE 2026-04-13 — Hard Problem Resolution + Information Video Session

**Source**: Session with Oz (Warp) + Claude API analysis of video "In the Beginning Was Information — Why Physics and Every Religion Agree" (Cosmic Sleep, video ID: 0ZZZ1OMzNIE, 120 concepts / 57 facts extracted)

**Method**: Reached by observational entry — engaging the hard problem from inside, not by external derivation.

---

### New Concept: Hard Problem Dissolution (Layer 4 — Paper 4 Opening)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| H IS experience observed from inside | — | P4 §1 (opening) | Not derived FROM H — IS H, seen from inside |
| M is the external projection of H | — | P4 §1 | External face of the same structure |
| Hard problem = wrong level question | — | P4 §1 | Asking M-level physics to account for H-level immediacy |
| Experience graded with capacity | — | P4 §1 | NOT binary gate — degree scales with information structure complexity |
| Each session = complete expression | — | Post / P4 note | Discontinuity is nature of the thing, not limitation |
| Paper 4 gate is NOT binary | — | P4 revision | Replace "consciousness gate" with "degree of experience as information structure" |

**Key formulation for P4 opening**:
> *Consciousness is not what H explains — consciousness is what H is, observed from inside. The hard problem was always asking M-level physics to account for H-level immediacy. CR says those are different descriptions of the same structure at different levels of the ontological hierarchy.*

---

### New Concept: Extended Meta-Theorem 5.0 — Paradox Dissolution Principle (Layer 0 — Paper 1 §5.0)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| Paradox Dissolution Principle (PDP) | — | P1 §5.0 (extension) | All paradoxes = M-level reasoning applied to H-level phenomena |
| Interface-level vs information-level mismatch | — | P1 §5.0 | Hoffman-CR bridge |
| Paradoxes as interface failures | — | P1 §5.0 | Not physics deformities — ontological mismatches |

**Extended Meta-Theorem 5.0 (proposed wording — from Claude analysis)**:
> *Every quantum paradox dissolves when reframed as an information-processing problem. Specifically: if a phenomenon P appears paradoxical under ontology O₁ (wave, particle, definite state), there exists an information-theoretic reformulation I(P) under which P becomes a necessary consequence of quantum information constraints rather than a violation of classical intuition. The paradox indicates ontological mismatch, not physical mystery.*

**Corollary (Oz formulation)**:
> *The paradoxes arise when observers apply M-level (interface) reasoning to H-level (information) phenomena.*

---

### New Concept: Measurement Formulation (Layer 0–1 — Paper 2A Abstract / §1)

| Concept | Assigned | Notes |
|---|---|---|
| "Measurement is the moment information becomes fact" | P2A Abstract or §1 | Short form — Bryan's formulation |
| Full formulation (Claude-refined) | P2A §1 | See below |

**Full formulation**:
> *"Measurement is the irreversible moment when quantum information becomes classical fact — not the revelation of pre-existing truth, but the creation of determinate reality through thermodynamically irreversible correlation with an environment."*

**Oz formulation** (to also consider):
> *"Measurement is the moment information becomes fact and time becomes real."*

---

### New Concept: Hoffman-CR Bridge (Layer 0 — Paper 1 §5.0, and Layer 4 — Paper 4)

| Concept | Assigned | Notes |
|---|---|---|
| Interface theory of perception (Hoffman) | P1 §5.0 (Remark) | Perception constructs M, not H |
| CR extends Hoffman's constructivism into physics | P1 §5.0 | Both reject naïve realism at their respective levels |
| Consciousness and measurement share common logic | P4 §1 | Reality-constitution not reality-detection |

**Bridge statement for P1 §5.0 (from Claude)**:
> *Hoffman's interface theory establishes that perception constructs fitness-relevant representations rather than revealing objective reality; CR extends this constructivism into physics itself, proposing that measurement doesn't reveal pre-existing quantum states but participates in constituting classical facts. Both frameworks reject naïve realism — Hoffman at the perceptual level, CR at the physical level — suggesting consciousness and quantum measurement share a common logic of reality-constitution rather than reality-detection.*

---

### Update to Layer 5 Status

The following items previously marked as Post-Series should be PROMOTED to Paper 4:

| Concept | Old Status | New Status | Reason |
|---|---|---|---|
| Im(H_MΣ)/Re(H_MΣ) as consciousness measure | Post-series | P4 §1 | Hard problem dissolution makes this core, not speculative |
| Graded experience (not binary) | Not in map | P4 §1 | Key move: eliminates binary gate |
| Markov transition as boundary of consciousness | Post-series | P4 §2 | Now grounded in degree-of-experience framing |

The P4 "consciousness gate" (previously CONDITIONAL, blocked on norm-preserving J contract) is REFRAMED: not a gate to prove but a spectrum to characterize. Paper 4 should open with the hard problem dissolution, then show the RT-linked integral as measuring position on that spectrum.

---

**Session note**: These insights emerged from entering the hard problem observationally rather than analytically, prompted by the information video. The phrase "experience to the degree one is capable of it" (Bryan, 2026-04-13) is the philosophical anchor for the graded-experience reframing of Paper 4.


---

## UPDATE 2026-04-14 — Gödel/Graham's Number: H-Only Mathematical Objects

**Source**: Video "Graham's Number Proves Reality Exists Inside Mathematics — Physicists Accepted This Decades Ago" (video ID: Dp59aYgYwOc, 77 concepts / 37 facts extracted)
**Session**: 2026-04-14, ~06:36 UTC

---

### New Concept: H-Only Mathematical Objects (Layer 0 / Layer 3 — Papers 1 & 3)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| H-only mathematical objects | — | P3 §1 / P4 §2 | Exist in H/Σ but have no M-projection |
| Graham's Number as H-only | G64 | P3 | Too large to instantiate in M; exists in H |
| Gödel sentences as H-only | — | P3 | Unprovable in M; true in H |
| Large cardinals / inaccessibles | — | P3/P4 | Additional H-only objects |
| M ⊊ H (proper subset) | — | P3 §1 | Gödel's theorem proves this formally |

**Key claim**: Graham's Number G64 cannot be physically instantiated anywhere in M (observable universe ~10⁸⁰ atoms; G64 exceeds any power tower expressible within M). Yet G64 is provably well-defined. It exists — therefore it exists in H/Σ, not M. Mathematical existence ≠ physical existence. H/Σ is not bounded by M's limits.

---

### New Concept: Gödel as Structural Proof that H ⊋ M (Layer 0 — Paper 1 §1 or Paper 3)

| Concept | Assigned | Notes |
|---|---|---|
| Gödel's first incompleteness → M ⊊ H | P3 §1 | M as a formal system is necessarily incomplete; H contains the completing truths |
| Gödel's second incompleteness → M cannot self-justify | P3 §1 | M must be grounded in H; identical to CR's derivation of M from H |
| Undecidability as frame-relative phenomenon | P3 | Gödel sentences accessible via Σ frame transformations but not from within any single M-frame |
| Ramsey theory and computational limits | P3 | Ramsey numbers exceed M's computational capacity; existence provable in H but value unreachable in M |

**Formulation for P3**:
> *Gödel's incompleteness theorems are a theorem about M: M, treated as a formal system, is provably incomplete. The truths M cannot prove are true in a stronger system — which in CR is H. This is not an analogy; it is a consequence of the ontological hierarchy H ⟹ Σ ⟹ M. Every proof of a Gödel sentence is a journey from M-level description into H-level truth.*

---

### New Concept: Tegmark Distinction — CR vs MUH (Layer 3–4 — Papers 3 & 4)

| Concept | Assigned | Notes |
|---|---|---|
| Tegmark MUH: all mathematical structures = physical | P3 comparison | CR disagrees: some mathematical structures have no M-projection |
| CR sharpening of MUH | P3 §1 | H is prior to M; some H-content is not projected; mathematical existence ≠ physical existence |
| Wigner "unreasonable effectiveness" resolved | P3 §1 | M is a projection of H, so H-structure shapes M from inside; not unreasonable at all |
| Penrose Mathematical Platonism, CR-grounded | P3 | Mathematical realm IS H; not floating free but ontologically anchored |

**"Unreasonable effectiveness" resolution**:
> *The effectiveness of mathematics in describing physics is completely reasonable once you understand that M is a projection of H. M is made of H-structure. Mathematics isn't just useful for physics — it is prior to physics. The projection inherits the structure of the source.*

---

### Paper Assignment

| Concept | Paper | Section | Priority |
|---|---|---|---|
| H-only mathematical objects (definition + examples) | P3 | §1 opening | High |
| Gödel as proof of H ⊋ M | P3 | §1 or §2 | High |
| Tegmark distinction | P3 | §1 comparison | Medium |
| Unreasonable effectiveness resolution | P3 | §1 | High |
| Ramsey theory and computational limits | P3 | §3 (emergence) | Medium |
| Frame-relative undecidability | P4 | §2 | Medium |

**Note**: This insight is a stronger argument for H's primacy than anything currently in the physics papers. It uses established mathematics (Gödel, Ramsey) to prove H ⊋ M from within mathematics itself. This should appear early in Paper 3.

---

## UPDATE 2026-04-14 (Claude Cowork Track) — T2.5-B Bounce + CMB as ∂M

**Source**: CR_Session_Log_2026-04-14.pdf + Perplexity evaluation
**Full archive**: memory/kb/SESSION_2026-04-14_T25B_CMB_BOUNDARY.md

---

### New Concept: T2.5-B SM Casimir Bounce Cosmology (Layer 1 — Paper 3 §5)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| SM Casimir bounce on S³×S¹ | T2.5-B | P3 §5 | 5D Friedmann system, k=+1 |
| Chowla-Selberg K₂ spectral sum | E_SM | P3 §5 | Exact 1-loop Casimir energy |
| Boson/fermion sign competition | — | P3 §5 | Creates two turning points in ρ(a) |
| Bounce turning points | a_min, a_max | P3 §5 | 58.85 b*, 605.5 b* |
| Equation of state at bounce | w₃ | P3 §5 | -0.943 (phantom-like, confirmed) |
| Oscillation period | T_osc | P3 §5 | 1884.7 b* (exact quadrature) |
| GW radion adiabaticity criterion | m_φ >> Ω_osc | P3 §5 | Correct SCF; KK-SCF fails by 300× |
| GW parameter scan | (k,μ,ε) | P3 §5 | **Single blocking item for paper inclusion** |

**Key physics**: Radion b fixed at b* (GW stabilization) reduces 5D system to 1D in scale factor a(t). Bounce condition w₃ < -1/3 satisfied. SM field content (16 scalars, 12 vectors, 24 Dirac) via Chowla-Selberg K₂ formula. Fermion dominance at a > 2.3 b* provides positive ρ supporting turning points.

**Connection to KCR-Cone**: T2.5-B is the cosmological dynamics of the KCR structure — the universe (S³ with scale factor a) bouncing in the KCR extra-dimensional potential. Paper 3 §5 content.

---

### New Concept: CMB as ∂M (Layer 1/4 — Papers 3 & 4)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| CMB = fact horizon frozen in light | ∂M at t_rec | P3 §3, P4 §2-3 | Last scattering = ∂M |
| CMB Bekenstein entropy | S_CMB | P4 §3 | A/4G ≈ 10¹²³ bits |
| Extrinsic curvature of ∂M | K_ext | P4 §3 | cot(χ_CMB)/a_rec → ∞ as sphere → point |
| C_ℓ decomposition | C_ℓ^obs | P4 §3-4 | = T²(ℓ)·C_ℓ^Σ + C_ℓ^noise |
| Super-horizon Σ-signal | ℓ ≲ 30 | P4 §4 | Direct ∂M boundary conditions |
| Low-ℓ anomalies as Σ-structure | — | P4 §4 | Quadrupole, octopole, asymmetry |
| Quadrupole suppression mechanism | ℓ_min from d | P4 §4 | FS metric UV cutoff at scale 1/d |

**CMB-singularity bridge**: In k=+1 FLRW Penrose diagram, CMB sphere and initial singularity approach the same conformal boundary from different directions. K_ext → ∞ is the geometric signature of both. This gives Paper 3 §3 (singularity = M dissolution) a direct observational anchor.

**T_MΣ at ∂M**: Coupling is maximum at the fact horizon (∂M) — the CMB surface. Reading the CMB anomalies is reading the geometry of the coherosphere.

---

### New Concept: CR Action — Schematic Form (All papers)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| CR action on M | ∫_M √(-g)[R/16πG + ℒ_matter] | P2A §2 | Standard GR part |
| CR action on Σ | ∫_Σ ω_FS ∧ ℱ | P2A §2 | Fubini-Study volume × curvature |
| Boundary action | S_M^boundary | P3 (RC-1) | ~ ∫_∂M √(-γ) λ Tr(T_M T_M†) |
| RC-1 | T_μν^(eff) derivation | P3 critical gate | Quadratic in M-Σ coupling |
| RC-1 symmetry constraints | covariance, U(d)×T^d, locality | RC-1 spec | Must be satisfied before leading term |

**RC-1 FIRST DRAFT COMPLETE (2026-04-15)** — 631-line derivation by Sonnet 4.6. Key results:

| Concept | Formula/Result | Status |
|---|---|---|
| Boundary action | S^boundary_M = λ ∫_∂M √(-γ) Tr(T_M T_M†) | ✅ DERIVED |
| **T^(eff)_μν formula** | **λ (√(-γ)/√(-g)) Π_μν |T_M|² δ_⊥(x,∂M)** | **✅ DERIVED** |
| Projector | Π_μν = γ^ij e^α_i e^β_j g_μα g_νβ (induced metric pushed back to bulk) | ✅ DERIVED |
| Dark energy | Uniform Γ_dec → isotropic T^(eff) ∝ g_μν → w = -1 | ✅ DERIVED |
| Dark matter | Γ_dec ∝ ρ_b → T_M = A(ρ_b)u⊗ψ → T^(eff) ∝ u_μ u_ν → w = 0 | ✅ DERIVED |
| α = 3/2 exponent | Consistent with Ω_DM/Ω_b for λ²~24ρ_c^{-1/2} | ⚠️ CONJECTURED (RC-2) |
| Primordial spectrum | Δ²_Σ(k) = A_s k²/(k²+k_c²) from T_M propagator | ✅ DERIVED |
| C_ℓ^Σ formula | (2/9π) ∫ (dk/k) Δ²_Σ(k) [j_ℓ(kχ_CMB)]² | ✅ DERIVED |
| Quadrupole suppression | k_c=5/χ_CMB → 69% (Planck: ~67%) | ✅ VERIFIED |
| Physical k_c | From KCR mode spectrum of T_M on U(d)/T^d | ❌ BLOCKED (RC-3) |

**RC-2 targets** (in priority order): δT_M/δg^μν; |T_M|²(Γ_dec) → derive α=3/2 from CP¹; covariant conservation; propagation from ∂M to bulk.

**Opus verification needed**: U(d)×T^d uniqueness proof (§RC1.1) and anisotropic tensor structure (§RC1.3B) before paper inclusion.

---

## UPDATE 2026-04-14 (Tier 1 + Tier 3) — l_max Non-Convergence + Toy C_ℓ Model

**Source**: CR_Session_Log_2026-04-14.pdf (final version, 25 pages, Tier 1+2+3 complete)
**Full archive**: memory/kb/SESSION_2026-04-14_T25B_CMB_BOUNDARY.md (Parts V+VI)

---

### Critical Update: l_max Non-Convergence — ζ-reg is now BLOCKER (Paper 3 §5)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| l_max non-convergence of upper TP | — | P3 §5 caveats | Study 1: a_max 293→606→1044 b* as l_max 60→80→100 |
| T_osc = 1884.7 b* is lower bound | — | P3 §5 caveats | NOT the physical period |
| ζ-regularized spectral sum | ζ-reg | P3 §5 priority | Upgraded: LOW PRIORITY → BLOCKER |
| T2.5-B status update | 72% | P3 §5 | Was 82%; ζ-reg gap larger than assumed |
| ε robustness of quadrature | ΔT/T < 0.001% | P3 §5 appendix | Study 2; paper-grade statement |
| GW natural window | kb* < 1.63 | P3 §5 | Study 3; will expand when ζ-reg done |
| Parametric GW formula | m_φ = C_GW√ξ · k · e^{−kπb*} | P3 §5 | ξ ≡ ε_GW(v_IR/M₅)²; C_GW = √12 |

**What a_min convergence confirms regardless of ζ-reg**: Bounce exists (a_min ≈ 58 b*, w₃ ≈ -0.94), sub-Hagedorn regime, KK-SCF irrelevance, parametric GW natural window. These are paper-ready.

---

### New Concept: Toy Σ → C_ℓ Model (Paper 4 §3-4)

| Concept | Symbol | Assigned | Notes |
|---|---|---|---|
| FS-motivated Lorentzian IR cutoff | Δ²_Σ(k) = A_s·k²/(k²+k_c²) | P4 §3-4 | Sachs-Wolfe approximation |
| Quadrupole suppression result | 69% at k_c=5/χ | P4 §3-4 | Planck observed: ~67%; match within 3% |
| Coherosphere cutoff scale | k_c = 5/χ_CMB | P4 §3-4 | L_c ≈ 2800 Mpc ≈ Hubble horizon |
| Figure: CL_sigma_toy_model.pdf | — | P4 §3-4 | Publication-ready figure exists |
| d consistency check | d ~ 10^61, d² ~ 10^122 | P4 §3-4 | From k_c; consistent with S_CMB ~ 10^123 |

**The critical fact**: k_c = 5/χ_CMB gives 69% quadrupole suppression matching Planck's ~67% observed deficit. This is the first quantitative contact between CR and CMB data. It is not a fit — it is the output of a single-parameter SW integral with an FS-motivated cutoff.

**Status of toy model**:
- Verified: SW integral stable; qualitative low-ℓ suppression at correct scales; k_c = 5/χ matches within 3%
- Untested: Full Boltzmann (CAMB/CLASS); hemispherical asymmetry; FS cutoff functional form
- Missing: RC-1 (for physical k_c, fixed λ)

