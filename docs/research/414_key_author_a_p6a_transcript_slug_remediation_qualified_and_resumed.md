# Research 414: Key Author A P6A Transcript-Slug Remediation Qualified and Resumed

**Date:** 2026-09-30
**Status:** TRANSCRIPT-SLUG REMEDIATION QUALIFIED / PUBLISHED / ACTIVATED / P6A RESUMED
**Parent:** Research 413
**Scope:** Preserve qualification and activation of the mechanical transcript-path remediation and the governed fresh-session resumption of P6A.
**Authority:** Mechanical runner remediation and resumption only. Research 410 semantic scope is unchanged. This record does not authorize P6B/P6C out of order, canonical Key A assembly, Key A commitment generation, Key Author B, scoring, successor implementation, migration, oracle retirement, or authority switching.

## 1. Successor runtime release

The Research 413 remediation was implemented in the managed local-runtime repository as:

    release ID
        p6-private-ops-v3

    target version
        0.1.1-preview.58-p6-transcript-slug-public

    local-runtime commit
        f44d868385e4bbbada78884957857e567bef0b7b

    public tool count
        175

    manifest SHA-256
        3380c8ddcfc5c1984ab915fb060a25fd573643e22372ca3ae766fcd25d92eb37

The local-runtime commit was pushed and synchronized with origin/main.

## 2. Minimal code change

The semantic runner logic remains unchanged except for Claude project-slug reconstruction.

V2:

    cwd.replace(/:/g, "-").replace(/[\\/]/g, "-")

V3:

    cwd.replace(/:/g, "-").replace(/[\\/]/g, "-").replace(/_/g, "-")

No semantic prompt, source order, model, effort, tool allowlist, schema, evidence rule, grouping rule, gate threshold, witness/control rule, retry policy, or owner-authorization rule changed.

## 3. Regression qualification

The transcript regression and headless smoke were strengthened to use a P6-style cwd containing:

    p6_jobs

while writing the synthetic transcript under the Claude-style project slug containing:

    p6-jobs

Direct qualification returned:

    P6_LEGACY_OPS_REGRESSION=PASS
        sources=17
        items=3088
        subphases=3
        freshSessions=51

    P6_HEADLESS_RUNNER_SMOKE=PASS
        cliFlags=PASS
        structuredOutput=PASS
        transcript=PASS

    P5_PRIVATE_OPS_REGRESSION=PASS
        batches=18
        presentations=3210
        attentionPairs=122

    P4_PRIVATE_OPS_REGRESSION=PASS

The copied public-surface registration test remains non-standalone inside an isolated release-bundle directory because the delta bundle does not carry every live runtime module. The managed release pipeline composes the candidate over the live runtime and runs the complete registered regression set.

Managed publication succeeded, therefore the complete governed staged release regression suite passed.

## 4. Publication and activation

Managed release preparation returned:

    prepared

Managed publication operation:

    rm_fe158afd4aadf673d9614dcd05ceeea2
    SUCCEEDED

Pre-activation verification returned:

    VERIFIED
    mismatchCount = 0

Runtime activation operation:

    rm_9a908772b02a54db1cd02917a8353021
    SUCCEEDED

Post-activation verification returned:

    VERIFIED
    mismatchCount = 0

## 5. Governed resumption

After activation, the bounded P6 status still correctly reported:

    currentSubphase = P6A
    runnerStatus = HOLD
    errorCode = ENOENT

The purpose-specific operation was then invoked with exactly:

    action = resume_after_hold

It returned:

    ok = true
    resumed = true
    currentSubphase = P6A
    acceptedPrefixPreserved = true
    runnerStatus = RUNNING
    hiddenSemanticDetailsExposed = false
    next = STATUS

The new orchestration therefore starts fresh Claude Code sessions for the unfinished suffix.

Because the prior accepted prefix was zero, the first source is rerun from the beginning in a fresh session.

The failed prior transcript remains preserved but is not resumed, continued, inspected, or supplied to the replacement session.

## 6. Current live state

Subsequent bounded status reports:

    currentSubphase = P6A
    runnerStatus = RUNNING
    boundaryReady = false
    hold = false
    errorCode = null

No P6A completion claim is yet made.

No P6B or P6C execution has started.

No canonical Key A assembly has started.

## 7. Exact next step

Continue to poll only the bounded P6 status surface.

If P6A reaches:

    COMPLETE

then invoke:

    finalize_subphase

to verify/freeze the complete P6A artifact set and advance to P6B.

If P6A reaches:

    HOLD

stop again for governed diagnosis.

    P6A_REMEDIATION=QUALIFIED_ACTIVATED
    P6A_RESUMED=true
    P6A_CURRENT_STATUS=RUNNING
    P6B=NOT_STARTED
    P6C=NOT_STARTED
    KEY_A_CANONICAL_ASSEMBLY_AUTHORIZED=false
    KEY_AUTHOR_B_AUTHORIZED=false
    NEXT=WAIT_FOR_BOUNDED_P6A_COMPLETE_OR_HOLD_BOUNDARY
