# Validation 118: Preview.21 Semantic Release Prepare/Verify Qualified

**Date:** 2026-09-07
**Status:** PASS / PREPARED STATE QUALIFIED / EXPECTED TWO-FILE PREPUBLICATION MISMATCH OBSERVED
**Research:** Research 122
**Release ID:** `preview21-semantic-release-e2e`
**Source head:** `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`
**Scope:** Qualify live `prepare` and pre-publication `verify` semantics before permitting the first semantic publication mutation.

## 1. Host calls

Exactly two `codex.runtime_release` calls were made in the refreshed disposable ChatGPT conversation. No other ADS tool was invoked.

### Prepare

```json
{
  "schemaVersion": "codexless.runtime-release.v1",
  "releaseId": "preview21-semantic-release-e2e",
  "requestId": "r122.preview21.prepare.20260907.01",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "prepare",
  "status": "prepared",
  "targetVersion": "0.1.1-preview.21-semantic-release-e2e",
  "targetSurfaceVersion": "codexless-public-preview-v2",
  "targetToolCount": 63,
  "fileCount": 2,
  "manifestSha256": "bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60",
  "surfaceVersion": "codexless-public-preview-v2"
}
```

### Verify before publication

```json
{
  "schemaVersion": "codexless.runtime-release.v1",
  "releaseId": "preview21-semantic-release-e2e",
  "requestId": "r122.preview21.verify.prepublish.20260907.01",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "verify",
  "status": "verification_failed",
  "targetVersion": "0.1.1-preview.21-semantic-release-e2e",
  "targetSurfaceVersion": "codexless-public-preview-v2",
  "targetToolCount": 63,
  "fileCount": 2,
  "manifestSha256": "bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60",
  "mismatchCount": 2,
  "surfaceVersion": "codexless-public-preview-v2",
  "is_error": true
}
```

## 2. Interpretation

The result matches the frozen expectation from Validation 117 exactly:

```text
prepare                  prepared
verify before publish    verification_failed
mismatchCount            2
```

The two mismatches correspond to the two release targets. The result proves verification is reading the still-installed preview.20 baseline rather than simply trusting prepared metadata. `is_error=true` is therefore expected API/tool-result signaling for a non-matching verification state, not evidence that release preparation failed.

## 3. Authority/receipt check

Neither result exposed unexpected host authority. No path/install root, PID, executable, command/argv, cwd, environment, credential, tunnel identity, permission profile, sandbox, URL, destination or arbitrary filesystem/process parameter appeared.

## 4. Independent unchanged-live verification

After the disposable-chat calls, read-only local inspection reported:

```text
version                    0.1.1-preview.20-runtime-release
toolCount                  63
PID                        41548
instanceId                 ri_c8620c8dc49e8af26a2d0d7480c3cae1
surface-contracts SHA-256  9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b
registration SHA-256       b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
tunnel health              live
tunnel readiness           ready
private head/upstream      7aa303f4f362f7d4a3ae9b4d492679751c5e892b
private tracked status     clean
```

Both live hashes remain the manifest expected-current hashes from Validation 117. No source publication or process replacement occurred during prepare/verify.

## 5. Next mutation discipline

The first semantic publish is now permitted as the next isolated mutation. Use the same release/source binding and one new stable publish requestId. Do not combine publish and restart in the same qualification turn. If publish returns `armed`, stop. Independently verify installed target hashes, process/version continuity, tunnel health/readiness and durable publish status before activation.

This split preserves the architecture:

```text
prepare
  -> server-owned immutable prepared state
verify prepublish
  -> expected mismatch against current install
publish
  -> source-only installed-byte mutation with regression/snapshot gates
independent verification
  -> prove source changed while old process still runs
runtime_maintenance restart
  -> activate prepared target contract
post-activation verify/status
```

```text
PREVIEW21_SEMANTIC_RELEASE_PREPARE_VERIFY=PASS
LIVE_INSTALL_MUTATION=false
NEXT=SEMANTIC_PUBLISH_ONLY
```
