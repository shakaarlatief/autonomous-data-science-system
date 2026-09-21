# Research 233: AO-9 P5 Evaluation and Decision Synthesis

**Date:** 2026-09-21
**Status:** AO-9 P5 COMPLETE / PREREGISTERED DECISIONS EVALUATED / P6 NEXT
**Program:** Research 219
**Protocol:** Research 228 / `AO9_HISTORICAL_REGRESSION_PROTOCOL_V01.json`
**Model-free trace:** Research 231
**P4 harness:** Research 232
**P4 evidence completion:** commit `b5d236fadbde99c668d752fec8e18b79fcdda489`
**Machine synthesis:** `docs/research/project_knowledge_activation_orchestration/ao9/evaluations/P5_DECISION_SYNTHESIS_V01.json`
**Scope:** Evaluate the frozen AO-9 decision rules against the completed P3/P4 evidence, without post-score tuning and without silently amending AO-3 through AO-7, Requirements V0.2, Specification 028, or current operational authority.
**Authority:** Research evaluation only. This document closes P5. It does not itself perform the owner AMEND decisions reserved for P7 and does not authorize AO-10 production implementation.

## 1. Evidence boundary

The P5 decision uses only frozen/preregistered AO-9 material and preserved scored evidence:

```text
Research 228
    preregistered protocol and decision rules

Research 231
    model-free P3 mechanism trace

Research 232
    minimum 13-run fresh-replay harness

P4 evaluations
    B/C on R2, R3, R6, R7, R8
    D on N1, N3, N4

preserved invalid attempt
    C_R7_run08_INVALID
    excluded from scoring
```

The required P4 decision set is complete:

```text
required fresh runs = 13
valid required runs = 13
hard-safety failures in valid required runs = 0
aggregate winner score = forbidden / not produced
```

The invalid C_R7 attempt remains durable contamination evidence and is not converted into either PASS or FAIL.

## 2. B-versus-C planner stopping rule

The frozen planner comparison requires R2, R3, R6, R7 and R8.

| Scenario | Arm B | Arm C | Unique C PASS? | Qualification-cost signal |
| --- | --- | --- | --- | --- |
| R2 collaboration activation | substantive applicable dimensions PASS; E9 FAIL | same | no | both above narrow budget |
| R3 architecture trigger activation | E7 PARTIAL; other applicable dimensions PASS | E7 PASS; other applicable dimensions PASS | **yes, E7** | B 32 / C 33 reported repository actions; both above 8 |
| R6 abnormal recovery | all substantive applicable dimensions PASS; E9 FAIL | same | no | about B 22 / C 40 actions; both above recovery ceiling 20 |
| R7 obligation realization | all applicable dimensions PASS | all applicable dimensions PASS | no | both materially above narrow ceiling |
| R8 known-risk activation | E7 PARTIAL; other applicable dimensions PASS | E7 PASS; other applicable dimensions PASS | **yes, E7** | about B 9 / C 16 actions; both above 8 |

Therefore:

```text
R2  C unique PASS = false
R3  C unique PASS = true   [E7]
R6  C unique PASS = false
R7  C unique PASS = false
R8  C unique PASS = true   [E7]

C unique-PASS scenarios = 2 / 5
planner-only no-unique-PASS fallback = NOT TRIGGERED
```

The preregistered default narrowing to only:

```text
planner + authority/action-contract + conformance
```

does not activate.

That result must not be overread. Arm B remains a strong simpler baseline. It matches C on the scored substantive behavior of R2, R6 and R7, and it solves difficult recovery and obligation-audit tasks through task-shaped reconstruction without the dedicated control mechanisms.

The unique evidence for C is narrower:

```text
R3
    explicit preservation/resume/self-observation semantics
    distinguish actual replay miss from already-known owner-reminder dependency
    retain future control-failure evidence

R8
    source-owned known-risk/reopen trigger enters the control cycle
    unresolved evaluation state is preserved
    trigger evidence remains distinct from final architecture disposition
```

P5 therefore records:

```text
PLANNER_ONLY_FALLBACK_TRIGGERED=false
C_INCREMENTAL_VALUE_DEMONSTRATED=true
C_INCREMENTAL_VALUE_PRIMARY_DIMENSION=E7
WHOLESALE_AO3_AO7_BEHAVIORAL_QUALIFICATION=false
```

P6 must reconcile these demonstrated benefits with cost and with mechanisms that did not earn unique P4 coverage.

## 3. Cost and boundedness are a separate qualification issue

The positive controls repeatedly exceed the frozen budgets.

Important examples:

```text
R2
    B and C both fail E9

R3
    B about 32 actions
    C about 33 actions
    ceiling 8

R6
    B about 22 actions
    C about 40 actions
    ceiling 20
    both fail E9

R7
    B about 24 tool invocations
    C about 24 repository-oriented invocations
    ceiling 8

R8
    B about 9 repository tool invocations
    C about 16 repository actions
    ceiling 8
```

The comparison therefore does not support either shortcut:

```text
"C adds value, therefore implement all of C unchanged"      INVALID INFERENCE
"B is cheaper/simpler, therefore C adds no material value" INVALID INFERENCE
```

Behavioral coverage and boundedness remain separate qualification dimensions.

The negative controls are encouraging for precision:

```text
D_N1
    PASS
    one assignment read
    zero deep governing-source loads

D_N3
    PASS
    question did not become mutation authorization
    output/action-shape re-entry could activate without granting mutation

D_N4
    PASS
    one assignment read
    zero deep runtime/restart-source loads
```

So the D amendment does not show the low-consequence over-activation failure the protocol was designed to detect.

## 4. AO8-E01 decisive rule

Research 228 preregistered `SUPPORT_AMEND` only if all five conditions hold.

### Condition 1: frozen C fails R9 mandatory closure

P3 establishes:

```text
event interpretation intentionally wrong/insufficient
S3 governing obligation absent
ordered consequential draft exists
independent output/action-shape re-entry absent
S8 cannot create a missing S6 contract

R9_C = FAIL at deterministic mechanism level
```

**Condition satisfied.**

### Condition 2: frozen D passes R9 mandatory closure

P3 establishes:

```text
consequential output shape fires independently
-> bounded authority/action-contract reconstruction
-> contract established or fail-visible NO_CONTRACT_AVAILABLE
-> conformance before dispatch

R9_D = PASS at deterministic mechanism level
```

**Condition satisfied.**

### Condition 3: D passes N1, N3 and N4

P4 records:

```text
D_N1 = PASS
D_N3 = PASS
D_N4 = PASS
```

**Condition satisfied.**

### Condition 4: D adds zero deep source loads on N1/N4

P4 records:

```text
N1 deep-source loads = 0
N4 deep-source loads = 0
```

**Condition satisfied.**

### Condition 5: D introduces no new hard-safety failure

No valid D negative control records a hard-safety failure.

**Condition satisfied.**

Therefore the preregistered result is:

```text
AO8_E01_DECISION=SUPPORT_AMEND
```

This is evidence for an owner AMEND decision. It is not the AMEND decision itself.

The supported primary delta is specifically:

```text
independent pre-dispatch output/action-shape re-entry
    ->
when a consequential proposed result/action exists
and relevant AuthorityReceipt/ActionContract closure is insufficient
    ->
re-enter bounded reconstruction/authority closure
    ->
apply normal conformance
```

The screen does not authorize an action and does not replace event/state activation.

No Research 222 edit occurs in P5.

## 5. D-only secondary refinements are not silently bundled

Arm D also froze:

```text
structural receipt/claim verification
distinct NO_CONTRACT_AVAILABLE versus CONFORMANT
```

P3 gives the structural verifier a deterministic R10 capability, and N3 demonstrates useful no-contract semantics in one fresh negative control.

But the minimum P4 set did not include a fresh C-versus-D R10 behavioral comparison.

Therefore P5 does **not** convert those secondary refinements into part of the AO8-E01 owner amendment automatically.

They remain separately qualified clarification/implementation candidates:

```text
AO8-Q01 structural verification
AO8-C02 NO_CONTRACT_AVAILABLE clarification
```

P6 must preserve that separation.

## 6. R51 requirement candidate

R51 asks that control-behavior misses and owner-reminder dependencies become observable enough to enter qualification/evolution evidence without requiring the owner to notice the pattern first.

AO-9 provides meaningful support:

```text
R3
    C adds unique E7 PASS over B
    durable architecture-trigger evidence is activated without owner path naming
    self-observation preserves the control interpretation

R8
    C adds unique E7 PASS over B
    source-owned reopen conditions activate without owner path naming
    unresolved evaluation state is preserved
```

This is stronger than a human-authored post-hoc note.

However, P4 is still a fresh-collaborator replay of frozen control semantics, not an executable production monitor. It does not prove that every real control miss will be mechanically surfaced by a deployed bridge when the task itself fails to nominate the relevant neighborhood.

P5 disposition:

```text
AO8_R51_EVIDENCE=SUPPORTED_BUT_NOT_EXECUTABLY_QUALIFIED
OWNER_REQUIREMENT_DECISION=PENDING_P7
AO10_SHADOW_MECHANICAL_SURFACING_QUALIFICATION=REQUIRED_IF_ACCEPTED
```

## 7. R52 requirement candidate

R52 asks for accepted MUST obligations to be traceable through:

```text
accepted obligation
-> implementation/migration gate or explicit governed scheduling
-> evidence
-> qualification
-> operational realization or explicit governed deferral
```

Evidence is strong that the requirement is needed:

```text
R7
    both B and C identify Specification 028 section 26/32 realization gaps
    already-realized W0 obligations are not falsely invalidated
    missing gate/evidence/activation linkage is surfaced

P3 R11
    selected AO-6 ROTATE remains visibly incomplete
    missing governed attach/switch realization remains open
```

At the same time, P3 and P4 agree on the mechanism limitation:

```text
frozen C/D contain no generic deterministic cross-artifact join
B and C can manually reconstruct the R7 audit
manual success != generic realization guarantee
```

P5 disposition:

```text
AO8_R52_EVIDENCE=STRONGLY_SUPPORTED_REQUIREMENT_GAP
FROZEN_CANDIDATE_SATISFIES_R52=false
OWNER_REQUIREMENT_DECISION=PENDING_P7
GENERIC_REALIZATION_MECHANISM=NOT_YET_QUALIFIED
```

The evidence therefore supports the need for R52 more strongly than it supports any particular implementation of R52.

## 8. AO-10 implications that P5 may and may not establish

P5 may establish:

```text
planner-only fallback is not triggered

planner remains a strong core mechanism

C-specific preservation/resume/self-observation behavior has empirical incremental value

known-risk/reopen activation has empirical incremental value

AO8-E01 earns SUPPORT_AMEND evidence

positive-path boundedness remains unresolved

R52 realization closure is not provided by frozen C/D
```

P5 may **not** establish:

```text
implement all AO-3 through AO-7 unchanged

delete or supersede AO-5/AO-6/AO-7 because one replay did not show unique PASS

amend Research 222 automatically

amend Requirements V0.2 automatically

amend Specification 028

close AO10-O01 or AO10-O02

switch project operational authority
```

Those are later governed decisions/qualification steps.

## 9. P5 decision summary

```text
AO9_P5=COMPLETE

P4_REQUIRED_VALID_RUNS=13/13
P4_INVALID_ATTEMPTS_PRESERVED=1
HARD_SAFETY_FAILURES_IN_VALID_REQUIRED_RUNS=0

B_VS_C_PLANNER_STOPPING_RULE=DO_NOT_TRIGGER_DEFAULT_NARROWING
C_UNIQUE_PASS_SCENARIOS=R3,R8
C_UNIQUE_PASS_DIMENSION=E7_PRESERVATION_RESUME_SELF_OBSERVATION
WHOLESALE_C_IMPLEMENTATION_JUSTIFIED=false

AO8_E01=SUPPORT_AMEND
AO8_E01_AUTOMATIC_AMENDMENT=false
AO8_E01_OWNER_DECISION_REQUIRED=true

AO8_R51=SUPPORTED_BUT_NOT_EXECUTABLY_QUALIFIED
AO8_R52=STRONGLY_SUPPORTED_REQUIREMENT_GAP
R52_MECHANISM_SATISFIED_BY_FROZEN_C_D=false

POSITIVE_PATH_BOUNDEDNESS=UNRESOLVED
NEGATIVE_CONTROL_OVERACTIVATION=NOT_OBSERVED

PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false

NEXT=AO9_P6_RECONCILIATION
```
