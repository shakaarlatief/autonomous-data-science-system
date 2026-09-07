# Checkpoint 363: Preview.21 Post-Activation Status/Verify Qualified

**Date:** 2026-09-07
**Status:** PASS / PUBLIC POST-ACTIVATION STATUS + VERIFY QUALIFIED / SEMANTIC ROLLBACK NEXT
**Checkpoint class:** LIVE POST-ACTIVATION READBACK QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves fresh-host public readback of the completed semantic publication and the exact installed preview.21 target after activation, before permitting rollback.
**Authority:** Research 122 governs the architecture; Validation 121 owns detailed host evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

A refreshed disposable ChatGPT conversation made exactly two read-only `codex.runtime_release` calls against the already-active release binding:

```text
releaseId            preview21-semantic-release-e2e
expectedSourceHead   7aa303f4f362f7d4a3ae9b4d492679751c5e892b
```

The first call used `action=status` with the original publish requestId `r122.preview21.publish.20260907.01`. It returned the already-existing publication operation unchanged:

```text
schemaVersion      codexless.runtime-release-operation.v1
operationId        rm_cad5ff919dff666fef050e98ddda8680
action             publish_release
status             succeeded
acceptedAtMs       1788789572617
armedAtMs          1788789572625
startedAtMs        1788789573452
finishedAtMs       1788789577231
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

The second call used `action=verify` with requestId `r122.preview21.verify.postactivation.20260907.01`. It returned:

```text
status               verified
targetVersion        0.1.1-preview.21-semantic-release-e2e
targetSurfaceVersion codexless-public-preview-v2
targetToolCount      63
fileCount            2
manifestSha256       bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
mismatchCount        0
```

Neither receipt exposed filesystem path/install root, PID, executable, command/argv, cwd, environment, credential, tunnel identity, permission profile, sandbox, URL, destination or arbitrary host/process/filesystem authority. No mutation or restart was invoked in that disposable qualification turn.

Independent project-side read-only verification afterward still found:

```text
version                    0.1.1-preview.21-semantic-release-e2e
toolCount                  63
PID                        56332
instanceId                 ri_3ae38f351e0586505e9404d64dad5f24
surface-contracts SHA-256  09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a
registration SHA-256       a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
pending activation         absent
shared mutation lock       absent
active release             preview21-semantic-release-e2e
tunnel                     live / ready
```

This closes the public forward-path readback gate: host-visible status proves the original semantic publication completed durably, and host-visible verification proves the active installed bytes exactly match the prepared release target after activation.

The next mutation is the explicit semantic rollback publication. It must remain separated from rollback activation. A fresh-host `codex.runtime_release action=rollback` call should return an asynchronous `armed` receipt for the active release. After that single call, stop. The project conversation will independently verify restored preview.20 source bytes, rollback operation status, forward `pending-activation` metadata, the still-running preview.21 process and tunnel continuity before any restart.

```text
CHECKPOINT_363=PREVIEW21_POSTACTIVATION_STATUS_VERIFY_QUALIFIED
PUBLISH_STATUS=succeeded
POSTACTIVATION_VERIFY=verified/mismatchCount=0
ACTIVE_RELEASE=preview21-semantic-release-e2e
NEXT=SEMANTIC_ROLLBACK_PUBLICATION_ONLY
```
