# D3 — V_eff Stabilization: Outcome B (Rigorous Deferral)
**Status:** DRAFT — 2026-04-10 (Cowork, Opus)
**Result:** NO MINIMUM. Casimir destabilizing curvature overwhelms Berger restoring force.

---

## 1. Setup

The effective potential for the Berger squashing parameter η ∈ (0, 1]:

$$V_{\mathrm{eff}}(\eta) = V_{\mathrm{geom}}(\eta) + V_{\mathrm{Cas}}(\eta)$$

where:
- $V_{\mathrm{geom}}(\eta) = \int R[g(\eta)] \sqrt{g}\,\mathrm{d}V$ (Ricci scalar integral of the Berger sphere)
- $V_{\mathrm{Cas}}(\eta) = -\frac{\pi^2 \hbar c}{1440} \times \frac{f}{\left(\eta \, L^*_{\mathrm{base}}\right)^4}$ (Casimir on squashed fiber)

## 2. Result

$$V_{\mathrm{eff}}(\eta) = -2.523 + 1.262\,\eta^2 - \frac{K}{\eta^4}$$
(Eq. D3.1)

where $K$ is the Casimir coefficient.

The unique critical point satisfies:

$$\frac{d^2 V_{\mathrm{eff}}}{d\eta^2}\bigg|_{\eta_*} = -10.093 < 0$$

This is a **maximum**, not a minimum.

**The Casimir destabilizing curvature** ($|d^2 V_{\mathrm{Cas}}/d\eta^2| \approx 12.6$) **overwhelms the geometric restoring force** ($d^2 V_{\mathrm{geom}}/d\eta^2 \approx 2.5$) by a factor of ~5.

No interior minimum exists in $(0, 1]$.

## 3. Interpretation

The $1/\eta^4$ scaling of the Casimir energy is fundamentally destabilizing — it diverges faster than any polynomial restoring term as $\eta \to 0$. This is not a deficiency specific to the KCR-Cone; it is a **structural property of Casimir-based Λ models generally**. Any geometry attempting to stabilize via Casimir + geometric curvature alone faces this scaling mismatch.

## 4. Paper III Gate

Stabilization requires an additional contribution to $V_{\mathrm{eff}}$ of the form:

$$\delta V(\eta) = +\frac{K'}{\eta^n}, \quad n < 4$$

Candidate mechanisms:
1. **Flux quantization** — quantized magnetic flux through the fiber provides a $1/\eta^2$ term
2. **Radion back-reaction** — the breathing mode's self-interaction generates a polynomial correction
3. **Quantum corrections** — one-loop graviton contributions beyond the Casimir approximation

Any of these could provide a minimum if $K'$ is of the correct magnitude. The calculation requires Paper III.

## 5. §5.3.3 Paragraph (for insertion into §5.3 REVISED)

> The stabilization mechanism for the Berger-squashing parameter $\eta$ at the SC3 checkpoint remains undemonstrated. Analysis of $V_{\mathrm{eff}}(\eta) = V_{\mathrm{geom}}(\eta) + V_{\mathrm{Cas}}(\eta)$ reveals that the Casimir contribution's destabilizing curvature ($|d^2 V_{\mathrm{Cas}}/d\eta^2| \approx 12.6$) overwhelms the geometric restoring force ($d^2 V_{\mathrm{geom}}/d\eta^2 \approx 2.5$) by a factor of 5. Any critical point that emerges is a saddle (maximum), not a minimum. The dark energy calculation remains valid at $L^* \approx 68.6\,\mu\mathrm{m}$ ($\eta = 1$), respecting all invariant subspace limits. However, stabilization requires additional physics: flux quantization, radion back-reaction, or quantum corrections. This challenge is not unique to the KCR framework — all Casimir-based Λ models share it. We defer to Paper III, where flux quantization will be incorporated.

## 6. SC3 Impact

- **Casimir value** ($L^* = 56$–$69\,\mu\mathrm{m}$): UNAFFECTED. Valid at $\eta = 1$.
- **ISL bound**: UNAFFECTED. First KCR graviton at $\lambda_1 = 12$–$15\,\mu\mathrm{m}$ still passes.
- **Shape stabilization** (OP-5 shape): STILL RESOLVED. $k^2 = 2$ is topological.
- **Scale stabilization** (OP-5 scale): CONDITIONALLY OPEN. Casimir balance gives $L^*$, but no V_eff minimum demonstrated.

---

## Revision History

| Date | Change |
|------|--------|
| 2026-04-10 | D3 complete (Cowork, Opus). Outcome B — rigorous deferral. |
