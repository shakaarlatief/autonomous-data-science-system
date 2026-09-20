# Research 216: W5 T1 V0.2 Subject Vocabulary Refinement and Blind-Calibration Fixture

**Date:** 2026-09-20
**Status:** T1 V0.2 FIXTURE FROZEN / SECOND BLIND CALIBRATION NEXT
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**T1 V0.1 disposition:** Research 215
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Scope:** Freeze the refined V0.2 controlled semantic-subject vocabulary, revised 65-carrier candidate annotations and second blind-calibration contract after MC-0019 exposed ambiguity in secondary membership admission.
**Authority:** Research fixture only. It does not create production subject metadata, mutate canonical source declarations, begin broad W5 migration, replace the legacy Knowledge Map, or change operational authority.

## 1. What V0.1 established

V0.1 produced strong primary navigation evidence:

```text
preferred-route legacy alignment 56 / 60 (93.3%)
bounded candidate scenarios      8 / 8 PASS
blind preferred-route agreement  22 / 24 (91.7%)
```

But exact blind multi-label agreement was only 7/24, with Claude using 36 memberships where ChatGPT used 49 on the same subset. The dominant failure mode was an undefined threshold for secondary membership rather than disagreement about the best route.

Claude also identified admissibility/authority as a missing semantic neighborhood. Repository inspection confirmed that admissibility is explicitly distinguished from assurance in the durable ADS foundations and methodological coverage map.

## 2. V0.2 membership contract

V0.2 adds a normative admission rule:

> Assign a subject only when the carrier substantively develops, governs, specifies, evaluates, or preserves durable meaning about that subject. Mere mention, dependency, implementation adjacency, generic cross-cutting relevance, artifact family, authority class, lifecycle, workstream, physical domain, or resolver scope is insufficient.

Every secondary subject must independently satisfy the same threshold.

The preferred route is the best default semantic navigation route for the carrier's primary purpose. `null` is allowed only when two or more subjects are genuinely co-primary.

## 3. V0.2 vocabulary contract

Each assignable subject now contains:

```text
description
include_when
exclude_when
broader[]
preferred_parent
legacy_topics
```

`preferred_parent` is explicitly a display/default navigation parent and does not narrow subject meaning.

`legacy_topics` is comparison/migration metadata only and must not guide placement.

Membership remains source-owned or source-adjacent. The catalog cannot enumerate source members.

## 4. New subject: admissibility-authority

V0.2 adds:

```text
admissibility-authority
    permission to act
    binding admissibility constraints
    authority to approve or accept
    residual-risk acceptance authority
    permission-triggered human gates
```

It explicitly excludes generic project governance and generic evaluation rigor.

This keeps permission/authority separate from `evaluation-assurance`, which concerns evaluation, falsification, assurance intensity and execution integrity.

## 5. Boundary refinements

V0.2 clarifies the boundaries that caused reviewer drift:

```text
knowledge-representation
    reusable knowledge representation/activation/lifecycle mechanics

methodological-knowledge
    substantive Methodological Knowledge Universe and its coverage/content

development-governance
    repository/development operating method

project-knowledge-architecture
    ownership/identity/preservation/reconstruction/migration/navigation
    of project-development knowledge

tooling-integrations
    developer tools, local execution bridges and external integration surfaces

runtime-persistence
    product runtime state, persistence and durable execution substrate
```

Broad Cockpit artifacts may receive several Cockpit subjects only when each concern is materially developed.

## 6. Revised 65-carrier annotation profile

The same source corpus is reused so V0.1 and V0.2 remain comparable.

V0.2 intentionally applies the stricter substantive-content threshold:

```text
memberships                 121 -> 94
mean memberships/artifact   1.862 -> 1.446
median memberships/artifact 2 -> 1
multi-subject artifacts     50 -> 23
assignable subjects         17 -> 18
zero-member subjects        0
singleton subjects          0
```

This is not an attempt to optimize agreement mechanically. It removes generic secondary tags that did not meet the clarified semantic threshold while preserving real multi-subject sources.

## 7. Preliminary deterministic self-check

Before blind review, the frozen fixture produced:

```text
candidate navigation scenarios   9 / 9 PASS
legacy comparator scenarios      4 / 9 PASS
preferred-route legacy alignment 59 / 62 (95.2%)
```

The new admissibility-authority probe passes while the evaluation-assurance probe still passes independently, demonstrating that splitting permission/authority from assurance does not remove the assurance neighborhood.

Generated self-check outputs are deliberately excluded from the blind reviewer target and will be regenerated after independent placement is frozen.

## 8. Second blind calibration design

The second calibration uses the same 24 carriers as MC-0019 so any change in placement agreement is interpretable against the refined contract rather than a changed sample.

A fresh reviewer receives only:

```text
subject_catalog_candidate_v02.json
reviewer_subset_v02.json
the 24 exact source-boundary carriers
```

It must not read:

```text
corpus_annotations_v02.json
navigation_scenarios_v02.json
any V0.2 generated result/projection output
Research 215/216 interpretation before freezing placement
prior MC-0019 placement/comparison messages
```

The goal is controlled remeasurement, not discussion.

## 9. Acceptance question

T1 V0.2 may freeze only if the second blind pass shows:

```text
high preferred-route stability
material improvement in multi-membership agreement
low or no repeated missing-vocabulary pressure
no need for central membership
no collapse into structural/resolver facets
```

Exact identical multi-label sets are not required as an artificial threshold.

## 10. Boundary

```text
T1_V0_2_FIXTURE=FROZEN
T1_V0_2_BLIND_CALIBRATION=NEXT
PRODUCTION_SUBJECT_CONTRACT=NOT_FROZEN
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
