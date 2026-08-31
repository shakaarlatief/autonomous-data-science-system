# Specification 025 — V1 Governed Repository Integrity and Continuity Hardening

**Date:** 2026-08-31  
**Status:** FROZEN / IMPLEMENTATION PENDING  
**Scope:** Prospective typed repository-integrity contracts, branch-scoped live-state freshness, explicit continuity bootstrap routing, public/private integrity separation, deterministic validation, and chat-rotation preflight.  
**Declared references:** `research:106`, `specification:024`, `checkpoint:268`, `path:docs/CONTINUITY.md`, `path:docs/DEVELOPMENT_METHOD.md`, `path:docs/current_routing.json`, `path:docs/CURRENT_STATE.md`, `path:docs/KNOWLEDGE_MAP.md`, `path:scripts/check_current_routing.py`, `path:scripts/check_checkpoint_metadata.py`, `path:scripts/check_model_collaboration_state.py`, `path:scripts/check_knowledge_map.py`

## 1. Status and intent

This specification freezes the first implementation boundary derived from Research 106 and the resolved MC-0008 repository-integrity review.

It is preventive hardening. It does not classify the existing ADS repository as corrupt, untrustworthy or improperly preserved.

The implementation MUST strengthen the existing authority architecture without creating a universal metadata database, mass-rewriting historical files, inferring semantic dependencies from arbitrary prose, or allowing public verification to overclaim private continuity.

No implementation conforming to this specification may weaken the Source Vault bootstrap gates or change source-artifact authority. Repository integrity hardening and Source Universe ingestion remain separate concerns.

## 2. Artifact families

The implementation MUST reason in these classes:

```text
A  live canonical state
B  numbered durable knowledge
C  checkpoints
D  validation/evidence
E  model collaboration
F  specialized ledgers/indexes
G  global prose/code/Git history
```

A generic schema MUST NOT be imposed on classes F or G merely because they contain Markdown.

## 3. Family-scoped numeric identity

The numbered durable families are:

```text
foundation
specification
research
checkpoint
```

For each family independently, the validator MUST reject duplicate numeric identities.

The validator MUST allow the same numeric identity to exist in different families.

Examples:

```text
research 106 + research 106          FAIL
research 106 + specification 106     PASS
checkpoint 106 + foundation 106      PASS
```

Identity MUST be derived from the repository's governed filename convention, not from a global manually maintained registry.

## 4. Prospective metadata cutover

Historical numbered knowledge remains legacy-compatible below these immutable cutovers:

```text
foundation     strict from 025 onward
specification  strict from 025 onward
research       strict from 106 onward
```

Every post-cutover file in those families MUST contain exactly discoverable top-level metadata fields for:

```text
Date
Status
Scope
```

The implementation MAY permit additional fields. It MUST NOT infer a missing required field from body prose.

Checkpoint metadata remains governed by the existing checkpoint contract and validator. This specification MUST NOT silently redefine that schema.

## 5. Validation/evidence compatibility boundary

Before implementing strict validation/evidence metadata, the implementation MUST inventory the exact validation/evidence file paths that predate this specification.

That exact pre-cutover path set MUST be frozen as an immutable legacy compatibility snapshot used only to distinguish legacy files from later files.

The snapshot MUST satisfy all of the following:

```text
- it is not an ongoing artifact registry;
- normal new-file creation does not append to it;
- a later file absent from the snapshot is governed prospectively;
- moving/renaming a legacy file creates a new path and does not automatically inherit legacy exemption;
- the validator does not require remote Git-history traversal merely to establish cutover age.
```

Every new validation/evidence file outside that snapshot MUST contain:

```text
Date
one of:
    Status
    Classification
one of:
    Research
    Specification
    Scope
```

The chosen anchor MUST be explicit. The validator MUST NOT construct one heuristically from prose.

## 6. Typed declared-reference contract

The only generic prose-level dependency field introduced by this specification is:

```text
**Declared references:** `research:104`, `specification:024`, `checkpoint:268`, `path:docs/CONTINUITY.md`
```

The field is OPTIONAL.

When present, every token MUST conform to one of:

```text
foundation:<positive integer>
specification:<positive integer>
research:<positive integer>
checkpoint:<positive integer>
path:<repository-relative path>
```

The validator MUST:

```text
- resolve numbered references inside the named family;
- verify path references exist in the checked repository tree;
- reject absolute paths;
- reject path traversal using ..;
- reject malformed or unknown types;
- reject declared targets that do not exist;
- ignore numbers and paths elsewhere in prose for generic dependency validation.
```

The validator MUST NOT reinterpret collaboration-specific provenance fields as this generic field. Existing stronger collaboration contracts remain authoritative for their scope.

## 7. Live-state synchronization

The existing `CURRENT_STATE.md` / `current_routing.json` synchronization contract remains in force.

The implementation MUST continue checking overlapping live values including at least the current checkpoint and active development branch.

Where the current routing contract carries the latest specification or another explicitly synchronized value, the existing check MUST remain compatible unless deliberately strengthened through an explicit tested rule.

## 8. Branch-scoped checkpoint freshness

Agreement between live-state files is insufficient if both point to an older checkpoint.

The strengthened checker MUST implement:

```text
IF checked_branch == active_development_branch:
    current_checkpoint == max(numbered checkpoint IDs present in checked_branch tree)
ELSE:
    do not fail active-development freshness merely because the checked unrelated branch has a different max checkpoint
```

The checked branch MUST be supplied explicitly or resolved deterministically from the execution context.

The implementation MUST NOT compare against the maximum checkpoint on every repository branch.

## 9. Stable current_boundary

`docs/current_routing.json.current_boundary` MUST match:

```regex
^[a-z]+(?:-[a-z]+)*$
```

and MUST be no longer than 64 characters.

Digits, underscores, spaces, path separators and punctuation other than the internal hyphen separator are invalid.

The purpose is to keep `current_boundary` semantic and relatively stable. Exact checkpoint/research/specification provenance belongs in their dedicated fields and artifacts.

The currently over-specific value is expected to be repaired during canonical reconciliation after implementation verification, not by weakening this rule.

## 10. Knowledge Map integrity

The existing Knowledge Map integrity contract remains authoritative.

The public aggregate MUST include the existing Knowledge Map validator or equivalent deterministic checks, rather than implementing a second independent semantic index.

New Research 106 and Specification 025 MUST be routed into the appropriate repository-continuity/integrity subject during canonical reconciliation before the final public-integrity PASS is claimed.

## 11. Checkpoint compatibility

The existing checkpoint metadata validator MUST remain part of the public integrity surface.

Checkpoint numbering and metadata MUST NOT be redefined by the generic numbered-family metadata rules.

A new checkpoint MUST NOT be created merely because this specification was frozen. Checkpoint 269 is earned only by a later meaningful, verified state transition.

## 12. Model-collaboration compatibility

The existing model-collaboration state validator MUST remain authoritative for collaboration state.

The implementation MUST preserve valid fenced provenance representations already present in collaboration messages. It MUST NOT require every collaboration message to be converted into bold Markdown headers.

Any new shared integrity logic that inspects collaboration messages MUST be representation-aware and regression-tested against existing valid forms.

## 13. Explicit new-session reconstruction sequence

`docs/CONTINUITY.md` and the provider-neutral standard continuation prompt MUST be reconciled so every new persistent ADS session directly enumerates these mandatory first reads, in this order:

```text
1. README.md
2. docs/README.md
3. docs/CONTINUITY.md
4. docs/current_routing.json
5. docs/CURRENT_STATE.md
6. docs/KNOWLEDGE_MAP.md
```

The bootstrap MUST NOT depend on a collaborator first inferring from `docs/README.md` that `docs/CONTINUITY.md` should be opened.

After these six reads, the existing routing model remains in force: current state and continuity rules determine governing canonical documents, current checkpoint/research boundaries, specialized ledgers/manifests and relevant private companion state.

This requirement MUST NOT cause current checkpoint, branch or test status to be duplicated into `CONTINUITY.md`.

## 14. Public repository integrity aggregate

A deterministic command or script MUST produce:

```text
PUBLIC_REPOSITORY_INTEGRITY=PASS
```

or:

```text
PUBLIC_REPOSITORY_INTEGRITY=FAIL
```

The aggregate MUST cover at least:

```text
family-scoped numbered identity
prospective family metadata
validation/evidence prospective metadata
Knowledge Map integrity
CURRENT_STATE/current_routing synchronization
active-branch checkpoint freshness
current_boundary stability
checkpoint metadata
model-collaboration state
typed declared-reference existence and safety
```

On `FAIL`, the process MUST exit non-zero and provide actionable human-readable diagnostics.

The public aggregate MUST NOT claim to have verified private companion freshness, private Source Universe contents, secrets, credentials or machine-local state that the execution surface cannot inspect.

## 15. Private continuity result

Private continuity MUST be represented separately as:

```text
PRIVATE_CONTINUITY_INTEGRITY=PASS
PRIVATE_CONTINUITY_INTEGRITY=FAIL
PRIVATE_CONTINUITY_INTEGRITY=NOT_VERIFIED
```

`NOT_VERIFIED` MUST remain distinct from `FAIL`.

A public `RESOLVED_PRIVATE` field MUST NOT be changed to unresolved merely because the active verification environment cannot read its private value.

The initial public repository validator MAY report `NOT_VERIFIED` without reading the private repository. It MUST NOT fabricate a private `PASS`.

## 16. Chat rotation preflight

A deterministic preflight surface MUST produce one of:

```text
CHAT_ROTATION_PREFLIGHT=PASS
CHAT_ROTATION_PREFLIGHT=HOLD
CHAT_ROTATION_PREFLIGHT=FAIL
```

Minimum composition:

```text
public repository integrity
live-state integrity
model-collaboration integrity
private continuity status when relevant
transition branch/working-state requirement
```

Required behavior:

```text
public integrity FAIL
    -> FAIL

required private continuity FAIL
    -> FAIL

public integrity PASS + required private continuity NOT_VERIFIED
    -> HOLD

public integrity PASS + no unresolved required transition obligations
    -> PASS
```

The preflight MUST explain the reason for `HOLD` or `FAIL`.

## 17. Local/pre-transition verification requirement

Because the active development branch is currently unprotected, the implementation MUST NOT describe a passing GitHub Actions workflow as enforced branch protection.

Before repository-integrity hardening is accepted or a governed chat rotation is declared ready, the relevant deterministic checks MUST be run on the actual implementation target through a controlled local execution surface or an equivalently authoritative execution path.

CI results MAY supplement this evidence.

The repository's existing verification-tier language remains applicable. Core/shared validator logic requires integrated verification before acceptance.

## 18. Required tests

The implementation MUST include deterministic tests covering at least:

### Identity

```text
duplicate same-family ID -> reject
same numeric ID across families -> accept
```

### Prospective metadata

```text
valid post-cutover Foundation -> accept
valid post-cutover Specification -> accept
valid post-cutover Research -> accept
missing Date/Status/Scope in post-cutover numbered knowledge -> reject
legacy pre-cutover numbered knowledge -> accept
valid new validation/evidence alternatives -> accept
invalid new validation/evidence result/anchor -> reject
legacy validation/evidence compatibility snapshot -> accept
```

### Collaboration representation

```text
accepted fenced provenance -> accept
existing collaboration fixtures/contracts remain compatible
```

### Declared references

```text
valid family reference -> accept
valid repository-relative path -> accept
missing target -> reject
absolute path -> reject
../ traversal -> reject
malformed type -> reject
ordinary prose numbers -> ignored
```

### Live routing

```text
synchronized current state -> accept
mismatched current state -> reject
stale-but-agreeing checkpoint on active branch -> reject
unrelated branch with different checkpoint maximum -> no false freshness failure
valid semantic current_boundary -> accept
volatile/digit-bearing current_boundary -> reject
```

### Aggregates

```text
public component failure -> PUBLIC_REPOSITORY_INTEGRITY=FAIL
all public components pass -> PUBLIC_REPOSITORY_INTEGRITY=PASS
private unavailable -> PRIVATE_CONTINUITY_INTEGRITY=NOT_VERIFIED
private unavailable must not alter public PASS/FAIL
required private NOT_VERIFIED + public PASS -> CHAT_ROTATION_PREFLIGHT=HOLD
required private FAIL -> CHAT_ROTATION_PREFLIGHT=FAIL
all required surfaces pass -> CHAT_ROTATION_PREFLIGHT=PASS
```

## 19. Expected implementation surfaces

The exact file decomposition is an implementation choice, but the expected bounded direction is:

```text
shared family-aware integrity logic
public aggregate command/script
chat-rotation preflight command/script
extension of current-routing validation
unit/regression tests
repository-integrity CI workflow
```

Existing scripts should be reused where their contracts already fit instead of copied into parallel implementations.

Likely integration points include:

```text
scripts/check_current_routing.py
scripts/check_checkpoint_metadata.py
scripts/check_model_collaboration_state.py
scripts/check_knowledge_map.py
```

No implementation is required to use these exact filenames for new surfaces if a cleaner tested decomposition is found.

## 20. Canonical reconciliation after implementation

After implementation and genuine verification, the same governed transition MUST reconcile the canonical surfaces that describe this architecture.

At minimum inspect and update when warranted:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
docs/KNOWLEDGE_MAP.md
docs/CONTINUITY.md
docs/DEVELOPMENT_METHOD.md
```

Reconciliation MUST:

```text
- route Research 106 and Specification 025 semantically;
- make the mandatory CONTINUITY first-read explicit;
- replace the volatile current_boundary with a valid semantic boundary;
- remove known stale live references where the verified state supersedes them;
- describe the actual verification result and tier, not the intended one;
- preserve Source Vault pre-ingestion state unless that state actually changes.
```

Private companion repair/verification remains a separate authority operation.

## 21. No mass legacy migration

Acceptance of this specification MUST NOT trigger a broad rewrite of historical Foundation, Specification, Research, validation/evidence or collaboration records solely to make them resemble new files.

Legacy compatibility is intentional. New artifacts become more regular prospectively.

Historical files may still be changed for an independent substantive correction, explicit provenance repair or supersession process when justified.

## 22. Acceptance gate

This specification may move from `FROZEN / IMPLEMENTATION PENDING` to an accepted implemented state only when all of the following are true:

```text
1. family-aware integrity implementation exists;
2. required test matrix is implemented;
3. existing checkpoint and collaboration validation remain compatible;
4. branch-scoped freshness is implemented;
5. typed reference safety is implemented;
6. public/private aggregate separation is implemented;
7. continuity bootstrap sequence is reconciled;
8. canonical routing and Knowledge Map are reconciled;
9. strongest required integrated verification genuinely passes on the implementation target;
10. public repository integrity reports PASS on the reconciled target;
11. any stronger chat-rotation claim reports PASS rather than HOLD/FAIL;
12. checkpoint creation, if any, reflects a meaningful verified boundary rather than document creation alone.
```

Until those conditions are met, no repository-integrity PASS or rotation-ready claim may be inferred from the existence of this specification.