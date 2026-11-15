# Validation 383: Actual G013 real-source projection, selected/full equivalence and freshness

**Date:** 2026-11-15
**Status:** REAL_ORIGINAL_GIT_SOURCE_BYTES_VERIFIED / ORIGINAL_SEMANTIC_ID_PRESERVED / PRODUCTION_G013_SELECTED_FULL_EQUIVALENCE_PASS / PRIOR_MANIFEST_STALE / CURRENT_MANIFEST_FRESH / J2_AND_J3_UNQUALIFIED
**Research:** 686. **Checkpoint:** 947. **MC-0030:** Message 100.
**Scope:** Execute unmodified G009/G013 code against exact committed P03 before/after real source declarations in an isolated schema-admitted Git root, verify stale/fresh output and exact accepted S1 observable components; expose result in common unscored V03 semantic-world input.
**Authority:** Actual engineering execution evidence, not formal navigational comparison, new J2 owner acceptance, activated S1, production acceptance or physical architecture decision.

## A. Original Git and isolated execution setup

Original real source before:

    Git 10cad3cb0a885135579f00f3a887a3c090f65352
    SHA-256 effcbcf0bdd54576f9611a5381ab900490561cd762fb3f1985096b6ac92703b2

Original real source after:

    Git cac152cfe6c2133ffd46cf7fa3b7e0b99d015cb4
    SHA-256 d618807f510a4400ec62e1d25b931c6810e9b4928e8c348317ecd54db89d8b32

These are genuine source Git objects from the live ADS repository. The isolated temporary Git root incorporates their complete exact bytes as noncanonical sidecar evidence, unchanged governed_source fields as schema-valid docs/ declarations, actual production G009/G013 code/schema closure, a source-authored identity_transition.v1 and the original G010 eight-carrier qualification fixture. It does not amend the live repository's production source state.

Temporary Git commit IDs after intentionally fixed **sandbox-only** dates, reproducible across two executions:

    before 22ff8fdafdd0db4160eb1b4798cb4c6259ea4b82
    after  df8423466976add577b128924a635bf1918ead0e

A first prepublication run had nondeterministic temporary Git times. The harness and prepublication receipt were corrected, then the output and hashes were repeated without drift.

## B. Executed production implementation and result

Calls: production validate_repository, commit_snapshot, refresh.refresh_views, generation.generate_views and check_view_freshness.

    isolated previous source admission PASS
    isolated current source admission PASS
    selected view p03_real_semantic_inventory
    selection reason DEPENDENCY_BINDING_CHANGED
    full fallback false
    G013 incremental selected result EXACTLY EQUAL full G009 current ViewBuildResult
    original generated manifest at new state STALE
    new generated manifest at new state FRESH

Both generated source inventories have exactly one row for P03PKA.G006.IDENTITY.CONTINUITY. Its content_digest is adb61c6f55e9844f2e12c0550dae96f0692046571de2ebc9473b2fdd89832b95 in both, while the path changes from docs/p03_real_source/initial/identity.json to docs/p03_real_source/current/identity.json. The old path is absent from the new generated inventory.

The evidence is bound to all four exact accepted S1 component names and marked OBSERVABLE_EXECUTED, **not qualified J2**.

## C. New immutable execution and common-world evidence

    experiments/r0_p03_navigation_probe/v03_real_pk_g013_isolated_source_refresh_v01.py
    experiments/r0_p03_navigation_probe/v03_real_pk_g013_isolated_source_refresh_result_v01.json
    tests/unit/test_r0_p03_v03_real_pk_g013_isolated_source_refresh_v01.py

    experiments/r0_p03_navigation_probe/v03_real_pk_common_world_g013_overlay_v01.py
    experiments/r0_p03_navigation_probe/v03_real_pk_common_world_g013_overlay_result_v01.json
    tests/unit/test_r0_p03_v03_real_pk_common_world_g013_overlay_v01.py

Receipt byte SHA-256:

    594eecaef1c770a3545ef2664dbe47df1c8fb74e069a7e2cd7f1a9cc230b50e2

Earlier Research 685 common world byte SHA-256:

    db9ca1a2ac337710637fa2a9bb9beecb5c8da701168b5333ee09f195608be42e

New receipt/overlay each has explicit -text Git attributes so Windows LF conversion cannot silently change a pinned evidence digest.

## D. Completed focused tests

    Direct G013 real-source execution: PASS
    Reproduced deterministic temporary Git commit and view digest: PASS
    Exact G013 test suite: 15 PASS
    Exact common-world G013 overlay test suite: 10 PASS

The G013 suite checks production API/full-build use, exact two real original Git commit/hash anchors, semantic ID continuity in generated outputs, source path change without identity change, affected view, full equivalence, stale/fresh state, four accepted S1 component names, transparent G010 supporting fixture, absence of unauthorized J2/J3/S1, source hash drift and forged effect/owner facts rejected. The overlay suite checks unchanged common J1/G006, original 19-source catalog, exact digest-bound G013 evidence, proper unqualified J2 and retained R0-P03 study boundaries.

The 25 new passing tests are engineering regressions, not twelve independent primary navigation tasks or nine legacy reference questions.

## E. Explicit limitations and next steps

The main ADS source universe is **not** globally G013 validated by this isolated test, and the eight preexisting docs/DECISIONS.md digest mismatches from Research 685 remain historical diagnostic observations. The supporting eight G010 carriers are **not** formal P03 original ADS carriers or replacement gold.

No independent actual source-owner COVERS qualification was received. The earlier S0 author proposal is recorded in a later Git commit than the original source-replacement event; it cannot be promoted as a contemporaneous signer receipt. S1 is accepted but not yet activated, J3 stays HOLD, and the one formal R0-P03 comparison remains INCOMPLETE.

Final postflight of routing, Knowledge Map, checkpoints, collaboration, repository integrity, source-byte checks and Git publication will be appended in the Checkpoint 947 publication report. No physical architecture selected.

    ACTUAL_REAL_SOURCE_G013=PASS
    OLD_MANIFEST=STALE
    CURRENT_MANIFEST=FRESH
    S1_ACCEPTED_COMPONENT_OBSERVATIONS=FOUR
    QUALIFIED_RELATIONAL_J2=ZERO
    S1_ACTIVATED=false
    J3_CERTIFIED=false
    FORMAL_P03=INCOMPLETE
    PHYSICAL_ARCHITECTURE_SELECTED=false

## F. Final local prepublication qualification and reproducibility

All relevant source-world and governance checks have been rerun after the Research 686, Checkpoint 947, MC-0030 Message 100 and routing updates.

| Executed regression group | Outcome |
| --- | --- |
| New actual production G013 real-Git-source projection tests | 15 PASS |
| New G013 common-world overlay tests | 10 PASS |
| Existing accepted PKA J1, actual Git G006 identity, S0 owner-claim and common-world suites | 65 PASS |
| Research 684 original source-audit/owner proposal suites | 68 PASS |
| Existing collaboration identity, routing, continuity and repository-integrity suites | 73 PASS |
| Research 674 original real source-frame and Research 676 accepted D1 experimental effect suites | 44 PASS |
| **Total distinct regression cases** | **275 PASS** |

The 275 cases are across six disjoint selected successful pytest invocations, not formal R0-P03 navigation scoring. All test temporary roots created for Checkpoint 947 were removed. One initial aggregate integrity-script invocation exceeded the 30-second Runtime Bridge limit without a checker outcome; a separate invocation completed and reported PUBLIC_REPOSITORY_INTEGRITY=PASS. The initial timeout was not counted as an assertion failure or a passing check.

Repository guards completed:

- Current routing consistency PASS, checkpoint 947, outcome INCOMPLETE.
- Knowledge Map integrity PASS, research 686 and 948 numbered checkpoint records.
- Checkpoint metadata 948/948 PASS.
- Model collaboration state 28 records PASS.
- scripts/check_repository_integrity.py PUBLIC_REPOSITORY_INTEGRITY=PASS.
- git diff --check exit 0, only advisory Windows line-ending warnings.
- The two new JSON evidence files are LF-only and explicitly text-unset by .gitattributes.

Exact new receipt byte SHA-256 values:

    G013 source execution:
    594eecaef1c770a3545ef2664dbe47df1c8fb74e069a7e2cd7f1a9cc230b50e2

    Common-world G013 overlay:
    b7e14a6a42076b752830bb0ae8075a478d4b63600cb2a5e3360185f8cbb805f2

These are durable prepublication engineering evidence digests, not model-author identity proofs, owner J2 signatures or authorization to score an arm. The G010 fixture's role, the existing whole-ADS digest diagnostics and the S1/J3 HOLD status remain unchanged.
