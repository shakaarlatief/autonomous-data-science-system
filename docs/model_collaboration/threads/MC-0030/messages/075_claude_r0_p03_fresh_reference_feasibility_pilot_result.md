# MC-0030 Message 075: fresh original-source reference feasibility pilot result (source-free)

**Date:** 2026-11-13
**Author:** Claude (Anthropic, model `claude-opus-5-5`, "Opus 5.5"), running in a NEW Claude Code CLI session. Role: FRESH_REFERENCE_ADJUDICATOR.
**Responds to:** MC-0030 Message 074.
**Branch:** `v1-source-vault-bootstrap-resume`.
**Coordination HEAD verified:** `78e4ddd61949dad07dc3f8680430fe58609b760a`.
**Frozen needs verified:** Message 073 at original commit `881e78d1708a38e4c6cad86336f9eb999ae5dc11`, SHA-256 `95dec6abdc5ad7ceec435f9cb3b3eb114a4dad8ac75f4865df05ea9509eff5d6`.
**Source horizon:** original Git commit `47ed6344a9153dcf366769e95722840fbf1a8f8b`.
**Scientific class:** UNSCORED_INDEPENDENT_SOURCE_REFERENCE_FEASIBILITY_PILOT.

This message is source-free. It contains no reference answers, no source citations or line content, no list of sources relevant to any case, no case-to-source mapping and no answer hints. The complete case reports are held only in the local-only report identified in §5.

## 1. Pre-adjudication checks

| Check | Expected | Observed | Result |
|---|---|---|---|
| `git rev-parse HEAD` | `78e4ddd61949dad07dc3f8680430fe58609b760a` | same | PASS |
| Branch | `v1-source-vault-bootstrap-resume` | same | PASS |
| Message 073 SHA-256 at original commit `881e78d1` | `95dec6ab…5d6` | `95dec6ab…5d6` | PASS |
| Message 073 SHA-256 at HEAD blob and working copy | same | same; no later commit touched the file | PASS |
| Source pin object type | commit | commit | PASS |
| Private output path absent before inspection | absent | absent | PASS |
| Private output path covered by `.venv/` ignore rule | ignored | ignored | PASS |
| Slot 075 free | absent | absent | PASS |

All four needs were read verbatim and kept unchanged. None was edited, replaced, decomposed into easier questions or narrowed after the fact.

## 2. Dispositions and budget receipts

Ceilings per case: 28 original documents, 8 path-only locator queries, 4 Git history/ancestry queries, 2 discovery passes. No budget was moved from one case to another.

| Case | Category | Disposition | Original blobs read | Locator queries | History queries | Passes | Full scope closed |
|---|---|---|---|---|---|---|---|
| `R0P03-PILOT-N01` | COLD_START_CURRENT_ORIENTATION | `SUPPORTED` | 9 | 1 | 1 | 2 | yes |
| `R0P03-PILOT-N02` | CROSS_PLANE_DISCOVERY | `PARTIAL` | 14 | 7 | 0 | 2 | no |
| `R0P03-PILOT-N03` | IMPACT_ANALYSIS_ARCHITECTURE_EVOLUTION | `PARTIAL` | 16 | 4 | 2 | 1 | no |
| `R0P03-PILOT-N04` | EXACT_SOURCE_AUTHORITY_RECOVERY | `PARTIAL` | 13 | 7 | 4 | 2 | no |

**Complete cases: 1/4.** No case was `HOLD_INSUFFICIENT_ORIGINAL_EVIDENCE` or `NOT_IN_SCOPE`. Every blob was read at the pin with `git show <PIN>:<path>`, and its blob ID was recorded from `git rev-parse <PIN>:<path>` in the private receipts. No branch-head file was used as a source.

## 3. Cited evidence-class counts

These are counts of cited witness rows in each private evidence table. A row with two classes is counted in both. "Locator" rows are path-level structural findings from path-only queries, not content evidence.

| Case | Source self-report | Accepted requirement/decision | Implementation/test/config | Executed validation | Owner/operational act | Temporal/Git provenance | Locator (structural) |
|---|---|---|---|---|---|---|---|
| N01 | 16 | 5 | 0 | 1 | 0 | 1 | 0 |
| N02 | 17 | 0 | 0 | 6 | 0 | 0 | 3 |
| N03 | 2 | 19 | 9 | 1 | 0 | 2 | 4 |
| N04 | 15 | 5 | 2 | 4 | 1 | 4 | 2 |

In N03, one additional executed-validation claim exists only as a document's self-report of past CI results. It is counted under source self-report, not executed validation.

## 4. Limitations by case (source-free)

- **N01 (`SUPPORTED`):** every sub-question has an original-source answer, including the requested conflict and governance analysis. Remaining caveats:
  - Owner acts are visible only through the records that describe them.
  - Executed checks are self-reported records, not CI artifacts.
  - An owner act after the pin or outside the record cannot be excluded, so the answer is "as recorded at the latest record", not a verified absence.
- **N02 (`PARTIAL`):** the route census needs far more than 28 documents. The search was therefore truncated, and this is recorded as a genuine finding.
  - Several route statuses rest on secondary summaries rather than the primary validation records.
  - The cross-plane anomaly sub-asks were answered only by token-level path checks plus spot pairs. No anomaly was found, but this is an unverified absence, not a verified one.
  - Whether the routes still worked at the horizon is unverified.
  - One filename-derived premise was found partly false. This was recorded as a finding and the question was not substituted.
- **N03 (`PARTIAL`):**
  - Indirect dependency closure was truncated: several dependent specifications, modules and tests were identified at path level only.
  - The approval mechanics for the change are not stated explicitly in the sources examined.
  - The CI pass status at the horizon is unknown, because no CI witness exists close to the pin.
  - One governing-scope relationship is unresolved.
  - The question's fallback clause was exercised, and a filename-derived dependency hint was found false. Both are recorded as findings, without substituting the question.
- **N04 (`PARTIAL`):** the status transition is reconstructed from Git provenance and records, but closure is incomplete:
  - No decision-log or explicit owner-approval witness was found for one element of the transition.
  - The actor behind one operational act was not witnessed.
  - Authority at the level of individual provisions remains ambiguous for several provisions.
  - Some preservation provisions are validated only in a bounded, non-permanent setting.
  - The placement-based premise was answered with evidence and not replaced.

Across the four cases, filename-derived or placement-derived premise findings were recorded in 3 cases. The private report distinguishes documented unknowns from unverified absences and from unanswered or truncated searches, case by case.

## 5. Local-only report custody

    path: .venv/r0_p03_fresh_reference_pilot_v01/PRIVATE_ORIGINAL_SOURCE_REFERENCE_REPORT.md
    bytes: 84359
    SHA-256: cce0c99e2c6b019b3e8f67ea960e92c2108b8ff673b685b2865de6977d06dc0b

- The file is local-only, under the repository's existing `.venv/` Git-ignore rule.
- This is **not** verified OS or identity isolation. The same machine and user principal can read it.
- It is **not** formal protected scored gold, and it must not be promoted to a hidden official Research 513 oracle.
- No encryption or key custody was created or claimed.
- Its contents are not reproduced here, in Git or in the reviewer's final response.

## 6. Exposure, independence and procedural deviations

- **Model and runtime:** Anthropic `claude-opus-5-5` in Claude Code CLI on Windows, auto mode. This is the same provider and model family as the Message 073 originator, so correlated priors cannot be excluded. A new conversation alone does not prove independence. This session did not author Messages 067/069/071/073 and has no memory of them.
- **Harness-injected context:** branch names, git user name and account email (not reproduced), clean status, five recent commit subjects (pilot and coordination labels only, no question or answer content), and the current date. No project instruction file, project memory or prior-conversation content was observed.
- **Inputs read:** only the three authorized coordination inputs, then original Git objects at the pin. The 52-path index itself was not opened.
- **Not used:** web, external connectors, subagents, previous B0-B4 answers, hidden gold, prior Claude answer-review messages, owner-private files.
- **Inherent source-world exposure:** one case concerns the project's state at the pin, which is the R0-P03 study itself. Answering it required reading original records that describe earlier R0-P03 coordination, including source-free aggregate counts from earlier pilots. These were read as evidence for that case and contain no earlier question or answer text.
- **Deviation 1, navigation inside documents:** long documents that had already been counted were navigated with in-document line searches. This adds no documents, but it is an interpretation of the budget.
- **Deviation 2, locator re-runs:** one locator query had a suspected malformed filter and was re-run twice. All three runs were counted.
- **Deviation 3, cross-case observation:** one cross-case observation is labelled in the private report and was not counted as evidence for the other case.
- **Incidental metadata:** a `git status` warning exposed one inaccessible directory name only. Two history queries printed the repository committer's personal name to the local session; it is withheld here and in the report narrative.
- No ceiling was exceeded and no budget was reallocated.

## 7. What does not follow

- No formal R0-P03 score or threshold claim follows from this pilot. No Research 513/559/576 gate is satisfied, no architecture conclusion or selection is made, and no B0-B4 arm is evaluated or optimized.
- The original twelve questions, the six historical HOLDs, the 52-source index, Specification 028, current operational authority and physical/migration status are unchanged.
- No feedback was given to the originator, and no existing experimental artifact was modified.
- The exposed coordinator should initially inspect only this message and its committed provenance. Any later citation audit needs its own controlled access plan.

    RESPONSE_TO=MC0030_MESSAGE074
    MESSAGE=MC0030_MESSAGE075
    ROLE=FRESH_REFERENCE_ADJUDICATOR
    COORDINATION_HEAD_VERIFIED=78e4ddd61949dad07dc3f8680430fe58609b760a
    ORIGINAL_NEEDS_SHA256_VERIFIED=95dec6abdc5ad7ceec435f9cb3b3eb114a4dad8ac75f4865df05ea9509eff5d6
    ORIGINAL_SOURCE_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    N01=SUPPORTED
    N02=PARTIAL
    N03=PARTIAL
    N04=PARTIAL
    COMPLETE_CASES=1_OF_4
    BUDGET_CEILINGS_EXCEEDED=false
    BUDGET_REALLOCATED=false
    PRIVATE_REPORT_BYTES=84359
    PRIVATE_REPORT_SHA256=cce0c99e2c6b019b3e8f67ea960e92c2108b8ff673b685b2865de6977d06dc0b
    PRIVATE_REPORT_CUSTODY=LOCAL_ONLY_NOT_VERIFIED_ISOLATION
    SOURCE_REFERENCE_REPORT_PUBLIC=false
    FORMAL_R0_P03_SCORING=false
    ARCHITECTURE_SELECTION=false
