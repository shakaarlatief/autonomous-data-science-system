# Validation 249: R0-P03 scrubbed historical intake and independent method candidate

**Date:** 2026-10-13
**Status:** NONSCORING SOURCE_INTAKE_MECHANICS_QUALIFIED / INDEPENDENT_GOLD_NOT_AUTHORED
**Scope:** Verify immutable historical 65-source and nine-theme input, B1 annotation/gold scrubbing, evidence that history remains unmodified, no new task or answer output, and original protocol gate preservation.
**Parent:** Research 561 / Checkpoint 897 / owner-approved Option A Research 559 / Checkpoint 896 / Claude MC-0030 Message 062.

The non-scored `independent_reference_intake_candidate.py` reads W5 V02 fixture bytes from Checkpoint 896 Git revision `54b603c5fe550af963aac808b1fe7cacb516c6d4` and verifies the exact original historical source ref `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`. Its output exposes **65 historical path@blob source carriers** and **nine neutral numbered aliases with subject-derived theme words**. It does *not* expose original B1 source memberships, required-source sets, distractors, preferred subject routes, a new natural-language task, an answer key or a scoring result.

The method JSON and reviewer brief expressly prohibit exposed ChatGPT/chatgpt-38 and Claude/claude-04 as fresh reference writers/evaluators; they preserve the separate twelve new tasks, original four categories, historic nine scenarios, >=10/12 and >=8/9 hard gates, 60/20 intent and zero false-authority requirement. Reviewer status and actual private durable gold version remain **NOT ASSIGNED / NOT QUALIFIED**. The historical 65-carrier set remains B1-originated, hence residual source-selection bias persists despite prospective neutral gold.

## Execute and report

Check both candidate and prior P03 unit test modules, no original Research 217/W5/Research 513 candidate mutation, correct Checkpoint 897 routing, independent reviewer still absent, no scored output/cohort, Knowledge Map and repository integrity, Git diff, exact changed-file scope and publication postflight. Record actual executed outcomes separately; never claim independently adjudicated answer gold from these structural tests.


## Actual executed prepublication checks

- `python -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_independent_reference_intake.py tests/unit/test_r0_p03_role_frame_candidate.py tests/unit/test_r0_p03_source_census.py --basetemp=.venv/.r0-p03-ref-method-897-postflight`: **29/29 PASS**, comprising 10 new scrubbed-intake tests plus 19 unchanged prior candidate tests.
- **19/19** exact changed-scope and scientific-history preservation assertions PASS: exactly 13 permitted changed/new paths, immutable Checkpoint 896 ref, exact historical W5 ref, 65 source blobs, nine anonymized theme case aliases, no original B1 relevance memberships/answers or old gold-file paths in reviewer manifest, original Research 513/Research 217 unchanged, no old P03 code/specimen modification, unselected primary author, unavailable restricted gold storage, no scores/heldout, correct Checkpoint 897 routing and no independent reviewer claim.
- `python -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS** across all six repository integrity components (family-aware, Project Knowledge, checkpoint metadata, Knowledge Map, collaboration, routing).
- `git diff --check`: **PASS** with only Windows LF/CRLF-normalization warnings.
- The independent reference intake remains a source-bound **task-owner-derived input**, not a reviewer-authored or scored gold result. An access-restricted complete gold packet and qualified independent annotator remain uncreated.

Commit/push and remote branch verification will be checked separately and must never be inferred from these prepublication tests.
