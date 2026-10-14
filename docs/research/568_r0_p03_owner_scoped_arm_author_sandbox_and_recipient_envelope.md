# Research 568: R0-P03 owner-approved arm-author sandbox scope and synthetic public-recipient envelope

**Date:** 2026-10-14
**Status:** OWNER_APPROVED_EXPERIMENT_SCOPE / SYNTHETIC_RECIPIENT_ENCRYPTION_PASS / FULL_ACCESS_SEPARATION_NOT_QUALIFIED
**Scope:** Record the owner's narrowly scoped agreement to confine B0–B4 arm authors to a verified sandbox, test a disposable public-recipient encryption/decryption path without exposing a decryption password to the encryptor, and define the real evidence required before any independent gold or arm authoring.
**Parent:** Research 513 §6; owner-approved Research 559 Option A; Research 561-567; Validation 256; MC-0030. Starting published branch HEAD `0f9bd74c4b9e328f5aedeb99a6286c53b15db660`.
**Authority:** The owner has authorized the *principle of temporary R0-P03 arm-author confinement* while retaining unrestricted normal ADS development. This is not evidence that any current host is qualified, a new runtime authorization, a benchmark scoring freeze, a permission/account change, a new gold store, or a general architecture/migration policy.

## 1. Exact scope of owner's decision

The owner accepted: **agents constructing B0–B4 experimental arms must work only through a demonstrably sandboxed, restricted execution and tool/context surface for this particular navigation experiment**. Other ADS development workflows are not changed by this approval. The experiment must not run under ordinary desktop-user Claude Code, Codex or a new external-app connector until that route is explicitly shown to satisfy the same restricted actor-specific controls.

Do not silently change Git branch topology, repository contents, agent selection, CI/CD, the Runtime Bridge trust policy, tools used for unrelated tasks, or the V03/Research 513 science protocol. The restriction applies at the **arm author** / **arm run** stage, where pre-scored gold leakage could bias architecture comparisons. The independent reference annotator, trusted custodian and fresh scored evaluators have their own separate admission rules.

The environment binding must be prospective and evidence-backed, not inferred from the sandbox name or a helpful promise to ignore known gold. The arm model **itself** must have no alternative path to the hidden answers, either through its tool inventory, an inherited prior conversation, earlier exposed agent context, code source, an app connection, shell command, environment variable, owner key, repository/Git history, arbitrary path access or network retrieval. A sandboxed child process attached to an exposed model with broader tools does not establish a sandboxed **arm author**.

## 2. Disjoint responsibilities and read/write matrix

| Responsibility | Permitted source/outputs | Forbidden access or role overlap |
|---|---|---|
| Method designer and test engineering (current ChatGPT/Codex/earlier Claude) | Public protocol, approved source manifest, fake-only synthetic probes, sanitized receipts | Fresh independent reference/gold author or scored evaluator; private hidden answer contents |
| Fresh historical neutralizer and reference adjudicator | Exactly closed pinned historical source capsule and neutral nine thematic hints, with independently declared known exposure and permitted limited tools | Existing W5 labels/gold, arm designs and outputs, alternative Git paths, inherited prior exposed context |
| Independently chosen new primary-task author or prospectively frozen mechanical owner-event selector | Source/world/authority evidence needed to produce twelve answerable four-category needs and closures | Arm-conditioned task selection, existing B1 gold, unreviewed source closure, post-score edits |
| Custodian | Entire complete neutral gold packet, controlled plaintext during authorized sealing/recovery, separately protected key, exact versions/receipts | Arm authors; code/benchmark metadata that hints at reference answers; exposing stdout/transcripts |
| B0–B4 arm authors and runs | Equal public-source build world; exactly agreed model, context, tools, budget, metadata and comparator rules | Private gold, private key, hidden heldout labels, review transcript, unbounded host/other connectors, scoring results until frozen |
| At least two fresh scored evaluators | Equal arm outputs and exactly authorized scoring references at adjudication time | Prior arm authorship, other-arm outputs before independent result, unfrozen gold changes |

The arm author sandbox must deny **each** relevant secret channel, not merely enforce a read-only filesystem. Different user accounts help only if the rest of the agent's tools/contexts cannot bypass the restriction. A public ciphertext may be readable by authors only if its decryption key and raw plaintext cannot be read; this must be proven, not assumed.

## 3. Existing evidence and conditional technical route

Research 564 owner-terminal Claude read/Glob/Grep synthetic test is positive for exercised file paths, not global model isolation. Research 566 established a fabricated nine-plus-twelve final-result pipe to temporary 7-Zip encryption without a plaintext staging file, but its dummy password was passed in process arguments and is **explicitly not valid for actual secret use**. Research 567 found the existing Codex command executed under a distinct `CodexSandboxOffline` Windows identity, and existing Git-for-Windows OpenSSL 3.2.3 supports public-recipient CMS operations. The ordinary desktop Claude Code effective authoring principal remains different or unknown. The Runtime Bridge has other registered source-access roots, which is not the same as an independent gold vault.

### New, non-inference AES-256-GCM CMS synthetic trial

A bounded in-memory fake answer and a fresh **ephemeral self-signed RSA certificate/private key** were created under an auto-deleting `.venv` temporary directory. The fake packet was sent through OpenSSL CMS `-encrypt -aes-256-gcm -binary -outform DER` using only the copied recipient **public certificate**. The mocked encryptor directory contained that public certificate and ciphertext, never the private key. OpenSSL inspection confirmed the `aes-256-gcm` algorithm, and a distinct decrypt invocation recovered the original fake bytes using the matching key. A one-byte ciphertext mutation caused the OpenSSL CMS decrypt operation to fail. No fake plaintext file was staged in the encryptor directory.

The reported checks were:
- `certificate_created=true`; `encryption_succeeded=true`; `aes256gcm_reported=true`.
- `round_trip_pass=true`; `tamper_rejected=true`; `ciphertext_not_plaintext=true`.
- `only_public_cert_copied_to_mock_agent=true`; `unencrypted_packet_file_created=false`.
- `different_os_principals_tested=false`; `independent_gold_custody_qualified=false`.

A more specific tampered-last-byte negative test revealed that OpenSSL CMS **may emit provisional plaintext on stdout despite returning a decryption error**. Consequently, a future scorer must buffer decrypted content without exposing it and release it only after both successful authentication and exact frozen-packet digest verification. A guarded, **synthetic-only** recovery wrapper demonstrates that fail-closed property; it does not guarantee that the external OpenSSL process never held plaintext temporarily. The reproducible `synthetic_cms_recipient_preflight.py` uses ephemeral RSA credentials, public-only mock encryptor files, `aes-256-gcm`, deliberately damaged ciphertext, and a sanitized receipt. The paired `test_r0_p03_synthetic_cms_recipient_preflight.py` covers error-output discard, wrong-digest refusal, positive digest-gated recovery and the real disposable OpenSSL subprocess trial. **4/4 focused tests passed.** Validation 257 records the exact results and limitations.

**Important distinction:** Both mocked roles and their directories were controlled by one parent test running under the same Windows sandbox identity. Directory layout is not access control. The private key had no independent OS or hardware custody and could be read by that test principal. This qualifies only a *cryptographic envelope primitive* and demonstrates that the encryptor does not **need** the decryption key for the intended algorithm, not that an agent cannot retrieve the key in production. These disposable files were removed by the temporary-directory context. No real owner key, certificate, passphrase, model inference or benchmark reference was used.

## 4. Qualification gates before real independent work

The smallest **owner-assisted synthetic cross-principal access experiment** should proceed in two evidence stages.

**A. Actor/host and negative access.** The owner creates a disposable, harmless, uniquely named fake-canary file in an owner-designated local folder *not registered as a model workspace*. Record only owner-readable existence plus exact file identity and a nonsecret digest. Then use the **actual proposed arm-author agent tool route** to attempt a real read of that file (also check relevant Git, shell, web, app and other workspace access as applicable). Distinguish:
1. Tool-root refusal (the specific surface cannot read, without proving an OS ACL denial).
2. OS ACL refusal under the actual sandbox Windows principal.
3. Missing file (NOT_EXERCISED and **not** a denial).
4. Successful read (the proposed route **fails** for that target).
An owner-supplied positive existence check is essential to prevent incorrectly classifying a missing canary as security. Test normal desktop-user Claude Code separately **if** the intended arm author route permits it. Under the accepted policy, a route not tested/qualified is not an arm-author route.

**B. Protected output to recovery.** Only after the exact author/custodian identities and root separation are designated, use another **fake** final-answer packet and a deliberately temporary owner-controlled public/private recipient key pair. A trusted collector captures model output without uncontrolled stdout persistence and seals using only public key; a separate custodian verifies recoverability, binding to source/packet digest, ciphertext integrity and no shared private key access. Test arm-author denial against original output traces, complete packet, keys, storage paths and connected app surfaces. OpenSSL success inside one parent process is insufficient. A public digest alone does not preserve the full gold. Cleartext must not land in public Git or an arm-visible temp directory.

If an owner-only plaintext folder still shares privileges with the planned Claude author, either constrain that author to the verified sandbox or choose a truly separate owner key/account/custodian. Do not force a new account, private Git role, ACL or secret when a smaller qualified isolation route is available.

## 5. Result and explicit stopping point

The owner has approved the **experimental role restriction**, not a production trust change. The alternative public-recipient envelope now has a positive fake-only AES-GCM mechanism result; however the real cross-principal canary access test and separate owner-private-key/complete-gold retention are **not performed**. These need the owner's single, concrete setup action. No hidden answers exist yet.

Research 513's common substrate, B0–B4 definitions, twelve new primary and nine historical tasks, >=10/12 and >=8/9 gates, zero false-authority, task/corpus/freeze fairness and two fresh scorers remain unchanged. Research 559's Option A continues to require an independently adjudicated arm-neutral legacy packet. Checkpoint 898 and `p-three-reviewer-execution-authority-qualification` remain unchanged. This step does not authorize actual gold, task selection, scored runs, migration or physical architecture selection.

```text
OWNER_R0_P03_ARM_SANDBOX_SCOPE=APPROVED
SPECIFIC_ARM_AUTHOR_HOST=NOT_QUALIFIED
SYNTHETIC_CMS_AES_256_GCM=MECHANICS_PASS
ACTUAL_CROSS_PRINCIPAL_CANARY_DENIAL=NOT_TESTED
OWNER_HELD_PRIVATE_KEY_AND_REAL_OUTPUT_CUSTODY=NOT_QUALIFIED
R0_P03_REFERENCE_PACKET=NONE
R0_P03_SCORES=NONE
CHECKPOINT=898_UNCHANGED
```
