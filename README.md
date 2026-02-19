# Coherence Relativity: Numerical Code

This repository contains Python code for numerical calculations and figure generation supporting the paper:

**"Coherence Relativity I: Coherence Frames, Frame Invariance, and the Born Rule"**  
Bryan Kaufman  
*Submitted to Foundations of Physics*

## Overview

This code implements:
- Fubini-Study metric calculations on coherence space
- Quasipotential landscape computation
- Publication-quality figure generation for 8 figures

## Contents

```
code/
├── calculate_g_lambda.py      # Fubini-Study metric G_λλ(λ) calculation
├── calculate_v_lambda.py      # Quasipotential V(λ) calculation
├── generate_figures.py        # Generate all 8 paper figures
├── gen_fig1_dual.py           # Figure 1: Dual view (G_λλ and dλ/ds)
└── gen_fig1b.py               # Figure 1b: dλ/ds standalone plot
```

**Note**: Figures 3, 4, and related conceptual diagrams are generated using TikZ code embedded directly in the LaTeX manuscript (`main.tex`).

## Requirements

- Python 3.8+
- NumPy
- Pandas
- Matplotlib
- SciPy
- SymPy

Install dependencies:
```bash
pip install numpy pandas matplotlib scipy sympy
```

Or using `uv`:
```bash
uv pip install numpy pandas matplotlib scipy sympy
```

## Usage

### 1. Calculate Fubini-Study Metric

```bash
python code/calculate_g_lambda.py
```

**Output**: `data/g_lambda.csv` containing λ and G_λλ values

### 2. Calculate Quasipotential

```bash
python code/calculate_v_lambda.py
```

**Output**: `data/v_lambda.csv` containing λ, G_λλ, F^λ, V(λ), and standard QM comparison

### 3. Generate Figures

```bash
python code/generate_figures.py
```

**Output**: 8 publication-quality figures in `figures/`:
- `fig1_g_lambda.pdf` - Fubini-Study metric
- `fig2_quasipotential.pdf` - V(λ) landscape
- `fig3_frame_transformation.pdf` - Frame transformation diagram
- `fig4_born_rule_invariant.pdf` - SR/CR analogy
- `fig5_double_slit_frames.pdf` - Double-slit in two frames
- `fig6_cr_vs_standard.pdf` - CR vs standard QM
- `fig7_experimental_setup.pdf` - Experimental schematics
- (Plus PNG versions)

## Physical Model

The code implements a double-slit which-path measurement model with:
- **Coherence parameter**: λ ∈ [0,1] (0 = fully coherent, 1 = which-path resolved)
- **Fubini-Study metric**: G_λλ(λ) measuring information-geometric distance
- **Quasipotential**: V(λ) from Freidlin-Wentzell large deviation theory
- **Environment**: Multi-mode decoherence model (N=10 modes)

## Key Results

- **Quantum-classical crossover**: λ ≈ 0.41 (where G_λλ is minimal)
- **Geometric activation distance**: s* ≈ 0.72
- **Frame transformation timescales**: τ_frame ~ 1-2 μs for superconducting qubits

## Citation

If you use this code, please cite:

```bibtex
@article{kaufman2026coherence,
  title={Coherence Relativity I: Coherence Frames, Frame Invariance, and the Born Rule},
  author={Kaufman, Bryan},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  year={2026}
}
```

## License

MIT License - see LICENSE file

## Contact

Bryan Kaufman  
Email: bryankaufman@mac.com

## Acknowledgments

Code developed as part of the Society of Mind coordination network. Generated using open-source scientific Python tools.
