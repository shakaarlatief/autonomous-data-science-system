# Checkpoint 174: Specification 021 Dependency-Backed Recommendation-Value Contract Frozen

**Date:** 2026-08-24  
**Status:** SPECIFICATION 021 FROZEN; IMPLEMENTATION NOT STARTED  
**Checkpoint class:** EXPERIMENT DESIGN / CONTINUITY  
**Project stage:** Post-V0 bounded V1 implementation and integration  
**Scope:** Freezes the first post-Specification-020 recommendation/action-value comparison using system-owned methodological provenance, explicit dependency-backed blocking relations, and explicit dependency-backed DEFER relations before implementation or provider execution.  
**Authority:** Specification 021 and its machine-readable fixture now govern this experiment. This checkpoint records the frozen boundary and does not authorize provider calls, project mutation, or production recommendation semantics.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-dependency-backed-recommendation-value`  
**PR:** #55

## 1. Starting boundary

Checkpoint 173 closed the Level-2 routing-consistency hardening after final push-triggered cross-platform routing validation on exact integration head:

```text
09670d5127c14cf3cece727b31823d5de4572211
```

The closure checkpoint was then committed to `v1-frontend-spike` at:

```text
8f29894667467e6ef58a02eb8f5d580c895968e6
```

This experiment branch was created from that exact closed integration boundary.

Historical scientific evidence remains:

```text
Specification 014   selective context preserved bounded reasoning quality with materially lower input burden
Specification 015   recommendation/action value FAIL
Specification 016   dependency-backed DEFER-vs-NOT_NOW boundary supported
Specification 017   relation-backed recommendation experiment INCOMPLETE
Specification 019   system-owned-provenance recommendation comparison FAIL
Specification 020   explicit dependency-backed RECOMMENDED-vs-BLOCKING_REQUIRED boundary supported
```

Nothing in Specification 021 changes or rescores those results.

## 2. Frozen artifacts

Prospective rationale:

```text
docs/research/029_dependency_backed_recommendation_value_design.md
```

Frozen contract:

```text
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
```

Frozen machine-readable benchmark:

```text
tests/fixtures/reasoning/dependency_backed_recommendation_action_v1.json
```

The exact design/fixture head before this checkpoint was:

```text
a771a905ebb4abe3652329c775f19ec6a18fb92d
```

PR #55 was opened as a draft against `v1-frontend-spike` after the three design artifacts were frozen.

## 3. Frozen scientific question

> Given matched project microstates with explicit requirement/scope/resolver relations, explicit defer-trigger relations, fixed reasoner/runtime treatment, and system-owned methodological provenance, does the accepted SELECTIVE exact-revision methodological-context path improve recommendation/action quality relative to a strong GENERIC reasoner while remaining no more expansion-prone than FULL_HORIZON?

The comparison is deliberately retained because Specification 020 established construct-validity evidence for the blocking boundary but did not establish methodological-context recommendation value.

## 4. Frozen case architecture

Exactly four new cases are used:

```text
DBRA-01  future validity and model sequencing
DBRA-02  compact nonlinear model shortlist
DBRA-03  distribution evidence before transformation
DBRA-04  missingness / class-imbalance decision framework
```

They reuse only the accepted selective methodological neighborhoods:

```text
DBRA-01
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

DBRA-02
    gradient-boosted-trees
    random-forest

DBRA-03
    ecdf
    histogram

DBRA-04
    class-imbalance
    missing-data
```

FULL_HORIZON remains the same ten-asset compact universe. GENERIC receives no reusable methodological assets.

No knowledge asset is added or rewritten for this experiment.

## 5. Structural semantics frozen before implementation

### BLOCKING_REQUIRED

Requires the supplied state to establish:

```text
exact unresolved requirement
+ exact active defended downstream scope
+ explicit scope DEPENDS_ON requirement relation
+ explicit action RESOLVES requirement relation
```

The model must return the exact requirement and scope pointers.

### DEFER

Requires:

```text
exact unresolved supplied trigger
+ explicit action WAITS_FOR trigger relation
```

The model must return the exact trigger pointer.

### RECOMMENDED

Worthwhile current work with no complete blocking construction.

### NOT_NOW

Neither currently justified nor activated by a supplied blocking/defer relation.

The experiment-owned result places relation pointers on each action decision rather than using one global blocked-scope list.

## 6. System-owned provenance boundary

Specification 019's durable instrumentation lesson is preserved:

```text
SYSTEM
    owns exact supplied stable_key@revision_id provenance
    owns methodology payload hash / byte count
    owns supplied project relation identities

MODEL
    owns recommendation content
    selects only among supplied identities
```

The model is not asked to self-report methodological provenance.

## 7. Frozen treatment and call plan

```text
conditions                   GENERIC / SELECTIVE / FULL_HORIZON
cases                        4
repetitions                  3 per condition per case
reasoner outputs             36 planned
judge outputs                36 planned
planned successful calls     72
maximum provider attempts    90
randomization seed           2026082402
reasoner model               gpt-5.6-sol
reasoner effort              medium
judge model                  gpt-5.6-sol
judge effort                 high
runtime                      OpenAI Agents SDK 0.19.4 behind ADS ReasoningRuntime
tools                        none
```

No provider call is authorized at this checkpoint.

## 8. Frozen hard evaluation logic

SELECTIVE must have zero:

```text
critical action omissions
blocking false positives
blocking pointer errors
defer pointer errors
```

and must meet the frozen aggregate/per-case exact and semantic quality floors.

It must also remain within the frozen GENERIC/FULL_HORIZON non-inferiority margins and must not be more expansion-prone than FULL_HORIZON.

Promotion additionally requires at least one prospectively frozen recommendation-quality value signal.

Descriptive token/context savings do not count as recommendation value.

## 9. Legitimate complete outcomes

```text
PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM
    safe + non-inferior + expansion-safe + at least one positive value signal

SAFE_BUT_NOT_DIFFERENTIATED
    safe + non-inferior + expansion-safe + zero positive value signals

FAIL
    complete design with any frozen absolute/relative/expansion gate failure

incomplete / integrity failed
    no scientific advancement classification
```

`SAFE_BUT_NOT_DIFFERENTIATED` is deliberately legitimate. The benchmark must not be rewritten simply because a strong GENERIC reasoner remains at or near ceiling.

## 10. Promotion audit

Promote now as frozen experiment authority:

```text
Research 029 as prospective rationale only
Specification 021 as frozen declared-scope authority
dependency_backed_recommendation_action_v1.json as exact machine-readable truth
this checkpoint as frozen-boundary provenance
```

Update current routing/current-state/open-question material to show Specification 021 is the active experiment and has not run.

Do not promote:

```text
production recommendation enums
production deterministic blocking policy
production dependency persistence schema
open-world action generation
project-state mutation
human approval/execution policy
large-scale knowledge-universe construction
new provider/model treatment
multi-agent architecture
```

## 11. Exact continuation

```text
1. implement Specification 021 provider-free only;
2. implement strict fixture construction audits for all blocking/defer relations and matched conditions;
3. implement the action-local structured result and exact pointer validation;
4. reuse system-owned methodological provenance and accepted exact-revision context construction;
5. implement deterministic metrics, blinded semantic judge payload construction, fake-runtime complete-design evaluation, and isolated persistence where needed;
6. add dedicated Ubuntu/Windows provider-free CI with no provider credential;
7. freeze an exact green implementation head in a later checkpoint;
8. do not add a live workflow or authorization before that green checkpoint;
9. do not modify or rescore Specifications 015-020.
```
