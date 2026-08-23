# Checkpoint 158: Specification 017 Live Boundary Frozen

**Date:** 2026-08-23  
**Status:** Live-ready boundary frozen after provider-free cross-platform pass; no Specification 017 live provider call has occurred  
**Checkpoint class:** PRE-LIVE FREEZE  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the explicit manual live workflow, credential/branch/confirmation boundary, result-preservation contract, and exact continuation for the already preregistered relation-backed recommendation/action-value experiment.  
**Authority:** Historical pre-live boundary. Specification 017 v0.1 and `relation_backed_recommendation_action_v1.json` remain authoritative for experiment semantics, cases, truth, gates, value signals, model/runtime treatment, and interpretation.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Associated branch:** `v1-recommendation-action-value-relation-backed`  
**Associated PR:** #16 -> `v1-frontend-spike`  
**Provider-free validated implementation head:** `07da2a091b5686b0378c7f8114495fe1d0b29c32`  
**Live-workflow introduction commit:** `da2c90b0ef883c15c24a3ff1e5007db14b478b56`

## 1. Starting evidence

Checkpoint 157 records the complete provider-free implementation gate.

Exact evidence on implementation head `07da2a091b5686b0378c7f8114495fe1d0b29c32`:

```text
V1 relation-backed recommendation action value
run 32655457836
Ubuntu PASS
Windows PASS

targeted provider-free suite
13 passed on Ubuntu
13 passed on Windows

full V1 Python suite
71 passed, 2 skipped on Ubuntu
71 passed, 2 skipped on Windows

Checkpoint metadata
run 32655457830 PASS

V1 reasoning context value
run 32655457833 PASS

V1 disposition semantics diagnostic
run 32655457848 PASS
```

No live provider credential was available to ordinary CI and no Specification 017 live call occurred.

---

## 2. Explicit manual live workflow

Branch workflow:

```text
.github/workflows/v1-relation-backed-recommendation-action-value-live.yml
```

Manual authorization literal:

```text
RUN_SPEC_017_FROZEN
```

The workflow is restricted to:

```text
refs/heads/v1-recommendation-action-value-relation-backed
```

and fails before provider execution unless:

```text
confirmation == RUN_SPEC_017_FROZEN
OPENAI_API_KEY is present
```

The workflow passes the same confirmation into the runner through:

```text
ADS_SPEC017_CONFIRM=RUN_SPEC_017_FROZEN
```

Before any live call it reruns the frozen provider-free targeted suite.

---

## 3. Frozen live plan remains unchanged

```text
4 frozen relation-backed project cases
3 conditions: GENERIC / SELECTIVE / FULL_HORIZON
3 repetitions per condition
36 planned successful reasoner outputs
36 planned successful blinded judge outputs
72 planned successful provider calls
90 maximum provider attempts
1 retry maximum per planned call
randomization seed 2026082303
```

Retry remains allowed only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never a retry reason.

The concrete reasoner/judge treatment remains exactly the frozen Specification 017 treatment. No live workflow parameter selects an alternative model, prompt, threshold, context treatment, or benchmark truth.

---

## 4. Frozen result distinction

The GitHub workflow's success state means only that the frozen experiment executed with preserved integrity and uploaded its artifacts.

It does not mean that Specification 017 earned promotion.

The only allowed advancement outcomes remain:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Promotion requires all absolute, relative, and expansion gates plus at least one preregistered value signal. A ceiling/tie result must remain `SAFE_BUT_NOT_DIFFERENTIATED`.

---

## 5. Complete result-preservation boundary

The runner writes:

```text
reasoning_plan.json
judge_plan.json
reasoner_attempts.jsonl
judge_attempts.jsonl
result.json
RESULT.md
relation_backed_recommendation_action.sqlite3
```

The workflow uploads the complete result directory with `if: always()` so partial execution evidence is retained when possible.

Every provider attempt must remain auditable. The mechanically generated `result.json` and `RESULT.md` are the first interpretation layer after the raw ledgers.

The downloaded artifact must be preserved durably in the repository before any post-result tuning, replacement experiment, or production-seam design.

---

## 6. Manual-dispatch exposure rule

The project already uses one narrow default-branch exception for `workflow_dispatch` discoverability:

```text
copy only the identical live-workflow file to main
```

For Specification 017, after the final experiment-branch head is green, it is permitted to copy only:

```text
.github/workflows/v1-relation-backed-recommendation-action-value-live.yml
```

to `main` without moving the active V1 implementation, specification, fixture, or canonical state there.

The workflow's explicit branch guard remains authoritative, so the manual run must select:

```text
v1-recommendation-action-value-relation-backed
```

---

## 7. Exact final pre-live gate

The live experiment is not yet authorized merely because this checkpoint exists.

The final branch head containing:

```text
Specification 017 frozen contract and fixture
provider-free implementation
cross-platform provider-free workflow
Checkpoint 157
explicit live workflow
Checkpoint 158
current routing reconciliation
```

must pass ordinary provider-free CI under all relevant workflows.

Required final checks:

```text
V1 relation-backed recommendation action value
V1 reasoning context value
V1 disposition semantics diagnostic
Checkpoint metadata
```

After that exact head is green:

```text
1. make no further experiment-branch commit
2. expose the identical live workflow on main only
3. manually dispatch the live workflow from v1-recommendation-action-value-relation-backed
4. enter RUN_SPEC_017_FROZEN
5. preserve the complete artifact before interpretation
```

Any experiment-branch commit after the final green validation invalidates that authorization boundary and requires ordinary CI again before a live run.

---

## 8. Promotion audit

### Promote relation-backed recommendation/action seam now

**Decision:** no.

Provider-free implementation success is not system-value evidence. The live three-condition comparison remains required.

### Promote production dependency relation schema now

**Decision:** no.

The benchmark's trigger pointers are experiment evidence and do not yet define the complete Foundation 018 relation model.

### Promote automatic Proposal/Question/Investigation/Decision mutation

**Decision:** no.

The experiment remains explicitly state-isolated.

### Execute one live Specification 017 experiment after exact green head

**Decision:** yes.

That bounded live comparison is the next legitimate evidence-producing action.
