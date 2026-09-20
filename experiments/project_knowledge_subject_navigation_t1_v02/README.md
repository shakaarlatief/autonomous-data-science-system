# W5 T1 V0.2: Refined Controlled Semantic-Subject Vocabulary

**Status:** Frozen non-authoritative research fixture before second blind calibration
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Authority:** Research fixture only. Nothing here is production subject metadata or current project authority.

## Why V0.2 exists

Research 215 and MC-0019 supported the controlled-subject direction but found two bounded problems in V0.1:

1. preferred/default routes were stable, but secondary membership admission was under-specified;
2. admissibility and action authority formed a durable semantic neighborhood that V0.1 did not represent separately.

V0.2 therefore keeps the same architecture but refines the authoring contract.

## Changes from V0.1

```text
assignable subjects         17 -> 18
new subject                 admissibility-authority
per-subject definitions     added
include_when                added
exclude_when                added
membership admission rule   explicit
preferred_parent semantics  explicitly display/default-only
legacy_topics semantics     explicitly comparison-only
source membership           remains outside the catalog
```

## Frozen inputs

```text
subject_catalog_candidate_v02.json
    controlled vocabulary, definitions, parent graph and membership policy

corpus_annotations_v02.json
    revised ChatGPT-authored non-authoritative placement over the same 65-carrier corpus

navigation_scenarios_v02.json
    nine task-shaped navigation probes, including admissibility-authority

evaluate_v02.py
    deterministic validator and evaluator
```

## Independence discipline

The 24-carrier reviewer subset is kept identical to MC-0019 so the second calibration can compare V0.1 and V0.2 on the same cases.

The blind reviewer may read only the V0.2 catalog, reviewer subset and exact source-boundary carriers. It must not read ChatGPT's V0.2 annotations, scenarios or generated results before freezing its answer.

## Preliminary author self-check

Before freezing the blind reviewer contract, the deterministic evaluator was run once locally against the V0.2 fixture. It reported:

```text
corpus artifacts                 65
assignable subjects              18
total memberships                94
mean memberships/artifact        1.446
median memberships/artifact      1
multi-subject artifacts          23 / 65 (35.4%)
zero-member subjects             0
singleton subjects               0
preferred-route legacy alignment 59 / 62 (95.2%)
candidate navigation scenarios   9 / 9 PASS
legacy comparator scenarios      4 / 9 PASS
```

The generated self-check outputs are intentionally not part of the blind reviewer target. They will be regenerated after independent placement is frozen.

## Acceptance boundary

V0.2 is still a candidate. Production freeze requires a fresh blind placement calibration showing that the added definitions materially improve placement consistency without creating new missing-vocabulary pressure or centralizing membership.
