# OP-21: ℓ* = S_max/2 — Numerical Assessment
**Date**: 2026-03-25
**Status**: CALCULATION COMPLETE — conjecture NOT supported by BH area entropy
**Target**: Revise OP-21 in §10 Open Problems

---

## The Claim Being Tested

OP-21 as stated: the stabilized fiber radius $\ell^* \approx 22\,\mu\text{m}$ marks the entropic
watershed $S(\ell^*) = S_{\max}/2$.

---

## Calculation

**$S_{\max}$** (Bekenstein-Hawking entropy of the cosmological horizon):
$$S_{\max} = \frac{\pi R_H^2}{\ell_P^2}
= \frac{\pi (4.4 \times 10^{26})^2}{(1.616 \times 10^{-35})^2}
\approx 2.3 \times 10^{123}$$

Matches standard estimate (Penrose 2004, Frampton et al. 2009). ✓

**$S(\ell^*)$** (BH area entropy of a sphere of radius $\ell^*$):
$$S(\ell^*) = \frac{\pi (\ell^*)^2}{\ell_P^2}
= \frac{\pi (2.2 \times 10^{-5})^2}{(1.616 \times 10^{-35})^2}
\approx 5.8 \times 10^{60}$$

**Ratio**:
$$\frac{S(\ell^*)}{S_{\max}} \approx \frac{5.8 \times 10^{60}}{2.3 \times 10^{123}}
\approx 2.5 \times 10^{-63} \neq \frac{1}{2}$$

---

## Verdict

**The conjecture is NOT supported by Bekenstein-Hawking area entropy.**
The ratio is $\sim 10^{-63}$, not $1/2$.

This does not rule out the conjecture — it means the identification requires a
different entropy measure. Candidates:

- **Entanglement entropy** accumulated by the universe up to scale $\ell^*$
  (requires a model of the decoherence history)
- **Holographic entropy of the KK-Cone** at $r = \ell^*$ from the induced
  $S^3$ metric (requires knowing $G_5$)
- **Fubini-Study/Bures volume entropy** on $\Sigma$ (natural to the CR
  framework; defined in Paper 3 §5 currency-of-the-realm)

---

## Revised OP-21 Statement for §10

> **OP-21. Entropic significance of $\ell^*$.** The stabilized fiber radius
> $\ell^*$ may mark a physically special entropic scale. The specific conjecture
> $S(\ell^*) = S_{\max}/2$ under the Bekenstein-Hawking area entropy is not
> supported numerically ($S(\ell^*)/S_{\max} \approx 2.5 \times 10^{-63}$
> under standard horizon entropy). A version of the conjecture using the
> information-geometric entropy defined by the Fubini-Study/Bures volume on
> $\Sigma$ — as defined in the currency-of-the-realm framework (Paper 3, §5)
> — remains open. Identifying the correct entropy measure is a prerequisite
> for evaluating this conjecture. The entropic watershed interpretation of
> $\ell^*$ is deferred pending Paper 3's formal treatment of the FS/Bures
> entropy functional.
