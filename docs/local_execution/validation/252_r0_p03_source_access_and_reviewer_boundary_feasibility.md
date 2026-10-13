# Validation 252: R0-P03 source access and reviewer-boundary feasibility

**Date:** 2026-10-13
**Status:** SOURCE_API_TESTS_PASS / REVIEWER_EXECUTION_NOT_QUALIFIED / PUBLIC_REPOSITORY_INTEGRITY_PASS
**Scope:** Verify the fixed historical source API and record actual execution-boundary probes, preservation and repository checks without model inference, independent adjudication, task selection or gold creation.
**Parent:** Research 563 / published Checkpoint 898 / Validation 250 / Research 513, 559-562.
**Starting branch / HEAD:** `v1-source-vault-bootstrap-resume` / `35eb45064006c8fbfd2acce59d10ce32948146bf`; initially clean worktree and index.
**Executor:** Existing exposed Codex/codex-01, with task-owner review/publication reserved to ChatGPT.

## Executed tests

From the public repository root, using the project interpreter and distinct ignored scratch directories:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_only_capsule.py tests/unit/test_r0_p03_independent_reference_intake.py tests/unit/test_r0_p03_role_frame_candidate.py tests/unit/test_r0_p03_source_census.py --basetemp=.venv/.r0-p03-reviewer-boundary-feasibility-baseline
46 passed in 28.94s

.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_only_access.py --basetemp=.venv/.r0-p03-access-candidate-initial
42 passed in 20.65s

.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/unit/test_r0_p03_source_only_access.py tests/unit/test_r0_p03_source_only_capsule.py tests/unit/test_r0_p03_independent_reference_intake.py tests/unit/test_r0_p03_role_frame_candidate.py tests/unit/test_r0_p03_source_census.py --basetemp=.venv/.r0-p03-access-candidate-final
90 passed in 49.55s
```

The final result comprises **44 source-access cases and 46 unchanged prior P03 cases**. Coverage includes exact reconstruction of all 65 immutable Git source blobs via paged API reads; 1,725,920 bytes and the original content commitment; source identities on list/read/search; uniform denials for traversal, malformed/absolute/Windows paths, metadata, old W5 answer fixtures and P03 design; extra-operation/parameter denials; integer/query/result/text budgets; literal deterministic search; altered, missing and extra sources; changed trusted manifest; a real Windows junction; and immutable behavior after disk changes. All tests are API mechanics, not OS, network or model-context isolation tests. Existing capsule/intake/census/specimen files and tests were not modified.

## Actual environment probes

- `codex.project_context` at the public root: model-free ephemeral bootstrap succeeded, reporting CLI 0.162.0-alpha.17.2, public workspace, `workspaceWrite`, command network disabled, and unavailable implicit skill routing (`IMPLICIT_SKILLS_STRUCTURE_MISMATCH`). No inference turn ran. A capsule-scratch cwd call returned EPERM; no repair or authority widening followed.
- `codex.command_exec(access="readOnly")`: a PowerShell loop used `File.ReadAllBytes` on relative W5 annotations, Research 562 and `.git/HEAD`, returning JSON path/readable/byte-count fields only. Exit 0; all three readable, at 15,486 / 11,217 / 49 bytes. Resolved profile `:read-only`, ceiling `:workspace`. This is a demonstrated failure of the required source-only exclusion, not a reviewer confinement PASS. The first version of the probe had a PowerShell pipeline syntax error; it performed no reads and was corrected before the recorded result.
- `codex --version`: PATH CLI 0.154.0; `claude --version`: Claude Code 2.1.283. `claude --help` and `claude auth status --help` inspected supported options without starting a Claude session or fetching credentials. Environment credential checks returned presence booleans only; no credential value or working provider authentication was established.
- `docker info --format '{{.OSType}} {{.ServerVersion}}'` and `docker image ls --format '{{.Repository}}:{{.Tag}}'`: configuration access denied and engine pipe unavailable. `wsl --list --quiet`: `Wsl/EnumerateDistros/Service/E_ACCESSDENIED`. No installed/running isolated environment was qualified, and no service/elevation/install was attempted.
- Direct immutable Git-object verification of the D-036 owner artifact reproduced Research 502's 1,007 bytes and SHA-256 `28ecf862a546c7aff2554877b061b661763571dae64b25ff5e63c361ceb4ab06`. Ledger inspection established mixed statuses and missing/uneven event provenance, not task-category eligibility or complete closure.

Research 563 preserves the concrete route comparison and observed qualification receipt. Fresh exposure, effective exclusive model tools, reviewer OS/network boundary and restricted reference-output custody remain unverified. No API/MCP transport was deployed, model/evaluator launched, benchmark answer authored, private store allocated or generic Runtime Bridge code changed.

## Repository postflight and preservation

`.venv/Scripts/python.exe -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, exit 0, across all six components (family-aware, Project Knowledge, checkpoint metadata, Knowledge Map, collaboration and routing). The final postflight repeats this aggregate after completing the MC-0030/validation additions. No executable change occurred after the 90-test pass.

The model-free Python/Git scope postflight returned **11/11 preservation assertions PASS**: unchanged HEAD and branch, empty index, exactly four modified continuity files and four new review files, unchanged routing content, preserved exposure history and thread chronology, unchanged task owner/next actor and phase boundary, and clean whitespace. The comparison against starting HEAD excludes every other tracked path from the changed set, preserving original W5, Research 513, previous checkpoints, contracts, generic Runtime Bridge and all existing executable code. No stronger reviewer/experimental qualification follows from a public repository-integrity pass.

`git diff --check`: **PASS**, exit 0; only LF-to-CRLF normalization warnings for the four modified tracked text files. Final aggregate/whitespace postflight is repeated after recording these outcomes. Generated test capsules remain in ignored `.venv` only.

The verified scope is eight review files: the new source-access module/test, Research 563, Validation 252, and bounded additions to Current State, Knowledge Map and MC-0030 STATE/THREAD. Checkpoint 898, current routing and all existing research/validation/checkpoints/contracts/executable files remain unchanged. No commit or push; no new checkpoint or experimental phase transition.
