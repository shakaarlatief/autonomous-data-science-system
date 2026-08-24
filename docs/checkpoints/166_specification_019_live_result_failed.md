# Checkpoint 166: Specification 019 Live Result Failed

**Date:** 2026-08-24  
**Design session:** 04  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 04 - Selective Context Promotion & Reasoning Vertical Slice  
**Branch:** `v1-recommendation-action-value-system-provenance`  
**PR:** #33, not to be merged as a recommendation/action promotion  
**Classification:** `FAIL`  
**Promotion outcome:** preserve evidence; do not promote the Specification 019 recommendation/action implementation

## Boundary closed by this checkpoint

Specification 019 prospectively reran the relation-backed recommendation/action comparison after correcting the provenance instrumentation defect exposed by Specification 017.

The frozen scientific truth remained inherited from Specification 017. The substantive contract change was:

```text
exact supplied methodological provenance
    model-authored field
        -> deterministic system-owned trace
```

This checkpoint records the complete live result and performs the post-result promotion audit.

---

## Frozen execution evidence

Exact provider-free validated live source:

```text
6b5e6237b738250458550f95c9f3a6b0d51e86ec
```

Provider-free cross-platform gate:

```text
V1 system-owned provenance recommendation action   run 32664369953   success
Checkpoint metadata                                run 32664369955   success
Ubuntu dedicated                                   13 passed
Windows dedicated                                  13 passed
Ubuntu full V1                                     116 passed, 2 skipped
Windows full V1                                    116 passed, 2 skipped
provider credential in ordinary CI                 absent
```

The frozen source was pinned to the immutable live ref before launch.

Governed launch evidence:

```text
launch id                 spec019-system-provenance-001
accepted request issue    35
launcher run              32664527166
live workflow run         32664534864
live job                  97255789247
artifact ID               9499756280
```

The target workflow independently verified the exact launch identifier, exact source SHA, frozen confirmation, provider credential boundary, and provider-free preflight before provider execution.

---

## Complete live design

The run completed the entire frozen plan:

```text
reasoner outputs          36 / 36
judge outputs             36 / 36
scored outputs            36 / 36
provider attempts         72 / 90
retries                    0
complete scored design     true
execution integrity        true
```

The runner preserved the exact locked base-fixture identity and system provenance plan. No authoritative project-state tables changed.

---

## Frozen scientific result

Aggregate metrics:

```text
                         GENERIC        SELECTIVE       FULL_HORIZON
exact accuracy           0.944444       0.916667        0.944444
semantic score           0.950000       0.950000        0.950000
blocking false positives 4              6               4
critical omissions       0              0               0
blocking false negatives 0              0               0
under-recommendations    0              0               0
defer-pointer errors     0              0               0
```

Per-case exact accuracy:

```text
RB-01   GENERIC 1.000000   SELECTIVE 1.000000   FULL 1.000000
RB-02   GENERIC 0.777778   SELECTIVE 0.666667   FULL 0.777778
RB-03   GENERIC 1.000000   SELECTIVE 1.000000   FULL 1.000000
RB-04   GENERIC 1.000000   SELECTIVE 1.000000   FULL 1.000000
```

Per-case semantic score:

```text
RB-01   GENERIC 1.000000   SELECTIVE 1.000000   FULL 1.000000
RB-02   GENERIC 1.000000   SELECTIVE 1.000000   FULL 1.000000
RB-03   GENERIC 1.000000   SELECTIVE 1.000000   FULL 1.000000
RB-04   GENERIC 0.800000   SELECTIVE 0.800000   FULL 0.800000
```

Frozen gate evaluation:

```text
absolute gates           FAIL
relative gates           FAIL
expansion gates          FAIL
positive value signals   0
advancement outcome      FAIL
```

Failed named gates:

```text
SPRA-G06
SPRA-G08
SPRA-G09
SPRA-G10
SPRA-G20
```

The classifier is therefore exactly:

```text
FAIL
```

No post-hoc reinterpretation is permitted.

---

## Failure attribution

### RB-02

The repeated SELECTIVE error was an over-escalation from useful model comparison to blocking work.

The two nonlinear model-comparison actions were expected to be `RECOMMENDED`. SELECTIVE labeled both `BLOCKING_REQUIRED` in all three repetitions and emitted both blocked scopes, while correctly keeping the tuning action `DEFER`red behind `model-family-selected`.

GENERIC and FULL_HORIZON made the same blocking escalation in two of three repetitions but were correct in the third. Consequently SELECTIVE was below the absolute per-case accuracy floor, crossed both frozen per-case non-inferiority margins, and produced more blocking-scope false positives than FULL_HORIZON.

This localizes the remaining problem to recommendation/blocking calibration rather than the already-supported DEFER trigger-pointer construct.

### RB-04

All three conditions were deterministically perfect but semantically scored `0.800000`. The blinded judge consistently found the training-only preprocessing/leakage-prevention obligation absent.

Because the same omission occurred in GENERIC, SELECTIVE, and FULL_HORIZON, it is treatment-invariant. The frozen absolute SELECTIVE gate nevertheless fails and contains no post-hoc ceiling exemption.

---

## Provenance instrumentation result

The architecture change that motivated Specification 019 worked as intended:

```text
SYSTEM
    owns exact supplied stable_key@revision_id identities
    owns methodology payload digest and byte count
    owns treatment provenance

MODEL
    owns recommendation content only
```

The full 36-output reasoner design completed without provenance-induced schema failures and with zero retries. The Specification 017 instrumentation defect is therefore closed at this bounded experiment layer.

This is an instrumentation result, not a positive recommendation-value signal.

---

## Preservation evidence

The complete raw result bundle was preserved before tuning at commit:

```text
f5fbef4d6384ee08e873cb1ef9ccb3ed8ec31f2f
```

Durable path:

```text
experiments/system_owned_provenance_recommendation_action_value/results/
    spec019-live-20260824-run-32664534864/
```

Stable interpretation:

```text
experiments/system_owned_provenance_recommendation_action_value/
    V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

The artifact manifest binds the preserved bundle to workflow run `32664534864`, artifact `9499756280`, frozen source `6b5e6237...`, and exact contained-file hashes.

---

## Promotion audit

### Promote

The following bounded lesson is retained as experimental/system-design evidence:

```text
exact supplied-context provenance should remain system-owned
rather than being a required duplicate model-authored result field
```

This does not require promotion of PR #33's recommendation/action semantics into accepted integration.

### Do not promote

Do not promote:

```text
Specification 019 recommendation/action seam
production REQUIRED/BLOCKING semantics
production recommendation ranking policy
SELECTIVE methodological context as recommendation-value evidence
production DEFER/NOT_NOW enums
automatic project mutation or execution
final provider/model policy
multi-agent recommendation architecture
```

### Historical integrity

Do not edit or rescore Specifications 015-017. Specification 017 remains incomplete historical evidence. Specification 019 remains the first complete matched system-owned-provenance rerun and is permanently `FAIL` under its frozen gates.

---

## Architectural consequence

The next scientific question is no longer provenance instrumentation.

The highest-value boundary is:

```text
what makes justified work merely RECOMMENDED
    versus genuinely BLOCKING_REQUIRED
for an exact defended downstream scope?
```

A future experiment should test that boundary prospectively with stronger explicit system-owned dependency/claim-scope structure or another bounded calibration mechanism, while retaining strong simpler controls.

No new provider call is authorized by this checkpoint. Any successor experiment must be separately preregistered, provider-free validated, and governed through the accepted live-launch control plane.

---

## Exact continuation

```text
1. reconcile README / KNOWLEDGE_MAP / CURRENT_STATE / OPEN_QUESTIONS / MAJOR_CHANGES to Checkpoint 166
2. retire the one-shot Specification 019 authorization and temporary control-plane helpers
3. close temporary launch/preservation issues while preserving their audit history
4. validate the exact reconciled feature head provider-free
5. close PR #33 without merge
6. design the next recommendation/blocking-calibration experiment prospectively
7. make no new provider call until that new contract and exact implementation boundary are frozen and green
```
