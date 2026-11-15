# Validation 387: One-event delegated source/realizer scope preflight

**Date:** 2026-11-15
**Status:** FROZEN_SCOPE_SOURCE_BOUND / EXPERIMENT_OWNED_COMPOSITE_EXECUTABLE_PRESENT / 28_PREACTION_TESTS_PASS / REAL_EVENT_NOT_RUN
**Research:** 690. **Checkpoint:** 951. **MC-0030:** Message 104.
**Scope:** Validate the exact new composite execution source and source-owner event contract, without creating or simulating the accepted policy's one permitted real source event.
**Authority:** Preaction design and positive synthetic G006 compatibility only; no qualified new event, J2/S1/J3 or formal navigation result.

Bound inputs: owner policy acceptance Git `872d461aecf1cbd4a6a18249e9e75050a5e97773`, binding hash `beabc995359f79fe8d4f659efa76ff912b8ec02de74397d3656c29438215672d`, frozen source scope hash `0fefd227092177e2e444a63fdb5b1ee8a7200ca75524145fe13e2c4a52d549d7`, and immutable previous source blob hash `6e0e90f4cf3b210adfac2a8d762ec6527ad260e34bad32aa5ceabf87c0ad5bef`.

Reproduce:

```powershell
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=2 -p no:cacheprovider tests/unit/test_r0_p03_v03_real_pk_delegated_s1_composite_realizer_v01.py
```

Observed: **28 passed in 14.89s**. Tests include false FULL/COVERS and J3 preexecution forgery, wrong accepted J1, wrong policy binding and event parent, missing scope realizer, changed authored identity, wrong carrier provenance, and synthetic source-pair execution by the actual production G006 identity index without real future Git event. They do not score primary cases, infer model/owner cryptographic authentication or qualify production G013 success for the future event.

The executable is authored before the real source action and will be verified again from its exact freeze commit Git blob at event execution. Its supporting G010 fixture is not the formal original ADS corpus.

Postfreeze Git event and production G013 evidence: **NOT OBSERVED**. The actual event is authorized only if this code/scope are published first, and only its three exact source paths are changed. Any failure will retain explicit HOLD rather than certifying J2 or J3.
