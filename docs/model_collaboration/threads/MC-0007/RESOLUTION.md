# MC-0007 Resolution: Source Universe Pre-Deployment Recovery Hardening

**Date:** 2026-08-30  
**Status:** CLOSED / ACCEPTED  
**Thread:** MC-0007  
**Implementation base:** `65bf6198ea77565551e4c4dabe690ce204497d79`  
**Implementation commit:** `a992fef2eda95109dacd06ee491f4604e6d11891`  
**Execution report commit:** `7ee480709aa1627cc770ebb4f229a3f82b189448`  
**Provenance correction commit:** `170f6e265829ce2f15f0f528ab4ec47b261980a3`  
**Task-owner disposition:** F1-F4 accepted implementation verified; no Source Universe redesign required

## 1. Write-surface and provenance verification

The implementation commit is exactly one commit ahead of the pre-implementation coordination head and changes only the five MC-0007-authorized implementation/test paths:

```text
src/ads_system/application/source_universe.py
src/ads_system/infrastructure/source_store.py
src/ads_system/source_cli.py
tests/integration/test_source_universe_cli.py
tests/integration/test_source_universe_recovery.py
```

The subsequent Claude Code execution-report commit changes only the permitted MC-0007 execution-report message. The later Claude Code provenance-correction commit changes only the same report's interaction-provenance metadata and leaves its substantive execution evidence unchanged.

No permanent Source Registry, Source Vault, private source corpus, real backup, or real clean-restore target was written by MC-0007.

## 2. Task-owner implementation review

### F1 existing-object corruption staging cleanup

`ACCEPTED / VERIFIED`

The duplicate-object branch now places incoming staging cleanup in `finally`, so the staging file is removed whether verification of the pre-existing object passes or raises. The pre-existing final object is deliberately left untouched on integrity failure.

### F2 newly placed bad object cleanup

`ACCEPTED / VERIFIED`

The new-object branch tracks whether this invocation successfully performed `os.replace`. A `SourceArtifactIntegrityError` after that placement removes the newly placed known-bad final object and re-raises. Unrelated `OSError`/fsync failures do not trigger final-object deletion, and the duplicate branch does not automatically remove pre-existing corruption.

### F3 structured batch-ingest partial progress

`ACCEPTED / VERIFIED`

The CLI now emits one deterministic JSON record per attempted request, preserves `stable_key`, preserves `sha256`/`result` for success, preserves exception type/detail for failure, continues through the reviewed batch, and returns non-zero when any item fails. `LogicalSourceConflict` remains unchanged as a conservative application-level review boundary.

### F4 retry-safe backup creation

`ACCEPTED / VERIFIED`

Backup creation now builds into a unique temporary sibling, verifies the staged backup, and only then publishes it to the requested target via `os.replace`. Failure removes the partial sibling and preserves/restores an originally empty target, while genuinely non-empty targets remain protected by the existing no-overwrite guard.

The sibling strategy keeps staging and publication on the same filesystem and is appropriate for the local filesystem V1 backend.

### Windows directory-fsync note

`ACCEPTED`

The intentional Windows no-op now explains that Python exposes no portable equivalent to POSIX directory fsync for durable rename metadata. No speculative workaround was introduced.

## 3. Execution evidence accepted

Claude Code reports real local Windows execution at the exact implementation commit:

```text
uv run --python 3.13 --locked alembic upgrade head
uv run --python 3.13 --locked python -m pytest -q tests/integration/test_source_universe_recovery.py tests/integration/test_source_universe_cli.py tests/integration/test_source_universe_substrate.py
uv run --python 3.13 --locked python -m pytest -q
```

Reported results:

```text
source-specific selection  15 passed
full suite                 158 passed, 2 skipped, 7 warnings
OS                         Windows 11 Home 10.0.26200
Python                     3.13.1
uv                         0.12.5
```

The two skips and warnings are reported as pre-existing and unrelated to the Source Universe hardening.

The disposable F4 regression injects a mid-backup `OSError`, confirms partial output is removed, and immediately retries successfully against the same intended target.

## 4. Evidence-accounting correction

The Claude Code execution report contains one small arithmetic/documentation error that does not affect the test result or implementation disposition.

It states:

```text
9 new F1-F4 regressions + 6 pre-existing substrate tests = 15
```

Direct repository inspection shows:

```text
test_source_universe_recovery.py   6 tests
test_source_universe_cli.py        2 tests
new MC-0007 tests total            8
pre-existing substrate file        7 tests
combined                           15
```

The named tests, the 15-pass output, and the implementation remain internally consistent. This task-owner resolution records the correction without changing the execution evidence or implementation disposition.

## 5. Interaction-provenance correction

After closure, the project owner identified a second provenance-hygiene defect in the MC-0007 launch: the Claude Code session had a repository interaction-session ID, `claude-code-01`, but no explicit visible conversation title following the accepted `NN - Main Topic / Stage` convention was established before execution and push.

The durable execution report also omitted the normally expected `Interaction environment`, `Project / workspace`, and `Conversation title` fields.

The omission and its exact correct values are preserved in:

```text
docs/model_collaboration/threads/MC-0007/messages/002_chatgpt_interaction_provenance_correction.md
```

The canonical visible title assigned to the existing Claude Code session is:

```text
01 - Source Universe Pre-Deployment Recovery Hardening
```

The visible Claude Code conversation was renamed to that title.

The provenance convention was refined after this omission was discovered. The project now distinguishes between rewriting Git history and making a transparent later correction to a canonical collaborator-authored artifact. A bounded factual metadata correction may be made in a later commit when the originating collaborator can make it directly and the original artifact remains recoverable through Git history.

Claude Code completed that authorized provenance-only correction at:

```text
170f6e265829ce2f15f0f528ab4ec47b261980a3
```

Task-owner inspection of the exact diff confirmed that the commit adds only:

```text
Interaction environment: Claude Code
Project / workspace: Autonomous Data Science System
Conversation title: 01 - Source Universe Pre-Deployment Recovery Hardening
```

`Interaction session: claude-code-01` was already present. No implementation evidence, findings, commands, test results, or other substantive content changed. The originally submitted report remains permanently recoverable at commit `7ee480709aa1627cc770ebb4f229a3f82b189448`.

The provenance follow-up is therefore fully reconciled and closed. No Source Universe implementation result depends on this metadata-only correction.

## 6. Closure

MC-0007 is complete, including its interaction-provenance follow-up. No implementation defect from F1-F4 remains open and no collaborator obligation remains.

This closure does not authorize Course 2 and does not itself perform the permanent bootstrap. It removes the model-review/implementation blocker. The next boundary is the human-controlled private storage preflight: enough free capacity, the five private locations, and genuine backup separation before the first permanent Source Registry / Source Vault write.
