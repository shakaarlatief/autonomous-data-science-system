# Research 601: R0-P03 source-free reviewer-report CMS handoff format and actual remaining boundary

**Date:** 2026-10-20
**Status:** FICTIONAL_REPORT_FORMAT_IMPLEMENTED / LOCAL_CMS_ROUNDTRIP_TESTED / CROSS_SESSION_OWNER_CUSTODY_NOT_TESTED / REAL_REVIEW_HOLD
**Scope:** Begin the proportionate M1 reviewer-workflow route identified in Research 600. Adapt the already evidenced fake CMS mechanics to a **reviewer-specific**, variable-decision, complete fictional source-status report, and separate its private notes from a safe progress receipt. Test the exact new local handoff property without invoking any real source review, allocating owner storage or broadening runtime access.
**Basis:** Research 513/559/576/579/586–589/592–600; prospective source review V0.4; Validation 268; Checkpoint 898 and Specification 028. Repository starting HEAD `0732fd07ec30ebb3668cd0802831a7833b4172b4`.
**Authority:** Exposed engineering coordinator and local synthetic engineering only. No owner-approved private reviewer destination, independent source-status reviewer, real source input, challenge, author packet admission, hidden reference or scored B0–B4 attempt.

## 1. A specific, not repeated, engineering need

Research 589 already reported one real Temporary Chat to owner recovery of a **fixed fabricated 9 legacy plus 12 primary answer packet**. The standalone sender `temporary_author_fake_cms_sender.py` and strict owner-side PowerShell recipient `scripts/r0_p03_fake_public_recipient.ps1` deliberately require exactly that fixed packet. Research 594 separately received a complete **unencrypted fictional reviewer intake report**. Neither earlier exercise tested preserving a versioned source-status reviewer report, with private source-specific rationale and varied holds, as an authenticated ciphertext while publishing **only** a safe receipt.

Research 600 accordingly identified the M1 owner-mediated review route as the preferred *prospective qualification hypothesis*, not as final custody selection. The immediate mechanical gap was not a new Windows account, a cloud reviewer service or another generic mock journal. It was a strongly bounded reviewer-report data and transfer format.

**Implemented:** `experiments/r0_p03_navigation_probe/s1_fake_reviewer_report_handoff.py` with focused tests `tests/unit/test_r0_p03_s1_fake_reviewer_report_handoff.py`. The script is standalone (stdlib + OpenSSL), so a future separately commissioned Temporary Chat could receive only this file and an owner-approved **public** certificate. This stage did **not** supply it to any such session.

## 2. Exact fictional-only report and output separation

The input report is a complete list of **exactly three invented source IDs**, bound to hardcoded fake content and source SHA-256 values. It contains a fake historical observation, a fictional exception, and a deliberately invented design cue. Unlike the earlier fixed 9+12 sender, entries can vary in inspected/delivered state, source-content disposition, review scope and restricted fake-note **codes**, while still requiring complete roster accounting. Missing bytes produce an explicit HOLD rather than disappearing.

The fake report validator requires:
- exact marker `S1_FICTIONAL_REVIEWER_REPORT_NO_REAL_PROJECT_MATERIAL`, schema format `s1-fictional-reviewer-report-v1` and exact three-source manifest identity;
- strict `synthetic_only=true`, `actual_independent_actor_verified=false`, `real_source_reviewed=false`, `source_world_admitted=false`;
- three unique exact fictional source IDs and matching fixed invented source digests, with no unknown extra fields, paths or arbitrary rationale text;
- strict boolean delivered/inspected states; missing or uninspected source cannot silently become candidate; typed file/span/component dispositions;
- fictional note values only from a closed `FAKE_NOTE_...` vocabulary; **not** real author-source classifications, old W5 relevance or raw human/LLM project reports;
- fixed actor-exposure limitation and explicit not-challenged/disputed status. A reviewer cannot self-certify independent challenge through one report field.

The sender reads the structured fake report from stdin (bounded to 16,384 bytes) and encrypts into a single exact filename, `R0_P03_FAKE_REVIEWER_REPORT.cms`, using the recipient's verified public PEM certificate and OpenSSL CMS AES-256-GCM. The sender writes no plaintext report file, refuses existing ciphertext output, private-key-looking certificates and no-OpenSSL fallback, and prints only a *strict public receipt*: format/filename, ciphertext byte length/SHA-256 and explicitly false custody/plaintext claims. The receipt's exact field set rejects source IDs, statuses, private notes and any counts that could expose source-specific dispositions.

A separate `verify` CLI operation accepts a local recipient key, certificate and ciphertext and verifies ciphertext SHA-256, authenticated GCM decryption, exact canonical complete fake JSON and closed schema **before** returning only `S1_FAKE_OWNER_REVIEW_READBACK=PASS/FAIL`. Failed decrypt stdout is never returned to the caller, because OpenSSL can produce provisional unauthenticated plaintext before reporting GCM failure. All outputs are fictional. This recipient mode is a reusable *mechanical test*, **not** a substitute for an owner-approved restricted storage or access-control workflow.

## 3. Integration decisions and observed portability issue

The earlier fake CMS sender relies on a standalone local Python/OpenSSL environment, while the owner recipient in Research 587/588 is a strict PowerShell 5.1 implementation bound to the original fixed packet. **It cannot be reused unchanged for this reviewer-shaped payload**, and this work does not modify or weaken it. No old owner-only fake key or recipient directory was opened or reused.

The first new combined test run returned `18 passed, 1 failed`: the isolated CLI sender could not resolve a bare `openssl` command through the current Windows PATH, although the preexisting Git-for-Windows binary was known and accessible. A bounded portability repair now first tries `shutil.which("openssl")` and, only on Windows, the **previously verified explicit** `C:\Program Files\Git\usr\bin\openssl.exe` path. If neither exists, it still fails closed. The authenticated algorithm, file constraints, recipient validation and private/public fields are unchanged.

The corrected focused test run returned **19 passed** for the new report sender/reader and the earlier fake sender and CMS tests. A further six-module S1 regression run returned **75 passed** including the earlier transport, mock-custody and role-boundary tests (Validation 268). This includes:
- source roster/hash/typed-status/booleans validation and incomplete fake delivery HOLD;
- rejection of arbitrary real-source paths, free-text/extra private fields and misclassified representations;
- public receipt rejection of fake private notes, variable statuses and bool/int coercion;
- actual disposable RSA certificate generation, real OpenSSL CMS sealing and authenticated full fake report readback;
- ciphertext tamper and wrong-digest rejection;
- a separate Python-process sender and recipient CLI, with observed stdout containing receipt/status only.

The temporary test private key/certificate and ciphertext were created only inside ignored pytest scratch and are not real owner-held custodial resources. Test subprocesses, even when separate, ran under the same host/permission context. The previous Runtime Bridge readOnly profile was observed working at the start of this stage; the only newly observed application defect was OpenSSL executable discovery and it was corrected without changing runtime service settings.

## 4. What this milestone does not establish

**Not established:** Owner-mediated real Temporary Chat delivery, a separately authenticated reviewer, actual prior-context/tool isolation, owner-approved full protected reviewer-output destination, owner recovery under a different privilege/session, protected raw reviewer rationale storage, data-retention/provider limitations, independently held journal anchors, a qualified separate challenger, or actual author-facing report exclusion.

The fake report has only three fabricated tokens, not genuine semantic adjudication of 406 candidate plus 2,133 historical evidence records. The bounded enum/code validation **intentionally cannot accept genuine free-form source-specific real reviewer reports**. A future production/private report schema and separately chosen custody route must be authorized and reviewed independently; this fake prototype cannot simply have its marker changed and be called ready for protected data.

The script's `verify` command returns only PASS/FAIL. It verifies the complete decrypted fictional report exists and matches the expected fake schema, but it is not a durable independent copy of the raw private report and does not itself supply append-only, tamper-evident audit or approved recovery key lifecycle.

## 5. Next bounded operational decision

**Next proposed step:** One owner-approved **fictional-only, separate Temporary Chat → owner** reviewer-report handoff using the new sender and a deliberately selected owner-only recipient mechanism. Before inviting that session, specify where the temporary public cert is created, which owner-controlled fake directory is used, how owner-side complete report recovery is independently confirmed, how ciphertext is handed back, how failures are classified, and which safe receipt the exposed coordinator may receive. The original fixed-packet PowerShell recipient does not already handle this format.

After **one** successful separately witnessed reviewer-shaped fake handoff, stop repeating this class of trial. Independently qualify V0.4, reviewer/challenger exposure, actual batch transport/inspection and protected output before even one real potentially contaminated source is opened. Windows-account/service hardening is conditional on a concrete M1 failure route, not the default next step.

## 6. Scientific and authority holds

```text
RESEARCH_601=FICTIONAL_REVIEWER_REPORT_FORMAT_AND_LOCAL_CMS_MECHANICS
S1_NEW_SOURCE_FREE_SCHEMAS=IMPLEMENTED_AND_TESTED
LOCAL_OPENSSL_CMS_REPORT_READBACK=TESTED
FIRST_TEST_RUN=18_PASS_1_FAIL
OPENSSL_WINDOWS_PATH_REPAIR=TESTED
FINAL_TEST_RUN=19_PASS
CROSS_SESSION_OWNER_REVIEWER_REPORT_HANDOFF=NOT_EXECUTED
OWNER_RESTRICTED_REVIEWER_LEDGER=NOT_SELECTED
ACTUAL_REVIEWER_AND_CHALLENGER=NOT_QUALIFIED
SOURCE_STATUS_V04=NOT_INDEPENDENTLY_ACCEPTED
REAL_SOURCE_REVIEW=NOT_STARTED
AUTHOR_SOURCE_ADMISSIONS=ZERO
HIDDEN_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
