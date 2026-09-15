# Research 180: W0 Substrate Slice 1 Implementation and Real-Repository Integration Result

**Date:** 2026-09-15
**Status:** W0 SUBSTRATE SLICE 1 ACCEPTED / PKA-G001..PKA-G005 PASS / W0 REMAINS IN PROGRESS / CURRENT CONTINUITY STILL AUTHORITY
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Implementation design:** Research 179
**Scope:** Record the first production W0 implementation slice, the real-repository integration defect exposed after the first isolated implementation pass, the bounded repair, and the final acceptance evidence for the substrate foundations.
**Authority:** Implementation evidence subordinate to Specification 028 and Research 179. This record accepts only the first W0 substrate slice. It does not accept W0 as a whole, begin W1 migration, or switch operational authority.

## 1. Implemented substrate boundary

The accepted slice creates the first production project-knowledge implementation under:

```text
tools/project_knowledge/
schemas/project_knowledge/
tests/fixtures/project_knowledge/
tests/unit/test_project_knowledge_substrate_*.py
```

The slice establishes:

```text
repository-local package boundary outside src/ads_system
shallow dependency layering with AST enforcement
immutable typed substrate model with selective identity
all eight V1 JSON Schema profiles + shared defs
strict Markdown/native-JSON declaration parsing
explicit COMMIT_SNAPSHOT and WORKTREE_SNAPSHOT modes
exact Git-blob revision binding with GIT_BLOB_BYTES_AT_COMMIT
centralized discovery/path-role classification
stable structured diagnostics
read-only validation CLI
```

No identity closure, authority resolver, workstream engine, persistent derived-view engine, reconstruction planner, capture promotion workflow, migration engine or authority-switch mechanism was implemented in this slice.

## 2. Initial implementation result and first real-repository failure

The first Codex implementation passed its isolated fixture suite but failed when ChatGPT executed the new validator against the actual ADS repository.

The failure was important evidence rather than a specification contradiction.

Two classes of integration defect were exposed:

```text
1. declaration examples inside fenced Markdown code blocks
   were incorrectly interpreted as live declarations;

2. canonical-discovery exclusion was conflated with
   "declaration forbidden here", causing legitimate evidence/test fixtures
   and future capture/generated areas to be treated too coarsely.
```

Concrete real files exposing the first defect were:

```text
docs/research/177_selected_candidate_physical_architecture_and_repository_contract_v01.md
docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
```

Both legitimately document the exact declaration syntax inside fenced code blocks.

The initial path semantics also made Candidate 01 research fixtures, test fixtures, and the future `docs/project_knowledge/captures/` / `generated/` areas indistinguishable under one blanket exclusion rule.

## 3. Repair

The bounded repair introduced context-aware Markdown parsing and role-aware discovery.

Markdown declaration markers now activate only when they occur as exact standalone marker lines outside ordinary backtick/tilde fenced code blocks. Fenced examples remain documentation. Real malformed declaration attempts outside fences still fail visibly.

Discovery now distinguishes:

```text
ELIGIBLE_SOURCE
EVIDENCE_FIXTURE
CAPTURE_AREA
GENERATED_AREA
DISALLOWED
```

This preserves the key distinction:

> exclusion from canonical source discovery is not equivalent to "a declaration here is forbidden."

Known evidence/test fixtures never enter production semantic discovery. Numbered research remains eligible. Valid `capture.v1` artifacts may later live under the capture area without becoming canonical authority. Valid `derived_view_manifest.v1` artifacts may later live under the generated manifest area without becoming canonical authority. Genuine misplaced production declarations still produce `EXCLUDED_BUT_DECLARED` at ERROR severity.

The repair also batches exact Git blob reads through `git cat-file --batch` while preserving byte-exact hash semantics and never falling back to working-tree bytes.

## 4. Accepted production behavior

### Selective identity

`semantic_id` remains optional outside profiles where continuity requires it. No production helper auto-mints IDs from paths, titles, hashes, filenames or positions.

### Schema strictness

All eight V1 profile schemas validate through Draft 2020-12. Every leaf declares its complete allowed property set with `additionalProperties: false`. Every profile has a live negative test proving an unknown property is rejected.

### Declaration parsing

The parser now proves:

```text
zero live declaration blocks                    valid absence
one live declaration outside fences             parsed
multiple live declarations                      hard failure
malformed live markers                          hard failure
fenced marker examples                          ignored as documentation
LF/CRLF                                          supported
strict JSON object only                         enforced
duplicate JSON keys at any depth               rejected
unknown profile                                 rejected
```

### Snapshot and revision safety

`COMMIT_SNAPSHOT` uses exact Git tree/blob materialization and is the only mode valid for durable commit-bound evidence.

`WORKTREE_SNAPSHOT` includes tracked plus non-ignored untracked candidates for local validation and remains structurally `NON_COMMITTED`. It cannot carry a persistent `SourceRevision` or be accepted as durable authority evidence.

### Discovery

Production discovery is role-aware and centralized. Research/test evidence is visible as excluded evidence without becoming current authority. Special future capture/generated areas remain compatible with their intended non-canonical profiles. Numbered research remains a legitimate source family.

## 5. Gate disposition

The first five frozen W0 gates are accepted:

```text
PKA-G001 PASS
    production package boundary under tools/project_knowledge
    and not src/ads_system

PKA-G002 PASS
    all eight V1 schemas validate positive fixtures and reject negative cases

PKA-G003 PASS
    strict declaration parsing, malformed/multiple blocks, LF/CRLF,
    duplicate-key rejection and fenced-example coexistence

PKA-G004 PASS
    typed substrate preserves selective identity and avoids universal IDs

PKA-G005 PASS
    exact Git-blob revision descriptors verify deterministically using
    GIT_BLOB_BYTES_AT_COMMIT
```

Strengthened Research 179 regressions also pass for:

```text
AST dependency-layer enforcement
no automatic SemanticId minting
unknown-property rejection for every profile
COMMIT_SNAPSHOT vs WORKTREE_SNAPSHOT durable-evidence boundary
EXCLUDED_BUT_DECLARED on genuinely misplaced declarations
real-repository fenced-example coexistence
fixture/evidence isolation from production discovery
future capture/generated-area compatibility
```

PKA-G006 through PKA-G017 remain unaccepted and are the remaining W0 program.

## 6. Real-repository validation

ChatGPT independently reran the production validator after repair.

### WORKTREE_SNAPSHOT

```text
ok                         true
diagnostics                0
governed live declarations 0
snapshot status            NON_COMMITTED
```

### COMMIT_SNAPSHOT @ HEAD

```text
ok                         true
diagnostics                0
governed live declarations 0
snapshot status            COMMITTED
source commit               e5563263acb5fd5cea6bf712ed9a86d320883ec2
```

Zero live declarations is expected at this stage because W0 does not migrate canonical sources.

## 7. Test evidence

Codex reported one monolithic final unit run of:

```text
531 passed
```

ChatGPT independently verified the same complete unit inventory through bounded partitions because the execution bridge has a 30-second command ceiling.

New substrate suites:

```text
17  architecture tests PASS
86  schema tests PASS
70  declaration tests PASS
49  snapshot/discovery/revision tests PASS
---
222 substrate tests PASS
```

Inherited unit inventory:

```text
101 PASS
116 PASS
92  PASS
---
309 inherited tests PASS
```

Total independently reverified:

```text
531 / 531 PASS
```

Repository integrity also independently passes:

```text
PUBLIC_REPOSITORY_INTEGRITY=PASS
```

`git diff --check` passes.

## 8. Architecture implication

The real-repository failure reinforces the redesign method rather than reopening Candidate 01:

```text
isolated fixture success
    !=
production repository compatibility
```

The implementation program therefore continues to require real-repository validation at each meaningful slice boundary, especially where the successor architecture interprets repository structure or source content.

The repair did not require a Specification 028 amendment, a Candidate 01 reopen or an H3 reopen.

## 9. Authority and migration boundary

```text
W0_OVERALL_ACCEPTED=false
W1_MIGRATION_STARTED=false
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

No live canonical/current source adopted Candidate 01 semantics in this slice.

## 10. Next W0 work

The next bounded implementation work should build the semantic engines that depend on this accepted substrate, beginning with identity-transition/current-index semantics and deterministic authority resolution. Workstream execution and derived-view generation can then build on those foundations in later bounded slices.

```text
RESEARCH180=W0_SUBSTRATE_SLICE1_ACCEPTED
PKA_G001_G005=PASS
PKA_G006_G017=PENDING
SPECIFICATION_028=UNCHANGED
NEXT=W0_IDENTITY_AND_AUTHORITY_ENGINES
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
