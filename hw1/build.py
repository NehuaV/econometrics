"""Rebuild the Homework 1 report from the notebook and main.tex."""
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent


def main():
    if shutil.which("pdflatex") is None:
        raise SystemExit("Install a LaTeX distribution with pdflatex, then rerun this script.")
    os.chdir(ROOT)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    # Run the submitted notebook in order, without changing its calculations.
    notebook = json.loads(Path("homework1.ipynb").read_text())
    namespace = {"__name__": "__main__"}
    plt.show = lambda: plt.close("all")
    with redirect_stdout(io.StringIO()) as log:
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                source = "".join(cell["source"])
                source = source.replace("%matplotlib inline", "")
                exec(compile(source, "homework1.ipynb", "exec"), namespace)
    print(log.getvalue())
    estimates = [namespace[name] for name in ("dgp1", "dgp2", "dgp3")]
    assert all(a.shape == (10, 2) for a in estimates)
    rows = [r"\begin{tabular}{lrrrrrr}", r"\toprule",
            r" & \multicolumn{2}{c}{DGP1} & \multicolumn{2}{c}{DGP2} & \multicolumn{2}{c}{DGP3} \\",
            r"Run & $\hat\beta_0$ & $\hat\beta_1$ & $\hat\beta_0$ & $\hat\beta_1$ & $\hat\beta_0$ & $\hat\beta_1$ \\", r"\midrule"]
    def row(label, values):
        return label + " & " + " & ".join(f"{x:.4f}" for x in values) + r" \\"
    for i in range(10):
        rows.append(row(str(i + 1), np.concatenate([a[i] for a in estimates])))
    rows += [r"\midrule", row("Mean", np.concatenate([a.mean(axis=0) for a in estimates])),
             row("SD across runs", np.concatenate([a.std(axis=0, ddof=1) for a in estimates])),
             row("Approximate SD", np.concatenate([np.sqrt(v / n * np.array([4, 12])) for n, v in [(20, .16), (20, 1), (200, 1)]])),
             r"\midrule", row("True value", np.array([5, -2.5] * 3)), r"\bottomrule", r"\end{tabular}"]
    Path("results.tex").write_text("\n".join(rows) + "\n")
    for _ in range(2):
        result = subprocess.run(["pdflatex", "-jobname=report", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if result.returncode:
            print(result.stdout)
            raise SystemExit(result.returncode)
    print(f"Built {ROOT / 'report.pdf'}")


if __name__ == "__main__":
    main()
