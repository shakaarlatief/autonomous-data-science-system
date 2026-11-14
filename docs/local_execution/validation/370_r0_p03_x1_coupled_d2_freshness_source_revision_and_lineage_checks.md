# Validation 370: X1 coupled D2 freshness, lineage, source-owner and model-index mutation checks

**Date:** 2026-11-14
**Status:** ACTUAL_D2_F09_F10_SEMANTIC_CONTRAST_EXECUTED / SOURCE_AND_MODEL_MUTATION_NEGATIVES_VERIFIED / FOCUSED_REGRESSION_152_PASS / FULL_X1_INCONCLUSIVE / FORMAL_P03_UNSCORED
**Research:** 671 and prospective method proposal Research 672. **Checkpoint:** 934. **Collaboration:** MC-0030 Message 086.
**Authority:** Development-replay and simulated source-authoring evidence only. The program does not modify production authority or accept a new R0-P03 protocol.

## 1. Base state and original source identity

Initial Git branch: v1-source-vault-bootstrap-resume, HEAD 372561d604cd8fb8b01e6078534e311de83b55f4, clean.

Unmodified original development-replay inputs:

- experiments/ao10_hybrid_d2_lineage_v01/reviewer_fixtures.json: 23,030 bytes; SHA-256 46b2ef98fde976f3659884e0de91e120d580ddfeeacdab9c983a5f55bd7cf464.
- experiments/ao10_hybrid_d2_lineage_v01/evaluator_chatgpt_a.py: 12,117 bytes; SHA-256 26b63dcc0968b73927145bdd495865091a5ef1847feb28213549d7eb6c914e6f.

F09_REPLACE_VALID_REALIZATION_CARRY and F10_REPLACE_STALE_CARRY_FACTS were verified to differ only by the source_realization_facts_fresh input boolean. The actual D2 evaluator reported S1 current in both; F09 CARRY_FACTS_FOR_REVALIDATION without additional reviewer error, F10 OPEN_RESET and CARRY_STALE_FACTS with review_required true. Neither case was promoted into historical real ADS production authority.

## 2. Executable witness identifiers

- experiments/r0_p03_navigation_probe/x1_coupled_mutation_contract_v02.py: 23,926 bytes; SHA-256 beafafc2ec809845fa81b9ae28893b838aaa2f8aa8dee32c8777236f7beed653.
- experiments/r0_p03_navigation_probe/x1_coupled_mutation_contract_result_v02.json: 5,344 bytes; SHA-256 2f12617a93368817748f3f8bbbffa06bb8b61ddca1f9d7dcece7f33fc7f55ffe.
- tests/unit/test_r0_p03_x1_coupled_mutation_contract_v02.py: 8,322 bytes; SHA-256 81063652e1d140a86076d70b6d5f8c2af26a8f689ca5f56ce1ba210fad072ee3.

The first-run JSON result is non-overwritable by the program: a later execution must exactly reproduce it, otherwise it refuses to replace its contents. All actual diagnostics use fixed original D2 inputs and clearly synthetic navigation metadata.

Result status: COUPLED_D2_MUTATION_EVIDENCE_X1_FULL_INCONCLUSIVE.

## 3. Executed engineering checks

The direct Python module execution returned exit code zero, reported five B0-B4 derived navigation views, valid-carry mode CARRY_FACTS_FOR_REVALIDATION, stale-carry mode OPEN_RESET, and nine detected invalid operations.

Verified:
- Per-arm actual D2 semantic and successor-realization changes visible in derived projections.
- Stale F09 publication rejected if used against the F10 semantic state.
- B2 effect P1 link becomes REVIEW_REQUIRED after successor S1 becomes current.
- Source path relocation keeps stable identity and body digest.
- Changed source bytes require explicitly renewed source-owned experimental declaration.
- Different B4 model ID or source digest invalidates the derived-index manifest, with exact rebuild restoring availability.
- Non-governing metadata cannot add an accepted J1 field or unrecognized vocabulary/concern and cannot forge a different carrier owner without detection.
- Derived currentness tampering and stale source-derived publication are refused.
- An unknown historical effect reference is conservatively REVIEW_REQUIRED but not positively distinguished from a retired known effect: this is an exposed missing contract, not a passing identity resolver.

The 20 newly added parametrized regression cases passed.

Broader focused test command:

    .venv/Scripts/python.exe -m pytest -q -p no:cacheprovider
        tests/unit/test_r0_p03_x1_coupled_mutation_contract_v02.py
        tests/unit/test_r0_p03_x1_navigation_extension_boundary_v01.py
        tests/unit/test_r0_p03_historical_semantic_evidence_chain_v01.py
        tests/unit/test_project_knowledge_authority.py

Result: 152 passed in 3.58s, exit 0.

## 4. Evidence and inference boundary

The real evaluated source is an existing developmental lineage fixture, not a production V02 kernel. Source-owner declarations, claimed owner names, four carriers, B4 vectors, metadata updates and proposed governance checks were deliberately generated for the experiment; source-owner identity is NOT cryptographically or operationally qualified. The B4 model version check does not demonstrate vector recomputation from changed source bytes or semantic quality. Existing Route-B rankers are exercised as interfaces rather than Research 513 formal arms. A user-facing connector-readable freshness SLA and real natural-owner J2 RELATIONAL declaration admission remain absent.

The test's success cannot be interpreted as actual whole-system kernel isolation or X1 PASS. Research 671 records the precise missing physical contracts and a finite stop; Research 672 proposes the next owner-governed methodological choice. No new formal tasks, hidden gold, independent scorer, accepted effect or migration was created.

## 5. Repository postflight

Run structural checks after writing the latest routing, Knowledge Map and checkpoint, before guarded exact-path commit:

    scripts/check_current_routing.py
    scripts/check_knowledge_map.py
    scripts/check_checkpoint_metadata.py
    scripts/check_model_collaboration_state.py
    scripts/check_repository_integrity.py
    git diff --check

Final observed postflight after Checkpoint 934 and all Research 671-672, collaboration and routing files were written:

- scripts/check_current_routing.py: PASS, checkpoint 934, active branch v1-source-vault-bootstrap-resume, latest experiment outcome INCOMPLETE, current boundary p-three-prospective-method-owner-decision.
- scripts/check_knowledge_map.py: PASS, 19 topics, 24 foundations, 28 specifications, 672 research records and 935 numbered checkpoint files.
- scripts/check_checkpoint_metadata.py: 935/935 numbered checkpoints compliant, zero errors, one historical intermediate compliant.
- scripts/check_model_collaboration_state.py: PASS, 28 model-collaboration state files.
- scripts/check_repository_integrity.py: PUBLIC_REPOSITORY_INTEGRITY=PASS; family-aware, Project Knowledge, checkpoint, map, collaboration and routing guards all pass.
- git diff --check: exit 0, only advisory future Windows working-copy LF/CRLF conversion warnings, no whitespace errors.
- Re-executed combined focused pytest suite after source/document updates: 152 PASS in 3.75 seconds, exit 0.

The first integrity attempt identified missing required Scope metadata in both newly authored Research records. Those source-metadata errors were corrected before the final PASS without relaxing the check. These are repository and experimental reproduction checks, not independent semantic admission, Research 513 formal scoring or physical target qualification.

    D2_ORIGINAL_FIXTURES=UNMODIFIED
    D2_F09_F10_FRESHNESS_CONTRAST=EXECUTED
    NEW_REGRESSION_CASES=20_PASS
    FOCUSED_SUITE=152_PASS
    NEGATIVE_OPERATIONS=9_REJECTED
    ORIGINAL_R0_P03_FORMAL=INCOMPLETE
    FULL_X1=INCONCLUSIVE
    NEXT=OWNER_EXACT_PROSPECTIVE_METHOD_DECISION
