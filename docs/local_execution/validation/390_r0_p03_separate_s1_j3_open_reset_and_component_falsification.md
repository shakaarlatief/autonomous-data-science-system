# Validation 390: Separately evaluated experimental S1 currentness/J3, with OPEN_RESET and ALL_REQUIRED falsifiers

**Date:** 2026-11-15
**Status:** EXPERIMENT_ONLY_S1_ACTIVATED / OPEN_RESET_NO_CARRY_PASS / S1_ALL_REQUIRED_4_OF_4_PASS / 77_ADVERSARIAL_TESTS_PASS / PRODUCTION_J3_FALSE
**Research:** 693. **Checkpoint:** 954. **MC-0030:** Message 107.
**Scope:** Validate the exact source-relative J1/J2/G006/G013/G009 J3 predicate without using the source author's FULL or derived manifest as acceptance authority.
**Authority:** Bounded experiment-only semantic evaluation, not an independently authored/blind reference, production S1/J3, formal comparative score, physical architecture or migration authority.

Sources:

    owner accepted J1 proposal Git ed1c379f31fadc47a62189363720e0cfb9390afa
    accepted weak source-owner policy Git 872d461aecf1cbd4a6a18249e9e75050a5e97773
    preaction composite realizer Git c523340a20dd7628bc2a470594e28b48929a29dc
    source event Git ca91cbc27dc47f6efa383a788d4c9c02689bb9bd
    execution evidence Git 338e591c3ba08bc1ca87af44df678086164a3f4b
    postexecution COVERS Git d4ef4d3ec259c2d578ad412f197dd49211225bc7
    admitted experimental J2 Git 14f48760b1e23d50cb2d30820817239c1d1ee7f0
    admitted experimental J2 receipt SHA-256 3e9e5c6ad65f381e50cd7605f0abdb1679d47d9fa59ec14311797554883fdbad
    new S1 J3 receipt SHA-256 1b31365160e29b902d578222a8dc39e15c55b49e0e592448baeada13284b4341

Reproduce with:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_real_pk_delegated_s1_j3_lifecycle_v01
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=3 -p no:cacheprovider tests/unit/test_r0_p03_v03_real_pk_delegated_s1_j3_lifecycle_v01.py
```

The first complete J3 test suite returned **77 passed in 12.04s**, and an amended strict-source-field regression returned **77 passed in 12.54s**. Source-replay after the amended evaluator again produced identical immutable J3 result with no conflict. Adjacent completed tests confirmed J2 admission **60 passed in 14.62s** and exact real source event **20 passed in 18.09s**. This validates three relevant test families, not the complete ADS test suite.

Pure semantic predicate controls exercised original J1 S0 currentness, accepted J1 effect types, two E01 components, four E02 ALL_REQUIRED components, E03 REPLACE/OPEN_RESET exact lineage, E04 false-authority prohibition, source event/Git digest identity, weak-assurance J2 qualification, absence of production J2, and source authored status non-authority.

The 16 combinations of intentionally wrong G006 identity, G013 affected view, G013 incremental/full equality and G013 manifest freshness verify:

- No failures: S1 ACTIVE, E02+E04 current, 4/4 S1 PASS.
- Failed G006 identity: source transition not qualified for activation, S0 current, S1 NOT_ACTIVATED.
- Other failed new-event components: S1 remains current under qualified event, but J3 HOLD (not incorrectly SATISFIED).
- In every S1-active case: realization opens with zero E01 carryover; source author COVERS flags alone add no component credit.

Additional negatives cover forged independent actor authentication, changed owner policy or natural-owner evidence, retrospective S0/948 source recrediting, altered E03 lifecycle, prohibited path or generated view as governing acceptance, missing fields, invalid SHA-256-like digest, injected extra authority metadata, and source self-activated J3. All fail closed or remain HOLD.

Observed exact result:

    S1=ACTIVATED_IN_EXACT_BOUNDED_EXPERIMENTAL_S1_WORLD
    J3=SATISFIED_EXPERIMENT_ONLY_SOURCE_RELATIVE_WEAK_ACTOR_ASSURANCE
    successor_initial_component_credit=0
    current_effects=E02,E04
    previous_S0_evidence_carryover=false
    S1_ALL_REQUIRED=4_OF_4_PASS
    authenticated_model_actor=false
    production_J3=false
    formal_R0_P03=INCOMPLETE

The evaluator is structurally distinct from the source-author executable and from J2 admission, but is authored/tested in the same exposed ChatGPT collaboration. That is mechanical evaluator separation, not independently authored blind scientific reference or independent human/model identity attestation.

Final repository integrity, branch publication and CI status are separate postflight checks and should be verified on the exact committed revision.
