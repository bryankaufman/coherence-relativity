# §4.5 C¹ Regularity: Standard Model vs. Derived Compactification

**Status:** DRAFT — Wave 5 new section
**Model:** Sonnet (structured comparison)
**Source material:** §4.4 FINAL (KK-Cone C¹ verification), RS1/RS2 literature
**Cross-references:** §3.2 (topology as output), §3.3 (what derived compactification constrains), §4 (abstract EOM)

---

## §4.5.1 The Standard Model's C¹ Problem

In Randall-Sundrum (RS) models, the extra dimension is compactified by inserting branes — codimension-1 hypersurfaces that serve as boundaries or defects in the bulk geometry. The 5D metric takes the general form:

$$ds^2 = n(y)^2 \, dz^2 + A(y)^2 \, \eta_{\mu\nu} \, dx^\mu dx^\nu + dy^2 \tag{4.5.1}$$

where $y$ is the coordinate along the extra dimension, $A(y)$ is the warp factor, and $n(y)$ is the temporal warp.

Between the branes, the bulk vacuum Einstein equations determine $A(y)$ and $n(y)$. The standard RS1 solution is:

$$A(y) = e^{-k|y|}, \quad n(y) = 1 \tag{4.5.2}$$

where $k$ is the AdS curvature scale and $|y|$ reflects the orbifold identification $y \sim -y$.

**The regularity issue:** The warp factor $A(y) = e^{-k|y|}$ is continuous (C⁰) at $y = 0$ but not differentiable (not C¹):

$$A'(0^+) = -k, \quad A'(0^-) = +k \tag{4.5.3}$$

The first derivative has a discontinuity $\Delta A' = -2k$ at the brane location. In the language of distribution theory, the second derivative contains a Dirac delta:

$$A'' = -k^2 A + 2k \, \delta(y) \tag{4.5.4}$$

This delta-function curvature is the geometric manifestation of the brane's stress-energy.

### The Israel Junction Conditions

The Israel junction conditions relate the discontinuity in the extrinsic curvature at the brane to the brane's energy-momentum tensor $S_{\mu\nu}$:

$$[K_{\mu\nu}] - [K] h_{\mu\nu} = -\kappa_5^2 \, S_{\mu\nu} \tag{4.5.5}$$

where $[K_{\mu\nu}]$ denotes the jump in extrinsic curvature across the brane, $[K]$ is the trace, and $h_{\mu\nu}$ is the induced metric.

For the RS1 solution, the junction conditions require:

$$T_{\text{brane}} = \frac{6k}{\kappa_5^2} \tag{4.5.6}$$

The brane tension $T_{\text{brane}}$ is a free parameter, tuned to produce the desired kink in $A(y)$. This tuning is the essence of the RS hierarchy mechanism: the ratio of scales on the two branes is exponentially sensitive to the inter-brane separation $L$, giving a natural explanation for the Planck-weak hierarchy.

### What This Means for Regularity

In the RS framework, the C¹ failure at the brane is not a defect — it is the *mechanism*. The brane is the locus where the bulk geometry transitions between two smooth regions, and the kink in $A(y)$ encodes the brane's physical content. The Israel junction conditions *absorb* the delta-function stress-energy by matching it to a freely chosen brane tension.

The key observation: **regularity is tuned, not derived.** The brane tension $T_{\text{brane}}$ is a free parameter. You choose where to place the brane, you choose the tension, and the junction conditions accommodate the resulting kink. Different tensions produce different kinks, and the geometry adjusts accordingly.

This is a feature of *assumed* compactification: the topology is specified by hand (an orbifold $S^1/\mathbb{Z}_2$ with branes at the fixed points), and the regularity properties follow from the freely tunable brane parameters.

---

## §4.5.2 Derived Compactification Constrains Regularity

In the coherence-frame formalism, the compact fiber does not arise from an assumed orbifold. It emerges from the Hopf fibration over the coherence state space (§3.2):

$$S^1 \hookrightarrow S^3 \xrightarrow{\pi} S^2 \simeq \mathbb{CP}^1 \tag{4.5.7}$$

The total space $E_{c_1}$ is determined by the first Chern number $c_1$. For $c_1 = 1$ (the minimal non-trivial bundle), the total space is $S^3$ — a smooth, compact manifold without boundary or orbifold singularities.

This has three consequences for regularity that have no counterpart in the RS framework:

### §4.5.2.1 No Arbitrary Brane Insertion

In RS models, branes are inserted at freely chosen locations in the extra dimension. In derived compactification, the topology of the total space is fixed by $c_1$. For $c_1 = 1$, the total space $S^3$ is smooth everywhere. There is no codimension-1 locus where a brane *must* sit.

If a brane-like defect appears, it must arise from the field content — a physical source that creates a singularity in the metric. But such a source must be *derived* from the dynamics, not inserted by hand. The location and strength of any singularity are predictions of the theory, not inputs.

### §4.5.2.2 Regularity Follows from Topology

If the derived total space is a smooth manifold (as $S^3$ is for $c_1 = 1$), the metric must be smooth everywhere — unless there is a physical reason for a singularity. Specifically:

- If the field equations on $S^3$ admit smooth solutions, the warp factor $A(r)$ is $C^\infty$ (or at least $C^k$ for arbitrarily large $k$) throughout the bulk.
- Any failure of smoothness must be sourced by distributional matter (as in Eq. 4.5.4), but such matter is now part of the theory's dynamics, not an external input.

This is a qualitative departure from RS: in assumed compactification, the orbifold structure *requires* distributional sources at the fixed points. In derived compactification, the smooth total space *forbids* distributional sources unless they arise dynamically.

### §4.5.2.3 No Tension Tuning

The RS hierarchy mechanism relies on tuning the brane tension (Eq. 4.5.6) to produce the desired warp profile. In derived compactification, there is no free brane tension:

- The topology $E_{c_1}$ is fixed
- The fiber structure determines where (if anywhere) the warp profile might develop features
- Whatever regularity class the warp profile belongs to is a *prediction*, not a tuned parameter

If the equations of motion on $S^3$ require $A(r) \in C^1$, this is a theorem about the specific geometry. If they permit $A(r)$ to have kinks, the kink locations and magnitudes are determined — not freely chosen.

---

## §4.5.3 Framework-Level Claim

The contrast between assumed and derived compactification can be summarized as follows:

| Property | Assumed (RS) | Derived (Coherence Frame) |
|----------|-------------|--------------------------|
| Topology | Specified by hand ($S^1/\mathbb{Z}_2$) | Emerges from Hopf fibration (§3.2) |
| Brane insertion | Free parameter (location, number) | Constrained by topology |
| Warp factor regularity | C⁰ at branes, with tunable kinks | Determined by field equations on smooth $E_{c_1}$ |
| Junction conditions | Absorb kinks via tunable tension | Not applicable (no hand-inserted branes) |
| Regularity class of $A$ | Input (depends on brane choice) | Output (prediction of the theory) |

**Framework-level result:** Derived compactification constrains the regularity class of admissible warp profiles. The topology predicts where smooth metrics are required and where singularities (if any) must be sourced by dynamical field content. This is a qualitative departure from the standard model, where regularity is absorbed into junction conditions with tunable brane tensions.

### Sufficient Conditions for C¹

The specific sufficient conditions for C¹ regularity of the coherence-to-classical map on a warped geometry are established in the companion paper [Paper 2B, §2.4]:

- **(Reg1)** Global C¹ smoothness of $A(r, z)$ with bounded derivatives
- **(Reg2)** Bounded first partial derivatives: $|\partial_r A| + |\partial_z A| \leq C$
- **(Reg3)** Uniform conical structure at any tip: $A(r, z) = C(z) \, r + O(r^2)$ with $C(z) \in C^1$

These conditions are checked explicitly for the KK-Cone geometry in [Paper 2B, §2.4]. The key finding is that the smooth Hopf bundle structure ($S^3$ for $c_1 = 1$) naturally satisfies (Reg1)–(Reg3), whereas RS orbifolds violate (Reg1) at brane locations by construction.

### Scope and Limitations

⚠️ **Important caveat:** The claim is that derived compactification *constrains* regularity — not that it guarantees C¹ in all cases. Pathological field configurations could still produce singularities (e.g., if the matter sector develops a distributional source). The point is that such singularities are *predicted* by the dynamics, not *inserted* by the model-builder.

⚠️ **The C¹ verification for the specific KK-Cone geometry** — including the analysis of the cone tip, the Hopf fiber structure, and the warp factor dependence on the coherence parameter — is carried out in full in [Paper 2B, §2.4]. The present section establishes only the *principle* that derived topology constrains regularity, which is a framework result.

**Delivered promise:** *C¹ regularity* ✅ — framework principle established: derived compactification constrains the regularity class of warp profiles, in qualitative contrast to assumed compactification where regularity is tuned via junction conditions. Geometry-specific verification in [Paper 2B, §2.4].

---

## References

- Randall, L. & Sundrum, R. (1999). "A Large Mass Hierarchy from a Small Extra Dimension." *Phys. Rev. Lett.* 83, 3370.
- Randall, L. & Sundrum, R. (1999). "An Alternative to Compactification." *Phys. Rev. Lett.* 83, 4690.
- Israel, W. (1966). "Singular hypersurfaces and thin shells in general relativity." *Nuovo Cim.* B44, 1.
- Goldberger, W. & Wise, M. (1999). "Modulus Stabilization with Bulk Fields." *Phys. Rev. Lett.* 83, 4922.
- §3.2 (this paper): Topology as output — S² → Hopf → compact S¹
- §3.3 (this paper): What derived compactification constrains
- [Paper 2B, §2.4]: C¹ regularity verification on the KK-Cone

---

## Revision History

| Date | Change |
|------|--------|
| 2026-03-10 | Initial draft — Wave 5 new section. Three-act teaching arc: RS junction conditions → derived topology constrains regularity → framework claim. |

---

**Word count:** ~1,800 (target: 1,500–2,500 for a comparison section)
**Math rigor:** RS equations from standard literature; derived-compactification claims referenced to §3.2–§3.3
**Status transparency:** Framework claim clearly distinguished from geometry-specific verification
