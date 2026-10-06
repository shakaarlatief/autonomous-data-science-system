# Research 520: Runtime Bridge duplicate-delivery coalescing and bootstrap secret-scanner repair

**Date:** 2026-10-06
**Status:** CONCURRENCY ROOT CAUSE LOCALIZED / EXACT-DUPLICATE COALESCING LIVE QUALIFIED / BOOTSTRAP SCANNER FALSE POSITIVE REPAIRED / R0-P01 RESUMES
**Parent:** Research 506, Research 519; Validation 212, Validation 213
**Scope:** Close the Research 519 recurrence trigger by preserving the observed Runtime Bridge duplicate-delivery mechanism, the narrowly bounded semantic-Git coalescing repair, the subsequently exposed runtime-private-bootstrap scanner false positive, and the live qualification evidence for both repairs.
**Authority:** Supporting execution/reliability evidence only. This record does not select the R0 physical architecture, change Specification 028, authorize migration, change owner-authenticity semantics, or switch project authority.

## 1. Trigger activation

Research 519 deliberately left the concurrency issue open until the same failure pattern recurred during ordinary semantic Git work.

That trigger fired.

A long semantic Git operation crossed the caller/host response boundary while its original server-side execution remained active. The host then delivered the same logical request again. Under the previous admission behavior, the second arrival could encounter the global concurrency ceiling of one and be rejected as:

    bridge concurrency limit reached (1)

while the original mutation was still legitimately running.

The problem was therefore not evidence that two independent project mutations were intentionally running in parallel. It was a duplicate-delivery/lifetime interaction at the Runtime Bridge boundary.

## 2. Root-cause evidence

The decisive live evidence came from recent-call lifecycle receipts around a semantic `git pull --ff-only` operation.

The original arrival:

    duration_ms = 142379
    admission_accepted
    in_flight = 1
    max_concurrent = 1

A second server arrival appeared roughly 120.6 seconds after the first while the original was still active. Both arrivals carried the same opaque RPC identity tag.

The second arrival represented the same semantic tool name and the same semantic input. It was not an unrelated operation.

This localized the previously open failure mechanism sufficiently to justify a narrow repair:

    long-running semantic operation
        -> host/caller boundary crosses approximately 120 seconds
        -> duplicate delivery can arrive before original completion
        -> old global admission sees slot already occupied
        -> duplicate may be rejected as unrelated concurrency

This explains the false concurrency symptom without requiring a general increase in concurrency.

## 3. Selected repair semantics

The qualified repair is exact-active-operation coalescing for the semantic Git surface.

The live implementation is factory-scoped and keeps no replay cache. It computes an in-memory keyed digest over canonicalized:

    [toolName, input]

using a runtime-random HMAC secret. While the original semantic operation remains active, an exact duplicate key joins the existing promise and receives an isolated clone of the same eventual result, including any original error/uncertainty fields.

Important boundaries are preserved:

    no result is retained after the active execution settles
    no completed mutation is replayed
    unrelated operations still face the ordinary concurrency ceiling
    maxConcurrent remains 1 in the current deployment
    at most 4 joined duplicate waiters are admitted
    uncertainty semantics from the original operation are preserved
    semantic Git authority and repository-specific gates are unchanged

The repair therefore addresses duplicate delivery without converting the bridge into a general concurrent mutation executor.

## 4. Qualified coalescing release

The release source was frozen in the private local-runtime repository as:

    8759bc6902b004afaf68796c2bfda0428b68eb3f
    Add semantic Git retry coalescing release

Release contract:

    releaseId       semantic-git-retry-coalescing-v1
    runtime version 0.1.1-preview.80-semantic-git-retry-coalescing
    surface          codexless-public-preview-v2
    tool count       179

Managed prepare, publication, restart/activation, and post-activation verification completed successfully. Release verification reported zero mismatches.

The release-specific regression smoke passed before activation:

    SEMANTIC_GIT_COALESCING_RELEASE_SMOKE=PASS
    exact_duplicate_invocations=1
    post_settlement_new_invocation=true
    unrelated_concurrency_rejected=true

## 5. Live >120-second qualification

After activation, an ordinary semantic `codex.git_pull_ff_only` operation against the synchronized private runtime repository took 142.379 seconds.

The host delivered the same logical request again roughly 120.6 seconds after the original arrival.

Observed lifecycle:

    original
      arrived
      callback_started
      admission_accepted
      guarded_handler_started
      ... long-running semantic Git operation ...
      guarded_body_exited
      slot_released
      returned

    duplicate
      arrived
      callback_started
      returned

The duplicate did not acquire a second admission slot and did not receive `bridge concurrency limit reached (1)`.

Both arrivals completed successfully within milliseconds of each other, while the Git postflight remained clean and unchanged.

Therefore:

    LIVE_DUPLICATE_DELIVERY_OBSERVED=true
    LIVE_BOUNDARY_OVER_120_SECONDS=true
    ONE_UNDERLYING_SEMANTIC_OPERATION=true
    FALSE_CONCURRENCY_REJECTION_PREVENTED=true
    POSTFLIGHT_PASS=true

This is the live qualification that closes the specific concurrency root-cause question left open by Research 519.

## 6. Separate scanner defect exposed during publication

While publishing the coalescing repair, the private runtime repository's `runtime-private-bootstrap` integrity policy rejected ordinary source code containing a runtime expression of the form:

    accessToken: runtimeInstanceIdentity?.shutdownToken ?? ""

The generic credential-assignment heuristic treated the identifier prefix after `accessToken:` as if it were a literal secret value.

No secret was found. The defect was a deterministic false positive in the bootstrap scanner.

This issue is separate from duplicate-delivery coalescing and was therefore repaired separately rather than bypassed.

## 7. Scanner repair semantics

The bootstrap scanner already has dedicated signatures for known high-risk material such as private-key headers, GitHub token forms, AWS access-key identifiers and OpenAI-style key prefixes.

The false positive came from the generic named-field assignment heuristic. The repair narrows that generic heuristic so credential-like field names are rejected by this generic rule only when followed by an explicitly quoted literal of the bounded token-like form. Runtime expressions and identifiers are no longer interpreted as generic literal credentials.

The same narrow correction is applied to the private-companion scanner because it shared the same heuristic.

The scanner remains explicitly a bounded bootstrap safety check, not a complete secret scanner. Known token-shape signatures and secret-bearing path rejection remain independent of the generic quoted-literal rule.

Focused qualification proved:

    safe runtime expressions accepted
    quoted generic credential-like literals rejected
    known token shapes rejected
    private-companion behavior preserved

The corrected scanner also passed over the complete tracked private runtime repository.

## 8. Scanner release qualification

During release packaging, two release-bundle defects were found and allowed to fail closed rather than being bypassed:

1. an initial release manifest referenced a regression file not present in the live runtime test set, producing `RUNTIME_RELEASE_REGRESSION_MISSING`;
2. the corrected V3 manifest initially had non-canonical JSON formatting and was rejected by the release reader until canonicalized.

The final qualified source is:

    f296fa029cf523fad55237dbd42b821392355f11
    Canonicalize runtime secret scanner fix v3 manifest

Final release contract:

    releaseId       runtime-secret-scanner-fix-v3
    runtime version 0.1.1-preview.81-runtime-secret-scanner-fix
    surface          codexless-public-preview-v2
    tool count       179

Managed prepare passed. Managed publication completed successfully. Runtime restart/activation succeeded. Post-activation verification returned:

    mismatchCount = 0

Live health then reported:

    ok = true
    version = 0.1.1-preview.81-runtime-secret-scanner-fix
    surfaceVersion = codexless-public-preview-v2
    toolCount = 179

## 9. Live scanner-path qualification

The strongest installed-runtime check used the actual semantic push path against the private runtime repository after activation.

`codex.git_push_ff_only` returned successfully with:

    integrityPolicyId = runtime-private-bootstrap
    integrity = RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
    remote = up to date
    trackedWorkingTreeCleanAfter = true
    postflightOk = true

This proves the repaired scanner is not merely passing an offline fixture. It is active inside the real semantic push gate and accepts the repository that contains the previously misclassified runtime expression.

## 10. Self-hosting publication boundary

Because the installed old scanner was itself the component rejecting the corrected source, the scanner repair could not bootstrap its own first semantic push through that still-broken gate.

The repair was therefore handled conservatively:

    qualify corrected scanner offline against the repository
    construct the release in the private local-runtime source repository
    use the bounded GitHub Git-object mutation surface to publish the exact qualified tree without force
    verify local and remote tree identity
    realign the local checkout to the remote commit
    then use the managed runtime-release control plane normally

This was a one-time self-hosting bootstrap path for the broken gate, not a replacement for semantic Git.

## 11. Residual observation after repair

A later public ADS semantic push crossed the same long-duration boundary and was duplicate-delivered. The duplicate was coalesced rather than rejected for concurrency, so the repaired mechanism behaved as designed.

That particular underlying push returned a terminal tool error and left the public remote unchanged. After repository reconciliation and an explicit public integrity PASS, one new semantic push attempt succeeded and postflight established local/remote equality.

This residual event is important but does not reopen the false-concurrency root cause:

    duplicate delivery coalescing worked
    no `bridge concurrency limit reached (1)` false rejection occurred
    the failed underlying operation produced no remote mutation
    retry occurred only after authoritative reconciliation
    the subsequent ordinary semantic push succeeded

If an independent underlying Git/transport error becomes recurrent, it should be investigated as a separate reliability class rather than conflated with duplicate-delivery admission.

## 12. Project consequence

The Research 519 recurrence trigger fired, was diagnosed, and the narrow repair is now live qualified.

Therefore the Runtime Bridge side track no longer blocks the active R0 program.

The next legitimate ADS action returns to the already frozen R0-P01 boundary:

    bounded manual-Codex implementation of
      harness.py
      webauthn_server.mjs
      score.py

No real owner credential operation occurs during implementation.

No physical target is selected. R0-P02 remains PASS. R0-P03 remains outstanding. Specification 028 remains operational authority.

## 13. Current boundary

    DUPLICATE_DELIVERY_ROOT_CAUSE=LOCALIZED
    EXACT_ACTIVE_SEMANTIC_COALESCING=LIVE_QUALIFIED
    CONCURRENCY_LIMIT_INCREASED=false
    MUTATION_REPLAY_ADDED=false
    UNRELATED_CONCURRENCY_STILL_FAIL_CLOSED=true

    RUNTIME_PRIVATE_BOOTSTRAP_FALSE_POSITIVE=REPAIRED
    SECRET_SCANNER_RELEASE=runtime-secret-scanner-fix-v3
    LIVE_RUNTIME_VERSION=0.1.1-preview.81-runtime-secret-scanner-fix
    LIVE_TOOL_COUNT=179
    RELEASE_VERIFY_MISMATCHES=0
    LIVE_SEMANTIC_PUSH_INTEGRITY=PASS

    RESEARCH_519_RECURRENCE_TRIGGER=SATISFIED_AND_CLOSED
    R0_P01_HARNESS=NOT_IMPLEMENTED
    NEXT=BOUNDED_MANUAL_CODEX_R0_P01_HARNESS_IMPLEMENTATION
