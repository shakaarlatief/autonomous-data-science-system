# Validation 250: R0-P03 source-only legacy capsule and preservation

**Date:** 2026-10-13
**Status:** FOCUSED_SOURCE_CAPSULE_TESTS_PASS / PRESERVATION_PASS / PUBLIC_REPOSITORY_INTEGRITY_PASS
**Scope:** Verify immutable source bytes, deterministic capsule output, exclusion of historical answer fixtures, demonstrated path/readback repairs, exact changed-file scope and repository continuity integrity; do not claim independent reference or scored experiment qualification.
**Parent:** Research 562 / Checkpoint 898 / Research 513, 559-561 / Checkpoint 897.
**Execution:** Owner-relayed Codex desktop / codex-01; local authorized worktree, no commit or push.
**Starting branch / HEAD:** `v1-source-vault-bootstrap-resume` / `159de980266e183cf24ee08d0ab2e9f7d4f1e1ba`.

## Actual focused test commands and results

Commands ran from the public repository root using `.venv/Scripts/python.exe` as the project Python interpreter. Explicit fresh `--basetemp` paths keep all capsule materializations in ignored `.venv`; the exporter intentionally rejects ordinary external pytest temporary locations.

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_only_capsule.py tests/unit/test_r0_p03_independent_reference_intake.py tests/unit/test_r0_p03_role_frame_candidate.py tests/unit/test_r0_p03_source_census.py --basetemp=.venv/.r0-p03-capsule-898-initial
36 passed in 38.03s

.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_only_capsule.py --basetemp=.venv/.r0-p03-capsule-898-defect-repro
8 failed, 9 passed in 49.36s

.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_only_capsule.py tests/unit/test_r0_p03_independent_reference_intake.py tests/unit/test_r0_p03_role_frame_candidate.py tests/unit/test_r0_p03_source_census.py --basetemp=.venv/.r0-p03-capsule-898-postflight
46 passed in 28.09s
```

The intermediate red run exercised new regressions against the original implementation. Six invalid-path cases and one injected corrupted-write case demonstrated implementation defects. The eighth failure was a newly written recomputation test sorting Windows `Path` objects case-insensitively; that test was corrected to explicit case-sensitive POSIX Git-path order, matching the documented commitment algorithm. It did not demonstrate a corpus/digest defect. The final suite passes all **17 capsule cases plus 29 unchanged earlier P03 cases**.

The implementation corrections are limited to validating raw source-path segments before `Path` normalization and reading each closed saved source for exact equality before receipt issuance. No source selection, theme wording, historical source revision, scoring rule or other candidate implementation was changed.

## Source-content evidence and preservation assertions

The tests compare all 65 saved source files against their exact historical `git show` bytes, recompute the source-content commitment from saved bytes, verify **1,725,920 bytes** and digest `baf2b893435c1951b52814a3de897f7684890b1449bb437b46948cc868d304d3`, and compare every file in two independent exports byte-for-byte. Intake has nine neutral case aliases; old relevance/membership/required/rejected fields, original W5 answer-fixture paths and `.git` are absent. Existing destinations and destinations outside `.venv` are refused; deliberately corrupted output fails before an integrity receipt is written.

The content commitment hashes UTF-8 `path + NUL + SHA256(file bytes) + LF` entries in case-sensitive Git-path order. It establishes reproducible source content, not actual reviewer isolation, hidden gold, reviewer exposure, fresh evaluator access or a score. Original source-selection/topic-origin bias remains disclosed.

The final independent immutable-Git recomputation and scope checks confirm exactly ten changed/new review files: the two existing capsule files, Research 562, Validation 250, Checkpoint 898, current routing, Current State, Knowledge Map and the two MC-0030 coordination surfaces. All other tracked paths, prior checkpoints, Research 217/W5 fixtures/results, Research 513, prior P03 executable candidates/tests, schemas and contracts match starting HEAD. No private repository operation or modification is part of this unit.

## Repository postflight

`.venv/Scripts/python.exe -B .venv/.r0-p03-capsule-898-preservation-check.py`: **PASS**. This one-off ignored scratch check independently reads the original immutable annotation object and all 65 historical Git source objects, compares every saved source, recomputes the exact byte total/content digest without importing the capsule/intake generator, and verifies receipt agreement. It checks the 36 decision-heading counts at both the immutable intake ref and current source, exact five modified tracked continuity paths plus five new review files, ignored scratch location, unchanged branch/HEAD, empty index, appended exposure chronology, preserved historical thread body, task ownership/next actor and whitespace. The original helper's hard-coded summary count was corrected to count executed assertions; the individual assertions passed throughout.

`.venv/Scripts/python.exe -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, exit 0. All six components pass: family-aware repository contracts, Project Knowledge, checkpoint metadata, Knowledge Map, model collaboration and current routing. This is the actual local aggregate, not an inferred result or a broader executable integration-test claim.

`git diff --check`: **PASS**, exit 0. Git reports only LF-to-CRLF working-copy normalization warnings on the five modified tracked text files. The final postflight repeats the aggregate and scope/whitespace check after completing this validation record; no executable code changed after the 46-test pass.

Generated capsules, test artifacts and the one-off verification helper stay only in ignored `.venv`; no generated capsule is added to the review diff. The starting HEAD remains unchanged and no file is staged. Current routing advances locally to Checkpoint 898 / `p-three-reviewer-execution-authority-qualification`; MC-0030 remains OPEN with task owner and next actor ChatGPT, no active target writer, and appended Codex engineering exposure. Its stale note about Message 062 pending is corrected to the already reconciled status without altering historical messages or exposure entries.

Publication and independent ChatGPT acceptance remain pending by explicit completion boundary. Independent reviewer execution, restricted complete-gold custody, primary-task selection/authorship and exact experimental freeze remain unresolved regardless of local test or repository-integrity outcomes.
