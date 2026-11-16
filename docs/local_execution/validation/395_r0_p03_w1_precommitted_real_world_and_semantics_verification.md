# Validation 395: Precommitted W1 source-world freeze and direct Git/source/connector proof

**Date:** 2026-11-16
**Status:** W1_BUILD_60_PRECOMMITTED_AND_REPRODUCED / W1_COMMON_SOURCE_EVIDENCE_NONPROMOTION_PASS / FORMAL_R0_P03_UNSCORED
**Scope:** Verify original-Git 60-source W1 build and one non-governing source-reported common evidence world exactly after separate W1_RULE preregistration. No tasks, gold, heldout identities, formal arm scores or owner authority created.
**Research:** 699. **Checkpoint:** 960. **MC-0030:** Message 114.

Precommitted rule commit `b084ec8aa775426a96742ca437394f1f7b0b0b00` with parent `56df05bbfc14aa6f33c3e0b37f61bd61bcc55597` contains only `experiments/r0_p03_navigation_probe/W1_RULE.md`, before the W1 generator and results existed. The original data source is Git `17ea403ef64092f275e3c7d6492d99929804f8e5`. The script binds the rule to its predecessor Git object, original bytes, 10 mandatory anchors, max-four-hop citation distance, exact seven stratum quotas and precommitted heldout rule.

Generator executed two independent computations byte-for-byte equal **in the same command** before it created any receipts. All 60 source original Git OIDs and SHA-256 values were verified, all 60 selected paths meet the exclusion rule and are reachable within four citation hops, and exactly the precommitted 9+7+12+10+8+10+4 build quota was selected. No disconnected backfill, rule amendment or holdout identity was used.

Create-only artifact SHA-256:
- Manifest: `b3e7de396f303fad1e14fe575d712693a784ab6732ced6e5667919bafdc5842e`
- Source-reported common substrate: `457390b693bddaaa62a0f536c6c4c4afa690bb61a5ece8fd44c9c7f0681347ac`
- Exclusion log: `61bcc3f2be2e6090c836e5eedfbe5e0bd14407f2ffdac51f673887164427a033`

Observed evidence classes: 374 source-reported claims, 189 definition-only records, 60 direct Git-byte records and one separately qualified accepted experiment-only S1 envelope with four J1 effects and one J2. Additional 34 literal-documentary-mention remainders are labelled unknown, not refuted. Five independent W1CommonRuntime labels were actually instantiated, and their common list/read/search/semantic/orientation results match with SHA-256 `3ea6617bdffbddfdb7b5d234c0598bae8d4a53b49e2641a1853b0712d0d62fe0`; this is **shared W1 connector parity**, not actual formal B0-B4 individual treatment execution.

The new regression `tests/unit/test_r0_p03_w1_precommitted_world_freeze_v01.py` passed **27 tests** including adversarial authority nonpromotion, build/heldout separation, original blob and line identity, generated-index-as-source rather than governing, zero excluded selections, and rejected out-of-world reads and invalid query budgets. The first test run had one **test-only** wrong expectation that HEAD already followed the rule commit, even though source selection legitimately ran while the local rule-only commit was HEAD. The test assertion was corrected to prove the separate rule prior to the original source pin without any change to `W1_RULE.md`, generator, source selection or output hashes. Second run: **27 passed in 19.62 seconds**.

Reproduction:

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.w1_freeze_v01
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=1 -p no:cacheprovider tests/unit/test_r0_p03_w1_precommitted_world_freeze_v01.py
```

The combined repository-integrity and adjacent legacy common-runtime tests, remote push and exact GitHub CI are independently verified as part of publication. Do not count this as a formal M6 attempt.

    VALIDATION=395
    W1_BUILD=60
    HELDOUT=NOT_DRAWN
    W1_CORE_PARITY=PASS
    W1_FOCUSED_TESTS=27_PASS
    FORMAL_P03=INCOMPLETE
