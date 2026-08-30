# MC-0007 Resolution: Source Universe Pre-Deployment Recovery Hardening

**Date:** 2026-08-30  
**Status:** CLOSED / ACCEPTED  
**Thread:** MC-0007  
**Implementation base:** `65bf6198ea77565551e4c4dabe690ce204497d79`  
**Implementation commit:** `a992fef2eda95109dacd06ee491f4604e6d11891`  
**Execution report commit:** `7ee480709aa1627cc770ebb4f229a3f82b189448`  
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

The subsequent Claude Code commit changes only the permitted MC-0007 execution-report message.

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

The named tests, the 15-pass output, and the implementation remain internally consistent. The collaborator-authored report is intentionally preserved unchanged; this resolution records the correction rather than rewriting provenance.

## 5. Interaction-provenance correction

After closure, the project owner identified a second provenance-hygiene defect in the MC-0007 launch: the Claude Code session had a repository interaction-session ID, `claude-code-01`, but no explicit visible conversation title following the accepted `NN - Main Topic / Stage` convention was established before execution and push.

The durable execution report also omitted the normally expected `Interaction environment`, `Project / workspace`, and `Conversation title` fields.

The original collaborator-authored report remains unchanged. The additive correction is preserved in:

```text
docs/model_collaboration/threads/MC-0007/messages/002_chatgpt_interaction_provenance_correction.md
```

The canonical visible title assigned to the existing Claude Code session is:

```text
01 - Source Universe Pre-Deployment Recovery Hardening
```

This does not change any implementation or verification result. It corrects interaction provenance and tightens the future session-launch naming rule in `docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md`.

## 6. Closure

MC-0007 is complete. No implementation defect from F1-F4 remains open.

This closure does not authorize Course 2 and does not itself perform the permanent bootstrap. It removes the model-review/implementation blocker. The next boundary is the human-controlled private storage preflight: enough free capacity, the five private locations, and genuine backup separation before the first permanent Source Registry / Source Vault write.
