# Research 134: Comparative Architecture Reconciliation and Common-Fixture Probe Protocol

**Date:** 2026-09-13
**Status:** MC-0013 COMPARATIVE RECONCILIATION COMPLETE / COMMON-FIXTURE PROBE PROTOCOL FROZEN / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Reconcile ChatGPT Research 133 with Claude MC-0013 Message 003, narrow the serious candidate set without prematurely selecting a target, define the semantic-ownership question that remains genuinely unresolved, and freeze a neutral common-fixture mechanism-probe protocol for the next Research 124 phase.
**Authority:** Supporting Research 124 architecture-design evidence only. Requirements V0.2 remain the frozen acceptance boundary. This record does not authorize target selection, migration or authority switch.
**Declared references:** `research:124`, `research:133`, `path:docs/model_collaboration/threads/MC-0013/messages/001_claude_independent_architecture_counter_design.md`, `path:docs/model_collaboration/threads/MC-0013/messages/002_chatgpt_independent_design_disposition_and_comparative_handoff.md`, `path:docs/model_collaboration/threads/MC-0013/messages/003_claude_comparative_architecture_critique.md`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:476`

## 1. Comparative-dialogue result

MC-0013 achieved its intended purpose. Claude first produced an architecture synthesis without exposure to Research 133, then reviewed Research 133 comparatively after that independent position was durably frozen. The comparative pass materially changed Claude's preferred architecture rather than merely polishing its first proposal.

The most important result is that the disagreement no longer concerns storage technology or whether semantic structure is useful. It has narrowed to one architectural ownership question:

> **Which deterministic semantic/control facts can honestly remain owned by one source artifact, and which facts need their own authoritative home because they span several artifacts or possess an independent lifecycle?**

Claude now agrees that Research 133's Bounded Semantic/Control Spine is a genuinely distinct semantic family, not simply a renamed compromise between document metadata and object-primary knowledge. It also accepts the core reason for the distinction: some facts, such as a merge mapping, a joint governing-source closure or a workstream spanning several artifacts, do not naturally belong to any one endpoint document.

The comparative dialogue therefore produced real synthesis rather than model averaging.

## 2. Revised candidate-family landscape

The original six Research 133 families remain useful as design-space provenance, but they no longer deserve equal active status.

### 2.1 Live serious hypotheses

#### H1: Distributed Document Contracts

Rich Git-authoritative sources carry their own bounded deterministic declarations. Generated views compile source-local identity, epistemic role, scope, applicability and declared relations into routing/authority/current-state projections. Cross-artifact semantics are expressed through source-local declarations and generated closure rather than a separately authoritative relation/control substrate.

Its main advantage is local authorship and minimal central curation. Its principal risk is that relations which do not honestly belong to one source become duplicated, asymmetric, underspecified or silently omitted.

#### H2: Partitioned Semantic Ownership with a Bounded Cross-Object Spine

Rich Git-authoritative sources remain primary for rationale, exact content, evidence and source-local declarations. A deliberately bounded structured substrate owns only deterministic facts whose semantics are inherently cross-object or whose lifecycle is independent of any one source. Global navigation/search/context views are rebuildable over both.

This is narrower than an object-primary repository and more explicit than pure distributed declarations. It is also more precise than Research 133's earlier broad spine description because ownership is now partitioned by semantic locus rather than by convenience.

Its main advantage is giving cross-object facts one unambiguous authoritative home. Its principal risk is that the word `bounded` proves unstable and the spine grows into a general registry, recreating global curation pressure in a more formal form.

### 2.2 Reference / falsification poles

#### H3: Object-Primary Structured Authority

This remains valuable as an upper-structure reference pole. It tests whether making semantic objects and relations primary actually simplifies the hard cases enough to justify the schema, migration and human-inspectability cost. It is not currently a leading target.

#### H0: Retrieval-First Minimal Formalism

This remains valuable as the lower-structure reference pole. It tests whether H1/H2 are introducing structure that could safely remain derived. It is not eligible to own consequential authority probabilistically, so its deterministic minimum must still satisfy V0.2.

### 2.3 Families no longer active as separate semantic candidates

```text
Transition Journal as project-wide primary authority
    -> dropped from serious consideration for now
    -> no demonstrated need justifies universal event/replay complexity

Narrow authority-transition ledger
    -> also dropped for now
    -> Git already supplies recording chronology; selective `effective_from`-like
       semantics can represent applicability divergence when needed

Relational Canonical Registry
    -> folded into H2/H3 as a possible physical representation
    -> relational storage is an implementation choice unless it changes semantic ownership
```

These families were not ignored. They were explicitly reasoned through and narrowed because the demonstrated problem does not currently justify their distinct complexity.

## 3. Semantic-ownership partition hypothesis

The strongest current synthesis hypothesis is now more specific than Research 133 Section 13. It is still **not selected**.

### 3.1 Source-local facts

A fact should normally remain source-local when one authoritative source can state it fully about itself, the fact does not require another object's participation to be true, and the fact has no independent lifecycle worth representing separately. Candidate examples:

```text
artifact/carrier stable id
artifact epistemic role or status
artifact-local scope
evidence/source citations
source-specific applicability where that source alone governs the task class
source-local freshness or effective date where no cross-object relation is implied
```

This does not mean every file receives universal metadata. The existing identity and maintenance-economics tests still apply.

### 3.2 Cross-object/control-state facts

A fact becomes a candidate for separate authoritative representation when no single source can honestly own the whole fact, when the relation has an independent lifecycle/provenance, or when one durable object spans several carriers. Candidate examples:

```text
semantic identity that persists across several carriers/representations
identity merge / split / redirect mappings
joint governing-source-set closure and precedence
workstream identity, parent/dependency/resume state spanning multiple artifacts
relations whose own status, dispute, qualification or temporal state matters
authority-transition semantics when applicability differs materially from recording
```

### 3.3 Reclassification is the critical lifecycle problem

Claude identifies the strongest challenge to the partition: a fact may begin source-local and later become cross-object. Example:

```text
source A initially declares: I govern task X
    -> later source B is introduced as a mandatory supplement
    -> the authoritative fact becomes: A + B jointly govern X in governed order
```

At that point ownership must move or be promoted from a local declaration into a cross-object authoritative representation. If the old local declaration remains independently authoritative, truth duplicates. If it disappears without provenance, history and rationale are damaged.

The candidate architecture therefore needs a **relation/semantic ownership promotion rule** analogous in spirit to KA-R48's capture/promotion distinction, but the probe must test whether this analogy is actually cheap and coherent rather than assuming it works.

A successful design should preserve:

```text
old local declaration provenance
new cross-object authoritative ownership
redirect/tombstone or non-authoritative historical trace
no simultaneous competing truth
rebuildable views updated from the new owner
```

## 4. Capture lifecycle correction retained

The comparative dialogue also resolves one gap in Claude's original H1. Ordinary canonical commits are not enough to satisfy KA-R48's low-friction intake requirement.

The architecture therefore needs an intentionally cheap **capture intake surface** for potentially valuable reasoning that is not yet ready for a full Research/Foundation/Specification-like artifact. Its required semantics are minimal:

```text
source/provenance sufficient to trace where it came from
recorded time
candidate/non-authoritative status
optional rough subject/workstream association
no requirement for full canonical metadata or polished prose
explicit later outcomes: consolidate/promote, retain as candidate/history, or retire
```

The physical form remains open. It could be a small repository-native intake record, a bounded generated handoff from conversation, or another mechanism. The probe should test lifecycle semantics rather than prematurely standardize a file format.

## 5. Event-ledger disposition

No dedicated event ledger is carried into the first probe round.

Git already supplies durable recording chronology. For the demonstrated selective temporal cases, an explicit applicability/effective field on the authoritative fact may be sufficient. A dedicated event-oriented mechanism should reopen only if a probe or later real case demonstrates a recurring need for cross-fact historical replay that ordinary Git history plus current semantic state cannot answer safely or economically.

This is a reversible deferral, not a permanent prohibition.

## 6. Common-fixture principle

The next phase must not prototype one model's preferred architecture first. The same semantic fixture must be represented through the competing hypotheses so that differences arise from architecture, not scenario selection.

The fixture is synthetic but modeled directly on observed ADS problem classes. It is not intended to resemble the current repository cosmetically.

Each hypothesis receives exactly the same facts, transitions and required queries. Implementations may use different internal representations, but may not omit a hard case merely because the representation makes it inconvenient.

## 7. Common Fixture V0.1

### F1. Identity continuity, merge, reversal and split

Start with durable semantic subject `S-A` represented by carrier `A1`. Then:

```text
1. move/rename A1 -> A2 without changing intended semantic identity
2. discover separately recorded subject S-B that appears equivalent to S-A
3. perform an accepted merge/redirect S-B -> S-A
4. later discover the merge was partly wrong and reverse the merge
5. split S-B into S-B1 and S-B2 while preserving provenance and prior references
```

Required queries:

```text
what is the current canonical identity for each historical reference?
what happened to the old identities?
which carrier(s) currently represent each semantic identity?
can the mistaken merge be reconstructed without treating it as current truth?
```

Primary requirements stressed: KA-R15, R16, R18, R43, R46, R49.

### F2. Joint authority closure, supersession and conflict

Create:

```text
P0  historical procedure, now explicitly superseded
P1  current base procedure
P2  mandatory supplement to P1, effective later than P1 recording
C1  unpromoted candidate that conflicts with one step of P1/P2
```

Required queries/actions:

```text
resolve the governing source set before P2 becomes effective
resolve it after P2 becomes effective
exclude P0 from current authority while preserving historical trace
surface C1 as non-authoritative conflict/candidate, not silently merge it
return fail-visible ambiguity if the P1/P2 precedence/order declaration is removed
```

Primary requirements stressed: KA-R08, R09, R12-R14, R16, R20, R23, R24, R49.

### F3. Nested workstream DAG and deterministic resume

Create parent objective `W0` with dependencies `W1` and `W2`. `W2` opens child `W2a`; `W2a` pauses on external condition `D1`; meanwhile `W1` completes. Then simulate an interruption before `W2a` resumes.

Required reconstruction:

```text
current state of W0/W1/W2/W2a
why W2a paused
what condition allows return
exact/typed resume target
what parent objective resumes after W2a and W2 close
which completed work must not be replayed after interruption
```

Primary requirements stressed: KA-R06, R25-R29, R31, R33.

### F4. Conversation-born capture, consolidation and promotion

Inject one potentially valuable insight `I1` with intentionally incomplete initial structure. Then:

```text
1. capture it cheaply as non-authoritative material
2. consolidate it with two supporting sources
3. promote one accepted conclusion into durable authority
4. retain one rejected alternative as historical rationale
5. remove the temporary capture representation without losing accepted unique insight
```

Required checks:

```text
capture did not imply authority
promotion is traceable to source/capture provenance
accepted unique reasoning survives deletion of transient candidate state
rejected rationale remains distinguishable from current truth
```

Primary requirements stressed: KA-R12, R17-R22, R48, KA-I16.

### F5. Active versus historical surface under 1x / 5x / 10x growth

Create a small live domain with a fixed number of genuinely active items and then multiply only historical/evidence items to 5x and 10x.

Required measurements:

```text
mandatory/bootstrap surface size
active routing/view size
number of manually maintained global entries
query/reconstruction path length to current governing source
view regeneration fan-out
stale-view detectability
```

The active semantic state is held constant unless the scenario explicitly adds a new current obligation.

Primary requirements stressed: KA-R30-R34, R50, KA-I12, KA-I13.

### F6. Derived-store destruction and rebuild

Delete every generated routing/search/graph/current-view artifact allowed to be derived by the hypothesis.

Required result:

```text
no unique accepted truth is lost
minimum safe project state can be reconstructed from authoritative inputs
rebuild output exposes source revision / freshness binding
missing derived state fails visibly where reconstruction depends on it
```

Primary requirements stressed: KA-R19-R23, R35, R42.

### F7. Post-activation contract fidelity

Use an ordered consequential procedure with at least five mandatory ordered constraints, including one precondition and one prohibition. The architecture must:

```text
resolve the correct governing source set
make source consumption observable
preserve all material ordered constraints into produced guidance/action contract
fail visibly when one mandatory constraint is unavailable or contradictory
```

This directly preserves the BL-001 lesson that finding and reading the right source is not enough.

Primary requirements stressed: KA-R08, R09, R13, R14, R24, R40, R41.

## 8. Hypotheses to represent against the same fixture

### H1 implementation boundary

H1 may use:

```text
rich source artifacts
source-local structured declarations
generated global closure/views
probabilistic retrieval only as subordinate nomination/discovery
```

H1 may **not** introduce a separately authoritative cross-object relation/control store. If it does, the probe has crossed into H2 and must report that transition rather than hide it.

### H2 implementation boundary

H2 may use:

```text
rich source artifacts with source-local declarations
a bounded authoritative cross-object/control-state substrate
derived global views over both
subordinate probabilistic retrieval
```

Every spine-owned fact must justify why it cannot remain source-local or why its independent lifecycle/query semantics earn separate ownership.

### H3 reference implementation boundary

H3 may model the same fixture with object/relationship-primary structured authority and human-readable projections. It exists to test whether H1/H2 are preserving document-oriented complexity that a more explicit object model would actually simplify. H3 does not become a leading candidate merely by being more expressive.

H0 is not required in the first implementation round unless H1/H2 both appear to over-structure the fixture. Its role is a lower-bound challenge rather than a default prototype.

## 9. Measurements and observation record

The probe must not collapse results into one architecture score. Record at least:

```text
correctness of each required query/action
fail-visible behavior on ambiguity/missing state
authoritative fact count by ownership surface
number of duplicate authoritative declarations
number of authored locations touched per transition/change
number of generated/rebuildable locations touched automatically
local-change propagation fan-out
manual global-maintenance steps
relation reclassification events
undetected omission opportunities and whether validators catch them
identity merge/split steps and preserved redirects/provenance
workstream resume reconstruction steps
derived-state rebuild success/failure
mandatory/active view bytes and rough context size
implementation/schema surface size
qualitative human inspectability
qualitative source-versus-control ownership clarity
```

Timing may be recorded but should not dominate because the fixture is small and implementation language can swamp architectural effects.

## 10. Falsification criteria

### H1 weakens materially if

```text
merge/split or joint-authority closure requires duplicated endpoint declarations
relation ownership becomes ambiguous
correct closure depends on whole-corpus heuristic reconciliation
missing source-local declarations are not detectable under the fixture
workstream state is forced into an arbitrary owning document
```

### H2 weakens materially if

```text
ordinary source-local additions routinely require spine edits
spine fact count grows with history rather than active cross-object semantics
reclassification creates persistent duplicate truth
humans/models cannot tell whether a fact belongs in source or spine
5x/10x history forces global spine maintenance despite stable active state
```

### H3 becomes more serious only if

```text
H1/H2 require comparable schema/relationship machinery anyway
AND object-primary representation materially simplifies hard cases
without unacceptable authoring, migration or inspectability cost
```

No one failed check automatically selects another candidate. Failures identify which assumption requires redesign or abandonment.

## 11. Public/private and degraded-mode overlay

The first common fixture does not need real private data, but every hypothesis must declare where KA-R37-R39 would be enforced and what would happen if delegated private continuity were unavailable. The probe should use labeled synthetic private-only facts if needed; no real private paths or secrets should be introduced.

Likewise, each hypothesis must state degraded behavior when a generated view or optional retrieval accelerator is unavailable. Consequential authority resolution must not silently fall back to model memory.

## 12. Probe sequencing

The next work should proceed in this order:

```text
1. freeze one representation-neutral fixture manifest for F1-F7
2. implement the smallest H1 representation + query/generation logic
3. implement the smallest H2 representation + query/generation logic
4. implement H3 only to the depth needed for upper-bound comparison
5. run identical fixture queries/transitions across representations
6. record observed semantic failures and maintenance behavior
7. reconcile which ownership boundary survived
8. only then deepen the leading candidate or reopen another family
```

The fixture manifest should be immutable within a comparison run. If the fixture itself proves deficient, revise it as a new version and rerun every compared hypothesis.

## 13. MC-0013 disposition

No additional Claude turn is needed before the mechanism probes. Claude's comparative Message 003 resolves the substantive architecture disagreement as far as prose reasoning can currently take it. Another abstract exchange would mostly repeat the newly converged hybrid and its boundedness risk.

A later Claude contribution will have higher value after probe evidence exists, ideally as adversarial interpretation of the same raw results rather than as another pre-result architecture opinion.

```text
MC0013_PURPOSE=SATISFIED
ADDITIONAL_DIALOGUE_BEFORE_PROBES=NO
```

## 14. Current disposition

The cross-model work has not selected H2. It has merely made the unresolved empirical question sharper:

> **Can a cross-object semantic/control spine remain genuinely bounded, locally maintainable and unambiguous under the exact hard cases that pure distributed declarations struggle to own?**

H1 remains serious because source-local declaration may still prove sufficient with less machinery. H2 is the strongest current integrated hypothesis because both independent reasoning paths now recognize a natural home for genuinely cross-object facts. H3 remains an important upper-structure reference pole. The common fixture is intended to challenge all of those claims.

```text
RESEARCH134=COMPARATIVE_RECONCILIATION_COMPLETE
LIVE_CANDIDATES=H1_DISTRIBUTED,H2_PARTITIONED_BOUNDED_SPINE
REFERENCE_POLE=H3_OBJECT_PRIMARY
EVENT_LEDGER=DEFERRED
LOW_FRICTION_CAPTURE=REQUIRED_SEMANTIC_ROLE
COMMON_FIXTURE_V01=FROZEN_CONCEPTUALLY
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=IMPLEMENT_COMMON_FIXTURE_AND_H1_H2_PROBES
```
