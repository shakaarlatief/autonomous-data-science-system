# Research 613: Actual owner CMS decryption witness and bounded S1 A2 verifier failure diagnosis

**Date:** 2026-10-29
**Status:** OWNER_REPORTED_DIRECT_CMS_DECRYPT_PASS / COMPLETE_PYTHON_REPORT_VALIDATION_HOLD / SOURCE_FREE_DIAGNOSTIC_PREPARED
**Scope:** Reconcile the actual prospective S1 A2 candidate source-free CMS handoff and owner-reported decryption with the still-failing strict Python readback, without accessing or revealing any owner credential, decrypted report, real historical source, or protected owner storage.
**Basis:** Research 574, 600–612, Validation 279–280, S1 A2 actor admission gate candidate, Checkpoint 898 and Specification 028 unchanged.

## 1. What actually occurred and what this establishes

The separately operated candidate reported processing the precise two synthetic attachments and producing a five-record source-free canonical report (two present, three explicitly missing), encrypted as OpenSSL DER CMS AES-256-GCM to the freshly created owner-public certificate. The candidate relayed public-safe ciphertext SHA-256 `a99c16edc049fb87f630803ee026752ff9d06625ef35f88386e92f36b70512fd`, length **2,527 bytes**, and a successful local binary readback. The owner uploaded the actual ciphertext to the coordinator conversation. The coordinator independently checked those 2,527 bytes and their exact SHA-256 from the uploaded attachment. The private report and canaries were **not** supplied or decrypted here.

The owner then reported these authentic owner-side outcomes in their own PowerShell process:

1. First `Receive` passed its source file digest and stored ciphertext plus minimal receipt before invoking the strict Python `owner-verify` CLI. Python printed `SOURCE_FREE_A2_PROBE_HOLD`, and the PowerShell wrapper printed `S1_A2_OWNER_HOLD=OWNER_REPORT_READBACK_FAILED`. **No complete validated report was attested.**
2. A second `Receive` printed `S1_A2_OWNER_HOLD=RECEIVED_CIPHERTEXT_VERSION_ALREADY_PRESENT`, which is consistent with the first attempt's exclusive saved-copy/receipt creation, not an overwrite or loss of data.
3. Owner-side separate `Verify` reached its private-key passphrase prompt but again yielded the generic Python hold.
4. Owner-side direct `openssl pkey -in <owner-held key> -noout` printed `OWNER_KEY_UNLOCK=PASS`.
5. Owner-side direct `openssl cms -decrypt -binary -inform DER -in <saved ciphertext> -recip <saved public certificate> -inkey <encrypted owner key> -out NUL` printed `OWNER_CMS_DECRYPT=PASS`. This establishes the existing encrypted report is decryptable with the owner's local key and a passphrase successfully provided to **that OpenSSL command**. This direct command deliberately discarded plaintext; it did not check the strict JSON report schema or validate all five synthetic records.

These are **owner-relayed local console results**, not coordinator access to owner keys, plaintext, or owner OS processes. The public coordinator has not accessed that directory and must not attempt to do so. No key/passphrase was transferred to this conversation.

## 2. Why the Python failure is now bounded but not yet attributed

The direct OpenSSL decrypt succeeds; therefore another certificate, new recipient, replay of the candidate output, VM, OS-account redesign, or synthetic transfer is **not justified** merely by this failure. The distinct Python CLI still does more work: obtains passphrase via `getpass`, encodes UTF-8 bytes, enforces an additional **8–256-byte** passphrase length constraint, invokes OpenSSL CMS decryption with `-passin stdin`, then validates the full decrypted canonical source-free JSON manifest/record schema. Any of those stages may fail. In particular, the Python minimum is stricter than OpenSSL's normal passphrase acceptance; this is a plausible but **not observed** cause. Other possibilities include stdin/encoding differences and report-validation defects.

Previously the CLI collapsed all expected errors into `SOURCE_FREE_A2_PROBE_HOLD`, giving no safe failure attribution. Research 613 introduces **only a diagnostic stage code for the owner-verify branch**, populated from a strict static allowlist of fictional-only `ProbeHold` identifiers; arbitrary exception text and subprocess stderr remain suppressed. It does not bypass CMS authentication, schema checks, private-output protection or source-free restrictions.

Next owner-side action after publishing is one `-Action Verify` with the **existing recipient**. Read the printed `SOURCE_FREE_A2_OWNER_HOLD_CODE` safely without disclosing owner key, password, private paths or decrypted content. The code will indicate which repair or evidence check is warranted. An unclassified hold remains HOLD, not an excuse to relax verification or leak traceback.

## 3. Unintended `NUL` output hazard identified before publication

An independent subsequent `git status --porcelain=v1 --untracked-files=all` unexpectedly showed `?? NUL` in the public repository root after the owner had run the direct OpenSSL `cms -decrypt ... -out NUL` command suggested by the coordinator. On this Windows/OpenSSL route, assuming that bare `NUL` discards output was **not justified**. The untracked file may contain the decrypted **synthetic-only** report and private fictional canaries. This represents a possible local plaintext staging/exposure defect even though `OWNER_CMS_DECRYPT=PASS`. The coordinator **did not read or open** the unexpected file and did not stage or publish it.

The owner was immediately directed to delete that **one exact unintended path** locally using a Windows extended-length file path, without displaying the file or touching the distinct owner private key, saved ciphertext, or receipt. Actual deletion has **not yet been confirmed** in this validation. Until absence is independently established through path/name metadata alone, do not run another reviewer route, stage anything from the public working tree, or claim protected-output confidentiality. The correct future local diagnostic uses the existing `Verify` reader, which buffers output privately and strictly controls whether authenticated report data is released. Do **not** use a bare `-out NUL` for a future decrypt-and-discard operation.

This unexpected file is an architecture/evidence trigger: even source-free tests can disclose restricted output through intermediate files, terminal/process behavior or path interpretation. Track the operational failure and prevention; do not infer that a successful cryptographic decryption automatically proves confidentiality or that a source-free trial establishes real reviewer custody.

## 4. Scientific nonpromotions and decisions

```text
SOURCE_FREE_CANDIDATE_CIPHERTEXT_TRANSPORT=VERIFIED_2527_BYTES
SOURCE_FREE_OWNER_OPENSSL_PRIVATE_KEY_UNLOCK=OWNER_REPORTED_PASS
SOURCE_FREE_OWNER_OPENSSL_DIRECT_CMS_DECRYPT=OWNER_REPORTED_PASS
SOURCE_FREE_OWNER_COMPLETE_CANONICAL_REPORT_READBACK=NOT_YET_PASS
PYTHON_OWNER_VERIFY_FAILURE=STAGE_UNATTRIBUTED_BEFORE_DIAGNOSTIC
PRIVATE_KEY_OR_OWNER_PLAINTEXT_EXPOSED_TO_COORDINATOR=NO
NEW_CERTIFICATE_OR_REKEY_REQUIRED=NO
S1_A2_R05_REAL_CONFIDENTIAL_CUSTODY=NOT_QUALIFIED
S1_A2_R07_ACTUAL_AUTHOR_ACCESS_DENIAL=NOT_TESTED
ACTUAL_REVIEWER_OR_CHALLENGER_ADMITTED=NO
REAL_HISTORICAL_SOURCE_DELIVERY=ZERO
S3_AUTHOR_WORLD=UNFROZEN
GOLD_OR_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
