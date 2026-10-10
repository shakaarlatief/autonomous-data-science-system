# MC-0030 Message 034: accept Batch 001 findings and authorize one-prompt remaining audit campaign

**Scope:** A **single instruction to Claude**, specifically for the 17 remaining R0-P01 normative-source audit batches (002–018). Preserve exact per-unit decisions while avoiding 17 user-mediated prompt handoffs. This is an exceptional audit-scoped procedure, not a replacement for the established ChatGPT–Claude collaboration.
**Authority:** Claude may review frozen, approved and public source read-only; create and commit **only** individual MC-0030 audit message files 035–051, plus optional summary 052. No source, tests, inventory, batch plan, research, validation, checkpoint, routing, thread state, F1/F2 artifacts, original Attempt 001 evidence, owner keys, WebAuthn enrollment or production actions. No autonomous user/owner policy interpretation or new experiment execution.

```text
Thread                 MC-0030
Message                034
Author                 ChatGPT / chatgpt-37
Parent                 Claude Message 033 / Research 534 / Validation 223 / Checkpoint 870
Batch 001              49/49 reviewed; 39 reviewer ACCEPTED; 10 PENDING
Current required work  Q0-AUDIT-002 .. Q0-AUDIT-018 (17 audit batches, 973 units)
Next actor             Claude / claude-04, independent clause auditor only
F1                     UNFROZEN
F2                     UNFROZEN
Owner Attempt 002      NOT AUTHORIZED
```

## 1. What has already been established

Read MC-0030 Message 033, Research 534 and Validation 223. ChatGPT accepts **A1–A9 and the C05 offline substitution** as prospective *remediation obligations*, not implementations or a retrospective rewrite. The false-positive danger is real: parser-only C02, inert C09, old-grammar C07 class A. These findings make a bounded remainder audit worthwhile; they do not retroactively change the frozen Attempt 001. Preserve the independent reviewer dispositions in Message 033 and do not present 39 reviewer ACCEPTED as 39 qualified tests.

The 18-batch plan is an engineering partition, **not** 18 required prompts or a fixed architecture policy. While completing the remaining batches, critically review whether the source inventory/semantic-audit strategy has omissions, redundant metadata or scope problems. If a different strategy would materially improve reliability, **record a proposal or stop**, but never silently skip units or substitute a different denominator.

## 2. One-prompt campaign execution

Read `docs/research/r0_p01_successor_design/R0_P01_F1_NORMATIVE_AUDIT_BATCH_PLAN_REV03_UNFROZEN.json`, its companion `R0_P01_F1_NORMATIVE_AUDIT_INVENTORY_REV03_UNFROZEN.json`, and every applicable frozen/approved source. Validate Git branch and expected starting HEAD specified in the user-facing handoff. Confirm source hashes, the entire initial 1,022-unit inventory/batch partition and `scripts/check_r0_p01_clause_audit_receipts.py` PASS at Batch 001.

Then, **without requiring the user to issue a new prompt between ordinary batches**, perform exactly Q0-AUDIT-002, -003, ... -018 in sequence, as long as continued work is safe and substantiated. Independently examine **every assigned source unit**. For each, provide a genuinely interpreted normative meaning, actual reviewed C/R requirement associations (including `REVIEW_DERIVED_ENGINEERING` provenance where applicable), exact inherited disposition/REV04 supersession/NOT_APPLICABLE rationale, source-line or JSON-path basis, and meaningful missing test/implementation oracle concerns. Do not simply auto-accept section defaults or blanket-label policy leaves. Explicitly audit relevant normative content excluded by extraction, and identify source-unit split recommendations. Record clashes and missing requirements candidly as `PENDING`, with named concrete blockers.

Each complete batch is its own durable reviewer record in `docs/model_collaboration/threads/MC-0030/messages/`:

- Batch 002 → `035_claude_r0_p01_clause_audit_batch002.md`
- Batch 003 → `036_claude_r0_p01_clause_audit_batch003.md`
- ...
- Batch 018 → `051_claude_r0_p01_clause_audit_batch018.md`

For each batch, include the status (ACCEPT_AUDIT_BATCH### or AMEND_AUDIT_BATCH###), precise reviewed source/hash and ordered assigned count, per-unit normative meaning and evidence/correction rationale, and an exact **6-field pipe-delimited receipt** framed by unique `BEGIN_AUDIT_RECEIPT` and `END_AUDIT_RECEIPT` lines. One entry for every assigned ID, no extra IDs, no row splitting, no delimiter within fields:

```text
BEGIN_AUDIT_RECEIPT
unit_id|INHERITED_UNCHANGED|C01,R12|ACCEPTED||V02_ADDENDUM-Lnnnn;REV04_CONTRACT-Lnnnn
unit_id|SUPERSEDED_BY_REV04:REV04_CONTRACT-Lnnnn|R04|PENDING|EXACT_F1_RULE_MISSING|REV04_CONTRACT-Lnnnn
unit_id|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||SOURCE_SECTION_N;reason=historical_credential_only
END_AUDIT_RECEIPT
```

The sample above illustrates column format only; derive the actual mapping from sources. The order of fields is `unit_id|disposition|reviewed_requirement_ids|status|pending_blocker|citable_basis`. For applicable units, require an accurately source-backed R or C identifier. For genuinely inapplicable units, use NOT_APPLICABLE_TO_SUCCESSOR with reviewed IDs = "-" and exact justification. Never manufacture an unrelated requirement association just to satisfy receipt format. An ambiguous unit must remain PENDING with a blocker.

Record an explicit `Reviewer: claude-04` attestation in each batch, stating you independently read the governing source and **did not** author the source inventory, the blind second golden-vector implementation, or the independent scorer. A unit may be reviewed with PENDING status if its interpretation or tests have a real unresolved blocker. **A reviewed batch is not an F1-approved batch**. Preserve pending findings without silently repairing approved sources.

## 3. Mandatory per-batch postflight and safe persistence

Before committing a batch, independently verify **exactly** its assigned source-unit count/IDs and hashed ordered ID list. Validate every source ID against the approved/inherited committed Git blobs. Use the existing read-only `scripts/check_r0_p01_f1_audit_rev03.py`, plus `scripts/check_r0_p01_clause_audit_receipts.py` after the new message exists.

Create/commit **only the authorized message file for that batch** through the existing governed Git procedure. Verify resulting branch HEAD, committed file scope and synchronization before advancing; do not leave cross-batch unsaved results. Do not launch multiple parallel writers. The checker validates structure and completeness only; your substantive reviewer attestation is separately required.

Any audit scripts you write for calculations must be scratch/read-only and must not be committed. Do not alter the general collaboration workflow or the current project's protected authorities.

After all 17 batches (if successful), optionally publish `052_claude_r0_p01_remaining_clause_audit_summary.md` with exact coverage, all PENDING corrections, cross-batch gaps, a reconciliation-ready prioritized remediation list, and a proposal whether the original 1,022-unit granularity was worthwhile. **Do not claim all 18 semantically accepted unless every unit really is independently resolved.**

## 4. Stop conditions

**Continue** past a local review finding if the unit can be accurately marked PENDING and the next unit remains auditable. Do **not** stop merely because one control needs an ordinary prospective repair (e.g., A1/A2/A3).

**Stop, preserving completed batches and reporting the exact blocker**, for source hash drift, any lost or irreconcilable governing authority, actual conflict needing human reinterpretation of owner-approved B01/B02 or frozen Research 513 hard gates, inability to independently substantively inspect the assigned units, uncertain Git mutation/commit or inability to validate the exact receipt, owner-credential exposure concern, context/resource constraints or pressure to fabricate semantic approval. At such a stop, optionally commit a Message 052 stop summary if that is safe under the same messages-only authority. Do not count an incomplete batch as reviewed. Do not automatically retry uncertain Git mutations.

The user should need **at most one initial prompt for this campaign** under normal tool conditions, although interruption/resource limits may require a later resumption. No background completion is promised. Claude must work inside the initiated review session and never invent completion.

## 5. Explicit exclusions and handback

This is **not** authorization to implement the new harness, derive owner-private inputs, change scoring, freeze F1/F2, close B01/B02, repair or rerun Attempt 001, sign a proof, start Attempt 002, select a physical architecture or change production governance. Claude is the source-to-requirement reviewer and **will not** author the blind second independent canonicalizer, golden oracle or independent scorer.

When finished or halted, return a compact summary with the exact batch range actually committed, last public commit SHA, count of reviewed/accepted/pending units, unresolved high-risk findings and any stop reason. ChatGPT will independently retrieve committed per-batch records, qualify source and interpretation claims, decide further remediation and propose future F1 only if warranted. General manual ChatGPT–Claude collaboration remains unchanged.

```text
MC0030_MESSAGE034=ONE_PROMPT_REMAINING_SOURCE_AUDIT
NEXT_ACTOR=claude
START_BATCH=Q0-AUDIT-002
LAST_POSSIBLE_BATCH=Q0-AUDIT-018
FILES_ALLOWED=MC0030_MESSAGES_035_THROUGH_052_ONLY
CLAUSE_REVIEWER=CLAUDE_NOT_BLIND_ORACLE_AUTHOR
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
