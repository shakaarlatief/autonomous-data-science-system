# MC-0019 Resolution: W5 T1 Blind Subject-Placement Calibration Closed

**Thread:** MC-0019
**Date resolved:** 2026-09-20
**Status:** RESOLVED / T1 V0.1 DIRECTION SUPPORTED / V0.2 REFINEMENT REQUIRED
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Task owner:** ChatGPT / `chatgpt-27`
**Independent reviewer:** Claude / fresh Opus session
**Reviewer-fixture target:** `dcd01d865340c0d562c07f68307ef0a2c7ee2d75`
**Source-corpus boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Authority:** Collaboration evidence only. Research 215 records the T1 V0.1 design disposition.

## Result

MC-0019 successfully measured cross-model placement behavior without exposing ChatGPT's frozen annotations or T1 outputs to Claude before Message 001.

The result is asymmetric:

```text
preferred-route agreement
    22 / 24 (91.7%)
    strong

exact full subject-set agreement
    7 / 24 (29.2%)
    too weak for production multi-membership freeze

micro membership F1
    0.753

main disagreement
    secondary-membership admission density

missing-vocabulary pressure
    admissibility / authority
```

The controlled semantic-subject architecture remains supported. V0.1 is not accepted as the production subject contract.

## Required refinement

Research 215 carries forward:

```text
explicit membership admission rule
per-subject description
include_when / exclude_when guidance
display-only preferred_parent semantics
admissibility-authority subject
clarified subject-boundary definitions
fresh blind V0.2 calibration
```

## Close

```text
MC0019=RESOLVED
T1_V0_1=DIRECTION_SUPPORTED_NOT_FROZEN
NEXT=T1_V0_2_REFINEMENT_AND_FRESH_BLIND_CALIBRATION
```
