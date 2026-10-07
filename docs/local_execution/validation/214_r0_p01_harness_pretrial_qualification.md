# Validation 214: R0-P01 harness pretrial qualification

**Date:** 2026-10-07
**Status:** INDEPENDENT CHATGPT PRETRIAL QUALIFICATION PASS / ATTEMPT 001 NOT STARTED
**Scope:** Preserve ChatGPT / chatgpt-37's independent final adversarial implementation review and synthetic pretrial qualification after the bounded Attempt-001 durability repair.
**Authority:** Probe implementation qualification evidence only; no owner-trial evidence or P01 result, physical-target selection, production implementation, migration or authority switch.

Starting HEAD and origin/v1-source-vault-bootstrap-resume were synchronized at fb19c4f9deebf1b667d64f2e4f82c68569ab2daf. Branch: v1-source-vault-bootstrap-resume. Codex materializes the owner-supplied independent ChatGPT review; the implementation remains uncommitted in this documentation task.

| Implementation file under experiments/r0_p01_owner_acceptance_v01/ | Bytes | SHA-256 (exact file bytes) |
|---|---:|---|
| harness.py | 64666 | 0aede5baccaf88e176b3f6c53d69135953405c9f22416e23b017cbd1eb272846 |
| webauthn_server.mjs | 32608 | 6ca17d7da0dbf65938ea7d9f98432ca200ca6233896f3895f10649a9bdc4edd8 |
| score.py | 24078 | 9817febe60db6d68e3dd3887d0dbd2e5573fa398ef2398cd39ceccea7696509c |

The original bounded defect allowed a second Attempt 001 in a fresh process using a new evidence directory after an interruption before SSH key files existed. This was an implementation defect against frozen P01-C16, not an architecture or contract defect. Before any owner execution, Codex repaired only harness.py. The production marker is %LOCALAPPDATA%\ADS-R0-P01\attempt-001.started.json: atomic/create-only, non-secret, flushed/fsynced, never automatically removed or overwritten, with no reset/retry flag. Existing and partial markers fail closed; claim and first raw snapshot precede owner-sensitive setup. Tests use temporary synthetic marker locations only. ChatGPT independently inspected and requalified the repair as ACCEPT_AFTER_BOUNDED_REPAIR.

| Independent check | Result / coverage |
|---|---|
| harness.py --selftest | PASS: four golden vectors; controls 1-13 synthetic A/B; decision consumption; stale-base/roles; historical trust; secret redaction; C construction; embedded WebAuthn; durable claim; fresh-process rejection; partial-marker rejection; production marker guard |
| webauthn_server.mjs --selftest | PASS: golden; synthetic ES256 assertion; 9 statement mutations; 14 structural negatives; counter policy; registration binding; single-use state; expiry; predeclared registration repeat; defect retry prohibition |
| score.py --selftest | PASS: normalization; raw immutability; integrity/provenance; INVALID / REOPEN / AMEND / PASS_WITH_SELECTION; A/B thresholds/ties; large/missing-measurement gates; infrastructure exception; volume; C ineligibility; full public-evidence reverification; synthetic cannot masquerade as owner evidence |
| Repository integrity | PUBLIC_REPOSITORY_INTEGRITY=PASS |

```text
semantic base 76a7391fafd9683566f011be522dd4c3bfbe6bcfb0f1963500d1776b77b4d7a6
envelope      b4a274d82c6bc22b8c6168c2fdd7ee8b0b5dea8f6140907960022eb0fd6dc71c
shown         e55af5a611651ca0efaae4aba2a013df9b9c87cbe8e61f147a612cd94f7e6d1d
statement     66b397b12d23d83b475e15e143272f68be7bd655d8432ff170de6985e87ade46
```

Inventory: 119155 Git-blob bytes / 97 acceptances / 157 effects; distribution 1->62 / 2->17 / 3->11 / 4->7. Source blob: 56ecc1da7677a6be450b3b38beaa9266d6ffb8a8; SHA-256: 2a3be898be6d7ac61d045a41492374d9fedb2ed3bf91734e4e07f0f20053355c.

Independent boundary checks:

```text
SECOND_ATTEMPT_001_START_ALLOWED=false
PRODUCTION_ATTEMPT_001_MARKER_EXISTS=false
PRIMARY_PRIVATE_EXISTS=false
RECOVERY_PRIVATE_EXISTS=false
```

No real owner setup, WebAuthn registration/assertion, recovery signing or Arm C attestation occurred. No owner result was observed. Research 522 / Checkpoint 858 / Message 015 freeze the qualified identities and route to ChatGPT-orchestrated owner execution under the committed reviewed implementation. This record does not begin that execution.

```text
R0_P01_HARNESS_PRETRIAL_QUALIFICATION=PASS
ATTEMPT_001=NOT_STARTED
OWNER_RESULT=NOT_OBSERVED
```
