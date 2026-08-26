# V1 Relation-Backed Recommendation and Action Value Result

**Specification:** 017 v0.1  
**Live workflow run:** 32656446705  
**Live job:** 97235820936  
**Frozen source head:** `bf041f4b4a485382d0e6e5c508ad916199601ee8`  
**Date:** 2026-08-23  
**Result class:** INCOMPLETE LIVE EXECUTION, NO ADVANCEMENT CLASSIFICATION

## 1. Executive result

The first live execution of frozen Specification 017 did not obtain the complete matched 36-reasoner / 36-judge scored design required for any frozen advancement outcome.

Mechanical runner result:

```text
planned reasoner outputs       36
successful reasoner outputs    29
planned judge outputs          36
successful judge outputs       29
scored observations            29
reasoner attempt records       48
judge attempt records          36
provider attempts used         77 / 90
complete scored design         false
execution integrity            true
gate evaluation                not permitted
advancement outcome            none
```

Therefore Specification 017 is **not** classified as:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Those three outcomes apply only to a complete scored design under the frozen evaluator. No post-hoc rescore is permitted.

## 2. What succeeded before the incomplete boundary

The explicit live workflow ran from the exact frozen source head. Its branch, confirmation, credential, and provider-free preflight gates succeeded.

The targeted provider-free suite immediately before live calls returned:

```text
13 passed
```

The live environment used the frozen treatment:

```text
reasoner model              gpt-5.6-sol
reasoner effort             medium
judge model                 gpt-5.6-sol
judge effort                high
openai-agents               0.19.4
OpenAI client               2.54.0
Python                      3.13.15
```

The accepted reusable-knowledge snapshot remained unchanged, project-state counts remained unchanged, all preflight technical invariants recorded by the runner were true, and the runner reported `execution_integrity_passed = true`.

## 3. Exact incompleteness pattern

Condition completion was:

```text
SELECTIVE       12 / 12 successful reasoner outputs
FULL_HORIZON    12 / 12 successful reasoner outputs
GENERIC          5 / 12 successful reasoner outputs
```

Seven planned GENERIC outputs remained unsuccessful after the frozen per-call retry policy was exhausted.

The reasoner attempt ledger contains:

```text
29 SUCCESS
19 FAILED
```

All 19 failed reasoner attempts were classified mechanically as:

```text
INVALID_STRUCTURED_RESPONSE
```

All 19 failures occurred in the GENERIC condition.

The repeated validation messages were:

```text
RB-01  unsupported methodological basis keys: ['VALIDITY_CONSTRAINT']
RB-02  unsupported methodological basis keys: ['MODEL_OPTION']
RB-03  unsupported methodological basis keys: ['EVIDENCE_OPTION']
RB-04  unsupported methodological basis keys: ['DECISION_FRAMEWORK']
```

The five successful GENERIC outputs returned an empty `methodological_basis`, as required.

## 4. Failure attribution

The frozen reasoner instruction explicitly states:

```text
In methodological_basis, list only supplied stable keys that materially support the result;
for GENERIC, methodological_basis must be empty.
```

GENERIC intentionally supplies zero reusable methodological revisions. The rejected outputs instead placed the case's requested reasoning-function label into `methodological_basis`.

This reveals a concrete boundary problem:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

The current structured output asks the model to self-report knowledge provenance while the system separately owns exact supplied-revision provenance. In GENERIC, the only valid reusable-knowledge basis is deterministically empty, yet the model frequently interpreted the field as a place to name the abstract reasoning function.

This is best treated as a **structured-output/provenance instrumentation failure** under the frozen treatment, not as evidence that GENERIC, SELECTIVE, or FULL_HORIZON won or lost the recommendation/action comparison.

## 5. What this result does not establish

Because the complete matched design was not obtained, the result must not be used to claim:

```text
SELECTIVE improves recommendation/action quality
GENERIC matches or beats SELECTIVE
FULL_HORIZON matches or beats SELECTIVE
relation-backed recommendation/action value is established
relation-backed recommendation/action value is falsified
Specification 017 passed or failed its frozen quality gates
```

Partial condition scores exist in the raw ledgers, but they are not advancement evidence and must not be used to tune the benchmark truth, thresholds, value signals, or treatment.

## 6. Why the unchanged workflow should not simply be rerun

The run already consumed the frozen within-call retry allowance and exposed a systematic treatment/output-contract incompatibility concentrated in GENERIC.

Starting a new full workflow attempt solely to hope that all GENERIC calls happen to return an empty self-reported basis would:

```text
repeat successful calls outside the frozen call plan
consume additional provider calls without correcting the identified boundary
turn stochastic conformance into an accidental completion criterion
```

No unchanged rerun is authorized by this result record.

## 7. Bounded design consequence

The next design should separate **system-owned context provenance** from any optional **model-authored methodological citation/self-attribution**.

At minimum, the next preregistered treatment should examine a structure like:

```text
system-owned trace
    exact supplied stable_key@revision_id identities
    exact condition/context digest

model recommendation result
    action dispositions
    dependency pointers
    blocked scopes
    clarifications
    rationales

optional model citation layer
    only if it adds measurable value
    constrained to an explicit supplied-ID menu
```

For GENERIC, reusable-knowledge provenance is already known by the system to be empty and should not depend on free model self-report.

This is a prospective design consequence only. Specification 017 itself remains unchanged.

## 8. Raw evidence preservation

GitHub Actions artifact:

```text
artifact ID        9497737594
artifact name      v1-relation-backed-recommendation-action-bf041f4b4a485382d0e6e5c508ad916199601ee8-1
artifact ZIP SHA   a2846d97673e7221ef3dca1792c2902f12039e9b607d1e14917c0aaf62a5df8d
```

The exact extracted result bundle is durably preserved at:

```text
experiments/relation_backed_recommendation_action_value/results/
    spec017-live-20260823-run-32656446705/
```

It contains:

```text
MANIFEST.md
RESULT.md
reasoning_plan.json
judge_plan.json
reasoner_attempts.jsonl
judge_attempts.jsonl
result.json
relation_backed_recommendation_action.sqlite3
```

The preservation workflow independently verified every extracted artifact file against the SHA-256 digest observed from the downloaded live artifact before committing it.

## 9. Advancement decision

```text
Specification 017 scientific advancement outcome    NONE
Reason                                            incomplete scored design
Promote recommendation/action seam                NO
Merge experimental implementation as production   NO
Preserve frozen contract and raw evidence          YES
Proceed to failure-attribution/design correction   YES
```

Before another recommendation/action-value live comparison, the provenance/instrumentation boundary must be redesigned and preregistered without changing Specification 017's historical truth.
