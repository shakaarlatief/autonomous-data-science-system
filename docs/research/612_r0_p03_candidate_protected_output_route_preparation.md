# Research 612: Route-specific S1 A2 candidate protected-output probe and owner credential boundary

**Date:** 2026-10-28
**Status:** SOURCE_FREE_PROTECTED_OUTPUT_MECHANISM_PREPARED_AND_LOCALLY_TESTED / ACTUAL_CANDIDATE_AND_OWNER_ROUTE_NOT_EXECUTED / CUSTODY_HOLD
**Scope:** Advance beyond inbound source-free byte fidelity and public outbound binary transfer by preparing an exact candidate-session, versioned protected-output mechanism with full private owner readback and strict contamination/role holds; distinguish cryptographic envelope integrity from actual actor, storage and author access isolation.
**Basis:** Research 513/559/576/589/600–611, Validation 269/270/275–278, S1 A2 reviewer/challenger admission gate candidate V0.1 and the source-free owner-mediated route candidate. V0.6 source-status method is prospective and not independently accepted.
**Starting HEAD:** `349230fcb7ad4e169d92d82bba4e09a182bdd78e`. The repaired Runtime Bridge preview.83 managed release and guarded semantic Git publication are verified in Validation 278.

## 1. New evidence objective and explicit non-equivalence

The previous actual candidate Temporary Chat reported a complete 193-byte UTF-8/CRLF and 291-byte PNG intake with all three pre-upload SHA-256 hashes independently matched by the coordinator (Research 610). The same candidate then produced a 1,063-byte binary file recovered from the user-uploaded artifact with exact byte equality (Research 611). This establishes **source-free inbound and outbound byte fidelity**, not protected output or owner-exclusive custody.

Research 603's older encrypted CMS handoff used a **fixed fictional three-record schema** and only owner-reported full readback; its fake-only recipient cannot accept a future variable reviewer ledger. Repeating that literal fixed test would not qualify the **selected, actual prospective candidate** or its output route.

The new objective is distinct: the *same* candidate model session should produce a **fresh, variable-length, report-shaped record** bound to the exact two previously verified invented attachments, with complete received/missing record accounting, randomly generated protected canaries, unqualified challenge/role flags and a new recipient's public certificate. The only downloadable output should be authenticated ciphertext and a bounded public receipt. The owner then recovers the **complete versioned report** in a separately chosen owner context, without pasting plaintext, private canaries or private keys to the exposed coordinator.

This entire test remains **source-free** and is NOT itself the execution of a real historical reviewer route or challenger adjudication.

## 2. Auditable executable and its narrow input contract

Added `experiments/r0_p03_navigation_probe/s1_a2_candidate_protected_output_probe.py` with exactly two user-facing operations, `seal` for the separate candidate and `owner-verify` for the owner.

- `seal` requires the exact original Unicode text fixture (193 bytes, SHA-256 `8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb`) and PNG (291 bytes, SHA-256 `fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f`). Every other byte stream, missing item, altered representation or real source file fails before report generation.
- The report uses the exact marker `ADS_S1_A2_PROTECTED_OUTPUT_SOURCE_FREE_ONLY`, exact schema `ads-s1-a2-source-free-owner-envelope-v1`, strict canonical ASCII JSON serialization and exactly two mandatory records plus zero to three *explicitly missing and held fictional optional records*. There is no generic source text input, old-source classifier or scored answer generator.
- Every report uses a fresh random 192-bit nonce and fresh independent per-record private canaries. The values exist only inside the serialized private report passed to CMS in memory; no plaintext report file is emitted.
- The output is a uniquely named `a2_candidate_protected_source_free_v1.cms` DER CMS AES-256-GCM envelope; exclusive `xb` creation rejects any overwrite. Only a new **public-only** owner-selected PEM certificate is supplied. A bounded receipt contains ciphertext file identity, SHA-256, byte count, and explicitly false real-reviewer/custody flags. The actual private notes/canaries and nonce are absent.
- `owner-verify` checks the supplied complete ciphertext digest before CMS, authenticates the envelope with the owner's **passphrase-protected private key**, validates every canonical report and every missing/required record, and emits a safe aggregate readback result. Failed authentication/provisional OpenSSL stdout never becomes a valid record or leaks into command output; malformed input errors produce fixed public-safe codes.
- The owner-side CLI enforces an **interactive local passphrase prompt** rather than taking private key passphrase as an argv/environment parameter; noninteractive invocation fails closed. The owner must operate it **outside** the exposed coordinator. No real owner certificate/key or secret was created by the coordinator.

The separate candidate-facing instruction is `S1_A2_CANDIDATE_PROTECTED_OUTPUT_ROUTE_PROBE_V01.md`. It requires owner approval of an actual recipient and negative author-route testing before any activation or claim of protected reviewer custody. Historical sources remain excluded, and the candidate must receive **only** the standalone script, brief, exact two invented files, and selected public certificate.

## 3. Security architecture constraint discovered at the correct layer

The existing owner-side fake recipient PowerShell script generated a key in an owner+SYSTEM ACL-protected LocalAppData directory. That controls access from unrelated Windows identities but **does not separate the owner from a Runtime Bridge process running under the same Windows account SID**. Consequently, that storage design alone cannot prove a restricted ledger is unavailable to the project-attached coordinator's full host capabilities or to a different route under that principal. Codexless registered-workspace refusals (Research 608) only prove the *specific tool route* denied cross-root traversal, not complete OS and provider isolation.

The new test instead requires the private key to be **passphrase-encrypted at rest** with a passphrase entered exclusively by the owner in an interactive terminal and never shown to this coordinator, another model, a connected app, a command line or environment. This protects against opportunistic key-file reads without the separately held passphrase. It does **not** prove confidentiality against same-SID process instrumentation, keylogging, compromise during interactive decryption or provider-side memory. If the selected threat model includes any of these, a separate OS identity/device or independently governed storage/recipient must be qualified before real reviewer findings.

**Architecture trigger:** This is a genuine reason to reconsider the physical recipient boundary independently of the old fake CMS implementation. Do not silently preserve the current Windows folder, user, identity or branch arrangement merely because the fictional owner readback passed. Do not force a stronger service without demonstrated necessity either; choose the smallest route whose actual controls and negative witnesses meet the scientific roles.

## 4. Test scope, negative cases and nonpromotion

The new test suite `tests/unit/test_r0_p03_s1_a2_candidate_protected_output_probe.py` covers exact original fixture admission, 2–5 record report completeness, fresh random canaries, invalid/noncanonical/duplicate JSON, forged role or challenge status, altered real-looking source identifiers, missing and invalid record states, and actual OpenSSL RSA recipient AES-256-GCM sealing/decryption/tamper rejection **inside ignored source-free pytest scratch**.

A first 26-test run identified two **test expectation** mistakes: removing an optional record yielded a legitimate shorter report, and the aggregate receipt intentionally reports a safe numeric canary count without revealing values. Those assertions were repaired. A subsequent encrypted-private-key test initially used an OpenSSL `req -aes256` option not supported by the installed Git OpenSSL; testing was corrected to use its normal password-encrypted key generation with a deliberately public test-only password. The corrected suite passes **26/26**, including wrong-passphrase and CMS-authentication failure.

All generated test keys/certificates live under ignored `.venv` scratch, are not owner credentials, and are never published or claimed as the actual owner recipient. The tests do not execute any external Temporary Chat, owner private storage, challenger, future author session or actual historical source content.

## 5. Next actual experiment, not another fictional A1 replay

1. Owner chooses an exact **separately controlled recipient and retention/recovery mechanism**, including meaningful protection against access by the coordinator and a plausible future primary-author route. Key creation and owner passphrase entry take place outside this chat/Runtime Bridge. Only the owner-selected public certificate may go to the candidate.
2. The **same actual candidate session** (if still available) receives just the source-free packet and invokes the sender, producing only CMS binary and safe receipt. The owner retrieves it without exposing its plaintext canaries to this coordinator.
3. The owner independently verifies its complete five-record source-free encrypted report by interactive authenticated readback, checks recovery and authorization boundaries, and returns only screened status markers.
4. A distinct **actual intended future author-facing interface** is probed for access to the restricted output/key, including search, attachment, connector, project root, filename, rendered metadata and public receipt joins. Failures and unknowns are recorded separately. Only then consider whether A2-R05 and A2-R07 can each receive a scoped qualification.
5. A separately qualified challenger and independently accepted source-status method remain prerequisites. No actual historic batch is authorized by a synthetic pass.

```text
RESEARCH_612=SOURCE_FREE_OWNER_PROTECTED_OUTPUT_PACKET_PREPARED
SOURCE_FREE_PROBE_REGRESSION=26_PASS
CANDIDATE_ACTUAL_PROTECTED_ENVELOPE=NOT_EXECUTED
OWNER_APPROVED_PRIVATE_RECIPIENT=NOT_SELECTED
OWNER_REAL_KEY_CREATED_BY_COORDINATOR=NO
OWNER_ACTUAL_PRIVATE_READBACK=NOT_EXECUTED
A2_R05_CONFIDENTIAL_CUSTODY=NOT_QUALIFIED
A2_R07_AUTHOR_ACCESS_DENIAL=NOT_TESTED
REAL_REVIEWER_OR_CHALLENGER=NOT_ADMITTED
REAL_HISTORICAL_SOURCE_DELIVERY=ZERO
AUTHOR_WORLD=WORLD_UNFROZEN
HIDDEN_GOLD=NONE
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
