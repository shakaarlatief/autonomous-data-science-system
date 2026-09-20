# Research 215: W5 T1 V0.1 Controlled Subject Vocabulary Calibration Result

**Date:** 2026-09-20
**Status:** T1 V0.1 DIRECTION SUPPORTED / PRODUCTION FREEZE WITHHELD / V0.2 REFINEMENT REQUIRED
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**T1 fixture freeze:** Research 210
**Blind calibration:** MC-0019
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Scope:** Interpret the 65-carrier primary T1 experiment together with the independent 24-carrier Claude blind placement calibration and decide whether the V0.1 semantic-subject contract is ready for production freeze.
**Authority:** W5 design evidence only. This result does not modify production source declarations, create production navigation metadata, replace the legacy Knowledge Map, begin broad W5 semantic migration, or switch operational authority.

## 1. Primary experiment result

The frozen ChatGPT-authored candidate corpus shows that a small controlled semantic-subject vocabulary can group real ADS knowledge substantially more usefully than the broad legacy topic layer on the bounded task-shaped probes.

```text
corpus artifacts                 65
assignable subjects              17
total memberships                121
mean memberships/artifact        1.862
median memberships/artifact      2
multi-subject artifacts          50 / 65 (76.9%)
zero-member subjects             0
singleton subjects               0
legacy Knowledge Map coverage    63 / 65 (96.9%)
preferred-route legacy alignment 56 / 60 (93.3%)
candidate navigation scenarios   8 / 8 PASS
legacy comparator scenarios      2 / 8 PASS
```

This rejects the concern that a controlled semantic-subject layer would necessarily reproduce folder structure, artifact families, or resolver scopes. The candidate vocabulary created useful cross-cutting neighborhoods and preserved polyhierarchy.

## 2. Independent blind calibration result

MC-0019 used a fresh Claude session against the frozen 24-source reviewer subset without exposing ChatGPT's candidate annotations, T1 scenarios, generated T1 outputs or the legacy Knowledge Map.

The comparison is:

```text
exact full subject sets          7 / 24  (29.2%)
preferred-route agreement        22 / 24 (91.7%)
mean subject-set Jaccard         0.642
median subject-set Jaccard       0.500
micro membership precision       0.889
micro membership recall          0.653
micro membership F1              0.753
ChatGPT memberships              49
Claude memberships               36
```

The strongest signal is that the two reviewers generally agree on the best default route but disagree materially on whether additional secondary subjects are warranted.

This is not evidence that the subject neighborhoods themselves are incoherent. It is evidence that V0.1 leaves the **membership admission threshold** under-specified.

## 3. Membership admission rule required for V0.2

V0.2 must state explicitly:

> A carrier receives a semantic-subject membership only when it substantively develops, governs, specifies, evaluates, or preserves durable meaning about that subject. Mere mention, dependency, implementation adjacency, or generic cross-cutting relevance is insufficient.

The production authoring contract must further distinguish:

```text
preferred_subject
    best default semantic navigation route for the carrier's primary purpose

preferred_subject = null
    allowed only when two or more subjects are genuinely co-primary

secondary subject
    substantial durable semantic content, not weak association

artifact family / authority / lifecycle / workstream / physical domain
    separate axes, not substitutes for subjects
```

## 4. Missing semantic neighborhood: admissibility / authority

Claude identified one explicit missing-vocabulary pressure around admissibility and authority.

Independent repository inspection confirms this is a durable ADS concept rather than a one-document anomaly. It appears repeatedly in:

```text
docs/VISION.md
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

Foundation 003 explicitly distinguishes whether an action is permitted from the level of assurance/review/control required for an action that is permitted. The coverage map also keeps the admissibility/governance neighborhood distinct from assurance.

V0.2 therefore adds a candidate assignable subject:

```text
admissibility-authority
```

with scope covering:

```text
permission to act
binding admissibility constraints
authority to approve or accept
residual-risk acceptance authority
action-specific human gates
```

and excluding generic repository governance or generic evaluation rigor.

## 5. Subject definitions are required

V0.1 labels alone caused predictable reviewer drift.

V0.2 must add for every assignable subject:

```text
description
include_when
exclude_when
```

and explicitly define:

```text
preferred_parent
    display/default navigation parent only
    does not narrow semantic meaning

broader[]
    semantic/navigation polyhierarchy

legacy_topics
    migration/comparison metadata only
    never placement guidance

membership
    source-owned
    never centrally enumerated in the subject catalog
```

## 6. Important boundary clarifications

### knowledge-representation vs methodological-knowledge

`knowledge-representation` covers how reusable knowledge is represented, activated, related, versioned, invalidated, consolidated and promoted.

`methodological-knowledge` covers the substantive methodological corpus/universe, its coverage, acquisition, organization and domain knowledge.

A source receives both only when it materially develops both concerns.

### development-governance vs project-knowledge-architecture

`development-governance` covers repository/development operating method, continuity, collaboration, review, commit/checkpoint discipline and routing method.

`project-knowledge-architecture` covers architecture for preserving, owning, identifying, reconstructing, migrating and navigating project-development knowledge.

The distinction is subject-matter based, not current-versus-successor status.

### tooling-integrations vs runtime-persistence

`tooling-integrations` covers developer/tooling/integration surfaces used to build, operate or connect ADS.

`runtime-persistence` covers durable runtime state, execution substrate and persistence behavior of the ADS system itself.

A local execution bridge belongs to tooling-integrations unless it also materially defines product runtime/persistence semantics.

### Cockpit subjects

Broad Cockpit architecture artifacts may legitimately receive several of `cockpit-product`, `cockpit-interaction`, `cockpit-visual-language` and `cockpit-implementation` when they materially develop each concern.

## 7. Product-versus-project is not duplicated into the subject taxonomy

Claude correctly observed that some semantic neighborhoods occur in both product architecture and project-development operations.

T1 does not respond by cloning subjects into product and project versions.

The product/project distinction is orthogonal and remains expressible through physical ownership, source purpose, artifact family, lifecycle/workstream and other structural facets.

For example, Source Universe architecture research and the Source Vault bootstrap workstream may both belong to `source-universe` while still being distinguishable through their other axes.

## 8. T1 V0.1 disposition

```text
CONTROLLED_SUBJECT_ARCHITECTURE_DIRECTION=SUPPORTED
PRIMARY_PREFERRED_ROUTE_SIGNAL=STRONG
MULTI_MEMBERSHIP_ADMISSION_RULE=UNDER_SPECIFIED
ADMISSIBILITY_AUTHORITY_SUBJECT=MISSING_IN_V0_1
V0_1_PRODUCTION_FREEZE=WITHHELD
T1=CONTINUES
```

V0.1 is a successful discriminator, not an accepted production contract.

It validates the architectural direction and narrows the remaining problem to explicit subject definitions, membership discipline and one missing semantic neighborhood.

## 9. Required V0.2 test

Before production subject freeze, create a revised controlled vocabulary with:

```text
18 assignable subjects
explicit descriptions
include_when / exclude_when guidance
display-only preferred-parent semantics
explicit multi-membership admission rule
admissibility-authority subject
```

Then perform a fresh blind calibration against the revised catalog.

The acceptance target is qualitative plus empirical:

```text
preferred/default routes remain highly stable
membership-set agreement materially improves
missing-vocabulary pressure is low
no central membership registry is needed
no structural/resolver axes are smuggled back into semantic subjects
```

Exact identical multi-label sets are not required as an artificial objective.

## 10. Current W5 boundary

```text
C1=ACCEPTED
T3=ACCEPTED
T4=ACCEPTED
T1_V0_1=DIRECTION_SUPPORTED_NOT_FROZEN
T1_V0_2=NEXT
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
