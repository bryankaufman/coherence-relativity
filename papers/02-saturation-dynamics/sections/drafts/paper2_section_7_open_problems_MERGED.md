# §7 Open Problems

**Status:** DRAFT — Wave 6 (merged: Cowork + Warp) + additions 2026-03-23
**Model:** Sonnet-level (structured catalog)
**Cross-references:** All preceding sections; [Paper 2B]; Paper 3 (future)

---

The framework developed in this paper raises several open questions that fall outside its scope. We organize these in four tiers: questions addressed in the companion paper, questions requiring new theoretical work, questions requiring experimental input, and internal consistency questions within this paper's formalism.

---

## §7.1 Questions Addressed in the Companion Paper [Paper 2B]

The following are well-posed questions whose answers require evaluating the framework on a specific geometry. The companion paper addresses them for the KK-Cone.

**OP-1. Norm convention resolution.** The Markov ratio $R_{\text{Markov}}$ (§2.3, Eq. 2.3.3) involves a Frobenius norm of the cross-term block $G^{(\text{cross})}$. At the abstract level, the norm convention — covariant, contravariant, or mixed — is a free choice that does not affect the qualitative criterion ($R_{\text{Markov}} < \epsilon$ iff the system is effectively classical). However, the *numerical value* of $R_{\text{Markov}}$ at finite $\lambda$ depends on this choice. The companion paper resolves this ambiguity for the KK-Cone geometry (Appendix A), establishing the asymmetric convention (contravariant for diagonal blocks, covariant for the cross-term) as the geometrically consistent choice. Whether a canonical convention exists at the framework level is an open question.

**OP-2. The coupling identification $\lambda = f(\text{warp factor})$.** The warp-factor hypothesis $\lambda \sim A^2$ (§2.2, Eq. 2.2.41) is derived from dimensional analysis and physical intuition. Its verification requires solving the boundary conditions of a specific geometry. The companion paper confirms $\lambda = A^2$ for the KK-Cone and derives the physical consequences (classical entry in the throat, frame-lag cancellation). Whether this identification generalizes to other geometries is unknown.

**OP-3. Self-consistency of the KK-Cone.** Three self-consistency conditions (spatial flatness, gravity localization, cosmological constant) must be checked on the first geometry from derived compactification. Two close; the third has a candidate Casimir mechanism [Paper 2B, §4.1–4.3].

**OP-4. Holographic verification.** Conjecture 5.1 (§5) is a structural conjecture about the $M \times \Sigma$ geometry. Testing it requires Ryu-Takayanagi surfaces, entanglement entropy calculations, and beta-function matching — all of which require a metric. The companion paper provides the first such test on the KK-Cone: monotonic geometric-entropic link confirmed, but proportionality refuted (sublinear power-law fit). Whether the sublinear power law is a feature of the KK-Cone or a generic prediction of coherence holography is unknown.

**OP-5. Fiber radius stabilization.** Derived compactification (§3.2) establishes that the fiber topology is $S^1$, but the fiber radius $R$ is not fixed by topology alone. Stabilization requires a dynamical mechanism. The companion paper investigates Casimir stabilization on the Hopf fiber, finding a characteristic radius $r_f^* \approx 21.8\,\mu\text{m}$ from the balance of Casimir energy and bulk curvature. Whether this value survives a full quantum treatment — and whether it can reproduce the observed cosmological constant — connects radius stabilization to the cosmological constant problem in a specific, testable way.

**OP-6. Explicit trajectory solutions.** The abstract equations of motion (§4, Eqs. 4.1.8–4.1.9) are well-posed but require a metric for numerical evaluation. The companion paper solves these equations on the KK-Cone and extracts decoherence timescales, trajectory deviations, and effective potentials.

---

## §7.2 Questions for Paper 3 and Beyond

These problems go beyond the scope of the companion paper and require new derivations or formalisms.

**OP-7. First-principles derivation of $\lambda$.** The distinguishability parameter $\lambda$ is introduced phenomenologically in §2.2. A first-principles derivation — relating $\lambda$ to a decoherence-rate functional or information-theoretic quantity — would strengthen the formalism. One candidate: $\lambda$ as the ratio of the coherence-frame adaptation timescale to the environmental decoherence timescale. A rigorous formula requires a microscopic model of the system-environment interaction.

**OP-8. Higher Chern numbers.** The derived compactification of §3.2 produces a family of geometries indexed by $c_1 \in \mathbb{Z}$. This paper evaluates only $|c_1| = 1$ (the Hopf fibration). The $|c_1| > 1$ cases correspond to lens spaces $S^3 / \mathbb{Z}_{c_1}$ and have different Kaluza-Klein spectra, different moduli constraints, and potentially different phenomenology. Whether nature realizes higher-$c_1$ bundles — and what physics they would produce — is an open question.

**OP-9. Non-abelian fiber structures.** The coherence frame for a qubit is $S^2$ with $U(1)$ fiber. For larger quantum systems (qutrits, multi-qubit systems), the coherence manifold may be $\mathbb{CP}^n$ with non-abelian fiber structure. Extending derived compactification to these cases could produce higher-dimensional compact fibers with non-abelian gauge content. The resulting compactification topology and gauge structure would be qualitatively different.

**OP-10. The coherence RG.** The holographic conjecture (§5) introduces a coherence RG — a flow along $\Sigma$ parameterized by $\lambda$. Several questions are open: Does the coherence RG satisfy a $c$-theorem (monotonic decrease of a central charge)? Is the coherence RG related to Wilsonian RG by a specific map? Can the coherence beta function (Dictionary Entry 3, Eq. 5.1.4) be computed from first principles?

**OP-11. Gravitational coupling.** Paper 1 noted the conceptual parallel between the coherence-frame metric and proposals where spacetime emerges from entanglement (Van Raamsdonk 2010, Swingle 2012). The identification of the spacetime metric $g_{\mu\nu}$ with a projection of the coherence-frame tensor $T_{AB}$ onto $M$ remains speculative. Paper 3 aims to make this connection rigorous.

**OP-12. Quantization of the $M \times \Sigma$ system.** The formalism of this paper is classical in the sense that $(x^\mu, \xi^a)$ are treated as classical coordinates on a manifold. Quantizing these degrees of freedom — via canonical quantization, path integrals, or geometric quantization using the Fubini-Study structure — is an open program. The relationship between the classical frame-lag dynamics (§4) and quantum corrections is unexplored.

**OP-13. Multi-sector extensions.** The formalism of §2.1–§2.2 treats $M \times \Sigma$ as a two-sector decomposition. Physical systems may require additional sectors (e.g., an environmental sector $E$, or multiple coherence frames for composite systems). Extending the formalism to $M \times \Sigma_1 \times \Sigma_2 \times \ldots$ is straightforward in principle but may introduce new cross-term structures and coupling patterns.

---

## §7.3 Experimental Questions

**OP-14. Frame-lag signatures.** The frame-lag mechanism (§4, Eq. 4.1.10) predicts that spacetime acceleration sources coherence-frame response. In principle, this produces measurable deviations from standard decoherence rates in accelerated systems — for example, in atom interferometry experiments in varying gravitational fields, or in quantum systems near black hole horizons. Computing these deviations requires the coupling identification $\lambda = f(\text{geometry})$ and the explicit cross-term scaling — both geometry-dependent. The companion paper provides the first estimates for the KK-Cone.

**OP-15. KK mode detection.** The KK spectrum from the derived Hopf fiber (§3.3, Eq. 3.3.5) predicts a tower of massive excitations with masses $m_n = n/R$. If the fiber radius $R$ is stabilized at $r_f^* \approx 21.8\,\mu\text{m}$ (as suggested by Casimir analysis in [Paper 2B]), the lightest KK mode has mass $m_1 \sim \hbar c / R \sim 10^{-2}\,\text{eV}$. This is within the range probed by short-range gravity experiments and fifth-force searches.

**OP-16. Geometric dark matter.** The companion paper develops a scenario in which KK excitations of the coherence field produce gravitational effects consistent with dark-matter observations (rotation curves, Bullet Cluster). Whether this scenario can reproduce the full dark-matter phenomenology — including large-scale structure formation, CMB power spectrum, and baryon acoustic oscillations — requires numerical simulations beyond the scope of either paper.

**OP-17. Cosmological constant.** The framework predicts $\Lambda(R)$ as a function of the fiber radius (§3.3.5). Whether the observed value $\Lambda_{\text{obs}} \sim 10^{-122} M_P^4$ can be reproduced depends on the stabilized radius — which in turn depends on the stabilization mechanism (OP-5). This connects the cosmological constant problem to radius stabilization in a specific, testable way.

---

## §7.4 Internal Consistency Questions

These are questions about the internal mathematical consistency of the formalism developed in this paper. They do not require new geometry or experimental input — they require careful analysis of the existing framework.

**OP-18. The left-right generator program.** §2.5 introduces the distinction between Schrödinger-side and Heisenberg-side generators on $M \times \Sigma$. For the dephasing model, $\mathcal{R}_t = \mathcal{L}_t$ exactly (Markovian, one metric face). The open question is the non-Markovian extension: derive $T_{M\Sigma}^{(\text{H})}$ for a two-level system with amplitude damping plus dephasing, confirm $\|\mathcal{L}_t - \mathcal{R}_t\|_{\text{op}} \to 0$ in Phase III, and give a full proof of Theorem 2.5.1 (pointer states as the zero set of $\mathrm{Im}(H_{M\Sigma})$).

**OP-19. §2.2 hypotheses verification for general geometries.** The $\delta\lambda$ formalism (§2.2) has several untested hypotheses: the warp-factor scaling $\lambda \sim A^2$ (Eq. 2.2.41), the cross-term scaling $T_{\mu a}^{\text{FS}} \sim A^{-2}$ (Eq. 2.2.38), and the $O(\lambda^2)$ corrections to the inverse metric (§2.2.3). These are verified for the KK-Cone in the companion paper but remain unverified for general geometries.

**OP-20. Frame-lag and decoherence timescales.** The frame-lag mechanism (§4, Eq. 4.1.10) provides a geometric account of coherence response to spacetime acceleration. The lag timescale — the time for the Σ-sector to respond to M-sector perturbations — is a physical observable in principle. The general question remains: is the frame-lag timescale related to standard decoherence timescales (e.g., $\tau_D \sim \hbar / k_B T$)? If so, the framework would make a connection to thermodynamics.

**OP-21. The $\ell^* = S(\ell^*) / S_{\max}$ entropic prediction.** The Casimir analysis yields $r_f^* \approx 21.8\,\mu\text{m}$ as the stabilized fiber radius. The currency-of-the-realm framework (see companion conceptual development) predicts that $\ell^*$ should mark the entropic watershed — the scale at which exactly half the universe's total entropic budget has been expended: $S(\ell^*) = S_{\max}/2$. The Hopf fiber density argument (§4.5.6) provides independent geometric grounding: $n_{\text{fiber}} = 1/4$ exactly at $r = \ell^*$, corresponding to the $25\%$ base coverage that anchors the entropy-midpoint identification. Verifying this numerically — computing $S_{\max}$ for the observable universe and checking the ratio — would provide a second, independent derivation of $\ell^*$ from completely different physical reasoning. Agreement between the Casimir geometric result and the entropic prediction would be strong evidence that $\ell^*$ is physically real.

**OP-22. Decoherence Recapitulates Cosmogenesis: formal derivation.** Every quantum decoherence event enacts the same three-phase sequence the universe traversed cosmologically (Phase I $\to$ II $\to$ III). The suppression parameters governing both are structurally identical: $e^{-\lambda_M} \sim (\ell^*/R)^2$. This scale covariance of the phase transition equation is stated throughout the paper but not formally derived. A rigorous derivation would: (1) establish the explicit proportionality constant relating $e^{-\lambda_M}$ to $(\ell^*/R)^2$; (2) identify the Born rule as the conserved quantity across both the cosmic and the local phase transition; and (3) show that thermodynamic irreversibility and cosmological expansion are the same asymmetry at different scales. This derivation would provide the bridge from Paper 2 §9 Discussion into Paper 3 §1 Introduction.

**OP-23. Settimo et al. (2026) citations and picture-inequivalence contributions.** Settimo et al. (2026) \cite{Settimo2026} establish that Schrödinger and Heisenberg divisibility are inequivalent for non-Markovian dynamics ($\mathcal{L}_t \neq \mathcal{R}_t$). This paper cites this result in §2.5. The outstanding bibliographic and technical tasks are: (1) add the Settimo citation to the Paper 2 bibliography and cross-reference it in §2.5, §7 (EOM), and §9 (Discussion); (2) determine whether $\|\mathcal{L}_t - \mathcal{R}_t\|_{\text{op}}$ makes a quantitative contribution to the $H_0$ tension channel analyzed in Paper 3 §5; (3) verify that the Born rule as $|H|$-invariant (§2.5.5) is consistent with the Settimo dual-picture structure. Citation: F. Settimo et al., \textit{PRX Quantum} \textbf{7}, 010340 (2026). DOI: 10.1103/6dt2-sq44.

---

## §7.5 Summary

| Problem | Scope | Priority |
|---------|-------|----------|
| OP-1 Norm conventions | Paper 2B | Addressed |
| OP-2 Coupling identification | Paper 2B | Addressed |
| OP-3 Self-consistency | Paper 2B | Addressed |
| OP-4 Holographic verification | Paper 2B | Addressed |
| OP-5 Radius stabilization | Paper 2B | **Critical** |
| OP-6 Explicit trajectories | Paper 2B | Addressed |
| OP-7 First-principles $\lambda$ | Paper 3 | High |
| OP-8 Higher Chern classes | Paper 3+ | High |
| OP-9 Non-abelian fibers | Paper 3+ | High |
| OP-10 Coherence RG | Paper 3+ | Medium |
| OP-11 Gravitational coupling | Paper 3 | High |
| OP-12 Quantization | Paper 3+ | Medium |
| OP-13 Multi-sector | Paper 3+ | Medium |
| OP-14 Frame-lag signatures | Experimental | Long-term |
| OP-15 KK mode detection | Experimental | Near-term |
| OP-16 Dark matter | Paper 2B + data | Near-term |
| OP-17 Cosmological constant | Paper 3 + data | High |
| OP-18 Left-right generators (non-Markovian) | Internal | Immediate |
| OP-19 §2.2 hypotheses | Internal | High |
| OP-20 Frame-lag timescales | Internal | Medium |
| OP-21 $\ell^* = S_{\max}/2$ entropic prediction | Internal + numerical | High |
| OP-22 Decoherence Recapitulates Cosmogenesis | Internal + Paper 3 bridge | High |
| OP-23 Settimo citation + picture-inequivalence | Internal (bibliography) | Immediate |

The most critical open problem is **radius stabilization (OP-5)**: without it, the derived-topology program produces a topological structure but not a unique geometry. The most immediate internal tasks are **OP-18** (left-right generator completion), **OP-22** (scale covariance derivation, which bridges to Paper 3), and **OP-23** (Settimo citation). The most testable prediction is **OP-21**: computing $S(\ell^*)$ numerically is a bounded calculation that could either confirm or falsify the entropic watershed interpretation of $\ell^*$.

---

## References (within Paper 2)

- §2.2: $\delta\lambda$ formalism
- §2.3, Eq. 2.3.3: Markov ratio
- §2.5: Left-right generator decomposition
- §3.2: Derived compactification (Hopf fibration, $c_1$ family)
- §3.3.5: Cosmological constant constraint
- §4, Eq. 4.1.10: Frame-lag mechanism
- §4.2: Evaluation limitations
- §4.5.6: Hopf fiber density at $r = \ell^*$
- §5, Conjecture 5.1: Holographic structure
- [Paper 2B]: Companion paper (KK-Cone evaluation)
- Settimo et al. (2026), PRX Quantum 7, 010340. DOI: 10.1103/6dt2-sq44

---

## Revision History

| Date | Change |
|------|--------|
| 2026-03-10 | Initial drafts — Wave 6 (Cowork + Warp independently) |
| 2026-03-10 | Merged version — 4-tier structure from Warp; internal consistency tier (OP-18, OP-19, OP-20) from Warp; expanded problem descriptions from both; priority table from Cowork |
| 2026-03-23 | Added OP-21 ($\ell^* = S_{\max}/2$ entropic prediction), OP-22 (Decoherence Recapitulates Cosmogenesis formal derivation), OP-23 (Settimo citation + picture-inequivalence contributions) |
