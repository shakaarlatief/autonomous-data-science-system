# Validation 396: W1 actual distinct B0–B3 primary-arm freeze and postfreeze diagnostics

**Date:** 2026-11-16
**Status:** FOUR_EXECUTABLE_W1_PRIMARY_NAVIGATION_ARMS / ACTUAL_PRETASK_C_ARM_FREEZE / 32_PLUS_10_FOCUSED_REGRESSIONS_PASS / EIGHT_EXPOSED_DIAGNOSTICS_NOT_SCORED
**Research:** 700. **Checkpoint:** 961. **MC-0030:** Message 115.
**Scope:** Verify same full original 60-source W1 bytes, exact shared experimental S1 substrate, explicitly limited authored B1/B2/B3 metadata, separate primary implementation/freeze Git commits, prospective B4 omission and no scoring or primary gold.

Three invariant Git boundaries:
- `b987b1837f38479c3ccd34410de4ef52ab4c1edd`: original W1 B0–B3 code/metadata and adversarial arm test suite.
- `f43390ab267810502d7538e212cd30f4fee18aaf`: one-file exact SHA/Git object bound primary arm-freeze contract **before** the eight new probes.
- Postfreeze actual mechanism execution proof at exact receipt SHA-256 `97403f0859b68ce1028944271014c7b0b6e963ccd9ac5d651cd4298e9623652c`.

Frozen file SHA-256 `31e77378218e60780cdbad2dfec98293ac71f3fbeb58206066dff268ea5d845a`. Frozen 60 original sources have 822,370 UTF-8 bytes and 4,626 BM25 passages. B0 zero added metadata, B1 120 authored controlled subject memberships and 60 preferred routes against Research 217's full hierarchy, B2 23 additional nonduplicate carrier-to-governing editorial about-links, B3 five crosscutting concern labels and 115 per-source assignments. Exact source-context line witnesses **do not** certify labels independently or grant governing authority. Per-arm incremental bytes/operations and unmeasured human cost are disclosed.

Actual deterministic exposure-only outputs across eight mechanical prompts: altered six-source ordering from B0 occurred B1 5, B2 6, B3 4 times. **No numerical quality result, relevance gold, fresh task, scorer, heldout selection, legacy nine or formal M6 attempt.** B4 omission was made prospectively within the frozen record and may not be silently reversed after outcome observation.

```powershell
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.w1_primary_c_arm_v01
.venv\Scripts\python.exe -m experiments.r0_p03_navigation_probe.w1_c_arm_postfreeze_mechanism_v01
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=1 -p no:cacheprovider tests/unit/test_r0_p03_w1_primary_c_arm_v01.py
.venv\Scripts\python.exe -m pytest -q --tb=short --maxfail=1 -p no:cacheprovider tests/unit/test_r0_p03_w1_c_arm_postfreeze_execution_v01.py
```

Observed focused suites: **32 PASS + 10 PASS**. Exact output re-execution verifies frozen implementation, raw committed Git bytes and the receipt. Earlier W1 source-world regression suite, prior 24-source original-Git arms and shared-runtime tests remain separately required.

Verify exact GitHub CI on the final published commit; never describe a pending check as complete.
