# Research 136: Common Fixture V0.1 H1/H2 Empirical Mechanism Probe

**Date:** 2026-09-13
**Status:** FIRST H1/H2 MECHANISM PROBE COMPLETE / BOTH CANDIDATES PASS V0.1 SEMANTICS / H2 HISTORY-BOUNDEDNESS SUPPORTED / SEPARATE-SPINE NECESSITY NOT ESTABLISHED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Implement the exact machine-frozen Common Fixture V0.1 against the two live Research 134 hypotheses, execute identical semantic and failure challenges, measure ownership and maintenance behavior, and interpret what the first empirical comparison does and does not establish.
**Authority:** Supporting Research 124 empirical architecture evidence only. Requirements V0.2 remain the frozen candidate-acceptance authority. This probe does not select a target architecture or authorize migration.
**Declared references:** `research:124`, `research:134`, `research:135`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `path:docs/research/project_knowledge_architecture_probe_v01/COMMON_FIXTURE_V01.json`, `path:docs/research/project_knowledge_architecture_probe_v01/RESULTS_V01.json`, `checkpoint:478`

## 1. Probe integrity

The representation-neutral fixture was durably committed and pushed before candidate implementation began.

```text
fixture_id: PKA-CF-V01
fixture SHA-256:
    c8ed1873014b7a69016eb6fb259791d1c34b9cd14219547f1ebc0e755b836fe8
fixture-freeze commit:
    30fd78f244e94a30ac21649fa591c77b572fe957
```

The runner refuses fixture drift through an exact SHA check. H1 and H2 consume the same fixture bytes and the same expected semantic/failure outcomes.

Implementation and evidence surfaces:

```text
scripts/research/project_knowledge_architecture_probe_v01.py
tests/unit/test_project_knowledge_architecture_probe_v01.py
docs/research/project_knowledge_architecture_probe_v01/RESULTS_V01.json
```

The implementation is deliberately a small deterministic architecture model, not production ADS infrastructure. It uses only the Python standard library and does not introduce a candidate architecture into current repository authority.

## 2. Candidate implementations actually tested

### 2.1 H1: Distributed Document Contracts

H1 gives semantic/control facts a source-local authoritative home wherever possible:

```text
identity carrier/history       -> subject source artifact
supersession                   -> superseding source
supplement + precedence        -> supplement source
a candidate conflict           -> candidate source
workstream state/parent/resume -> each workstream source
promotion provenance           -> promoted/rejected source
contract constraints           -> governing contract sources
```

Global governing sets and contract closure are deterministic **derived results** rather than separately authoritative relation objects.

This is an important strengthening of H1 relative to the earlier prose discussion. H1 was not implemented as symmetric duplicate metadata on both endpoints. Directional relations are declared once by the source that asserts the relation, and generated closure composes them.

### 2.2 H2: Partitioned Semantic Ownership / Bounded Spine

H2 keeps rich/source-local artifacts while adding three explicitly modular cross-object/control modules:

```text
identity spine
authority spine
workstream spine
```

Carrier-local facts and promoted knowledge/provenance remain in sources. Identity merge/split state, joint authority, cross-source contract closure and workstream control state live in the spine. Global views remain derived.

One local-to-spine authority reclassification is exercised: P1 begins as a sole source-local governor, then the later P2 supplement causes the TASK-X authority relationship to be promoted into the authority spine.

This directly tests the reclassification cost identified in Research 134 rather than assuming it away.

## 3. Semantic result: both candidates pass Common Fixture V0.1

Both H1 and H2 pass every deterministic semantic/failure challenge in F1-F7 plus the synthetic private non-leakage overlay.

```text
H1 semantic correctness: PASS
H2 semantic correctness: PASS
```

Both correctly handle:

```text
S-A carrier continuity
S-B merge -> mistaken-merge reversal -> split
P0 supersession
P1/P2 time-sensitive joint authority
C1 non-authoritative conflict visibility
fail-visible missing precedence
fail-visible missing cross-source authority relation
nested W0/W1/W2/W2a interruption/resume state
conversation-born candidate capture and explicit promotion
rejected rationale retention
complete derived-view destruction and deterministic rebuild
freshness/source-digest binding
G1/G2 source-consumption receipt
six-element ordered action contract
fail-visible missing mandatory prohibition
fail-visible contradictory accepted supplement
synthetic private-only value non-leakage
```

The first major empirical conclusion is therefore negative but important:

> **Common Fixture V0.1 does not establish that a separately authoritative spine is necessary for correctness.**

H1 satisfies the same semantics without introducing one.

## 4. Normalized semantic-ownership result

The probe defines one representation-neutral 32-proposition semantic inventory and requires both implementations to cover exactly that inventory. This avoids the invalid comparison of “number of H1 metadata fields” against “number of H2 records.”

Observed ownership:

```text
H1
    source-local authoritative propositions   30 / 32
    spine-owned propositions                   0 / 32
    derived-only closure propositions          2 / 32
    duplicate authoritative owners             0

H2
    source-local authoritative propositions    5 / 32
    spine-owned propositions                  27 / 32
    derived-only closure propositions          0 / 32
    duplicate authoritative owners             0
```

This changes the interpretation of “bounded spine.” H2 uses only seven top-level spine records, but those seven records own **27 of the 32 normalized control/relationship propositions** in this fixture. Record count alone can therefore make a semantically dense control layer look smaller than it is.

That is not automatically a defect. The workstream module, for example, intentionally packs a coherent workstream's state and edges into one record. But future boundedness qualification should track at least both:

```text
physical/record count
semantic fact / responsibility share
```

A spine that remains physically small while gradually owning most project semantics would still be drifting toward H3-like centralization.

## 5. Historical-scale result

F5 increases only historical/evidence volume while holding active semantic state fixed.

```text
history items             20      100      200
                          1x       5x       10x

H1 active-view bytes     138      138      138
H2 active-view bytes     138      138      138

H1 spine records           0        0        0
H2 spine records           7        7        7

H1 full rebuild scan      41      121      221
H2 full rebuild scan      48      128      228
```

This supports two bounded claims:

1. **Both candidates can keep the active semantic view constant while history alone grows.**
2. **H2's spine does not grow merely because historical source/evidence count grows in this fixture.**

So the specific H2 failure hypothesis “the spine automatically grows with passive history” does **not** reproduce here.

However, the full-rebuild source scan still grows linearly with history for both implementations. That is not itself a V0.2 failure because generated full rebuilds may be periodic/global while required reconstruction uses bounded materialized views. But this probe does **not** establish an incremental rebuild/index design or independently qualify KA-R31 across real repository scale. The valid conclusion is active-surface boundedness under this synthetic condition, not globally sublinear processing cost.

## 6. Maintenance and representation observations

The instrumented transition/change path records:

```text
                               H1       H2

authored-location touches       12       18
relation reclassifications       0        1
authoritative serialized bytes 3223     3631
```

H2 therefore pays visible extra authorship/coordination cost in this fixture because some transitions update both a rich source and its cross-object control representation, and the P1 -> P1+P2 change crosses the local-to-spine ownership boundary.

The 18-versus-12 touch count is a useful direction-of-effect observation, not a universal 50% maintenance law. The fixture is small, and several touches are challenge instrumentation rather than production behavior. Likewise the roughly 12.7% serialized-byte difference is representation-specific and should not be generalized as storage overhead.

The stronger conclusion is qualitative:

> **H2 makes cross-object ownership more explicit, but that explicitness has a real write/reclassification cost which H1 avoids when a stable directional source owner exists.**

## 7. The most important surprise: H1 is stronger than the pre-probe argument assumed

The comparative dialogue leading to Research 134 treated several cases as evidence that a fact might have “no honest single-document owner.” The executable H1 model shows that this premise needs sharper qualification.

For Common Fixture V0.1:

```text
merge / reversal / split history
    can be owned by the identity being merged/split (S-B)

supplement + precedence
    can be owned directionally by the supplement (P2)

workstream state and return semantics
    can be owned by first-class workstream source artifacts (W0/W1/W2/W2a)

joint governing-source set
    can be a deterministic derived closure over those source-local facts
```

No duplicated authoritative declaration is required.

This does **not** prove H1 is the target. It establishes a more precise architectural lesson:

> **“A fact references multiple objects” is not sufficient reason to give the relation its own authoritative store.**

A directional relation can remain source-owned, and an n-source closure can sometimes remain derived rather than authoritative.

That finding materially narrows the admission rule for any future H2 spine.

## 8. What would actually justify separate relation/control ownership?

After V0.1, the strongest remaining H2 case is no longer generic cross-objectness. A separate authoritative home would need to earn itself through a stronger condition such as:

```text
the relation itself has an independent lifecycle/status/provenance
no endpoint has a non-arbitrary directional ownership role
the relation is genuinely n-ary and cannot be safely decomposed without semantic loss
concurrent updates require one relation identity / conflict boundary
relation-level temporal state changes while endpoints remain unchanged
policy/authority semantics require addressing the relation itself as a governed object
```

This is closer to the mature database/knowledge-model idea of promoting an association/relationship into a first-class entity only when the association itself carries facts or lifecycle.

The current H2 candidate should therefore become **more selective**, not broader, if it survives.

## 9. H2 boundedness result is mixed rather than simply positive

H2 passes the physical-history boundedness test:

```text
7 spine records at 1x
7 spine records at 5x
7 spine records at 10x
```

But it centralizes 27/32 normalized semantic propositions in those seven records.

Therefore:

```text
physical boundedness under passive history      SUPPORTED IN V0.1
semantic boundedness / responsibility share     NOT YET ESTABLISHED
ordinary-change marginal advantage over H1      NOT OBSERVED IN V0.1
cross-object ownership clarity                   STRONGER / MORE EXPLICIT IN H2
necessity of separate spine                      NOT ESTABLISHED
```

This is exactly why a single count like number of spine files/rows is an insufficient health metric.

## 10. H3 disposition after the first probe

Research 134 said H3 should be implemented only if H1/H2 required comparable object/schema machinery or both appeared over-structured.

That trigger is not met yet. H1 satisfies V0.1 with source-local declarations plus generated closure and no separate relation substrate. H2 also remains small enough physically to test further. Building H3 now would add implementation breadth without answering the newly isolated question.

```text
H3_IMPLEMENTATION_REQUIRED_NOW=NO
```

H3 remains the upper-structure reference pole and can reopen if a stronger relation-lifecycle probe forces H1/H2 toward comparable first-class relation machinery.

## 11. Construct-validity limitation of Common Fixture V0.1

V0.1 is useful, but its strongest result exposes its own next limitation.

Every cross-object case in the fixture still admits a plausible directional or subject-local owner:

```text
S-B owns its identity transition history
P2 owns the supplement relation
individual workstream artifacts own their own control state
derived authority closure does not itself need durable authority
```

So V0.1 tests whether H1 can handle non-trivial cross-object semantics. It does **not** yet strongly test a relation whose independent lifecycle is impossible to model source-locally without an arbitrary owner or semantic distortion.

This is not a reason to rewrite V0.1. The fixture was frozen correctly and produced useful evidence. Per Research 134, the next discriminator should be a new fixture version rather than an in-place repair.

## 12. Next empirical discriminator

Before target narrowing, the next probe should isolate relation-level lifecycle rather than simply add more volume. A V0.2 fixture should include at least one relationship that:

```text
has its own stable identity
is proposed/disputed/accepted/superseded independently of either endpoint
changes applicability while endpoint sources remain unchanged
has relation-specific provenance/evidence
is genuinely n-ary or symmetric enough that endpoint ownership is arbitrary
is concurrently edited/challenged so stale relation state must be detectable
```

H1 must then either represent that semantics source-locally without duplication/arbitrary ownership or fail visibly. It may not create a dedicated authoritative relation document under another name, because that would cross into H2.

H2 should be revised toward a **minimal admission-rule spine** for the same fixture rather than automatically moving every workstream/control fact into central modules. This directly tests whether semantic responsibility share can remain bounded as well as record count.

If H1 and minimal H2 both remain clean under that stronger test, the distinction may be smaller than Research 133/134 assumed. If H1 needs an artificial owner while H2 stays bounded, H2 earns stronger empirical support. If H2 expands rapidly, its central-registry risk becomes concrete.

## 13. Verification

Probe-specific verification:

```text
fixture hash guard: PASS
probe no-write execution: PASS
H1 semantic checks: PASS
H2 semantic checks: PASS
unit tests: 9 passed
Python compile check: PASS
```

A first broad `tests/unit` run was blocked for many tmp-path tests by host Temp-directory permission, not by code failures. Re-running the same unit suite with a repository-bounded pytest base temp succeeded:

```text
176 passed in 2.63s
```

The temporary pytest directory was then removed.

The repository integrity aggregate is run after this result is reconciled into current routing/checkpoint state; only that later aggregate may establish `PUBLIC_REPOSITORY_INTEGRITY=PASS` for the full transition.

## 14. Current disposition

The first empirical mechanism probe has reduced uncertainty but does not justify target selection.

```text
COMMON_FIXTURE_V01=COMPLETE
H1_SEMANTIC_CORRECTNESS=PASS
H2_SEMANTIC_CORRECTNESS=PASS
H2_PHYSICAL_HISTORY_BOUNDEDNESS=SUPPORTED_IN_V01
H2_SEMANTIC_BOUNDEDNESS=NOT_ESTABLISHED
H1_NEEDS_SEPARATE_SPINE_IN_V01=NO
SEPARATE_SPINE_NECESSITY=NOT_ESTABLISHED
H3_IMPLEMENTATION=DEFERRED
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=RELATION_LIFECYCLE_DISCRIMINATOR_FIXTURE_V02
```

## 15. Post-probe adversarial measurement correction

MC-0014 code-level review identified that two V0.1 scale metrics were aliases rather than independent measurements. `authoritative_location_count` and `full_rebuild_source_scan_count` use the same formula, and H2 `manual_global_entries` equals `spine_records` by construction. The raw result file remains valid evidence of the executed implementation, but these pairs must not be counted as independent lines of architecture support.

The core V0.1 conclusions survive this correction: both candidates pass the fixture semantics; H1 requires no duplicate authoritative fact ownership; directional relations can remain source-local; derived authority closure can avoid a second authority store; and passive historical growth does not enlarge the active view in this fixture.

Research 139 owns the corrected cross-probe interpretation and next real-corpus protocol.
