# Validation 388: Postfreeze delegated source event and actual production-backed G006/G013 replay

**Date:** 2026-11-15
**Status:** REAL_GIT_EVENT_PASS / PRODUCTION_G006_PASS / PRODUCTION_G013_SELECTED_FULL_EQUIVALENCE_PASS / OLD_STALE_NEW_FRESH / J2_J3_HOLD
**Research:** 691. **Checkpoint:** 952. **MC-0030:** Message 105.
**Scope:** Reproduce exact delegated one-event source history and execute production G006 and G013/G009 on new source pair; reject false J2/activation claims.
**Authority:** Bounded engineering evidence, not independent source-actor proof, J2 relation, S1/J3 activation, formal P03 scoring or production approval.

    accepted-policy Git commit 872d461aecf1cbd4a6a18249e9e75050a5e97773
    frozen source/realizer commit c523340a20dd7628bc2a470594e28b48929a29dc
    actual source event commit ca91cbc27dc47f6efa383a788d4c9c02689bb9bd
    exact event parent c523340a20dd7628bc2a470594e28b48929a29dc

The source event itself contains exactly D predecessor carrier, A delegated_s1 successor carrier, A co-committed `INTENT_NOT_J2_COVERS` declaration. Nothing else changed in that event. The source actor owns the experimental composite orchestration, not G006/G013 production implementation; actor authenticity is weaker, not independently verified.

Reproduction:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_real_pk_delegated_s1_composite_realizer_v01 --event-commit ca91cbc27dc47f6efa383a788d4c9c02689bb9bd --scope-commit c523340a20dd7628bc2a470594e28b48929a29dc
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=2 -p no:cacheprovider tests/unit/test_r0_p03_v03_real_pk_delegated_s1_real_event_v01.py
```

The direct executable completed twice without drift against its create-only receipt (SHA-256 `47e41bb4c0fde09b9d245751ab7d727e81a9b7d78ec557053828cebad34e42f2`). The exact real-event suite completed **20 passed in 15.96s**.

    same authored semantic ID: PASS
    G006 current and historical source continuity: PASS
    G006 identity serialization order invariance: PASS
    G013 affected view: p03_delegated_s1_inventory
    G013 selection reason: DEPENDENCY_BINDING_CHANGED
    G013 selected build equals full G009 current build: PASS
    previous generated manifest: STALE
    current generated manifest: FRESH
    prior source absent from generated current view: PASS
    production source modified: NO
    whole ADS original corpus rebuilt: NO
    formal B0-B4 scored: NO
    qualified RELATIONAL J2: 0
    S1 activation: NOT_ACTIVATED
    J3: HOLD

The new event is source-revision specific, not an assertion about other ADS source transitions. Temporary isolated Git commits were produced with deterministic **test-only** timestamps. The reused G010 schema-supporting fixture remains not a formal P03 original corpus; this distinction is retained in the receipt. A future code change in production helper closure could make later fresh reruns differ; the currently observed output is bound to the exact source event and preserved receipt, and subsequent implementation updates must not be silently interpreted as requalification of this run.

A first postevent public integrity call failed specifically because Knowledge Map still routed to the now-deleted physical predecessor. The immediately following preservation change repairs that live locator without rewriting this immutable three-path event. Final repository integrity and GitHub CI must be separately observed on the eventual published preservation commit.
