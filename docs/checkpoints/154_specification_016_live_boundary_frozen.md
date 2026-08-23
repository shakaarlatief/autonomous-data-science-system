# Checkpoint 154: Specification 016 Live Boundary Frozen

**Date:** 2026-08-23  
**Status:** Live-ready boundary frozen after provider-free cross-platform pass; no Specification 016 live provider call has occurred  
**Checkpoint class:** PRE-LIVE FREEZE  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the exact live-execution workflow and continuation boundary for the already preregistered Specification 016 disposition-semantics diagnostic.  
**Authority:** Historical pre-live boundary. Specification 016 v0.1 and `disposition_semantics_v1.json` remain authoritative for experimental semantics, tasks, gates, and interpretation.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-disposition-semantics-diagnostic`  
**Associated PR:** #15 -> `v1-frontend-spike`  
**Provider-free validated implementation head:** `6e7af25fd96d79673a59845e1c608c752970f658`  
**Live-workflow introduction commit:** `fe30a9d3b1d9e26d3c170633ce7d64be59f5c371`

## 1. Starting evidence

Checkpoint 153 records the provider-free closure of Specification 016 mechanics.

Exact evidence on implementation head `6e7af25fd96d79673a59845e1c608c752970f658`:

```text
V1 disposition semantics diagnostic
run 32646969810
Ubuntu PASS
Windows PASS

provider-free targeted tests
15 passed on Ubuntu
15 passed on Windows

full V1 Python suite
62 passed, 2 skipped on Ubuntu
62 passed, 2 skipped on Windows

Checkpoint metadata
run 32646969848
PASS

V1 reasoning context value
run 32646969808
PASS
```

No live provider credential was available to ordinary CI and no live model call occurred.

---

## 2. Live workflow is now explicit and secret-gated

Branch workflow:

```text
.github/workflows/v1-disposition-semantics-live.yml
```

Manual authorization string:

```text
RUN_SPEC_016_FROZEN
```

The workflow is restricted to:

```text
refs/heads/v1-disposition-semantics-diagnostic
```

and fails before provider execution unless `OPENAI_API_KEY` is present.

Before any live call the workflow reruns the frozen provider-free targeted suite:

```text
tests/unit/test_reasoning.py
tests/unit/test_disposition_semantics_harness.py
tests/unit/test_disposition_semantics_runner.py
tests/integration/test_disposition_semantics_vertical_slice.py
```

The live execution command installs only the already frozen experiment runtime dependency:

```text
openai-agents==0.19.4
```

and executes:

```text
python -m experiments.disposition_semantics.runner
```

No semantic judge, tool call, reusable methodological context, project-state mutation, or previous-response state participates.

---

## 3. Frozen live call plan remains unchanged

```text
6 contrastive pairs
2 variants per pair
3 repetitions per variant
36 planned successful reasoner calls
45 maximum provider attempts
1 retry maximum per planned call
randomization seed 2026082302
```

Retry remains allowed only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

A semantic classification miss is never retried merely because it is wrong.

---

## 4. Frozen advancement gates remain unchanged

```text
DS-G01  zero unresolved invalid successful outputs
DS-G02  aggregate exact disposition accuracy >= 0.95
DS-G03  every variant correct in at least 2 / 3 repetitions
DS-G04  every pair has both sides correct in at least 2 / 3 repetitions
DS-G05  expected-DEFER exact trigger-pointer accuracy == 1.00
DS-G06  expected-NOT_NOW null-pointer correctness == 1.00
```

Frozen outcomes:

```text
DISPOSITION_BOUNDARY_SUPPORTED
DISPOSITION_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

No threshold, fixture truth, operational definition, repetition count, randomization seed, retry rule, model configuration, runtime version, or output schema may be changed after live results are observed and then used to reinterpret this experiment.

---

## 5. Result preservation contract

The live runner writes:

```text
reasoning_plan.json
reasoner_attempts.jsonl
result.json
RESULT.md
```

The workflow uploads the complete directory even when execution fails after partial output creation.

Every provider attempt is preserved. The mechanically generated `result.json` and `RESULT.md` are the first interpretation layer after raw attempts.

Any durable repository interpretation must preserve the downloaded artifact before design changes or another experiment.

---

## 6. Manual-dispatch exposure rule

GitHub only offers convenient `workflow_dispatch` selection from workflows exposed on the default branch. The project therefore permits one narrow exception to the rule that `main` trails active V1 work:

```text
copy only .github/workflows/v1-disposition-semantics-live.yml to main
```

The branch restriction inside the workflow remains authoritative. The manual run must still explicitly select:

```text
v1-disposition-semantics-diagnostic
```

The default-branch copy is dispatcher exposure only. It does not merge the active implementation, specification, fixture, or canonical V1 state into `main`.

---

## 7. Exact pre-live gate

Do not execute the manual live workflow until the final branch head containing:

```text
Specification 016 frozen contract
provider-free implementation
provider-free cross-platform workflow
Checkpoint 153
live workflow
Checkpoint 154
current routing reconciliation
```

has passed ordinary provider-free CI.

After that exact head is green:

```text
1. do not modify the experiment branch before the live run
2. expose the identical live-workflow file on main only
3. manually dispatch V1 disposition semantics live
4. choose branch v1-disposition-semantics-diagnostic
5. enter RUN_SPEC_016_FROZEN
6. preserve the complete artifact before interpretation
```

Any experiment-branch commit after the final green pre-live validation invalidates that authorization boundary and requires another ordinary CI validation before live execution.

---

## 8. Promotion audit

### Promote production DEFER / NOT_NOW semantics now

**Decision:** no.

The live construct-validity evidence does not yet exist.

### Promote historical RA-02 relabeling

**Decision:** no.

Specification 015 remains immutable and failed under its own frozen contract.

### Promote automatic project mutation or execution

**Decision:** no.

This diagnostic has no authoritative project-state mutation path.

### Promote final provider/model selection

**Decision:** no.

The model/runtime settings remain controlled experiment constants only.

### Continue to live diagnostic after exact green head

**Decision:** yes.

The provider-free mechanics have earned one bounded live test of the frozen semantic boundary.
