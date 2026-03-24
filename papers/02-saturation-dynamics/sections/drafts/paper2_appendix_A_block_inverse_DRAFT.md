# Appendix A — Block Inverse for \(G(\lambda)\) up to \(O(\lambda^2)\)

Consider the block matrix
\[
G(\lambda)=
\begin{pmatrix}
A & \lambda B\\
\lambda C & D
\end{pmatrix},
\]
with \\(A\\) and \\(D\\) invertible and \\(\\lambda\\) a small dimensionless coupling parameter.
For correspondence with §2.2 notation:
\\[
A\\leftrightarrow G_{\\mu\\nu},\\quad D\\leftrightarrow G_{ab},\\quad B\\leftrightarrow T_{\\mu a},\\quad C\\leftrightarrow T_{a\\mu}.
\\]

Write
\[
G^{-1}(\lambda)=
\begin{pmatrix}
X(\lambda) & Y(\lambda)\\
Z(\lambda) & W(\lambda)
\end{pmatrix},
\]
and use the Schur-complement form (with respect to \(A\)):
\[
G^{-1}(\lambda)=
\begin{pmatrix}
A^{-1}+A^{-1}\lambda B\,S^{-1}(\lambda)\,\lambda C\,A^{-1} & -A^{-1}\lambda B\,S^{-1}(\lambda)\\
-S^{-1}(\lambda)\,\lambda C\,A^{-1} & S^{-1}(\lambda)
\end{pmatrix},
\]
where
\[
S(\lambda)=D-\lambda C A^{-1}\lambda B
=D-\lambda^2 C A^{-1}B.
\]

For small \(\lambda\),
\[
S^{-1}(\lambda)=\left(D-\lambda^2 C A^{-1}B\right)^{-1}
=D^{-1}+\lambda^2 D^{-1} C A^{-1} B D^{-1}+O(\lambda^4).
\]

Substituting and keeping terms through \(O(\lambda^2)\):
\[
X(\lambda)=A^{-1}+\lambda^2 A^{-1} B D^{-1} C A^{-1}+O(\lambda^4),
\]
\[
W(\lambda)=D^{-1}+\lambda^2 D^{-1} C A^{-1} B D^{-1}+O(\lambda^4),
\]
\[
Y(\lambda)=-\lambda A^{-1} B D^{-1}+O(\lambda^3),
\]
\[
Z(\lambda)=-\lambda D^{-1} C A^{-1}+O(\lambda^3).
\]

Hence
\[
G^{-1}(\lambda)=
\begin{pmatrix}
A^{-1}+\lambda^2 A^{-1} B D^{-1} C A^{-1}+O(\lambda^4)
&
-\lambda A^{-1} B D^{-1}+O(\lambda^3)
\\
-\lambda D^{-1} C A^{-1}+O(\lambda^3)
&
D^{-1}+\lambda^2 D^{-1} C A^{-1} B D^{-1}+O(\lambda^4)
\end{pmatrix}.
\]

Therefore, diagonal inverse blocks receive first corrections at even order \\(O(\\lambda^2)\\), while the *off-diagonal entries* of \\(G^{-1}(\\lambda)\\) are odd in \\(\\lambda\\), starting at \\(O(\\lambda)\\) via the factors \\(\\lambda Y(\\lambda)\\) and \\(\\lambda Z(\\lambda)\\). This matches the order-counting in Eq. 2.2.11, where \\(G^{\\mu a}(\\lambda)=\\lambda H^{\\mu a}(\\lambda)\\). The leading identifications are
\[
G^{\\mu\\nu}_0=A^{-1},\\qquad G^{ab}_0=D^{-1},\\qquad H^{\\mu a}_0=-A^{-1}BD^{-1},\\qquad H^{a\\mu}_0=-D^{-1}CA^{-1},
\]
consistent with Eq. 2.2.12–2.2.13.

Status: derivation-level appendix for reference and reuse in manuscript integration.
