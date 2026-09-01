# Research 107 — Post-Outage Repository Integrity Recovery Audit

**Date:** 2026-09-01  
**Status:** CLOSED / RECOVERY AUDIT COMPLETE / BOUNDED SPECIFICATION AMENDMENT REQUIRED  
**Scope:** Reconstruct the repository-preservation work spanning the Codexless continuity boundary, MC-0008, Research 106 and Specification 025 after abnormal ChatGPT task interruption; distinguish intentional transitional state from genuine defects before implementation proceeds.  
**Declared references:** `research:105`, `research:106`, `specification:025`, `checkpoint:268`, `checkpoint:269`, `path:docs/model_collaboration/threads/MC-0008/RESOLUTION.md`, `path:docs/model_collaboration/threads/MC-0008/messages/003_claude_comparative_governed_document_integrity_review.md`, `path:docs/model_collaboration/threads/MC-0008/messages/004_chatgpt_final_reconciliation_and_accepted_integrity_architecture.md`, `path:docs/CURRENT_STATE.md`, `path:docs/current_routing.json`, `path:docs/KNOWLEDGE_MAP.md`, `path:docs/CONTINUITY.md`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Why this audit exists

On 2026-08-31, a prolonged ChatGPT service incident overlapped two ADS collaboration periods. In the current persistent interaction, a long GitHub-backed task successfully committed Research 106 and Specification 025, but the conversation response then terminated at a transitional sentence before the intended implementation phase began. The preceding long-running interaction had also experienced failed/aborted ChatGPT tool output around the same period.

The project owner therefore required a recovery audit before further implementation, with an important constraint:

> Recovery must not treat every intentionally stale or deferred repository surface as outage damage. ADS was already in the middle of a staged integrity redesign, and several known inconsistencies were explicitly scheduled for post-implementation reconciliation.

This audit reconstructs what actually survived from repository authority and classifies findings before any repair.

## 2. Audit classification model

Every finding is assigned one of four classes:

```text
EXPECTED / DEFERRED
    intentionally transitional state whose repair belongs to a later frozen phase

KNOWN DEFECT / PLANNED REPAIR
    genuine defect already diagnosed before the interruption with an explicit repair point

INTERRUPTION RESIDUE
    work the interrupted task was supposed to complete but did not complete

NEW UNPLANNED DEFECT
    inconsistency or omission not part of the accepted staging plan and requiring disposition
```

The audit is therefore reconstruction and classification first, not an indiscriminate repair sweep.

## 3. Durable chronology reconstructed from Git

The relevant chronology is intact:

```text
Checkpoint 268
    permanent Source Registry migrated / verified
    first permanent corpus 20 / 20 MATCH
    source ingestion NOT STARTED
    Codexless evaluation opened

Research 105
    read-only local execution path verified
    controlled write validation still pending

Checkpoint 269
    planned chat-rotation handoff after read-only success
    controlled write still NOT YET RUN
    source ingestion still NOT STARTED

MC-0008
    deeper repository metadata/provenance/reference-integrity pressure identified
    independent Claude proposal
    ChatGPT candidate
    Claude comparative review
    five bounded amendments accepted
    architecture resolved without target-state implementation

Research 106
    normal ADS design promotion of the accepted architecture

Specification 025
    implementation boundary frozen

interrupted ChatGPT task
    stopped before validator/test implementation began
```

The Source Vault safety boundary therefore survived. No source ingestion, backup acceptance or clean-restore transition occurred during the affected period.

## 4. No hidden partial implementation

The last resolved MC-0008 architecture commit is:

```text
8508e851838f21ec10f5b0e9c34e6c7c1815e666
Resolve MC-0008 governed repository integrity architecture
```

The current design-freeze head before this audit is:

```text
851ff497261a15d7ca499b1b68e92fce70202672
Freeze repository integrity hardening design
```

The two intervening commits changed only:

```text
docs/CURRENT_STATE.md
docs/research/106_governed_repository_integrity_and_continuity_bootstrap_hardening.md
docs/specifications/025_v1_governed_repository_integrity_and_continuity_hardening.md
```

No validator, test, workflow, Source Universe implementation file or private operational artifact was partially committed. The interrupted implementation phase is therefore classified as **not started**, not partially accepted.

## 5. Research 105 and Source Vault status are not stale failures

Research 105 currently states:

```text
OPEN / READ-ONLY PATH VERIFIED / WRITE VALIDATION PENDING
```

Checkpoint 269 independently records controlled local write validation as `NOT YET RUN`.

These records agree. The write test was deliberately displaced by the repository-preservation reflection and remains unfinished. It is not outage residue to be silently completed during the integrity audit.

The permanent Source Vault also remains correctly frozen before first ingestion. This is an intentional safety boundary.

Classification:

```text
Research 105 write validation pending     EXPECTED / DEFERRED
Source Vault ingestion not started        EXPECTED / DEFERRED
```

## 6. Known canonical/routing drift remains deliberately staged

The current branch still exposes known integrity failures:

```text
CURRENT_STATE / current_routing point to Checkpoint 268 while Checkpoint 269 exists
current_routing.current_boundary is an over-specific volatile slug
Knowledge Map does not route Research 105
Knowledge Map checkpoint coverage omits 268 and 269
Research 106 and Specification 025 are not yet Knowledge Map-routed
CONTINUITY still omits itself from the direct first-read bootstrap list
DEVELOPMENT_METHOD does not yet contain the accepted aggregate/pre-transition integrity method
private CURRENT_PRIVATE_STATE is stale relative to later public Codexless evidence
```

The GitHub Knowledge Map workflow proves the first four public routing defects directly. At MC-0008 resolution commit `8508e851...`, it failed specifically for Research 105 and checkpoints 268/269. At the Research 106 / Specification 025 design-freeze commit it additionally failed for the newly created Research 106 and Specification 025.

These failures are not evidence that the outage damaged the repository. Research 106 and Specification 025 deliberately froze this order:

```text
implement
-> verify
-> canonical reconciliation
-> private continuity repair/verification
-> aggregate preflight
-> meaningful checkpoint
```

Classification:

```text
Research 105 Knowledge Map routing       KNOWN DEFECT / PLANNED REPAIR
checkpoint 268/269 topic coverage        KNOWN DEFECT / PLANNED REPAIR
live checkpoint freshness                KNOWN DEFECT / PLANNED REPAIR
volatile current_boundary                KNOWN DEFECT / PLANNED REPAIR
Research 106 / Specification 025 routing EXPECTED / DEFERRED
CONTINUITY bootstrap promotion           EXPECTED / DEFERRED
DEVELOPMENT_METHOD promotion             EXPECTED / DEFERRED
private companion freshness              KNOWN DEFECT / PLANNED REPAIR
```

None of these should be repaired before the implementation reaches the canonical-reconciliation phase unless a separate blocking requirement explicitly changes that staging.

## 7. The original metadata inventory is authoritative, and downstream summary counts drifted

MC-0008 amendment MF1 required a real family inventory before schema freeze. The successful temporary workflow run was:

```text
workflow run  33415541195
job           99565171066
commit        adce1b47011ec0cee98393c2b6ff8c5c753b0ba0
result        SUCCESS
```

The preserved job log is the authoritative raw inventory evidence. It reported:

```text
FOUNDATIONS
    files                   24
    Date                    18
    Status                  18
    Scope                   10
    no parsed bold fields    5

SPECIFICATIONS
    files                   24
    Date                    24
    Status                  24
    Scope                   23
    no parsed bold fields    0

RESEARCH
    files                  105
    Date                   105
    Status                 104
    Scope                   94
    no parsed bold fields    0

VALIDATION / EVIDENCE
    files                   15
    Date                    15
    Classification          11
    Research                11
    Status                   4
    Scope                    4
    Specification            1
    no parsed bold fields    0

COLLABORATION MESSAGES
    files                   31
    Thread                  28
    Interaction environment 28
    Interaction session     27
    no parsed bold fields    3
```

The three collaboration messages without parsed bold headers were MC-0008 Messages 001 through 003, which intentionally used the established fenced provenance representation.

Research 106 contains materially incorrect inventory counts, including claims such as Foundation `Date 24 / 24`, Specification `Status 11 / 24`, Research `Status 40 / 105`, and validation `Status 9 / 15`. Those values are not supported by the raw workflow output.

The abbreviated inventory transcription in MC-0008 Message 004 also contains at least a minor count mismatch relative to the raw log. Because Message 004 is a closed collaboration record, this audit does not rewrite it. The raw workflow log plus this correction record govern the factual inventory interpretation.

Classification:

```text
Research 106 inventory transcription     NEW UNPLANNED DEFECT
Message 004 abbreviated count mismatch   HISTORICAL TRANSCRIPTION DEFECT / CORRECTED BY THIS RECORD
```

The substantive conclusion survives unchanged: the families are heterogeneous, so a universal historical metadata schema remains rejected.

## 8. Specification 025 incorrectly treats Checkpoint 269 as future

Specification 025 states that `Checkpoint 269 is earned only by a later meaningful, verified state transition`.

That is chronologically impossible. Checkpoint 269 already existed before MC-0008 opened and is the exact frozen evidence target from which the integrity review began.

The intended rule is sound but the number is wrong:

> No checkpoint is created merely because a specification is frozen; the **next checkpoint after the already-existing 269** must be earned by a later meaningful verified transition.

Classification:

```text
future-Checkpoint-269 wording     NEW UNPLANNED DEFECT
```

## 9. Specification 025 narrows accepted relationship checking too far

MC-0008 Message 004 accepted V1 reference checking for relationships whose semantics are explicitly declared by a family contract and gave examples including:

```text
Supersedes
Superseded by
Promoted to / Promoted from
Governed by / Research / Specification where defined as artifact references
collaboration-thread references
explicit repository-local path references
canonical current pointers
```

It also explicitly said existing declared relationships should be validated when safely parseable and that free prose must not be mined heuristically.

Specification 025 introduces a good prospective generic `Declared references` field, but as written it makes that field the only generic prose-level dependency mechanism and does not preserve a bounded compatibility rule for already-existing explicit relationship fields.

This is narrower than the accepted MC-0008 architecture.

The correction is bounded:

```text
new prospective documents
    prefer the strict typed Declared references field

existing explicit relationship fields
    validate only when the complete value is unambiguously machine-resolvable
    such as a backticked repository-relative path, a single numbered artifact label,
    or a collaboration thread ID

mixed narrative values
    do not scrape or guess
```

Classification:

```text
existing declared-relationship compatibility omission     NEW UNPLANNED DEFECT
```

## 10. The private-companion synchronization pointer was dropped

Claude's comparative Amendment G explicitly split private hardening into two pieces:

```text
private-side pointer recording the public checkpoint last reconciled against
    MUST_DO_NOW

more involved private checker / universal preflight reachability
    SHOULD_DO_LATER pending environment availability
```

MC-0008 Message 004 then accepted a minimal separate private continuity mechanism and stated that later implementation should define a durable public-safe synchronization token or checkpoint relationship.

Specification 025 preserves `PASS / FAIL / NOT_VERIFIED`, which is correct, but does not freeze the required private-side synchronization pointer itself.

That omission would make `PRIVATE_CONTINUITY_INTEGRITY` underspecified.

The smallest contract is to extend the existing private routing surface rather than create a new registry:

```text
CURRENT_PRIVATE_STATE.md
    Public continuity checkpoint: <positive integer>
    Public continuity commit: <40-hex public commit SHA>
```

These values are public-safe by definition. They reveal no private paths or secrets. A private continuity check can compare them with the public boundary it claims to complement. Public CI remains unable to assert private freshness when it cannot access that file.

Classification:

```text
private synchronization pointer omission     NEW UNPLANNED DEFECT
```

## 11. Explicit title/header identity agreement needs to survive promotion

MC-0008 Message 004 also required filename/header identity agreement wherever a family contract declares an explicit identity.

Specification 025 freezes filename-derived uniqueness but does not state the corresponding agreement rule.

The bounded rule is:

```text
if the H1 explicitly declares a governed family + numeric identity
    that identity must equal the filename-derived identity

if the H1 does not declare such an identity
    do not manufacture one
```

This does not require historical header normalization.

Classification:

```text
explicit header/filename identity-agreement omission     NEW UNPLANNED DEFECT
```

## 12. Disposable Codexless-chat provenance repair remains a known obligation

Checkpoint 269 incorrectly promoted the fresh Codexless plug-in validation chat to canonical persistent `chatgpt-12`.

MC-0008 later corrected that interpretation: the plug-in test chat was disposable; the canonical persistent interaction remained `chatgpt-11` until the current real persistent session was opened and correctly allocated as `chatgpt-12`.

The technical Codexless read-path evidence is still valid.

The provenance wording in Checkpoint 269 remains intentionally unrepaired at this pre-implementation stage. However, the later canonical reconciliation must explicitly correct it rather than allowing a generic stale-reference cleanup to overlook it.

Classification:

```text
Checkpoint 269 disposable-chat provenance     KNOWN DEFECT / PLANNED REPAIR
```

## 13. Abnormal execution interruption is itself a continuity failure mode worth governing

The outage exposed a Level-2 process weakness not previously stated explicitly.

A tool-backed task can terminate after some durable writes have completed but before later writes, verification, reconciliation or the final completion report. The correct recovery behavior is not to trust the interrupted conversation's completion implication and not to rerun the entire plan blindly.

Accepted recovery principle:

> After an abnormal execution interruption, provider outage, tool failure, unexplained termination or user interruption during a multi-step repository mutation, reconstruct the operation from the last durable repository boundary and classify intended-versus-completed work before further mutation.

Minimum recovery sequence:

```text
1. read current branch HEAD
2. identify the last independently trusted durable boundary
3. enumerate commits/files/actions that actually completed after it
4. compare them with the intended staged plan
5. classify each apparent inconsistency as expected/deferred, known planned repair,
   interruption residue, or new unplanned defect
6. repair only what belongs at the current stage
7. rerun the required verification rather than inheriting a pre-interruption success claim
8. preserve the recovery result when it materially affects project continuity
```

A normal user interruption is not itself repository corruption. Completed Git operations remain durable. The rule exists to prevent a partially completed logical workflow from being mistaken for a completed transition.

This principle should be promoted into `CONTINUITY.md` and `DEVELOPMENT_METHOD.md` during the already-planned canonical reconciliation, not inserted early by bypassing the frozen staging sequence.

## 14. Audit disposition

The audit finds **no evidence of Source Vault corruption, hidden partial implementation, or loss of the MC-0008 design chain**.

It does find several correctable design-freeze defects in the outage-affected Research 106 / Specification 025 promotion:

```text
1. incorrect metadata inventory transcription
2. future-Checkpoint-269 numbering error
3. missing compatibility rule for existing explicit declared relationships
4. missing private-side public continuity pointer contract
5. missing explicit H1/filename identity-agreement rule
6. canonical reconciliation checklist must explicitly retain the Checkpoint 269 provenance repair
7. new abnormal-interruption recovery rule should be promoted during reconciliation
```

These findings do not justify early Knowledge Map/current-routing/private-state repair. They justify one bounded specification amendment before implementation.

## 15. Next legitimate step

Proceed through a narrow amendment that:

```text
- preserves Specification 025 as the outage-affected frozen base;
- corrects only the confirmed implementation-contract defects above;
- leaves known canonical/routing/private reconciliation at its already-frozen later stage;
- then implements Specification 025 as amended;
- verifies the implementation at integrated risk tier;
- only afterward performs canonical and private reconciliation.
```

This preserves chronology, avoids silent rewriting of a frozen contract, and gives the post-outage recovery a durable auditable boundary.