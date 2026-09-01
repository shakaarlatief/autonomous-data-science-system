# Specification 026 — V1 Repository Integrity Recovery Amendment

**Date:** 2026-09-01  
**Status:** FROZEN / AMENDS SPECIFICATION 025 / IMPLEMENTATION PENDING  
**Scope:** Correct the bounded implementation-contract defects found by the post-outage recovery audit without prematurely performing the canonical/routing/private reconciliation deliberately deferred by Specification 025.  
**Declared references:** `research:107`, `research:106`, `specification:025`, `checkpoint:269`, `path:docs/model_collaboration/threads/MC-0008/RESOLUTION.md`, `path:docs/model_collaboration/threads/MC-0008/messages/003_claude_comparative_governed_document_integrity_review.md`, `path:docs/model_collaboration/threads/MC-0008/messages/004_chatgpt_final_reconciliation_and_accepted_integrity_architecture.md`, `path:docs/private_companion/README.md`

## 1. Amendment relationship

Specification 025 remains the base implementation contract for V1 governed repository integrity and continuity hardening.

This specification is a narrow recovery amendment created after an abnormal ChatGPT execution interruption prompted a repository-first quality audit.

Rules:

```text
Specification 025 remains in force except where this amendment explicitly corrects or extends it.
If an explicit conflict exists, Specification 026 governs that point.
No canonical routing, Knowledge Map, CURRENT_STATE, CONTINUITY, DEVELOPMENT_METHOD,
private-companion or Source Vault repair is authorized merely by freezing this amendment.
```

Implementation must satisfy Specifications 025 and 026 together.

## 2. Authoritative metadata-inventory evidence

The authoritative MC-0008 raw inventory evidence is the successful temporary workflow output at:

```text
run     33415541195
job    99565171066
commit  adce1b47011ec0cee98393c2b6ff8c5c753b0ba0
```

Its relevant counts are:

```text
Foundations          24 files | Date 18 | Status 18 | Scope 10 | no parsed bold fields 5
Specifications       24 files | Date 24 | Status 24 | Scope 23 | no parsed bold fields 0
Research            105 files | Date 105 | Status 104 | Scope 94 | no parsed bold fields 0
Validation/evidence  15 files | Date 15 | Classification 11 | Research 11 | Status 4 | Scope 4
Collaboration        31 files | Thread 28 | Interaction environment 28 | Interaction session 27
                                  | no parsed bold fields 3
```

The three fieldless collaboration results under the generic bold-header parser were MC-0008 Messages 001 through 003, which use the accepted fenced provenance representation.

Any conflicting abbreviated count in Research 106 or MC-0008 Message 004 is a transcription error and MUST NOT drive implementation behavior.

This correction does not change the substantive conclusion: historical family heterogeneity is demonstrated and no universal legacy schema is authorized.

## 3. Checkpoint chronology correction

Specification 025 Section 11 must be read as:

> A new checkpoint MUST NOT be created merely because Specification 025 or this amendment was frozen. Checkpoint 269 already predates MC-0008. The next checkpoint after 269 must be created only for a later meaningful, verified state transition.

No recovery-audit checkpoint is required merely because Research 107 / Specification 026 exist.

## 4. Existing declared-relationship compatibility

Specification 025's prospective `Declared references` field remains the preferred generic mechanism for new governed documents.

It is not the only relationship-existence surface covered by the accepted MC-0008 V1 architecture.

The implementation MUST also validate an existing explicit relationship field when, and only when, the complete field value is unambiguously machine-resolvable under one of these forms:

```text
1. a single backticked repository-relative path
2. a single numbered artifact label:
       Foundation N
       Specification N
       Research N
       Checkpoint N
3. a single collaboration thread identity:
       MC-NNNN
```

Candidate existing relationship-field names include:

```text
Supersedes
Superseded by
Promoted to
Promoted from
Governed by
Research
Specification
Companion collaboration thread
Companion thread
```

The implementation MUST NOT infer a dependency from a mixed narrative value merely because it contains an artifact-looking number or path.

Examples:

```text
**Promoted from:** `docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md`
    -> validate exact path existence

**Promoted by:** Checkpoint 143 after the frozen v0.1 RH-C contract passed ...
    -> mixed narrative; do not heuristically mine a generic dependency

ordinary body prose mentioning Research 105
    -> ignored by generic relationship validation
```

A safely parseable existing field that declares a target MUST fail when its target does not exist.

This compatibility rule restores the accepted MC-0008 relationship-existence scope without introducing free-prose scraping or a general dependency graph.

## 5. Filename and explicit H1 identity agreement

Family-scoped filename uniqueness remains required by Specification 025.

Additionally:

```text
IF a numbered governed document's H1 explicitly declares both its family and numeric identity
THEN that H1 identity MUST equal the filename-derived identity.

IF the H1 does not explicitly declare a family numeric identity
THEN no identity is inferred from unrelated title prose.
```

Recognized family labels are:

```text
Foundation
Specification
Research
Checkpoint
```

This check is strict when the explicit H1 form exists and requires no mass historical header migration.

Required tests:

```text
matching filename/H1 identity -> PASS
mismatching explicit filename/H1 identity -> FAIL
H1 without explicit governed numeric identity -> no manufactured failure
```

## 6. Private-side public continuity anchor

The accepted private-companion synchronization pointer is restored as a MUST-DO-NOW contract.

The existing private routing file is extended rather than introducing a new registry or sidecar system:

```text
autonomous-data-science-system-private/CURRENT_PRIVATE_STATE.md

**Public continuity checkpoint:** <positive integer>
**Public continuity commit:** <40 lowercase hexadecimal public ADS commit SHA>
```

Semantics:

```text
Public continuity checkpoint
    the public checkpoint boundary against which the current private continuity content
    was last deliberately reconciled

Public continuity commit
    the exact public ADS commit inspected/reconciled when that private anchor was written
```

These are public-safe values. They MUST NOT contain private paths, secrets or machine identifiers.

A private continuity checker MUST be able to evaluate an accessible private routing file against an expected public checkpoint/commit and report:

```text
PASS
    both anchor values are present, valid and equal to the required public reconciliation target

FAIL
    the private file is accessible but the required anchor is malformed, missing, or does not match

NOT_VERIFIED
    the verification surface cannot access the private companion or was not supplied an
    accessible private state surface
```

Public CI MUST NOT fabricate `PASS` when the private repository is inaccessible.

The public repository MAY contain the checker implementation and tests because the contract itself contains no private values. Actual private values remain in the private repository.

## 7. Chat-rotation preflight clarification

Specification 025's `PASS / HOLD / FAIL` preflight remains correct.

The private anchor above gives `PRIVATE_CONTINUITY_INTEGRITY` a concrete minimal basis when private state is accessible.

Required behavior remains:

```text
public PASS + private required but inaccessible
    PRIVATE_CONTINUITY_INTEGRITY=NOT_VERIFIED
    CHAT_ROTATION_PREFLIGHT=HOLD

public PASS + accessible private anchor mismatch
    PRIVATE_CONTINUITY_INTEGRITY=FAIL
    CHAT_ROTATION_PREFLIGHT=FAIL

public PASS + accessible required private anchor match + no other open transition obligation
    private component may PASS
    rotation may PASS if every other required component passes
```

The implementation does not need to make private access universal. Environment reachability remains separate from the pointer contract.

## 8. Explicit Checkpoint 269 provenance reconciliation obligation

The later canonical reconciliation MUST explicitly address the known Checkpoint 269 provenance defect:

```text
the fresh Codexless plug-in validation chat was disposable
it was not canonical persistent chatgpt-12
the technical read-path evidence remains valid
the canonical persistent session remained chatgpt-11 until the actual current
persistent interaction was opened and allocated as chatgpt-12
```

The repair MUST be transparent and metadata/provenance-only. It MUST NOT rewrite Checkpoint 269 to pretend that later technical or architectural results were already known at checkpoint creation.

This obligation was already accepted by MC-0008 and is made explicit here so generic canonical cleanup cannot omit it.

## 9. Abnormal-interruption recovery protocol

The later `CONTINUITY.md` / `DEVELOPMENT_METHOD.md` reconciliation MUST add a bounded abnormal-execution recovery rule.

After an outage, tool failure, unexplained task termination or user interruption during a multi-step repository mutation:

```text
1. inspect current branch HEAD before further mutation
2. identify the last independently trusted durable boundary
3. enumerate what actually committed/completed after that boundary
4. compare completed work with the intended staged plan
5. classify apparent inconsistencies as:
       EXPECTED / DEFERRED
       KNOWN DEFECT / PLANNED REPAIR
       INTERRUPTION RESIDUE
       NEW UNPLANNED DEFECT
6. repair only findings appropriate to the current stage
7. rerun required verification rather than inheriting interrupted completion claims
8. preserve a recovery record when the interruption materially affects continuity
```

The protocol MUST state that a user interruption is allowed and does not itself imply Git corruption. Its purpose is to prevent partial logical workflows from being mistaken for completed transitions.

## 10. Canonical reconciliation remains deferred

This amendment does not move forward the reconciliation step.

The following remain deliberately deferred until implementation plus the strongest required verification are complete:

```text
CURRENT_STATE current-checkpoint/latest-specification repair
current_routing synchronization and current_boundary replacement
Knowledge Map routing for Research 105, Research 106, Research 107,
Specification 025 and Specification 026
checkpoint semantic range repair for 268 and 269
CONTINUITY bootstrap promotion
DEVELOPMENT_METHOD integrity/recovery promotion
Checkpoint 269 disposable-chat provenance correction
private companion freshness repair and anchor write
final public/private/preflight claims
```

This list distinguishes intentional staging from outage damage.

## 11. Implementation acceptance additions

In addition to every Specification 025 acceptance condition, implementation MUST now demonstrate:

```text
1. exact behavior is not derived from the incorrect downstream inventory summary counts;
2. safe compatibility checking exists for unambiguous existing explicit relationship fields;
3. explicit H1/filename identity mismatch is detected;
4. private continuity anchor parsing/comparison supports PASS / FAIL / NOT_VERIFIED;
5. tests cover those three additions;
6. canonical reconciliation explicitly corrects the Checkpoint 269 disposable-chat provenance;
7. canonical reconciliation promotes the abnormal-interruption recovery protocol;
8. no early canonical/private/Source Vault mutation was used to make pre-implementation checks appear green.
```

## 12. Next action

The next legitimate action after this amendment is implementation of Specification 025 **as amended by Specification 026**.

Implementation should reuse existing focused validators and shared helpers, remain family-aware and prospective, and preserve the already-frozen post-implementation reconciliation sequence.