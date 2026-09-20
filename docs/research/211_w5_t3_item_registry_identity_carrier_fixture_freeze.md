# Research 211: W5 T3 Item-Registry Identity / Carrier Fixture Freeze

**Date:** 2026-09-20
**Status:** T3 FIXTURE FROZEN / EXECUTION NOT YET PERFORMED
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**C1 qualification:** Research 209 / ACCEPTED
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Scope:** Freeze the empirical comparison for first-class identity inside aggregate decision/backlog registries before choosing the final W5 item-registry carrier contract.
**Authority:** Research fixture freeze only. It does not split live registry files, permit multiple declarations per carrier, create new canonical item identities, start broad W5 migration, or change operational authority.

## 1. Question

T3 asks:

> When one item inside an aggregate registry has an independent lifecycle or must participate in typed semantic relations, should ADS give that item a selective standalone carrier, change the substrate to support multiple declarations in one carrier, or keep anchor-only identity?

## 2. Why the question is real

The current contracts create a genuine tension:

```text
Specification 028 / declaration parser
    one structured declaration per Markdown carrier

typed authority relations
    target semantic IDs

current aggregate registries
    may contain many independently meaningful items
```

Anchor-only items therefore cannot automatically participate as first-class typed relation targets.

## 3. Frozen alternatives

```text
A  SELECTIVE PER-ITEM CARRIER
    independently governed item gets its own natural carrier + semantic ID
    existing one-declaration-per-carrier substrate remains

B  MULTIPLE DECLARATIONS IN ONE CARRIER
    preserve aggregate file physically
    change parser/discovery/source-revision semantics to admit several governed units

C  ANCHOR-ONLY ITEM
    preserve current aggregate file and heading reference
    no first-class semantic identity for the item
```

## 4. Primary case: D-011

`D-011` remains applicable to implementation subsystems not yet selected but is superseded in distinct scopes by:

```text
D-028  v1_persistence_retrieval_architecture
D-029  persistence_tooling
D-030  python_project_dependency_tooling
D-031  reusable_knowledge_interchange
D-032  initial_reasoning_runtime
D-033  source_universe_substrate
D-035  project_development_knowledge_architecture
```

This is a stronger test than a simple all-or-nothing replacement because a correct representation must preserve both seven scoped successor resolutions and the residual D-011 base.

Research 161 previously established shadow support for the six-successor version of this case. T3 now uses the accepted production schema/parser/resolver to compare carrier alternatives rather than merely prove that scoped supersession is representable.

## 5. Secondary case: AB-032

`AB-032: Governed Git branch lifecycle policy` currently lives as a heading inside `docs/OPEN_ARCHITECTURE_BACKLOG.md`.

W4 preserved provenance to it as a path-plus-heading reference. The item has its own OPEN/deferred lifecycle and may later need durable first-class reference.

T3 therefore also asks whether:

```text
standalone AB-032 semantic identity
    can satisfy an exact required-authority reference

versus

anchor-only AB-032
    cannot satisfy that semantic-ID requirement
```

This does not assert that AB-032 must become canonical now. It tests the capability difference.

## 6. Mechanical use of production mechanisms

The evaluator imports the real:

```text
SchemaValidator
parse_markdown
resolve_authority
semantic_source.v1 / relation contract
```

It does not modify production code or live registry files.

Option A is represented using the current natural relation direction: each scoped successor owns a `REPLACE` relation targeting `D-011`.

Option B constructs two otherwise valid declarations inside one Markdown carrier and records whether the current parser accepts that cardinality.

Option C deliberately leaves the aggregate base without a semantic ID and tests the resulting relation/required-authority behavior.

## 7. Interpretation

T3 is not a file-count aesthetics test.

The preferred design must minimize semantic and implementation complexity while preserving:

```text
first-class reference integrity where justified
independent lifecycle where justified
scoped supersession
residual applicability
move/rename continuity
selective rather than universal identity
no duplicate current authority during migration
```

A result favoring A would not authorize mass historical splitting. It would support the Research 208 rule that a separate carrier is justified only when independent lifecycle/authority/provenance/revision or first-class relation targeting materially requires it.

## 8. Frozen files

```text
experiments/project_knowledge_item_registry_t3/README.md
experiments/project_knowledge_item_registry_t3/fixture.json
experiments/project_knowledge_item_registry_t3/evaluate.py
```

## 9. Boundary

```text
T3_FIXTURE=FROZEN
T3_EXECUTION=NOT_STARTED
ITEM_REGISTRY_CONTRACT=NOT_FROZEN
ONE_DECLARATION_PER_CARRIER=CURRENT_CONTRACT
LIVE_REGISTRIES=UNCHANGED
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=EXECUTE_T3_AND_INTERPRET_RESULT
```
