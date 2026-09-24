# Research 278: P-H Current Host Capability Study

**Date:** 2026-09-24
**Status:** P-H INCONCLUSIVE / CURRENT EXECUTION-SURFACE CAPABILITY GAP / NO TARGET PROVIDER SELECTION / NO HOST MUTATION
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-H
**Scope:** Read-only observation of current Git-host assurance/enforcement capabilities available from the active ChatGPT execution surface.
**Authority:** Empirical provider/executor evidence only. This result neither selects nor rejects GitHub as the target assurance provider.

## 1. Preregistered question

Which trust/enforcement properties can the current GitHub installation support today?

The probe was explicitly read-only.

No branch protection, ruleset, workflow, identity, permission or repository setting was authorized to change.

## 2. Observation attempts

The active execution surface attempted bounded read-only GitHub operations through the available Runtime Bridge:

    repository metadata read
    branch-protection reads
    check-run reads

The GitHub read surface failed before returning repository settings with:

    the OS-backed GitHub credential store is unavailable;
    plaintext fallback is forbidden

A separate local GitHub CLI authentication check reported:

    active GitHub account configured
    stored token invalid
    re-authentication required

No authentication repair was attempted because P-H is read-only and credential mutation was not authorized.

No host setting was changed.

## 3. Important asymmetry

The same broader working environment can still:

    fetch repository Git data
    pull branch state
    commit locally
    push through the bounded Codexless Git path

while the host-settings/checks read surface used by P-H is unavailable from this execution surface.

This is direct evidence for Research 276:

    execution surface
        !=
    capability set
        !=
    trust class

It is not safe to infer:

    "ChatGPT has GitHub access"
        therefore
    "ChatGPT can inspect every GitHub assurance/control surface"

nor:

    "a model can push Git"
        therefore
    "the same model can read/mutate branch protection"

## 4. What was not observed

The probe did NOT establish current facts about:

    branch-protection presence
    ruleset configuration
    required-status producer binding
    protected-location workflow definitions
    GitHub App status-authentication behavior
    exact current host-admin boundaries

Historical repository records may contain earlier observations, but they are not substituted for a current read in this probe.

## 5. Result

Under Research 277:

    P-H=INCONCLUSIVE

More specifically:

    CURRENT_GITHUB_CAPABILITY=UNKNOWN_FROM_ACTIVE_READ_SURFACE
    CURRENT_EXECUTION_SURFACE_HOST_SETTINGS_READ=UNAVAILABLE
    HOST_MUTATION_ATTEMPTED=false

This is not:

    TARGET_ARCHITECTURE_AMEND

and not:

    GITHUB_REJECTED

## 6. Architecture interpretation

WARRANT-F V0.2 remains unchanged.

The result strengthens three existing rules:

    WF-A34
        executor capability must be explicit

    WF-A35
        execution surface does not imply trust

    WF-A36
        provider/workflow mechanism remains open

The future host/provider feasibility stage must use an execution surface with authorized, working read capability.

If GitHub later cannot satisfy target T2 authenticity or exact-subject enforcement, the architecture is free to:

    use a different GitHub realization
    use a separate producer identity
    use different host controls
    use a different provider
    or use another version-control/promotion mechanism

The architecture is not weakened to fit today's observation surface.

## 7. Owner-decision effect

Research 277 allows INCONCLUSIVE when explicitly scoped.

This P-H result does not falsely support a T2 implementation claim.

Therefore it does not by itself block eventual semantic architecture acceptance, provided:

    target T2/provider realization remains unclaimed and unresolved

    host/provider realization is qualified before any dependent cutover

    no decision report treats current hosted execution as authenticated T2

## 8. Current state

    P_H=INCONCLUSIVE
    CURRENT_DEBT_CLASS=EXECUTION_SURFACE_CAPABILITY
    TARGET_ARCHITECTURE_CHANGE=NO
    TARGET_PROVIDER_SELECTED=false
    HOST_MUTATION=false

    COMPLETED_DECISION_PROBES=1_OF_8
    NEXT=P_D6_EXECUTOR_CAPABILITY_TRUST_SEPARATION
