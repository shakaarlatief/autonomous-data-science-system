# Research 587: R0-P03 Temporary Chat to owner public-recipient trial preparation

**Date:** 2026-10-18
**Status:** OWNER_FAKE_PUBLIC_RECIPIENT_WORKFLOW_PREPARED / OWNER_KEY_CREATION_UNEXECUTED / TEMPORARY_CHAT_HANDOFF_UNEXECUTED
**Scope:** Prepare a real owner-desktop-to-Temporary-Chat-to-owner-desktop transfer trial of an *entirely fictional* 9+12-case CMS packet, reusing Research 586 and preserving all private owner keys outside the repository, ChatGPT coordinator, external temporary author and future scored arms.
**Basis:** Research 513/559 and accepted Level B 576, Research 565/566/568/570, Research 582–586, and the owner request "Perfect. Proceed" following the recommended actual fake Temporary Chat to owner controlled recipient handoff.
**Provenance:** ChatGPT/chatgpt-39, exposed engineering coordinator and code/test author. No owner identity, production secret, independent gold writer or fresh scored evaluator has yet acted.
**Authority:** Synthetic-only experimental mechanics and future operator instructions. Not owner/private key custody proven, a scored R0-P03 fixture, source-answer closure, arm independence qualification, or permission to treat unreviewed Temporary Chat output as gold.

## 1. What is prepared

Added three tracked engineering artifacts and one new research record:

- scripts/r0_p03_fake_public_recipient.ps1
- experiments/r0_p03_navigation_probe/temporary_author_fake_cms_sender.py
- tests/unit/test_r0_p03_fake_public_recipient.py
- tests/unit/test_r0_p03_temporary_author_fake_cms_sender.py

The Windows PowerShell 5.1 recipient script exposes Prepare, Receive, Verify and SelfTest. It deliberately rejects SYSTEM, CodexSandboxOffline/Online and elevated owner sessions. A normal non-elevated **owner** PowerShell must execute Prepare, which allocates exactly one new randomly named direct child of owner LocalAppData and atomically creates the directory with inheritance-disabled DACL that allows only current owner SID and SYSTEM. This is a **new distinct mock recipient**; it does not mutate the Research 584/585 owner fake-packet directory or reuse that previous 21-case data.

Only a **disposable RSA-2048 fake private key and self-signed certificate** are generated under that new protected directory. The certificate is exported to the user's default Downloads as an expressly shareable public-only PEM file. The private key is unencrypted-at-rest for this fictional demonstration but is placed solely in the owner-restricted folder. It is NOT an acceptable production reference-custody key format/rotation/retention policy. The script returns public cert filename/digest and owner folder for use only in owner PowerShell; do not commit or attach the private key, owner path or real gold to this chat.

The entirely standalone Temporary Chat sender script contains no private material or scored R0-P03 content. It accepts only the public PEM certificate, constructs in-memory the exact fixed synthetic 9+12 JSON cases inherited from the Research 566 strict schema, encrypts with existing OpenSSL CMS AES-256-GCM and writes only the file R0_P03_FAKE_AUTHOR_PACKET.cms. It refuses nonexistent OpenSSL, private-key-bearing PEM, alternate encryption modes and file overwrite. Its receipt reveals only fake case counts, ciphertext digest/length and express nonqualification of real reference custody. A Temporary Chat can upload/run this publicly shareable script and the public PEM; the author must not be given this coordination conversation, owner private key or private folder.

Once the owner downloads the ciphertext into Downloads using the exact fixed filename, the owner invokes Receive with their own protected recipient directory and local ciphertext path. The script restricts input to one specifically named non-reparse Downloads file with bounded size, authenticates/decrypts via the owner's private key directly into process memory, and verifies the **entire** fictional packet: exact JSON top-level fields, marker, 9 case IDs and fixed fake claims, 12 case IDs, four groups of three, exact source labels, and no extra fields. Only validated ciphertext and a nonsecret digest/version receipt are stored in the owner-protected folder. No decrypted packet file is created or printed. The operation calls Verify in a separate fresh owner PowerShell process, authenticating and checking the retained CMS bytes and full fictional answer contents again. Any failure must be preserved and diagnosed, not labeled PASS or automatically retried, because failed Receive could have left partial ciphertext/receipt files.

The mock sender's own Temporary Chat file access and actual available OpenSSL must be observed, not assumed. The owner remains the only holder of the fake private key. Cryptographic public certificate attachment and ciphertext transmission do not themselves qualify provider output-log secrecy; the Temporary Chat will necessarily see the *fictional* input before encryption. Real author answers must not be handled by this fake-only procedure.

## 2. Owner setup and trial procedure

Preparation-only from owner ordinary (non-elevated) Windows PowerShell:

    & "C:\Projects_Data\autonomous-data-science-system\scripts\r0_p03_fake_public_recipient.ps1" -Action Prepare

If execution policy blocks the file, use a single separate process with process-scoped policy bypass only after reporting the error, not a permanent settings change. The output should include FAKE_PUBLIC_CERT_PREPARED=PASS, FAKE_OWNER_PRIVATE_FOLDER, FAKE_PUBLIC_CERT_PATH, FAKE_PUBLIC_CERT_SHA256 and NO_REAL_GOLD_OR_PRODUCTION_KEYS=TRUE. Do not repeat Prepare after an uncertain result; unique partial owner folders could exist.

The next ChatGPT instruction will ask the owner to open an entirely new Temporary Chat, attach only (1) the public PEM under Downloads and (2) temporary_author_fake_cms_sender.py, and request a generated encrypted .cms attachment. Use no private key, ADS source ZIP, other experiment reference, plugin/GitHub connection or previous model response. The Temporary Chat may fail because of actual tool limitations; if OpenSSL/Python is unavailable, report unqualified rather than send plaintext/replace algorithms. The resulting file must be downloaded to the named Downloads path only for owner Receive.

Only after ciphertext exists, run in owner PowerShell:

    & "C:\Projects_Data\autonomous-data-science-system\scripts\r0_p03_fake_public_recipient.ps1" -Action Receive -OwnerDirectory <the-exact-folder-from-Prepare> -Ciphertext "$env:USERPROFILE\Downloads\R0_P03_FAKE_AUTHOR_PACKET.cms"

This is an operator format, not an instruction to create or import real references now. Owner should share only printed outcome markers and nonsecret digest, not private key, certificate private material, decrypted packet, or complete owner folder path in public source records.

## 3. Tested and deliberately untested boundaries

Already qualified by previous Research 586: correct fake 21-case stream extraction, synthetic CMS AES-256-GCM, separate-process exact authenticated readback, tampered ciphertext rejection and wrong digest rejection. The new independent sender now has a direct unit cross-check against the exact old synthetic packet bytes and an actual OpenSSL certificate/envelope/decrypt test. The Windows recipient script is parser-verified and SelfTest verifies fictional schema construction without creating protected owner files. Automated tests never invoke Prepare/Receive/Verify under a Codex agent identity.

Not yet demonstrated: actual owner keypair creation, public cert exported/downloaded, real Temporary Chat with working Python/OpenSSL, CMS attachment transfer through chat UI, owner Receive and Verify, owner directory ACL/actual Windows principal, transcript/storage/log confinement for real model outputs, or owner-restricted access exclusion against actual future arm-author tools. Any full Level B real reference custody certification remains on HOLD even after positive fake-only transfer; record the actual account/tool route and the owner-only key absence from author context.

No fresh primary scored author, no twelve task selection, no new nine legacy neutral reference adjudications, no owner private companion repurpose, no actual scored B0–B4 or heldout, no Docker/VM/security redesign and no checkpoint/routing change.

## 4. Stop after one transfer

Once one genuine Temporary Chat sends a fully fabricated CMS file and owner Receive independently recovers it, **stop**. Do not run more fake handoff variants absent a concrete failure. Use the outcome to make the next scientific source/role admission decision, rather than indefinitely tuning isolation mechanics. Report any failed or blocked real route honestly and retain only a bounded nonsecret evidence receipt in public ADS.

**Disposition:** TEMPORARY_CHAT_FAKE_HANDOFF=PREPARED_NOT_RUN; OWNER_FAKE_KEY=NOT_CREATED; REAL_GOLD=NONE; SCORED_TASKS=NONE; R0_P03_SCORE=NOT_RUN; CHECKPOINT=898_UNCHANGED.
