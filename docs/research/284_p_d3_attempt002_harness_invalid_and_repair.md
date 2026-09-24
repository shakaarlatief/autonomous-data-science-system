# Research 284: P-D3 Attempt 002 Harness Invalid and Negative-Control Repair

**Date:** 2026-09-24
**Status:** P-D3 ATTEMPT 002 HARNESS_INVALID / NO ARCHITECTURE INFERENCE / SECOND NARROW PROSPECTIVE REPAIR REQUIRED
**Parent protocol:** Research 277
**Prior harness history:** Research 281, Research 282, Research 283
**Probe:** P-D3
**Attempt:** 002
**Scope:** Preserve the second invalid P-D3 execution, identify the negative-control injection defect, and authorize only the repair needed to make the preregistered forbidden-dependency control discriminate.
**Authority:** Harness-failure record and narrow prospective repair authorization only.

## 1. Attempt 002 binding

    HARNESS_COMMIT
        1841fb62b5f41556381535263b567f43c97d8d2d

    SOURCE_COMMIT
        721545c46b94e0a87c87a572fb357ff314f6913f

The repaired harness from Research 283 was frozen before execution.

## 2. Observed failure

Attempt 002 progressed beyond the Attempt 001 fixture-bootstrap defect.

It then reached the Product forbidden-dependency negative control.

The harness injected:

    import ads_project_system

by prepending it to:

    ads_system/application/reasoning.py

That source contains:

    from __future__ import annotations

The prepended import therefore caused Python to fail first with:

    SyntaxError:
        from __future__ imports must occur at the beginning of the file

The harness correctly refused to count this as a valid negative-control failure because stderr did not contain the intended forbidden module token.

## 3. Classification

    P_D3_ATTEMPT_002=HARNESS_INVALID

The defect is in how the negative control is injected.

No Product/JW1 dependency conclusion is permitted.

    TARGET_ARCHITECTURE_INFERENCE=NONE
    WARRANT_F_V0_2_AMENDMENT_REQUIRED=false
    THRESHOLDS_CHANGED=false

Durable attempt evidence:

    experiments/r8c_assurance_probe_v01/evidence/
        p_d3_run_002_harness_invalid.json

## 4. Narrow prospective repair

The forbidden import may be appended to the copied fixture module instead of prepended.

Because Python executes module top-level statements during import, an appended:

    import ads_project_system

or:

    import ads_system

still exercises the same intended forbidden-dependency condition after the copied module has parsed correctly.

The repair may change only:

    inject()

from prepend to append.

It must not alter:

    source commit
    target-shaped paths
    representative behaviors
    static scan
    expected forbidden module tokens
    result thresholds
    architecture interpretation

## 5. Required next sequence

    repair inject() only
    validate without executing P-D3
    commit and push
    compute Git-blob hashes
    refreeze
    execute as Attempt 003

Attempts 001 and 002 remain preserved.

## 6. Current state

    P_D3_ATTEMPT_001=HARNESS_INVALID
    P_D3_ATTEMPT_002=HARNESS_INVALID
    VALID_P_D3_RESULT=NONE

    REPAIR_SCOPE=APPEND_FORBIDDEN_IMPORT_ONLY
    COMPLETED_VALID_DECISION_PROBES=2_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=REPAIR_REFREEZE_P_D3_ATTEMPT003
