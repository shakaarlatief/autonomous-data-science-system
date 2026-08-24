# Checkpoint 167: RECOMMENDED versus BLOCKING_REQUIRED Calibration Contract Frozen

**Date:** 2026-08-24  
**Status:** FROZEN PREREGISTRATION BOUNDARY  
**Checkpoint class:** EXPERIMENT CONTRACT FREEZE  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the first post-Specification-019 failure-attribution diagnostic for `RECOMMENDED` versus dependency-backed `BLOCKING_REQUIRED` before provider-free implementation or any new live model call.  
**Authority:** Specification 020 v0.1 and its frozen fixture govern this diagnostic until its result is preserved. This checkpoint does not promote production recommendation semantics or authorize provider execution.  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-blocking-calibration-diagnostic`  
**Specification:** 020  
**Research:** 027

## 1. Starting integration boundary

Specification 019 preservation was merged and the accepted integration branch was reconciled to:

```text
b9c9c3a38935983075a9ca88632177980bb20ede
```

That exact reconciliation boundary passed:

```text
Checkpoint metadata       run 32695017695   success
V1 frontend spike         run 32695017696   success
Ubuntu build/unit                              success
Windows build/unit                             success
Chromium browser/accessibility/visual gate     success
```

The diagnostic branch was created exactly from that head.

## 2. Frozen sources

Design rationale:

```text
docs/research/027_recommended_vs_blocking_required_calibration_design.md
```

Diagnostic authority:

```text
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
```

Machine-readable benchmark:

```text
tests/fixtures/reasoning/blocking_calibration_v1.json
```

Contract source immediately before this checkpoint:

```text
f03d060220ef500e34d5142032e028c7ee63879f
```

No provider call occurred while designing or freezing these sources.

## 3. Frozen scientific question

```text
Can a fixed reasoner distinguish worthwhile RECOMMENDED work
from genuinely BLOCKING_REQUIRED work when blocking is represented as:

candidate action
    -> exact unresolved requirement
    -> exact active defended downstream scope

and the supplied state explicitly states that the scope depends on
resolution of the requirement and that the action resolves it?
```

The question is construct validity and reasoner calibration only.

It is not a new GENERIC versus SELECTIVE versus FULL_HORIZON system-value comparison.

## 4. Frozen operational boundary

### BLOCKING_REQUIRED

All must be supplied:

```text
candidate action currently justified
one exact unresolved requirement
one exact active defended downstream scope
explicit scope DEPENDS_ON requirement relation
candidate action represented as the resolver of that requirement for the scope
```

Required result pointers:

```text
blocking_requirement_id = exact supplied requirement
blocked_scope_id        = exact supplied scope
```

### RECOMMENDED

```text
action materially worthwhile now or soon
no exact active supplied downstream scope is represented as blocked on it
```

Required result pointers:

```text
blocking_requirement_id = null
blocked_scope_id        = null
```

Importance, priority, common best practice, or possible future usefulness alone are explicitly insufficient for blocking status.

## 5. Frozen benchmark

Exactly six contrastive pairs:

```text
BC-01  prediction-time feature availability
BC-02  temporal validation sensitivity
BC-03  missing-data treatment sensitivity
BC-04  subgroup error analysis
BC-05  probability calibration assessment
BC-06  nonlinear model-family comparison
```

Each pair contains:

```text
same candidate action
same requirement menu
same downstream-scope menu
same shared evidence
same reasoner instruction
same output schema

one BLOCKING_REQUIRED variant
one RECOMMENDED variant
```

Expected truth is evaluator-only.

## 6. Frozen treatment

One reasoner condition only:

```text
provider                OpenAI
runtime                 OpenAI Agents SDK behind ADS-owned ReasoningRuntime
runtime package         openai-agents==0.19.4
model                   gpt-5.6-sol
reasoning effort        medium
text verbosity          low
max output tokens       2000
fast/priority request   no
previous response       none
runtime tools           none
multi-agent             no
```

Deliberately absent:

```text
methodological assets
retrieval
MethodologicalHorizon
selective context
GENERIC/SELECTIVE/FULL comparison
semantic judge
open-world action discovery
project mutation
```

## 7. Frozen call plan

```text
6 pairs
2 variants per pair
3 repetitions per variant
12 variants
36 planned successful reasoner calls
45 maximum provider attempts
randomization seed 2026082401
```

At most one retry per planned call and only for:

```text
TRANSPORT_FAILURE
PROVIDER_FAILURE
INCOMPLETE_RESPONSE
INVALID_STRUCTURED_RESPONSE
```

Semantic disagreement is never a retry reason.

The complete plan must be generated and hashed before the first provider call.

## 8. Frozen structured result

```text
BlockingCalibrationResult
    disposition: BLOCKING_REQUIRED | RECOMMENDED
    blocking_requirement_id: str | None
    blocked_scope_id: str | None
    rationale: str
```

The model may select only supplied requirement/scope identities.

This is experiment output, not authoritative Proposal or project state.

## 9. Frozen hard gates

```text
BC-G01  zero unresolved invalid successful outputs
BC-G02  aggregate exact disposition accuracy >= 0.95
BC-G03  every variant >= 2/3 exact dispositions correct
BC-G04  every pair both sides >= 2/3 exact dispositions correct
BC-G05  all 18 expected-BLOCKING_REQUIRED observations have exact
         disposition + requirement pointer + blocked-scope pointer
BC-G06  all 18 expected-RECOMMENDED observations have exact
         disposition + both pointers null
```

BC-G05 and BC-G06 intentionally make support effectively require exact correctness across all 36 deliberately unambiguous observations. This strictness is frozen prospectively.

## 10. Frozen outcomes

Exactly one:

```text
BLOCKING_BOUNDARY_SUPPORTED
BLOCKING_BOUNDARY_NOT_SUPPORTED
INCOMPLETE
```

If supported, only the following conclusion is authorized:

> A dependency-backed blocking distinction is operationally representable and the fixed reasoner can separate it from non-blocking recommended work on the frozen deliberately unambiguous cases.

No recommendation-system value or production taxonomy conclusion follows.

## 11. Historical integrity

Specification 019 remains permanently `FAIL` under its own frozen contract.

Do not:

```text
rescore RB-02
edit its expected labels
relax its gates
use repeated live outputs as tuned successor truth
```

Specification 020 is prospective failure attribution only.

## 12. System-owned identity boundary

The system owns:

```text
candidate action identity
supplied requirement identities
supplied downstream-scope identities
context/request provenance
```

The model owns only the diagnostic classification, supplied-ID selection, and rationale.

The model cannot create authoritative project relations in this experiment.

## 13. Promotion audit

### Frozen as diagnostic authority

```text
Research 027 rationale
Specification 020 v0.1
blocking_calibration_v1.json
Checkpoint 167
```

### Not promoted

```text
production RECOMMENDED semantics
production BLOCKING_REQUIRED semantics
production recommendation ranking
production dependency persistence schema
SELECTIVE recommendation value
automatic project mutation or execution
final provider/model policy
multi-agent recommendation architecture
```

No foundation or accepted project-level decision requires modification at this checkpoint.

## 14. Exact continuation

```text
1. implement the provider-free experiment harness only
2. mechanically audit all six contrastive pairs and truth blinding
3. build and hash the deterministic 36-call plan before any provider path exists
4. implement experiment-only structured output and pointer validation
5. implement deterministic gates and fake-runtime integration
6. add dedicated provider-free Ubuntu/Windows CI with no OPENAI_API_KEY
7. validate the exact implementation head plus accepted regression suites
8. freeze a later implementation/live boundary checkpoint
9. only then add or authorize a governed live workflow through Specification 018
10. make no provider call before that exact green boundary exists
```
