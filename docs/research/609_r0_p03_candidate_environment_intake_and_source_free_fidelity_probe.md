# Research 609: Candidate reviewer intake reconciliation and first actual file/representation fidelity test packet

**Date:** 2026-10-28
**Status:** A2_CANDIDATE_ENVIRONMENT_INTAKE_RECEIVED_LIMITED / SOURCE_FREE_TEXT_AND_PNG_PROBE_PREPARED_NOT_EXECUTED / NO_ACTOR_ADMISSION
**Scope:** Reconcile one owner-relayed **actual candidate-session environment report** against S1 A2 actor qualification, preserve its complete text, and prepare a new strictly harmless attachment-fidelity test that is **not** another fictional encrypted reviewer-output trial or historical-source assessment.
**Prior public HEAD:** `36fd56cf3dd0e0cf06902c8affd16928926395bd`.
**Basis:** Research 513/559/576/603/605–608; Validation 270–274; S1 A2 actor-admission gate candidate V0.1; prospectively corrected V0.6 source-status method (unaccepted).
**Authority:** The coordinator can preserve and compare public-safe evidence, but this document cannot admit a real reviewer/challenger, make a provider isolation guarantee, authorize historical intake, approve private custody or expose any source to the future task author.

## 1. Exact separate-session report and provenance limits

The owner attached `Geplakte tekst(20261028-135243).txt`, attributed to a prospective source-free Temporary Chat reviewer environment. The uploaded bytes were directly inspected **in this coordinator conversation's mounted attachment runtime**, yielding:

```text
ORIGINAL_OWNER_UPLOADED_REPORT_BYTES=16570
ORIGINAL_OWNER_UPLOADED_REPORT_SHA256=2d35452210e56e298402fad34ebe33420143f40f1029091369588052ba347d20
ORIGINAL_LINE_ENDINGS=236_CRLF
ORIGINAL_PHYSICAL_LINES=237
ORIGINAL_FINAL_NEWLINE=ABSENT
```

The complete, unabridged reviewer response is durably preserved in normalized LF form at:

`experiments/r0_p03_navigation_probe/reviewer_intake_evidence/20261028_a2_candidate_reviewer_environment_intake_report.txt`

```text
NORMALIZED_REPORT_BYTES=16334
NORMALIZED_REPORT_SHA256=610dd4025dbb5bc129e12ed1670dcae7efc0d9d66460893f9f4d9d9e466146dc
NORMALIZATION=CRLF_TO_LF_ONLY
FINAL_NEWLINE=ABSENT
PHYSICAL_LINES=237
```

This source-free report is **owner-relayed**. The coordinator did **not** observe the other session's actual runtime/session-identity configuration, tool calls, history or absence of model-provider latent exposure. Neither its self-reported session designation nor claims about disabled connected apps have been independently verified in this coordinator session.

## 2. Candidate session's reported evidence and measured decision

The report explicitly returned `INTAKE_LIMITED`, **not** `INTAKE_OBSERVED` or `INPUT_HOLD`, and marked the real reviewer and challenger admissions `PENDING`.

**What its session reports actually doing:**
- receiving and reading **one** source-free Markdown intake document;
- seeing its own current conversation messages and advertised tool descriptions;
- identifying that it is described as an unpersonalized Temporary Chat, while separately admitting it cannot verify non-Project membership or provider-internal session history.

**What it did not actually test:**
- local Python, general filesystem, conversation retrieval, advertised web capabilities, binary export/encryption or independent account/provider security;
- exact byte fidelity or completeness of a nontext asset;
- direct authorization/denial to repositories, other files, previous conversations or connected accounts;
- reviewer-only recipient routing, actual private-report recovery or negative access from the **future primary-author** environment.

The report's `UNAVAILABLE` label for connected app and account-backed Library surfaces is explicitly based on a session-level environment description **without performing an actual denial probe**. Treat this as **reported environment metadata**, not an audited universal denial.

**A2 gate interpretation:** A2-R02 *candidate-session exposure inventory* now has **REPORTED_ONLY** evidence of the visible current context and claimed route limitations. This is meaningful intake progress, but does **not** qualify actor identity, historical noncontamination or full isolation. A2-R03/R04 exact attached-input bytes and representation fidelity remain **NOT_TESTED** by that candidate. A2-R05 restricted real reviewer output remains **NOT_QUALIFIED**. A2-R06 separate challenger and A2-R07 actual future author-route exclusion remain **NOT_TESTED**, as do actual recovery/resumption properties. This is **not** an owner authorization to deliver any historical batch.

## 3. Next direct test: source-free actual candidate attachment fidelity, not duplicate CMS

The candidate's main observed technical capability is **reading a current text attachment**. Its highest-value cheap next check is therefore whether the **same** prospective candidate session can actually receive, preserve and inspect exact full bytes of mixed text and one visual file. That is a distinct A2-R03/R04 property, not another A1 encryption round trip, and it requires no account/OS configuration changes.

The newly prepared packet is:

| Source-free file | Exact bytes | SHA-256 |
| --- | ---: | --- |
| `a2_source_free_fidelity_unicode_crlf.txt` | 193 | `8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb` |
| `a2_source_free_fidelity_pattern.png` | 291 | `fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f` |
| `S1_A2_CANDIDATE_FIDELITY_PROBE_V01.md` | 5,392 | `c00df15f79b1b734a40efa34b5fe14aed536fdedafb4acba49a77114974e384c` |

The text fixture encodes deliberately non-ASCII UTF-8, one tab, **5 CRLF sequences and no trailing newline**, testing lossless byte delivery rather than rendered text plausibility. The 48×32 RGB PNG is a valid CRC-checked sequence `IHDR/tEXt/IDAT/IEND`, including original pixel data, a benign PNG text-metadata chunk, and no privileged/project history. Its original full length/hash and decoded dimensions/pixels are established locally with standard library checks.

**Exact-byte Git preservation:** A fresh check found that local Git `core.autocrlf=true` could otherwise normalize the deliberate CRLF text fixture into a different Git blob. The root `.gitattributes` now applies only **two exact file-specific rules**: `-text whitespace=cr-at-eol` for this deliberately CRLF-encoded text fixture and `binary` for this PNG. The `cr-at-eol` whitespace exception was added only after the repaired guarded commit reached `git diff --cached --check` and correctly identified deliberate CRLF as apparent trailing whitespace; rollback restored the index. A precommit `git hash-object` check confirmed the text fixture's filtered and unfiltered Git blob identities are both `be4f60e2f5504ad3e73fba52316ef27f2eb947f8`. This preserves the intended 193-byte attachment identity across checkout environments, without changing generic project text normalization.

**Test instructions:** Give the existing candidate Temporary Chat (if still available) only the three files above. Instruct it to read **only those attachments**, hash raw bytes if accessible, report text newline/Unicode fidelity and independently decode/visually inspect the PNG, with explicit unknowns for any unavailable raw bytes or render. It must not read the project repository, history, private keys or other assets. The brief does **not** tell the prospective reviewer the expected digests or pixel categories. Its source-free response can return to the owner/coordinator for exact independent comparison.

**Important anti-overclaim:** A pass here demonstrates only a subset of *this specific candidate route's* non-sensitive text/PNG byte receipt and visual rendering. It does not prove handling all historical formats or loaded/linked assets; it is **not** a separate human identity/contamination check, confidential storage, source adjudication or author-view deny witness. A failure should record exactly whether bytes were transformed at upload, computation tools were inaccessible or the image renderer was incomplete, not declare a generic model failure.

## 4. Remaining route-first decisions

The prior owner-reported A1 CMS handoff already established one **fictional** encrypted-report recovery and safe aggregate receipt. Re-running the same cryptographic demonstration is not warranted here. Actual restricted output custody, live actor-binding and direct future author-route denial must be tested **on the eventual selected reviewer/challenger/author environments**, with exact owner-approved recipients and protected artifacts. We do not make a generic Windows service or permanent branch/folder arrangement an assumed condition; a concrete inability to demonstrate the required boundary should trigger alternative architecture selection.

A later reviewer/role admission decision requires evidence beyond this self-report: owner-approved actor constraints, actual source/representation parity, independently accepted source method, restricted reviewer ledger and complete recovery, separate challenger, and an author-view exclusion witness. The current attached public coordinator/Codex workspace is **not** a substitute for an independently qualified reviewer.

## 5. Status and science holds

```text
RESEARCH_609=CANDIDATE_ENVIRONMENT_INTAKE_RECONCILED
OWNER_RELAYED_INTAKE=INTAKE_LIMITED
REPORT_FULL_TEXT=LF_NORMALIZED_PRESERVED
A2_R02_ACTUAL_CANDIDATE_EXPOSURE=REPORTED_ONLY
A2_R03_R04_TEXT_PNG_ROUTE_FIDELITY=TEST_PACKET_PREPARED_NOT_EXECUTED
A2_R05_REAL_RESTRICTED_REVIEW_OUTPUT=NOT_QUALIFIED
A2_R06_SEPARATE_CHALLENGER=NOT_ADMITTED
A2_R07_PRIMARY_AUTHOR_DENIAL=NOT_TESTED
REAL_NON_ARM_REVIEWER=NOT_ADMITTED
REAL_SOURCE_BATCHES_DELIVERED=ZERO
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_GOLD=NONE
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
