# RC-1 Verification Memo — §RC1.1 through §RC1.5

**Date:** 2026-04-17
**Verifier:** Claude (Opus pass on Sonnet 4.6 draft)
**Ledger item addressed:** #17 (RC1.1 + RC1.2 symmetry argument — Opus verification recommended)
**Scope:** Paper 2C §2 (RC-1), lines 12–626 of `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`

---

## Overall assessment

**Realistic status: RC-1 is ~85% verified.**

The derivation is structurally sound. Both the symmetry argument (§RC1.1) and the metric variation (§RC1.2) reach the correct result, and the downstream physical limits (§RC1.3) and spectrum formula (§RC1.4) follow correctly from the boxed form of $T^{(\mathrm{eff})}_{\mu\nu}$. None of the issues below invalidate the RC-1 conclusion.

However, the draft has six specific issues — four presentational, two substantive — that should be addressed before the manuscript is submitted. I mark them below with explicit severity.

- ✅ **VERIFIED:** Final boxed results (ℒ_bdry, T^(eff)_μν, 𝒫^Σ(k), w = −1 and w = 0 identifications)
- ⚠️ **UNTESTED / NEEDS TIGHTENING:** Six specific steps listed below
- ❌ **MISSING:** Nothing structural is missing at the RC-1 level; the RC-2/RC-3 gates are correctly flagged
- 🤔 **UNKNOWN:** The α = 3/2 spectral-dimension argument (C1) is not actually derived from the stated CP¹ spectral density — see Issue #4 below

---

## Issue #1 — Σ-index dimension convention (⚠️ presentational)

**Location:** §RC1.1, line 77
**Severity:** Low (does not affect result) but confusing to a careful reader

**Problem:** The text writes `T_M^{μa}` with `a = 1, …, d²`. But Σ = U(d)/T^d has real dimension `d² − d`, not `d²`. The dimension `d²` is the dimension of u(d) (the Lie algebra of U(d)), which is the tangent space at the identity coset.

**What's actually happening:** T_M is most naturally interpreted as valued in a u(d) representation (the off-diagonal block of the Kaluza-Klein-type metric on M × Σ). Whether the relevant representation is u(d) itself (adjoint), a complement to t^d in u(d) (real dim d²−d, which is T_pΣ), or the fundamental of U(d) (complex dim d) — the text is ambiguous.

**Why the result survives:** In all three interpretations, there is a unique leading U(d)-invariant real bilinear, and it is $\mathrm{Tr}(T_M T_M^\dagger)$ contracted with $g_{\mu\nu}$ on M-indices. The Σ-index range ambiguity does not affect the boxed form.

**Recommended fix:** Add one sentence after line 41 specifying the representation. Suggested:

> "Throughout, we treat $T_M^{\mu a}$ as a section of $TM \otimes \mathfrak{u}(d)^\perp$, where $\mathfrak{u}(d)^\perp$ is the complement of $\mathfrak{t}^d$ in $\mathfrak{u}(d)$ — equivalently, the tangent space $T_p\Sigma$. The Σ-index $a$ therefore ranges over $d^2 - d$ values and transforms under the isotropy representation of U(d)/T^d."

Then §RC1.1 Constraint 2 should be revised to note that the fundamental-rep language in line 73 is a convenient shorthand; the rigorous statement uses the isotropy representation.

---

## Issue #2 — Linear-invariance argument is misstated (⚠️ presentational)

**Location:** §RC1.1, line 81 ("Why this is the only leading bilinear" bullet 1)
**Severity:** Low (conclusion is correct, argument is wrong)

**Problem:** The text says:

> "A linear invariant Tr(T_M) would require contracting both M and Σ indices with a fixed tensor. The only fixed tensors available are g_{μν} (M-metric) and h_{ab} (Σ-metric). The combination g_{μν} h^{ab} T_M^{μ}{}_b vanishes for off-diagonal T_M when M and Σ are not mixed."

This is not the reason linear invariants are forbidden. A linear scalar in $T_M^{\mu a}$ requires contraction with a fixed (1,1)-tensor having one M-covariant index and one Σ-covariant index. Neither $g_{\mu\nu}$ nor $h_{ab}$ has that structure. What is needed is a preferred M×Σ "pair" — a fixed vector in $TM \otimes T_p\Sigma$. The non-existence of such a fixed tensor under U(d) × Diff(M) follows from the fact that U(d) acts transitively on Σ, so by Schur's lemma there is no U(d)-invariant vector in the isotropy representation.

**Recommended fix:** Replace lines 80-82 with:

> "A linear scalar in $T_M^{\mu a}$ would require contraction with a fixed element of $T^*M \otimes T_p^*\Sigma$. Under the action of U(d) on Σ, which is transitive, no such invariant tensor exists: the isotropy representation at $p \in \Sigma$ contains no U(d)-invariant vector (Schur's lemma). Linear invariants are therefore forbidden by the U(d) symmetry alone, independent of the form of any contracted tensor."

This is a one-paragraph rewrite, not a structural change.

---

## Issue #3 — Dimensional convention for T_M needs a sentence (⚠️ presentational)

**Location:** §RC1.1, line 115 ("The field T_M^{μa} is a metric component (dimensionless in the metric signature convention where g_{\mu\nu} has no mass dimension)")
**Severity:** Low (conventions are consistent, but the reader isn't told)

**Problem:** The dimensional accounting that makes λ have mass dimension [M³] depends on T_M being dimensionless (metric-perturbation convention). If the reader interprets T_M as a tensor field with dimension [M] or [M²] (e.g., a Goldstone mode convention), λ acquires a different dimension. This should be stated.

**Recommended fix:** Insert after line 113:

> "We adopt the metric-perturbation convention throughout, in which $T_M^{\mu a}$ is dimensionless — consistent with its definition as an off-diagonal block of the M × Σ metric $G_{AB}$. Under this convention, couplings that multiply $\mathrm{Tr}(T_M T_M^\dagger)$ carry mass dimension."

---

## Issue #4 — α = 3/2 "spectral density" sketch has an internal inconsistency (🤔 UNKNOWN / substantive)

**Location:** §RC1.3, lines 346-353
**Severity:** Moderate — the exponent α = 3/2 is already flagged as Conjecture C1, but the stated derivation sketch is internally inconsistent and may mislead a reader.

**Problem:** The text claims:

> "The spectral density of the FS Laplacian on CP¹ scales as ρ(λ) ~ λ^{1/2}"
>
> "|T_M|² ~ ∫₀^{Γ_dec} dλ ρ(λ) ~ Γ_dec^{3/2}"
>
> "The 3/2 power arises from the **spectral dimension** of Σ in the d=2 case: a single complex dimension gives the Weyl-type density of states ρ(λ) ~ λ^{d_Σ/2 - 1} = λ^0..."

The two statements do not agree. Weyl's formula on a $d_\Sigma$-dimensional compact manifold gives a density of eigenvalues $\rho(\lambda) \sim \lambda^{d_\Sigma/2 - 1}$. For CP¹ (real dimension 2), this is $\rho(\lambda) \sim \lambda^0 = \mathrm{const}$, leading to $|T_M|^2 \sim \int_0^{\Gamma_{\rm dec}} d\lambda \cdot \mathrm{const} \sim \Gamma_{\rm dec}^1$, giving $\alpha = 1$, not $3/2$.

To obtain $\alpha = 3/2$ from the spectral-density integral, one would need $\rho(\lambda) \sim \lambda^{1/2}$, which corresponds to $d_\Sigma = 3$, not 2. Alternatively, one could argue that the *Zeta-regularized* sum over modes gives a $3/2$ power via a different mechanism — e.g., a Bekenstein-type coupling where $|T_M|^2$ integrates against the propagator rather than just the spectral density — but that argument is not made here.

**What I verified:** I confirm that the Weyl formula for CP¹ gives $\rho \sim \mathrm{const}$, so the stated route does not produce 3/2. I did NOT verify that 3/2 is wrong — there may be a different spectral mechanism (e.g., a one-loop correction with a logarithm, or a Casimir-type sum) that recovers $\alpha = 3/2$. That derivation is what RC-2 owes.

**Recommended fix:** The explicit "ρ(λ) ~ λ^{1/2}" claim in line 350 should be removed, because it contradicts Weyl's formula for CP¹. Replace with honest flagging:

> "**Status:** The exponent $\alpha = 3/2$ is not derived here. A naive Weyl-formula argument on CP¹ (real dim 2) gives $\rho(\lambda) \sim \mathrm{const}$ and would yield $\alpha = 1$, not $3/2$. A derivation producing $3/2$ must invoke additional structure — e.g., the full M×Σ propagator contracted against the FS Laplacian, or a Bekenstein-bound normalization of the T_M amplitude. This derivation is the central task of RC-2."

This is a substantive honest-reporting fix. The α = 3/2 remains Conjecture C1, as already labeled.

---

## Issue #5 — DM-limit ansatz T_M = A(ρ_b) u⊗ψ is not justified as unique (⚠️ substantive)

**Location:** §RC1.3 Limit B, line 373
**Severity:** Moderate — the form is presented as "minimal" but alternative rank-1 or rank-2 structures would also work.

**Problem:** The ansatz $T_M^{\mu a}(y) = A(\rho_b(y))\, u^\mu\, \psi^a$ is one specific factorized rank-1 outer product. Other structures consistent with "tracks ρ_b" include:

- Rank-1 with a different M-vector: $T_M = A(\rho_b)\, \hat{n}^\mu \psi^a$ (normal direction instead of comoving velocity)
- Rank-2: $T_M = A(\rho_b)(u^\mu \psi^a + \epsilon\, v^\mu \chi^a)$ with a secondary mode
- Non-factorized: $T_M = f(\rho_b, u)^{\mu a}$ where the spatial profile mixes M and Σ indices non-trivially

The text's ansatz gives the cleanest w = 0 result, but the uniqueness claim is not established. The derivation of "pressureless dust emerges from anisotropic T^(eff)" therefore assumes the specific outer-product form.

**Recommended fix:** Replace line 373 with:

> "The minimal anisotropic ansatz consistent with (i) a single preferred M-direction (comoving with baryons), (ii) a single preferred Σ-direction (the "baryonic decoherence channel"), and (iii) leading-order scaling $T_M \propto A(\rho_b)$ is the rank-1 outer product:
>
> $$T_M^{\mu a}(y) = A(\rho_b(y))\, u^\mu\, \psi^a$$
>
> We adopt this ansatz for concreteness; the derivation of w = 0 below depends on this factorization. A uniqueness argument would require solving the M-Σ EOM for T_M with $\Gamma_{\rm dec} \propto \rho_b$ as source, which is RC-2."

---

## Issue #6 — Conservation check in the DM limit is loose (⚠️ substantive)

**Location:** §RC1.2 Conservation Check, lines 265-279
**Severity:** Low-moderate — the argument is correct in the DE limit, appropriately flagged (A4) in the DM limit, but the intermediate algebra is sparse.

**Problem:** The text writes:

$$\nabla^\mu T^{(\mathrm{eff})}_{\mu\nu}\big|_{\partial M} = \partial_i(\sqrt{-\gamma}\, f)\, e^i_\nu \cdot \delta_\perp + \sqrt{-\gamma}\, f \cdot [\partial_\perp \delta_\perp]\, n_\nu$$

This is correct but missing the extrinsic curvature contribution. The full computation (using $T^{(\mathrm{eff})}_{\mu\nu} = \lambda q_{\mu\nu} |T_M|^2 \delta(\ell)$ where $q_{\mu\nu} = g_{\mu\nu} - \epsilon n_\mu n_\nu$ is the standard projector):

$$\nabla^\mu T^{(\mathrm{eff})}_{\mu\nu} = \lambda\,\delta(\ell)\left[\, q_{\mu\nu}\nabla^\mu |T_M|^2 - (K n_\nu + a_\nu)|T_M|^2 \,\right] + \lambda\, q_{\mu\nu}|T_M|^2 \, n^\mu\,\delta'(\ell)$$

where $K = \nabla^\mu n_\mu$ is the mean extrinsic curvature and $a_\nu = n^\mu \nabla_\mu n_\nu$ is the acceleration of the normal. The $\delta'(\ell)$ term vanishes because $q_{\mu\nu} n^\mu = 0$ (the projector is tangential by construction). The remaining $\delta(\ell)$ term gives the tangential conservation equation:

$$q_{\mu\nu}\nabla^\mu |T_M|^2 = (K n_\nu + a_\nu)|T_M|^2$$

In the DE limit ($|T_M|^2$ uniform), both sides are zero: LHS because $\nabla |T_M|^2 = 0$, RHS because $|T_M|^2$ multiplied by geometric factors still has to be balanced by the ∂M evolution equation (essentially the null energy condition for the ∂M hypersurface). For a null ∂M (fact horizon), K = 0 and conservation is automatic.

In the DM limit, the tangential gradient is non-zero and must be absorbed by the T_M EOM, which is correctly flagged as A4.

**Recommended fix:** Expand the conservation check with the explicit q_μν decomposition, include the K and a_ν terms, and state clearly that the fact-horizon ∂M (null surface with K = 0 to leading order) makes the DE limit automatic without needing A4. This is a 3-paragraph tightening; no structural change.

---

## Downstream status — what RC-1 delivers to the rest of Paper 2C

The following downstream claims in §5 (Holographic Dictionary), §7 (RC-2 open items), and §8 (Quantum-Foundations Applications) are supported by the verified parts of RC-1:

- ✅ T^(eff)_μν = λ q_μν |T_M|² δ(ℓ) — **used by** §5 (holographic conjecture made precise), §7 (RC-2 gate)
- ✅ w = −1 for isotropic (DE) limit — **used by** §5.3 Λ-sector, Paper 2B §5.3
- ✅ w = 0 for anisotropic (DM) limit — **used by** Paper 3 dark-sector predictions (modulo ansatz in Issue #5)
- ✅ 𝒫^Σ(k) = A_s k²/(k² + k_c²) formula — **used by** RC-3 CMB pipeline, 69% quadrupole suppression check
- ⚠️ α = 3/2 exponent — **Conjecture C1, not derived here** (Issue #4 above)
- ⚠️ Ω_DM/Ω_b consistency — **Conjecture C2, requires λ normalization from RC-2**
- ⚠️ Covariant conservation — **Assumption A4, requires RC-2**

---

## Integration with the Open Items Ledger

This verification resolves ledger item #17 (RC1.1 + RC1.2 symmetry argument — Opus verification recommended) with the status: **verified with six specific issues flagged above**.

Ledger items that remain untouched by this memo:
- #12 (δT_M/δg^{μν} extraction — RC-2 work)
- #13 (Covariant conservation — RC-2 work)
- #18 (FR holonomy Ω = π — §8.1 verification still pending)
- #19 (Proietti protocol — §8.2 verification still pending)
- #20 (Eq. 8.4.5 — §8.4 verification still pending)

These are the remaining Opus verification passes for Paper 2C §8 quantum-foundations applications — separate from the RC-1 work.

---

## Recommended action

**For Warp:** Apply the six fixes above as a single commit to `paper2C_HOLOGRAPHIC_STRUCTURE_2026-04-17.md`. Issues #1, #2, #3, #5 are surgical (1-3 sentences each). Issue #4 requires removing one inconsistent sentence and adding honest-reporting language. Issue #6 requires a 3-paragraph expansion of the conservation check.

**For Bryan:** After Warp's patches are applied, the RC-1 line is ready for the Paper 2C reconciliation audit. The RC-2 work (ledger items #12, #13) then becomes the next gating calculation — it is the right target for a dedicated Opus session, because it requires solving the M-Σ coupled equations of motion and deriving both δT_M/δg^{μν} and the |T_M|² ∝ Γ_dec^{3/2} scaling from first principles (resolving Conjecture C1 and Assumption A3-A4).

**For the ledger:** Update item #17 status to "VERIFIED with 6 issues flagged — see RC1_VERIFICATION_MEMO_2026-04-17.md". Do not mark C1 or A4 as resolved — these remain for RC-2.

---

## Next Steps

1. Warp applies the six fixes (estimated 30-60 minutes)
2. Warp updates PAPER2_OPEN_ITEMS_LEDGER to reflect item #17 status
3. Bryan initiates RC-2 session (dedicated Opus pass, scope: δT_M/δg^{μν} + |T_M|² ∝ Γ_dec^{3/2} derivation)
4. Items #18, #19, #20 are scoped for a separate Opus pass on Paper 2C §8

## Realistic Status

**RC-1 derivation: ~85% verified.** Core results are correct. Six surgical fixes close the remaining presentation gaps and resolve the one internal inconsistency (α = 3/2 sketch). The substantive gates — α = 3/2 derivation, covariant conservation, δT_M/δg^{μν} — are correctly flagged as RC-2 work and are not expected to be resolved in RC-1.
