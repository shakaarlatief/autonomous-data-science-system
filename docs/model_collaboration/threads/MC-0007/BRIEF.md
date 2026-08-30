# MC-0007 Brief: Source Universe Pre-Deployment Recovery Hardening and Windows Verification

**Date:** 2026-08-30  
**Status:** ACTIVE IMPLEMENTATION / VERIFICATION REQUEST  
**Mode:** COORDINATED_HANDOFF  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Implementation base:** `65bf6198ea77565551e4c4dabe690ce204497d79`  
**Task owner:** ChatGPT / `chatgpt-10`  
**Implementer / verifier:** Claude Code / `claude-code-01`

## Purpose

Implement and execute-verify the four narrow recovery-hardening findings accepted from MC-0006 before the first permanent private Source Registry / Source Vault write.

This is not a redesign of the Source Universe and not an authorization to perform permanent deployment.

Read first:

```text
docs/model_collaboration/threads/MC-0006/messages/001_claude_source_universe_architecture_review.md
docs/model_collaboration/threads/MC-0006/messages/002_chatgpt_task_owner_disposition.md
docs/model_collaboration/threads/MC-0006/THREAD.md
docs/specifications/023_v1_source_universe_substrate.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
```

## Accepted implementation findings

### F1. Existing-object verification failure must not leak the incoming staging file

Current failure mode:

```text
final object exists
-> verify final object
-> verification raises
-> incoming staging file is never deleted
```

Required contract:

```text
incoming staging file is cleaned on both success and failure of the existing-object verification branch
pre-existing corrupt final object is not silently deleted or repaired
integrity failure remains visible to the caller
```

### F2. A newly placed object that fails explicit final integrity verification must not remain at the permanent path

Current failure mode:

```text
os.replace(staging, final) succeeds
-> explicit digest/size verification raises SourceArtifactIntegrityError
-> generic cleanup only tries the now-absent staging path
-> known-bad final object remains and blocks future legitimate retry
```

Required contract:

```text
only when this invocation has just placed the final object and explicit integrity verification proves it bad:
    remove that known-bad final object
    re-raise the integrity failure

do not delete a pre-existing corrupt object in the duplicate branch
do not delete a final object merely because an unrelated fsync/OS operation fails
```

### F3. Batch `ingest` must preserve structured partial progress

Current failure mode:

```text
bare list comprehension
-> one reachable LogicalSourceConflict aborts the command
-> traceback is the only operator-visible record
-> successes before the failure are not emitted as structured output
```

Required contract:

```text
process the reviewed requests deterministically
record a structured success or failure entry per attempted request
preserve stable_key in every entry
preserve sha256/result for successful entries
record error type/detail for failed entries
return non-zero if any request fails
one item failure must not erase structured evidence for earlier successes
```

Do not weaken `LogicalSourceConflict`; it remains a required conservative review boundary.

### F4. Failed backup creation must leave a straightforward retry path

Current failure mode:

```text
backup writes directly into final target
-> mid-copy or verification failure leaves partial target non-empty
-> next create_backup(target) is rejected by the non-empty-target guard
```

Required contract:

```text
failure must never be reported as complete
partial backup state must not block a straightforward retry to the same intended target
existing no-overwrite behavior for a genuinely non-empty target remains
an intentionally pre-existing empty target must remain a supported input unless there is a strong demonstrated reason to change the contract
```

Acceptable implementation patterns include:

```text
temporary sibling + publish only after full verification
or
explicit cleanup of partial output on failure, restoring an originally empty target when needed
```

Choose the smallest robust implementation for Windows and POSIX rather than adding a general backup framework.

## Cheap accepted documentation hardening

In the Windows branch of directory fsync handling, add a concise code comment explaining that the no-op is intentional because Python exposes no portable Windows equivalent to POSIX directory fsync for durable rename metadata.

Do not invent a Windows fsync workaround.

## Regression requirements

Add direct regression coverage for all four accepted findings.

At minimum prove:

```text
F1
    existing corrupt object -> commit raises -> incoming staging file gone -> corrupt existing object remains for explicit investigation

F2
    new-object post-replace integrity failure -> commit raises -> newly placed final object removed

F3
    one successful request plus one reachable ingest failure -> JSON includes both records -> command returns non-zero

F4
    simulated mid-backup failure in a disposable location -> incomplete output no longer blocks immediate retry -> subsequent verified backup succeeds
```

Keep tests provider-free and deterministic.

## Local Windows execution evidence

After implementation, run on the real operator Windows checkout:

```text
uv run --python 3.13 --locked alembic upgrade head
uv run --python 3.13 --locked python -m pytest -q
```

Run the new source-specific regressions separately first if useful for diagnosis, but the final evidence should include the full inherited provider-free pytest suite.

Also exercise the F4 failure/retry path in a disposable test location. This may be the deterministic injected-failure regression if it genuinely executes the filesystem cleanup/retry path; do not attempt a real disk-full condition on the operator machine.

## Explicit exclusions

Do not:

```text
write or migrate the permanent Source Registry
write the permanent Source Vault
modify the original educational source corpus
perform the real permanent backup
perform the real clean restore
admit Course 2
redesign source identity or provenance architecture
change the backup interchange format
modify unrelated Cockpit/frontend work
```

Real storage-capacity/separation checks and real-corpus restore-performance sanity remain later private bootstrap preflight steps after disk cleanup.

## Allowed repository mutation

Only the write paths declared in `MC-0007/STATE.json` are in scope.

Commit the implementation and tests to `v1-source-vault-bootstrap-resume`, then write one execution report at:

```text
docs/model_collaboration/threads/MC-0007/messages/001_claude_code_source_hardening_verification.md
```

The report must include:

```text
exact implementation commit(s)
exact files changed
exact commands run
source-specific regression result
full pytest result
Windows environment confirmation
F1-F4 disposition after execution
git status at completion
any remaining blocker before permanent bootstrap
```

If implementation requires a broader architectural change than the contracts above, stop and report that instead of expanding scope silently.
