# Research 430: Codex command/exec compatibility recovery and managed runtime release

**Date:** 2026-10-01
**Status:** LOCAL RUNTIME RECOVERY COMPLETE / COMPATIBILITY RPC TIMEOUT QUALIFIED / P8 STATE PRESERVED
**Parent:** Research 429
**Scope:** Recover the Codexless Runtime Bridge after the local compatibility gate stopped starting under the current Codex Windows runtime, establish the failure mechanism experimentally, and replace the temporary break-glass recovery edit with a qualified managed runtime release.
**Authority:** Local-runtime recovery and compatibility qualification only. This record does not alter Key Author B semantic outputs, accepted classifications, accepted grouping decisions, frozen packets, semantic rules, Key A blindness, construct comparison, DRP-03 scoring, production implementation, migration, or authority switching.

## 1. Incident boundary

After the Research 429 public boundary had been committed, a managed Codexless restart left the Runtime Bridge unavailable because Codexless startup failed its model-free compatibility probe with:

    CodexRpcTimeoutError: command/exec timed out after 10000ms

The public Research 429 commit was later reconciled through the restored Runtime Bridge:

    public HEAD = 43f71d9bb098316714e8f834a3db972a8d77324d
    origin/v1-source-vault-bootstrap-resume = 43f71d9bb098316714e8f834a3db972a8d77324d
    tracked working tree = clean

The earlier uncertain push therefore completed successfully. It was not blindly retried.

## 2. Compatibility diagnosis

The current native Codex runtime selected for the bridge is:

    codex-cli 0.155.0-alpha.9.2

Direct elevated Windows sandbox execution succeeds with this runtime, including the exact model-free marker command used by the Codexless compatibility gate.

A direct Codex App Server client reproduction then isolated the timeout boundary:

    app-server initialization                 0.186 s
    command/exec successful round trip       13.593 s
    stdout                                   TOOLWIRE_CODEX_CONTRACT_OK

A second reproduction preserved the original command budget:

    command timeout                          5,000 ms
    outer RPC timeout                        45,000 ms
    successful round trip                    13.030 s
    stdout                                   TOOLWIRE_CODEX_CONTRACT_OK

Therefore the five-second command execution budget remains sufficient. The failure is the ten-second outer RPC deadline around the compatibility probe, which is shorter than the observed successful Windows elevated-sandbox/App-Server round trip.

The older native Codex 0.155.0-alpha.2.6 runtime was separately rejected as a recovery candidate because its Windows sandbox could not launch its setup helper. No downgrade, sandbox weakening, trust broadening, permission broadening, or semantic bypass was used.

## 3. Break-glass recovery

Because the control plane itself was unavailable, one reversible bootstrap edit was applied directly to the installed Codexless authority executor:

    compatibility probe command timeout      5,000 ms unchanged
    compatibility probe outer RPC timeout    10,000 -> 45,000 ms
    profile-resolution timeout               10,000 ms unchanged

This restored Codexless and the secure tunnel sufficiently to regain the governed Runtime Bridge.

The temporary edit was treated only as break-glass recovery state. A PowerShell UTF-8 write introduced a BOM, producing recovered installed-file SHA-256:

    32d984ba02399612abc995fd51987e6ae2a92b09ccd7e3f56774bc61e61e59e7

That exact recovered runtime hash was used as the managed replacement baseline rather than ignored.

## 4. Managed release qualification

The permanent correction was moved into the private local-runtime repository and qualified as an immutable managed release.

Private local-runtime source is synchronized at:

    8eaa65b87f0489c75b3b68aa864840e2082fc950

The final release is:

    release id        codex-command-exec-rpc-timeout-v2
    target version    0.1.1-preview.69-codex-command-exec-rpc-timeout-v2
    surface           codexless-public-preview-v2
    tool count        177
    manifest SHA-256  f1d0cdfc60fe9ee044859a060aeea34d31f685940382ec1ff1c633069753094f

The release replaces the authority executor with canonical source that defines a dedicated 45-second compatibility-probe RPC deadline while preserving the five-second command budget and the independent ten-second profile-resolution deadline. It adds a focused regression proving those three bounds and carries the existing inherited authority, public-surface, bounded-Git, P8/P7/P6/P5/P4, and runtime-release regression set.

An initial immutable V1 release attempt failed closed with RUNTIME_RELEASE_BASELINE_MISMATCH because its manifest expected the no-BOM equivalent of the temporary recovery file. The already-bound release ID was not mutated or replayed. A new V2 release was created with the exact recovered installed baseline.

Managed V2 lifecycle:

    prepare                 PASS
    publish                 SUCCEEDED
    restart / activation    SUCCEEDED
    post-activation verify  VERIFIED
    mismatchCount           0

No activation recovery was required.

## 5. P8 preservation check

After Runtime Bridge recovery, purpose-specific P8 status remained:

    P8 prepared                    true
    P8 authorized                  true
    runner                         HOLD
    Key B STATE                    ACCEPTED
    classification batches         15 / 15
    attention gate                 PASS
    grouping events                10 / 13
    grouping floor                 NOT RUN
    component commitment           NOT FROZEN
    error                          P8_SEMANTIC_OUTPUT_INVALID
    quality replacement required   false
    hidden semantic details        false

The runtime incident did not advance, regenerate, inspect, or alter Key B semantic state.

## 6. Disposition

The local-runtime recovery is complete and the temporary break-glass state has been superseded by a qualified managed release.

Research 429 remains the governing semantic-harness authority. The next project action is unchanged:

    IMPLEMENT_QUALIFY_DEPLOY_P8_V6_GROUPING_CONTRACT_REPAIR

Only after that V6 release is qualified, published, activated and verified with mismatchCount=0 may the single Research-429-authorized fresh resume_after_hold occur.
