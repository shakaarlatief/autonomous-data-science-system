# Research 131: Owner-Provided ICM Source Incremental Evaluation

**Date:** 2026-09-13
**Status:** OWNER-SOURCE INCREMENTAL EVALUATION COMPLETE / REQUIREMENTS V0.2 UNCHANGED / CANDIDATE ARCHITECTURE SYNTHESIS NEXT / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Evaluate the project-owner-provided Interpretable Context Methodology (ICM) paper and current `RinDig/icm-architect` implementation as incremental evidence after the Research 124 anti-anchoring sequence and Requirements V0.2 freeze. Identify independent reinforcement, genuinely additional ideas, candidate mechanisms, evidence limitations, tensions with ADS requirements, and coverage gaps without treating ICM as a recommended target architecture.
**Authority:** Supporting owner-source evidence under Research 124. This record does not make ICM authoritative over ADS, does not amend the frozen V0.2 requirements, does not select an implementation family, and does not authorize migration.
**Declared references:** `research:124`, `research:125`, `research:126`, `research:127`, `research:128`, `research:129`, `research:130`, `checkpoint:470`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`

## 1. Why this source is evaluated now

The project owner deliberately withheld this material while Research 124 independently completed:

```text
internal architecture decomposition
    -> historical failure corpus
    -> blind historical ChatGPT baseline
    -> broad cross-disciplinary external research
    -> D1-D8 targeted deep dives
    -> requirements/evidence reconciliation
    -> owner acceptance
    -> Requirements V0.2 freeze
```

Only after Checkpoint 470 was the source exposed. The evaluation therefore asks what ICM adds to an already-established evidence field rather than allowing it to define the problem or anchor the solution space.

The owner explicitly did **not** recommend that ADS adopt ICM, its filesystem structure, its five-layer hierarchy, its forms, or any other mechanism. The correct evidentiary posture is:

```text
ICM observed
    !=
ICM selected

independent convergence
    !=
mechanism mandate

useful concrete implementation pattern
    !=
ADS target architecture
```

## 2. Primary sources inspected and access boundary

The evaluation uses two primary source families.

### 2.1 ICM paper

**Source:** Jake Van Clief and David McDermott, *Interpretable Context Methodology: Folder Structure as Agentic Architecture*, arXiv:2603.16021v2, revised 2026-03-18.

URLs:

```text
https://arxiv.org/abs/2603.16021
https://arxiv.org/html/2603.16021v2
https://arxiv.org/pdf/2603.16021
```

The paper is 28 pages with five figures, two tables and 54 references. It presents ICM primarily for sequential, repeatable, human-reviewed workflows and explicitly distinguishes that target class from high-concurrency, real-time multi-agent and complex automated branching systems.

### 2.2 Current ICM Architect repository

**Source:** `RinDig/icm-architect`.

URL:

```text
https://github.com/RinDig/icm-architect
```

Material inspected includes the current repository README, `SKILL.md`, `references/core.md`, `references/forms.md`, `references/system-map.md`, `references/reference-integrity.md`, and the stage-contract template. The current repository materially extends the paper's pipeline-centered presentation into six composable forms and adds explicit restructuring, system-map and reference-integrity practices.

### 2.3 Instagram limitation

The project owner also supplied the `@lostandlucky` Instagram account and reel `DbwnCJqRtXJ`. Direct retrieval of that account/reel remained unavailable through the active web and Browser surfaces. No transcript or video content was therefore treated as evidence in this record. The source remains supplemental and non-blocking; no claim below is attributed to unseen reel content.

## 3. What ICM actually proposes

The paper's core architecture is intentionally simple:

```text
numbered folders       -> stage order
folder hierarchy       -> context scoping
plain files            -> state + handoff artifacts
CONTEXT.md              -> stage contract
local scripts           -> deterministic/mechanical work
one orchestrating model -> different behavior from different stage context
human stage boundary    -> inspection / edit / decision point
```

The paper defines five design principles:

```text
one stage, one job
plain text as the interface
layered context loading
every output is an edit surface
configure the factory, not the product
```

and a five-layer context hierarchy:

```text
L0  global/workspace identity
L1  workspace task routing
L2  stage-specific contract
L3  stable reference material / constraints
L4  run-specific working artifacts
```

The stage contract makes inputs, process and outputs explicit. The current ICM Architect repository strengthens this into an exact-path contract with a concrete human check and, in its template/forms material, an explicit `Do NOT load` boundary.

The current repository also generalizes the method beyond a linear pipeline into six forms selected by the repeating unit of work:

```text
Pipeline
Umbrella
Record library
Knowledge bundle
Context map
System map
```

These forms may compose recursively, while a small catalog at each level routes downward rather than describing lower-level internals.

## 4. Strong independent reinforcement of conclusions already reached by Research 124

The strongest value of the owner source is not that it overturns the independent work. It independently converges on several Research 124 principles through a concrete implementation tradition.

### 4.1 Small stable routing core, not history-growing bootstrap payload

ICM Architect states that the root entry file should be small and stable, answer orientation/routing questions, and carry no content payload. `references/core.md` makes the rule sharper: the catalog holds no books; routing files point and store almost nothing.

This independently reinforces:

```text
KA-R02  stable project-controlled bootstrap
KA-R05  progressive disclosure
KA-R31  non-linear-history reconstruction cost
KA-R32  bounded mandatory active core
KA-R50  recurring active-surface consolidation
```

and the MC-0011 working bootstrap principle that a stable core should contain protocol/pointers rather than ordinary history-growing state.

ICM supplies a particularly concrete failure signal: when a routing file grows, it is probably absorbing payload that should move behind the route.

### 4.2 Task-shaped context instead of whole-workspace loading

The paper and repository repeatedly require agents to load the contract, relevant references and working inputs for the current step rather than the whole workspace. Large reference collections receive their own routers recursively.

This strongly reinforces:

```text
KA-R04  task-shaped safe orientation
KA-R05  progressive disclosure
KA-R07  relevant discovery
KA-R30  bounded qualification budgets
KA-R31  non-linear-history reconstruction cost
KA-R32  bounded mandatory active core
```

The important convergence is architectural rather than numerical. Research 124 had already concluded that long context is not the primary scaling escape hatch; ICM independently operationalizes selective loading as a default structural behavior.

### 4.3 Source truth separated from derived/catalog views

The current System map form says the subject tree remains source of truth, the map cites it, and the map must never become a second specification. Generated entry twins and file maps are generated rather than separately hand-maintained. Cards marked verified require source citations and freshness coordinates.

This independently reinforces:

```text
KA-R19  one explicit project-development authority
KA-R20  explicit authority class for stores/views
KA-R21  rebuildability appropriate to representation
KA-R23  freshness/source/authority-closure binding
KA-I02  no accidental competing truth
KA-I03  derived state does not silently own unique accepted truth
```

This convergence is especially relevant because Research 124 reached the source-versus-derived distinction before exposure to ICM.

### 4.4 One home per fact and generated indexes

ICM Architect's library rules say one home per fact, links instead of copies, and generated indexes rather than hand-edited duplicates.

This independently reinforces the Research 124 diagnosis of convenience-view drift and the V0.2 requirements around non-duplicated multi-axis organization, rebuildable derived state and dependency-local maintenance:

```text
KA-R21
KA-R33
KA-R47
KA-I02
KA-I13
```

ICM's implementation is deliberately simpler than V0.2's broader authority model, but the anti-duplication direction is strongly aligned.

### 4.5 Cold reconstruction should be tested behaviorally

ICM's walk test uses a memoryless agent and asks whether it can orient, select a stage/node, understand exact inputs/output/human check, report status and answer change-impact questions under a bounded read/context path.

This independently reinforces Research 124's central move from structural validity to behavioral reconstruction qualification:

```text
KA-R40  structural and behavioral qualification
KA-R41  multidimensional reconstruction qualification
KA-S01  generic cold start
KA-S05  saturated semantic domain
KA-S09 / KA-S10  scaling behavior
KA-S12  provider/model switch
```

ICM's walk test is narrower than ADS qualification, but it is a useful concrete example of a repository architecture being tested from the perspective of a cold collaborator rather than only validated as files and links.

### 4.6 Change impact should follow explicit dependencies rather than whole-corpus search

The paper's incremental-compilation analogy says a stage's input declarations identify which outputs can become stale when a source changes. The current System map adds explicit `Hits / Does not hit` change-impact surfaces and a small effects catalog.

This independently reinforces D8's dependency-local maintenance conclusion and:

```text
KA-R15  relationship semantics
KA-R23  freshness binding
KA-R33  dependency-local marginal maintenance
KA-R43  migration identity/reconciliation
```

The `Does not hit` field is particularly useful as an anti-neighbor discriminator: it records an obvious similar object that should *not* be included in the change radius, reducing over-broad context and accidental edits.

### 4.7 Migration must preserve inbound references, not merely produce a tidy destination

The repository's current `reference-integrity.md` is a move-safety gate. Before a move, it checks in-workspace references, sibling relative paths, symlinks and external consumers; it also checks case-folded destination collisions, requires copy/verify/remove ordering, and requires parity before source removal.

This is direct concrete reinforcement of:

```text
KA-R43  migration preservation and identity reconciliation
KA-I07  must-preserve semantics/provenance survive migration
KA-I17  semantic continuity is not forced to equal carrier/path continuity
```

It also sharpens a general migration lesson: a successful post-move walk test proves navigability, not necessarily safety. Inbound-reference preservation is a separate qualification dimension.

## 5. Genuinely useful incremental ideas and sharper design discriminators

Most ICM principles overlap with Research 124. Several mechanisms nevertheless sharpen the candidate-design space enough to preserve explicitly.

### 5.1 Positive and negative context contracts

The current stage template does not merely list inputs. It explicitly supports `Do NOT load` guidance for context an eager agent might otherwise pull in.

Research 124 already requires task-shaped reconstruction and relevance control, but it does not explicitly freeze **negative context selection** as a runtime requirement. ICM shows a low-complexity mechanism for expressing exclusions alongside inclusions.

This should enter candidate comparison as a design discriminator:

```text
Can a task/view contract say both:
    what must be activated
    and
    what must remain latent unless a trigger occurs?
```

No new V0.2 requirement is justified yet; the broader existing requirements already permit this behavior.

### 5.2 Catalog payload pressure as an observable architectural smell

Research 124 measures active-surface saturation through fan-out, context size, stale views and maintenance cost. ICM contributes a simple local invariant: **catalogs route; they do not carry the books**.

A candidate could therefore expose a measurable `routing-payload pressure` or equivalent signal: how much unique semantic content has leaked into what is supposed to be a bounded routing surface. This is a useful specialization of KA-R34 and KA-R50 rather than a new requirement.

### 5.3 Repeating-unit-first form selection

ICM Architect chooses among forms by first identifying the repeating unit: a run, portfolio, accumulating record, body of knowledge, organization, or editable system tree.

Research 124 already rejects one universal hierarchy and requires multi-axis organization. The genuinely useful incremental idea is the **selection question**: begin architecture decomposition by asking what kind of thing persists/recurs and what operation the representation optimizes, rather than selecting an artifact family by habit.

For ADS this is a candidate-design heuristic, not a requirement that these six forms exist.

### 5.4 Explicit universe state for system maps

The System map distinguishes:

```text
live       in force
leftover   still present but no longer the primary path
ghost      named/filed but not actually wired
```

V0.2 already requires current/historical/superseded/rejected distinctions, so the taxonomy is not a new semantic requirement. However, `ghost` is a useful concrete diagnostic state for **representation claiming operational reality that implementation does not actually instantiate**. That maps well to ADS's historical experience with stale convenience views and should be available as a candidate diagnostic concept where appropriate.

### 5.5 Source-improvement loop from repeated human corrections

The paper's `edit-source` discussion distinguishes one-off human value added to an output from recurring corrections that diagnose a weak source contract/reference. A future system could observe repeated correction patterns and propose a source-level improvement.

Research 124 already has capture, consolidation, promotion and evolution triggers, but this adds a sharper feedback loop:

```text
repeated downstream correction
    -> candidate pattern
    -> trace to governing source/contract
    -> propose source improvement
    -> explicit review/promotion
```

This is a promising candidate mechanism for KA-R10, KA-R45, KA-R48 and self-improving project infrastructure. It must remain proposal-only because the ICM paper itself describes the mechanism as future work.

### 5.6 Semantic debugging as source-map-like provenance

The paper explicitly says current ICM has observability but not traceability. Its proposed semantic debugging mechanisms include identifiers or markers that connect output sections to source instructions/reference material, cross-stage verification, and possible `Verify` sections in stage contracts.

Research 124 had already reached proportionate source-unit provenance and contract fidelity in D7/R129 and KA-R09/KA-R18. ICM adds a useful **debugger analogy** and a concrete candidate mechanism: source-map-like provenance for high-consequence transformations.

Again, this is not evidence that GUIDs or section markers are the correct implementation. It is a candidate mechanism and qualification probe.

### 5.7 Reverse walk as a separate move-safety test

The current ICM repository explicitly distinguishes outward change-impact walking from inbound external references. A map inside a tree cannot know what outside the tree points inward unless those consumers are discovered separately.

This is a useful refinement to migration qualification:

```text
forward walk
    what does this knowledge/object affect?

reverse walk
    what depends on / points into this knowledge/object?
```

Research 124 relationship and migration requirements allow this already, but candidate evaluation should test both directions rather than assuming a forward dependency graph is sufficient.

## 6. Evidence limitations and claims that remain weaker than ADS's existing evidence discipline

ICM is useful evidence, but several claims should remain calibrated.

### 6.1 The empirical base is preliminary

The paper reports an invite-only community of 52, with 33 users of the script-to-animation or structurally similar workflows and 30 self-reporting a U-shaped intervention pattern. The authors explicitly state that these observations come from conversations rather than instrumented or controlled measurement.

The paper also acknowledges self-selection/enthusiasm bias, concentration in content-production use cases, early-stage academic/policy deployment, testing on one model family, and no controlled ICM-versus-monolithic same-task comparison.

Therefore ICM is strong **design/practitioner evidence** and weak evidence for universal performance claims.

### 6.2 The 2k-8k context band is not an ADS requirement

The paper and repository repeatedly cite roughly 2,000-8,000 tokens as a healthy stage-context range. This is a useful practitioner target in ICM's tested workflows, not a demonstrated universal threshold for ADS project-development reconstruction.

Research 124's task-class-specific bounded-budget approach remains better calibrated than freezing ICM's number.

### 6.3 Filesystem transparency does not by itself solve authority

Plain files make state inspectable, but inspectability is not equivalent to resolving governing authority, supersession, conflict, current applicability or promotion status. ICM's current system-map taxonomy and source citations improve this, but ADS requires a stronger authority model than `the file is visible and linkable`.

### 6.4 Generated does not mean impossible to drift

ICM correctly prefers generated indexes over hand-maintained duplicates. The stronger phrasing that a generated file map "cannot drift" should not be imported literally. A generated view can still be stale because the generator did not run, the source binding is wrong, the generator is buggy, or its declared semantics changed.

Research 124's KA-R21/KA-R23 requirements around generator/source/freshness binding and validation remain stronger and should be retained.

## 7. Important tensions with V0.2

No owner-source evidence currently warrants changing a frozen V0.2 requirement, but several ICM implementation choices expose useful tensions candidate designers must handle.

### 7.1 Folder/path structure is useful control state but cannot become semantic identity by default

ICM deliberately encodes stage ordering and much orchestration meaning in filenames/folders. That is elegant for its target workflows. ADS V0.2, however, requires representation-independent continuity where a durable subject/workstream/knowledge object is intended to survive a rename, move or carrier replacement.

Therefore an ADS candidate may borrow folder-based routing or ordering while still satisfying:

```text
KA-R46
KA-I17
```

A path may be a carrier, route or current control encoding without being the durable semantic identity of the thing it represents.

### 7.2 Filesystem-as-state-machine is too narrow for the full ADS continuation problem

For a simple pipeline, output existence can represent stage state effectively. ADS project development also needs paused/blocked/superseded workstreams, multiple dependencies, return conditions, concurrent collaborators, interruption recovery and authority transitions.

Therefore ICM's filesystem state-machine pattern is a candidate mechanism for some subdomains, not sufficient evidence against KA-R25 through KA-R29.

### 7.3 Mandatory human review at every stage is workflow-specific

ICM's central target class assumes human review between stages, and the skill says nothing moves forward until a person has read the last output. ADS uses human authority strategically but also supports bounded autonomous execution where risk and policy permit it.

The transferable principle is explicit, consequence-shaped intervention surfaces, not mandatory human inspection after every transformation.

### 7.4 One-stage-one-job is useful decomposition, not a universal project-knowledge atomization rule

ICM's modularity principle is well supported for workflow stages. Research 126 explicitly rejected universal semantic atomization. A durable ADS knowledge object may legitimately carry several tightly coupled facts/relations when separating them would destroy coherence or create maintenance burden.

The decomposition heuristic should therefore remain scoped to responsibilities/interfaces rather than converted into `one fact = one file/object`.

## 8. V0.2 requirements that ICM does not substantially solve

The owner source is most mature around context scoping, human-visible workflow state, simple routing, local source/derived separation and sequential handoffs. It does not provide a complete answer for several requirements that remain central to ADS:

```text
KA-R09   action-bound governing-authority resolution and contract fidelity
KA-R12   rich epistemic role beyond simple live/leftover/ghost states
KA-R13   action-shaped authority source-set resolution
KA-R14   replacement/update/correction/conflict semantics
KA-R16   selective applicability/recording/authority-transition time
KA-R22   explicit source-traceable promotion of unique accepted synthesis
KA-R24   probabilistic retrieval subordinate to verifiable authority resolution
KA-R25-29 workstream identity, pause/return, DAG dependencies, interruption recovery,
          concurrent collaborator safety
KA-R37-39 public/private delegated authority and non-leakage
KA-R42   consequence-sensitive degraded mode
KA-R44   qualified authority switch during migration
```

Some current ICM forms touch adjacent concerns, especially knowledge-bundle access tiers, typed frontmatter and system-map source fidelity, but they do not amount to the full semantics V0.2 requires.

This coverage gap is expected rather than a criticism: ICM's declared problem class is narrower than ADS's project-development knowledge infrastructure.

## 9. Requirement-set disposition

The owner source does **not** currently justify changing Requirements V0.2.

The reasons are:

1. the strongest ICM ideas already fit or reinforce existing V0.2 requirements;
2. the genuinely additional mechanisms are implementation/design discriminators that V0.2 intentionally leaves open;
3. the source's empirical limitations do not justify making its specific token bands, human-gate frequency, folder identities or filesystem state semantics mandatory;
4. the tensions with V0.2 favor keeping the broader requirements rather than weakening them toward ICM's narrower workflow class.

Therefore:

```text
REQUIREMENTS_V02_AMENDMENT=NO
REQUIREMENTS_COUNT=50
INVARIANTS_COUNT=17
TARGET_ARCHITECTURE=NOT_SELECTED
```

## 10. Candidate mechanisms worth carrying forward

Without selecting a target, later candidate architecture work should deliberately keep the following ICM-derived mechanisms in the option pool:

```text
small payload-free recursive catalogs
explicit task contracts with positive + negative context selection
reference vs working-context separation where semantically useful
one-home-per-fact with links/views rather than copied truth
scripted/rebuildable indexes instead of manually duplicated catalogs
cold-agent walk tests with bounded reads/context
system-map cards tied directly to authoritative source
first-order Hits / Does not hit change-impact semantics
forward + reverse dependency/reference walks
copy -> verify parity -> remove migration discipline
case-fold collision checks during path migration
source-map-like provenance for selected high-consequence transformations
cross-stage Verify contracts
repeated-human-correction -> source-improvement proposals
repeating-unit-first choice of representation/form
```

These are **candidate mechanisms**, not a bundled ICM adoption decision.

## 11. New qualification probes suggested by the source

The source also adds concrete probes that can strengthen later common candidate evaluation without privileging ICM's file format:

```text
CATALOG-PAYLOAD TEST
    does a routing surface contain unique content that should live behind it?

NEGATIVE-CONTEXT TEST
    can the task contract identify material context that must remain latent?

COLD-WALK TEST
    can a memoryless collaborator reach the governing/source object under a bounded hop/read budget?

SOURCE-VIEW TEST
    does a derived map/card disagree with source, and if so does source visibly win?

FORWARD/REVERSE IMPACT TEST
    can the design find both what X affects and what depends on X, including external consumers?

MOVE-SAFETY TEST
    are inbound references, destination collisions, parity and removal ordering checked during migration?

SOURCE-IMPROVEMENT TEST
    can repeated corrections be captured as evidence for a governed source/contract amendment rather than repeated forever downstream?
```

These probes fit under existing KA-R40/KA-R41/KA-R43 qualification requirements.

## 12. Overall evaluation

The owner-provided ICM material is **relevant and useful**, but not because it supplies a ready-made ADS successor.

Its strongest contribution is threefold:

```text
1. independent convergence
   It independently validates the architectural direction of bounded routing,
   progressive task-shaped context, source/derived separation, cold reconstruction
   tests and dependency-local change impact.

2. implementation concreteness
   It turns several abstract Research 124 ideas into compact operational mechanisms:
   payload-free catalogs, explicit stage contracts, negative loading rules,
   walk tests, source-citing system maps and move-safety gates.

3. new debugging/evolution prompts
   Its incremental-compilation, semantic-debugging and edit-source analogies provide
   useful candidate mechanisms for provenance, verification and source improvement.
```

At the same time, ICM is intentionally narrower than the ADS problem. Its paper is centered on sequential, human-reviewed repeatable workflows; its empirical evidence is preliminary; and its filesystem-first state/identity mechanisms do not replace V0.2's stronger requirements for authority, epistemic state, temporal semantics, multi-workstream continuation, concurrency, public/private governance and migration identity.

The correct outcome is therefore neither `ADOPT ICM` nor `ICM IRRELEVANT`.

It is:

> **Carry ICM forward as a well-aligned concrete mechanism family and independent reinforcement source inside a broader candidate-architecture space whose requirements were frozen before ICM exposure.**

The anti-anchoring owner-source gate is now satisfied. Research 124 can move to serious candidate architecture synthesis, using ICM-derived mechanisms alongside materially different alternatives and testing all candidates against the same V0.2 requirements rather than treating ICM as the default target.

```text
RESEARCH131=OWNER_SOURCE_INCREMENTAL_EVALUATION_COMPLETE
ICM_RELEVANCE=HIGH_AS_INCREMENTAL_EVIDENCE
ICM_TARGET_SELECTION=NO
REQUIREMENTS_V02_AMENDMENT=NO
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CANDIDATE_ARCHITECTURE_SYNTHESIS
```
