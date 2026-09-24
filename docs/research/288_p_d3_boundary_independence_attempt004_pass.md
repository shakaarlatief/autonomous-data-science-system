# Research 288: P-D3 Boundary Independence Attempt 004 PASS

**Date:** 2026-09-24
**Status:** P-D3 PASS / PRODUCT-JW1-ENGINEERING BOUNDARY REALIZABILITY SUPPORTED / NO TARGET ARCHITECTURE AMENDMENT / NO PHYSICAL MIGRATION
**Parent protocol:** Research 277
**Harness freeze:** Research 287
**Frozen harness commit:** 542018f1290864bc7735c896a64f5aed5de48a76
**Frozen source commit:** 721545c46b94e0a87c87a572fb357ff314f6913f
**Probe:** P-D3
**Attempt:** 004
**Candidate:** WARRANT-F V0.2
**Scope:** Record the first valid P-D3 result after preserving three harness-invalid attempts.
**Authority:** Empirical architecture evidence only.

## 1. Result

Observed:

    P-D3
    result                         PASS
    Product Python files scanned   35
    JW1 Python files scanned       54
    Product import violations       0
    JW1 import violations           0

Durable evidence:

    experiments/r8c_assurance_probe_v01/evidence/
        p_d3_run_004.json

Harness binding matches Research 287 exactly.

## 2. Layer A: current-state observation

At frozen source commit 721545c46b94e0a87c87a572fb357ff314f6913f, the explicit absolute-import scan found:

    src/ads_system/
        35 Python files
        0 imports of tools, project, ads_project_system

    tools/project_knowledge/
        54 Python files
        0 imports of ads_system, project.engineering, tests, scripts

Representative isolated Product reasoning behavior and JW1 identity-index behavior both passed without the forbidden neighboring runtime present.

## 3. Layer B: target-shaped isolation

Target-shaped fixtures used product/runtime/src/ads_system/ and project/system/src/ads_project_system/.

Observed:

    Product representative behavior   PASS
    JW1 representative behavior       PASS

This supports the accepted direction that Product runtime does not require Project runtime correctness and JW1 does not require Engineering runtime correctness.

## 4. Negative controls

Product fixture deliberately imported ads_project_system and failed with ModuleNotFoundError.

JW1 fixture deliberately imported ads_system and failed with ModuleNotFoundError.

The repaired child interpreter using -I -S therefore actually removes ambient site-package leakage.

## 5. Attempt history

    Attempt 001   HARNESS_INVALID / nonexistent tools/__init__.py assumption
    Attempt 002   HARNESS_INVALID / forbidden import injected before __future__
    Attempt 003   HARNESS_INVALID / ambient venv site-packages defeated absence control
    Attempt 004   PASS

The invalid attempts remain assurance-harness evidence and are not erased.

## 6. Architecture interpretation

    P_D3=PASS
    TARGET_ARCHITECTURE_EVIDENCE=SUPPORTED
    CURRENT_IMPLEMENTATION_DEBT=false
    WARRANT_F_V0_2_AMENDMENT_REQUIRED=false

The result is bounded. It demonstrates representative realizability, not exhaustive proof that every future module is dependency-clean.

## 7. Current state

    P_H=INCONCLUSIVE
    P_D6=PASS
    P_D3=PASS

    COMPLETED_VALID_DECISION_PROBES=3_OF_8
    UNRESOLVED_AMEND_RESULTS=0
    HARNESS_INVALID_RESULTS_PRESERVED=3

    OWNER_ASSURANCE_DECISION=HELD
    NEXT=P_D5_ADAPTER_FIDELITY
