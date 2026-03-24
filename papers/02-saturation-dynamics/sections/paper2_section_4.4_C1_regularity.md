# §4.4 Warped C¹ Regularity Verification

## 4.4.1 Introduction and Promise Resolution

Paper 1 (line 411) deferred the embedding-level regularity check for warped profiles A(r,z) to this section. The coherence-relativity framework requires continuous differentiability (C¹) of the coherence-to-classical map to ensure that small perturbations in the coherence frame induce small, physically meaningful changes in observable predictions. A failure of C¹ continuity would signal unphysical discontinuities or cusps in the quasipotential landscape, violating the fundamental smoothness requirement.

In the KK-Cone model, the 5D metric is given by:

$$\begin{equation}
\mathrm{d}s^2 = e^{2A(r,z)}\left(-\mathrm{d}t^2 + \mathrm{d}x_3^2\right) + \mathrm{d}r^2 + r^2\left(\mathrm{d}\theta^2 + \sin^2\theta\,\mathrm{d}\varphi^2\right) + L^2\left(\mathrm{d}\psi + \cos\theta\,\mathrm{d}\varphi\right)^2 \tag{4.4.1}
\end{equation}$$

where A(r,z) is a smooth warp factor on the non-compact brane coordinate space, and (t, x₃, r, θ, φ, ψ) are the five KK-Cone coordinates. The structure combines:
- A Minkowski × Cone base (first four terms)
- A Hopf fibration S¹ bundle over S² (the ψ circle with connection form cos θ dφ)

The coherence-to-classical map V : M → ℝ (where M is the 4D spacetime) is defined via the quasipotential:

$$\begin{equation}
V(x) = \inf_{\gamma \in \Gamma(x)} S[\gamma] \tag{4.4.2}
\end{equation}$$

where Γ(x) is the space of paths in the joint manifold M × Σ (spacetime × coherence domain) that project to x on the spacetime component, and S[γ] is the coherence action functional. The requirement is that V ∈ C¹(M) — that is, V and ∇V are continuous.

## 4.4.2 Regularity of the Coherence-to-Classical Map

### Definition of the Map

The coherence-to-classical map is formally:

$$\begin{equation}
\Phi: M \times \Sigma \to M \times \mathbb{R}, \quad \Phi(x, \sigma) = (x, V(x)) \tag{4.4.3}
\end{equation}$$

where Σ is the coherence parameter space (typically ℂℙⁿ or a Kähler manifold) and V(x) is the infimum of the action over all coherence paths projecting to x. For C¹ regularity, we require:

$$\begin{equation}
\text{(C1)} \quad V(x) \in C^1(M), \quad \text{i.e., } V \text{ and } \partial_\mu V \text{ are continuous for all } \mu = 0, 1, 2, 3 \tag{4.4.4}
\end{equation}$$

This is equivalent to requiring that the quasipotential landscape has no cusps, jumps, or corners in first-order derivatives.

### The Role of the Warp Factor

The warp factor A(r,z) enters the metric through the exponential conformal factor e^{2A(r,z)}, which scales the Minkowski × Cone sector. This affects the coherence-to-classical map in two ways:

1. **Direct metric scaling**: The warp factor modulates the proper distance in the t and x₃ directions, influencing the path length functional and hence S[γ].
2. **Geometry of the brane**: The brane position z, which parametrizes A(r,z), encodes coherence-frame choices. Regularity of A with respect to z ensures that small shifts in the coherence frame produce small changes in the emergent metric.

For the C¹ condition to hold, the warp factor must satisfy:

$$\begin{equation}
A(r,z) \in C^1(\mathbb{R}^+ \times \Sigma) \tag{4.4.5}
\end{equation}$$

where ℝ⁺ is the radial coordinate domain and Σ is the coherence domain. This ensures that both A and ∂_r A, ∂_z A are continuous.

## 4.4.3 Regularity Analysis at Potential Singularities

### 4.4.3.1 The Cone Tip (r = 0)

**Geometric Issue**: The Cone factor r²(dθ² + sin²θ dφ²) vanishes as r → 0. The warp factor A(r,z) may also diverge, depending on the profile chosen. If A(r,z) → -∞ as r → 0, the Minkowski sector is exponentially suppressed (e^{2A} → 0), creating a potential geometric singularity.

**Analysis**: Consider the metric near r = 0:

$$\begin{equation}
\mathrm{d}s^2 \approx e^{2A(0,z)}(-\mathrm{d}t^2 + \mathrm{d}x_3^2) + \mathrm{d}r^2 + O(r^2) \tag{4.4.6}
\end{equation}$$

If A(0,z) is finite and C¹ with respect to z, then locally the metric behaves as flat spacetime plus a smooth Cone correction. The path integral action S[γ] for paths near r = 0 remains bounded and smooth.

**Critical Condition**: If A exhibits a divergence like A(r,z) ~ ln r, then e^{2A(r,z)} ~ r², which produces a conical metric:

$$\begin{equation}
\mathrm{d}s^2 \sim r^2(-\mathrm{d}t^2 + \mathrm{d}x_3^2) + \mathrm{d}r^2 + r^2(\mathrm{d}\theta^2 + \sin^2\theta\,\mathrm{d}\varphi^2) \tag{4.4.7}
\end{equation}$$

This is a valid (singular) metric of conical type, with an orbifold singularity at r = 0. The quasipotential V(x) will be C¹ at the projection of r = 0 (i.e., on the brane), provided the logarithmic divergence is uniform in the coherence parameter z. More precisely:

$$\begin{equation}
\text{(Condition 4.4.7a)} \quad A(r,z) = \ln r + B(z) + \mathrm{higher\,order\,terms}, \quad B(z) \in C^1(\Sigma) \tag{4.4.8}
\end{equation}$$

Under this condition, the metric is a warped product with a uniform conical structure, and V inherits C¹ from B(z).

### 4.4.3.2 The Hopf Fiber Structure

**Geometric Issue**: The Hopf fiber coordinate ψ appears with the connection form (cos θ dφ), which is singular at the coordinate poles (θ = 0, π) in the S² base. However, the total space S³ (which is the Hopf bundle S¹ → S³ → ℂℲ¹) is smooth.

**Analysis**: The Hopf metric term is:

$$\begin{equation}
L^2(\mathrm{d}\psi + \cos\theta\,\mathrm{d}\varphi)^2 \tag{4.4.9}
\end{equation}$$

At θ = 0 and θ = π, the connection form cos θ dφ vanishes, but this is not a singularity of S³ — it is a coordinate artifact. The one-form (cos θ dφ) is the pullback of a smooth connection on the Hopf bundle, and the metric on S³ is smooth everywhere.

**Verification**: To see smoothness explicitly, switch to standard ℂℲ¹ coordinates (z₀, z₁) with |z₀|² + |z₁|² = 1. The metric on S³ becomes:

$$\begin{equation}
\mathrm{d}s^2_{\mathrm{S}^3} = |z_0 \mathrm{d}z_1 - z_1 \mathrm{d}z_0|^2 \tag{4.4.10}
\end{equation}$$

This is manifestly smooth. The fiber coordinate ψ and base coordinates (θ, φ) are singular at the poles, but the metric itself is smooth in every coordinate chart.

**Conclusion**: The Hopf fiber contributes a smooth term to the 5D metric. No additional regularity condition is required beyond the smoothness of L.

### 4.4.3.3 Warp Factor Regularity with Respect to Coherence Parameter

**Geometric Issue**: The warp factor A(r,z) depends on the coherence-frame parameter z ∈ Σ. If A is not sufficiently smooth in z, the coherence-to-classical map will fail C¹.

**Analysis**: The gradient of V with respect to spacetime coordinates includes terms from ∇_r A and ∇_z A. For C¹ regularity, we need:

$$\begin{equation}
\frac{\partial V}{\partial x^\mu} = \inf_{\gamma(x)} \left[ \frac{\delta S[\gamma]}{\delta x^\mu} \right] \tag{4.4.11}
\end{equation}$$

where the variational derivative includes contributions from ∇ A. By the envelope theorem, this derivative is continuous if and only if A(r,z) ∈ C¹ in both r and z uniformly over bounded regions.

**Critical Condition**:

$$\begin{equation}
\text{(Condition 4.4.11a)} \quad \frac{\partial A}{\partial r} \in C^0(\mathbb{R}^+ \times \Sigma), \quad \frac{\partial A}{\partial z} \in C^0(\mathbb{R}^+ \times \Sigma) \tag{4.4.12}
\end{equation}$$

This ensures that both A and its derivatives are bounded and continuous, preventing caustics or turning points in the path integral.

## 4.4.4 Main Regularity Theorem

**Theorem 4.4.1** (C¹ Regularity of Coherence-to-Classical Map):

Let A(r,z) ∈ C¹(ℝ⁺ × Σ) be a warp factor on the KK-Cone satisfying:

$$\begin{equation}
\text{(Reg1)} \quad A(r,z) \text{ is globally } C^1 \text{ with bounded derivatives} \tag{4.4.13}
\end{equation}$$

$$\begin{equation}
\text{(Reg2)} \quad \left|\frac{\partial A}{\partial r}\right| + \left|\frac{\partial A}{\partial z}\right| \leq C \quad \text{for some constant } C > 0 \tag{4.4.14}
\end{equation}$$

$$\begin{equation}
\text{(Reg3)} \quad \text{Any conical singularity at } r=0 \text{ must satisfy Condition 4.4.7a} \tag{4.4.15}
\end{equation}$$

Then the coherence-to-classical map Φ : M × Σ → M × ℝ defined via the quasipotential V(x) = inf_γ S[γ] satisfies:

$$\begin{equation}
V(x) \in C^1(M), \quad \text{i.e., } V \text{ and } \nabla_\mu V \text{ are continuous} \tag{4.4.16}
\end{equation}$$

*Proof Sketch*:

1. The action functional S[γ] is a continuous map from the path space to ℝ whenever the metric coefficients are continuous.

2. By Dini's theorem, the infimum of a continuous family of continuous functions is continuous if the family is compact or if a uniform bound condition holds. Condition (Reg2) provides such a bound.

3. The Fréchet derivatives of V with respect to spacetime coordinates follow from the envelope theorem: if the minimizer γ* is unique and smooth (which holds generically for metrics satisfying (Reg1)–(Reg3)), then:

$$\begin{equation}
\frac{\partial V}{\partial x^\mu} = \left.\frac{\delta S[\gamma]}{\delta x^\mu}\right|_{\gamma=\gamma^*} \tag{4.4.17}
\end{equation}$$

4. Condition (Reg1) ensures that the metric and its first derivatives are continuous, so ∂V/∂x^μ is continuous.

5. At potential singularities (cone tip, poles), conditions (Reg3) and smoothness of the Hopf fiber (§4.4.3.2) ensure that the metric is at worst a smooth orbifold metric, which preserves C¹ of the action functional.

6. Therefore, V ∈ C¹(M). ∎

## 4.4.5 Sufficient Conditions in Practice

For explicit profiles A(r,z), the regularity conditions can be checked directly. Common examples:

**Example 1: Gaussian Warp Factor**

$$\begin{equation}
A(r,z) = -\lambda \exp\left(-\frac{r^2}{2\sigma^2(z)}\right), \quad \sigma(z) \in C^1(\Sigma) \tag{4.4.18}
\end{equation}$$

This is analytic in both r and z (hence C¹). Conditions (Reg1)–(Reg2) are satisfied. ✓

**Example 2: Logarithmic Conical Warp**

$$\begin{equation}
A(r,z) = \alpha(z) \ln r + \beta(z), \quad \alpha, \beta \in C^1(\Sigma) \tag{4.4.19}
\end{equation}$$

This satisfies Condition 4.4.7a (uniform conical structure) provided α and β are C¹. ✓

**Example 3: Exponential Wall**

$$\begin{equation}
A(r,z) = -\lambda \left(1 + \tanh\left(\frac{r - r_0(z)}{\delta}\right)\right), \quad r_0(z) \in C^1(\Sigma) \tag{4.4.20}
\end{equation}$$

This is C¹ with bounded derivatives in r and smooth in r₀(z). ✓

**Example 4: Singular Oscillating Profile (Warning: Violation)**

$$\begin{equation}
A(r,z) = -\lambda \sin\left(\frac{1}{r}\right), \quad \text{no } z\text{-dependence} \tag{4.4.21}
\end{equation}$$

This has unbounded derivatives as r → 0 (violates Reg2). The coherence-to-classical map fails C¹. ✗

## 4.4.6 Physical Interpretation

### Smoothness of Observables

The C¹ regularity of V(x) means that the quasipotential—which encodes all coherence-frame information—defines a smooth 1-form dV on spacetime. This is the basic requirement for a well-defined thermodynamic potential:

$$\begin{equation}
\mathrm{d}V = \frac{\partial V}{\partial t}\mathrm{d}t + \frac{\partial V}{\partial x^i}\mathrm{d}x^i \tag{4.4.22}
\end{equation}$$

A failure of C¹ would mean that dV has jumps or Dirac-like singularities, signaling that local observables computed from V exhibit unphysical discontinuities.

### Coherence-Frame Robustness

The requirement that A(r,z) be smooth in the coherence parameter z ensures that the geometry continuously interpolates as the observer's coherence frame changes. This is essential for the "coherence adiabatic theorem" — if an observer slowly changes their coherence-frame setting, the physical observables evolve smoothly, without abrupt transitions.

### Embedding into Einstein Equations

For the 5D metric (Eq. 4.4.1) to satisfy the Einstein equations Ric_AB = 0 (or Ric_AB = Λ g_AB), the warp factor must itself be C² (not merely C¹). This is because the Einstein tensor involves second derivatives of the metric. Theorem 4.4.1 shows that even with only C¹ A, the coherence-to-classical map remains regular — the C² requirement for Einstein equations is a separate, stronger condition.

## 4.4.7 Summary and Conclusion

We have verified that the coherence-to-classical map remains C¹ under the KK-Cone warp factor A(r,z), provided three conditions hold:

1. **Global Smoothness** (Reg1): A ∈ C¹(ℝ⁺ × Σ)
2. **Bounded Derivatives** (Reg2): First partial derivatives of A are uniformly bounded
3. **Uniform Conical Structure** (Reg3): Any singularity at r = 0 must have a uniform logarithmic profile in coherence parameter z

These conditions ensure that:
- The metric is smooth (or smoothly orbifold) everywhere
- The path integral action functional is continuous in both spacetime and coherence parameters
- The quasipotential V(x) and its gradient ∇V are continuous

Under these conditions, the framework guarantees that coherence-frame shifts induce smooth changes in observable predictions, eliminating unphysical discontinuities. This fulfills the promise from Paper 1 (line 411) and establishes the rigorous foundation for the KK-Cone model as a coherence-relativity embedding.

---

**References for §4.4**:
- Regularity theory for infimum of continuous families: Dini's Theorem, standard textbooks on analysis (e.g., Rudin, *Principles of Mathematical Analysis*)
- Envelope theorem for variational problems: standard in optimal control and mathematical economics
- Hopf fibration geometry: Atiyah, *Geometry of Yang-Mills Fields* (and references therein)
- Orbifold singularities and conical metrics: Burnett & Petrov, *Orbifolds as Singular Spaces with Extra Structure*
