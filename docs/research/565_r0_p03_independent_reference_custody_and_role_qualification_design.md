# Research 565: R0-P03 independent reference custody and role qualification design

**Date:** 2026-10-14
**Status:** CANDIDATE CONTROL DESIGN / NO CUSTODIAN OR FRESH REFERENCE AUTHOR QUALIFIED / NO GOLD OR SCORE
**Scope:** Reconcile the R0-P03 independent-annotator, output-custody and arm-author exclusion requirements, compare candidate restricted retention routes, and specify prospective synthetic qualification gates without producing real references or changing authority.
**Basis:** Published repository HEAD `841c950b3cdc589f92f3ba23376bd3c71eda731f`, Research 513 §6, Research 559 owner-approved Option A, Research 561–564, Validation 253, and owner-terminal synthetic enforcement observations.
**Authority:** Prospective engineering/experimental-method analysis only. This document does not authorize a new private repository role, production secret, fixture freeze, independent annotation, arm implementation, scoring, physical target, or migration. Checkpoint 898 and the current R0-P03 routing boundary remain unchanged.

## 1. Decision now required

The immediate question is not whether restricted Claude can read the prepared historical capsule: the owner-terminal synthetic run produced strong, **owner-relayed** positive evidence for the tested built-in file-tool restrictions. The remaining decision is how a genuinely unexposed reference author receives a closed, unbiased source world and delivers a **complete, immutable, recoverable scoring packet** that subsequent B0–B4 arm authors cannot inspect, including through model output, logs, transcripts, caches, temporary directories or alternate tool access.

Preserve the scientific distinction among: (a) neutralizing nine B1-derived historical topic hints without reusing B1-authored gold; (b) selecting twelve new whole-system tasks through a genuinely independent author **or** a prospectively frozen mechanical owner-event method; (c) obtaining source-bound answer rubrics; (d) adjudicating/evaluating scored arm outputs with at least two fresh evaluators for judgment cases. A single successful host preflight does not conflate these roles.

The original Research 513 §6 definitions, 3/3/3/3 category balance, historical nine cases and >=8/9 gate, primary twelve and >=10/12 gate, zero false-authority tolerance, exact source/revision fidelity, full B0–B4 definitions, common substrate, equal resources, controlled 60/20 intended corpus, scorer and prospective freeze rules remain in force. Research 559 changes only the prospective legacy answer basis by accepted Option A. It is not a general waiver of independence or an authorization to invent tasks.

## 2. Threat and evidence model

The relevant experimental threat is **answer contamination**, whether accidental or opportunistic. Prevent an arm author or an arm agent from reading, inferring from task-specific metadata, receiving in its chat context, or recovering via a generic tool the pre-scored relevant-source/authority labels and complete answer rubrics. Model results that simply claim they were restricted are not evidence of actual permission enforcement. Identity or network labels alone do not establish real access exclusion.

Distinct exposure surfaces must be considered:

| Surface | Failure mode | Minimum qualification |
|---|---|---|
| Reviewer input | Old W5 answers, scenario memberships, other-arm outputs, live repository/Git history, instruction injection | Pinned 65-source historical capsule for legacy; independently frozen eligible source world for primary tasks; exact tool inventory and negative path tests |
| Fresh-model context | Resumed chat, local/global instruction files, managed policy, built-in plugins, cached context, unexpected tool channels | New unresumed session, declared known exposure, observed effective tool inventory, negative synthetic inherited-context tests, explicit residual uncertainty |
| Host execution | Parent/sibling/Git access, junction or symlink, shell, web, connector/MCP, unapproved external paths | Correlated host allow/deny evidence under the actual intended invocation and principal |
| Inference output | Assistant final answer, stream-JSONL, debug/profile logs, shell stdout, error messages | No complete reference text returned to exposed ADS chats, accessible public files or arm-agent logs; verify actual capture destinations |
| Complete answer packet | Missing bytes, editable version, altered answer key, only a public digest, unverified restore | Versioned complete packet, precise byte commitment, atomic retention and independent readback/recovery |
| Scorer and arm author | Same principal/tools can read private packet, encryption key, or authoring gold metadata | Deny checks using **the actual proposed author/scorer principals and tool surfaces**, not nominal folder names |
| Publication | Public plaintext answers before build/arm freeze, post-score changes, ambiguous hashes | Public digest and permitted provenance only before arm construction; controlled scorer disclosure after freeze |

Do not require provability of a model's never having encountered a public historical topic during pretraining; instead require operational independence from **known** project-specific answer sets, earlier conversations, source worlds and compared arms, and disclose unavoidable uncertainties. Conversely, a new CLI session alone cannot be asserted to satisfy operational independence when inherited instructions, plugins and account-wide context are not fully qualified.

## 3. Actual evidence carried forward

The original Codex-launched Claude attempt ended in `ECONNREFUSED`, with zero model tools used. It remains a separate, historically valid failed attempt.

The owner subsequently ran a new restricted synthetic session from ordinary Windows PowerShell. Its reported 41 events, 14 matched tool uses/results, two verified permitted synthetic reads, eight denied forbidden Reads including Git and junction, two denied neighboring Glob/Grep operations, and no reported forbidden canary leakage provide **positive evidence for exactly those exercised paths**. Allowed Glob/Grep results lacked explicit `is_error` and were not content-qualified. Both known built-in plugins (`agents-md`, `telemetry`) were advertised. No `CLAUDE.md` or `AGENTS.md` marker appeared in returned assistant text; absence of such text is not a general inherited-context proof. The temporary synthetic output marker appeared, not a private output-custody proof. A 26-test assessor suite and six repository-integrity checks independently passed.

The owner's synthetic Temp raw trace could not be independently opened by the existing workspace-restricted Runtime Bridge; the owner-relayed assessment is therefore accurately identified as **derived owner-terminal evidence**, not a separately attested full-transcript review. The earlier public sanitized receipt records a different run. The bridge denial was not bypassed.

The active Python environment does **not** currently have `cryptography` or `PyNaCl`, and `age`, `gpg`, `7z` and `openssl` were not found on its searched PATH. These are tool-discovery observations, not a claim that strong authenticated encryption is unavailable on the owner machine. Do **not** invent a home-grown cipher, substitute a hash for secrecy, or silently add a dependency.

## 4. Candidate custody arrangements

### C1. Owner-controlled, access-restricted, versioned output location

An independently controlled owner-designated storage principal receives the completed packet directly from the isolated reviewer or from a trusted relay. Store exact complete packet bytes and version manifest, validate retention/readback, and publish only a digest plus source-world and reviewer-provenance commitments. Keep all raw reviewer output, spool files and transcripts under the same effective access policy or demonstrate that no independent arm author can retrieve them.

**Advantages:** Simple conceptual custody, no bespoke encryption code or always-on service; can reuse a pre-existing owner-controlled versioned store *if* its purpose and access exclusions are explicitly authorized. **Failure risks:** Different folder, private repository flag or another account name is not enough. Same Windows-account bridge/Codex/GitHub plugin access and inherited credentials may still read the packet. The existing ADS private companion is contractually knowledge-preservation only and **must not** be silently repurposed. A future separate private repo/storage responsibility is a distinct owner decision.

### C2. Standard authenticated-encryption sealed packet, owner-held key

Capture complete reference bytes only inside a genuinely bounded authoring process, seal them using a **mature, qualified authenticated encryption implementation** with a high-entropy key unavailable to arm-author principals, durably version the ciphertext and full nonsecret integrity/algorithm manifest, and publish the hash commitment. Verify recovery by a separate authorized scorer/custodian before arm authoring. Public versioning of ciphertext can simplify immutable retention but public ciphertext **does not** prove key isolation.

**Advantages:** Confidentiality can remain meaningful even if arm authors can read the ciphertext. **Failure risks:** Key stored in the same owner account or passed through a model-visible terminal, transcript or script defeats isolation; cleartext intermediate files/stdout and backups still leak; key loss destroys recoverability. A Windows user-scoped protection mechanism **alone** does not isolate other processes using the same user identity. Ciphertext size and publication metadata are not secret. Do not select a tool or key-management workflow until availability, an owner-held recovery arrangement and real negative principal-access tests have been demonstrated. No key, encryption operation or protected packet was created in this stage.

### C3. Dedicated segregated reviewer/custodian process or account

A fresh model works in a separate OS identity/container or a purpose-exclusive model tool surface and writes into C1 or C2 through an authenticated limited output channel. This may be needed if normal same-account CLI stdout, profile logs or generic tooling are accessible to future arm authors.

**Advantages:** Potentially strongest context/host/custody segregation. **Costs:** Provisioning, model authentication, network/OS setup and operational maintenance. The previous Docker/WSL probes were unavailable **to that sandbox**; this does not imply global impossibility. Do not build a permanent service or rewrite the generic Runtime Bridge solely to compensate for an untested account boundary.

### Non-solutions

A publicly committed digest with **no retained complete packet**, Git branch secrecy, an ordinary temporary directory under the same user, a public plaintext gold file, an unqualified private-repository path, `--no-session-persistence` by itself, a shared-key DPAPI assumption, a verbal promise not to read answers, and merely starting a new chat do not satisfy the protocol.

## 5. Proportionate preferred qualification sequence

**Conditional default:** Qualify C1 with a truly separated custodian principal and exact access-denial checks first **if an authorized pre-existing storage route and separate identity are already available**. This requires the least extra implementation. Otherwise evaluate C2 through an established authenticated-encryption tool **and** a demonstrably owner-isolated key, before considering C3. The strongest practical design may combine C2 with a small bounded C3 handoff. This is a test order, **not an unconditional technology selection**. No crypto/deployment decision is justified by the current evidence.

1. **Identify execution principals and rights, without mutations.** Record what the existing Codex/Desktop, ChatGPT/connector, normal Claude CLI and owner-only custodian can actually read. A separate process under the same OS account must not be reported as a separate authorization principal. Existing private companion capabilities do not confer experimental authority.
2. **Pin a synthetic full-packet schema.** Choose deterministic canonical UTF-8 serialization, exact source-world identities, nine legacy case aliases, twelve primary category slots, provenance/independence/exposure declaration, source path@blob citations, authority/relevance/negative controls, ambiguity and adjudication flags, version ID and whole-packet SHA-256. This is a *schema sample*, not real tasks or answers.
3. **Run a synthetic custody preflight only after a candidate location is designated.** Use invented answers/canaries, preserve the whole version, recover/reopen exact bytes independently after a process restart, validate commitment and reject tampering/partial writes; positively demonstrate that an arm-author principal cannot read the plaintext or key, including through exported stream/log paths. If a proposed negative test can only demonstrate ordinary command-tool denial but other exposed tools can still read, mark NOT_QUALIFIED.
4. **Qualify author independence separately.** Identify a genuinely new, unresumed reference-author invocation, declare prior known exposures and source-world inputs, verify tool and context restrictions. Historical cases remain B1-theme-derived; if a meaningful neutral historical information need cannot be reconstructed, retain `CANNOT_NEUTRALIZE` and stop for prospective scientific disposition.
5. **Then choose the primary task route prospectively.** A fresh non-arm author may be viable once the host/exposure/custody boundary exists. Otherwise evaluate a frozen historical owner-query/event rule for source provenance, four-category breadth, temporal authority and task closure. Research 563's 36 decision headings **do not** already establish 12 answerable events. In either route, source closure precedes task-conditioned build sampling.
6. **Freeze in correct order.** Complete independently adjudicated packet and restricted version first; publish only its matching commitment before B0–B4 construction. Apply the existing arm parity/heldout/source-closure/scorer rules, then permit fresh evaluators to access the references according to an exact prospective scoring/disclosure policy. Do not make a post-result reference correction inside an existing attempt.

### Minimum synthetic custody acceptance evidence

Required observations are (i) complete round-trip byte identity plus committed cryptographic digest; (ii) immutable version and independently repeatable recovery; (iii) real *denial or ciphertext-only result* for every relevant later arm-author access route; (iv) absence of plaintext from public/agent-readable outputs, diagnostics, history and intermediate artifacts within the explicitly qualified scope; (v) demonstrable key/custodian separation where applicable; (vi) reviewer and evaluator exposure/provenance record; and (vii) an owner-authorized storage responsibility. All are conjunctive. A unit test of an access-check function or encryption primitive, on its own, cannot meet them.

## 6. Installed 7-Zip discovery and synthetic sealed-archive feasibility (2026-10-14)

A follow-up **read-only** local executable census found `C:\\Program Files\\7-Zip\\7z.exe` and graphical `7zFM.exe` / `7zG.exe`, despite `7z` not being available on the user's `PATH`. `7z i` reported 7-Zip **26.02 (x64)**. No package installation, credential change or store authorization was needed. The official format documentation at https://www.7-zip.org/7z.html describes 7z AES-256 encryption; 7-Zip's command-line format supports archive-header/filename encryption.

In a self-cleaning `.venv` temporary directory, an existing locally installed 7-Zip binary encrypted a **fabricated one-file JSON reference** into a `.7z` archive with `-t7z -mhe=on` and a generated **throwaway synthetic-only password**. These tests returned:

| Synthetic observation | Result |
|---|---|
| Archived file encryption method `7zAES` independently listed after providing the test password | PASS |
| Exact synthetic input bytes recovered with correct test password | PASS |
| Recovered SHA-256 matches original | PASS |
| Wrong password rejected for extraction and filename listing | PASS |
| Internal filename absent from wrong-password listing output | PASS |
| Deliberately modified encrypted archive rejected by 7-Zip's test command | PASS |
| Ephemeral test folders absent in a separate subsequent host read | PASS, zero matching directories |

**Important interpretation:** Standard stock 7z AES encryption uses non-AEAD encryption and archive checksums; the observed corruption rejection is **not an authenticated-encryption proof**. A future scorer/custodian therefore must independently verify the *exact original plaintext packet SHA-256* recorded in a trustworthy pre-arm public commitment. That supplies a content-integrity check against the frozen packet bytes, but cannot restore lost/corrupted data, prove a fresh source if the original commitment is untrusted, or compensate for weak password/key isolation. This newly discovered executable is a tested *confidentiality/storage component candidate* within C2, **not a claim that the authenticated-encryption C2 requirement is fully met**. Use an established authenticated mechanism instead if the eventually frozen threat model requires AEAD.

This synthetic demonstration passed a **throwaway password on a subprocess command line** and held an intentionally nonsecret fabricated plaintext under the usual development workspace. Those facts are permissible *only for synthetic feasibility*: they are explicitly disallowed as the real-reference procedure. Actual secrets must never be supplied as CLI arguments, to model-visible code, chat, version control, task logs or the current shared-agent account environment. If ultimately selected, favor a trusted owner-operated GUI/password-manager flow with independently tested key secrecy and recovery. Windows user-scoped encryption and GUI entry alone do not automatically prevent same-user agents from seeing decrypted material.

This was **not a denial test from a distinct arm-author principal**, not a new reviewer inference, not a full versioned packet/store restore across independently controlled sessions, not a review-output collector, and not complete secrecy of Claude/CLI stdout, system caches and provider transcripts. A technically encrypted archive still fails the P03 gold-custody contract if any agent can retrieve its password or pre-encryption answers. No owner password, key, production archive, full gold, reference author or private repository was created or changed.

The next useful step is narrower than a new storage platform: design and synthetically verify an **owner-controlled GUI secret entry + end-to-end reviewer output sealing/retention path**, explicitly checking where reference plaintext exists before encryption and testing the actual future arm-author tools against ciphertext-only access. A manual owner-owned archive can be a simple final retention artifact *if* those pipeline and identity boundaries pass. Otherwise retain C1/C3 alternatives without forcing 7-Zip to satisfy controls it does not provide.

## 7. Immediate outcome and stop boundary

**Findings:** The successful synthetic Claude file restrictions justify continuing with that low-cost host candidate for controlled **input**, not declaring the reference author/custody channel ready. C1/C2/C3 have plausible qualification paths; none has a separately proven output principal, committed complete hidden packet, tested recovery or effective arm-author denial. Selecting one permanently now would conflate proposed design with evidence.

**Next useful action:** Perform a bounded, read-only capability census of actual candidate custodian principals/stores and concrete available sealing tools, then present one or at most two synthetic access/custody trials requiring only the minimum specific owner action. Do not run more inference simply to repeat verified file denials. If every route requires new secrets, a new identity or a new repository role, stop for a narrow owner decision before creating one.

No real historical source/case neutralization, 12 primary tasks, complete gold packet, private storage mutation, new trust, model-specific execution authorization, B0–B4 arm build, scorer run, checkpoint promotion, implementation migration or physical selection occurred.

```text
P03_FILE_RESTRICTIONS=POSITIVE_FOR_TESTED_SYNTHETIC_PATHS
P03_FRESH_REFERENCE_AUTHOR=NOT_QUALIFIED
P03_COMPLETE_GOLD_CUSTODY=NOT_QUALIFIED
P03_PRIMARY_TASK_ROUTE=UNSELECTED
P03_EXACT_FIXTURE=UNFROZEN
P03_ARM_SCORES=NONE
NEXT_BOUNDARY=p-three-reviewer-execution-authority-qualification
CHECKPOINT=898_UNCHANGED
```
