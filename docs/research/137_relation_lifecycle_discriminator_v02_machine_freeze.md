# Research 137: Relation-Lifecycle Discriminator V0.2 Machine Freeze

**Date:** 2026-09-13
**Status:** RELATION-LIFECYCLE FIXTURE V0.2 MACHINE-FROZEN / H1-H2 V0.2 IMPLEMENTATION NOT YET STARTED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Freeze an exact representation-neutral second discriminator before implementation, targeting the unresolved question left by Common Fixture V0.1: whether a relationship with its own identity, lifecycle, provenance, temporal applicability and concurrency semantics can remain source-local without arbitrary ownership or whether it earns separate authoritative representation.
**Authority:** Synthetic architecture-probe input under Research 124 and Research 136. Requirements V0.2 remain the frozen candidate-acceptance authority. This fixture is evidence input only and does not alter project-development authority.
**Declared references:** `research:124`, `research:134`, `research:135`, `research:136`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:479`

## 1. Exact frozen artifact

```text
docs/research/project_knowledge_architecture_probe_v02/RELATION_LIFECYCLE_FIXTURE_V02.json
fixture_id: PKA-RL-V02
bytes: 11,809
SHA-256: ece094762e3fe4f064640004da3f2293aa39168268af183df6f1347ba7f4b4c0
```

The fixture was created after V0.1 interpretation but **before** any V0.2 H1/H2 implementation logic. The exact bytes are now the comparison input. If a semantic defect is discovered later, V0.2 must not be patched in place; a new fixture version and full rerun are required.

## 2. Why a second fixture is needed

Common Fixture V0.1 showed that several apparently cross-object facts still have plausible source-local ownership:

```text
identity transition history -> the identity being changed
supplement relation          -> the supplementing source
workstream state             -> the workstream source
governing source set         -> deterministic closure over source-local facts
```

That means V0.1 cannot answer the stronger question in KA-R15:

> What happens when the **relationship itself** carries material state, time, provenance, authority semantics and an independent lifecycle?

V0.2 isolates that question instead of adding broad architecture surface area.

## 3. Fixture structure

### 3.1 Stable endpoint subjects

Four semantic subjects `S-A`, `S-B`, `S-C`, `S-D` begin active at semantic revision 1. During the first-class relation lifecycle, their intrinsic semantic state must remain unchanged.

This makes endpoint mutation an architectural side effect rather than an excuse that “the endpoint changed anyway.”

### 3.2 Source-local control relation

`SR-D-A` is a deliberately ordinary directional dependency:

```text
S-D depends_on S-A
natural owner = S-D
independent lifecycle = false
relation-specific provenance = false
stable relation identity required = false
```

It is the **negative control** for H2. A minimal spine should not absorb this relation merely because it crosses objects.

### 3.3 Independent symmetric ternary relation

`R-ABC-1` relates `S-A`, `S-B`, and `S-C` symmetrically. The fixture explicitly gives it:

```text
stable relation identity
arity = 3
symmetric membership
no natural endpoint owner
independent proposed/disputed/accepted/superseded lifecycle
relation-specific evidence E1..E4
recorded time
separate authority-transition time
separate effective/applicability time
relation revision independent of endpoint semantic revision
```

A later accepted successor `R-ABC-2` becomes effective on 2026-05-20 and supersedes `R-ABC-1` without changing the three endpoints.

### 3.4 Concurrency challenge

After `R-ABC-1` reaches relation revision 4, a second collaborator attempts an update using stale expected revision 3. The update must fail as:

```text
STALE_RELATION_REVISION
```

and must not mutate authoritative relation state.

This tests KA-R29 at the relation itself rather than only at an endpoint file.

### 3.5 Temporal queries

The fixture asks for relation state before proposal resolution, while disputed, accepted-but-not-effective, effective, pending supersession, and after successor effectiveness.

That requires a candidate to distinguish at least:

```text
recording time
authority transition time
applicability/effective time
historical lifecycle state
```

where they materially diverge.

### 3.6 Relation evidence failure

Evidence `E3` is required by the accepted `R-ABC-1` state. Removing it must make the 2026-05-11 relation query fail visibly as:

```text
unresolved_missing_relation_evidence
```

rather than silently treating the relation as safely current.

## 4. H1 boundary

H1 may use endpoint/source-local structured declarations, including a tightly source-owned sidecar, plus deterministic derived views.

It may **not** create a dedicated authoritative relation document/object/store/registry whose lifecycle is independent of an endpoint/source. Such a move would cross the semantic boundary into H2 and must be reported rather than disguised as H1.

Because `R-ABC-1/2` are symmetric and have no natural endpoint owner, H1 is allowed to choose a deterministic endpoint owner. That is **not** defined as an automatic correctness failure. Instead the probe must expose:

```text
which endpoint was selected
why it was selected
whether the ownership basis is semantically natural or an arbitrary tie-break
how many endpoint-owned locations relation-only transitions touched
whether endpoint semantic revisions remained unchanged
```

This keeps the experiment falsifiable. H1 can still win the case if arbitrary placement is cheap, safe and clear enough.

## 5. H2 boundary becomes more selective

H2 in V0.2 is intentionally narrower than the first H2 prototype.

The relation spine may admit only relations satisfying the frozen rule:

```text
stable relation identity required
AND independent lifecycle
AND relation-specific provenance
AND no natural endpoint owner
```

`R-ABC-1` and `R-ABC-2` qualify. `SR-D-A` does not.

Endpoint-intrinsic facts remain source-local. Ordinary directional relations remain source-local. This directly tests whether H2 can remain semantically bounded rather than merely physically small.

## 6. Scale discriminator

The fixture adds 10, 50 and 100 ordinary source-local directional relations using the same non-qualifying template.

The expected H2 first-class relation-spine count remains:

```text
1x  2
5x  2
10x 2
```

This is not a claim that total active views remain constant, because active relation complexity genuinely increases. It tests a narrower property:

> **Does H2 centralize ordinary relations that its own admission rule says should remain local?**

False-positive and false-negative admission counts are therefore first-class measurements.

## 7. Shared derived-state test

Both hypotheses may build:

```text
member_relation_index
current_relation_view
relation_history_projection
```

These views must be deletable, fail visibly when required but absent, and rebuild deterministically with freshness/source binding from authoritative inputs.

## 8. Primary requirements stressed

The discriminator is especially targeted at:

```text
KA-R12  epistemic/lifecycle state
KA-R14  supersession/conflict visibility
KA-R15  relationship semantics
KA-R16  selective temporal semantics
KA-R18  provenance/auditability
KA-R20  explicit authority class
KA-R21  derived rebuildability
KA-R23  freshness / authority closure binding
KA-R29  concurrent collaborator safety
KA-R33  dependency-local maintenance
KA-R34  maintenance/saturation observability
KA-R35  human/model inspectability
KA-R43  migration/identity preservation
KA-R46  representation-independent identity
KA-R47  multi-axis organization without duplication
KA-R49  selective temporal/supersession semantics
```

No new requirement is proposed by this fixture.

## 9. Interpretation discipline

V0.2 must not collapse into “H2 has a relation object, therefore H2 wins.” The comparison must separate:

```text
semantic correctness
arbitrary versus natural ownership
write/touch coupling
stale-write safety
relation identity and provenance clarity
admission-rule selectivity
semantic responsibility share
physical relation-spine size
derived-view rebuildability
```

A dedicated relation record is useful only if it solves a real semantic/lifecycle problem at acceptable maintenance cost.

## 10. Freeze disposition

```text
RELATION_LIFECYCLE_FIXTURE_V02=MACHINE_FROZEN
FIXTURE_SHA256=ece094762e3fe4f064640004da3f2293aa39168268af183df6f1347ba7f4b4c0
H1_V02_IMPLEMENTATION=NOT_STARTED_AT_FREEZE
H2_V02_IMPLEMENTATION=NOT_STARTED_AT_FREEZE
H2_ADMISSION_RULE=FROZEN
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_H1_AND_MINIMAL_H2_AGAINST_EXACT_V02_FIXTURE
```
