# Research 213: W5 T4 Historical Navigation Preservation Fixture Freeze

**Date:** 2026-09-20
**Status:** T4 FIXTURE FROZEN / EXECUTION NOT YET PERFORMED
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**C1 qualification:** Research 209 / ACCEPTED
**T3 result:** Research 212 / ACCEPTED
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Legacy Knowledge Map SHA-256:** `a212bb2bf5ba2fa7f9e19e573932c3663dc83b02d980373dcd8f811d03b2d291`
**Scope:** Freeze a content-bound compact representation of legacy subject routing and cold-navigation probes before deciding what historical navigation evidence must survive eventual Knowledge Map retirement.
**Authority:** Research fixture freeze only. It does not retire the live Knowledge Map, create successor navigation authority, alter historical files, or change operational authority.

## 1. T4 question

T4 asks:

> If the live legacy Knowledge Map is unavailable, what is the smallest durable evidence representation that still preserves its historical subject routing and checkpoint-topic navigation without keeping the entire prose document as a second active navigation authority?

## 2. Why flat inventory is not enough

A high-recall artifact inventory can prove that a file exists. It does not preserve authored relations of the form:

```text
subject -> artifact
checkpoint-number range -> subject(s)
specialized domain -> dedicated navigation surface
```

Research 208 therefore required explicit historical-routing preservation before Knowledge Map retirement rather than silently degrading to path inventory.

## 3. Frozen compact evidence candidate

`historical_navigation_candidate.json` is generated once from the exact source-boundary Knowledge Map and records:

```text
source boundary
source path
source SHA-256
authority_class = evidence_candidate
rebuildability claim = NONE_AFTER_SOURCE_RETIREMENT

19 subject records:
    topic_id
    label
    short description
    explicit artifact paths

31 compact checkpoint ranges:
    start
    end
    one or more topic IDs

5 specialized domain index paths
```

The candidate deliberately excludes general maintenance prose, current-state prose and other Knowledge Map content that is not needed to preserve the routing relation itself.

## 4. Cold queries

The frozen query set exercises eight legacy subjects:

```text
system-identity
runtime-persistence
recommendation-action
source-universe
development-governance
cockpit-world
conversation-workspace
canonical-history
```

and seven checkpoint numbers spanning the project history:

```text
5
110
140
200
267
300
554
```

The specialized-index list is also tested.

## 5. Evaluation contract

The evaluator independently reparses the exact source-boundary Knowledge Map and requires exact structural parity with the compact evidence.

Only after that check does the cold-navigation phase use the compact evidence to answer subject and checkpoint queries.

Pass evidence requires:

```text
19/19 subject structures preserved
31/31 checkpoint ranges preserved
5/5 specialized indexes preserved
all frozen subject queries exact
all frozen checkpoint queries exact
source digest exact
live working-tree Knowledge Map unnecessary for the cold-query phase
```

The experiment also reports the byte-size ratio between full Markdown and compact evidence. Size is diagnostic rather than a pass/fail criterion.

## 6. Lifecycle interpretation under test

If T4 passes, the intended future lifecycle is:

```text
before legacy Knowledge Map retirement
    capture exact final qualified routing map
    content-bind it to exact source bytes/ref
    classify it as evidence

after retirement
    preserve it immutably as migration/historical-navigation evidence
    allow successor navigation to consult it for legacy routing
    do not treat it as substantive semantic authority
    do not promise regeneration after the retired source disappears
```

This is intentionally different from a normal derived view.

## 7. Frozen files

```text
experiments/project_knowledge_historical_navigation_t4/README.md
experiments/project_knowledge_historical_navigation_t4/historical_navigation_candidate.json
experiments/project_knowledge_historical_navigation_t4/cold_queries.json
experiments/project_knowledge_historical_navigation_t4/evaluate.py
```

## 8. Boundary

```text
T4_FIXTURE=FROZEN
T4_EXECUTION=NOT_STARTED
LEGACY_KNOWLEDGE_MAP=STILL_LIVE
HISTORICAL_NAVIGATION_CONTRACT=NOT_FROZEN
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=EXECUTE_T4_AND_INTERPRET_RESULT
```
