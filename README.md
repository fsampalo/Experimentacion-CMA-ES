# CMA-ES sampling comparison

[![CI](https://github.com/fsampalo/Experimentacion-CMA-ES/actions/workflows/ci.yml/badge.svg)](https://github.com/fsampalo/Experimentacion-CMA-ES/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

**Author:** Fernando Sampalo

Small experimental project comparing **three ways to generate offspring** inside a CMA-ES-style loop: **classical Gaussian** draws, **Sobol** quasi-random normal variates, and **Latin Hypercube** sampling. The same benchmark suite is run for each sampler; the notebook saves convergence curves, runtime summaries, and simple pairwise statistics (Mann–Whitney on final fitness).

## Repository layout

| Path | Purpose |
|------|---------|
| `cma_sampling.ipynb` | Implementation, experiment driver, plots |
| `main.tex` | Short write-up (expects figures under `imgs/`) |
| `requirements.txt` | Python dependencies |
| `scripts/smoke_test.py` | Fast import / sanity check (used in CI) |
| `docs/gallery/` | Optional PNG previews for the README ([how to](docs/gallery/README.md)) |
| `CITATION.cff` | Citation metadata for GitHub / Zenodo-style reuse |
| `LICENSE` | MIT |

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell
# source .venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
python scripts/smoke_test.py
```

Then open `cma_sampling.ipynb` and run all cells. A full sweep is **on the order of two minutes** on a typical laptop (30 runs × 12 functions × 3 samplers).

**Python:** 3.11 recommended (see `.python-version`); CI also runs on 3.12.

## Outputs

Figures are written to:

- `imgs/<sampler_name>/` — per-sampler convergence plots  
- `imgs/comparisons/` — overlays and `runtime_comparison.png`

If you migrated from an older Spanish-path version, rename `imgs/comparaciones/` → `imgs/comparisons/` and `tiempo_comparison.png` → `runtime_comparison.png`, or simply re-run the notebook.

## Build the PDF (optional)

With a LaTeX distribution installed (`pdflatex` on `PATH`):

```bash
pdflatex -interaction=nonstopmode main.tex
```

Or, if you have [GNU Make](https://www.gnu.org/software/make/) (e.g. Git Bash on Windows):

```bash
make pdf
```

## Reproducibility note

`requirements.txt` uses minimum versions so installs stay compatible across machines. For a frozen environment (e.g. supplementary material), run:

```bash
pip install -r requirements.txt
pip freeze > requirements-lock.txt
```

Commit `requirements-lock.txt` only if you want reviewers to reproduce exact package versions.

## Citation

GitHub reads [`CITATION.cff`](CITATION.cff). You can also cite the repository URL directly: [github.com/fsampalo/Experimentacion-CMA-ES](https://github.com/fsampalo/Experimentacion-CMA-ES).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is released under the [MIT License](LICENSE).
