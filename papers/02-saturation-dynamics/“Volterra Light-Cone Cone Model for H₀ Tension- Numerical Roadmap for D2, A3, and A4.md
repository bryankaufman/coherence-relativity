This is a very clean critical path; you’re basically one numerical confirmation (item 1) away from having a falsifiable toy model for D2 and a GR-consistent story for A3/A4.

### 1. γ·S regularization at r → c/H₀

I would treat this as the immediate next task: discretize r on a logarithmically crowded grid (e.g. r = 0.1, 0.2, … in units of c/H₀, then 0.9, 0.95, 0.98, 0.99, 0.995, …) and evaluate γ(r)·S(r,T) at fixed T up to r = (1 − ε)c/H₀ with ε down to at least 10⁻⁶. Plot: [en.wikipedia](https://en.wikipedia.org/wiki/Volterra_integral_equation)

- γ(r)·S(r,T) vs r  
- log|γ(r)·S(r,T) − 1| vs log(1 − rH₀/c)

If S is truly 1/γ algebraically at the horizon, you’ll see the product tend to exactly constant; if causal suppression only approximately cancels, you should still see bounded approach rather than oscillatory blow‑up. Numerically, I’d consider it “physically safe” if the product stays within a few percent of a finite limit for ε ≳ 10⁻⁴ and doesn’t show wild oscillations at smaller ε. [en.wikipedia](https://en.wikipedia.org/wiki/Volterra_integral_equation)

### 2. Making K(T,T′) concrete

For the Volterra structure to actually *do* anything you need K explicitly for at least two scale factors. [ui.adsabs.harvard](https://ui.adsabs.harvard.edu/abs/2010AIPC.1309...33E/abstract)

- Radiation era: \(a(t) \propto t^{1/2}\) → comoving distance and null geodesics give you α(T) directly. [jila.colorado](https://jila.colorado.edu/~ajsh/astr3740_14/flrw.pdf)
- Matter era: \(a(t) \propto t^{2/3}\) → same, but with different power in the radial null integral.

Once you have α(T), defining  
\(K(T,T') = \partial_T[\alpha(T) - \alpha(T')]\)  
and checking that \(K \in L^2([0,T]\times[0,T])\) is enough to guarantee uniqueness for the Volterra equation of the second kind, so long as your norm is under control. I’d write this out symbolically for each a(t) and explicitly check square‑integrability at the endpoints. [ui.adsabs.harvard](https://ui.adsabs.harvard.edu/abs/2010AIPC.1309...33E/abstract)

### 3. First iteration ψ⁽¹⁾ vs ψ⁽⁰⁾

With K in hand, the first correction

\[
\psi^{(1)}(T) = \int_0^T K(T,T')\,\psi^{(0)}(T')\,dT'
\]

is just a quadrature on the same grid you used to define K. Here the key diagnostic is the dimen dimensionless ratio |ψ⁽¹⁾/ψ⁽⁰⁾| as a function of T:

- If it stays ≪ 1 over the relevant range, you’re in a perturbative regime and the Volterra machinery is behaving like a small geometric correction.  
- If it naturally grows to ≈ 0.05–0.15 by the lookback time corresponding to the CMB, you are squarely in the “H₀ tension” window without needing to tune extra physics. [arxiv](https://arxiv.org/pdf/2302.05709.pdf)

I’d compute |ψ⁽¹⁾/ψ⁽⁰⁾| at:  
- “local ladder” scales (T corresponding to z ≲ 0.1)  
- the sound horizon / last scattering (z ≈ 1100).

### 4. Geometric prediction for H₀ tension (D2)

Once you trust K and ψ⁽¹⁾, define two effective Hubble parameters from the same underlying model:

- H₀,local from a low‑T expansion (essentially truncating the Volterra series after the first correction).  
- H₀,CMB from the full cone integral out to the last scattering surface. [imperial.ac](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/theoretical-physics/msc/dissertations/2021/Linda-Yuan-Dissertation.pdf)

You can implement this in one script that:

1. Solves the Volterra equation numerically for ψ(T) with your chosen a(t).  
2. Fits the small‑T distance–redshift relation to extract H₀,local.  
3. Uses the full ψ(T) to infer the angular diameter distance to last scattering and hence H₀,CMB in the “CMB‑style” way. [imperial.ac](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/theoretical-physics/msc/dissertations/2021/Linda-Yuan-Dissertation.pdf)

If H₀,local/H₀,CMB lands near 1.07–1.10 (roughly 73/67) without perverse choices of parameters, that’s a direct, falsifiable geometric candidate for the observed H₀ split. If it stubbornly stays ≈1, that’s equally informative: the cone geometry alone won’t buy you enough effect. [arxiv](https://arxiv.org/pdf/2302.05709.pdf)

### 5. A3: Past light cone as Penrose surface of K³ cone

For A3 you basically want to prove that null geodesics in your cone metric

\[
ds^2 = -dT^2 + T^2 d\Omega^2
\]

trace the same causal boundary as FLRW past light cones when appropriately embedded. [phys.libretexts](https://phys.libretexts.org/Bookshelves/Relativity/General_Relativity_(Crowell)/07:_Symmetries/7.03:_Penrose_Diagrams_and_Causality)

Plan:

- Write the radial null condition in FLRW (k=0): \(ds^2 = 0 \Rightarrow c\,dt/a(t) = \pm dr\). [jila.colorado](https://jila.colorado.edu/~ajsh/astr3740_14/flrw.pdf)
- Write the null condition in the cone metric and parameterize the radial coordinate in terms of T and angle α(T).  
- Show that with your α(T)–a(t) identification, the null cones coincide as sets, so the past light cone of an observer at (T_obs, r=0) in the cone metric maps exactly to the usual Penrose past light cone surface of the same FLRW observer. [en.wikipedia](https://en.wikipedia.org/wiki/Penrose_diagram)

If that check goes through, then taking the redshift sum over that Penrose surface is just a coordinate re‑expression of the standard light cone integral, and A3 is automatically satisfied.

### 6. A4: FLRW as the small‑angle cone limit

Here the target is: in the limit of slowly varying, small cone angle, your effective metric reduces to a flat‑k Robertson–Walker metric. [damtp.cam.ac](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html)

- Write the full cone metric in terms of α(T) and whatever radial coordinate you’re using on K³.  
- Expand for small deviations δα(T) around a constant angle (nearly flat cone).  
- Show that the induced spatial 3‑metric on T = const slices is conformally flat with scale factor a(T) related to α(T); the leading term in that expansion should match the k=0 FLRW metric. [damtp.cam.ac](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html)

Conceptually, you want an argument parallel to “Minkowski as large‑r Schwarzschild”: at zeroth order you get standard FLRW, with your cone corrections appearing as higher‑order terms in a small parameter like dα/dT.

### Suggested execution order and time boxing

Your ordering 1→2→3→4, then 5 and 6 in parallel, is exactly right.

Concrete way to time‑box:

- Day 1:  
  - Get γ·S(r,T) plots and asymptotics near r = c/H₀.  
  - Draft analytic expressions for α(T) and K(T,T′) in radiation and matter eras.

- Day 2:  
  - Implement numerical ψ⁽¹⁾ for both a(t) choices; scan |ψ⁽¹⁾/ψ⁽⁰⁾| vs T.  
  - If promising, bolt on the H₀ extractor (local vs CMB‑like) and get a first pass on H₀,local/H₀,CMB.

- Next week:  
  - In parallel, work through the short GR calculations for A3 (null cones) and A4 (small‑angle limit) using standard FLRW + Penrose diagram machinery. [phys.libretexts](https://phys.libretexts.org/Bookshelves/Relativity/General_Relativity_(Crowell)/07:_Symmetries/7.03:_Penrose_Diagrams_and_Causality)

If you want, I can help you next with either (a) specifying the exact numerical grid and diagnostics for item 1, or (b) symbolically deriving α(T) and K(T,T′) for a(t) ∝ t^{2/3} as a starting point.