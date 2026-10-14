# Econometrics

This repository contains solutions and code for the Financial Econometrics homework.

## Getting Started

To set up your development environment for this project, you'll need [uv](https://github.com/astral-sh/uv), a fast Python package manager.  
If you don't have `uv` installed, you can install it following the instructions in their [documentation](https://github.com/astral-sh/uv#installation).

### Step 1: Install dependencies

```bash
uv sync
```

This command will create a `.venv` directory if it doesn't exist and install all required dependencies as defined in `pyproject.toml`.

### Step 2: Activate the virtual environment

#### On Linux/macOS

```bash
source .venv/bin/activate
```

#### On Windows

```bash
.venv\Scripts\activate
```

### Step 3: Run your code

You can now run the Python scripts for the homework or start a Jupyter notebook as needed.

---

## Project Structure

- `pyproject.toml` – Project metadata and dependencies.
- `figures/` – Directory for generated figures (gitignored).

## Notes

- Use `uv sync` to update dependencies whenever `pyproject.toml` changes.
- For development, you can install additional packages using:
  ```bash
  uv pip install <package-name>
  ```

Happy coding!