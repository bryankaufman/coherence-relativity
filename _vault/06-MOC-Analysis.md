# MOC — HCR Numerical Analysis
*Index of all computational scripts, data outputs, and figures.*

---

## Code Entry Points
| Script | Purpose | Output |
|--------|---------|--------|
| [[code/calculate_g_lambda]] | G_λλ(λ) Fubini-Study metric | data, fig1 |
| [[code/calculate_v_lambda]] | V(λ) quasipotential | data, fig2 |
| [[code/generate_figures]] | all figures from data | `figures/` |
| [[analysis/T3A_casimir_spectral]] | T3A Casimir spectral analysis | JSON + PNG |
| [[analysis/T3A_casimir_multispin]] | multi-spin extension | JSON + PNG |
| [[analysis/T3A_antiperiodic_v3]] | antiperiodic BC v3 | JSON + PNG |
| [[analysis/T3A_full_5D_ansatz]] | full 5D ansatz | JSON + PNG |
| [[analysis/T3A_anisotropic]] | anisotropic scan | JSON + PNG |
| [[analysis/casimir_computation]] | P2 Casimir computation | casimir_results.txt |

**Run environment**: `source .venv/bin/activate` (uv-managed venv)

---

## Figure Inventory
| File | Description | Status |
|------|-------------|--------|
| [[figures/fig1_g_lambda]] | G_λλ(λ) metric — U-shaped, N=10 | ✅ P1 |
| [[figures/fig1b_dlam_ds]] | dλ/ds geodesic | ✅ P1 |
| [[figures/fig2_quasipotential]] | V(λ) quasipotential landscape | ✅ P1 |
| [[figures/fig2_born_invariant_parallel]] | Born rule as frame invariant | ✅ P1 |
| [[figures/fig3_frame_transformation]] | Frame transformation diagram | ✅ P1 |
| [[figures/fig4_born_rule_invariant]] | Born rule invariant (alt) | ✅ P1 |
| [[figures/fig4_quasipotential_well]] | Quasipotential well | ✅ P1 |
| [[figures/fig5_double_slit_frames]] | Double-slit in two coherence frames | ✅ P1 |
| [[figures/fig6_cr_vs_standard]] | HCR prediction vs standard QM | ✅ P1 |
| [[figures/fig7_experimental_setup]] | Experimental setup schematics | ✅ P1 |
| [[figures/fig_geometric_entropy]] | Geometric entropy | ✅ P1 |
| T3A figures (analysis/) | Casimir landscape, spectral, phase portrait | 🔄 P2 |

---

## T3A Analysis Archive
All T3A outputs live in `analysis/`. Key files:

### Stage Results
- [[analysis/T3A_antiperiodic_v3_stage1]] (JSON)
- [[analysis/T3A_antiperiodic_v3_stage2]] (JSON)
- [[analysis/T3A_full5d_casimir_isotropic]] (JSON + PNG)
- [[analysis/T3A_multispin_full_SM]] (JSON + best PNG)
- [[analysis/T3A_multispin_scalar_graviton]] (JSON + PNG)

### Analysis Document
- [[analysis/T3A_analysis]] — main T3A analysis markdown

### Run Logs
- `analysis/T3A_run.log` — most recent run
- `analysis/T3A_antiperiodic_v3.log`

---

## Regeneration Commands
```bash
# Activate environment
source .venv/bin/activate

# Regenerate all data + figures
python3 code/calculate_g_lambda.py
python3 code/calculate_v_lambda.py
python3 code/generate_figures.py

# T3A Casimir (from analysis/)
python3 analysis/T3A_casimir_spectral.py
python3 analysis/T3A_antiperiodic_v3.py

# Build P1 PDF
cd papers/01-coherence-frames
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/bibtex main
/Library/TeX/texbin/pdflatex main.tex
/Library/TeX/texbin/pdflatex main.tex
```

---

## Data Outputs Location
- Figures: `figures/` (PDF + PNG)
- JSON outputs: `analysis/*.json`
- Casimir results: `papers/02-saturation-dynamics/casimir_results.txt`
- Session audit data: `audit/paper1/`, `audit/paper2/`, `audit/shared/`
