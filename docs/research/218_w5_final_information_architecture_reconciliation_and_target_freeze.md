# Research 218: W5 Final Information Architecture Reconciliation and Target Freeze

**Date:** 2026-09-20
**Status:** FULL W5 INFORMATION ARCHITECTURE FROZEN / BROADER CURRENT SEMANTIC MIGRATION MAY BEGIN
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing implementation contract:** Specification 028
**Evidence base:** Research 208, Research 209, Research 212, Research 214, Research 217
**Prior accepted project milestone:** Checkpoint 554 / W4 ACCEPTED AND FINALIZED
**Scope:** Reconcile all W5 information-architecture evidence, freeze the future physical and authoring contract, select the production navigation realization, define the current-semantic migration sequence, and open broader W5 migration without changing operational authority.
**Authority:** This record freezes the W5 target information architecture and authoring model. It does not itself migrate all current semantics, overwrite live compatibility surfaces, accept W5, create a cutover candidate, or switch operational authority.

## 1. Why the final freeze is now justified

Research 208 intentionally froze only the physical/authoring subset and withheld the remaining architecture until four empirical obligations were closed.

Those obligations are now resolved:

```text
C1  Research 209
    per-view implementation closures accepted

T1  Research 217
    controlled semantic-subject architecture accepted

T3  Research 212
    selective per-item carrier contract accepted

T4  Research 214
    historical-navigation evidence contract accepted
```

No unresolved architecture question from Research 208 remains large enough to justify another design round before migration.

## 2. Final physical repository architecture

The future repository remains hybrid. Physical containment expresses primary responsibility only.

```text
docs/
    README.md
    VISION.md
    PRINCIPLES.md
    DEVELOPMENT_METHOD.md
    CONTINUITY.md
    MAJOR_CHANGES.md

    # compatibility / browsing surfaces during migration
    CURRENT_STATE.md
    current_routing.json
    KNOWLEDGE_MAP.md
    DECISIONS.md
    OPEN_QUESTIONS.md
    OPEN_ARCHITECTURE_BACKLOG.md

    # epistemic / lifecycle families
    foundations/
    specifications/
    research/
    checkpoints/
    experiments/

    # natural subsystem homes
    cockpit/
    source_universe/
    methodological_knowledge/
    local_execution/
    model_collaboration/
    private_companion/

    # selective first-class item homes
    decisions/
    architecture_backlog/
    open_questions/            # only when stable first-class question IDs exist

    # narrow project-knowledge infrastructure
    project_knowledge/
        architecture/
        navigation/
        migration_evidence/
        generated/
        captures/
            open/
            historical/
        transitions/
        joint_authority/
```

A generic `docs/domains/` wrapper remains rejected.

`docs/project_knowledge/` remains infrastructure for project-development knowledge architecture, not a universal home for substantive project truth.

## 3. Physical placement semantics

```text
physical parent != exclusive semantic parent
folder path != semantic identity
folder path != authority by itself
folder path != complete navigation
```

A source lives where its primary natural responsibility lives.

Cross-cutting semantic organization is expressed through subject navigation, not file duplication.

## 4. Placement precedence

When a carrier could plausibly live in an epistemic family or a domain home, use primary responsibility.

```text
epistemic/lifecycle family wins when the primary responsibility is:
    governed contract
    bounded investigation / comparison / design study
    deep durable rationale
    meaningful historical project-state boundary

domain home wins when the primary responsibility is:
    current domain operation
    domain procedure / runbook
    current domain state or control
    resume target
    domain-local manifest
    domain-local validation evidence consumed by that operation
```

The diagnostic question `what breaks if this source is wrong?` may help, but does not override primary responsibility.

## 5. Naming contract

New ordinary directories and descriptive files use `lowercase_snake_case` by default.

Established role names such as `README.md`, `VISION.md`, `STATE.json` and `RESOLUTION.md` remain valid exceptions.

Numbered epistemic families retain `NNN_lower_snake_case.md` where ordered artifact/provenance identity is useful.

Numbers and paths are not semantic IDs.

Existing files are not renamed merely for cosmetic normalization.

## 6. Granularity contract

Update the existing natural owner unless a new carrier is materially justified.

A new carrier is warranted when one or more of the following apply:

```text
independent lifecycle
distinct authority scope
independent provenance or revision control
several sources must refer to the item directly
remaining embedded would create duplicate or ambiguous authority
size / volatility materially overloads the current owner
the item must become a first-class typed-relation target
```

This rejects both mega-documents and file-per-fact atomization.

## 7. Final item-registry contract

One project-knowledge declaration per carrier remains the V1 rule.

Aggregate decision/question/backlog documents may continue to preserve historical prose and browsing value.

An embedded item stays anchor-only when it has no independent lifecycle, authority, revision or first-class relation requirement.

An embedded item moves to its own canonical carrier when first-class semantics require it.

Prospective homes are:

```text
docs/decisions/
docs/architecture_backlog/
docs/open_questions/       # only after stable first-class question IDs are introduced
```

During migration, an item must never remain simultaneously current-authoritative in both the aggregate source and the new item carrier.

Aggregate root registries become compatibility/index surfaces only after every still-current governing item inside them has a migration disposition.

Mass splitting of historical registry entries remains rejected.

## 8. Final semantic-subject contract

The accepted subject architecture contains 18 assignable semantic subjects plus 6 non-assignable navigation parents.

Membership is source-owned or source-adjacent and is never centrally enumerated.

```text
subject membership
    only when the carrier substantively develops, governs, specifies,
    evaluates, or preserves durable meaning about that subject

secondary subject
    must independently clear the same threshold

preferred_subject
    best default semantic route

preferred_subject = null
    allowed only when genuinely co-primary subjects have no defensible
    unique default route
```

Constitutional or summary carriers receive secondary subjects only when they themselves contain durable governing meaning, not merely summaries or links.

Structural facets and resolver facets remain separate from semantic subjects.

## 9. Production subject catalog

The production catalog will live at:

```text
docs/project_knowledge/navigation/subject_catalog.json
```

It owns only vocabulary and hierarchy:

```text
subject ID
human label
description
include_when
exclude_when
zero or more broader parents
optional preferred parent
optional aliases
status / merge redirect when needed
```

It must never list source members.

The preferred production representation is a governed native JSON `semantic_source.v1` carrier with `kind=SUBJECT_CATALOG` and a dedicated catalog payload validated by schema.

The catalog does not require a universal semantic identity merely because it is canonical navigation vocabulary. Subject IDs inside the catalog are stable navigation identifiers and are not inferred from file paths.

## 10. Source-local navigation metadata

Current migrated carriers may optionally add:

```json
{
  "navigation": {
    "subjects": ["project-knowledge-architecture"],
    "preferred_subject": "project-knowledge-architecture"
  }
}
```

This metadata belongs inside the existing project-knowledge declaration for that carrier.

It does not alter:

```text
semantic identity
authority class
scope
relations
lifecycle
physical ownership
```

Historical files are not retrofitted merely to maximize subject coverage.

## 11. Production navigation realization

The production realization will extend the existing `subject_index` persistent view rather than create a parallel navigation generator.

Reason:

```text
the view already owns project-knowledge navigation projection
C1 now gives it a precise view-specific implementation closure
the accepted restricted execution layer is already qualified
a second generator would duplicate input binding, freshness and determinism logic
```

`subject_index` advances to a V2 contract that keeps semantic subjects explicitly separate from structural/resolver facets.

Conceptual output:

```text
schema_version
authority_class = derived

subjects
    controlled subject definitions / hierarchy needed for navigation

semantic_memberships
    subject_id
    source_path
    semantic_id when present
    preferred flag

structural_facets
    profile
    kind
    selected non-semantic generated facets
```

`scope:*` resolver matching does not silently become semantic-subject membership.

## 12. Navigation validation rules

Production validation must fail closed when:

```text
the canonical subject catalog is missing or duplicated
subject IDs are duplicated
parentage is cyclic
preferred_parent is not an allowed broader parent
a source names an unknown or non-assignable subject
preferred_subject is not one of that source's subjects
catalog entries attempt to enumerate members
a merged/retired subject is authored as active membership without a valid redirect
```

The catalog itself is an input datum, not generator implementation. Changing vocabulary must stale the subject navigation view as data dependency, not masquerade as a code-closure change.

## 13. Pure-unit proportionality decision

The accepted decision is selective reuse, not blanket expansion.

```text
semantic-subject projection
    extend the existing qualified subject_index pure-unit path

other persistent views
    unchanged unless their semantics genuinely require the new navigation fields

historical Knowledge Map evidence
    do NOT turn into a persistent rebuildable pure view
```

This preserves C1's implementation-closure discipline.

## 14. Historical-navigation evidence

Before the live legacy Knowledge Map can retire, the final qualified version must be frozen into:

```text
docs/project_knowledge/migration_evidence/
    legacy_knowledge_map_routing_v1.json
```

That artifact is immutable evidence for an exact source boundary and digest.

It preserves:

```text
legacy topic IDs
labels / short descriptions
topic -> artifact routes
checkpoint-range -> topic routes
specialized index routes
exact source ref
exact source digest
```

It is not substantive authority and does not claim post-retirement rebuildability.

Because the current Knowledge Map will continue changing during W5, the final production evidence artifact is not created yet.

## 15. Final authoring decision tree

Use this order for ordinary future work:

```text
1. Does an existing current natural owner already own the responsibility?
       yes -> update it

2. Is the understanding unreviewed / provisional / interaction-derived?
       yes -> capture; review before promotion

3. Is this a current decision/backlog/question item that needs independent
   lifecycle, authority, provenance or typed relations?
       yes -> create/select the first-class item carrier

4. Is this an explicit governed implementation/execution contract?
       yes -> Specification

5. Is this a bounded investigation, comparison, design study or research result?
       yes -> Research

6. Is this deep durable rationale that should survive implementation detail?
       yes -> Foundation, sparingly

7. Is this current domain operation, procedure, runbook, state, resume target
   or domain-local manifest/evidence?
       yes -> natural domain home

8. Is this a governed experiment program/result?
       yes -> experiment family / executable experiment surface as appropriate

9. Is this a meaningful historical project-state boundary?
       yes -> Checkpoint

10. Is this only navigation, orientation or indexing?
       yes -> generated/index surface; do not create unique accepted truth there

11. Otherwise:
       use the narrowest natural canonical owner justified by the granularity rules
```

Subject metadata is added only after the carrier is placed by primary responsibility.

## 16. Migration-unit dispositions

Specification 028 migration dispositions remain governing:

```text
MIGRATE_CANONICAL
DERIVE_COMPATIBILITY_VIEW
KEEP_HISTORICAL_LATENT
KEEP_EVIDENCE_ONLY
CAPTURE_OR_CANDIDATE
PRIVATE_DELEGATED
UNRESOLVED_MIGRATION
```

`UNRESOLVED_MIGRATION` blocks W5 acceptance for any unit required by the active/current architecture.

## 17. W5 broader migration sequence

Broader migration now proceeds by current semantic responsibility, not chronology.

```text
W5-F0  production navigation substrate
       subject catalog schema/carrier
       optional navigation declaration field
       cross-source validation
       subject_index V2

W5-F1  root/current project-development control owners
       narrative singletons and current item-registry responsibilities

W5-F2  active subsystem/domain owners
       project knowledge
       Source Universe
       Cockpit
       local execution
       model collaboration
       methodological knowledge

W5-F3  current epistemic owners
       only still-current Foundations / Specifications / Research responsibilities
       needed by active authority or reconstruction

W5-F4  selective first-class item migration
       decisions / architecture backlog / questions where justified

W5-F5  subject membership completion for migrated current owners
       plus reverse-reference / identity / authority audit

W5-G   parity, provenance, deterministic rebuild, compatibility, rollback
       and migration-audit qualification
```

Deep passive history stays latent except where identity, authority, active workstream continuation or migration parity requires structure.

## 18. Root compatibility surfaces during W5

The following remain live current-continuity surfaces throughout W5:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
docs/CONTINUITY.md
docs/KNOWLEDGE_MAP.md
```

Root aggregate registries remain available while their current items are migrated.

No successor-generated file may replace these live paths until W6 cutover-candidate entry.

## 19. Explicit rejections retained

```text
no universal semantic IDs
no path-target typed relations
no multiple declarations per ordinary carrier
no universal central content registry
no subject catalog member lists
no mass historical declaration retrofit
no one-file-per-fact atomization
no generic docs/domains wrapper
no folder taxonomy as complete semantic organization
no scope:* resolver vocabulary promoted wholesale into semantic subjects
no live compatibility overwrite during W5
```

## 20. Full W5 target freeze result

```text
W5_INFORMATION_ARCHITECTURE=FROZEN
PHYSICAL_AUTHORING_CONTRACT=FROZEN
C1=ACCEPTED
T1=ACCEPTED
T3=ACCEPTED
T4=ACCEPTED
ITEM_REGISTRY_CONTRACT=SELECTIVE_PER_ITEM_CARRIER
ONE_DECLARATION_PER_CARRIER=RETAINED
SEMANTIC_SUBJECTS=CONTROLLED_SOURCE_OWNED_POLYHIERARCHY
SUBJECT_CATALOG_MEMBERSHIP_REGISTRY=false
PRODUCTION_NAVIGATION_REALIZATION=SUBJECT_INDEX_V2
HISTORICAL_NAVIGATION=IMMUTABLE_PRE_RETIREMENT_EVIDENCE
BROAD_W5_MIGRATION=AUTHORIZED_TO_BEGIN
W5_ACCEPTED=false
W6_CUTOVER_CANDIDATE_ALLOWED=false
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=W5_F0_PRODUCTION_NAVIGATION_SUBSTRATE
```
