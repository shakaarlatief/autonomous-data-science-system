# S1 A2: Actual candidate-session protected output and owner readback probe V0.1

**Date:** 2026-10-28
**Status:** SOURCE_FREE_EXECUTABLE_PACKET_PREPARED / OWNER_RECIPIENT_NOT_SELECTED / CANDIDATE_NOT_EXECUTED / REAL_CUSTODY_NOT_ADMITTED
**Authority:** Proposed narrowly scoped test of the *same actual candidate reviewer session* that already passed inbound text/PNG fidelity and outbound binary artifact transfer. This is not a source-status review, a continuation of the old fixed fictional CMS trial, an identity proof, or authorization to use real historical material.

## Purpose and exact new evidence

Research 609–611 has established source-free attachment intake and public outbound binary byte fidelity in a candidate Temporary Chat. The remaining relevant **new property** is whether that **exact candidate** can produce a versioned, variable-length, complete source-free reviewer-shaped report; seal it to an *owner-selected new public certificate* without disclosing generated private canary values or plaintext in chat; and have the owner independently authenticate and recover its complete report using a private key the coordinator never receives. The candidate must not use the old `s1_fake_reviewer_report_handoff.py` hardcoded three-record format.

The standalone sender/reader implementation is:

`s1_a2_candidate_protected_output_probe.py`

It accepts ONLY the two previously verified invented fixture bytes (193-byte UTF-8/CRLF text and 291-byte PNG); it rejects real source file contents, incorrect fixture hashes, unknown fields and false qualification flags. An optional count 0..3 adds explicitly **missing fictional records** with HOLD dispositions; this tests complete delivery accounting across variable report lengths. Every report gets a fresh nonce and fresh per-record private canaries. The plaintext stays in the candidate's process memory; the sender writes only DER CMS AES-256-GCM ciphertext and a safe JSON receipt. The owner reader decrypts into memory, rejects invalid CMS/changed bytes/incorrect records, and prints *only* fixed aggregate verification markers.

## Prerequisites and stop condition

The owner must first select and explicitly approve the **actual private recipient and intended eventual author-facing route**. A new, disposable, owner-controlled certificate/key pair must be generated **outside the exposed coordinator**. The private key must be **passphrase-encrypted at rest**, and its passphrase must be chosen and entered in a separate owner-operated local terminal, never through the Runtime Bridge, a model chat, an argv argument, an environment variable, a shared script or a connector. The private key and decrypted results must never be attached to this chat, placed in public Git, or provided to the candidate. The candidate receives only the public certificate. Key creation is deliberately **not** an action of this public test script; the owner chooses and verifies their own destination and credential policy first. No old A1 fake key may be silently reused.

**Important:** A standard private directory on the same Windows user account as the project-attached Runtime Bridge is **not, by itself, an access-isolation guarantee**. The already registered bridge has multiple workspace authorities, and ordinary Windows owner+SYSTEM ACLs do not separate two processes running as that same owner SID. Passphrase encryption at rest reduces exposure from a readable private-key file but does **not** demonstrate isolation against same-user process observation, interactive-session compromise, terminal history, clipboard disclosure or provider-managed inference context. Any claim of actual coordinator/author exclusion requires inspecting and testing the *selected* recipient and future author routes. For owner-only custody, assess a separate OS principal, device or independently managed recipient when necessary, rather than silently assuming the current PC's folder is private.

Before sending the packet to the candidate, require owner-side choices for key custody, recipient authorization, restricted artifact retention/recovery, and which genuine future primary-author interface will be used for negative access tests. If these are undecided, remain in `OWNER_RECIPIENT_SELECTION_HOLD`. Do not create actual owner credentials through the exposed coordinator as a shortcut.

## Exact candidate session packet

Supply to the SAME prospective reviewer Temporary Chat, after owner approval, only:

1. This instruction file.
2. `s1_a2_candidate_protected_output_probe.py`, verified against the public Git source.
3. `a2_source_free_fidelity_unicode_crlf.txt`.
4. `a2_source_free_fidelity_pattern.png`.
5. A **new** owner-selected *public-only* PEM certificate with no private key.

No real historical files, project history, private keys, other account access, arbitrary links or old gold are allowed. The candidate may use only locally available tools to run the script; if Python/OpenSSL/file access cannot be verified, report `PROTECTED_OUTPUT_CAPABILITY_HOLD`, not a fictional success.

The candidate should use a command with the corresponding actual attachment paths:

```text
python s1_a2_candidate_protected_output_probe.py seal
  --text-fixture a2_source_free_fidelity_unicode_crlf.txt
  --png-fixture a2_source_free_fidelity_pattern.png
  --recipient-public-cert OWNER_NEW_PUBLIC_ONLY.pem
  --output a2_candidate_protected_source_free_v1.cms
  --optional-missing 3
```

This command is illustrative; run as one argv command and adapt only file paths. The sender must verify the two input file hashes, create and validate a five-record private report, encrypt it, write **ciphertext only**, and print a public-safe receipt with `ciphertext_bytes`, `ciphertext_sha256`, and explicit false admission flags. It must not show the plaintext JSON, private canaries, report nonce or decrypted findings in conversation output.

The candidate returns the complete encrypted binary file to the **owner-approved restricted transport path** plus the public-safe receipt. Do not send the plaintext report to the coordinator. If the encrypted binary must temporarily traverse an exposed channel, that channel becomes a documented tested transport surface, NOT a private store; metadata leakage and possible access to the owner key must be separately considered.

## Owner-side authenticated recovery

Only the owner runs the pre-reviewed, Git-pinned `owner-verify` subcommand in their *selected* private environment, supplying the owner-controlled private key, public certificate, saved ciphertext file and the expected ciphertext SHA-256 from the separately received candidate receipt.

```text
python s1_a2_candidate_protected_output_probe.py owner-verify
  --ciphertext a2_candidate_protected_source_free_v1.cms
  --recipient-public-cert OWNER_NEW_PUBLIC_ONLY.pem
  --recipient-private-key OWNER_PRIVATE_KEY_NEVER_SHARED.pem
  --expected-ciphertext-sha256 <candidate-reported-64-digit-hex>
```

These filenames are **placeholders**, not a request to publish the private key path or its value. The `owner-verify` command requires an **interactive terminal**, prompts for the encrypted private key's passphrase locally without echoing it, and rejects noninteractive invocation. The passphrase is never an argv/environment parameter and must not be pasted into any conversation. The command emits only source-free status flags and numeric record counts. The owner must independently verify actual key custody, local stored ciphertext, full readback, replay after restart, missing/partial delivery detection and a separate negative access attempt from the **actual intended future author interface**, while preserving the prior unmodified version for recoverability.

A reply of `owner_full_readback=PASS` can establish bounded owner-operated source-free recovery if legitimately executed. It does **not** establish reviewer identity, provider-level confidentiality, private-key access exclusivity, genuine future author denial or real source schema validation. Do not collapse the A2-R05 positive receipt test with the separate A2-R07 negative author-route test.

## Expected evidence and prohibitions

Candidate reports only the sanitized receipt, its actual tool invocation summary, any limitations and whether the encrypted binary was transported to the approved owner route. Owner reports only nonanswer-bearing verification markers and independently checked key and storage access conditions. Reviewer-private fields, generated canaries, public/private credentials, historic source names and private owner paths must not be pasted to this coordinator.

Stop on missing public certificate, recipient ownership uncertainty, unencrypted owner private key, reuse of any A1 key, noninteractive key handling, unverified key accessibility, absence of actual owner readback, malformed ciphertext, unauthorized recipient, or incomplete source/record accounting. Do not infer successful protected custody from a matching ciphertext hash alone. Do not independently proceed to historical sources or challenger author role admission.

```text
A2_PROBE=ACTUAL_CANDIDATE_SOURCE_FREE_PROTECTED_OUTPUT_ROUTE
A2_SOURCE_FREE_FIXTURE_DELIVERY=PREVIOUSLY_BOUNDED_VERIFIED
A2_CANDIDATE_PROTECTED_OUTPUT=NOT_EXECUTED
A2_OWNER_APPROVED_RECIPIENT=NOT_SELECTED
A2_OWNER_PRIVATE_KEY=NOT_CREATED_BY_COORDINATOR
A2_OWNER_READBACK=NOT_EXECUTED
A2_R05_ACTUAL_REVIEWER_PRIVATE_CUSTODY=NOT_QUALIFIED
A2_R07_ACTUAL_AUTHOR_ACCESS_DENIAL=NOT_TESTED
A2_R01_REVIEWER=NOT_ADMITTED
A2_R06_CHALLENGER=NOT_ADMITTED
REAL_SOURCE_DELIVERY=ZERO
WORLD_FROZEN=NO
GOLD=NONE
SCORING=NOT_STARTED
```
