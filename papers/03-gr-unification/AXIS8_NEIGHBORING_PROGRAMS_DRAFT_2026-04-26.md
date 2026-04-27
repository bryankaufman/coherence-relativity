# Axis 8: Neighboring Programs — Emergent Spacetime, Pre-Geometry, and NCG
**Draft for**: Paper 3 §2 extension (canonical home); back-pointer from Paper 2C §9.6
**Accuracy basis**: Claude's 2026-04-26 review of Perplexity's Axis 8 materials
**Vocabulary**: HCR canonical — T_{MΣ}, T^(eff)_μν, λ(x,ξ), R_Markov, 𝒫_holo
**Status**: Draft — needs citation verification before manuscript inclusion

---

## §2.X Neighboring Programs and the Position of HCR

*[This section extends the §2 "Σ as Dual Source of Q and Spacetime" seed paragraph. The seed paragraph establishes that Σ simultaneously generates the pilot-wave potential Q via Born-Oppenheimer projection (the Born-rule side) and an AdS-like emergent bulk metric via FS/Bures flow (the holographic side). The present section locates this dual role within the landscape of programs that derive spacetime from quantum structure, and states precisely where HCR departs from each.]*

---

### 8.1 Van Raamsdonk — Entanglement and Geometric Connectivity

**Program.** Van Raamsdonk (2010) \cite{VanRaamsdonk:2010pw} uses AdS/CFT to argue that classically connected bulk regions correspond to entangled boundary regions, and that disentangling degrees of freedom causes the bulk geometry to pinch off. The controlling object is the entanglement pattern of the boundary state; geometry on M is a functional of that pattern.

**Interface with HCR.** In HCR, the effective stress tensor T^(eff)_μν on ∂M is a functional of T_{MΣ} and λ (RC-1, Paper 2C §3), and the bulk geometry follows from Einstein's equations with T^(eff)_μν as the source. Van Raamsdonk's entanglement–connectivity correspondence is recovered as a special case: when T_{MΣ} → 0 (decoupled sectors), T^(eff)_μν → 0 and M loses its induced geometry from the ∂M boundary; when T_{MΣ} ≠ 0 (coherence coupled to geometry), the boundary stress tensor is non-zero and M acquires geometric structure.

**Departure.** Van Raamsdonk works within the AdS/CFT setting and requires a presupposed CFT on the boundary. HCR's boundary is ∂M — the fact horizon (Paper 3 §3) — identified with the CMB last-scattering surface at t_rec, not an asymptotic conformal boundary. The mechanism is not entanglement renormalization but boundary action variation (RC-1), which works without a CFT and with a positive cosmological constant.

---

### 8.2 Cao–Carroll–Michalakis — Space from Hilbert Space

**Program.** Cao, Carroll, and Michalakis (2017) \cite{Cao:2016mst} start with an abstract Hilbert space equipped with a tensor factorization and a class of "redundancy-constrained" states. They define a graph metric from entanglement (mutual information) and use multidimensional scaling to reconstruct an approximate spatial manifold. Small entanglement perturbations change the emergent spatial curvature in a way consistent with linearized Einstein's equations.

*[Note: the authors are Cao, Carroll, and Michalakis — not "Cao–Carroll–Singh." Singh is not an author on this paper; that is a name error in some secondary sources. The Cao–Carroll–Lloyd (2020) quantum mereology paper is a separate but related reference.]*

**Interface with HCR.** This is the closest direct competitor to the reconstruction map 𝓕: (ℋ, entanglement pattern) → (M, g_μν). Their multidimensional scaling construction extracts spatial geometry from mutual information in a way that HCR's 𝒫_holo should subsume: the FS/Bures flow on Σ generates the same AdS-like entanglement-wedge bulk metric that Cao et al. recover by multidimensional scaling, in the appropriate regime. HCR adds: (1) the coherence manifold Σ and pointer structure, absent in Cao et al.; (2) T_{MΣ} as the geometric mediator between coherence and stress-energy; (3) the fact-horizon ontology (H ⊋ M, M = accumulated quantum-Darwinian records) as an ontological completion of their reconstruction procedure.

**Departure.** Cao et al. produce a spatial manifold; they do not derive a dynamics (Einstein's equations) from first principles, and their construction requires a specific tensor factorization and class of states as inputs. HCR derives T^(eff)_μν from a symmetry-constrained boundary action (RC-1) and places the reconstruction map in a principled ontological hierarchy. Whether HCR's 𝒫_holo can recover the Cao–Carroll–Michalakis MDS construction in a finite-d limit is an open research question.

---

### 8.3 Swingle — MERA and Holographic Spacetimes

**Program.** Swingle (2012) \cite{Swingle:2009bg} argues that the MERA tensor network provides a discrete holographic geometry whose entanglement-renormalization structure encodes the bulk. In the large-N limit, the network approximates a smooth AdS-like spacetime; sparse operator spectra and mutual-information phase transitions match AdS/CFT structure.

**Interface with HCR.** Swingle's MERA provides a discrete pre-geometric skeleton that can be interpreted as a specific realization of 𝒫_holo on a lattice. The HCR continuum picture — T_{MΣ} as the smooth bundle-connection limit of the entanglement structure, with λ(x,ξ) controlling classicalization — can be viewed as the continuum counterpart. Whether this identification can be made precise — whether T_{MΣ} and the FS connection A_C reduce to a MERA-like network in a finite-d discretization — is an open research direction, not an established result.

**Departure.** MERA applies in the AdS setting; HCR works with a positive cosmological constant and a non-conformal boundary. The MERA renormalization group is Wilsonian (integrating out high-energy modes); HCR's coherence RG on Σ parameterizes coherence loss, not energy scale, and is conceptually distinct.

---

### 8.4 Connes — Noncommutative Geometry and Spectral Triples

**Program.** Connes' noncommutative geometry \cite{Connes:1994yd} encodes a manifold and its physical content in a spectral triple (𝒜, ℋ, D) — an algebra, Hilbert space, and Dirac operator. For the Standard Model, the almost-commutative geometry takes the form M × F, where F is a finite internal space whose spectral data reproduce the gauge structure.

**Interface with HCR.** HCR's M × Σ has structural overlap with M × F: both supplement spacetime with an internal geometric object carrying algebraic and metric data. In HCR, Σ = U(d)/T^d carries the Berry/Hopf structure and the FS metric; T_{MΣ} is the cross-term encoding how internal (coherence) and external (spacetime) structures couple. The pointer-sector criterion (Theorem 2.5.1: Im(H_MΣ) = 0 iff pointer sector) is the HCR analog of the fermion mass matrix constraint in Connes' NCG.

**Departure.** Σ is not an arbitrary internal finite space. It is *constructed* from coherence frames and pointer sectors (Paper 1 Definition 1), not postulated. T_{MΣ} is not a Dirac operator but a cross-term coupling tensor derived from the Fubini-Study pullback (Paper 2A §2.1) and constrained by the RC-1 boundary action symmetries. These differences are structural: NCG's internal geometry is geometrically arbitrary (the algebra 𝒜 is a free input); HCR's Σ is derived from the quantum-mechanical axioms.

*[Caveat: Spectral triples do not always factor as M × F. The almost-commutative form is specific to the SM; generic spectral triples are richer. The comparison above is to the SM spectral triple only.]*

---

### 8.5 Causal Sets, CDT, and Quantum Graphity

**Program.** Causal set theory (Dowker 2020 \cite{Dowker:2020qde}) treats a locally finite partial order as the fundamental structure, with continuum spacetime as emergent. Causal dynamical triangulation and quantum graphity similarly derive M from a combinatorial pre-geometric structure.

**Interface with HCR.** These programs address the same general problem — derive M from a non-spatial primitive — but use causal or combinatorial data rather than coherence-geometric data. HCR's reconstruction map 𝓕 (ontological route via H ⊋ M, M = accumulated quantum-Darwinian records) is orthogonal to these constructive approaches.

**Departure and gap.** How T_{MΣ} would be defined on a causal set is not yet addressed. Conversely, causal set theory provides no coherence mediator. These are complementary, not competing, programs at the current stage.

---

### 8.6 ER=EPR and the Entanglement-Wormhole Correspondence

**Program.** Maldacena and Susskind (2013) \cite{Maldacena:2013xja} proposed that entangled particle pairs (EPR) are geometrically connected by Einstein-Rosen bridges (wormholes) in the bulk, making entanglement and geometric connectivity two descriptions of the same structure.

*[Note: The canonical ER=EPR reference is arXiv:1306.0533, Fortsch. Phys. 61, 781 (2013). This is distinct from arXiv:1401.3416, which is a 3D TQFT model by Hernandez-Cuadros et al.]*

**Interface with HCR.** Paper 4 develops the ER=EPR correspondence within the HCR framework: entanglement on Σ defines geometric connectivity in M, with T_{MΣ} mediating the correspondence. The separable submanifold S_sep ⊂ Σ (no EPR correlations) maps via 𝒫_holo to disconnected bulk regions; the Bell orbit (EPR locus) maps to geometrically connected regions with ER-type structure.

---

## Four Missing Neighborhoods (to add to literature scan)

The eight axes above are the correct high-level decomposition, but four areas are not yet on the spine and are directly relevant to open gates:

### N1: Generalized Contextuality (Spekkens 2005)

**Ref:** R. W. Spekkens, "Contextuality for preparations, transformations, and unsharp measurements," Phys. Rev. A 71, 052108 (2005); Liang–Spekkens–Wiseman (2011) for the operational framework.

**Relevance.** The SCF → COV → frame-noncontextuality → Born chain (DERIVATION_BORN_CHAIN_SYNTHESIS) lives within the Spekkens operational contextuality landscape. Theorem 6.1 (SCF + COV ⇒ frame noncontextuality) needs to be positioned relative to Spekkens' notion of noncontextuality for preparations and measurements. The DERIVATION_KCBS file is directly in this literature. This belongs on Axis 1 (Born reconstructions), not Axis 8, but is missing from the spine entirely.

**Action:** Check whether the frame-noncontextuality result of Theorem 6.1 is strictly weaker than, equivalent to, or stronger than Spekkens' preparation-noncontextuality. State the comparison explicitly before Theorem 6.1 appears in manuscript.

### N2: Non-Abelian Berry Holonomy / Wilczek–Zee Modern Literature

**Ref:** Wilczek & Zee (1984), PRL 52, 2111. Modern literature: Pachos & Chountasis (1999); Zanardi & Rasetti (1999); recent topological quantum computing literature.

**Relevance.** The Banach contraction argument (§6, DERIVATION_SCF_FIXED_POINT_SUBSTITUTION) assumes non-degenerate pointer bases. When eigenstates are degenerate, the Berry connection A_C becomes non-Abelian. The modern Wilczek–Zee literature (geometric phases under degenerate adiabatic evolution) is the natural framework for extending the Banach argument to the degenerate case. This closes the Wilczek–Zee refinement gap (OP-A4).

### N3: Stochastic Gravity / Einstein–Langevin (Hu–Verdaguer)

**Ref:** B. L. Hu and E. Verdaguer, *Semiclassical and Stochastic Gravity* (Cambridge, 2020); Living Reviews in Relativity review.

**Relevance.** RC-1 Assumption A1 treats T_M as a classical background field. The fluctuation side — where T_M's quantum fluctuations source noise correlators in g_μν — is exactly the Hu–Verdaguer Einstein–Langevin framework. When T^(eff)_μν is promoted to an operator and its fluctuations are retained, the back-reaction becomes stochastic. This connection is needed for the RC-1 result to connect to gravitational decoherence literature (Paper 1 Signature 4). Should appear in Paper 2C §8 "Discussion" as a future-direction paragraph, and in Paper 3 when cosmological fluctuations are discussed.

### N4: Constructor Theory (Deutsch–Marletto)

**Ref:** Deutsch & Marletto, "Constructor theory of information," Proc. R. Soc. A 471, 20140540 (2015); Marletto, "Constructor theory of life," J. R. Soc. Interface 12, 20141226 (2015).

**Relevance.** Constructor theory claims to be a more general framework than QM, treating information as a primitive and using the possible/impossible distinction as the fundamental ontological category. Their "substrate-independence" of information has structural overlap with HCR's H ⊋ M claim — HCR also treats quantum-information-level facts as prior to spacetime. The admissibility-band framing (λ-slice where R_Markov and the SCF equation are both satisfied) is analogous to the constructor-theory "possible" region. A short comparison in Paper 3 §9 "Relationship to Existing Programs" is warranted; the key departure is that constructor theory is axiomatic about information-as-primitive, while HCR derives information-primacy from H ⊋ M via Gödel + Bekenstein.

---

## Placement Recommendation

**Canonical home**: Paper 3 §2 (as an extension of the "Σ as Dual Source" seed paragraph).
**Back-pointer**: Paper 2C §9.6 "Relationship to Existing Programs" — one paragraph per axis, pointing to Paper 3 §2 for the full treatment.
**Axis 1 addition**: N1 (generalized contextuality / Spekkens) belongs in Axis 1, not Axis 8.
**Future directions**: N3 (Hu–Verdaguer stochastic gravity) as a future-direction paragraph in Paper 2C §8 Discussion and Paper 3 §5.
**Open item**: N2 (non-Abelian holonomy) and N4 (constructor theory) as Paper 3 §9 comparison paragraphs.

---

## Vocabulary Discipline Note

When using shorthand in sessions, the following translations apply:
- "T-flow on Σ" → the flow induced on Σ by the EOM for T_{MΣ} and λ
- "Basin measure" → the Φ-invariant measure of the flow induced by T_{MΣ}, evaluated on basins of attraction B_i under that flow. This is **not** automatically the FS measure; it agrees with FS pullback only under specific assumptions about the flow. Do not conflate.
- "Admissibility band" → the λ-slice where R_Markov < ε and the SCF fixed-point equation are both satisfied simultaneously.

---

*Draft: 2026-04-26. Accuracy basis: Claude review of Perplexity Axis 8 output, 2026-04-26.*
*Corrections applied: Cao–Carroll–Michalakis name (not Singh); ER=EPR canonical citation (1306.0533, not 1401.3416); basin-measure gloss (Φ-invariant, not FS by default); Swingle framing as research direction.*
*Four missing neighborhoods added: Spekkens contextuality, Wilczek–Zee modern, Hu–Verdaguer, Deutsch–Marletto.*
