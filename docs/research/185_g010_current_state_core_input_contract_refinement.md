# Research 185: G010 Current-State-Core Input-Contract Refinement

**Date:** 2026-09-17
**Status:** PROSPECTIVE RESEARCH-179 REFINEMENT ACCEPTED / SPECIFICATION 028 UNCHANGED / G010 REOPENED / NO G010 IMPLEMENTATION YET / W1 STILL BLOCKED
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing specification:** Specification 028
**Refines:** Research 179 W0 implementation choices only
**Trigger:** first bounded PKA-G010 implementation attempt stopped under Research 179 section 24 because the accepted W0 schemas could not honestly carry several frozen current-state-core fixture semantics
**Scope:** freeze the smallest typed production input contract needed to implement G010 through the accepted G009 derived-view architecture without weakening schema strictness, promoting research fixtures into authority, parsing global compatibility prose, or starting W1 migration.
**Authority:** prospective implementation-design refinement. Specification 028 remains governing; Research 157/158 remain immutable qualification evidence; current continuity remains operational authority.

## 1. Why the first G010 implementation correctly stopped

The frozen Research 157/158 fixture requires 23 must-preserve semantic items. Fifteen are represented in the compact current-state core and eight remain recoverable from deeper source-owned state/evidence.

The accepted production W0 schemas before this refinement could represent some of those facts, but not all of them honestly. In particular, they had no adequate typed machine contract for:

```text
active execution checkpoint / development branch / PR / semantic boundary
active stage identity + stage state
promoted integration branch + exact promoted commit
current experiment outcome
source-owned governing-procedure identity
compact Source Vault ingestion / Course-2 orientation states
```

Research 179 deliberately kept `project_boundary.v1` and other W0 profiles narrow. G009 then correctly enforced those schemas before durable view execution. Therefore the missing facts could not be smuggled through the G009 pipeline without either changing the accepted W0 input contract or weakening the gate.

Rejected shortcuts remain rejected:

```text
read docs/CURRENT_STATE.md or docs/current_routing.json as G010 inputs
import the Research 157/158 script into production
read the oracle from production code
hard-code the old oracle payload in Python
add a generic arbitrary facts object
encode structured JSON inside current_anchor/scope/references/provenance
infer semantic role from carrier path or lexical path order
parse ungoverned free-form prose as the normative machine contract
make a test-only normalized projection pass stand in for the production G009 path
start W1 source migration just to make W0 green
```

The stop therefore demonstrated the exact condition anticipated by Research 179 section 24: an accepted implementation choice could not satisfy the frozen gate honestly and must be amended prospectively.

## 2. Specification 028 does not need amendment

Specification 028 already freezes the relevant architectural rules:

```text
profile-specific strict schemas
source-local canonical ownership
workstream durable continuation controls
Project Integration Boundary as a natural project-global semantic source
compact deterministic current-state derived view
no unique accepted truth in generated views
old continuity remains authority through W0
W1 live-control migration only after W0 acceptance
```

It does not freeze Research 179's exact minimal field inventory as the only legal W0 representation. Research 177 also explicitly described workstream execution-anchor semantics and expected `project_boundary.v1` to become meaningful when implementation evidence required distinguishing fields.

Therefore Research 185 refines Research 179 prospectively while leaving Specification 028 unchanged.

## 3. Design principle

The production rule is:

```text
natural semantic owner
    owns the fact once

strict typed declaration
    exposes only the small machine control needed by deterministic views

G009 derived-view framework
    projects that control into current_state_core

current_state_core
    remains derived, compact and non-authoritative
```

No canonical `CURRENT_STATE` database or global current-facts registry is introduced.

## 4. Workstream profile refinement

`workstream.v1` gains four narrowly bounded optional machine-control structures.

### 4.1 `execution_anchor`

A strict object representing the machine current execution anchor for a workstream:

```json
{
  "checkpoint": 501,
  "development_branch": "v1-source-vault-bootstrap-resume",
  "pull_request": null,
  "current_boundary": "project-knowledge-source-vault-current-state-core-shadow-next"
}
```

Contract:

```text
checkpoint
    non-negative integer

development_branch
    nonblank authored text

pull_request
    positive integer or null

current_boundary
    authored semantic identifier, not a path-derived identity
```

All four members are required when `execution_anchor` is present.

`execution_anchor` is the typed production refinement of the existing loose `current_anchor` concept. A declaration MUST NOT carry both `execution_anchor` and `current_anchor`; that would create two machine representations of one current anchor.

Existing G008 fixtures using `current_anchor` remain valid. Production projection may normalize `execution_anchor.current_boundary` into the existing internal route-anchor surface where needed, but the declaration contains only one normative machine anchor.

### 4.2 `stage`

A strict current-stage control:

```json
{
  "stage_id": "RESEARCH:124",
  "stage_state": "TARGET_ARCHITECTURE_NOT_SELECTED"
}
```

Both values are authored semantic identifiers. This is one current stage/state pair only. It is not an arbitrary metadata object and carries no payload, prose, counters, paths or nested facts.

The stage source itself remains independently discoverable by `stage_id` when it has its own durable source. The workstream stores only the small current-stage control required for broad orientation.

### 4.3 `governing_procedure`

A single authored `semantic_id` identifying the governing procedure applicable to the workstream.

This replaces the Research 157 shadow experiment's path-valued governing-procedure field with representation-independent semantic identity. The carrier path is resolved from the semantic source, never embedded as workstream identity.

### 4.4 `orientation_milestones[]`

A bounded array of compact workstream-local orientation milestones:

```json
[
  {
    "milestone_id": "SOURCE-VAULT:INGESTION",
    "state": "NOT_STARTED"
  },
  {
    "milestone_id": "COURSE:2",
    "state": "BLOCKED"
  }
]
```

Allowed milestone states are:

```text
NOT_STARTED
PENDING
ACTIVE
PAUSED
BLOCKED
COMPLETED
SUPERSEDED
```

Rules:

```text
milestone_id must be an authored semantic identifier
milestone IDs must be unique inside one workstream
no arbitrary value/payload field exists
no counters, hashes, paths or nested metadata are allowed
array order has no semantic priority
```

This structure is intentionally smaller than a generic `facts` collection. It represents only compact lifecycle-like controls that the workstream naturally owns and that broad orientation must expose.

If a milestone later needs independent authority, relations, rich provenance, its own continuation, or a richer state than `milestone_id + state`, it must become a natural semantic source/workstream rather than expanding this structure into a universal object store.

## 5. Project-boundary profile refinement

`project_boundary.v1` gains the two fields that make the Project Integration Boundary a meaningful machine contract:

```json
{
  "promoted_branch": "v1-frontend-spike",
  "promoted_commit": "2480109fadeee1e480ef03b82e335aacdf9adf91"
}
```

Contract:

```text
promoted_branch
    nonblank authored Git branch text

promoted_commit
    exact 40-character lowercase Git commit identity
```

They are a pair: either both are absent or both are present.

For `kind = PROJECT_INTEGRATION_BOUNDARY`, both are required.

This resolves Research 179's explicit W1/watch risk that `project_boundary.v1` could remain merely a label rather than a meaningful contract. The evidence arrived earlier than W1 because G010 needs the exact bounded integration facts.

## 6. Semantic-source profile refinement

`semantic_source.v1` gains one narrowly scoped optional scalar:

```text
outcome
```

`outcome` is an authored semantic identifier, not an arbitrary JSON value.

For `kind = EXPERIMENT_RESULT`, `outcome` is required. For other kinds it is not permitted by this refinement.

This gives the frozen `latest_experiment_outcome` semantic one natural machine representation without introducing a generic value/facts bag.

A current specification needs no equivalent value field. Its durable `semantic_id` is the specification identity itself.

## 7. G010 semantic-role selection contract

G010 may not choose required owners from file paths, input order, lexical semantic-ID order, timestamps, or arbitrary first match.

The bounded production fixture uses explicit profile/kind/state roles:

```text
active project workstream
    profile = workstream.v1
    kind = PROJECT_KNOWLEDGE_ARCHITECTURE_WORKSTREAM
    state = ACTIVE
    exactly one required

Project Integration Boundary
    profile = project_boundary.v1
    kind = PROJECT_INTEGRATION_BOUNDARY
    exactly one required

current specification
    profile = semantic_source.v1
    kind = SPECIFICATION
    canonical candidate set must contain exactly one

current experiment result
    profile = semantic_source.v1
    kind = EXPERIMENT_RESULT
    canonical candidate set must contain exactly one
    outcome required

paused resumable workstreams
    profile = workstream.v1
    state = PAUSED
    expected_to_resume = true
    project all matching workstreams
```

Zero or multiple candidates for any required singular role is a hard G010 failure.

Paused-workstream presentation order is deterministic by authored `semantic_id`; this order is representation only and does not choose authority or priority.

Every `resume_target`, `governing_procedure`, stage source when required by the fixture, and other semantic reference required for G010 qualification must resolve to exactly one admitted canonical semantic identity. Missing or ambiguous referenced identity fails visibly.

## 8. Production current-state-core V1 output contract

G010 freezes the production output around semantic identity rather than the old experimental path-oriented representation.

Equivalent shape:

```json
{
  "schema_version": "1",
  "active_workstream": {
    "semantic_id": "WS-PKA-CURRENT",
    "state": "ACTIVE",
    "objective": "...",
    "execution_anchor": {
      "checkpoint": 501,
      "development_branch": "v1-source-vault-bootstrap-resume",
      "pull_request": null,
      "current_boundary": "project-knowledge-source-vault-current-state-core-shadow-next"
    },
    "stage": {
      "stage_id": "RESEARCH:124",
      "stage_state": "TARGET_ARCHITECTURE_NOT_SELECTED"
    }
  },
  "integration_boundary": {
    "semantic_id": "PROJECT-INTEGRATION-BOUNDARY",
    "promoted_branch": "v1-frontend-spike",
    "promoted_commit": "2480109fadeee1e480ef03b82e335aacdf9adf91"
  },
  "current_specification": {
    "semantic_id": "SPECIFICATION:027"
  },
  "current_experiment": {
    "semantic_id": "EXPERIMENT:192",
    "outcome": "INCOMPLETE"
  },
  "paused_workstreams": [
    {
      "semantic_id": "WS-SOURCE-VAULT-BOOTSTRAP",
      "state": "PAUSED",
      "resume_target": "SOURCE-VAULT:REVIEWED-INGESTION",
      "governing_procedure": "PROCEDURE:PERMANENT-SOURCE-VAULT-BOOTSTRAP",
      "orientation_milestones": [
        {
          "milestone_id": "COURSE:2",
          "state": "BLOCKED"
        },
        {
          "milestone_id": "SOURCE-VAULT:INGESTION",
          "state": "NOT_STARTED"
        }
      ]
    }
  ]
}
```

The exact schema is to be added/frozen by the G010 implementation tests before migration depends on it, as Specification 028 requires.

The core remains bounded by the previously qualified broad-orientation budget:

```text
canonical serialized current-state-core <= 2,048 bytes on the frozen G010 fixture
```

The output has `authority_class = derived` only through its G009 manifest; it is never a canonical semantic owner.

## 9. Crosswalk to the frozen 23-item must-preserve fixture

The old Research 157 representation remains immutable evidence. G010 uses an explicit semantic crosswalk rather than modifying that fixture until it fits production schemas.

### 9.1 Fifteen items represented in the production core

```text
MP01 current_checkpoint
    -> active_workstream.execution_anchor.checkpoint

MP02 active_development_branch
    -> active_workstream.execution_anchor.development_branch

MP03 active_pr
    -> active_workstream.execution_anchor.pull_request

MP04 current_boundary
    -> active_workstream.execution_anchor.current_boundary

MP05 active_research_stage
    -> active_workstream.stage.stage_id

MP06 target_architecture_selection_state
    -> active_workstream.stage.stage_state

MP07 promoted_integration_branch
    -> integration_boundary.promoted_branch

MP08 promoted_integration_sha
    -> integration_boundary.promoted_commit

MP09 latest_specification
    -> current_specification.semantic_id
       production uses representation-independent identity such as SPECIFICATION:027
       rather than parsing the unstructured value "027"

MP10 latest_experiment_outcome
    -> current_experiment.outcome

MP11 source_vault_workstream_state
    -> paused_workstreams[].state

MP12 source_vault_resume_target
    -> paused_workstreams[].resume_target
       production strengthens the old prose target into a semantic target identity

MP13 source_vault_governing_procedure
    -> paused_workstreams[].governing_procedure
       production strengthens the old path into governing-procedure semantic identity

MP17 source_vault_ingestion_status
    -> orientation milestone SOURCE-VAULT:INGESTION / NOT_STARTED

MP21 course2_gate
    -> orientation milestone COURSE:2 / BLOCKED
```

The Research 157 values and the production semantic identities are connected by qualification-fixture crosswalk assertions, not by runtime string parsing.

### 9.2 Eight items deliberately excluded from the compact core

```text
MP14 source_vault_registry_status
MP15 source_vault_alembic_head
MP16 source_vault_first_corpus_compare
MP18 source_vault_working_audit_status
MP19 source_vault_backup_status
MP20 source_vault_restore_status
MP22 source_vault_resume_sequence
MP23 source_vault_private_dependency_state
```

These remain source-owned drill-down semantics in the Source Vault governing procedure and exact evidence/runbook sources already hash-bound by Research 157/158.

G010 qualification MUST prove for each of these eight:

```text
a frozen exact source-owner/evidence binding exists
the historical fixture value remains recoverable from that bounded source set
no corresponding unique value is copied into current_state_core
no new generic production field is introduced merely to preserve it
```

A qualification-only crosswalk may name those exact immutable evidence bindings. That crosswalk is test evidence, not production authority and is not a G009 canonical input.

## 10. New production fixture rule

Research 157/158 fixture and oracle hashes remain frozen and MUST NOT be edited.

G010 adds a separate production-contract fixture containing strict production-schema-valid governed sources that represent the same 15 core semantics using the refined contracts above.

The production fixture is synthetic W0 qualification data, not migrated live authority.

Required relationship:

```text
Research 157/158 fixture + oracle
    immutable historical behavioral basis

G010 semantic crosswalk
    proves old must-preserve semantics -> production representation

G010 production fixture
    strict production-schema-valid source corpus

G009 builder + G010 pure unit
    deterministic production generation path
```

Production code MUST NOT read the Research 157 oracle or production-fixture expected output.

## 11. G010 implementation boundary after this refinement

G010 implementation must now:

```text
extend strict schemas only as frozen above
retain additionalProperties=false
add malformed/unknown-property regressions for every refined profile
requalify affected G002 schema behavior
requalify affected G008 workstream behavior
freeze current_state_core V1 output shape in tests
register one G009 ViewSpecification for current_state_core
implement the compute unit through the accepted restricted pure-unit architecture
use canonical_json.v1 serialization
bind exact implementation closure and execution identities
use the G010 production fixture for positive qualification
use Research 157/158 only as immutable behavioral/crosswalk evidence
fail visibly for missing/duplicate/ambiguous required roles
prove input/permutation independence
prove meaningful input changes affect bytes/manifest/freshness
prove full/selected G009 builder equivalence for current_state_core
prove no read/dependency on CURRENT_STATE.md, current_routing.json or the oracle
prove no authority switch or persistent compatibility-path overwrite
```

G010 does not publish live successor semantic sources and does not start W1.

## 12. Regression consequences

Because this prospective refinement changes accepted W0 profile semantics, G010 acceptance requires rerunning at least:

```text
G002 strict schema tests for semantic_source/workstream/project_boundary + shared defs
G003 declaration parser/schema dispatch tests
G004 substrate/semantic model tests affected by new declaration fields
G008 workstream suite, including existing current_anchor behavior
G009 view/execution/adversarial suites
G010 focused production-fixture/current-core suite
architecture/layer guards
full substrate suite
G006/G007 identity/authority regression suites
inherited unit inventory
compileall
WORKTREE project-knowledge validation
accepted-HEAD COMMIT validation
PUBLIC_REPOSITORY_INTEGRITY
git diff --check
```

Existing unknown-property rejection remains mandatory. New fields are not an excuse to weaken schema strictness.

## 13. Explicit anti-registry constraints

The following are part of the refinement, not optional implementation style:

```text
NO generic facts/value/payload/map field
NO arbitrary JSON under orientation_milestones
NO source path used as semantic identity
NO duplicate current_anchor + execution_anchor declarations
NO implicit "latest" from filename/number/path sort
NO arbitrary first-match role selection
NO current-state-core-only canonical owner
NO derived view consumed as authority
NO research fixture/oracle consumed as production authority
```

The bounded new fields exist because their natural owners already possess these semantics and deterministic orientation requires a machine representation.

## 14. Gate disposition

```text
PKA-G001..PKA-G009   PASS
PKA-G010              REOPENED FOR IMPLEMENTATION UNDER RESEARCH 185
PKA-G011..PKA-G017   PENDING
W0                    IN PROGRESS
W1                    NOT STARTED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
SPECIFICATION_028=UNCHANGED
RESEARCH_179=PROSPECTIVELY_REFINED_BY_RESEARCH_185
```

The next action is a bounded G010 implementation against this refined production input contract, followed by independent adversarial review before acceptance.
