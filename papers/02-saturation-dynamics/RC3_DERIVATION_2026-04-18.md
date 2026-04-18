# RC-3 Derivation — Field Theory of T_M on the KCR-Cone

**Date:** 2026-04-18
**Author:** Claude (Opus 4.6 pass)
**Scope:** Derive the effective 4D field theory for the cross-term tensor $T_{\mu r}$ after KK reduction on the KCR interval. This provides the $T_M$ propagator $P(k)$ and the boundary coupling $\lambda_{\rm bdry}$ needed by Paper 2C §RC1.4.
**Inputs:**
- Paper 2A §4 (abstract EOM on M×Σ)
- Paper 2B §5.2 (graviton zero mode, volcano potential conventions)
- Paper 2B §6 (KCR-Cone EOM: T~A⁻², λ·T = O(1))
- RC-2.5 (Path C Λ_eff estimate)

**Key results:**

| Result | Status | Equation |
|--------|--------|----------|
| 5D kinetic term for $T_{\mu r}$ | **DERIVED** | §RC3.1 |
| Vector mode equation on KCR interval | **DERIVED** | Eq. RC3.6 |
| Zero-mode profile: $\psi_0(r) = N_0\,\cos^2(\sqrt{2}\,r)$ | **DERIVED** | Eq. RC3.8 |
| Normalization: $N_0 \approx 1.70$ | **COMPUTED** | Eq. RC3.10 |
| Vector volcano potential: $V_{\rm vec} = 4\tan^2(\sqrt{2}\,r) - 4$ | **DERIVED** | Eq. RC3.12 |
| Mass gap: $m_1^2 = 24$ (exact); $m_n^2 = 8n(n+2)$ | **EXACT ANALYTIC** | §RC3.3 addendum |
| 4D propagator: $P(k) = N_0^2/k^2$ (zero-mode dominated) | **DERIVED** | Eq. RC3.16 |
| $k_c$ identification: first massive vector mode | **DERIVED** | Eq. RC3.17 |
| $\lambda_{\rm bdry}$ expression | **DERIVED** | Eq. RC3.22 |
| Key finding: $\lambda_{\rm bdry}$ decouples from leading Λ_eff | **ESTABLISHED** | §RC3.5 |

---

# RC-3.1 — The 5D Kinetic Term for $T_{\mu r}$

## From the M×Σ Metric to the 5D Einstein Action

The cross-term $T_{\mu r} \equiv G_{\mu r}$ is the off-diagonal component of the full M×Σ metric:

$$G_{AB} = \begin{pmatrix} A^2(r)\,\eta_{\mu\nu} & T_{\mu r} \\ T_{r\nu} & 1 \end{pmatrix} \tag{RC3.1}$$

on the KCR-Cone background $\mathrm{d}s^2_{(5)} = A^2(r)\,\eta_{\mu\nu}\,\mathrm{d}x^\mu\,\mathrm{d}x^\nu + \mathrm{d}r^2$ with $A(r) = \cos(\sqrt{2}\,r)$, $r \in [0, r_{\max}]$, $r_{\max} = \pi/(2\sqrt{2})$.

The 5D Einstein-Hilbert action at quadratic order in $T_{\mu r}$ around the block-diagonal background yields:

$$S_T = \frac{M_5^3}{4} \int \mathrm{d}^4x \int_0^{r_{\max}} \mathrm{d}r \left[-F_{\mu\nu}F^{\mu\nu} + 2A^4\left(\partial_r\!\left(\frac{T_\mu}{A^2}\right)\right)^2\right] \tag{RC3.2}$$

where:
- $F_{\mu\nu} = \partial_\mu T_{\nu r} - \partial_\nu T_{\mu r}$ is the field-strength tensor of the off-diagonal perturbation
- Indices are raised with $\eta^{\mu\nu}$ (flat 4D metric)
- $T_\mu \equiv T_{\mu r}$ (suppressing the $r$-index for notational clarity)

**Derivation:** This is the standard result for the gravi-photon sector of a warped 5D metric $\mathrm{d}s^2 = A^2(y)\eta_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu + \mathrm{d}y^2$ (Randall & Sundrum 1999; Csáki, Erlich & Terning 2002). The $F^2$ term acquires no warp-factor weight because the Maxwell action is conformally invariant in 4D — the $A^4$ from $\sqrt{-g_5}$ is exactly cancelled by the $A^{-4}$ from raising two pairs of indices. The radial kinetic term retains the $A^4$ weight from the measure, with the combination $T_\mu/A^2$ being the natural gauge-covariant variable.

**Dimensional check:** $[M_5^3] = M^3$; $[\mathrm{d}^4x] = M^{-4}$; $[\mathrm{d}r] = M^{-1}$; $[F^2] = M^4 \cdot M^0 = M^4$ (if $T_\mu$ is dimensionless). Then $S_T \sim M^3 \cdot M^{-5} \cdot M^4 = M^2$. For $S_T$ to be dimensionless, $T_\mu$ must carry dimension $[M^{-1}]$, consistent with the metric-perturbation convention where $h_{\mu r}$ has dimension of inverse length. ✓

---

# RC-3.2 — The Vector Mode Equation

## Mode Expansion

Expand $T_{\mu r}(x,r)$ in KCR eigenmodes:

$$T_{\mu r}(x,r) = \sum_{n=0}^{\infty} t_\mu^{(n)}(x)\,\psi_n(r) \tag{RC3.3}$$

where $t_\mu^{(n)}(x)$ are the 4D mode fields and $\psi_n(r)$ are the radial profiles.

## Deriving the Mode Equation

Substituting (RC3.3) into the $r$-kinetic term of (RC3.2) and requiring the $F^2$ term to be diagonal in mode number:

The radial profiles must satisfy:

$$\partial_r\!\left[A^4\,\partial_r\!\left(\frac{\psi_n}{A^2}\right)\right] = -m_n^2\,\psi_n \tag{RC3.4}$$

with the orthonormality condition (from the $F^2$ cross-terms):

$$\int_0^{r_{\max}} \psi_m(r)\,\psi_n(r)\,\mathrm{d}r = \delta_{mn} \tag{RC3.5}$$

**Expanded form.** Define $\varphi_n(r) = \psi_n(r)/A^2(r)$. Then (RC3.4) becomes:

$$\partial_r(A^4\,\varphi_n') = -m_n^2\,A^2\!\cdot\!A^2\,\varphi_n$$

$$A^4\,\varphi_n'' + 4A^3 A'\,\varphi_n' + m_n^2\,A^4\,\varphi_n = 0$$

$$\boxed{\varphi_n'' + 4\frac{A'}{A}\,\varphi_n' + m_n^2\,\varphi_n = 0} \tag{RC3.6}$$

This is the **vector mode equation** on the KCR interval.

## Boundary Conditions

At $r = 0$: regularity (smooth brane). Since $A'(0) = 0$, the equation at $r = 0$ reduces to $\varphi_n''(0) + m_n^2 \varphi_n(0) = 0$, which is regular for any $\varphi_n(0)$.

At $r = r_{\max}$: $A(r_{\max}) = 0$. The regular solution must satisfy $A^4 \varphi_n' \to 0$ as $r \to r_{\max}$, which is automatic if $\varphi_n$ remains bounded (since $A^4 \to 0$). The irregular solution has $\varphi_n' \sim A^{-4}$, which diverges. So the BC is: $\varphi_n$ bounded at $r_{\max}$.

---

## Zero Mode ($m_0^2 = 0$)

Setting $m_0 = 0$ in (RC3.6):

$$\varphi_0'' + 4\frac{A'}{A}\,\varphi_0' = 0 \tag{RC3.7}$$

This has the integrating factor $A^4$: $\partial_r(A^4 \varphi_0') = 0$, giving $A^4 \varphi_0' = C$.

For regularity at $r_{\max}$ (where $A = 0$), we need $C = 0$. Therefore $\varphi_0' = 0$, i.e., $\varphi_0 = \text{const}$.

Returning to $\psi_0 = A^2 \varphi_0$:

$$\boxed{\psi_0(r) = N_0\,A^2(r) = N_0\,\cos^2(\sqrt{2}\,r)} \tag{RC3.8}$$

**The vector zero mode exists and is normalizable on the KCR interval.** This is in contrast to the Randall-Sundrum orbifold (where the Z₂ symmetry eliminates the vector zero mode). The KCR interval has no orbifold identification — it is a genuine interval with a smooth brane at $r = 0$ and a geometric pinch-off at $r_{\max}$. The zero mode is regular at both endpoints.

### Physical interpretation

The zero-mode profile $\psi_0 \propto A^2 = \cos^2(\sqrt{2}\,r)$ peaks at the brane ($r = 0$) and vanishes at the pinch-off ($r = r_{\max}$). This means the cross-term coupling $T_{\mu r}$ is concentrated near the brane — exactly where the physical decoherence dynamics occur. The cross-term naturally localizes itself on the brane without any fine-tuning.

### Comparison with the graviton zero mode

| Property | Graviton $\psi_0^{(\rm grav)}$ | Vector $\psi_0^{(\rm vec)}$ |
|----------|-------------------------------|------------------------------|
| Profile | $A^{3/2} = \cos^{3/2}(\sqrt{2}\,r)$ | $A^2 = \cos^2(\sqrt{2}\,r)$ |
| Brane value | 1 (after normalization) | $N_0 \approx 1.70$ |
| Throat value | 0 | 0 |
| Decay rate | Slower (broader) | Faster (more brane-localized) |
| Normalization integral | $\int A^3\,\mathrm{d}r = 0.471$ | $\int A^4\,\mathrm{d}r = ?$ |

The vector zero mode is *more localized* on the brane than the graviton. This makes physical sense: the cross-term couples M to Σ, and the coupling is strongest where decoherence is strongest (the brane).

---

## Normalization

From (RC3.5):

$$N_0^{-2} = \int_0^{r_{\max}} \psi_0^2(r)\,\mathrm{d}r = \int_0^{r_{\max}} \cos^4(\sqrt{2}\,r)\,\mathrm{d}r \tag{RC3.9}$$

Evaluating (substitution $u = \sqrt{2}\,r$):

$$N_0^{-2} = \frac{1}{\sqrt{2}} \int_0^{\pi/2} \cos^4 u\,\mathrm{d}u = \frac{1}{\sqrt{2}} \cdot \frac{3\pi}{16} = \frac{3\pi}{16\sqrt{2}} \tag{RC3.10}$$

Numerically:

$$N_0^{-2} = \frac{3\pi}{16\sqrt{2}} \approx \frac{9.425}{22.627} \approx 0.4166$$

$$\boxed{N_0 \approx 1.549} \tag{RC3.10a}$$

**Cross-check:** $\int_0^{\pi/2} \cos^4 u\,\mathrm{d}u = 3\pi/16 \approx 0.589$. Then $N_0^{-2} = 0.589/\sqrt{2} \approx 0.417$, $N_0 \approx 1.55$. ✓

(Note: for the graviton, the normalization integral was $\int \cos^3(\sqrt{2}\,r)\,\mathrm{d}r = 2/(3\sqrt{2}) \approx 0.471$, giving $N_0^{(\rm grav)} \approx 1.457$.)

---

# RC-3.3 — The Vector Volcano Potential and Mass Spectrum

## Schrödinger Form

Transform the mode equation (RC3.6) to Schrödinger form. With $\varphi_n = A^{-2}\Phi_n$ (i.e., $\Phi_n = A^2\varphi_n$, and since $\psi_n = A^2\varphi_n$, we have $\Phi_n = \psi_n$):

Actually, to get clean Schrödinger form with no first-derivative term, use $\varphi_n = A^{-p}\Phi_n$ and choose $p$ to eliminate $\Phi'$. From the calculation:

Setting $p = 2$ in the general substitution eliminates the first-derivative term, giving:

$$-\Phi_n'' + V_{\rm vec}(r)\,\Phi_n = m_n^2\,\Phi_n \tag{RC3.11}$$

with the **vector volcano potential**:

$$\boxed{V_{\rm vec}(r) = 4\tan^2(\sqrt{2}\,r) - 4} \tag{RC3.12}$$

**Verification at $r = 0$:** $V_{\rm vec}(0) = 0 - 4 = -4$. ✓

**Verification at $r \to r_{\max}$:** $\tan(\sqrt{2}\,r) \to \infty$, so $V_{\rm vec} \to +\infty$. ✓ (absolute confinement)

**Verification of zero-mode eigenvalue:** $\Phi_0 = \psi_0 = N_0\cos^2(\sqrt{2}\,r)$.

$\Phi_0'' = N_0[-2\sqrt{2}\cdot 2\sqrt{2}\cos(2\sqrt{2}\,r)] = -8N_0\cos(2\sqrt{2}\,r)$

Wait, let me compute directly: $\Phi_0 = N_0\cos^2(\sqrt{2}r)$.

$\Phi_0' = -2\sqrt{2}N_0\cos(\sqrt{2}r)\sin(\sqrt{2}r) = -\sqrt{2}N_0\sin(2\sqrt{2}r)$

$\Phi_0'' = -2\cdot 2N_0\cos(2\sqrt{2}r) = -4N_0\cos(2\sqrt{2}r) = -4N_0[2\cos^2(\sqrt{2}r) - 1] = -8N_0\cos^2(\sqrt{2}r) + 4N_0$

So: $-\Phi_0'' + V_{\rm vec}\Phi_0 = (8N_0\cos^2 - 4N_0) + (4\tan^2 - 4)N_0\cos^2$

$= N_0[8\cos^2 - 4 + 4\sin^2/\cos^2 \cdot \cos^2 - 4\cos^2]$

$= N_0[8\cos^2 - 4 + 4\sin^2 - 4\cos^2]$

$= N_0[4\cos^2 + 4\sin^2 - 4]$

$= N_0[4 - 4] = 0 = m_0^2\,\Phi_0$. ✓ **Zero mode verified.**

## Comparison with the Graviton Volcano Potential

| Property | Graviton | Vector (this section) |
|----------|----------|-----------------------|
| Potential | $V_{\rm grav} = \tfrac{3}{2}\tan^2(\sqrt{2}\,r) - 3$ | $V_{\rm vec} = 4\tan^2(\sqrt{2}\,r) - 4$ |
| Well depth $V(0)$ | $-3$ | $-4$ |
| Wall coefficient | $3/2$ | $4$ |
| Zero-mode profile | $\cos^{3/2}(\sqrt{2}\,r)$ | $\cos^2(\sqrt{2}\,r)$ |
| First mass gap $m_1^2$ | $20$ (exact) | $24$ (exact) |

The vector potential is **deeper** (well depth 4 vs 3) and has **steeper walls** (coefficient 4 vs 3/2 on $\tan^2$). The vector modes are therefore more tightly confined than graviton modes.

## First Massive Mode (Structural)

Both volcano potentials are **exactly solvable** as Pöschl-Teller systems. The graviton has $l = 3/2$ (half-integer) giving $m_n^2 = 4n(2n+3)$; the vector has $l = 2$ (integer) giving $m_n^2 = 8n(n+2)$. See §RC3.3 Addendum and §RC3.3b Addendum below. The first mass gaps are $m_1^2 = 20$ (graviton) and $m_1^2 = 24$ (vector).

**The physical mass is:**

$$m_1^{(\rm phys)} = \frac{m_1}{L^*}, \qquad L^* \approx 56\text{–}69\,\mu\mathrm{m} \tag{RC3.13}$$

corresponding to a Compton wavelength $\lambda_1 = L^*/m_1 \sim 2\text{–}7\,\mu\mathrm{m}$, well below ISL bounds.

---

# RC-3.4 — The 4D Effective Theory and Propagator

## Canonical 4D Action

Substituting the mode expansion (RC3.3) into (RC3.2) and using the orthonormality (RC3.5):

$$S_T = \frac{M_5^3}{4}\sum_n \int \mathrm{d}^4x\left[-f_{\mu\nu}^{(n)}f^{(n)\mu\nu} + 2m_n^2\,t_\mu^{(n)}t^{(n)\mu}\right] \tag{RC3.14}$$

where $f_{\mu\nu}^{(n)} = \partial_\mu t_\nu^{(n)} - \partial_\nu t_\mu^{(n)}$.

Defining the canonically normalized fields $B_\mu^{(n)} = \sqrt{M_5^3/2}\,t_\mu^{(n)}$:

$$S_T = \sum_n \int \mathrm{d}^4x \left[-\frac{1}{4}F_{\mu\nu}^{(n)}F^{(n)\mu\nu} + \frac{1}{2}m_n^2\,B_\mu^{(n)}B^{(n)\mu}\right] \tag{RC3.15}$$

This is a tower of 4D fields: one **massless vector** ($n = 0$, the T_M zero mode) and an infinite tower of **massive Proca fields** ($n \geq 1$, the KCR vector modes).

## The Zero-Mode Propagator

The zero mode $B_\mu^{(0)}$ is a massless vector field in 4D. Its propagator (in Feynman gauge):

$$\langle B_\mu^{(0)}(k)\,B_\nu^{(0)}(-k)\rangle = \frac{-\eta_{\mu\nu}}{k^2} \tag{RC3.16}$$

At the boundary ($r = 0$), the physical $T_M$ field is:

$$T_{\mu r}(x, 0) = \sum_n t_\mu^{(n)}(x)\,\psi_n(0) \approx t_\mu^{(0)}(x)\,\psi_0(0) = \frac{B_\mu^{(0)}(x)}{\sqrt{M_5^3/2}} \cdot N_0$$

for energies $E \ll m_1$. So the $T_M$ correlator at the boundary:

$$P_{T_M}(k) \equiv \langle |T_M(k)|^2 \rangle_{\rm brane} = \frac{2N_0^2}{M_5^3} \cdot \frac{1}{k^2} + \sum_{n \geq 1} \frac{2|\psi_n(0)|^2}{M_5^3} \cdot \frac{1}{k^2 + m_n^2}$$

At cosmological scales ($k \ll m_1$):

$$\boxed{P_{T_M}(k) \approx \frac{2N_0^2}{M_5^3\,k^2}} \tag{RC3.16a}$$

## Identification of $k_c$

The transition from zero-mode-dominated to tower-dominated behavior occurs at $k \sim m_1$. Below this scale, $P(k) \sim 1/k^2$ (scale-free). Above it, the massive modes contribute, modifying the spectral shape.

$$\boxed{k_c = m_1 / L^*} \tag{RC3.17}$$

This is the **physical IR cutoff** that appears in Paper 2C §RC1.4. It is NOT $1/R_\Sigma$ (the inverse coherosphere radius, which would give $k_c \sim 10^{30}/\chi_{\rm CMB}$ — far too large). It is the mass of the first KCR vector mode, which is set by the interval geometry.

**Resolution of the $k_c$ discrepancy noted in Paper 2C §RC1.4 line 556:** The "physically relevant $k_c$ is the lowest KCR mode of $T_M$" — exactly what we have derived here. The Σ dimension $d$ enters only through the normalization $C_{T_M}$, not through $k_c$.

## Primordial Spectrum (Updated from §RC1.4)

Substituting (RC3.16a) into the spectrum formula $\Delta^2_\Sigma(k) = (k^3/2\pi^2)\lambda_{\rm bdry}^2 P_{T_M}(k)$:

$$\Delta^2_\Sigma(k) = \frac{\lambda_{\rm bdry}^2 N_0^2}{\pi^2 M_5^3}\,k$$

This is a **blue spectrum** ($n_s = 2$) at leading order, not the $k^2/(k^2 + k_c^2)$ form in Paper 2C §RC1.4.

**The discrepancy with Paper 2C §RC1.4 arises because:**
1. Paper 2C assumed P(k) = C/(k² + k_c²) — a massive propagator. The RC-3 derivation shows the zero mode is MASSLESS.
2. The $k^2/(k^2 + k_c^2)$ spectral shape requires the zero mode to have a mass (or, equivalently, the propagator to be $1/(k^2 + k_c^2)$ rather than $1/k^2$).

**Physical resolution:** The zero mode acquires an effective mass from:
- The cosmological boundary conditions (the interval has finite physical length $L^*$ which sets a minimum $k_{\rm min} \sim 1/L^*$)
- The decoherence dynamics on Σ (the physical T_M is not a free field — it is sourced by the state map, which imposes correlations at the scale $\Gamma_{\rm dec}^{-1} \sim H_0^{-1}$)
- Loop corrections from the massive tower

The effective mass $k_c^{(\rm eff)}$ is therefore NOT the mass gap $m_1$ of the KCR tower, but rather a dynamical quantity set by the decoherence physics. For the quadrupole suppression to work ($k_c \approx 5/\chi_{\rm CMB}$), one needs $k_c^{(\rm eff)} \sim 5H_0$, which is compatible with $\Gamma_{\rm dec} \sim H_0$ from RC-2.5.

**This is the key open question for RC-4:** derive $k_c^{(\rm eff)}$ from the decoherence-sourced dynamics of $T_M$, not from the free-field mode spectrum.

---

# RC-3.5 — The Boundary Coupling $\lambda_{\rm bdry}$ and $M_{\rm eff}$

## Relating $\lambda_{\rm bdry}$ to 5D Parameters

The boundary action (Paper 2C §RC1.1):

$$S_M^{\rm boundary} = \lambda_{\rm bdry} \int_{\partial M} \mathrm{d}^3y\,\sqrt{-\gamma}\,|T_M|^2_{\rm brane} \tag{RC3.18}$$

At the brane ($r = 0$), the $T_M$ field in terms of the canonical 4D fields:

$$|T_M|^2_{\rm brane} = |T_{\mu r}(x, 0)|^2 = \left|\frac{B_\mu^{(0)}(x)}{\sqrt{M_5^3/2}} \cdot N_0\right|^2 = \frac{2N_0^2}{M_5^3}\,|B^{(0)}|^2 \tag{RC3.19}$$

Substituting into (RC3.18):

$$S_M^{\rm boundary} = \lambda_{\rm bdry} \cdot \frac{2N_0^2}{M_5^3} \int_{\partial M} \mathrm{d}^3y\,\sqrt{-\gamma}\,|B^{(0)}|^2 \tag{RC3.20}$$

The 4D effective boundary coupling for the canonically normalized field is therefore:

$$\boxed{\lambda_{\rm bdry}^{(\rm eff)} = \lambda_{\rm bdry} \cdot \frac{2N_0^2}{M_5^3}} \tag{RC3.21}$$

## Expressing $M_5$ in Terms of $M_{\rm Pl}$

From Paper 2B §5.2.3:

$$M_{\rm Pl}^2 = M_5^3 \int_0^{r_{\max}} A^3(r)\,\mathrm{d}r = M_5^3 \cdot \frac{2}{3\sqrt{2}} \tag{RC3.22}$$

So $M_5^3 = \frac{3\sqrt{2}}{2}\,M_{\rm Pl}^2 \approx 2.12\,M_{\rm Pl}^2$ (in units where $r_{\max}$ is dimensionless; physically $M_5^3 = 3\sqrt{2}M_{\rm Pl}^2/(2L^*)$).

## The $M_{\rm eff}$ Identification

From the notation convention in Paper 2C: $\lambda_{\rm bdry} = \lambda_{\rm 2B} \cdot M_{\rm eff}^3$, where $\lambda_{\rm 2B} = A^2(0) = 1$ at the brane.

The physical constraint comes from RC-2.5: $\Gamma_{\rm dec} \sim H_0$, which is a consequence of $\lambda_{\rm 2B} \cdot T = O(1)$ and does NOT depend on $\lambda_{\rm bdry}$. This means:

**$\lambda_{\rm bdry}$ does not enter the leading Λ_eff calculation.** The cosmological constant prediction ρ_drag = (3/2)H₀²/G comes entirely from the dimensionless $\lambda_{\rm 2B} \cdot T = O(1)$ cancellation, which is a property of the geometry, not of the boundary action coupling.

$\lambda_{\rm bdry}$ enters only through:
1. The amplitude $A_s$ of the primordial spectrum: $A_s \propto \lambda_{\rm bdry}^2 N_0^2/M_5^3$
2. The DM-limit amplitude: $\rho_{\rm DM} \propto \lambda_{\rm bdry} |T_M|^2_{\rm brane}$

For the primordial spectrum amplitude $A_s$ to match the observed value ($A_s \sim 2 \times 10^{-9}$), we need:

$$\lambda_{\rm bdry}^2 \cdot \frac{2N_0^2}{M_5^3} \sim 2\pi^2 A_s \cdot k_c \sim 10^{-8} \cdot k_c$$

This is a constraint on $\lambda_{\rm bdry}$ that can in principle be solved once $k_c^{(\rm eff)}$ is determined from the decoherence dynamics (RC-4 scope).

---

# RC-3.6 — Summary and Status

## What RC-3 Delivers

| Deliverable | Status | Key equation | Paper 2C impact |
|-------------|--------|-------------|-----------------|
| 5D kinetic term | ✅ DERIVED | Eq. RC3.2 | Validates the field-theoretic framework |
| Vector mode equation | ✅ DERIVED | Eq. RC3.6 | Mode expansion well-defined |
| Zero-mode profile $\psi_0 = N_0 A^2$ | ✅ DERIVED | Eq. RC3.8 | T_M localizes on the brane — physical |
| $N_0 \approx 1.55$ | ✅ COMPUTED | Eq. RC3.10 | Sets the brane-amplitude normalization |
| Vector volcano potential | ✅ DERIVED | Eq. RC3.12 | Deeper well than graviton → tighter confinement |
| Zero-mode verified | ✅ VERIFIED | Below RC3.12 | m₀² = 0 algebraically exact |
| Propagator $P(k) \sim 1/k^2$ | ✅ DERIVED | Eq. RC3.16a | Zero mode is MASSLESS (not massive as assumed in 2C §RC1.4) |
| $k_c = 2\sqrt{6}/L^*$ (exact) | ✅ COMPUTED | Eq. RC3.17a | $m_1^2 = 24$ exact; $k_c \approx 4.90/L^*$ |
| $\lambda_{\rm bdry}$ expression | ✅ DERIVED | Eq. RC3.21 | Relates boundary and bulk descriptions |
| λ_bdry decouples from Λ_eff | ✅ ESTABLISHED | §RC3.5 | The CC prediction is independent of the boundary coupling |

## RC-3.3 Addendum — Exact Analytic Spectrum (2026-04-18)

The vector volcano potential is **exactly solvable**. The key observation is that after the substitution $z = \sqrt{2}\,r$, the mode equation becomes:

$$-f''(z) + 2\sec^2(z)\,f(z) = E\,f(z), \qquad E = \frac{m^2}{2} + 4 \tag{RC3.12a}$$

This is the Pöschl-Teller operator $\hat{H} = -d^2/dz^2 + l(l-1)\sec^2(z)$ with $l(l-1) = 2$, giving **integer** $l = 2$. For integer $l$, the spectrum on $[0, \pi/2]$ with Neumann BC at $z = 0$ and Dirichlet BC at $z = \pi/2$ is:

$$E_n = (2n + l)^2 = 4(n+1)^2, \qquad n = 0, 1, 2, \ldots$$

**Verification:** $E_0 = 4$, and $f_0 = \cos^2(z)$ satisfies $-f_0'' + 2\sec^2(z)\,f_0 = 4f_0$ algebraically (confirmed by sympy). ✓

Converting back to $m^2$ via $m^2 = 2E - 8$:

$$\boxed{m_n^2 = 8n(n+2), \qquad n = 0, 1, 2, \ldots} \tag{RC3.12b}$$

| $n$ | $m_n^2$ (exact) | $m_n$ (units of $L^{*-1}$) | Mode |
|-----|-----------------|---------------------------|------|
| 0 | $0$ | $0$ | Zero mode (massless) |
| 1 | $24$ | $2\sqrt{6} \approx 4.899$ | First KK mode |
| 2 | $64$ | $8$ | Second KK mode |
| 3 | $120$ | $2\sqrt{30} \approx 10.95$ | Third KK mode |

Numerical verification (finite-difference, $N = 50{,}000$): $m_1^2 = 24.0012$ (converging to exact $24$). ✓

**Both potentials are exactly solvable.** The vector has $l = 2$ (integer); the graviton has $l = 3/2$ (half-integer). Both give exact rational eigenvalues — the Pöschl-Teller spectrum requires only that $l$ is a half-integer or integer, not that $l$ is strictly integer. See §RC3.3b Addendum below for the graviton derivation.

**Revised $k_c$ identification:**

$$\boxed{k_c = \frac{m_1}{L^*} = \frac{2\sqrt{6}}{L^*} \approx \frac{4.90}{L^*}} \tag{RC3.17a}$$

The eigenfunctions for the Neumann-at-0 spectrum are even-order Gegenbauer polynomials of $\sin(z)$, weighted by $\cos^2(z)$: $f_n(z) \propto \cos^2(z)\,C_{2n}^{(3/2)}(\sin z)$.

---

## RC-3.3b Addendum — Graviton Exact Spectrum (2026-04-18)

The graviton volcano potential is **also exactly solvable**. This corrects the earlier claim (now struck) that the graviton has irrational $l$ and no closed-form spectrum.

**Derivation.** The graviton mode equation after $z = \sqrt{2}\,r$:

$$-\psi''(z) + \tfrac{3}{4}\sec^2(z)\,\psi(z) = E\,\psi(z), \qquad E = \frac{m^2}{2} + \frac{9}{4} \tag{RC3.18a}$$

where the factor $3/4$ comes from the graviton potential $V_{\rm grav} = (3/2)\tan^2(\sqrt{2}\,r) - 3$: after the substitution and dividing by 2, the $\sec^2(z)$ coefficient is $(3/2)/2 = 3/4$.

This is Pöschl-Teller with $l(l-1) = 3/4$, i.e., $l^2 - l - 3/4 = 0$, giving:

$$l = \frac{1 + \sqrt{1 + 3}}{2} = \frac{1 + 2}{2} = \frac{3}{2}$$

**Key point:** The earlier error was computing $l(l-1) = 3/2$ (using the $\tan^2$ coefficient directly), when the correct value after the $z$-substitution is $l(l-1) = 3/4$. The factor of 2 from $d^2/dr^2 = 2\,d^2/dz^2$ halves the $\sec^2$ coefficient.

Neumann (even) spectrum on $[0, \pi/2]$:

$$E_n = (2n + \tfrac{3}{2})^2, \qquad n = 0, 1, 2, \ldots$$

Converting to $m^2$ via $m^2 = 2E - 9/2$:

$$m^2 = 2\bigl[(2n + \tfrac{3}{2})^2 - \tfrac{9}{4}\bigr] = 2(4n^2 + 6n) = 8n^2 + 12n$$

$$\boxed{m_n^2 = 4n(2n+3), \qquad n = 0, 1, 2, \ldots} \tag{RC3.18b}$$

| $n$ | $m_n^2$ (exact) | $m_n$ (units of $L^{*-1}$) | Mode |
|-----|-----------------|---------------------------|------|
| 0 | $0$ | $0$ | Zero mode (massless graviton) |
| 1 | $20$ | $2\sqrt{5} \approx 4.472$ | First KK graviton |
| 2 | $56$ | $2\sqrt{14} \approx 7.483$ | Second KK graviton |
| 3 | $108$ | $6\sqrt{3} \approx 10.39$ | Third KK graviton |

Numerical verification (finite-difference, Richardson extrapolation, $N = 4000$): $m_1^2 = 20.000000$ (error $< 3 \times 10^{-7}$). ✓

**Complete KCR-Cone spectrum summary:**

| Sector | Potential | Pöschl-Teller $l$ | Spectrum | Mass gap $m_1^2$ |
|--------|-----------|-------------------|----------|------------------|
| Graviton | $(3/2)\tan^2(\sqrt{2}\,r) - 3$ | $l = 3/2$ (half-integer) | $4n(2n+3)$ | $20$ |
| Vector | $4\tan^2(\sqrt{2}\,r) - 4$ | $l = 2$ (integer) | $8n(n+2)$ | $24$ |

The graviton mass gap ($m_1 = 2\sqrt{5}/L^*$) is lighter than the vector ($m_1 = 2\sqrt{6}/L^*$) by a factor $\sqrt{5/6} \approx 0.913$, consistent with the graviton's shallower potential well.

---

## What RC-3 Does Not Deliver (RC-4 Scope)

1. ~~**The numerical value of $m_1^2$**~~ — **RESOLVED above** (exact: $m_1^2 = 24$, $m_1 = 2\sqrt{6}/L^*$).

2. **The effective $k_c^{(\rm eff)}$ for the primordial spectrum** — the zero-mode $T_M$ acquires its effective mass from decoherence dynamics, not from the free-field spectrum. Deriving $k_c^{(\rm eff)} \approx 5H_0$ requires the sourced (non-free) T_M EOM.

3. **The amplitude $A_s$** — requires $\lambda_{\rm bdry}$ value, which depends on the T_M normalization from the microscopic (field-theoretic) action.

4. **Paper 2C §RC1.4 needs revision:** The assumed propagator form $P(k) = C/(k^2 + k_c^2)$ is incorrect at the free-field level — the zero mode is massless, giving $P(k) \sim 1/k^2$. The massive-propagator form must come from the decoherence-sourced dynamics. The spectral formula $\Delta^2_\Sigma(k) = A_s k^2/(k^2 + k_c^2)$ is therefore correct in structure but the origin of $k_c$ is dynamical, not from the KK spectrum.

## Key Finding: The λ_bdry Decoupling

The most important result of RC-3 is that the leading Λ_eff estimate from Path C (RC-2.5) is **independent of $\lambda_{\rm bdry}$**. The cosmological constant prediction:

$$\rho_{\rm drag} = \frac{3}{2}\frac{H_0^2}{G} \sim 18\,\rho_\Lambda$$

uses only:
- $\lambda_{\rm 2B} \cdot T = O(1)$ (geometric cancellation, Paper 2B §6)
- $\alpha_{\rm geom} = 3/2$ (CP¹ zero-mode integral)
- $\Gamma_{\rm dec} \sim H_0$ (consequence of the above)

None of these involves $\lambda_{\rm bdry}$. The boundary coupling enters only in:
- The amplitude of the primordial spectrum ($A_s$)
- The DM-limit density ($\rho_{\rm DM}$)

This is a clean separation: **the CC comes from geometry; the fluctuation spectrum comes from the coupling.**

---

## References

- Paper 2A §2.2 (δλ formalism, worldline action)
- Paper 2A §4 (abstract EOM on M×Σ)
- Paper 2B §5.2 (graviton zero mode, volcano potential conventions)
- Paper 2B §6 (KCR-Cone EOM: T~A⁻², λ·T = O(1))
- Paper 2C §RC1.4 (primordial spectrum formula, k_c identification)
- RC-2.5 (Path C Λ_eff derivation)
- Randall, L. & Sundrum, R. (1999). Phys. Rev. Lett. 83, 3370.
- Csáki, C., Erlich, J. & Terning, J. (2002). Phys. Rev. D 65, 015003. (Warped KK vector spectrum)

---

## Revision History

| Date | Change |
|------|--------|
| 2026-04-18 | Initial derivation — full 5D → 4D reduction for the vector sector on KCR-Cone. Zero-mode profile, volcano potential, propagator, λ_bdry identification. |
| 2026-04-18 | §RC3.3 addendum — exact analytic vector spectrum: $m_n^2 = 8n(n+2)$, integer $l=2$. $k_c = 2\sqrt{6}/L^* \approx 4.90/L^*$ exact. |
| 2026-04-18 | §RC3.3b addendum — exact analytic graviton spectrum: $m_n^2 = 4n(2n+3)$, half-integer $l=3/2$. Corrects earlier claim that graviton is not exactly solvable (error: used $l(l-1)=3/2$ instead of correct $3/4$ after $z$-substitution). Both KCR-Cone sectors now fully analytic. |
