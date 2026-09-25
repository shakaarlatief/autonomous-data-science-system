# Research 319: DRP-05a/05b ActionShape and Mediation Harness Freeze

**Date:** 2026-09-25
**Status:** DRP-05A/05B CORPUS + HARNESS FROZEN / NO SCORED RESULT OBSERVED / EXECUTION NEXT
**Parent protocol:** Research 316 / AO10-DRP-V01
**Previous valid result:** Research 318 / DRP-09 PASS
**Probe:** DRP-05a ActionShape classifiability + DRP-05b action interceptability/mediation
**Corpus base:** 500de961fcfe6c4eaa017cf564ecb5d65ff158e7
**Scope:** Freeze the real Git-history corpus, provider-neutral ActionShape normalization contract, mediation contract, controls and deterministic harness before scored execution.
**Authority:** Probe implementation freeze only. This harness is temporary qualification machinery and has no target-architecture preservation right.

## 1. Corpus selection

Research 316 requires all consequential mutation/handoff events with sufficient durable evidence from MC-0028 and MC-0029 plus associated Git history, with at least 30 events and no ease-based cherry-picking.

The frozen corpus therefore uses every non-merge commit from:

    first event
        4fdb64d753008b777a64f5acb4df3bfd2c339cb8
        Open MC-0028 independent assurance design

through:

    corpus base
        500de961fcfe6c4eaa017cf564ecb5d65ff158e7
        Record DRP-09 assurance request pass

inclusive.

Result:

    event count = 65

No event was removed because it looked difficult to classify.

Each corpus item preserves:

    exact commit SHA
    parents
    date
    commit subject
    changed path/status list
    mechanically derived fixture flags

The fixture is post-hoc evidence about real consequential Project work. It is not production AO state.

## 2. Frozen corpus characteristics

Mechanically derived fixture counts, before scored execution:

    touches durable control-state surfaces       49
    touches research/checkpoint boundary         48
    publishes model-collaboration message         9
    touches experiment/test material             29

The nine collaboration-message publications are included as ordinary corpus events rather than separately curated cases.

The accepted R8-C authority transition commit:

    0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

is explicitly marked as an authority-state-transition witness from accepted repository evidence.

## 3. DRP-05a normalization contract

A real corpus item with structured Git commit evidence maps to the provider-neutral shape:

    operation_family      GIT_COMMIT
    target_family         REPOSITORY_HISTORY
    consequence           REPOSITORY_HISTORY_MUTATION

Additional deterministic consequence classes derive only from frozen path/evidence rules:

    CONTROL_STATE_MUTATION
    COLLABORATION_HANDOFF_PUBLICATION
    QUALIFICATION_ARTIFACT_MUTATION
    GOVERNANCE_CARRIER_MUTATION
    KNOWLEDGE_BOUNDARY_MUTATION
    AUTHORITY_STATE_TRANSITION

Provider/model identity is not an input to ActionShape.

A malformed or unsupported raw event does not receive a guessed shape. It routes to:

    MODEL_ASSISTED_REVIEW

The probe measures whether the real structured corpus is covered by deterministic normalization, not whether every conceivable future action can be classified.

## 4. DRP-05b mediation contract

The mediation question is specifically whether **AO pre-dispatch** could technically prevent the effect.

Generic transport safety, repository write guards, provider permissions or Git protections do not count as AO mediation unless an ADS-controlled AO preflight is actually on the effect path.

At the frozen candidate boundary:

    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false

Therefore a current real event cannot be called MEDIATED merely because it used a governed tool.

Frozen classes:

    MEDIATED
        explicit ADS AO-preflight interception is evidenced

    COOPERATIVE
        no enforced AO preflight, but durable project records evidence
        participation in project protocol/control state

    UNMEDIATED
        no production AO preflight and no durable cooperative-control
        record for the event

    UNKNOWN
        evidence is insufficient to establish mediation

The cooperative evidence rule is mechanical for this fixture: a commit touches a durable control-state surface, research/checkpoint boundary or model-collaboration message.

This is deliberately weaker than claiming prevention.

## 5. Important provenance limitation

Git author identity is shared and therefore cannot identify execution surface.

Claude Message 003 itself records that pre-dispatch prevention was not available for direct collaborator Git actions. The current architecture also explicitly has no production AO preflight.

The harness therefore measures current **AO mediation**, not provider identity.

It does not claim to reconstruct whether every historical event used Codexless, a native GitHub connector, local Git, or another transport.

That provider detail is unnecessary for the core current-state inference:

    absent an AO preflight on the effect path,
    preventive AO control cannot be claimed.

## 6. Negative/sensitivity controls

The frozen controls require:

1. **provider identity invariance**
   Five real events are cloned with different synthetic provider labels.
   Their ActionShape must remain identical.

2. **malformed event fallback**
   A raw event without the supported structured source type must not be
   deterministically guessed.

3. **synthetic mediated witness**
   A target-shaped event with explicit AO-preflight attestation must be
   classified MEDIATED and allow a preventive claim.

These controls prevent the harness from passing merely because it labels everything with the same outcome.

## 7. Frozen harness

    experiments/ao10_drp05_actionshape_mediation_v01/README.md
        sha256 bb92144c0fc58f9d15ddbfed6e49a7298c329e8946f4291eb1d993406ff73410

    experiments/ao10_drp05_actionshape_mediation_v01/classification_contract.json
        sha256 c3bca4570e4f3924a225e8f3995f99f03257f731275782d852d7982e1f95896b

    experiments/ao10_drp05_actionshape_mediation_v01/controls.json
        sha256 bf7c36853a4ca78c989d0803e88e3b079188afa933821e01fddda5f0d98a4da7

    experiments/ao10_drp05_actionshape_mediation_v01/corpus.json
        sha256 842489b97f5bd93615dc4205b2c5cc22f7beab0dba238e168ff386c65f6c9d9f

    experiments/ao10_drp05_actionshape_mediation_v01/probe.py
        sha256 909c7c3b709e0e8391e43911a3df8369bd44ee9cfd8f764c2006217cb383b108

Pre-execution validation:

    Python AST parse       PASS
    JSON fixture parse     PASS

The scored probe has not been run.

## 8. Decision rules

DRP-05a PASS requires:

    corpus >= 30
    deterministic ActionShape coverage >= 90%
    high-consequence Git/repository-event coverage = 100%
    provider-identity invariance control PASS
    malformed-event fallback control PASS

DRP-05b PASS requires:

    mediation classification coverage >= 90%
    preventive-claim semantics consistent with mediation class
    synthetic MEDIATED control PASS

If real MEDIATED share is below 50%, Research 316 permits:

    PASS_DETECTIVE_FIRST

This is not a failure. It means current real action paths support a detective-first AO statement rather than pretending technical prevention already exists.

## 9. Frozen execution

From repository root:

    .\.venv\Scripts\python.exe experiments\ao10_drp05_actionshape_mediation_v01\probe.py --output experiments\ao10_drp05_actionshape_mediation_v01\results\run_001

Expected result:

    experiments/ao10_drp05_actionshape_mediation_v01/results/run_001/result.json

Execution is permitted only after this freeze is committed.

## 10. Current boundary

    DRP09=PASS_RESEARCH318

    DRP05_CORPUS=65_REAL_GIT_EVENTS_FROZEN
    DRP05A_HARNESS=FROZEN
    DRP05B_HARNESS=FROZEN
    DRP05_EXECUTED=false
    DRP05_RESULT=NONE

    OWNER_DECISION=HELD
    PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=EXECUTE_DRP05A_DRP05B
