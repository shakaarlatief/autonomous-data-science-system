# Validation 389: Exact postexecution COVERS, Git ancestry and evidence-replayed experimental J2

**Date:** 2026-11-15
**Status:** DISTINCT_POSTEXECUTION_GIT_COVERS_PASS / FOUR_NEW_EVENT_COMPONENTS_REPLAYED / ONE_EXPERIMENT_ONLY_RELATIONAL_J2_QUALIFIED_WITH_WEAK_ASSURANCE / J3_HOLD
**Research:** 692. **Checkpoint:** 953. **MC-0030:** Message 106.
**Scope:** Validate a later single-path source-owner COVERS declaration and qualify one bounded natural-owner RELATIONAL J2 under the owner's expressly weaker experiment-only policy.
**Authority:** No independent model actor or source-owner signing, no production J2, no S1 or J3 automatic activation, no formal P03 or physical-selection result.

Exact binding:

    owner policy accepted in Git 872d461aecf1cbd4a6a18249e9e75050a5e97773
    source scope freeze c523340a20dd7628bc2a470594e28b48929a29dc
    actual one source event ca91cbc27dc47f6efa383a788d4c9c02689bb9bd
    execution evidence commit 338e591c3ba08bc1ca87af44df678086164a3f4b
    distinct COVERS declaration commit d4ef4d3ec259c2d578ad412f197dd49211225bc7
    source declaration SHA-256 a1fd016deb19d1468bfbbe2810fccd1bb5c0487711adc4d9dc17bb77901c2d6f
    replayed engineering receipt SHA-256 47e41bb4c0fde09b9d245751ab7d727e81a9b7d78ec557053828cebad34e42f2
    J2 admission receipt SHA-256 3e9e5c6ad65f381e50cd7605f0abdb1679d47d9fa59ec14311797554883fdbad

Exact execution:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_real_pk_delegated_s1_j2_admission_v01
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=2 -p no:cacheprovider tests/unit/test_r0_p03_v03_real_pk_delegated_s1_j2_admission_v01.py
```

Observed source-relative J2 receipt:

    status=QUALIFIED_SOURCE_RELATIVE_EXPERIMENTAL_J2_WEAK_ACTOR_ASSURANCE
    qualified_experimental_relational_j2_count=1
    all_component_evidence_replayed=true
    one_fact_tuple_in_bounded_source_world=true
    independent_model_identity_proven=false
    production_j2_qualified=false
    previous_s0_execution_credited_to_s1=false
    prior_948_j2_upgraded=false
    s1_activated_by_this_j2_verifier=false
    j3_satisfied_by_this_j2_verifier=false

60 focused tests PASS. These include negative tests for source author masquerading as independently authenticated model, inherited production G006/G013 author, mutated exact J1 or policy, forged future event identity, substituted execution receipt, source-author self-declaration of qualified J2/S1/J3, omitted components, contradictory currentness and stale prior manifest. All tests are subsystem-level, not independent blinded R0-P03 scoring.

Qualification interpretation: the exact ChatGPT source author did author the new composite experimental runner in this interaction, but a Git commit does not prove model-session identity. The owner specifically accepted this **lower assurance class** for one forward experiment source event, so the result is one *source-relative experiment-only* J2. It is not strongly authenticated production J2. This precise weaker provenance must remain visible in all future shared-world references and B0–B4 arms.

No J3 was run or certified by this J2 verifier. Later formal currentness and lineage evaluation requires a distinct evaluator.
