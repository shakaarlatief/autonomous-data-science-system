# Research 212: W5 T3 Item-Registry Identity / Carrier Result

**Date:** 2026-09-20
**Status:** T3 ACCEPTED / SELECTIVE PER-ITEM CARRIER CONTRACT FROZEN
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**Fixture freeze:** Research 211
**Fixture commit:** `86833a1174874a3c1a8a93bb3a680c63a24efd9a`
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Scope:** Interpret the frozen T3 comparison and freeze the prospective carrier/identity rule for independently governed items currently embedded in aggregate decision/question/backlog registries.
**Authority:** W5 design result only. This result does not migrate live registry items, demote the current aggregate registries, start broad W5 semantic migration, or switch operational authority.

## 1. Execution note

The first invocation used the README's direct script form and failed before experiment logic with `ModuleNotFoundError: No module named 'tools'`. No result artifact was produced by that attempt.

The frozen evaluator was then executed as a repository module:

```text
.\.venv\Scripts\python.exe -m experiments.project_knowledge_item_registry_t3.evaluate
```

No fixture semantics changed. The README invocation is corrected prospectively in the result commit.

## 2. Mechanical result

```text
A_native_semantics_pass            true
B_requires_substrate_change        true
C_fails_typed_relation_target      true
C_fails_required_item_identity     true
```

### Option A: selective per-item carrier

All seven scoped successors resolve exactly as intended:

```text
v1_persistence_retrieval_architecture      -> D-028
persistence_tooling                        -> D-029
python_project_dependency_tooling          -> D-030
reusable_knowledge_interchange             -> D-031
initial_reasoning_runtime                  -> D-032
source_universe_substrate                  -> D-033
project_development_knowledge_architecture -> D-035
```

The residual scope still resolves to `D-011`.

A standalone `AB-032` carrier with semantic ID `AB-032` also satisfies an exact required-authority query for that identity.

### Option B: multiple declarations in one Markdown carrier

The current production parser rejects a second declaration block with:

```text
MALFORMED_DECLARATION_MARKERS
```

This is not interpreted as evidence that multi-declaration carriers are impossible. It demonstrates that choosing B would be a substrate redesign rather than a representation-only choice. It would require changes to declaration cardinality, source discovery, carrier/source revision semantics, downstream path-key assumptions, identity indexing and migration reasoning.

### Option C: anchor-only item

When the aggregate carrier has no semantic ID for `D-011`, a successor's typed `REPLACE` relation cannot resolve the target:

```text
status       MISSING_REQUIRED_AUTHORITY
diagnostic   MISSING_RELATION_TARGET
```

Likewise, anchor-only `AB-032` cannot satisfy a required semantic identity `AB-032`.

Option C therefore preserves low immediate migration cost only by leaving the motivating first-class identity/reference problem unsolved.

## 3. Architectural conclusion

T3 supports the existing Candidate 01 selective-identity principle rather than introducing a new universal object layer.

The frozen prospective rule is:

```text
ONE DECLARATION PER CARRIER REMAINS

aggregate registry item
    + no independent lifecycle/reference/authority need
    -> may remain an anchor / aggregate historical item

aggregate registry item
    + independent lifecycle, authority scope, revision/provenance need,
      or requirement to participate as a first-class typed relation target
    -> migrate selectively to its own canonical carrier + semantic ID

aggregate browsing surface
    -> may later become generated/derived or curated index
       after all still-current governing items are migrated/dispositioned
```

Multiple declaration blocks per ordinary Markdown carrier are **not** adopted for V1.

Path/heading anchors remain valid provenance/navigation references, but they are not promoted into a substitute semantic-identity mechanism.

## 4. Prospective physical homes

T3 also closes the previously deferred prospective placement question enough for W5 migration planning:

```text
first-class decision items
    docs/decisions/

first-class architecture-backlog items
    docs/architecture_backlog/

first-class open-question items, if/when durable item IDs are introduced
    docs/open_questions/
```

These directories are prospective natural homes, not instructions to split every existing aggregate item.

Where a stable human item identifier already exists, the filename should normally preserve it as a readable label while remaining distinct from semantic identity, for example:

```text
d_035_project_knowledge_architecture.md
ab_032_git_branch_lifecycle_policy.md
```

The exact open-question ID vocabulary is not invented by T3 because the current `OPEN_QUESTIONS.md` is organized by thematic sections rather than stable item IDs.

## 5. Migration invariant

During later W5 migration, no still-current item may be authoritative simultaneously in both its legacy aggregate representation and a new per-item canonical carrier.

The transition sequence must therefore be explicit:

```text
identify still-current item
-> create/validate successor carrier in a bounded migration change
-> reconcile identity/relations/provenance
-> demote/supersede the old aggregate item's current-authority role
-> rebuild derived browsing/index surfaces
-> verify no duplicate current authority
```

Historical aggregate prose remains provenance and does not require mass rewriting.

## 6. Why T3 is sufficient without another architecture round

MC-0018 already compared the conceptual alternatives. T3 adds production-mechanism evidence:

- A works natively with the existing one-carrier/one-declaration source model and authority resolver;
- B requires broad substrate semantics not otherwise needed;
- C mechanically cannot satisfy the first-class relation/required-identity cases that triggered the question.

No material ambiguity remains that justifies another model-collaboration round before migration design.

## 7. Result

```text
T3=ACCEPTED
ITEM_REGISTRY_CONTRACT=SELECTIVE_PER_ITEM_CARRIER
ONE_DECLARATION_PER_CARRIER=RETAINED
MULTI_DECLARATION_CARRIER=NOT_ADOPTED_V1
ANCHOR_ONLY=PERMITTED_WHEN_FIRST_CLASS_IDENTITY_NOT_REQUIRED
MASS_HISTORICAL_SPLIT=REJECTED
DECISION_HOME=docs/decisions/
ARCHITECTURE_BACKLOG_HOME=docs/architecture_backlog/
OPEN_QUESTION_HOME=docs/open_questions/ WHEN FIRST_CLASS ITEM IDS EXIST
LIVE_REGISTRY_MIGRATION=NOT_STARTED
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=T1_INDEPENDENT_CALIBRATION_AND_T4_HISTORICAL_NAVIGATION
```
