# Homework 1: simple OLS regression

## Files

- `assignment.pdf`: the assignment instructions.
- `homework1.ipynb`: Dobri's original notebook, with unchanged calculations.
- `main.tex`: editable LaTeX source for the revised report.
- `report.pdf`: the compiled report to submit alongside the notebook.
- `results.tex` and `figures/`: results and plots generated from the notebook.
- `build.py`: rebuilds the figures, results table, and PDF.

The LaTeX source is based on the team's supplied `Hw1_econometrics.zip`, with
the revised authors, student numbers, and discussion. The report covers the ten repetitions requested by
the assignment and does not include the supplementary 5,000-run simulation.

## Rebuild everything

Install the Python dependencies from the repository root with `uv sync`.
You also need a LaTeX installation providing `pdflatex` and the packages used
in `main.tex` (for example, TeX Live or MacTeX).

From the repository root:

```bash
uv run python hw1/build.py
```

The script runs the notebook's code cells in order with a noninteractive plotting
backend, regenerates the three figures and `results.tex`, and compiles `main.tex`
twice. It does not change the notebook. The final file is `hw1/report.pdf`.

To compile only the report using the committed figures and results:

```bash
cd hw1
pdflatex -jobname=report -interaction=nonstopmode -halt-on-error main.tex
pdflatex -jobname=report -interaction=nonstopmode -halt-on-error main.tex
```

## Open the notebook

From the repository root:

```bash
cd hw1
uv run --project .. jupyter notebook homework1.ipynb
```

Run the notebook from `hw1/` so its figures are saved in `hw1/figures/`.
