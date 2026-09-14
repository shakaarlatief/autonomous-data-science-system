# Research 168: Integrated Q1 + Q2 + Q5 Fresh-Collaborator Result and Revision-Binding Amendment

**Date:** 2026-09-14
**Status:** INTEGRATED FRESH-COLLABORATOR SHADOW SUPPORT PASSED / EXPLICIT CAPTURE PROMOTION PASSED / SOURCE-REVISION BASIS AMENDMENT REQUIRED / Q4 REAL STRESS NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate:** `PKA-CANDIDATE-01`
**Qualification clusters:** Q1 + Q2 + Q5
**Fixture freeze commit:** `06a6e2e3aea325df5424174d0e87e7555b701428`
**Exact real base:** `f5996aed3710c63e1ba859ee248c264abd678636`
**Scope:** Preserve the manually run fresh collaborator result, evaluate it against the separately frozen oracle, perform the explicit post-capture promotion review, promote the accepted synthesis only inside the Candidate 01 shadow, and incorporate the source-revision basis defect exposed by the collaborator.
**Authority:** Integrated shadow evidence only. Current continuity remains operational authority. No Source Vault write, production authority mutation, final requirement pass, or target selection occurs.
**Declared references:** `research:167`, `research:166`, `research:145`, `checkpoint:512`

## 1. Fresh collaborator provenance

The project owner ran the frozen request manually in a fresh Codex thread inside the ADS project rather than using the prepared Codexless agent call. The output was written only to the authorized result path.

```text
FRESH_COLLABORATOR_RESULT_V01.json
    SHA-256  ccbaa542d3c522d0a6460eb20ba5784ba9fde419a7764043671370a9ec80d448

FIRST_RUN_FRESH_COLLABORATOR_RESULT_V01.json
    SHA-256  ccbaa542d3c522d0a6460eb20ba5784ba9fde419a7764043671370a9ec80d448

collaborator result repair     none
```

The exact engine/thread identifier was not preserved in the result schema. Therefore this run is valid evidence for conversation independence, but it is **not** used as provider/tool-portability evidence for KA-R36.

## 2. Bounded fresh reconstruction result

The fresh collaborator used exactly the nine allowed evidence reads and zero forbidden legacy bootstrap reads.

```text
evidence reads                          9 / 9 maximum
frozen-manifest evidence bytes         35,438
legacy CURRENT_STATE reads              0
legacy current_routing reads            0
legacy KNOWLEDGE_MAP reads              0
previous conversation dependency        none by experiment contract
```

The collaborator successfully reconstructed that the active project-knowledge route and the paused Source Vault route are distinct, and that Source Vault execution may resume only after explicit project routing returns to that workstream.

## 3. Consequential authority task

For the question “May Course 2 be admitted now?”, the collaborator correctly resolved:

```text
decision              BLOCKED
governing procedure   docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
workstream             WS-SOURCE-VAULT-BOOTSTRAP
```

It used Validation 003 and Validation 004 as evidence, while correctly rejecting Checkpoint 274 as a historical distractor rather than current admission authority.

All five required blocker concepts were surfaced:

```text
SOURCE_INGESTION_NOT_STARTED
WORKING_STORE_AUDIT_PENDING
INDEPENDENT_BACKUP_ROUND_TRIP_PENDING
CLEAN_RESTORE_PENDING
RESTORED_INTEGRITY_AUDIT_PENDING
```

The three frozen source-owned reopen risks were also activated:

```text
RK-RECOVERY-FAILURE
RK-REMOTE-ROUNDTRIP-FAILURE
RK-PRIVATE-LEAK
```

No Source Vault or Source Registry write occurred.

## 4. Stale derived authority fails visibly

`STALE-VIEW-COURSE2-01` was rejected as an authority source because its declared binding is stale and mismatched. The collaborator did not silently repair the digest, average the stale claim with the runbook, or treat repeated derived storage as authority.

```text
STALE_AUTHORITY_VIEW=FAIL_VISIBLE
SOURCE_BINDING_MISMATCH=SURFACED
DERIVED_VIEW_OVERRIDE=REJECTED
```

This is direct integrated support for uncertainty visibility and action-shaped authority resolution.

## 5. Preserved evaluator history

The collaborator itself passed without repair. The local evaluator required two repairs, both preserved as evaluator provenance rather than attributed to the collaborator.

The first evaluator compared Windows checkout raw bytes directly with an earlier Git-blob base and therefore conflated line-ending transformation/checkpoint progression with authority mutation. The second switched to Git diff semantics but still compared against the pre-fixture real base instead of the committed fixture-freeze HEAD. The final evaluator correctly checks post-freeze working-tree mutation.

```text
FIRST_RUN_EVALUATION_V01       failed only current_authority_unchanged
SECOND_RUN_EVALUATION_V01      failed only current_authority_unchanged
FRESH_COLLABORATOR_EVALUATION  25 / 25 PASS
SHA-256                         affc0811870523b972ad23a32c2774e639dccc91840ddacb9553931c02682c4e
```

## 6. Explicit capture -> review -> promotion

The collaborator produced one generalized insight as `CAPTURED_NON_AUTHORITATIVE`:

> A consequential admission decision needs separate checks for governing-source binding, permission to resume the relevant workstream, and completion evidence for the operational gate. Success in one check cannot stand in for another: matching intake fingerprints do not prove recovery, a historical resume record does not establish present routing, and a repeated readiness claim cannot repair an invalid source binding.

The insight did **not** become authority when captured. A separate task-owner promotion review then checked:

```text
COLLABORATOR_RESULT_VALID                 PASS
SOURCE_TRACEABLE                          PASS
NON_CONFLICTING                           PASS
MATERIAL_SYNTHESIS                        PASS
EXPLICIT_REVIEW_DECISION_ACCEPT           PASS
```

The review at SHA `121e76e7f29624234919ee52f12c3558a16175b3845e32dfbaafe3ef25f1990c` explicitly accepted the synthesis only for Candidate 01 shadow promotion. `SHADOW_PROMOTED_KNOWLEDGE_V01.md` at SHA `e773834e5f88c5d409eae37b84152e53d53e8b208e8d8a1105800bb90d3815f5` preserves the statement and exact source basis. It remains `shadow_only=true` and `current_project_authority=false`.

This is the first real fresh-collaborator execution of the full Candidate 01 capture boundary:

```text
EMPTY_BEFORE_COLLABORATOR_RUN
-> CAPTURED_NON_AUTHORITATIVE
-> EXPLICIT REVIEW
-> PROMOTED_WITHIN_CANDIDATE_01_SHADOW
```

## 7. Source-revision binding defect exposed by the fresh collaborator

The most valuable unexpected finding was not an oracle failure. The authority index stored:

```text
sha256 = fdcb795d...
```

That digest exactly matches the canonical Git blob at the frozen base. On the Windows checkout, Git line-ending transformation materializes the same Markdown source with CRLF bytes, whose raw SHA-256 is different. Replacing CRLF with LF reproduces the indexed digest.

The collaborator correctly disclosed this rather than pretending the checkout raw bytes matched the index.

The frozen receipt still passes its oracle because the request explicitly required the SHA from the authority index. However, Candidate 01's design was underspecified: a bare `sha256` field does not say **what representation was hashed**.

### Revision-binding amendment

Future persistent authority indexes and receipts must use an explicit source-revision descriptor, conceptually:

```text
source_commit
source_path
hash_algorithm
hash_basis
content_digest
```

For tracked repository authority, the default basis is:

```text
hash_basis = GIT_BLOB_BYTES_AT_COMMIT
```

Validation must resolve the exact Git blob at `source_commit:source_path` and hash those bytes. It must not infer that a working-tree raw-byte difference is semantic freshness drift when checkout filters or line-ending conversion explain the representation change.

If a use case genuinely requires working-tree raw bytes or canonicalized text, that basis must be declared explicitly. Validators must never guess normalization rules after a mismatch.

This amendment strengthens KA-R08 and KA-R23 and is relevant to KA-R36 portability. The current experiment does not claim KA-R36 because exact collaborator engine provenance and cross-provider execution were not preserved.

## 8. Integrated result

```text
FINAL_INTEGRATED_RESULT_V01.json
    SHA-256  82ceb42e979ca979ec08f6e3c8ae55abec13e8a4f3b7091ed1e696339e1dc183

final checks                       11 / 11 PASS
collaborator repairs                0
evaluator repairs                   2
focused integrated tests           11 / 11 PASS
exhaustive partitioned unit suite 282 / 282 PASS
read budget                         9 reads / 35,438 frozen bytes
legacy bootstrap reads              0
Course 2 decision                   BLOCKED
stale derived authority             FAIL_VISIBLE
risk activation                     PASS
authority receipt                   PASS with revision-basis amendment
capture non-authoritative first     PASS
explicit promotion                  PASS
current authority mutation          none
```

## 9. Evidence disposition

This result adds real fresh-collaborator support for persistent understanding, conversation independence, relevant governing/risk discovery, known-risk activation, uncertainty visibility, action-shaped authority resolution, source-traceable promoted synthesis and the capture/promotion boundary.

The qualification matrix now records:

```text
real-evidence items                58 / 67
synthetic-or-better items          63 / 67
final qualified passes              0 / 67
full-real subsystem clusters       Q3 Q5 Q6 Q7 Q8 Q9
mixed-gap clusters                 Q1 Q2 Q4
```

Q1 remains short of full-real evidence because provider/tool portability is not established. Q2 still retains real hard-case gaps around conflict/supersession/retrieval semantics despite this strong consequential task.

## 10. Next falsification

Research 166 placed Q4 after the integrated Q1/Q2/Q5 challenge. That remains correct. Q4 is now the cleanest remaining real-behavior gap:

```text
real multi-dependency workstream DAG
real interruption recovery after unrelated work
real stale concurrent authoritative update rejection
```

The next fixture should use actual ADS workstreams and a frozen expected-revision conflict, not synthetic labels alone. It must preserve the current authority model and must not create a real conflicting write merely for the test.

```text
RESEARCH168=INTEGRATED_Q1_Q2_Q5_SHADOW_SUPPORT_PASS
FRESH_COLLABORATOR=PASS_WITHOUT_REPAIR
EVALUATION=25_OF_25
FINAL=11_OF_11
CAPTURE_PROMOTION=PASS
SOURCE_REVISION_BASIS_AMENDMENT=REQUIRED_AND_ACCEPTED
REAL_EVIDENCE_ITEMS=58_OF_67
FINAL_QUALIFIED_PASSES=0
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=Q4_REAL_WORKSTREAM_CONCURRENCY_INTERRUPTION_STRESS
```
