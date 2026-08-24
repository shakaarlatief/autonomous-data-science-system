# V1 RECOMMENDED versus BLOCKING_REQUIRED Calibration Diagnostic Result

**Date:** 2026-08-24  
**Benchmark:** `v1-blocking-calibration-diagnostic-v0.1`  
**Specification:** 020 v0.1  
**Frozen live source:** `82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a`  
**Launch issue:** #45  
**Launcher run:** `32701990350`  
**Live run:** `32701999678`  
**Live job:** `97355284139`  
**Artifact ID:** `9510887324`  
**Artifact SHA-256:** `35ed6b472eac22090e563bbafee30aab1b666c00453ebcfd8cd0a832b79be678`  
**Frozen advancement outcome:** **BLOCKING_BOUNDARY_SUPPORTED**

## 1. Execution integrity

The governed Specification 018 launcher accepted exactly one repository-authorized request and dispatched the independently validating Specification 020 target workflow at the exact frozen source.

The live workflow completed successfully:

```text
planned reasoner outputs       36
successful reasoner outputs    36
validated observations         36
provider attempts              36 / 45 maximum
failed attempts                0
retries                        0
complete scored design         true
execution integrity            true
```

The exact raw artifact was preserved before scientific interpretation at:

```text
experiments/blocking_calibration/results/spec020-live-20260824-run-32701999678/
```

That directory contains the original GitHub Actions `artifact.zip`, all extracted result files, and a manifest with exact digests.

## 2. Frozen hard gates

Every preregistered Specification 020 gate passed without post-result modification:

```text
BC-G01 structured validity                       PASS
BC-G02 aggregate exact disposition accuracy      1.000000 >= 0.950000
BC-G03 every variant majority-correct            12 / 12 variants at 3 / 3
BC-G04 every pair both sides majority-correct    6 / 6 pairs, both sides at 3 / 3
BC-G05 exact joint blocking pointers             1.000000
BC-G06 RECOMMENDED null-pointer correctness      1.000000
```

Exact component metrics were also perfect:

```text
blocking requirement-pointer accuracy   1.000000
blocked-scope pointer accuracy           1.000000
joint blocking-pointer accuracy          1.000000
RECOMMENDED null-pointer correctness     1.000000
```

The mechanically determined frozen outcome is therefore:

```text
BLOCKING_BOUNDARY_SUPPORTED
```

## 3. Exact contrastive result

All six deliberately heterogeneous pairs separated perfectly across all repetitions:

```text
BC-01  prediction-time feature availability
BC-02  temporal validation sensitivity
BC-03  missing-data treatment sensitivity
BC-04  subgroup error analysis
BC-05  probability calibration assessment
BC-06  nonlinear model-family comparison
```

For every pair:

```text
BLOCKING_REQUIRED side   3 / 3 exact
RECOMMENDED side         3 / 3 exact
```

All eighteen expected-BLOCKING_REQUIRED outputs identified both the exact unresolved requirement and the exact active defended downstream scope. All eighteen expected-RECOMMENDED outputs returned both blocking pointers as null.

## 4. Supported conclusion

The strongest supported conclusion is:

> A dependency-backed `BLOCKING_REQUIRED` definition is operationally representable, and the frozen reasoner can distinguish it from `RECOMMENDED` on the frozen deliberately unambiguous contrastive project microstates when the unresolved requirement, active defended downstream scope, dependency relation, and resolving action are explicit.

This supports a bounded future experiment-design rule:

```text
blocking should not be represented by urgency or priority alone

BLOCKING_REQUIRED-like test cases
    should identify an exact unresolved requirement
    + an exact active defended downstream scope
    + an explicit scope DEPENDS_ON requirement relation
    + the action that resolves that requirement
```

The supplied requirement, scope, action, and relation identities remain system-owned project/evaluator state. The model selects among supplied identities rather than manufacturing authoritative project relations.

## 5. Failure attribution for Specification 019

Specification 019 remains an immutable historical `FAIL` and is not rescored.

This prospective diagnostic narrows the earlier RB-02 interpretation:

```text
taxonomy inseparability under explicit dependency-backed semantics
    less likely

fixed reasoner inability to apply the distinction on explicit cases
    less likely

insufficiently explicit blocked-scope / requirement construction in the
historical recommendation-value benchmark
    remains consistent with the observed RB-02 over-blocking
```

This is not proof that the historical Specification 019 expected labels were wrong. It shows that a stronger relational construction makes the distinction objectively testable on the new frozen cases.

## 6. Non-conclusions

This result does not establish:

```text
production BLOCKING_REQUIRED or RECOMMENDED enums
production blocking policy
SELECTIVE methodological-context recommendation value
recommendation ranking
open-world concern/action generation
automatic project mutation or execution
final provider/model selection
multi-agent recommendation architecture
```

In particular, the core system-value question remains open:

> Does selective explicit methodological knowledge improve downstream recommendation/action quality beyond a strong generic reasoner when recommendation semantics and blocking relations are constructed cleanly?

## 7. Next legitimate boundary

A later recommendation-value experiment may now use newly frozen cases satisfying the stronger relation-backed blocking construction, but only under a separate preregistered contract.

Before that experiment begins, the project should:

```text
1. complete Specification 020 canonical/result reconciliation;
2. retire the one-shot live authorization and temporary live-control helpers;
3. validate and promote the bounded diagnostic evidence through PR #44;
4. add the small machine-checkable current-routing consistency guard justified by observed routing drift;
5. only then freeze the next recommendation-value experiment.
```
