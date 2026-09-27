# Project hygiene report

## Policy

- `build/` and `dist/` are generated and are not canonical source.
- Python/cache artifacts are removed by the hygiene gate and excluded from packages.
- Canonical state lives in `gpt-project.yaml`, `project-status.yaml`, `assistant/`, `contracts/`, `knowledge/`, `schemas/`, `tests/`, `evals/`, `scripts/`, `templates/`, `reports/` and `.github/`.
- Runtime distributions are generated from canonical sources and are never edited as authorities.

## Step 12 result

`python scripts/project_hygiene.py --project-root . --mode final --fix` returned **PASS** in the clean-source CI simulation. No generated `build/` or `dist/` directory is retained in the canonical checkpoint.
