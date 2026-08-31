# Research 106 — Governed Repository Integrity and Continuity Bootstrap Hardening

**Date:** 2026-08-31  
**Status:** CLOSED / DESIGN ACCEPTED FOR IMPLEMENTATION  
**Scope:** Repository artifact identity, prospective metadata, live-routing freshness, explicit new-session bootstrap authority, public/private integrity separation, and chat-rotation readiness.  
**Declared references:** `research:103`, `research:104`, `specification:024`, `checkpoint:268`, `path:docs/CONTINUITY.md`, `path:docs/DEVELOPMENT_METHOD.md`, `path:docs/README.md`, `path:docs/current_routing.json`, `path:docs/CURRENT_STATE.md`, `path:docs/KNOWLEDGE_MAP.md`, `path:docs/model_collaboration/threads/MC-0008/RESOLUTION.md`, `path:docs/model_collaboration/threads/MC-0008/messages/004_chatgpt_final_reconciliation_and_accepted_integrity_architecture.md`

## Question

As the Autonomous Data Science System repository grows across hundreds of durable knowledge artifacts, checkpoints, validation records, collaboration threads, source-universe evidence, frontend experiments and implementation history, what is the smallest governed integrity architecture that makes repository reconstruction increasingly reliable without turning the repository into a second metadata system that must itself be manually synchronized?

A second question emerged empirically during the `chatgpt-12` reconstruction on 2026-08-31:

> If a canonical continuity procedure is bootstrap-critical, is it sufficient for the structural repository guide to route a new collaborator toward that procedure, or must the initial reconstruction contract enumerate the procedure directly?

The investigation is preventive hardening. It is not evidence that the repository is substantively corrupted or that the existing preservation architecture has failed. The repository already contains strong authority separation, current-state routing, a global Knowledge Map, checkpoint metadata validation, collaboration-state validation and durable decision history. The purpose here is to remove failure modes that become more likely as the corpus continues to scale.

## Inputs

This research consolidates the accepted MC-0008 integrity review and one additional live reconstruction observation.

Primary inputs:

```text
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/model_collaboration/threads/MC-0008/RESOLUTION.md
docs/model_collaboration/threads/MC-0008/messages/003_claude_comparative_governed_document_integrity_review.md
docs/model_collaboration/threads/MC-0008/messages/004_chatgpt_final_reconciliation_and_accepted_integrity_architecture.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/README.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

The MC-0008 resolution accepted the architecture for normal ADS governance and required five refinements before implementation:

```text
MF1  full metadata inventory before schema freeze
MF2  branch-scoped freshness
MF3  explicit validator test matrix
MF4  preventive-hardening framing
MF5  public/private integrity claim separation
```

All five are incorporated below.

## Existing strengths that must be preserved

The current repository already separates several authority concerns correctly:

```text
docs/README.md
    repository structure and artifact roles

docs/current_routing.json
    compact machine-readable live pointer

docs/CURRENT_STATE.md
    human-readable live state and exact next step

docs/KNOWLEDGE_MAP.md
    evergreen semantic subject retrieval

docs/CONTINUITY.md
    reconstruction and recovery procedure

docs/DEVELOPMENT_METHOD.md
    development, verification, review and preservation method

Git history
    exact implementation chronology

checkpoints
    meaningful historical state boundaries

private companion repository
    durable private continuity complement only

.ads-private
    machine-local execution configuration
```

The hardening must reinforce these boundaries rather than centralize them into a new universal registry.

## Metadata inventory

The pre-freeze inventory established that existing families are intentionally heterogeneous:

```text
Foundations
    24 files
    Date    24 / 24
    Status   5 / 24
    Scope    1 / 24

Specifications
    24 files
    Date    24 / 24
    Status  11 / 24
    Scope    6 / 24

Research
    105 files
    Date    105 / 105
    Status   40 / 105
    Scope     7 / 105

Checkpoints
    169 files
    existing checkpoint schema already governs this family

Validation / evidence
    15 files
    Date            15 / 15
    Status           9 / 15
    Classification   2 / 15
    Research        11 / 15

Model-collaboration messages
    33 files
    only 18 / 33 use the counted bold-header representation
    fenced provenance is intentional and must remain valid
```

This inventory rejects a universal Markdown metadata schema. Retrofitting all historical files would create churn, obscure chronology and make validation dependent on a large one-time rewrite whose scientific value is negligible.

## Artifact classes

Integrity is family-aware rather than universal.

```text
A. live canonical state
   CURRENT_STATE.md + current_routing.json

B. numbered durable knowledge
   foundations / specifications / research

C. checkpoints
   existing checkpoint metadata contract

D. validation and evidence
   heterogeneous result/evidence records with a prospective minimum contract

E. model collaboration
   existing JSON/thread/message contracts, including fenced provenance

F. specialized ledgers and indexes
   domain-specific contracts where already justified

G. global prose, code and Git history
   no generic Markdown schema
```

Numeric identity is scoped to the numbered family.

Therefore:

```text
duplicate research 106          INVALID
duplicate specification 025     INVALID
research 106 + checkpoint 106   VALID
research 106 + specification 106 VALID
```

A globally unique number would conflate independent historical namespaces that were never designed to share one counter.

## Prospective metadata contract

The accepted design is prospective. Existing documents remain valid unless a separate substantive reason justifies migration.

Cutover boundaries are deterministic from the already-consumed family counters:

```text
Foundation    IDs >= 025 require the prospective contract
Specification IDs >= 025 require the prospective contract
Research      IDs >= 106 require the prospective contract
Checkpoint    existing checkpoint validator remains authoritative
```

Required metadata for newly governed numbered durable knowledge:

```text
Foundation
    Date
    Status
    Scope

Specification
    Date
    Status
    Scope

Research
    Date
    Status
    Scope
```

The validator must not infer status or scope from prose.

### Validation/evidence cutover

Validation/evidence files do not have a reliable family-wide numeric cutover. The accepted mechanism is therefore a one-time immutable compatibility snapshot of the exact validation/evidence paths that existed before this prospective contract.

Properties of the snapshot:

```text
- it is migration-boundary data, not a hand-maintained artifact registry;
- existing listed paths remain legacy-compatible;
- any later validation/evidence path not in the snapshot must satisfy the prospective minimum contract;
- renaming a legacy file does not silently grant legacy status to the new path;
- adding a file to the compatibility snapshot during ordinary development is not an accepted bypass;
- Git history need not be fetched in CI merely to determine whether a file predates the cutover.
```

Prospective validation/evidence minimum:

```text
Date
one result field:
    Status OR Classification
one governed anchor:
    Research OR Specification OR Scope
```

`Scope` is allowed as the governed subject anchor when neither Research nor Specification is semantically appropriate.

## Declared references

Repository integrity should validate references that authors intentionally declare, not scrape arbitrary prose and guess whether a number or path is normative.

The exact optional field is frozen as:

```text
**Declared references:** `research:104`, `specification:024`, `checkpoint:268`, `path:docs/CONTINUITY.md`
```

Allowed reference types:

```text
foundation:N
specification:N
research:N
checkpoint:N
path:REPO_RELATIVE_PATH
```

Rules:

```text
- only the exact Declared references field is parsed by the generic validator;
- absence of the field is valid;
- numbered references resolve within their own family;
- path references must be repository-relative;
- absolute paths are rejected;
- traversal such as ../ is rejected;
- malformed typed references are rejected;
- ordinary prose, code blocks and historical numbers are never heuristically interpreted as declared dependencies.
```

Existing collaboration-specific reference/provenance contracts remain separate when they are stronger or structurally different. The generic field does not replace the collaboration validator.

## Live-state integrity

`CURRENT_STATE.md` and `current_routing.json` must continue to agree on overlapping live facts. Agreement alone, however, is insufficient because two files can be consistently stale.

The strengthened live-state contract adds branch-scoped freshness:

```text
if checked branch == current_routing.active_development_branch:
    current_checkpoint must equal the maximum numbered checkpoint present in that checked branch tree

if checked branch != active_development_branch:
    that unrelated branch does not make the active branch stale
```

This avoids a false global invariant in a repository where historical and experimental branches legitimately contain different checkpoint populations.

The checker must receive or deterministically resolve the checked branch rather than silently guessing from unrelated remote branch state.

### Stable current boundary

`current_boundary` is a machine-readable semantic routing label, not a second checkpoint title.

The accepted syntax is:

```text
^[a-z]+(?:-[a-z]+)*$
maximum length: 64 characters
```

Consequences:

```text
repository-integrity-hardening      VALID
source-vault-bootstrap              VALID
checkpoint-268-...                  INVALID
research-106-...                    INVALID
2026-08-31-...                      INVALID
```

Digits are intentionally excluded so checkpoint/research/specification identifiers cannot be smuggled into a field intended to remain stable across nearby historical transitions.

## Explicit new-session bootstrap authority

The `chatgpt-12` reconstruction exposed a small but important continuity weakness.

The standard continuation prompt directly required:

```text
README.md
docs/README.md
docs/current_routing.json
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

`docs/README.md` correctly routes context-loss reconstruction to `docs/CONTINUITY.md`. Therefore the architecture was logically sufficient for a careful collaborator to discover the continuity procedure. However, in the live reconstruction it was not possible to verify reliably that `docs/CONTINUITY.md` itself had been explicitly opened before the user asked about it.

This is a bootstrap problem rather than a substantive knowledge-loss problem.

Accepted principle:

> A document that governs how the bootstrap itself is performed must be directly enumerated by the bootstrap contract. Bootstrap-critical authority must not depend on a semantic routing hop.

The mandatory first-read sequence therefore becomes:

```text
1. README.md
2. docs/README.md
3. docs/CONTINUITY.md
4. docs/current_routing.json
5. docs/CURRENT_STATE.md
6. docs/KNOWLEDGE_MAP.md
```

`CONTINUITY.md` may then route the collaborator onward to governing specifications, current checkpoints, specialized ledgers and private companion state exactly as before.

The standard continuation prompt must enumerate `docs/CONTINUITY.md` explicitly.

This change is deliberately small. It does not duplicate live state inside `CONTINUITY.md` and does not weaken `docs/README.md` as the structural router.

## Public and private integrity are separate claims

The public repository cannot truthfully prove freshness of private companion knowledge or machine-local `.ads-private` state when those surfaces are inaccessible to the current execution environment.

Therefore there are two distinct aggregate results:

```text
PUBLIC_REPOSITORY_INTEGRITY
    PASS | FAIL

PRIVATE_CONTINUITY_INTEGRITY
    PASS | FAIL | NOT_VERIFIED
```

`NOT_VERIFIED` means exactly that the current verification surface did not prove private continuity. It must not be converted into `FAIL`, and it must not convert public `RESOLVED_PRIVATE` facts back into `UNRESOLVED`.

The public aggregate may verify only public facts.

## Chat rotation preflight

A separate transition-oriented result combines the integrity surfaces needed before deliberately rotating a long ADS conversation:

```text
CHAT_ROTATION_PREFLIGHT
    PASS | HOLD | FAIL
```

Interpretation:

```text
PASS
    public integrity passes and every continuity surface required for this rotation is verified sufficiently

HOLD
    public integrity passes, but a required private continuity surface is NOT_VERIFIED or another non-failure transition obligation remains open

FAIL
    a required public or verified-private integrity condition fails
```

A `HOLD` is not a repository-integrity failure. It prevents a stronger rotation-ready claim until the missing transition evidence is obtained.

The preflight considers at least:

```text
public repository integrity
live-state synchronization and freshness
model-collaboration state
required private continuity status when relevant
branch / working-state requirement appropriate to the transition
```

## Public aggregate gate

The first public aggregate is intentionally bounded:

```text
PUBLIC_REPOSITORY_INTEGRITY
    numbered-family identity
    prospective family metadata
    Knowledge Map integrity
    live-state synchronization
    branch-scoped current-checkpoint freshness
    stable current_boundary syntax
    checkpoint metadata
    model-collaboration state
    typed declared references
    validation/evidence provenance minimum
```

It does not attempt semantic contradiction detection, universal dependency inference, vector similarity auditing or a replacement authority database.

Expected stable machine-readable summary lines:

```text
PUBLIC_REPOSITORY_INTEGRITY=PASS|FAIL
PRIVATE_CONTINUITY_INTEGRITY=PASS|FAIL|NOT_VERIFIED
CHAT_ROTATION_PREFLIGHT=PASS|HOLD|FAIL
```

Human-readable diagnostics should accompany failures/holds. A public integrity `FAIL` must return a non-zero process exit status.

## Explicit validator test matrix

The implementation must include deterministic tests for at least the following cases:

```text
identity
    duplicate ID inside one numbered family rejected
    same numeric ID across different families allowed

prospective metadata
    valid new Foundation / Specification / Research accepted
    missing required new metadata rejected
    legacy pre-cutover numbered files remain compatible
    new validation/evidence record with accepted alternative result/anchor fields accepted
    malformed new validation/evidence metadata rejected
    legacy validation/evidence compatibility snapshot honored

collaboration compatibility
    existing fenced provenance remains valid
    stronger collaboration-state validator remains compatible

declared references
    valid numbered and path references accepted
    missing declared target rejected
    absolute path rejected
    traversal rejected
    malformed typed reference rejected
    prose numbers not treated as references

live state
    CURRENT_STATE / current_routing synchronization success/failure
    stale-but-agreeing current checkpoint rejected on active branch
    unrelated branch does not create false freshness failure
    volatile current_boundary rejected

aggregate behavior
    public aggregate PASS/FAIL composed correctly
    private status remains independent
    NOT_VERIFIED private state does not become public FAIL
    rotation preflight maps required-private NOT_VERIFIED to HOLD

regression compatibility
    existing checkpoint validator still passes its accepted fixtures
    existing model-collaboration validator still passes its accepted fixtures
```

## Local verification and branch protection

The active branch is currently unprotected. Even if a repository-integrity workflow is added, GitHub branch state cannot be treated as though required checks were enforced by branch protection.

Therefore the development method must require the relevant deterministic integrity/pre-transition checks locally or through an equivalently controlled execution surface before a governed transition is declared complete.

CI is valuable evidence. It is not a substitute for an enforcement mechanism that is not actually configured.

## Rejected alternatives

### Universal Markdown schema

Rejected because existing artifact families have different semantics and historical representations.

### Mass legacy metadata rewrite

Rejected because it creates high-churn historical edits without improving the substantive evidence in those records.

### Sidecar metadata for every document

Rejected because it doubles synchronization surfaces and makes a new consistency problem.

### Central hand-maintained artifact registry

Rejected because the filesystem and family conventions already define existence. A second list would become another source that can drift.

The immutable validation/evidence compatibility snapshot is not such a registry. It is a one-time cutover boundary and is not extended during normal artifact creation.

### Universal dependency graph

Rejected because most repository relationships are semantic, contextual and historical. Typed declared references cover the small subset whose mechanical existence is worth enforcing.

### Heuristic reference scraping

Rejected because years, checkpoint numbers, experiment counts, citations and examples would create false dependencies.

### Global max-checkpoint rule across all branches

Rejected because branches intentionally preserve different historical states.

### Public CI asserting private integrity

Rejected because absence of access is not evidence of either correctness or corruption.

### CONTINUITY discovered only through docs/README

Rejected for the initial bootstrap path. The structural route remains valuable, but bootstrap-critical authority is now directly enumerated.

## Accepted implementation sequence

The accepted sequence remains deliberately governed:

```text
1. preserve this research/design record
2. freeze a bounded implementation specification
3. implement family-aware validators, tests and aggregate/preflight surfaces
4. run the strongest genuinely available verification
5. reconcile CURRENT_STATE, current_routing, KNOWLEDGE_MAP, CONTINUITY, DEVELOPMENT_METHOD and known stale references
6. repair/verify private companion continuity separately when required and accessible
7. run the aggregate repository/chat-rotation preflight
8. create a new checkpoint only when the verified state transition is meaningful
```

Steps 1 and 2 do not by themselves establish a repository-integrity PASS. During the short design-to-implementation transition, canonical live routing may still describe the preceding operational boundary. Reconciliation belongs after the implementation has earned acceptance so that canonical surfaces do not claim a gate that has not actually passed.

## Conclusion

The repository does not need a larger preservation bureaucracy. It needs a small typed integrity layer around the authority architecture it already has.

The accepted hardening therefore consists of:

```text
family-scoped identity
prospective family metadata
one-time legacy compatibility boundary for validation/evidence
explicit typed declared references only
branch-scoped live-state freshness
stable semantic current_boundary values
public/private integrity claim separation
chat-rotation preflight
explicit CONTINUITY bootstrap enumeration
risk-scaled deterministic verification
```

The live `chatgpt-12` observation strengthens the same architectural principle that motivated the wider integrity work: important knowledge may exist correctly yet still be operationally fragile if the routing path is not deterministic enough. The right response is not duplication. It is to strengthen the smallest authoritative route that removes the ambiguity.