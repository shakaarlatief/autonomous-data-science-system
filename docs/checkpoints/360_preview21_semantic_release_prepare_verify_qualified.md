# Checkpoint 360: Preview.21 Semantic Release Prepare/Verify Qualified

**Date:** 2026-09-07
**Status:** PASS / LIVE PREPARE + EXPECTED PRE-PUBLICATION VERIFY MISMATCH QUALIFIED / FIRST SEMANTIC PUBLISH NEXT
**Checkpoint class:** LIVE SEMANTIC RELEASE PREPARATION QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves the first live use of `codex.runtime_release` against the genuine preview.21 bundle without publishing or restarting the runtime.
**Authority:** Research 122 governs the architecture; Validation 118 owns detailed live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

A refreshed disposable ChatGPT conversation invoked exactly two ADS tool calls, both `codex.runtime_release`, against the exact qualified release binding:

```text
releaseId            preview21-semantic-release-e2e
expectedSourceHead   7aa303f4f362f7d4a3ae9b4d492679751c5e892b
```

Call 1 used `action=prepare` / `requestId=r122.preview21.prepare.20260907.01` and returned:

```text
schemaVersion        codexless.runtime-release.v1
action               prepare
status               prepared
targetVersion        0.1.1-preview.21-semantic-release-e2e
targetSurfaceVersion codexless-public-preview-v2
targetToolCount      63
fileCount            2
manifestSha256       bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
```

Call 2 used `action=verify` / `requestId=r122.preview21.verify.prepublish.20260907.01` and returned the deliberately expected pre-publication mismatch:

```text
action               verify
status               verification_failed
mismatchCount        2
fileCount            2
targetVersion        0.1.1-preview.21-semantic-release-e2e
manifestSha256       bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
is_error             true
```

The `is_error=true` transport/result flag is not interpreted as a failed qualification here. `verification_failed` with exactly two mismatches was the predicted healthy pre-publication observation because the live install still contains the two preview.20 baseline files rather than the prepared preview.21 target bytes.

Neither receipt exposed filesystem path/install root, PID, executable, command/argv, cwd, environment, credentials, tunnel identity, permission profile, sandbox, URL, destination or arbitrary host/process/filesystem authority. No `publish`, `rollback`, runtime-maintenance, command, Git, Browser, Agent, workspace or file operation was invoked in the disposable qualification turn.

Independent project-side read-only verification afterward confirmed the live install/runtime is still unchanged:

```text
version                    0.1.1-preview.20-runtime-release
toolCount                  63
PID                        41548
instanceId                 ri_c8620c8dc49e8af26a2d0d7480c3cae1
surface-contracts SHA-256  9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b
registration SHA-256       b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
tunnel                     live / ready
private HEAD/upstream      7aa303f4f362f7d4a3ae9b4d492679751c5e892b
private tracked status     clean
```

Therefore `prepare` copied and bound the release into server-owned prepared state without changing the live install, and `verify` independently observed the exact expected difference between prepared target and currently installed source.

The next mutation is now the first live semantic publication into the Codexless install tree. It must use exactly one `codex.runtime_release action=publish` call for the already prepared release binding and one new stable requestId. The publication receipt must be treated as an asynchronous durable mutation receipt. If it returns `armed`, stop that qualification turn and do not immediately invoke restart or another mutation. The project conversation should then independently inspect the live installed hashes, runtime version/process identity, tunnel state and durable release status before any activation restart.

```text
CHECKPOINT_360=PREVIEW21_SEMANTIC_RELEASE_PREPARE_VERIFY_QUALIFIED
PREPARE=prepared
PREPUBLICATION_VERIFY=verification_failed/mismatchCount=2
LIVE_INSTALL_UNCHANGED=true
NEXT=FIRST_LIVE_SEMANTIC_PUBLISH
```
