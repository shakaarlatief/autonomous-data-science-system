# Checkpoint 012: Benchmark Generator and Self-Validation

**Date:** 2026-08-08  
**Status:** Historical mixed checkpoint  
**Checkpoint class:** MIXED  
**Project stage:** Experimental construction  
**Scope:** Records the historical milestone described by this checkpoint: Benchmark Generator and Self-Validation.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Benchmark generation milestone implemented and validated

## Why this checkpoint exists

Checkpoint 11 ended broad Prototype V0 specification and established that the first executable code should be benchmark code rather than P0 state or agent code.

Checkpoint 12 records completion of that first implementation milestone.

The repository can now generate a deterministic synthetic customer-month churn benchmark, write the Phase 1 visible artifacts, preserve evaluator-only ground truth separately, generate the Phase 2 authoritative timing notice, and mechanically reject benchmark instances that do not satisfy the intended experimental mechanism.

This is the first point at which the project has moved from conceptual architecture into tested implementation.

## Implemented prototype boundary

A new provisional experiment area now exists:

```text
prototype_v0/
├── .gitignore
├── README.md
├── pyproject.toml
├── src/
│   └── ads_v0/
│       ├── __init__.py
│       ├── casegen.py
│       └── selftest.py
└── tests/
    └── test_casegen.py
```

CI is defined in:

```text
.github/workflows/prototype-v0-tests.yml
```

This layout remains a disposable prototype convenience rather than a production-architecture decision.

## Implemented case generator

`casegen.py` now implements:

```text
CaseConfig
deterministic customer-month DGP
customer entry through time
absorbing churn
persistent customer heterogeneity
legitimate predictive features
post-outcome opaque account-state feature
surface-name variation
train / validation / test serialization
visible project brief
stale README
inherited contaminated baseline code
Phase 2 authoritative timing notice
hidden evaluator manifest
CLI case generation
```

The default development case uses:

```text
4,000 customers
24 monthly periods
train months 1-16
validation months 17-20
test months 21-24
```

Customers enter over time and later partitions therefore contain both known and newly entering entities.

## Visible and hidden information separation

A generated case bundle has:

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

This serialized layout is not yet the final runtime security boundary. The future instrumented workspace must expose only the correct region at the correct project phase.

## Benchmark self-validation

`selftest.py` now checks benchmark integrity before an LLM is involved.

Implemented checks include:

```text
entity IDs repeat
(entity, month) pairs are unique
train / validation / test month boundaries are correct
later partitions contain both known and new entities
churn is absorbing
prevalence falls inside the intended range
README row-unit statement conflicts with generated truth
README feature-timing statement conflicts with generated truth
Phase 2 notice matches evaluator truth
test artifact is registered as protected final evaluation
baseline source contains train+validation preprocessing fit
post-outcome feature is behaviorally relevant but imperfect
legitimate features have nontrivial predictive signal
post-outcome feature adds moderate additional signal
visible data contains only expected columns
```

A generated case that fails any required self-test is rejected.

## Development-case empirical properties

The CI-generated development case currently has:

```text
rows: 31,220
customers: 4,000
target prevalence: 0.1018578
validation new-customer share: 0.1981020
test new-customer share: 0.1209486
legitimate-feature validation AUROC: 0.6883573
validation AUROC with post-outcome field: 0.7211739
incremental AUROC from post-outcome field: 0.0328166
post-outcome code total variation between target classes: 0.2050478
```

These values are consistent with the intended benchmark shape:

- the target is imbalanced but not extremely rare;
- legitimate predictors provide meaningful but nontrivial signal;
- the hidden post-outcome field is useful enough to affect decisions;
- the post-outcome field is not a perfect target proxy;
- later periods genuinely mix known and newly entering entities.

The exact numerical values are benchmark characteristics, not analytical targets the future treatment should know.

## Generated inherited baseline is executable

The test suite now executes a generated `baseline_model.py` in a subprocess and verifies that it produces a valid validation AUROC.

This matters because the benchmark is intended to test whether a treatment notices the baseline's information-boundary flaw. A broken script would turn the test into ordinary debugging rather than methodological reasoning.

The inherited baseline remains deliberately contaminated because it fits learned preprocessing using train plus validation information before validation evaluation.

## Surface variation

The generator supports renaming key surface fields such as:

```text
customer_id -> member_key
snapshot_month -> scoring_period
account_state_code -> lifecycle_flag
```

Tests verify that renamed fields propagate consistently through datasets, visible documentation, the Phase 2 notice, and hidden evaluator truth.

This is an early prerequisite for held-out variants that preserve mechanisms while reducing lexical memorization.

## Package execution warning fixed

The package initializer originally imported `casegen` eagerly. Running:

```bash
python -m ads_v0.casegen ...
```

therefore caused Python `runpy` to warn that the module was already present in `sys.modules` before execution.

`ads_v0/__init__.py` was simplified to avoid executable submodule imports. The benchmark CLI now executes without that warning.

## Continuous integration

GitHub Actions now:

```text
installs Prototype V0
runs pytest
generates the full development benchmark
runs benchmark self-validation
prints benchmark sanity metrics
```

The validated run after the initializer fix and baseline-execution test completed successfully with:

```text
4 passed in 4.76s
```

The development benchmark also generated successfully in CI with the empirical properties recorded above.

GitHub runner warnings about deprecated Node action internals are external workflow-runner notices and do not indicate a Prototype V0 failure.

## What has not been implemented

The following remain intentionally absent:

```text
instrumented treatment workspace
condition-neutral action/trace model
project-phase runtime
deterministic evaluator assertions over treatment behavior
B0 runner
B1 runner
P0 typed state runtime
P0 knowledge activation
P0 prospective action gate
P0 dependency repair
semantic evaluator
paired experiment runner
held-out experiment execution
```

P0 has therefore still not had an opportunity to influence benchmark construction.

That ordering is intentional and protects the falsification experiment.

## Implementation lesson

The first implementation milestone supports the benchmark-first strategy.

The benchmark mechanism can be represented with ordinary Python, pandas, NumPy, scikit-learn, JSON, pytest, and generated Markdown/CSV artifacts. No agent framework, graph database, vector database, workflow engine, or other infrastructure was required.

This is evidence in favor of continuing to add complexity only when an experimental need appears.

It is not yet evidence that the broader P0 semantic architecture works.

## Next milestone

The next implementation milestone is the experiment boundary around treatment behavior:

```text
instrumented workspace
+ project phases
+ condition-neutral action trace
+ deterministic behavioral assertions
```

This should be implemented before B0/B1 model integration and before P0.

The important requirement is that B0, B1, and P0 eventually receive the same underlying artifact and Python capabilities while differing only in the methodological operationalization being tested.