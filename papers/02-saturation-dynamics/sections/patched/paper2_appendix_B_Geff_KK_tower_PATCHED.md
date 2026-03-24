# Appendix B — Schematic Origin of \(G_{\mathrm{eff}}(r)=G_4[1+\alpha R_c/r+\dots]\)

Consider a static, spherically symmetric baryonic source of mass \(M_b\) localized on the brane at \(r=r_0\). In the linearized regime of §6.2, model the 4D effective potential on the brane as a zero mode plus a tower of massive KK modes:
\[
\Phi(r)= -\frac{G_4M_b}{r}-\sum_{n\ge 1}c_n^2\,G_4M_b\,\frac{e^{-m_nr}}{r},
\]
where \(m_n\) are KK masses and \(c_n\propto\chi_n(r_0)\) are brane-overlap coefficients.

Then
\[
a_{\mathrm{eff}}(r)=-\frac{\partial\Phi}{\partial r}
=-\frac{G_4M_b}{r^2}\left[1+\sum_{n\ge 1}c_n^2(1+m_nr)e^{-m_nr}\right].
\]

For a quasi-continuous tower with spectral density \(\rho(m)\) peaked around \(m_c\sim 1/R_c\), approximate the sum by
\[
\sum_{n\ge 1}c_n^2(1+m_nr)e^{-m_nr}
\approx \int_0^\infty \rho(m)(1+mr)e^{-mr}\,\mathrm{d}m.
\]

If \(\rho(m)\) is slowly varying on scale \(1/r\) (galaxy-scale \(r\gg R_c\)) and normalized so \(\int_0^\infty \rho(m)\,\mathrm{d}m\sim \alpha R_c^{-1}\), the asymptotic expansion gives
\[
\int_0^\infty \rho(m)(1+mr)e^{-mr}\,\mathrm{d}m
\sim \alpha\frac{R_c}{r}
+\mathcal{O}\!\left(\frac{R_c^2}{r^2}\right),\qquad r\gg R_c,
\]
with \(\alpha\) a dimensionless combination of overlap factors and spectral details.

Hence
\[
a_{\mathrm{eff}}(r)\approx -\frac{G_4M_b}{r^2}
\left[1+\alpha\frac{R_c}{r}
+\mathcal{O}\!\left(\frac{R_c^2}{r^2}\right)\right],
\]
or equivalently
\[
G_{\mathrm{eff}}(r)=G_4\left[1+\alpha\frac{R_c}{r}
+\mathcal{O}\!\left(\frac{R_c^2}{r^2}\right)\right].
\]

Status: schematic asymptotic motivation consistent with §6 assumptions; not a substitute for a full 5D eigenmode derivation.
