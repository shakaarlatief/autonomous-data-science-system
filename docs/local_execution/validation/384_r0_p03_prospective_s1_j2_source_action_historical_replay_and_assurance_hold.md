# Validation 384: Prospective S1 source-owner Git event, bounded compatibility repair and J2 HOLD

**Date:** 2026-11-15
**Status:** SOURCE_GIT_EVENT_COCOMMIT_PASS / HISTORICAL_REPLAY_COMPATIBILITY_REPAIRED / 184_FOCUSED_REGRESSIONS_PASS / NATURAL_OWNER_J2_UNQUALIFIED
**Research:** 687. **Checkpoint:** 948. **MC-0030:** Message 101.
**Scope:** Verify the exact prospective accepted-S1 source-owner event and ensure historical Git-pinned P03 source replay remains reconstructable after a later source carrier move. Preserve the separate failed-first-broad-run and later passing segmented-regression evidence.
**Authority:** Actual bounded Git/source/test evidence, not an independently authenticated source-owner assertion, S1 activation, governing J3, full regression verdict, completed formal R0-P03, physical selection or production mutation.

## Source anchor

    pre-event experiment contract commit f13046f579e614870f7fe255d66c7a55368e1e65
    pre-event fixture correction       2def5a1751f579138cf67047d5f68362eff92af4
    real source event commit           faf8ff2686c6b09f53d3569470cf2057c11e5971
    real event parent                  2def5a1751f579138cf67047d5f68362eff92af4

Exactly three path changes were verified from Git: previous carrier deleted, prospective new carrier added, source-local COVERS proposal added. The new source preserves the previously authored semantic ID and governed_source field values. The claim explicitly targets all four exact accepted S1 components but marks coverage pending actual execution and owner qualification.

    previous carrier SHA-256       d618807f510a4400ec62e1d25b931c6810e9b4928e8c348317ecd54db89d8b32
    new carrier SHA-256            6e0e90f4cf3b210adfac2a8d762ec6527ad260e34bad32aa5ceabf87c0ad5bef
    colocated declaration SHA-256  0befd1310967547a1063d04c41863f63fea5a55daf682409683ce2f99642a95c
    derived assay receipt SHA-256  b64569b802f5d9d6de2e6d975ba8a3e462698ba696752afe0392c4abd0f565ac

Reproduction:

```text
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.v03_real_pk_prospective_j2_source_assay_v01 --event-commit faf8ff2686c6b09f53d3569470cf2057c11e5971
```

Observed receipt status:

    SOURCE_COCOMMIT_AND_GIT_TRANSITION_VERIFIED_J2_OWNER_ASSURANCE_HOLD
    git_observable_verified=true
    source_owner_claim_independently_authenticated=false
    claimed_relational_J2_qualified=false
    component_execution_verified_for_this_transition=false
    S1_activated=false
    J3=HOLD_J2_OWNER_ASSURANCE_AND_NEW_EVENT_EXECUTION

## Honest failing and repaired regression sequence

The initial broad run of the nine relevant current P03 source-world test files reported **2 FAIL, 57 ERROR** because older `committed_carriers()` replay required the former current source file to remain physically present. No failure was reclassified as PASS. The implementation was changed to verify the historical source from its immutable Git object and check live worktree bytes only if the historical path exists. The adversarial stale-worktree case was adjusted so it still tests rejection when a conflicting worktree carrier is actually present. A positive later-move case was added.

A combined re-execution timed out at the 30-second command ceiling, so it does not establish a full aggregate PASS. Three isolated passing runs subsequently covered the relevant test files:

```text
.venv\Scripts\python.exe -m pytest -q -p no:cacheprovider \
    tests/unit/test_r0_p03_v03_real_pk_source_transition_v01.py \
    tests/unit/test_r0_p03_v03_real_pk_prospective_j2_source_assay_v01.py \
    tests/unit/test_r0_p03_v03_real_pk_source_owner_coverage_preflight_v01.py \
    tests/unit/test_r0_p03_v03_real_pk_common_world_preflight_v01.py
    75 passed

.venv\Scripts\python.exe -m pytest -q -p no:cacheprovider \
    tests/unit/test_r0_p03_v03_real_pk_g013_isolated_source_refresh_v01.py
    15 passed

.venv\Scripts\python.exe -m pytest -q -p no:cacheprovider \
    tests/unit/test_r0_p03_v03_real_pk_accepted_j1_projection_v01.py \
    tests/unit/test_r0_p03_v03_real_pk_common_world_g013_overlay_v01.py \
    tests/unit/test_r0_p03_v03_real_pk_semantic_candidate_audit_v01.py \
    tests/unit/test_r0_p03_v03_real_pk_semantic_j1_owner_proposal_v01.py
    94 passed
```

The 184 PASS total consists of distinct completed pytest batches. The test execution used the repository's existing `.venv` Python because a `uv` invocation was blocked by access to the machine-level cache under the current restricted execution surface. That cache restriction is not a model test failure or an authorization to widen file access.

## Repository-integrity routing trigger

The first post-event `scripts/check_repository_integrity.py` run returned PUBLIC_REPOSITORY_INTEGRITY=FAIL because `docs/KNOWLEDGE_MAP.md` still referenced a physically deleted carrier file as a currently available direct route. Its route was repaired to the new experimental source. The historic source can still be retrieved from the exact old Git commit and replay receipt; no stale material was silently reintroduced as an additional current carrier.

Final repository-integrity and remote publication results must be evaluated separately at the complete preserved head. Never infer an online GitHub CI result from local pytest execution.

## Qualification limitations

- Exact Git history and contemporaneous source-claim co-location are OBSERVABLE facts. They do not authenticate ChatGPT as natural owner.
- The COVERS declaration is explicitly an unqualified RELATIONAL source-author proposal, not admitted J2.
- Prior G006 and G013 executed evidence is pinned to the previous transition, not automatically to this new event.
- No new true G006/G013 test has yet been performed for the new S1 event, and S1 was not activated or mechanically certified under J3.
- No formal B0-B4 architecture navigation arms, gold or scores were created.
