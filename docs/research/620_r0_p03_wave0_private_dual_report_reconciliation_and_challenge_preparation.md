# Research 620: Owner-private authenticated comparison of the two Wave0 source assessments

**Date:** 2026-11-02
**Status:** OWNER_REPORTED_SECOND_REPORT_SEPARATE_VERIFY_PASS / PRIVATE_TWO_REPORT_RECONCILIATION_TOOL_SYNTHETIC_TESTED / REAL_COMPARISON_NOT_EXECUTED / ADVERSARIAL_CHALLENGE_PENDING
**Scope:** Progress from two independently authored encrypted ten-record Wave0 source-status assessments to a **source-preserving, owner-only, authenticated and encrypted paired comparison**, retaining source-specific reasoning and disagreement evidence for a later adversarial challenger without importing restricted plaintext into the exposed engineering coordinator.
**Basis:** Research 513, 559, 576, 591, 617–619, Validations 288–296 and the owner's new full second-report `Verify` log.
**Authority:** Engineering preparation and source-free testing only. Does not authorize a second actor to receive reviewer-private reasoning; does not constitute semantic review, accepted source release, score, authorization of author packet or completion of the adversarial challenger phase.
**Specification:** 028 unchanged.

## 1. Qualified input state: both encrypted reports independently recovered

The first reviewer report, SHA-256 `9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366`, 41,697 bytes, already passed owner-reported `Receive` and separate `Verify` with **ten canonical records** and no source-specific plaintext printed (Validation 293).

After returning with the newly sealed challenger first-pass receipt (Validation 296), the owner supplied the following independently invoked **challenger `Verify` output**:

```text
{"actual_adversarial_challenge": "PENDING", "author_world": "WORLD_UNFROZEN", "complete_independent_source_records": 10, "independent_source_dispositions": "RESTRICTED_NOT_PRINTED", "original_reviewer_conclusions_exposed_to_challenger": false, "original_reviewer_report_opened_by_coordinator": false, "original_source_batch_bound": "PASS", "owner_independent_challenger_cms_authenticated": "PASS"}
S1_WAVE0_OWNER_INDEPENDENT_FIRST_PASS_READBACK=PASS
S1_WAVE0_CHALLENGER_OWNER_FULL_READBACK=PASS
S1_WAVE0_CHALLENGER_OWNER_RECHECK=PASS
```

The challenger ciphertext identity remains SHA-256 `50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64`, reported 46,807 bytes. The current log directly supports **owner-relayed independently successful verification of the saved second ciphertext** and an authenticated complete ten-record second report. It does **not** show the initial second `Receive` stdout in this message: do not claim that action was directly observed or use the second `Verify` to infer independently observed `Receive=PASS`. The successfully saved file is nevertheless present in the owner's protected recipient store as required by that `Verify`.

The absence of reviewer exposure is a required **self-reported record field** validated by the schema; it is not an independent proof about provider memory, prior exposure or latent model training. Both reports remain **proposals pending independent semantic challenge** and no source is author-admitted.

## 2. Scientific method: mechanical comparison is not adversarial adjudication

The immediate next material work is a **mechanical paired comparison** of ten same-identity original sources, not a simplistic vote on labels or a new source-free actor inventory:

- Compare the exact reviewer/challenger **complete-file disposition tokens**, inspection claims, proposed claims, missing-context lists, contamination/disclosure risks and source-bound reasoning. Preserve the entire original records in a protected comparison object rather than eliding rationale because two token labels agree.
- Every exact-field difference is a private **inspection priority**, not automatically a scientifically material disagreement: string inequality may reflect harmless paraphrase, and string equality may reflect shared omissions or correlated bias.
- A matching disposition does not constitute corroborated correctness or `CHALLENGED_ACCEPTED`. **All ten records remain to be independently challenged** against original context and the source universe.
- The comparison must be reproducible from the authenticated fixed **original report**, **independent challenger report** and exact original source ZIP; it must not silently update either historical assessment, leak individual source paths/statuses to public Git, or insert old answer material into the eventual blind author packet.
- A later **targeted adversarial challenge** may use strictly owner-authorized private reviewer reasoning plus the original context, but not before the owner has qualified the private paired dossier, scoped the access and approved that disclosure.

The original source ZIP is 26,416 bytes, SHA-256 `c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387`. The first reviewer CMS and second challenger CMS stay separate and immutable in the existing owner-held Windows recipient directory. No new key or public certificate is needed.

## 3. Implemented specific owner-only comparator

New `experiments/r0_p03_navigation_probe/s1_wave0_owner_private_compare.py` performs:

1. Exact **three-input identity** checks for the fixed historical Wave0 ZIP and the two already saved ciphertext SHA-256 values.
2. Owner-only OpenSSL authenticated AES-256-GCM decryption of **each** report. Passphrase is entered interactively in the owner session and piped to OpenSSL via stdin; ciphertext comes from named file arguments. Partial unauthenticated OpenSSL output is discarded if decryption fails.
3. Independent strict schema validation of the first `NON_ARM_SOURCE_STATUS_REVIEWER` record and the separate `NON_ARM_SOURCE_STATUS_INDEPENDENT_CHALLENGER_CANDIDATE` record, each bound to the ten exact pinned original source entries.
4. A deterministic private canonical **paired dossier** containing all ten source-bound reviewer/challenger records, exact difference flags for disposition token, inspection state, claims, missing context, disclosure risks and rationale, plus explicit non-adjudication/required semantic challenge for **every** record.
5. Re-encryption of the paired dossier under the **same existing owner's public certificate** using authenticated CMS AES-256-GCM, with no plaintext disk file. No-overwrite save to `R0_P03_S1_WAVE0_OWNER_PRIVATE_COMPARISON.cms` in the owner's already protected folder. Standard output emits only ciphertext digest/length, record count, authenticated source/report markers and explicit **no source-specific findings printed**.
6. Distinct owner-only `Verify` action re-authenticates all three stored ciphertexts (reviewer, challenger and private comparison), independently recomputes the canonical paired dossier in process memory and compares **exact plaintext bytes**. This is reproducibility of the mechanical transformation, not semantic truth.

New `scripts/r0_p03_s1_owner_wave0_private_compare.ps1` wraps `SelfTest / Compare / Verify` in the owner's normal interactive PowerShell, checks the original source ZIP and both archived CMS exact SHA-256 values, verifies original recipient identity and restrictive owner ACL, uses the existing encrypted private key without exporting it, and prints only fixed-safe markers. **Never run its Compare/Verify actions through Runtime Bridge or the exposed engineering coordinator.**

Existing original and second CMS files are read-only inputs and remain unchanged. The new encrypted dossier is additional restricted evidence, **not an author-facing knowledge file or a score**.

## 4. Verification and limitation disclosure

The first synthetic code tests use only *invented ten-source ZIP contents, invented first-reviewer/challenger statuses and reasoning, and an ephemeral fictional encrypted RSA key* stored under ignored pytest scratch. They exercise real authenticated encryption/decryption, full paired report/flag creation, byte-for-byte owner re-verification, wrong passphrase rejection, altered input and tampered comparison rejection, no ciphertext overwrite and no protected findings in the safe receipt. They do not read either real saved CMS or the owner's private key, and their synthetic disagreement count does not describe actual historical content.

PowerShell static parsing, integrated regressions, source-bound integrity and guarded publication are independent engineering checks to record as actually observed, not upgrade to proof of owner-side privacy. In particular, Windows same-SID processes may share access to the owner-local folder, and owner reporting is separate from directly observed result. The Level B practical assurance limitation remains explicit.

## 5. Next scientific step, not yet executed

Once the owner runs local `SelfTest`, `Compare` and later independent `Verify`, the two first-pass judgments and their exact mechanical differences will have a **complete owner-held, encrypted comparison dossier**. The next substantive task is then designing the smallest **owner-private materiality triage and scoped adversarial challenge** that can test the first reviewer and second challenger reasoning without revealing sensitive pairings to the exposed coordinator. That phase must distinguish material disagreements, false agreements/shared blind spots and absence of context evidence; do not prematurely declare ten/ten correctness or freeze the source world.

```text
RESEARCH_620=OWNER_PRIVATE_DUAL_REPORT_COMPARATOR_PREPARED
FIRST_REVIEWER_OWNER_RECEIVE_AND_SEPARATE_VERIFY=OWNER_REPORTED_PASS
SECOND_CHALLENGER_SEPARATE_OWNER_VERIFY=OWNER_REPORTED_PASS
SECOND_CHALLENGER_RECEIVE_MARKERS=NOT_DIRECTLY_SUPPLIED_IN_THIS_TURN
BOTH_FIRST_PASS_RECORD_SETS=10_EACH_OWNER_AUTHENTICATED
PRIVATE_COMPARISON_REAL_RUN=NOT_EXECUTED
ACTUAL_ADVERSARIAL_CHALLENGE=PENDING
SOURCE_AUTHOR_ADMISSIONS=ZERO
S3=WORLD_UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
