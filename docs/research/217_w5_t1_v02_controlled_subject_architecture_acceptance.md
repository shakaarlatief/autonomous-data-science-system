# Research 217: W5 T1 V0.2 Controlled Subject Architecture Acceptance

**Date:** 2026-09-20
**Status:** T1 ACCEPTED / CONTROLLED SUBJECT ARCHITECTURE FROZEN
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**V0.1 calibration:** Research 215 / MC-0019
**V0.2 fixture:** Research 216
**V0.2 blind calibration:** MC-0020
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Scope:** Reconcile the V0.2 deterministic 65-carrier experiment and the second blind 24-carrier calibration, freeze the V1 semantic-subject contract, and identify bounded definition clarifications for production realization.
**Authority:** W5 design result only. This does not yet add navigation metadata to production sources, change source authority, replace the legacy Knowledge Map, begin broad semantic migration, or switch operational authority.

## 1. Why T1 existed

W3 proved that Candidate 01 can emit multi-axis navigation, but the existing `kind`, `profile` and `scope:*` axes were structural/resolver facets rather than demonstrated semantic subjects.

T1 therefore tested whether a small controlled semantic-subject vocabulary could organize real repository knowledge without:

```text
turning folder paths into semantic parentage
turning resolver scopes into navigation ontology
creating one central member registry
mass-retrofitting historical files
or creating one file per subject
```

## 2. V0.2 primary corpus result

V0.2 uses the same 65-carrier representative corpus as V0.1, with explicit subject definitions, include/exclude guidance, an explicit secondary-membership threshold and the added `admissibility-authority` subject.

```text
corpus artifacts                 65
assignable subjects              18
total memberships                94
mean memberships/artifact        1.446
median memberships/artifact      1
multi-subject artifacts          23 / 65 (35.4%)
no unique preferred route        1
zero-member subjects             0
singleton subjects               0
legacy Knowledge Map coverage    63 / 65 (96.9%)
preferred-route legacy alignment 59 / 62 (95.2%)
candidate navigation scenarios   9 / 9 PASS
legacy comparator scenarios      4 / 9 PASS
```

The controlled vocabulary remains useful under the stricter membership threshold and does not depend on dense tagging.

## 3. Blind calibration result

MC-0020 reused exactly the same 24 carriers and source boundary as MC-0019 but exposed the refined V0.2 reviewer catalog in a fresh Claude Opus conversation.

```text
metric                           V0.1        V0.2        change
exact full subject sets          29.2%       66.7%       +37.5 pp
mean subject-set Jaccard         0.642       0.852       +0.210
median subject-set Jaccard       0.500       1.000       +0.500
micro membership F1              0.753       0.867       +0.115
preferred-route agreement        91.7%       91.7%       unchanged
absolute membership-count gap    13          5           -8
```

The revised contract materially improves multi-membership reproducibility while preserving the already-strong default-route signal.

Claude also reports that the definitions, paired include/exclude clauses and secondary-membership rule materially helped placement.

## 4. Accepted membership rule

The V1 authoring rule is:

> Assign a semantic subject only when the carrier substantively develops, governs, specifies, evaluates, or preserves durable meaning about that subject.

The following are not sufficient on their own:

```text
mere mention
dependency
implementation adjacency
generic cross-cutting relevance
artifact family
authority class
lifecycle
workstream
physical domain
resolver scope
```

Every secondary subject must independently clear the same threshold.

## 5. Preferred route contract

`preferred_subject` is the best default semantic navigation route for the carrier's primary purpose.

`preferred_subject = null` is allowed only when two or more assigned subjects are genuinely co-primary and no unique default route is defensible.

This is navigation only. It does not change source authority or semantic identity.

## 6. Constitutional and summary carriers

A constitutional or summary carrier receives a secondary subject only when that carrier itself states durable governing meaning for the subject.

Merely summarizing, indexing, or routing to a detailed owner is insufficient.

This prevents broad root documents from becoming universal tags while preserving subject membership for genuinely governing principles.

## 7. Final vocabulary structure

The V1 controlled vocabulary contains:

```text
6 non-assignable navigation parents
18 assignable semantic subjects
```

Assignable subjects:

```text
system-identity
project-orchestration
knowledge-representation
admissibility-authority
evaluation-assurance
runtime-persistence
retrieval-context
recommendation-action
methodological-knowledge
source-universe
development-governance
project-knowledge-architecture
model-collaboration
tooling-integrations
cockpit-product
cockpit-interaction
cockpit-visual-language
cockpit-implementation
```

The subject catalog is a vocabulary/parentage contract only and must never enumerate source members.

## 8. Bounded definition clarifications from MC-0020

These clarifications are accepted for production realization without another blind round because they resolve localized wording/scope ambiguity and do not change the subject graph.

### 8.1 `knowledge-representation`

Production wording should emphasize representation, relation, versioning, invalidation, consolidation, promotion and lifecycle mechanics.

Activation in the sense of selecting relevant knowledge for a concrete reasoning context belongs to `retrieval-context`.

### 8.2 `development-governance`

Production wording explicitly includes:

```text
repository integrity
CI and validation gates
risk-scaled development verification
checkpoint and routing integrity
development qualification evidence
```

No new Level-2 verification subject is introduced.

### 8.3 `tooling-integrations`

Tool-specific capability, sandbox, permission, approval and execution-lane semantics remain part of the tool/integration subject when they are properties of that development surface.

They do not become product `admissibility-authority` merely because the word permission is used.

### 8.4 `cockpit-product`

The subject ID remains stable.

Its production human label/definition should make explicit that it covers the ADS professional product-interface architecture as realized through the promoted Project Cockpit product/world/control model, including durable frontend/interface foundations that predate the current Cockpit terminology.

This avoids adding a speculative second product-interface leaf while preserving a route for the durable professional-interface foundation.

## 9. Missing-vocabulary disposition

MC-0020 raised three recurring pressures:

```text
Level-2 verification / CI assurance
development-time execution authority / permission
professional product interface / frontend quality
```

All three are representable through the clarified existing subjects above.

A weaker prospective reporting/deliverables pressure is intentionally not allocated a subject until current corpus evidence requires one.

The controlled vocabulary is designed to evolve prospectively through stable IDs, aliases, status and merge redirects rather than pre-allocating speculative ontology.

## 10. Subject hierarchy semantics

```text
broader[]
    semantic/navigation polyhierarchy
    multiple parents allowed

preferred_parent
    deterministic display/default hierarchy only
    does not narrow subject meaning

parent nodes
    may be non-assignable navigation structure
    source memberships are authored only to assignable subjects
```

## 11. Structural and resolver facets remain separate

The accepted subject layer does not absorb:

```text
profile
kind
authority state
lifecycle state
workstream/dependency
privacy/access
physical domain
temporal/evidence facets
scope:* resolver matching
```

Those remain generated/structural or resolver axes.

## 12. Production realization contract

The preferred production realization is:

```text
docs/project_knowledge/navigation/subject_catalog.json
    vocabulary and parentage only

source-local optional navigation metadata
    subjects[]
    preferred_subject

generated navigation projection
    semantic subjects kept explicitly distinct from structural/resolver facets
```

Membership must never move into the catalog.

The exact schema/parser/view implementation belongs to the next W5 production-realization step.

## 13. T1 result

```text
T1=ACCEPTED
W5_SUBJECT_ARCHITECTURE=FROZEN
CONTROLLED_VOCABULARY=ACCEPTED
ASSIGNABLE_SUBJECTS=18
NON_ASSIGNABLE_PARENTS=6
MEMBERSHIP_SOURCE_OWNED=true
CENTRAL_MEMBER_REGISTRY=false
PREFERRED_ROUTE_OPTIONAL=true
POLYHIERARCHY=true
STRUCTURAL_FACETS_SEPARATE=true
RESOLVER_SCOPE_SEPARATE=true
V0_2_BLIND_CALIBRATION=PASS
BROAD_W5_MIGRATION=STILL_PAUSED_PENDING_FULL_W5_RECONCILIATION
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=RECONCILE_C1_T1_T3_T4_AND_FREEZE_FULL_W5_INFORMATION_ARCHITECTURE
```
