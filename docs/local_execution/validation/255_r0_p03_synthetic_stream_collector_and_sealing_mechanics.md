# Validation 255: R0-P03 synthetic stream final-output collector and sealing mechanics

**Date:** 2026-10-14
**Status:** SYNTHETIC_ONLY_FINAL_PIPE_PASS / REAL_GOLD_AND_ACTOR_CUSTODY_UNQUALIFIED
**Scope:** Verify a simulated Claude-style final-answer stream can be bounded, validated and piped to an existing encrypted archive without a plaintext packet file; preserve negative cases and explicitly withhold real-reference and secret-storage claims.
**Parent:** Research 566, Research 565, Validation 254, Research 513 `6, owner-approved Research 559 Option A.
**Starting HEAD:** `6294ef031e85911ca67e63bc27748e9c592a2cb6`, branch `v1-source-vault-bootstrap-resume`.
**Authority:** Reproducible synthetic mechanism checks only. No actual Claude invocation, owner password, independent adjudication, complete gold custody, scoring or architecture selection.

## Actual execution

An initial model-free Python/7-Zip `-si` check encrypted a fake final payload directly from subprocess stdin. The archive created successfully, a separate subprocess recovered exact bytes with the synthetic password, and no plaintext member file was present in the test directory.

The new `experiments/r0_p03_navigation_probe/synthetic_output_collector_candidate.py` then simulated a Claude stream-JSONL response with a single final result. It validates exactly nine invented historical slots plus twelve invented primary slots across the four Research 513 category names. The payload is deliberately not a task, answer or source from the actual corpus. It refuses non-fake content before encryption.

The demo `python -B -m experiments.r0_p03_navigation_probe.synthetic_output_collector_candidate` returned a nonsecret receipt with `exact_recovery_after_subprocess=true`, `wrong_password_rejected=true`, `plaintext_file_written_by_collector=false`, `not_for_real_gold=true` and `real_output_custody_qualified=false`. The archive and disposable synthetic password existed only for the scope of its temporary directory; no permanent stored reference was created.

The dedicated tests initially exposed an overly permissive synthetic archive path: pytest's general test directory was under `.venv`, satisfying an insufficient ancestor-only check. The destination validation was tightened to specifically named disposable `.r0p03-` directories, and the test suite subsequently passed **17/17**. A separate oversized-stream test was added without emitting a half-megabyte pytest parameter ID. Passing test outcomes describe the corrected version only.

Unit and real 7-Zip subprocess tests include exact synthetic source digest, duplicate/failed/malformed result rejection, forbidden real-looking packet or password, boundary and overwrite rejection, 7zAES listing, wrong-password member-listing concealment and absence of dummy plaintext or dummy password from printed receipt.

## Security limitation and custody distinction

The collector **does not write an intermediate plaintext packet file**. It still builds the entire **fake packet in Python memory**, passes a test-only password as a 7-Zip child-process CLI argument and returns a receipt into the development agent context. No real secret was used. The ciphertext by itself is not proof against access by all other principals: no distinct arm-author identity, actual reviewer logs, GUI password entry, provider retention, full versioned packet or independent future scorer access was examined.

Standard 7zAES is not an authenticated-encryption protocol. The byte digest is a synthetic integrity check; a real answer packet requires a separately trusted prospective byte commitment and an appropriate security/recovery method. The prototype must remain fake-only; changing it into a real collector requires a new explicit design, complete end-to-end host/custodian evidence and owner-approved custody responsibility.

## No scientific state change

No real reference, historical theme neutralization, twelve new owner-task selection, corpus closure, B0–B4 arm realization or scored evaluation was produced. Research 513's criteria, Research 559's narrow legacy gold amendment, owner approvals and the remaining reviewer independence gates remain unchanged. No new credential, account, security policy, private-repository role, Runtime Bridge implementation, physical architecture selection or migration is authorized.

**Disposition:** Synthetic pipe-to-ciphertext mechanics are reproducibly useful, but real output handling and complete independent gold custody are **NOT_QUALIFIED**. Continue with the smallest owner-designated synthetic end-to-end actor/plaintext/secret/restore/denial preflight, not a real gold run. Checkpoint 898 and current routing are unchanged.
