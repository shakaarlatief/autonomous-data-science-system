# Validation 257: R0-P03 temporary arm-author scope and synthetic CMS envelope verification

**Date:** 2026-10-14
**Status:** OWNER_SCOPE_ACKNOWLEDGED / FAKE_ONLY_AES256_GCM_VERIFIED / REAL_CROSS_PRINCIPAL_DENIAL_NOT_EXECUTED
**Scope:** Verify a disposable public-recipient CMS mechanism, test fail-closed GCM decryption result handling, and preserve the owner's authorization of a temporary sandbox restriction on R0-P03 B0–B4 authors without changing existing development permissions or generating reference data.
**Parent:** Research 568; Research 513 and owner-approved Research 559; Research 564–567; Validation 253–256.
**Starting branch / HEAD:** `v1-source-vault-bootstrap-resume` / `0f9bd74c4b9e328f5aedeb99a6286c53b15db660`.
**Authority:** Synthetic mechanism/owner workflow evidence only; no actual independent reviewer or evaluator, gold, operational key, account, ACL, private store, authorization, score, physical target or migration change.

## Authorized policy boundary

The owner explicitly accepted confining **B0–B4 experimental arm authors** to a *verified* restricted sandbox for this experiment, without restricting normal ADS development. This is an approved prospective experiment-specific rule, not a claim that the present Codex, Claude or other agent hosts have completed independent confinement qualification.

An arm agent with a sandboxed child-process shell but unrestricted inherited chat, browser, GitHub/private connectors, user-account filesystem or prior gold exposure remains **NOT_QUALIFIED**. Future role-specific tool inventories and an actual synthetic owner-canary access-denial result are prerequisites for declaring an authoring host ready. Neither comparison arms nor scoring runs were started.

## Executed fake-only CMS envelope observations

Using the locally installed Git-for-Windows OpenSSL 3.2.3, a model-free Python script created one disposable self-signed RSA 2048 certificate and matching private key under an auto-deleting `.venv` scratch directory. The mock encryptor directory received **only the public certificate** and encrypted CMS bytes. The fake payload entered the encryptor subprocess on standard input, with no intermediate plaintext file.

OpenSSL `cms -encrypt -binary -outform DER -aes-256-gcm` succeeded. Structural output inspection verified `aes-256-gcm`. A different decryption subprocess recovered the exact fake bytes and matched their SHA-256 digest. Changing ciphertext caused decryption failure. There was **no model inference**, real task/reference data, lasting secret, password shared with the model or public/private repository mutation outside this engineering commit.

A second negative probe deliberately corrupted the last byte of the encoded CMS envelope. Decryption returned **exit code 4** yet emitted provisional **stdout bytes** before reporting an error. Therefore `stdout` is never a trusted packet merely because bytes exist. The recovery wrapper added in `experiments/r0_p03_navigation_probe/synthetic_cms_recipient_preflight.py` returns plaintext **only if both** the authenticated CMS command exits successfully **and** the recovered SHA-256 equals the independently provided expected digest. On failure, the provisional bytes are discarded in memory and never written to a plaintext file, printed, or forwarded.

### Added reproducibility and negative tests

Added:
- `experiments/r0_p03_navigation_probe/synthetic_cms_recipient_preflight.py`: disposable test certificate, public-only mock encryptor, AES-256-GCM CMS round trip, tampered envelope rejection, safe decryption result gate and sanitized fake-only receipt.
- `tests/unit/test_r0_p03_synthetic_cms_recipient_preflight.py`: tests GCM failure stdout suppression, digest mismatch rejection, exactly matched successful fake packet and live disposable key/ciphertext trial.

**4/4 new tests PASS.** The synthetic receipt indicates `aes_256_gcm_confirmed=true`, `tampered_ciphertext_rejected=true`, `tampered_provisional_stdout_was_possible=true`, `unsafe_plaintext_returned_to_safe_caller=false`, `mock_encryptor_private_key_file_present=false`, and explicitly `different_os_principals_tested=false` and `real_gold_custody_qualified=false`.

**Caveat:** Both mock directories were controlled by the same Windows test account, and the generated test private key was unencrypted only because it was **ephemeral synthetic data**. None of these demonstrate production private-key isolation, owner-only credential access, recoverable and durably versioned complete gold, clean real reviewer/model transcript handling, actual forced arm-agent sandboxing or independent scoring. The simulation must never be reused with real answers.

## Next test and stopping condition

The smallest next owner-assisted step is a single harmless, owner-created file with random synthetic canary content **outside registered agent workspaces**, confirmed locally present and readable by the owner, followed by actual read attempts through **proposed confined B0–B4 agent tool surfaces**. A rooted-tool denial and an OS ACL denial are different observations and must be reported separately. Testing a nonexistent path is not a meaningful denial. Only an actual closed-world test of relevant model-facing tools, along with owner-private-key and provider transcript exclusion, could qualify the next end-to-end reviewer/custodian handoff.

No attempt to change Windows users, local sandbox settings, Runtime Bridge workspace registration, owner directory ACL, private repository role, password/credential store, R0-P03 protocol, task sampling, heldout, gold or architecture was made. Preserve Checkpoint 898, R0-P01 AMEND/deferred, R0-P02 PASS and original R0-P03 gates.

```text
EXPERIMENT_ARM_AUTHOR_RESTRICTION=OWNER_APPROVED
FAKE_CMS_AES256_GCM_RECOVERY=PASS
FAIL_CLOSED_CORRUPTED_DECRYPT_STDOUT=TESTED
FAKE_ONLY_CMS_UNIT_TESTS=4_PASS
ACTUAL_OWNER_CANARY_DENIAL=NOT_EXERCISED
REAL_REFERENCE_CUSTODY=NOT_QUALIFIED
REAL_B0_B4_ARM_EXECUTION=NOT_STARTED
CHECKPOINT=898_UNCHANGED
```
