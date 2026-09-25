# Research 320: DRP-05a ActionShape PASS and DRP-05b Detective-First PASS

**Date:** 2026-09-25
**Status:** DRP-05A PASS / DRP-05B PASS_DETECTIVE_FIRST / V0.3 MEDIATION-SCOPED AO RETAINED / NEXT DRP-01
**Protocol:** Research 316 / AO10-DRP-V01
**Harness freeze:** Research 319
**Harness freeze commit:** 240e3246d18c5d375e1f04d9f00f0c879fe27965
**Result SHA-256:** fc3649b85fdf23b2028e7f2017b6af2484843af6697859d543860d2430c1de4b
**Durable evidence:** docs/research/project_knowledge_activation_orchestration/ao10/evidence/drp05_run001_result.json
**Scope:** Reconcile DRP-05a/05b against the frozen 65-event corpus and preregistered decision rules.
**Authority:** Research evidence only. It does not authorize AO implementation, provider selection, branch/workflow change, migration or authority switch.

## 1. Execution

Exact frozen command:

    .\.venv\Scripts\python.exe experiments\ao10_drp05_actionshape_mediation_v01\probe.py --output experiments\ao10_drp05_actionshape_mediation_v01\results\run_001

Observed corpus:

    real non-merge Git events     65
    MC-0028 open                 through DRP-09 result
    ease-based exclusions         0

No protocol threshold, corpus rule, classification contract or control changed after result observation.

## 2. DRP-05a result

Primary class:

    PASS

Observed:

    classifiable events                65 / 65
    deterministic coverage             1.00
    high-consequence coverage          1.00
    provider-identity invariance       PASS
    malformed-event fallback           PASS

The frozen real Git history can be normalized deterministically into provider-neutral ActionShape records without relying on provider/model identity.

The result supports the V0.3 direction:

    structured tool/effect classes should use deterministic normalization
    genuinely unsupported/unstructured action shapes should route to review
    provider identity should not determine consequence semantics

This does not prove that every future action family is covered. It validates the real Git-centered action classes in the frozen corpus.

## 3. DRP-05b result

Primary class:

    PASS

Subtype:

    PASS_DETECTIVE_FIRST

Observed mediation classification:

    MEDIATED       0
    COOPERATIVE   53
    UNMEDIATED    12
    UNKNOWN        0

    classification coverage   1.00
    MEDIATED share            0.00
    prevention consistency    PASS
    synthetic MEDIATED control PASS

The zero mediated share is not interpreted as failure because V0.3 no longer claims universal preventive preflight.

It is evidence that the current real coordination path is **detective-first** with respect to AO:

    Project collaborators often participate in governed protocol
    but
    no production AO preflight sits on the effect path

The current system therefore must not describe those actions as technically prevented by AO.

## 4. Important interpretation

The probe measures AO mediation, not generic transport safety.

A Codexless guard, native Git-host permission, repository branch policy or provider confirmation can constrain an action without being an AO preflight.

Those mechanisms may later become qualified adapters or independent admission controls, but they do not retroactively make the current action path MEDIATED.

The provider transport used for every historical commit is also not reconstructed from shared Git author identity.

That is intentional. Shared author identity is insufficient provenance.

## 5. Architecture consequence

V0.3 is retained without semantic amendment.

The empirical result strengthens its mediation-specific guarantee:

    MEDIATED
        preventive AO preflight may be claimed only after a qualified
        AO-controlled interception path exists

    COOPERATIVE / UNMEDIATED
        raw effect control is detective-first
        separate host/WARRANT-F accepted-state controls may still prevent
        downstream admission where independently qualified

This is the exact realism correction Claude requested in Message 003.

F-D LOW MEDIATED SHARE is therefore not unresolved as a target falsifier.

It resolves as:

    current operating reality = detective-first
    target architecture       = mediation-aware
    future preventive coverage = realization/adapter qualification question

No provider or workflow mechanism is selected by this result.

## 6. Probe controls

Provider-identity invariance:

    PASS

Changing synthetic provider labels on five representative real events does not change ActionShape.

Malformed raw event:

    PASS

It routes to MODEL_ASSISTED_REVIEW rather than receiving a guessed deterministic class.

Synthetic AO-mediated event:

    PASS

An event with explicit AO-preflight attestation classifies MEDIATED and permits a preventive claim, proving the mediation harness is capable of producing the opposite class.

## 7. Current state

    DRP09=PASS
    DRP05A=PASS
    DRP05B=PASS_DETECTIVE_FIRST

    DRP05_EVENT_COUNT=65
    DRP05A_COVERAGE=1.00
    DRP05B_CLASSIFICATION=1.00
    DRP05B_MEDIATED_SHARE=0.00

    DRP_RESULT_COUNT=3
    UNRESOLVED_AMEND_RESULTS=0
    ACTIVE_HARNESS_INVALID_RESULTS=0

    V03_ACTIONSHAPE=RETAIN
    V03_MEDIATION_CLASSES=RETAIN
    CURRENT_AO_CONTROL_POSTURE=DETECTIVE_FIRST

    OWNER_DECISION=NOT_READY
    PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=DRP01_CORPUS_AND_HARNESS_FREEZE
