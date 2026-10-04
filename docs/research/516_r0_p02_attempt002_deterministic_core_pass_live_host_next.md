# Research 516: R0-P02 Attempt 002 deterministic-core PASS and live-host leg authorization

**Date:** 2026-10-04
**Status:** ATTEMPT 002 DETERMINISTIC CORE PASS / LIVE-HOST LEG AUTHORIZED NEXT / FULL P02 NOT YET CLASSIFIED
**Parent:** Research 513-515
**Probe:** R0-P02
**Candidate under test:** GOVERNED_LEDGER_KERNEL_V02
**Attempt 002 candidate commit:** `83f9fad87e910b75299a3f478cf2b294d9d4ff7a`
**Attempt 002 result commit:** `3cc196f12903725ee703ac2c12ce2e6f2cbd06a9`
**Scope:** Preserve the valid Attempt 002 deterministic-core result and authorize only the already-preregistered Research 514 live-host transport leg.
**Authority:** Deterministic-core result reconciliation only. No full R0-P02 classification, physical-target selection, production implementation, migration, Specification 028 amendment, Runtime Bridge extraction, or authority switch is authorized.

## 1. Attempt integrity

Attempt 002 was prospectively refrozen by Research 515 before implementation.

The bounded implementer changed only:

    experiments/r0_p02_authority_admission_v01/candidate.py

and remained blind to:

    oracle.json
    score.py
    attempt_001_result.md
    any Attempt 002 result

Task-owner postflight confirmed that the diff was limited to canonical external result classification/reporting while preserving the existing mechanism primitives.

The candidate was committed alone and pushed before scoring:

    83f9fad87e910b75299a3f478cf2b294d9d4ff7a
    Freeze R0-P02 candidate attempt 002

Public repository integrity passed.

## 2. Single scorer execution

The frozen scorer was executed exactly once for Attempt 002:

    python experiments/r0_p02_authority_admission_v01/score.py

Observed result:

    deterministic_core = PASS
    case_count         = 20
    error_count        = 0
    errors             = []
    metamorphic_checks = 2
    process exit       = 0

The raw result was frozen before further interpretation at:

    experiments/r0_p02_authority_admission_v01/attempt_002_result.md

and committed/pushed at:

    3cc196f12903725ee703ac2c12ce2e6f2cbd06a9
    Freeze R0-P02 attempt 002 scorer result

## 3. Deterministic-core disposition

Research 514 Section 9 requires:

    score.py exits 0
    deterministic_core = PASS
    error_count = 0
    20/20 cases match
    both metamorphic checks pass

Attempt 002 satisfies all of those gates.

Therefore:

    R0_P02_DETERMINISTIC_CORE=PASS

This is not yet the full R0-P02 result because the preregistered live-host transport leg remains mandatory.

## 4. Live-host authorization

The next action is exactly Research 514 Section 10.

Create temporary refs from the exact coordination-branch head containing the frozen passing candidate result boundary:

    r0-p02-host-v01-base
    r0-p02-host-v01-work

Use only Runtime Bridge GitHub connector capability for the host leg.

The coordination branch must remain unchanged.

The work branch receives exactly one new probe payload:

    experiments/r0_p02_authority_admission_v01/host_probe_payload.json

Then:

    open work -> base PR
    verify exact PR head
    squash merge into base
    fetch merged payload
    prove exact payload/proof preservation across commit transformation
    prove coordination branch unchanged
    clean temporary refs

No production credential or production authority surface is involved.

## 5. Current state

    R0_P02_ATTEMPT_002=VALID
    DETERMINISTIC_CORE=PASS

    LIVE_HOST_LEG=AUTHORIZED_NEXT
    FULL_R0_P02_CLASSIFICATION=NOT_YET_AVAILABLE

    PHYSICAL_ARCHITECTURE_SELECTED=false
    SPECIFICATION_028_AUTHORITY=UNCHANGED

    NEXT=EXECUTE_R0_P02_LIVE_HOST_TRANSPORT_LEG
