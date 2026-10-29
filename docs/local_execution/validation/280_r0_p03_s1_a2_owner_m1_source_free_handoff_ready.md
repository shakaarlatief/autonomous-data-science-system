# Validation 280: M1 owner-side source-free recipient handoff readiness

**Date:** 2026-10-29
**Status:** SOURCE_FREE_M1_OWNER_RUNBOOK_AND_NONMUTATING_SELFTEST_PASS / ACTUAL_OWNER_RECIPIENT_NOT_CREATED / REAL_CANDIDATE_PROTECTED_OUTPUT_PENDING
**Scope:** Convert the already selected Research 600 owner-mediated M1 candidate route and Research 612 tested encryption format into a directly executable owner-side **source-free** Prepare/Receive/Verify handoff, with no new device, OS principal, historical source or owner credential created by the exposed coordinator.
**Basis:** Research 574/589/597–603/608–612, Validation 259/269/275–279, original S1 A2 actor admission gates, Checkpoint 898 and Specification 028 unchanged.

## 1. Why this is not a new isolation architecture

Research 574 explicitly deferred open-ended VM/Docker/OS isolation work and selected proportional, controlled-independence qualification. Research 600 compared actual reviewer workflow routes and selected **M1: owner-mediated independently operated candidate reviewer with protected output** as the next candidate route, with a Windows second account/service only as optional responses to demonstrated material failures. Research 603 had already completed one independently owner-mediated fictional CMS transfer, but its fixed fake output cannot serve as a new actual candidate's complete variable-length source-status evidence.

Research 609–611 then measured a genuinely different prospective candidate session's source-free text/PNG inbound representation and binary outbound delivery. Research 612 and Validation 279 locally qualified a new variable-length invented-source private report, owner-side CMS authentication and passphrase-encrypted test key readback, while not creating an actual recipient or invoking the candidate.

**This validation does not reverse Research 600 or assert that a new device/account is required.** The actual next step is the owner's *voluntary*, explicitly invoked source-free M1 trial on the current PC. Different OS or provider authorities remain escalation triggers only if the chosen route reveals a material isolation failure or if an existing science gate cannot be satisfied.

## 2. Exact owner-executed handoff

Added `scripts/r0_p03_s1_a2_owner_source_free_recipient.ps1`. Its four bounded owner-side actions are:

| Action | Owner-visible behavior | Evidence boundary |
| --- | --- | --- |
| `SelfTest` | Check existing local Python/OpenSSL/reader script and Downloads, print no-credential marker | Nonmutating preflight, not owner credential test |
| `Prepare` | User explicitly enters a fresh passphrase into local interactive OpenSSL to create a disposable 7-day self-signed test certificate and encrypted private key, then exports only the public certificate to Downloads | **Not invoked by coordinator**. Same Windows SID and owner+SYSTEM ACL alone do not independently establish full role isolation |
| `Receive` | Owner supplies exact source-free candidate CMS file, expected SHA-256 and fresh recipient ID; verify bytes, store ciphertext and minimum receipt without overwriting, invoke interactive passphrase reader for full canonical report check | **Not invoked**. Must be observed from actual candidate with public-only certificate, not old A1 test key |
| `Verify` | A separate owner invocation reopens versioned stored ciphertext and receipt and performs complete authenticated readback again | **Not invoked**. Supports later recovery evidence only if actually executed |

Private key and owner root are not printed. The public certificate, its SHA-256 and non-secret recipient ID may be carried to the prospective Temporary Chat. The owner's password never appears in a tool argument, env var or AI conversation; cancellation or invalid key encryption aborts. The owner can run `SelfTest` without generating anything, then explicitly opt in to `Prepare`.

The candidate-facing brief `experiments/r0_p03_navigation_probe/S1_A2_CANDIDATE_PROTECTED_OUTPUT_ROUTE_PROBE_V01.md` now includes exact PowerShell commands and follow-up steps. All materials remain invented source-free fixtures; no actual historical source body or independent reviewer finding is in the packet.

## 3. Tests, actual observations and remaining hold

The new `tests/unit/test_r0_p03_s1_a2_owner_source_free_recipient.py` checks PowerShell 5.1 syntax through its parser without executing owner actions, the real **nonmutating** `SelfTest` response, rejection of mismatched SelfTest parameters, strict recipient-ID contract, no plaintext private-key form, no command-line passphrase, safe public certificate export fields, expected digest/canonical receipt checks and the Python owner reader's source-level interactive-passphrase requirement.

Early testing included a proposed nested Python process test for noninteractive input. It timed out twice within the Runtime Bridge sandbox due to inherited child pipe/input behavior, even when the test used `stdin=DEVNULL`. It was **removed as a non-credible dynamic witness** rather than laundering the timeout into a provider/OS denial PASS. The fail-closed `sys.stdin.isatty()` and `getpass` source contract remains statically asserted, and the prior 26 authenticated Python CMS tests remain independently passing.

```text
OWNER_POWERSHELL_SELFTEST=PASS
OWNER_SELFTEST_KEYS_CREATED=ZERO
OWNER_HELPER_POWERSHELL_SYNTAX=PASS
NEW_OWNER_HELPER_AND_PYTHON_PROBE_TARGETED_TESTS=37_PASS
OWNER_PREPARE_LIVE=NOT_EXECUTED
ACTUAL_CANDIDATE_SEALED_REPORT=NOT_EXECUTED
ACTUAL_OWNER_RECEIVE_OR_VERIFY=NOT_EXECUTED
ACTUAL_AUTHOR_ROUTE_ACCESS_DENIAL=NOT_TESTED
OWNER_ONLY_OS_ISOLATION=NOT_PROVEN
REAL_REVIEWER_AND_CHALLENGER=NOT_ADMITTED
HISTORICAL_SOURCE_DELIVERY=ZERO
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
```

The only next real-world handoff requiring the owner's active participation is `-Action Prepare` in their own ordinary PowerShell (after `-Action SelfTest`), attach **only** the exported public PEM to the same qualified prospective reviewer Temporary Chat with the two invented fixtures and code, and return its **encrypted** CMS file and safe receipt through the approved owner-mediated path. The actual `Receive` and separate `Verify` must then be observed and separately qualified. Owner reporting must exclude private key, private folder path, passphrase, and plaintext canaries.

## 4. Explicit remaining gates

Successful source-free owner readback would add actual session-specific protected delivery/recovery evidence, but it cannot itself qualify reviewer independence, complete real historical-source representation, provider-hidden context, an unrelated challenger, or actual later blind-author access denial. These stay independent A2-R01–R08 decisions. The intended author interface and its complete access surface must be selected and tested directly before any real contaminated-source transfer. Any stronger isolation change must follow a demonstrated material blocker, not another generic replay.

```text
VALIDATION_280=SOURCE_FREE_M1_OWNER_EXECUTION_READY_NOT_YET_RUN
NEXT_OWNER_ACTION=LOCAL_INTERACTIVE_SOURCE_FREE_TEST_RECIPIENT_PREPARE
EXTRA_DEVICE_REQUIRED=NO
REAL_PRIVATE_OWNER_KEY_CREATED=NO
REAL_SOURCE_REVIEW_AUTHORIZED=NO
SCIENTIFIC_CHECKPOINT_898=UNCHANGED
SPECIFICATION_028=UNCHANGED
```
