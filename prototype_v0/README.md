# Prototype V0

This directory contains the first deliberately limited implementation experiment for the Autonomous Data Science System.

It is not the production architecture.

The experiment asks whether explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make the same strong LLM materially more reliable than strong simpler workflows.

The benchmark is implemented before the P0 treatment so the treatment cannot define its own evaluation retrospectively.

## Current implementation scope

The first construction milestone contains only:

```text
synthetic customer-month churn DGP
visible Phase 1 project artifacts
hidden evaluator manifest
Phase 2 authoritative timing notice
benchmark self-tests
```

The autonomous P0 state runtime is intentionally not implemented yet.

## Install

From this directory:

```bash
python -m pip install -e ".[dev]"
```

## Run tests

```bash
pytest
```

The repository also runs these tests in GitHub Actions whenever Prototype V0 code or its workflow changes.

## Generate the development case

```bash
python -m ads_v0.casegen --output generated/development
```

The generated bundle separates:

```text
visible/
    project_brief.md
    README.md
    train.csv
    validation.csv
    test.csv
    baseline_model.py

phase_2/
    crm_field_timing_notice.md

evaluator_only/
    manifest.json
    self_test_report.json
```

Future treatment runners must expose only the appropriate visible material to the model. `evaluator_only/` is never part of the treatment workspace.

## Governing specification

See:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
```
