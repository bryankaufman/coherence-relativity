# §7 (§10) Open Problems — v2

**Status:** v2 DRAFT — 2026-04-10.
**Supersedes:** `paper2_section_7_open_problems_MERGED.md` (2026-03-23)
**Changes from v1:** (1) OP-5 radius stabilization: RESOLVED. (2) OP-15 KK detection: updated to non-linear spectrum and interval geometry. (3) OP-17 cosmological constant: updated for geometric Λ primary source. (4) OP-24 added: Klein independence — RESOLVED. (5) OP-25 added: Weak values from T_{MΣ} cross-terms (TSVF connection). (6) OP-26 added: Three-box paradox from Berry phase non-commutativity. (7) Summary table updated.

---

The framework developed in this paper raises several open questions that fall outside its scope. We organize these in four tiers: questions addressed in the companion paper, questions requiring new theoretical work, questions requiring experimental input, and internal consistency questions within this paper's formalism.

---

## §7.1 Questions Addressed in the Companion Paper [Paper 2B]

**OP-1. Norm convention resolution.** The Markov ratio $R_{\text{Markov}}$ (§2.3) involves a Frobenius norm convention choice. The companion paper resolves this for the KCR-Cone geometry (Appendix A), establishing the asymmetric convention as geometrically consistent.

**OP-2. The coupling identification $\lambda = f(\text{warp factor})$.** The warp-factor hypothesis $\lambda \sim A^2$ is verified for the KCR-Cone in the companion paper. Generalization to other geometries is unknown.

**OP-3. Self-consistency of the KCR-Cone.** Three self-consistency conditions must be checked on the derived-compact geometry. SC1 (flatness) and SC2 (gravity localization) close in the companion paper. SC3 (cosmological constant): **resolved — see §5.3 v2** (geometric Λ from warp curvature, Casimir as correction).

**OP-4. Holographic verification.** Conjecture 5.1 is tested on the KCR-Cone in the companion paper: monotonic geometric-entropic link confirmed; proportionality refuted (sublinear power-law fit, §8.0 v2).

**OP-5. Fiber scale stabilization.**

**Status: RESOLVED (2026-04-10).**

The stabilization problem splits into two parts, both now resolved:

- **Shape (TOPOLOGICALLY FROZEN):** $r_{\max} = \pi/(2\sqrt{2})$ is fixed by the Fubini-Study eigenvalue $k^2 = 2$ — a topological invariant of $\Sigma = \mathbb{CP}^1$. The shape has zero moduli and cannot be continuously perturbed.

- **Scale (COSMOLOGICAL ATTRACTOR):** The physical scale factor $s$ (mapping dimensionless $r$ to meters) is determined by the Friedmann balance $H^2 = (8\pi G_4/3)[\rho_{\mathrm{geom}}(s) + \rho_{\mathrm{Cas}}(s)]$ at each epoch. The scale cannot decrease (non-traversability, Proposition 4.2) and increases at the Hubble rate. This is a cosmological attractor.

No Goldberger-Wise scalar, no KKLT potential, no new stabilization mechanism is required. Stabilization uses only: topology ($k^2 = 2$), classical geometry (warp curvature energy), cosmology (Friedmann balance), and thermodynamics (non-traversability).

The radion appearing in the KK spectrum (near-zero mode, $m^2 \approx 0.01$, 71% wavefunction overlap with breathing mode) is the manifestation of this stabilized breathing mode in the KK tower — not a new problem.

**OP-6. Explicit trajectory solutions.** The companion paper solves the abstract EOM on the KCR-Cone and extracts decoherence timescales, trajectory deviations, and effective potentials.

---

## §7.2 Questions for Paper 3 and Beyond

**OP-7. First-principles derivation of $\lambda$.** Unchanged from v1.

**OP-8. Higher Chern numbers.** The derived compactification gives a unique interval $r \in [0, r_{\max}]$ in the bulk. The Hopf fiber structure in $\Sigma$ admits $c_1 \in \mathbb{Z}$; higher-$c_1$ cases correspond to different gauge bundle structures, not higher-dimensional bulk spaces.

**OP-9. Non-abelian fiber structures.** Unchanged from v1.

**OP-10. The coherence RG.** Unchanged from v1.

**OP-11. Gravitational coupling.** Unchanged from v1.

**OP-12. Quantization of the $M \times \Sigma$ system.** Unchanged from v1.

**OP-13. Multi-sector extensions.** Unchanged from v1.

**OP-24. Klein Independence — Derived Compactification.**

**Status: RESOLVED (2026-04-09).**

When Klein's ad hoc $S^1$ compactification is replaced by the derived-compact interval $[0, r_{\max}]$ from $A(r) = \cos(\sqrt{2}\,r)$, five downstream calculations were reanalyzed:

| Calculation | Result |
|-------------|--------|
| ISL bounds | First genuine KK graviton at $\lambda = 13.3\,\mu\mathrm{m} < 44\,\mu\mathrm{m}$ ✓ |
| Charge quantization | Berry phase $c_1 = 1$ on $\mathbb{CP}^1$ — topological, Klein-independent ✓ |
| APS index | $\mathrm{ind}(D) = 0$ on $[0, r_{\max}] \times S^2$ — $\eta = 0$ by symmetry ✓ |
| KK reduction | Gravity + U(1) + radion all emerge from 5D interval ✓ |
| Dimensional accounting | 5D (4 + r): ψ is gauge phase, not spatial dimension ✓ |

Klein's mechanism is **not required** by CR. His compactification was sufficient but not necessary; the derived-compact interval provides everything Klein provided, from first principles.

New prediction: non-linear KK mode spacing $m_n/m_1 \approx 1, 1.67, 2.32, 2.97$ (vs. Klein's exactly linear $1, 2, 3, 4$) — a falsifiable observational distinction.

**OP-25. Weak Values from $T_{M\Sigma}$ Cross-Terms (TSVF connection).**

**Status: OPEN — Paper 3 or standalone (2026-04-09).**

The Aharonov Two-State Vector Formalism (TSVF) weak value $\langle\phi|A|\psi\rangle/\langle\phi|\psi\rangle$ maps to CR's joint geometry as follows: the numerator involves the off-diagonal block $T_{M\Sigma}$ of the joint metric, while the denominator involves the inner product between boundary conditions on the geodesic in $M \times \Sigma$. Anomalous weak values (outside the eigenvalue spectrum) correspond to $\Omega/G > 1$ in the joint curvature — the Berry connection curvature $\Omega_{AB}$ exceeds the Fubini-Study metric $G_{AB}$ in the off-diagonal block.

**Required calculation:** Derive the TSVF weak value formula explicitly from $T_{M\Sigma}$. Show that $|\langle\phi|A|\psi\rangle/\langle\phi|\psi\rangle| > \|A\|$ corresponds to the ratio $\Omega_{M\Sigma}/G_{M\Sigma} > 1$ in the cross-block. This would give a geometric explanation for anomalous weak values without invoking any new physics.

**Retrocausality dissolved:** In CR, both $|\psi\rangle$ and $\langle\phi|$ are boundary conditions on the same joint geodesic in $M \times \Sigma$ — not causal influences. The frame-lag $F^A$ captures the TSVF gap between the two boundary conditions. The Markov transition criterion $G_{MM} = G_{\delta\lambda,\delta\lambda}$ (§2.6) is the condition at which the forward and backward state vectors "meet." No retrocausality is required.

**OP-26. Three-Box Paradox from Berry Phase Non-Commutativity.**

**Status: OPEN — Paper 3 or standalone (2026-04-09).**

The Aharonov-Vaidman three-box paradox: with pre-selected state $(|A\rangle + |B\rangle + |C\rangle)/\sqrt{3}$ and post-selected state $(|A\rangle + |B\rangle - |C\rangle)/\sqrt{3}$, the weak measurement certifies particle presence in box $A$ with certainty and in box $B$ with certainty, yet the joint probability $P(A \cap B) \neq 1$.

**CR resolution path:** In the $M \times \Sigma$ joint geometry, the projectors $P_A$ and $P_B$ do not commute when the Berry connection $\Omega_{AB} \neq 0$. "Particle in $A$" and "particle in $B$" are cross-sections of the joint manifold along non-commuting fibers. The TSVF boundary conditions guarantee certainty along individual fibers, but not their intersection — because the intersection requires a joint measurement that opens a third path in $M \times \Sigma$ incompatible with the fiber structure.

**Required calculation:** Show explicitly that $[P_A, P_B] \neq 0$ in $M \times \Sigma$ under nonzero $\Omega_{AB}$, and derive the TSVF three-box certainty results from the joint geodesic boundary conditions. This would be the CR derivation of contextuality from first principles.

---

## §7.3 Experimental Questions (updated)

**OP-14. Frame-lag signatures.** Unchanged from v1.

**OP-15. KK mode detection (updated).**

The KK spectrum from the derived-compact interval (§3.3, Eq. 3.3.6–3.3.7) predicts:
- First KK graviton: $\lambda_1 \approx 13.3\,\mu\mathrm{m}$ (at the self-consistent Casimir correction scale)
- Mode spacing: non-linear ($m_n/m_1 \approx 1, 1.67, 2.32, 2.97$)

The non-linear spacing is the key experimental discriminator from Klein (linear spacing). If the first mode is detected, the ratio $m_2/m_1 \approx 1.67$ (not 2.0) confirms derived compactification over the Klein circle.

**OP-16. Geometric dark matter.** Unchanged from v1.

**OP-17. Cosmological constant (updated).**

The framework now provides a **geometric** origin for $\Lambda > 0$ (§5.3.2, §3.3.5.1). The warp-factor curvature energy produces $\rho_{\mathrm{geom,4D}} = +3.534 \times M_5^3 k^2/s > 0$ classically. The question is no longer "does Casimir energy explain $\Lambda$?" but rather "does the Friedmann balance at the current epoch correctly reproduce $H_0$?"

The quantitative check — computing $s_{\mathrm{now}}$ from $H_0$ via Eq. 5.3.2 and verifying consistency with $\Lambda_{\mathrm{obs}}$ — requires the explicit 5D-to-4D reduction factor from the companion paper [Paper 2B].

---

## §7.4 Internal Consistency Questions

**OP-18. Left-right generator program.** RESOLVED in Wave 1 dispatch (2026-04-08). See `paper2_section_2.5_left_right_generators_v2.md`.

**OP-19. §2.2 hypotheses verification.** Unchanged from v1.

**OP-20. Frame-lag and decoherence timescales.** Unchanged from v1.

**OP-21. $\ell^* = S_{\max}/2$ entropic prediction.** Unchanged from v1.

**OP-22. Decoherence Recapitulates Cosmogenesis.** Unchanged from v1.

**OP-23. Settimo et al. citation and picture-inequivalence.** Bibliography updated in master.bib (2026-04-08 Warp audit). Citation present in §2.5. Remaining: verify $\|\mathcal{L}_t - \mathcal{R}_t\|_{\mathrm{op}}$ contribution to $H_0$ tension.

---

## §7.5 Summary (v2)

| Problem | Scope | Status v1 | Status v2 |
|---------|-------|-----------|-----------|
| OP-1 Norm conventions | Paper 2B | Addressed | Addressed |
| OP-2 Coupling identification | Paper 2B | Addressed | Addressed |
| OP-3 Self-consistency | Paper 2B | Addressed | **SC3 resolved (geometric Λ)** |
| OP-4 Holographic verification | Paper 2B | Addressed | Addressed |
| OP-5 Radius stabilization | Paper 2B | **Critical — OPEN** | **RESOLVED** |
| OP-6 Explicit trajectories | Paper 2B | Addressed | Addressed |
| OP-7 First-principles λ | Paper 3 | High | High |
| OP-8 Higher Chern classes | Paper 3+ | High | High |
| OP-9 Non-abelian fibers | Paper 3+ | High | High |
| OP-10 Coherence RG | Paper 3+ | Medium | Medium |
| OP-11 Gravitational coupling | Paper 3 | High | High |
| OP-12 Quantization | Paper 3+ | Medium | Medium |
| OP-13 Multi-sector | Paper 3+ | Medium | Medium |
| OP-14 Frame-lag signatures | Experimental | Long-term | Long-term |
| OP-15 KK mode detection | Experimental | Near-term | **Updated: non-linear spacing** |
| OP-16 Dark matter | Paper 2B + data | Near-term | Near-term |
| OP-17 Cosmological constant | Paper 3 + data | High | **Updated: geometric Λ primary** |
| OP-18 Left-right generators | Internal | Immediate | **RESOLVED** |
| OP-19 §2.2 hypotheses | Internal | High | High |
| OP-20 Frame-lag timescales | Internal | Medium | Medium |
| OP-21 $\ell^* = S_{\max}/2$ | Internal + numerical | High | High |
| OP-22 Decoherence Recapitulates Cosmogenesis | Internal + Paper 3 | High | High |
| OP-23 Settimo citation | Internal | Immediate | Bibliography updated |
| **OP-24 Klein independence** | Internal | **Critical — OPEN** | **RESOLVED** |
| **OP-25 Weak values from $T_{M\Sigma}$** | Paper 3/standalone | — | Open (new) |
| **OP-26 Three-box from Berry phase** | Paper 3/standalone | — | Open (new) |

**Most significant changes in v2:**
- OP-5 resolved: No stabilization potential needed; cosmological attractor + topological shape freezing
- OP-24 resolved: Klein's mechanism is unnecessary; derived compactification passes all five tests
- Two new OPs added: TSVF connections giving geometric explanations of quantum measurement paradoxes
- OP-15 updated: testable non-linear KK mode spacing prediction
- OP-17 updated: geometric Λ changes the character of the cosmological constant problem

---

## References (within Paper 2)

- §2.2: $\delta\lambda$ formalism
- §2.3, Eq. 2.3.3: Markov ratio
- §2.5: Left-right generator decomposition (v2 complete)
- §3.2: Derived compactification (A(r) = cos(√2 r), Proposition 4.2)
- §3.3 v2: Constraints from derived compactification (this document)
- §4, Eq. 4.1.10: Frame-lag mechanism
- §5.3 v2: SC3 — geometric Λ + Casimir correction
- [Paper 2B]: Companion paper (KCR-Cone evaluation)
- Settimo et al. (2026), PRX Quantum 7, 010340. DOI: 10.1103/6dt2-sq44
- Lee, J.G. et al. (2020), Phys. Rev. Lett. 124, 101101. [ISL 44 μm bound]
- Aharonov, Y. & Vaidman, L. (1990). Phys. Rev. A 41, 11. [TSVF]
- Aharonov, Y., Bergmann, P.G., Lebowitz, J.L. (1964). Phys. Rev. 134, B1410. [Three-box]

---

## Revision History

| Date | Change |
|------|--------|
| 2026-03-10 | Initial draft |
| 2026-03-23 | Added OP-21, OP-22, OP-23 |
| 2026-04-10 | **v2:** OP-5 resolved; OP-24 added and resolved; OP-25/26 added; OP-15/17 updated |
