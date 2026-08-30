# MC-0007 Message 001: Claude Code Source Hardening Verification

**Thread:** MC-0007
**Message:** 001
**Author / collaborator:** Claude Code
**Role:** IMPLEMENTER / VERIFIER
**Interaction environment:** Claude Code
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `claude-code-01`
**Conversation title:** `01 - Source Universe Pre-Deployment Recovery Hardening`
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Implementation base (frozen handoff):** `65bf6198ea77565551e4c4dabe690ce204497d79`
**Exact implementation commit:** `a992fef2eda95109dacd06ee491f4604e6d11891`

Base ancestry was confirmed before implementation: `65bf619` is an ancestor of the pre-implementation `HEAD` (`eafd9e48c9a0089f5e65d2bfb0b8a05fab585ce9`), and `git diff --stat 65bf619 eafd9e4` showed only `docs/model_collaboration/**` routing changes — no code drift from the frozen base.

## Exact files changed

```text
src/ads_system/application/source_universe.py       | 92 +++++++++++--------
src/ads_system/infrastructure/source_store.py        | 24 ++++-
src/ads_system/source_cli.py                         | 39 +++++----
tests/integration/test_source_universe_cli.py        | 123 (new file)
tests/integration/test_source_universe_recovery.py   | 183 (new file)
5 files changed, 406 insertions(+), 55 deletions(-)
```

All five paths are declared write paths in `MC-0007/STATE.json`. The other three declared test paths (`test_source_universe_substrate.py`, and the CLI/recovery files just named) were either left unmodified (`test_source_universe_substrate.py` — its existing 6 tests still pass unchanged) or created new, as scoped.

## F1-F4 disposition after execution

**F1 — FIXED / VERIFIED.** `LocalSourceArtifactStore.commit()`'s existing-object branch now wraps `_verify_path` in `try/finally`, unlinking `staged.staging_path` on both success and failure. The pre-existing final object is never touched by this branch. Regression: `test_f1_existing_corrupt_object_cleans_staging_and_preserves_corruption` — asserts the staging file and staging directory are empty after the raised `SourceArtifactIntegrityError`, and that the corrupt final object is unchanged.

**F2 — FIXED / VERIFIED.** `commit()`'s new-object branch now tracks whether `os.replace` has actually placed the final object (`replaced` flag) and, only on a `SourceArtifactIntegrityError` raised after that replace, unlinks the known-bad final object before re-raising. A generic `except BaseException` (e.g. an unrelated fsync/OS failure) still only attempts the now-absent staging path and does **not** touch the final object. Regressions: `test_f2_new_object_post_replace_integrity_failure_removes_bad_final_object` (bad object removed, legitimate retry with correct bytes then succeeds) and `test_f2_unrelated_fsync_failure_does_not_remove_final_object` (simulated `_fsync_directory` `OSError` leaves the successfully-placed final object intact).

**F3 — FIXED / VERIFIED.** `source_cli.py`'s `ingest` command now loops per request, records a structured entry (`stable_key` always present; `sha256`/`result` on success; `error_type`/`error_detail` on failure), continues deterministically across the batch, and returns `1` if any request failed. `LogicalSourceConflict` itself is unmodified — it is caught only at the CLI boundary, not weakened in `ingest_file()`. Regressions: `test_ingest_preserves_partial_progress_on_reachable_conflict` (one `NEW_ARTIFACT` success plus one reachable `LogicalSourceConflict` failure both appear in the JSON output; exit code `1`) and `test_ingest_returns_zero_and_all_ok_when_every_request_succeeds` (exit code `0`, both records `OK`).

**F4 — FIXED / VERIFIED.** `SourceUniverseService.create_backup()` now builds the backup in a temporary sibling directory (`.{name}.partial-{uuid4}`) next to the target and publishes it via `os.replace` only after `verify_backup` succeeds on the staging copy. Any failure removes the staging sibling; if the target directory pre-existed empty, it is restored empty rather than left deleted. The original non-empty-target guard is unchanged. Regressions: `test_f4_mid_backup_failure_leaves_retryable_target_and_subsequent_backup_succeeds` (injected `OSError` on the second object copy — this is the deterministic failure/retry regression that genuinely exercises the filesystem cleanup path; confirms the target is left empty/absent and a retry with the real copy path then succeeds and verifies), `test_f4_pre_existing_empty_target_is_restored_after_failure_and_then_succeeds` (pre-existing empty target case), and `test_f4_genuinely_non_empty_target_is_still_rejected` (existing no-overwrite behavior is unchanged).

**Windows fsync documentation hardening — DONE.** `_fsync_directory`'s Windows no-op branch now carries a one-line comment explaining that Python exposes no portable Windows equivalent to POSIX directory fsync for durable rename metadata. No Windows fsync workaround was invented.

## Exact commands run

All commands were run from the repository root on the real local Windows checkout, from a fresh shell, against commit `a992fef2eda95109dacd06ee491f4604e6d11891`:

```text
uv run --python 3.13 --locked alembic upgrade head
uv run --python 3.13 --locked python -m pytest -q tests/integration/test_source_universe_recovery.py tests/integration/test_source_universe_cli.py tests/integration/test_source_universe_substrate.py
uv run --python 3.13 --locked python -m pytest -q
```

## Source-specific regression result

```text
uv run --python 3.13 --locked python -m pytest -q tests/integration/test_source_universe_recovery.py tests/integration/test_source_universe_cli.py tests/integration/test_source_universe_substrate.py

...............                                                          [100%]
15 passed in 2.89s
```

(9 new F1-F4 regressions across the two new files, plus the 6 pre-existing `test_source_universe_substrate.py` tests, all passing unchanged.)

## Full pytest result

```text
uv run --python 3.13 --locked python -m pytest -q

.....s...s.............................................................. [ 45%]
........................................................................ [ 90%]
................                                                         [100%]
158 passed, 2 skipped, 7 warnings in 9.10s
```

The 2 skips are the pre-existing, unrelated `ADS_TEST_POSTGRES_URL is not configured` skips in `test_knowledge_interchange_roundtrip.py` and `test_persistence_vertical_slice.py` — expected on a provider-free local run, not a regression. The 7 warnings are a single pre-existing Alembic `path_separator` deprecation notice repeated across test IDs, unrelated to this change.

`alembic upgrade head` produced no output and no error, i.e. a clean apply against a fresh SQLite database.

## Windows environment confirmation

```text
OS: Windows 11 Home 10.0.26200
Shell used for verification: PowerShell 5.1 (native, not WSL/git-bash)
Python 3.13 interpreter selected by uv: C:\Users\shaka\AppData\Local\Programs\Python\Python313\python.exe (3.13.1)
uv version used: 0.12.5 (matches pyproject.toml's [tool.uv] required-version == 0.12.5)
```

**Disclosed environment gap:** `uv` was not present on this machine's `PATH` at the start of this session (only a bare Python 3.11 interpreter was on `PATH`; Python 3.13 was available only via the `py` launcher). To run the exact commands the brief specifies, I installed `uv==0.12.5` for the Python 3.13 interpreter via `py -3.13 -m pip install --user uv==0.12.5` (first installing the latest 0.12.7, then pinning down to 0.12.5 to match the repo's declared required version) and added its user Scripts directory to `PATH` for this session only. `uv run --python 3.13 --locked ...` then created its own managed `.venv` and installed the locked dependency set from `uv.lock` (21 packages, SQLAlchemy/Alembic/pytest/psycopg-binary/etc.), matching the repository's committed lockfile rather than any ad hoc dependency resolution. This is a local Python-tooling installation only; it did not touch the Source Universe substrate, registry, or vault.

`alembic upgrade head` created a fresh `ads_system.db` SQLite file at the repository root (the default `sqlalchemy.url` in `alembic.ini`) — this is the ordinary operational-database migration target the brief's command produces on any clean checkout, not the permanent Source Registry or Source Vault. It was deleted after the verification run since it is not one of MC-0007's declared write paths and was not committed.

## Git status at completion

```text
On branch v1-source-vault-bootstrap-resume
nothing to commit, working tree clean
```

`git log --oneline -3` at completion:

```text
a992fef MC-0007: implement Source Universe F1-F4 recovery hardening
eafd9e4 Route accepted Source Universe hardening to Claude Code
65bf619 MC-0006: Claude Source Universe architecture review
```

## Explicit exclusions honored

No permanent Source Registry was created or migrated, no permanent Source Vault was written, the original educational source corpus was not touched, no real permanent backup or clean restore was performed, Course 2 was not admitted, and no Source Universe architecture/identity/provenance redesign or backup interchange format change was made. All test fixtures in the new regression files operate exclusively inside `tmp_path` (pytest's disposable temp directories); no operator private-storage location was read, written, or referenced.

## Remaining blocker before permanent bootstrap

None from MC-0007's own scope: all four accepted findings are implemented and directly regression-tested, the Windows fsync documentation hardening is in place, and the full provider-free suite is green on the real local Windows checkout with the pinned toolchain. Per `MC-0007/THREAD.md`, the first permanent Source Registry / Source Vault write remains blocked until ChatGPT inspects this diff and this evidence and closes MC-0007/MC-0006. Real free-disk-space suitability and real-corpus restore-performance sanity remain explicitly out of MC-0007's scope, deferred to the later private bootstrap preflight as already agreed in the MC-0006 disposition.
