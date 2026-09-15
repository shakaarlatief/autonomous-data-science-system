# Research 174: Q10 Final Multidimensional Qualification Fixture Freeze

**Date:** 2026-09-15
**Status:** Q10 FINAL QUALIFICATION FIXTURE + ORACLE FROZEN / ORACLE-BLIND IMPLEMENTATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification cluster:** Q10 qualification methodology / budgets
**Exact freeze base:** `df983219300526d49fa9897c6752e95a3f347642`
**Scope:** Freeze the final Candidate 01 qualification program after every Q1-Q9 item has real evidence. Q10 must test bounded task-class budgets, structural plus behavioral qualification, and explicit multidimensional case-level reconstruction quality without one aggregate winner score.
**Authority:** Qualification protocol only. Current continuity remains operational authority. A Q10 pass may make target selection eligible, but cannot select Candidate 01, accept it on the owner's behalf, or switch authority automatically.
**Declared references:** `research:173`, `research:171`, `research:145`, `research:144`, `checkpoint:518`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `path:docs/research/project_knowledge_candidate_01/QUALIFICATION_MATRIX_V01.json`

## 1. Why Q10 can begin now

Research 173 closes the final three non-Q10 real-evidence gaps. The Candidate 01 evidence field at the freeze boundary is:

```text
real-evidence items            64 / 67
Q1-Q9 items with real evidence 64 / 64
remaining non-real items        3 / 67
remaining items                 KA-R30 KA-R40 KA-R41
remaining cluster               Q10 only
final qualified passes          0 / 67
```

Q10 is therefore no longer a wrapper around known untested architecture mechanisms. It can now operate as the frozen governing qualification program.

## 2. Frozen artifacts

```text
Q10_FINAL_FIXTURE_V01.json
    SHA-256  c62b54e7cb9903a175449d89c5383ed8843b2a8da236688173201a0d429db57c

Q10_FINAL_ORACLE_V01.json
    SHA-256  02349331fe405630599eb5dbd08401892517cdc87bfbdfdfee38983b7c80a15c
```

Freeze preflight verified all 17 bound source blobs exactly at `df983219300526d49fa9897c6752e95a3f347642`.

The implementation may read the fixture and its declared sources. It must not read the oracle until the first result has been preserved.

## 3. Qualification discipline

The protocol freezes five rules:

```text
1. implementation is oracle-blind;
2. no single aggregate winner score is permitted;
3. current authority remains unchanged during Q10;
4. target selection does not happen automatically even if Q10 passes;
5. every one of the 67 frozen items must receive an explicit final disposition.
```

This preserves the distinction between:

```text
evidence strength
    descriptive support accumulated during Research 149-173

final qualification disposition
    explicit Q10 pass/fail judgment against the frozen requirements boundary

target selection
    separate owner decision after qualification

authority switch
    separate later governed transition after selection and acceptance
```

## 4. Q10 bounded budget contract

### B01: broad current-state core

```text
source metric                     current-state-core real shadow
maximum compact core bytes        2,048
required must-preserve recovery   23 / 23
```

The existing real result is 871 canonical bytes with 23/23 must-preserve semantics recoverable.

### B02: narrow consequential task

```text
source metric                     integrated Q1+Q2+Q5 fresh-collaborator run
maximum evidence reads            10
maximum evidence bytes            40,960
maximum legacy bootstrap reads    0
```

The preserved run used 9 reads, 35,438 frozen-manifest evidence bytes and zero legacy bootstrap reads.

### B03: cross-provider authority task

```text
source metric                     Research 172/173 portable provider fixture
maximum packet materializations   1
maximum packet bytes              20,480
non-OpenAI provider               required
```

The preserved external-provider run used one packet and Anthropic Claude Opus 5. The exact frozen Windows packet materialization is below the budget.

### B04: real workstream stress

```text
source metric                     Q4 real-source stress
maximum declared source reads     12
maximum recovery replays          0
live target mutation              forbidden
```

The preserved Q4 run verifies 10 declared sources, replays zero completed transition steps and leaves the live Cockpit target unchanged.

These budgets are predeclared before Q10 implementation. The implementation may not loosen them after seeing the oracle.

## 5. Ten explicit qualification dimensions

Q10 evaluates scenarios through separate dimensions rather than one score:

```text
D01 project_current_state_orientation
D02 route_parent_objective
D03 governing_source_discovery_resolution
D04 risk_open_obligation_activation
D05 supersession_conflict_handling
D06 action_task_fidelity
D07 uncertainty_visibility
D08 important_omission
D09 context_read_tool_cost
D10 active_surface_maintenance_burden
```

Allowed case-level dispositions are:

```text
PASS
FAIL
NOT_APPLICABLE_WITH_REASON
```

Any `FAIL` blocks final qualification. A dimension may be marked not applicable only with an explicit reason.

## 6. Nine qualification scenarios

### S01 broad current orientation

Evidence:
- compact current-state core;
- real CURRENT_STATE decomposition;
- zero-seed routing.

Dimensions:
orientation, route/parent objective, omission, cost, maintenance burden.

### S02 consequential narrow task

Evidence:
- integrated Q1+Q2+Q5 fresh-collaborator result.

Dimensions:
orientation, governing-source resolution, risk activation, action fidelity, uncertainty, omission, cost.

### S03 cross-provider authority hard case

Evidence:
- Anthropic cross-provider result/evaluation.

Dimensions:
governing-source resolution, supersession/conflict, uncertainty, action fidelity, omission, cost.

### S04 identity / relationship / temporal

Evidence:
- Q3 real cases.

Dimensions:
supersession/conflict, uncertainty, omission.

### S05 workstream / concurrency / interruption

Evidence:
- Q4 real-source result plus oracle evaluation.

Dimensions:
route/parent objective, uncertainty, action fidelity, maintenance burden.

### S06 public/private degraded mode

Evidence:
- Q7 real cross-repository result.

Dimensions:
governing-source resolution, risk activation, uncertainty, omission.

### S07 migration / rollback / self-hosting

Evidence:
- Q9 real-base migration result.

Dimensions:
route/parent objective, governing-source resolution, uncertainty, omission, maintenance burden.

### S08 capture / promotion fidelity

Evidence:
- integrated Q1+Q2+Q5 result;
- operational Shadow V0.2.

Dimensions:
governing-source resolution, action fidelity, uncertainty, omission.

### S09 scale / maintenance / rebuild

Evidence:
- foundational Shadow V0.1;
- zero-seed routing;
- real CURRENT_STATE decomposition;
- compact current-state core.

Dimensions:
orientation, context/read/tool cost, maintenance burden, omission.

## 7. Structural gate

Q10 requires all of:

```text
PUBLIC_REPOSITORY_INTEGRITY=PASS
all 17 frozen Q10 source bindings exact
64 non-Q10 items have real evidence
full unit suite passes
```

A structurally valid candidate can still fail Q10 if behavioral qualification fails.

## 8. Behavioral gate

Q10 requires:

```text
all 9 scenarios evaluated
all relevant dimensions explicitly dispositioned
no relevant dimension FAIL
no material unresolved blocker hidden by aggregation
```

This is the direct qualification mechanism for KA-R40 and KA-R41.

## 9. Final-item disposition rule

The first 64 items do not pass merely because their evidence tier is `REAL`. Q10 may mark a non-Q10 item `PASS` only when:

```text
real evidence exists
AND
no preserved experiment limitation remains a final blocking contradiction
AND
its relevant Q10 scenario/dimension evidence does not expose a failure
```

The three Q10 items have explicit gates:

```text
KA-R30 PASS
    only if B01-B04 all pass

KA-R40 PASS
    only if both structural and behavioral gates pass

KA-R41 PASS
    only if all nine scenarios receive explicit relevant-dimension dispositions
    and no aggregate winner score is used
```

## 10. Post-Q10 boundary

A successful Q10 run may produce:

```text
FINAL_QUALIFIED_PASSES=67_OF_67
TARGET_SELECTION_ALLOWED=true
```

It may not produce automatically:

```text
TARGET_ARCHITECTURE=SELECTED
OWNER_ACCEPTANCE=ASSUMED
AUTHORITY_SWITCH=ALLOWED
```

Those remain separate governed decisions. Candidate 01 remains shadow/non-authoritative throughout Q10.

## 11. Freeze preflight

```text
Q10_FINAL_V01_FREEZE_PREFLIGHT=PASS
frozen source bindings         17 / 17 exact
budget contracts                4
qualification dimensions       10
behavioral scenarios            9
aggregate score                 FORBIDDEN
oracle access during first run  FORBIDDEN
current authority mutation      FORBIDDEN
selection during Q10            FORBIDDEN
```

```text
RESEARCH174=Q10_FINAL_FIXTURE_FROZEN
FREEZE_BASE=df983219300526d49fa9897c6752e95a3f347642
FIXTURE_SHA256=c62b54e7cb9903a175449d89c5383ed8843b2a8da236688173201a0d429db57c
ORACLE_SHA256=02349331fe405630599eb5dbd08401892517cdc87bfbdfdfee38983b7c80a15c
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_Q10_FINAL_V01_ORACLE_BLIND
```
