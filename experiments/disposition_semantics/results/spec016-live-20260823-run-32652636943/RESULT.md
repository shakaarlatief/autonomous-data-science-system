# V1 Disposition Semantics Diagnostic Result

**Benchmark:** `v1-disposition-semantics-diagnostic-v0.1`  
**Source head:** `7db27fd35151c10cdb3562cdf4410fb8f4b09e8b`  
**Started:** 2026-08-23T16:45:15.780363+00:00  
**Finished:** 2026-08-23T16:46:37.818235+00:00  
**Advancement outcome:** `DISPOSITION_BOUNDARY_SUPPORTED`  
**Overall frozen gate passed:** True

## Execution

```text
successful outputs  36 / 36
provider attempts   36 / 45
validated outputs   36
failed attempts     0
```

## Frozen gates

```text
completed                         True
structured validity               True
aggregate exact accuracy          1.000000
aggregate accuracy gate           True
variant majority gate             True
pair polarity gate                True
DEFER pointer accuracy            1.000000
DEFER pointer gate                True
NOT_NOW null-pointer accuracy     1.000000
NOT_NOW null-pointer gate         True
```

## Historical Specification 015 diagnostic

This diagnostic does not rescore Specification 015. It only tests whether its historical RA-02 expected-DEFER examples satisfy the stronger construction rule used by Specification 016.

```text
add-generic-bagging-baseline: NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER
plot-all-feature-histograms-before-shortlist: NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER
```

## Audit artifacts

```text
reasoning_plan.json
reasoner_attempts.jsonl
result.json
RESULT.md
```

This report is generated mechanically from the frozen Specification 016 runner. Raw attempt records remain the provider-level audit source.
