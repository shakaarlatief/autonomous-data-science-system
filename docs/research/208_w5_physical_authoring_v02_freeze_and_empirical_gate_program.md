# Research 208: W5 Physical/Authoring V0.2 Freeze and Empirical-Gate Program

**Date:** 2026-09-20
**Status:** PHYSICAL/AUTHORING V0.2 FROZEN / SUBJECT-REGISTRY-HISTORY EMPIRICAL GATES NEXT / BROAD W5 MIGRATION PAUSED
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Prior W5 records:** Research 206 and Research 207
**Model-collaboration basis:** MC-0018 Messages 001-004
**Last accepted project milestone:** Checkpoint 554 / W4 ACCEPTED AND FINALIZED
**Scope:** Freeze the physical repository and future-authoring subset of W5 after representative-corpus audit and ChatGPT/Claude reconciliation, while explicitly withholding freeze on subject vocabulary, item-registry identity, historical-navigation preservation and production navigation realization until empirical gates complete.
**Authority:** This record governs the W5 design program only. It does not begin broad semantic migration, switch operational authority, overwrite live compatibility surfaces, or amend Specification 028 by implication.

## 1. Why this is a partial freeze rather than a full W5 architecture freeze

Research 206 opened W5 by asking how durable ADS knowledge should actually be authored and stored in the future. Research 207 proposed V0.1 from a representative repository audit. MC-0018 then attacked that proposal against real W0-W4 implementation evidence.

The result is asymmetric:

```text
physical placement / family roles / naming / granularity / authoring
    -> sufficiently converged to freeze as V0.2

semantic-subject vocabulary and hierarchy
    -> not yet empirically demonstrated

multi-item registry identity
    -> real one-declaration-per-carrier collision remains

post-cutover historical navigation
    -> preservation mechanism not yet measured

production navigation generator realization
    -> proportionality decision intentionally deferred
```

Broad W5 migration therefore remains paused until the remaining empirical gates are resolved.

## 2. Frozen physical-information architecture V0.2

### 2.1 One physical home expresses primary responsibility only

```text
physical parent
    != exclusive semantic parent

folder path
    != semantic identity

folder path
    != authority by itself

folder path
    != complete project navigation
```

A source lives where its **primary natural responsibility** lives. Cross-cutting subject membership is handled separately.

### 2.2 Root-level families are no longer treated as one homogeneous singleton class

The future architecture distinguishes:

```text
NARRATIVE SINGLETONS
    README.md
    VISION.md
    PRINCIPLES.md
    DEVELOPMENT_METHOD.md
    CONTINUITY.md

ITEM-REGISTRY / INDEX SURFACES
    DECISIONS.md
    OPEN_QUESTIONS.md
    OPEN_ARCHITECTURE_BACKLOG.md
    exact future current-item contract still gated by T3

SELECTIVE CHRONOLOGY
    MAJOR_CHANGES.md

COMPATIBILITY / DERIVED-ROLE SURFACES
    CURRENT_STATE.md
    current_routing.json
    KNOWLEDGE_MAP.md
    current live roles remain unchanged until later qualified cutover
```

This is a semantic role split. It is not a mass-move instruction.

### 2.3 Epistemic/lifecycle families remain justified

The following remain prospective first-class families:

```text
docs/foundations/
docs/specifications/
docs/research/
docs/checkpoints/
docs/experiments/
```

They are retained because they encode distinct epistemic/lifecycle roles, not merely because the legacy repository already has those directories.

### 2.4 Natural domain/subsystem homes remain top-level

Current domain homes remain valid where the domain has independent durable responsibility:

```text
docs/cockpit/
docs/source_universe/
docs/methodological_knowledge/
docs/local_execution/
docs/model_collaboration/
docs/private_companion/
```

A generic `docs/domains/` wrapper remains rejected because it adds containment without a new semantic boundary.

A new top-level domain home is warranted only when the domain has a meaningful independent lifecycle/responsibility and enough related current knowledge to justify a natural owner area.

### 2.5 `docs/project_knowledge/` remains narrow

The project-knowledge area remains infrastructure for the project-knowledge architecture itself, not a universal destination for substantive project truth.

Its justified roles remain:

```text
architecture/
generated/
captures/
transitions/
joint_authority/
candidate navigation infrastructure
genuinely project-global project-knowledge control owners
```

A universal `docs/project_knowledge/data/` registry remains rejected.

## 3. Frozen placement precedence

When an artifact could plausibly belong to both a domain and an epistemic family, placement follows **primary responsibility**, not topic.

```text
if primary responsibility is:
    governed contract
    bounded investigation/comparison/design study
    deep durable rationale
    meaningful historical project-state boundary

then:
    epistemic/lifecycle family wins

if primary responsibility is:
    current domain operation
    domain procedure/state/control
    runbook
    resume target
    domain-local manifest
    domain-local evidence used as part of that operation

then:
    natural domain home wins
```

The diagnostic question “what breaks if this artifact is wrong?” may help resolve ambiguity, but is not itself the normative rule.

## 4. Frozen naming policy V0.2

### 4.1 New ordinary names

New ordinary directories and descriptive carriers default to:

```text
lowercase_snake_case
```

with normal extensions such as `.md` and `.json`.

### 4.2 Existing names

Existing filenames are not renamed merely for cosmetic normalization.

Established role names such as:

```text
README.md
STATE.json
RESOLUTION.md
VISION.md
PRINCIPLES.md
CONTINUITY.md
```

may remain conventional exceptions.

Mixed legacy/new casing inside a domain is acceptable when avoiding churn is semantically preferable.

### 4.3 Numbered families

`NNN_lower_snake_case.md` remains appropriate where ordered artifact/provenance identity materially helps the family, including the existing numbered Foundation, Specification, Research and Checkpoint families.

The number is artifact/provenance identity, not semantic identity.

### 4.4 Semantic identity

Semantic IDs remain separate from filenames.

A move/rename does not mint a new semantic identity merely because the path changes.

## 5. Frozen granularity policy V0.2

Prefer editing an existing natural canonical owner when the new knowledge is simply a state change, refinement or extension of the same responsibility.

A new carrier is justified when one or more of these materially apply:

```text
independent lifecycle
distinct authority scope
independent provenance/revision control
several other sources need to refer to it directly
keeping it inside the current owner would create ambiguous or duplicate authority
size/volatility would operationally overload the current owner
the item must be a first-class durable typed-relation target
```

The last condition matters because Specification 028 relations target semantic IDs, not carrier paths.

This policy rejects both mega-documents and one-file-per-claim atomization.

## 6. Frozen future-authoring principles

The authoring flow must follow these rules:

```text
1. update an existing natural owner whenever responsibility already matches

2. unreviewed/candidate understanding enters capture rather than current authority

3. specific governed/evidence families are considered before the broad Research bucket

4. placement uses primary responsibility, not subject topic

5. orientation/routing/indexing contains no unique accepted truth

6. machine-checkable constraints must be visible in the authoring contract,
   not discovered only after validator failure

7. no new global summary copy is created merely because knowledge is important
```

The final detailed decision tree will be codified after T1/T3/T4 close the remaining ambiguous families.

## 7. Item-registry architecture: converged direction, empirical T3 still required

MC-0018 verified a real structural problem:

```text
Specification 028:
    at most one declaration block per carrier

relation target:
    semantic ID only

therefore:
    independently meaningful items inside a multi-item registry cannot all
    become first-class relation targets while remaining anchor-only
```

D-011 is a concrete example: its scoped supersession by several later decisions is expressible conceptually through typed relations but cannot be fully represented while D-011 and most successors lack independent semantic identities.

The converged direction entering T3 is:

```text
ONE DECLARATION PER CARRIER REMAINS

current governing items needing first-class identity
    -> selective individual canonical carriers

legacy aggregate registry content
    -> historical evidence after still-current items migrate/disposition

current browsing/discovery surface
    -> generated/derived index over current item carriers

path-target relations
    -> rejected
```

T3 must compare:

```text
A  selective per-item carrier
B  scoped multi-declaration carrier
C  anchor-only item
```

using D-011 as the primary difficult case and AB-032 as the secondary W4-proven case.

The exact future item-family paths remain unfrozen until T3.

## 8. Subject/navigation architecture: controlled vocabulary required, empirical T1 next

W0-W4 implementation evidence changes one earlier assumption.

The existing generated `subject_index.json` demonstrates multi-axis emission, but the current axes do not yet demonstrate useful semantic grouping.

The schema explains why:

```text
scope:*      open resolver/matching vocabulary
kind         free text
profile      controlled representation vocabulary
lifecycle    controlled state vocabulary
authority    controlled authority vocabulary
```

Resolver/matching facets and semantic subjects therefore cannot be treated as the same vocabulary.

The V0.2 candidate entering T1 is:

```text
AUTHORED SEMANTIC SUBJECTS
    controlled vocabulary
    memberships owned beside participating sources/candidate annotations
    optional preferred route
    polyhierarchical parentage

DERIVED STRUCTURAL FACETS
    profile
    kind
    authority state
    lifecycle state
    workstream/dependency
    privacy/access
    physical domain where useful
    temporal/evidence facets

RESOLVER FACETS
    scope:*
    remain matching semantics
    exposed for navigation only where later evidence justifies it
```

### 8.1 Vocabulary-only catalog candidate

The preferred V1 candidate is a narrow vocabulary catalog that may define:

```text
subject ID
label
description
zero or more broader parents
optional preferred parent
aliases
status / merge redirect when needed
```

It must **never list members**.

Membership remains source-owned.

A subject catalog is therefore a closed-vocabulary/parentage contract, not a substantive project-content registry.

### 8.2 Subject-as-source alternative

One-carrier-per-subject remains a falsifiable fallback, but is not the preferred V1 design because it would:

```text
over-reify navigation vocabulary into project semantic sources
increase governed-source/identity machinery
risk conflating navigation parentage with authority relations
create one file per subject even where vocabulary maintenance is the only need
```

T1 will test the lighter vocabulary-catalog design first.

### 8.3 T1 must remain non-authoritative

T1 will use real representative carriers plus candidate annotations held outside production authority.

It must not retrofit speculative navigation metadata into production sources.

Useful diagnostics include:

```text
members per subject
distinct values / members
singleton rate
coverage
overlap
multi-parent usefulness
placement agreement
reduction in ad hoc axes
cold navigation/reconstruction usefulness
```

No arbitrary numeric threshold is frozen in advance.

## 9. Historical navigation: evidence preservation, not derived rebuildability

The legacy Knowledge Map currently carries curated historical subject routing that a flat artifact inventory does not replace.

Before retirement, the final qualified legacy subject-to-artifact mapping must be preserved.

The candidate lifecycle is:

```text
authority_class    evidence
purpose            one-time historical-navigation migration evidence
input              exact final qualified legacy Knowledge Map boundary
substantive truth  none
future rebuild     not claimed after the legacy input retires
```

It should not masquerade as a derived view requiring post-retirement rebuildability.

T4 must first measure cold historical retrieval with the live Knowledge Map withheld. The exact evidence shape is designed from that observed need.

## 10. W0-W4 architecture-conformance findings adopted into W5

### 10.1 Strengthened assumptions

```text
source-local natural ownership
selective identity instead of universal identity
exact Git-byte generator binding
structural COMMIT-snapshot discipline
complete-input full/incremental equivalence
capture non-authority
revision-bound promotion
narrow docs/project_knowledge boundary
project_boundary.v1 promoted-branch/commit semantics
```

### 10.2 Revised assumptions

```text
multi-axis grouping is not yet demonstrated merely because axes exist
one-declaration-per-carrier needs selective per-item carriers for first-class items
shared generator implementation closures are too coarse
historical navigation needs explicit preservation before Knowledge Map retirement
pure-unit execution should not expand automatically into every new W5 mechanism
```

### 10.3 Explicit non-changes

```text
no universal semantic IDs
no path-target typed relations
no universal central registry
no mass historical declaration retrofit
no general multiple-declarations-per-carrier escape hatch
no automatic scope-facet proliferation into navigation
no reopening W0-W4 acceptance
```

## 11. C1 pre-navigation implementation obligation

All eight persistent view specifications currently reuse one maximal `implementation_files` closure.

That means any byte change to any listed generator/schema dependency invalidates every view manifest.

C1 is accepted as a W5 MUST-FIX before production navigation work:

```text
goal:
    bind each view to the smallest explicit implementation closure
    that actually determines that view's generated semantics

preserve:
    explicit ordered paths
    exact GIT_BLOB_BYTES_AT_COMMIT digest basis
    deterministic rebuild
    complete-input semantics
    full/incremental equivalence
    circularity guards
    global canonical-source integrity
```

Narrowing implementation-file closures must not weaken global source-integrity checks.

## 12. Pure-unit execution proportionality

The existing restricted pure-unit execution layer remains accepted.

It must not be extended for T1/T3/T4 merely because those experiments involve navigation or projections.

```text
T1/T3/T4
    research/test/prototype surfaces only

after empirical success
    explicit decision:
        extend production pure-unit layer
        OR
        use a smaller qualified generation path
```

This is a forward proportionality rule, not a rollback of W0.

## 13. Empirical-gate sequence

The next W5 sequence is:

```text
C1
    narrow production view implementation closures

T1
    controlled subject-vocabulary candidate corpus

T3
    item-registry identity/carrier comparison

T4
    cold historical-navigation reconstruction without live Knowledge Map

then:
    reconcile empirical evidence
    freeze subject + item-registry + historical-navigation contracts
    decide production navigation realization
    codify the full W5 target contract
    only then begin broader current semantic migration
```

## 14. Collaboration disposition

MC-0018 completed the architecture-dialogue role needed before empirical work.

No further Claude design turn is required before C1/T1/T3/T4.

If empirical evidence later creates a material architectural ambiguity, open a new narrowly scoped review using whichever collaborator has the needed evidence access. Claude can review repository-contained architecture/evidence; Claude Code may be used in future when the task materially requires local-machine access.

## 15. Current boundary

```text
W4=ACCEPTED_AND_FINALIZED
W5=IN_PROGRESS
W5_PHYSICAL_AUTHORING_V02=FROZEN
W5_SUBJECT_ARCHITECTURE=NOT_FROZEN / T1
W5_ITEM_REGISTRY_CONTRACT=NOT_FROZEN / T3
W5_HISTORICAL_NAVIGATION=NOT_FROZEN / T4
C1_IMPLEMENTATION_GRANULARITY=MUST_FIX
PROJECT_BOUNDARY_PROFILE=RETAIN
PURE_UNIT_EXTENSION=EXPLICIT_PROPORTIONALITY_DECISION_REQUIRED
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=C1_THEN_T1_T3_T4
```
