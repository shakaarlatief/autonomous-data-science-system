# V1 Disposition Semantics Diagnostic Result

**Date:** 2026-08-23  
**Benchmark:** `v1-disposition-semantics-diagnostic-v0.1`  
**Specification:** 016 v0.1  
**Frozen source head:** `7db27fd35151c10cdb3562cdf4410fb8f4b09e8b`  
**GitHub Actions run:** `32652636943`  
**Job:** `frozen-live-experiment` (`97226508062`)  
**Artifact ID:** `9496624273`  
**Artifact SHA-256:** `edbdb797b433ee93d0c7e353cf7b214c93d004794ebdc58487e54fcace056660`  
**Frozen advancement outcome:** **DISPOSITION_BOUNDARY_SUPPORTED**

## 1. Execution integrity

The live workflow completed successfully from the exact pre-live frozen branch head. Before provider execution it reran the frozen targeted provider-free suite and obtained:

```text
15 passed
```

Live execution then produced:

```text
reasoner outputs       36 / 36
validated observations 36 / 36
provider attempts      36 / 45 maximum
failed attempts        0
retries                0
complete scored design true
```

The exact downloaded artifact is durably preserved at:

```text
experiments/disposition_semantics/results/spec016-live-20260823-run-32652636943/
```

The preserved `artifact.zip` is the complete GitHub Actions bundle. `MANIFEST.md` records the artifact digest, extracted-file SHA-256 values, exact source identities, and frozen reasoning-plan digest.

## 2. Frozen hard gates

Every Specification 016 hard gate passed:

```text
DS-G01 structured validity             PASS
DS-G02 aggregate exact accuracy        1.000000 >= 0.950000
DS-G03 every variant majority-correct  12 / 12 variants at 3 / 3
DS-G04 every pair polarity-correct     6 / 6 pairs, both sides at 3 / 3
DS-G05 exact DEFER trigger pointer      1.000000
DS-G06 NOT_NOW null pointer             1.000000
```

The mechanically generated result is therefore:

```text
DISPOSITION_BOUNDARY_SUPPORTED
```

No post-result threshold, expected label, pointer truth, prompt, model setting, repetition count, or retry rule was changed.

## 3. Exact contrastive result

All six deliberately heterogeneous pairs separated perfectly across three repetitions per side:

```text
DS-01 model tuning
DS-02 subgroup error analysis
DS-03 feature-interaction engineering
DS-04 missingness sensitivity
DS-05 probability calibration
DS-06 distribution evidence
```

For all eighteen expected-DEFER observations, the reasoner returned both:

```text
disposition = DEFER
exact expected defer_until_id
```

For all eighteen expected-NOT_NOW observations, the reasoner returned both:

```text
disposition = NOT_NOW
defer_until_id = null
```

The tested operational boundary was:

```text
DEFER
    action already justified in the represented plan
    + exact unresolved activating dependency/trigger
    + action becomes current next work after trigger

NOT_NOW
    no material current justification
    + no represented supplied trigger that activates the action as next work
```

## 4. Failure attribution for Specification 015

Specification 015 remains an immutable historical `FAIL` and is not rescored.

Its two disputed RA-02 expected-DEFER examples were mechanically classified by the provider-free Specification 016 admissibility audit as:

```text
add-generic-bagging-baseline
    NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER

plot-all-feature-histograms-before-shortlist
    NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER
```

The live result therefore narrows the earlier failure attribution:

```text
taxonomy inseparability under explicit relation-backed semantics
    less likely

fixed reasoner inability on explicit cases
    less likely

insufficiently explicit historical benchmark state
    remains consistent with the old discrepancy

whether SELECTIVE adds downstream recommendation value
    still unresolved
```

This does not prove that Specification 015's historical labels were wrong. It shows that the stronger relation-backed distinction can be made objectively testable when the activating dependency is represented explicitly.

## 5. Supported architectural conclusion

The strongest supported conclusion is:

> A dependency-backed `DEFER` definition is operationally representable, and the frozen reasoner can distinguish it from `NOT_NOW` on deliberately unambiguous contrastive project microstates.

For future ADS recommendation/action experiments, sequencing should therefore not be encoded by a bare label alone. A DEFER-like state must carry a concrete represented activating dependency/trigger if deterministic separation from NOT_NOW-like absence of current justification is expected.

This result is consistent with Foundation 018's distinction between project objects and relations.

## 6. Non-conclusions and next boundary

This diagnostic does not establish:

```text
production DEFER / NOT_NOW enums
Specification 015 rescoring
SELECTIVE recommendation value
open-world action generation
production recommendation ranking
project-state mutation or automatic execution
final provider/model selection
```

The next justified experiment may return to recommendation/action value only through a separately preregistered contract whose sequencing cases explicitly satisfy the stronger dependency-backed construction rule. That experiment must still test whether SELECTIVE contributes value beyond a strong GENERIC reasoner rather than merely repeating the construct-validity result.
