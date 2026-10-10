# Validation 220: R0-P01 successor Q0 trace and guard unit tests

**Date:** 2026-10-10
**Status:** STATIC TRACEABILITY GUARD PASS / Q1 DESIGN ONLY / NO CRYPTO IMPLEMENTATION QUALIFICATION
**Scope:** Check exact B01/B02-approved source bindings, historical V02 read-only reference hashes, frozen hard-gate inventory and in-memory fault-injection rejection in the proposed Q0 manifest.
**Parent:** Research 531 / Research 530 / Checkpoint 866
**Authority:** Non-sensitive read-only source/guard test evidence only. No real owner experiment, new credentials, full synthetic A/B/C or future fixture freeze.

### Read-only independent baseline checks

- Repository parent HEAD expected `323acf5238a344c4f27d3eded36ecd558efa135d`.
- Old frozen `fixture.json` has exactly thirteen named security controls and S01/S02/S03/L01 effects 1,2,4,30.
- Old result contract retains 60-second median, 120-second individual small and large; viability subset controls 1–10.
- Old inventory frozen projected count 97, effects 157 and effect distribution 62/17/11/7.
- Seven old source identities pinned by exact SHA-256 in the Q0 trace. Approved REV04 contract and policy independently recomputed to their human-authorized hashes.
- Original V02 executable was *read* only, never invoked as owner-run or scorer on private evidence.

### New guard and mutation tests

Command: `python -B scripts/check_r0_p01_successor_trace.py`. Output:

```text
R0_P01_Q0_TRACE_GUARD=PASS requirements=34 controls=13 trials=4 approved_sources=2 historical_artifacts=7
QUALIFICATION_SCOPE=STATIC_TRACEABILITY_ONLY_NOT_OWNER_EXECUTION
```

First `pytest` run in Codexless readOnly profile failed before collection because OS tempfile creation was not permitted. Second pytest attempt under the allowed workspace profile ran **nine** unit tests successfully; the tenth fixture setup failed due to access denied to the system pytest temporary root. Re-run with an isolated new workspace-local pytest base directory (an environment-only change, no test or experiment edits):

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.tmp/r0-p01-q0-guard-check-20261010 tests/unit/test_r0_p01_successor_trace_guard.py
..........                                                               [100%]
10 passed in 0.05s
```

The ten tests include deliberate mutation of control coverage, requirement identity, missing synthetic test mapping, owner-timing threshold, projected inventory, B02 approval status, unauthorized owner-execution lifecycle, premature fixture/implementation qualification claims, and duplicate-key JSON handling. These are in-memory synthetic defects, not modifications of historical accepted evidence. Any new programmatic correctness checks still need independent expected-oracle qualification.

### Limits

No new owner source has been frozen, no cryptographic signature or ES256 RP verification was performed, no true Windows sign-prompt, RP child or filesystem crash-atomicity test ran, and no new owner marker or evidence was created. Q1 remains a revisable design under targeted independent review. Passing 10 tests cannot be presented as passing R0-P01's 13 security gates or predicting actual owner burden.

```text
VALIDATION_220=Q0_STATIC_GUARD_PASS
REQUIREMENTS=34
SECURITY_CONTROLS_PRESERVED=13
UNIT_TESTS=10_PASS
REAL_OWNER_ATTEMPT_002=NOT_AUTHORIZED
```
