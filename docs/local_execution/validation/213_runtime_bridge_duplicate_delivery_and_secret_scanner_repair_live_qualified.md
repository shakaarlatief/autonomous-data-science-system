# Validation 213: Runtime Bridge duplicate-delivery and secret-scanner repair live qualified

**Date:** 2026-10-06
**Status:** EXACT-DUPLICATE COALESCING PASS / >120S LIVE REPRODUCTION PASS / SCANNER REPAIR PASS / LIVE SEMANTIC PUSH INTEGRITY PASS
**Scope:** Preserve the execution evidence that closes the Runtime Bridge concurrency recurrence trigger from Validation 212 and qualifies the separately exposed runtime-private-bootstrap scanner repair.
**Authority:** Operational validation evidence only. This record does not redefine R0-P01, select a physical architecture, change Specification 028, authorize migration, or change project authority.

## 1. Coalescing release

Qualified release:

    releaseId       semantic-git-retry-coalescing-v1
    source commit   8759bc6902b004afaf68796c2bfda0428b68eb3f
    runtime version 0.1.1-preview.80-semantic-git-retry-coalescing
    surface          codexless-public-preview-v2
    tool count       179

Managed release prepare, publish, activation and verify completed successfully. Verification returned zero mismatches.

Release-specific smoke:

    SEMANTIC_GIT_COALESCING_RELEASE_SMOKE=PASS
    exact_duplicate_invocations=1
    post_settlement_new_invocation=true
    unrelated_concurrency_rejected=true

## 2. Exact repair boundary

The active semantic-operation map is factory-scoped and in-memory only.

The coalescing key is an HMAC-SHA256 digest, using a runtime-random secret, over canonicalized:

    [toolName, input]

If an exact key is already active, the later caller joins the existing promise and receives an isolated clone of the same result.

The active entry is deleted when the original operation settles. There is no completed-result replay cache.

The global concurrency limit remains one. Unrelated semantic operations are still rejected when the slot is occupied. The joined-waiter limit is four.

## 3. Live >120-second duplicate-delivery reproduction

After activation, one ordinary semantic `codex.git_pull_ff_only` operation against the private local-runtime repository produced:

    original receipt duration_ms = 142379
    original admission_accepted  = true
    original max_concurrent      = 1

A second arrival appeared roughly 120.6 seconds later while the first was still running.

Both receipts had the same opaque RPC identity tag.

Original lifecycle:

    arrived
    callback_started
    admission_accepted
    guarded_handler_started
    guarded_body_exited
    slot_released
    returned

Duplicate lifecycle:

    arrived
    callback_started
    returned

The duplicate did not record a second `admission_accepted` event and did not return `bridge concurrency limit reached (1)`.

Both completed successfully within milliseconds of each other. Repository postflight remained clean and unchanged.

Result:

    LIVE_OVER_120_SECOND_OPERATION=true
    HOST_DUPLICATE_DELIVERY_OBSERVED=true
    EXACT_DUPLICATE_JOINED=true
    UNDERLYING_INVOCATION_COUNT=1
    FALSE_CONCURRENCY_REJECTION=false
    POSTFLIGHT_OK=true

## 4. Scanner defect reproduction

The installed pre-repair `runtime-private-bootstrap` scanner rejected the tracked private runtime repository with:

    obvious secret-like material rejected in tracked file:
    .ads-private/codexless/public-call-lifecycle-candidate/src/mcp-http-public.mjs

The relevant source was an ordinary runtime expression:

    accessToken: runtimeInstanceIdentity?.shutdownToken ?? ""

The generic assignment heuristic treated the identifier prefix as a literal credential-like value.

No actual credential was identified by this observation.

## 5. Scanner correction and focused regression

The generic named-field assignment heuristic was narrowed to quoted token-like literals. Known token-shape patterns and secret-bearing-path checks remain separate.

Focused candidate regression returned:

    RUNTIME_SECRET_SCANNER_FIX=PASS
    safe_expressions=true
    quoted_literals_rejected=true
    known_token_shape_rejected=true
    private_companion=true

The corrected scanner was also executed against the complete tracked private runtime repository and returned:

    RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
    tracked regular text files = 1355
    content bytes = 35079653

## 6. Fail-closed release packaging

Two invalid release package states were observed and rejected before activation.

First:

    RUNTIME_RELEASE_REGRESSION_MISSING

because the release regression list referenced `test/runtime-maintenance-regression.mjs`, which is not present in the current live runtime test set.

Second:

    RUNTIME_RELEASE_MANIFEST_NONCANONICAL

because the first V3 manifest bytes were not the exact canonical `JSON.stringify(value, null, 2) + "\n"` form required by the release reader.

Both defects were corrected prospectively. Neither was bypassed.

## 7. Final scanner release

Final qualified source:

    f296fa029cf523fad55237dbd42b821392355f11

Final release:

    releaseId       runtime-secret-scanner-fix-v3
    runtime version 0.1.1-preview.81-runtime-secret-scanner-fix
    surface          codexless-public-preview-v2
    tool count       179

Managed prepare:

    status = prepared

Managed publication:

    status = succeeded

Runtime restart:

    status = succeeded

Post-activation verification:

    status = verified
    mismatchCount = 0

Health after activation:

    ok = true
    version = 0.1.1-preview.81-runtime-secret-scanner-fix
    surfaceVersion = codexless-public-preview-v2
    toolCount = 179

## 8. Live installed scanner-path test

An actual semantic no-op push against the synchronized private runtime repository returned:

    exitCode = 0
    upstream = origin/main
    integrityPolicyId = runtime-private-bootstrap
    integrity = RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
    [up to date]
    trackedWorkingTreeCleanAfter = true
    postflightOk = true

This confirms that the repaired scanner is active in the real semantic push path.

## 9. Public ADS publication reconciliation

The previously local-only public ADS checkpoint commit:

    cd3558c2cd75c2c65c9c988b12ea8a9b7e90e199
    Preserve Runtime Bridge recovery and concurrency trigger

was then published through semantic Git.

The first post-repair public push invocation crossed the long-duration boundary and received an exact duplicate delivery. The duplicate was coalesced, not rejected for concurrency. The underlying operation returned a terminal tool error and the public remote remained unchanged.

After authoritative state reconciliation and a direct public integrity check:

    PUBLIC_REPOSITORY_INTEGRITY=PASS

one new semantic push attempt was made. It succeeded:

    origin/v1-source-vault-bootstrap-resume
    5f41625a..cd3558c2

Postflight:

    HEAD == origin/v1-source-vault-bootstrap-resume
    trackedWorkingTreeCleanAfter = true
    postflightOk = true

The retry therefore followed the no-blind-replay rule: terminal state and repository effect were reconciled before a new mutation attempt.

## 10. Validation conclusion

    DUPLICATE_DELIVERY_ROOT_CAUSE_LOCALIZED=true
    COALESCING_RELEASE_LIVE=true
    LIVE_DUPLICATE_DELIVERY_REPRODUCTION=PASS
    FALSE_CONCURRENCY_REJECTION_PREVENTED=true
    UNRELATED_CONCURRENCY_POLICY_PRESERVED=true

    SCANNER_FALSE_POSITIVE_REPRODUCED=true
    SCANNER_FIX_FOCUSED_REGRESSION=PASS
    SCANNER_FIX_FULL_REPOSITORY_SCAN=PASS
    SCANNER_RELEASE_LIVE=true
    SCANNER_RELEASE_VERIFY_MISMATCHES=0
    LIVE_SEMANTIC_PUSH_SCANNER_GATE=PASS

    CHECKPOINT_855_PUBLICATION_RECONCILED=true
    R0_P01_RUNTIME_BLOCKER_CLOSED=true
    NEXT=BOUNDED_MANUAL_CODEX_R0_P01_HARNESS_IMPLEMENTATION
