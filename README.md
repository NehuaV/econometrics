# Financial Econometrics

Course assignments, code, and reports.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```bash
uv sync
```

## Assignments

All Homework 1 files are in [`hw1/`](hw1/), including the assignment instructions,
original notebook, editable LaTeX source, generated figures, and compiled report.
See [`hw1/README.md`](hw1/README.md) for notebook and build instructions.

To rebuild the Homework 1 report from the notebook:

```bash
uv run python hw1/build.py
```

A LaTeX installation with `pdflatex` is required in addition to the Python dependencies.
