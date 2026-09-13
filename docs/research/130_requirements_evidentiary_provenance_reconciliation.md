# Research 130: Requirements and Evidentiary-Provenance Reconciliation

**Date:** 2026-09-13
**Status:** PROVISIONAL RECONCILIATION V0.2 COMPLETE / OWNER REVIEW NEXT / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Reconcile the 45 Phase-B requirements and 15 architecture invariants frozen before the historical baseline and external evidence program against owner intent, the historical failure corpus, blind ChatGPT baseline results, and Research 126-129 D1-D8 external evidence. Produce a solution-neutral proposed V0.2 requirement boundary without selecting a successor architecture.
**Authority:** Research support and proposed requirements revision under Research 124. The original Phase-B requirements remain the last frozen requirements boundary until the project owner accepts or amends this reconciliation. This record does not select a target architecture and does not authorize migration.
**Declared references:** `research:124`, `research:125`, `research:126`, `research:127`, `research:128`, `research:129`, `checkpoint:463`, `checkpoint:468`, `path:docs/research/PROJECT_KNOWLEDGE_FAILURE_CORPUS.md`, `path:docs/research/project_knowledge_baselines/evaluations/BL-001_chatgpt_a_evaluation.md`, `path:docs/research/project_knowledge_baselines/evaluations/BL-002_chatgpt_b_evaluation.md`, `path:docs/research/project_knowledge_baselines/evaluations/BL-002U_chatgpt_a_evaluation.md`, `path:docs/research/project_knowledge_baselines/evaluations/BL-003_chatgpt_a_evaluation.md`, `path:docs/research/project_knowledge_baselines/evaluations/BL-004_chatgpt_a_evaluation.md`

## 1. Why reconciliation is required

The Phase-B boundary was intentionally frozen **before** two major evidence phases:

```text
historical blind ChatGPT baseline
    -> showed that several feared failures are possible but not universal
    -> exposed a new post-activation task-fidelity failure
    -> separated recoverability from reconstruction cost

cross-disciplinary D1-D8 evidence
    -> added distinctions around identity, views, capture/promotion,
       derived state, action-shaped authority, temporal semantics,
       consolidation fidelity and lifecycle economics
```

The owner then explicitly clarified at Checkpoint 463 that Research 124 is a whole-architecture redesign rather than a patch list derived from current failures.

Therefore the correct next action is not to treat the original 45 requirements as immutable simply because they were once frozen. They must be checked for:

```text
continued evidentiary support
requirements made too strong by early failure interpretation
requirements made too weak by later evidence
hidden assumptions inherited from current artifact families
missing distinctions revealed by D1-D8
redundancy
solution-shaping language
appropriate normative strength
```

## 2. Evidence key

The matrix uses compact evidence tags:

```text
O   project-owner purpose / Checkpoint 463 whole-architecture clarification
H   historical failure corpus
B1  BL-001 exact operational-authority baseline
B2  BL-002-B + BL-002U model-collaboration baselines
B3  BL-003 broad-orientation baseline
B4  BL-004 exact-source-fidelity baseline
D1  Research 126 stable knowledge identity
D2  Research 126 multi-axis organization/views
D3  Research 127 capture/consolidation/promotion
D4  Research 127 source versus derived state
D5  Research 128 authority-aware retrieval / pre-action activation
D6  Research 128 temporal / supersession semantics
D7  Research 129 consolidation fidelity / provenance
D8  Research 129 maintenance economics / active-surface scaling
P   explicit project public/private governance policy
T   transition-safety / migration policy already accepted by owner
```

External evidence tags mean **supporting transfer evidence**, not direct proof that ADS must copy a source domain's mechanism.

## 3. Normative-strength vocabulary for V0.2

The original Phase-B record treated all `KA-R` statements as acceptance requirements. Reconciliation needs a more precise vocabulary:

```text
MUST
    candidate cannot be selected without satisfying the property

CONDITIONAL MUST
    mandatory when the stated condition/task/consequence class applies

SHOULD
    strong architecture preference; a candidate may diverge only with an explicit
    evidence-backed trade-off and compensating mechanism

QUALIFICATION MUST
    mandatory property of the comparison/qualification process rather than a runtime feature

DISCRIMINATOR
    must be measured/compared, but no direction is frozen before candidate evidence exists
```

This prevents evaluation methodology and runtime architecture from being conflated.

## 4. Reconciliation summary

The original requirements remain substantially sound, but the later evidence changes their shape in four important ways.

First, **broad orientation is no longer mandatory before every narrow consequential task**. BL-001 showed that broad reconstruction can actively distract from exact task fidelity, while D5 supports action-shaped authority resolution. Generic continuation still needs broad orientation; narrow governed tasks need the minimum orientation sufficient to establish state, scope and authority safely.

Second, **source activation must be stronger than source consumption**. BL-001 requires action-contract fidelity after activation. D5 therefore strengthens authority preflight into action-bound activation/conformance for consequential work.

Third, **the original boundary lacks first-class requirements for knowledge identity, multi-axis organization, capture/promotion, selective temporal semantics and recurring active-surface consolidation**. D1-D8 justify five additions.

Fourth, **scale requirements should focus on marginal fan-out and lifecycle cost, not only fixed context budgets**. B3 and D8 show that the current architecture is broadly recoverable but can become expensive; the redesign must improve economics rather than claim that recovery is impossible.

No original requirement is deleted outright. Several are materially refined; two qualification-oriented requirements are reclassified as qualification constraints rather than runtime architecture properties.

## 5. Original requirement reconciliation matrix: KA-R01 through KA-R23

| ID | Disposition | Proposed strength | Evidence | Reconciliation |
|---|---|---|---|---|
| KA-R01 | RETAIN + CLARIFY | MUST | O, H, B3, D7 | Preserve reusable **understanding**, not bytes; include semantic identity, rationale, epistemic state and provenance where material. |
| KA-R02 | REFINE | MUST | O, B2, B3, D2, D8 | Replace `repository-native bootstrap` with **stable project-controlled bootstrap**. The authority may still be the repository, but the target design must not be constrained to a file-only entry mechanism. No growing human continuation prompt. |
| KA-R03 | RETAIN | MUST | O, H, B2, P | No material project truth may live only in one conversation/model/provider memory. |
| KA-R04 | REFINE / CONDITION | CONDITIONAL MUST | B1, B3, D5, D8 | Generic continuation/cold start requires broad Tier-A orientation. A narrow governed task may use a smaller task-shaped orientation sufficient for current state, scope, authority and uncertainty; full broad orientation is **not** mandatory before every narrow consequential action. |
| KA-R05 | RETAIN + STRENGTHEN | MUST | B3, B4, D2, D7 | Progressive broad-to-deep traversal remains core; depth must be shaped by the task/view contract. |
| KA-R06 | RETAIN | MUST | H, D1, D2 | Active continuation chain and parent/return semantics must be reconstructable where a live route exists. |
| KA-R07 | REFINE / SPLIT | MUST for governing/risk discovery; SHOULD for adjacent recall | H, B2, B3, D5 | High recall is safety-critical for governing/risk-bearing knowledge. Discovery of merely adjacent exploratory knowledge remains important but is not a deterministic safety guarantee. |
| KA-R08 | REFINE / CONDITION | CONDITIONAL MUST | B1, B2, D5, D8 | A receipt is mandatory for consequential authority resolution, migration/qualification and other governed transitions. Ordinary exploratory reconstruction may use a lighter receipt. Receipt proves traversal/decision state, not semantic comprehension. |
| KA-R09 | STRENGTHEN | MUST | H, B1, D5 | Authority preflight must resolve applicable governing source set **and bind the material action contract to the proposed guidance/action**. Reading the right source alone is insufficient. Missing/conflicting required authority fails visibly according to consequence policy. |
| KA-R10 | RETAIN + CLARIFY | CONDITIONAL MUST | H, B2, D5 | Material known risks/reopen triggers must activate when task/conditions intersect them; activation reliability is the goal, not proof that current discoverability is always poor. |
| KA-R11 | RETAIN | MUST | H, B1, D5, D6, D7 | Missing authority, conflict, inaccessible private state and material uncertainty remain explicit. |
| KA-R12 | REFINE | MUST | H, D1, D3, D6 | Preserve necessary epistemic distinctions, but do not freeze the original list as one universal artifact taxonomy. Current, candidate, historical/formerly-applicable, superseded, rejected/known-wrong, evidence, unresolved and limitation states must remain distinguishable when material. |
| KA-R13 | STRENGTHEN | MUST | H, B4, D5, D6 | Resolve authority from action, scope, role/status, environment, applicability/authority time and supersession semantics. Current authority can be a **source set**. Recency/similarity alone are insufficient. |
| KA-R14 | STRENGTHEN | MUST | H, D5, D6 | Make conflict/supersession machine-resolvable where declared and distinguish replacement/obsolescence from update/supplement/refinement/correction when current authority depends on the difference. |
| KA-R15 | REFINE | MUST | H, D1, D2, D5, D6 | Material relationships must be explicitly queryable. Relation types/metadata are demand-driven; richer relation state/time/certainty/provenance is required only when the relation itself carries material semantics. |
| KA-R16 | STRENGTHEN | MUST | H, D2, D6, D8 | Preserve current/history separation and allow selective distinction among applicability time, repository-knowledge time and authority-transition time when those differ materially. Do not impose universal bitemporal structure. |
| KA-R17 | STRENGTHEN | MUST | H, B1, D7 | `loss-aware synthesis` becomes **view-contract fidelity**: source support, coverage, epistemic/authority/relational/temporal meaning, minority evidence and drill-down must survive where required by the representation's purpose. |
| KA-R18 | STRENGTHEN | MUST | H, B4, D3, D4, D7 | Material promoted/consequential synthesis needs source/transformation provenance at sufficient granularity for audit without forcing universal sentence-level provenance. |
| KA-R19 | RETAIN | MUST | O, P, D4 | Keep one explicit project-development authority. Current authority remains public ADS repository until an explicit accepted switch. |
| KA-R20 | RETAIN + CLARIFY | MUST | H, D3, D4 | Every persistent store/view has an explicit authority class; capture/candidate surfaces and derived views do not acquire authority by convenience or repeated use. |
| KA-R21 | REFINE | MUST | D4, D8 | Derived state used materially by reconstruction declares an appropriate rebuildability class. Structural projections should normally be reproducible deterministically; probabilistic synthesis may be regenerable/auditable rather than byte-identical. Loss of derived state cannot destroy unique accepted truth. |
| KA-R22 | STRENGTHEN | MUST | D3, D4 | Unique accepted insight discovered through human/model synthesis crosses an explicit, source-traceable authority-promotion boundary. Promotion is an authority transition, not cache persistence. |
| KA-R23 | STRENGTHEN | MUST | H, D4, D6, D8 | Material derived views expose sufficient source revision, transformation/generator and freshness/authority-closure information to detect staleness for their declared contract. |
## 6. Original requirement reconciliation matrix: KA-R24 through KA-R45

| ID | Disposition | Proposed strength | Evidence | Reconciliation |
|---|---|---|---|---|
| KA-R24 | RETAIN + STRENGTHEN | MUST | H, B2, D5 | Probabilistic retrieval may nominate candidates and improve recall, but may not silently resolve high-consequence governing authority where explicit applicability/precedence semantics exist. |
| KA-R25 | RETAIN + CLARIFY | MUST | H, D1, D2 | Active/paused/blocked/completed/superseded workstream state remains explicitly queryable; workstream identity is not assumed to equal the file documenting it. |
| KA-R26 | RETAIN | MUST | H, D1 | Deliberately resumable paused work preserves reason, return condition, parent objective and resume target. |
| KA-R27 | RETAIN | MUST capability | H, D2 | Multiple dependency edges remain supported; no forced tree when control flow is naturally DAG-like. |
| KA-R28 | RETAIN + CLARIFY | MUST | H, D3, D6 | Recovery distinguishes intended, durably completed and still-pending work from durable action/project evidence, not previous-chat plans. |
| KA-R29 | RETAIN | MUST | H, O | Stale/conflicting updates by concurrent collaborators must be detectable; exact concurrency mechanism remains open. |
| KA-R30 | RECLASSIFY | QUALIFICATION MUST | B3, D8 | Fixed/read-budget discipline is a **candidate qualification rule**, not a runtime architecture property. Budgets should be task-class-specific and calibrated against useful current performance. |
| KA-R31 | REFINE | MUST | B3, D8 | Required cold-start/reconstruction cost must not be structurally proportional to total history. Drop the overly rigid expectation that every 5x/10x scenario must fit exactly the same budget regardless of legitimately increased active-domain complexity. |
| KA-R32 | RETAIN + CLARIFY | MUST | B3, D7, D8 | Mandatory bootstrap/active core remains bounded; historical growth moves behind progressive drill-down and recurring consolidation rather than being copied forever into active surfaces. |
| KA-R33 | STRENGTHEN | MUST | H, D8 | Ordinary local changes should incur manual and generated maintenance proportional to the affected semantic/dependency neighborhood, not total corpus/history. Global generated rebuilds may be automated and periodic. |
| KA-R34 | STRENGTHEN | MUST | H, B3, D4, D8 | Observe active-surface pressure, route fan-out, stale derived state, ambiguity, reconstruction cost, consolidation pressure and other candidate-specific saturation signals before catastrophic degradation. |
| KA-R35 | RETAIN + CLARIFY | MUST | O, D2, D4 | Core authority, state and navigation semantics remain human-inspectable and machine-consumable; not every internal index representation must be hand-readable if its source/contract is inspectable. |
| KA-R36 | RETAIN | MUST | O, B2, D4 | Core continuity remains provider/tool portable at the authority level. Equal performance across every tool is not required, but capable collaborators must be able to reconstruct from project-controlled durable state. |
| KA-R37 | RETAIN | MUST / OWNER POLICY | P | Preserve explicit public/private authority delegation. Private continuity cannot silently redefine public ADS state. |
| KA-R38 | RETAIN | MUST / OWNER POLICY | P | Public derived outputs must not leak private-only paths, credentials, locations or facts outside their delegated boundary. |
| KA-R39 | RETAIN | MUST / OWNER POLICY | P | Public reconstruction remains usable without private detail unless the task genuinely requires delegated private state; then dependency/verification status is explicit. |
| KA-R40 | STRENGTHEN | QUALIFICATION MUST | H, B1-B4, D5, D7, D8 | Candidate qualification must test structural integrity **and behavior**, now including source activation, action-contract fidelity, uncertainty, reconstruction efficiency, consolidation fidelity and maintenance economics. |
| KA-R41 | REFINE / EXPAND | QUALIFICATION MUST | B1-B4, D7, D8 | Reconstruction evaluation remains multidimensional; extend it with task fidelity, material omission, authority/action resolution cost and relevant active-surface/maintenance metrics. Do not reduce selection to one aggregate score. |
| KA-R42 | RETAIN + CLARIFY | MUST | H, D4, D5 | Optional-service failure must not create false confidence. Fallback/failure behavior is consequence-sensitive: high-consequence required authority fails visibly; low-risk optional capability may degrade with explicit uncertainty. |
| KA-R43 | STRENGTHEN | MUST | T, D1, D3, D6, D7 | Migration preserves semantic identity where continuity is intended, authority, provenance, temporal/supersession meaning, discoverability and rejected/historical rationale where material. Merge/split/rename/representation changes need explicit reconciliation. |
| KA-R44 | RETAIN | MUST / TRANSITION INVARIANT | T | Current authority remains live until the successor passes qualification, migration reconciliation and rollback/recovery criteria. |
| KA-R45 | RETAIN + CLARIFY | MUST | O, T | The architecture must coordinate a redesign of itself, including capture of the redesign reasoning, authority transition and recovery from interruption. |

## 7. New requirements revealed by D1-D8 and owner clarification

The later evidence adds five properties that are not cleanly expressible by merely editing the original wording.

### KA-R46: representation-independent continuity of identity

**Proposed strength: MUST**

Where the project deliberately regards a subject, governed knowledge unit, workstream/activity, evidence object or other durable thing as continuous across a rename, path move, representation replacement or other carrier change, the architecture must be able to preserve that continuity without assuming that the human-readable label/path is the identity.

This requirement does **not** require universal semantic IDs for every paragraph, file or relation. Identity granularity must be justified by persistence, cross-context reference, independent lifecycle, provenance or ambiguity-reduction value.

Evidence: O, D1, D2, D6.

### KA-R47: multi-axis organization without truth duplication

**Proposed strength: MUST**

The same durable knowledge must be able to participate in multiple relevant organizational views or contextual groupings, such as semantic subject, authority state, workstream, provenance, temporal state, artifact/evidence depth and reconstruction task, without copying unique project truth into independently maintained competing structures.

A deterministic preferred/default route may exist for ordinary continuation without becoming the object's only semantic parent.

Evidence: O, H, D1, D2, D8.

### KA-R48: capture, consolidation and promotion boundary

**Proposed strength: MUST for semantic separation; SHOULD for capture ergonomics**

The architecture must distinguish potentially valuable captured reasoning from consolidated candidate understanding and explicitly promoted durable authority when those roles differ. Conversation-born insight must have a sufficiently low-friction intake path that important reasoning need not be lost merely because it does not yet fit a heavyweight canonical artifact.

Captured/candidate material must not acquire authority automatically. Promotion of unique accepted understanding is explicit and source-traceable. Retention of unpromoted material is selective rather than an obligation to store every token/intermediate result forever.

Evidence: O, D3, D4, D7, D8.

### KA-R49: selective temporal and supersession semantics

**Proposed strength: CONDITIONAL MUST**

Where authority, audit, historical reconstruction or correction semantics depend on time, the architecture must be able to distinguish domain/applicability time, repository knowledge/recording time and authority-transition time as needed. It must also preserve materially different replacement, update/supplement, correction and former-validity semantics.

The requirement is selective: universal bitemporal/tritemporal metadata is not justified for knowledge where these dimensions cannot diverge materially.

Evidence: H, D5, D6.

### KA-R50: recurring active-surface consolidation lifecycle

**Proposed strength: MUST capability**

The architecture must provide a recurring mechanism for reducing active-routing/context pressure as knowledge accumulates while preserving durable history, provenance and drill-down. Consolidation should be triggerable from measurable lifecycle or saturation pressure rather than arbitrary file-count aesthetics, and high-consequence consolidation must satisfy the relevant fidelity/view contract before detail is made latent.

Evidence: O, H, B3, D7, D8.

## 8. Requirements deliberately **not** added

The evidence could easily tempt the project into freezing mechanisms prematurely. Research 130 explicitly rejects the following as requirements at this boundary:

```text
use RDF / SKOS / OWL
use a graph database
use SQLite / SQL
use an event-sourced knowledge store
assign a semantic ID to every sentence or claim
store every conversation message indefinitely
use a vector database
use GraphRAG / RAPTOR / one named retrieval system
use one particular policy language / rule engine
implement bitemporal tables universally
require every derived view to be materialized persistently
require two-model review for every summary
require a fixed count of lifecycle states
```

Those remain mechanism choices or disproportional generalizations from external evidence.

## 9. Invariant reconciliation matrix

| ID | Disposition | Evidence | Proposed V0.2 interpretation |
|---|---|---|---|
| KA-I01 | RETAIN | O, H | Durable project authority outranks transient chat/model memory. |
| KA-I02 | RETAIN | O, D4 | One explicit project-development authority; convenience/derived stores cannot silently become competing truth. |
| KA-I03 | RETAIN + STRENGTHEN | D3, D4 | Derived state contains no unique accepted truth unless explicitly promoted through the authority boundary. |
| KA-I04 | STRENGTHEN | H, D6 | Current, historically/formerly valid, superseded, rejected/known-wrong and unresolved knowledge remain distinguishable where material. |
| KA-I05 | STRENGTHEN | H, B1, D5 | Consequential guidance/action requires applicable governing authority resolved and observably consumed **and material action-contract constraints preserved**, or it fails according to consequence policy. |
| KA-I06 | RETAIN | H, D5 | Missing required evidence or unresolved governing conflict is surfaced rather than guessed/blended away. |
| KA-I07 | STRENGTHEN | H, D7 | Provenance plus every must-preserve semantic property required by the target view survive synthesis/compression/migration; deeper evidence remains recoverable. |
| KA-I08 | RETAIN | T | Old continuity remains operational until explicit qualified authority switch. |
| KA-I09 | RETAIN | H | Resumable paused work has explicit reason, return condition, parent relationship and target. |
| KA-I10 | RETAIN | P | Public/private authority separation is preserved and public derived views do not leak private-only material. |
| KA-I11 | RETAIN | O, B2 | Fresh continuation cannot depend on the previous conversation being available. |
| KA-I12 | RETAIN + CLARIFY | B3, D8 | Required cold-start/reconstruction cost is not structurally proportional to accumulated history; legitimate active complexity may still change the exact budget. |
| KA-I13 | STRENGTHEN | H, D8 | Routine local knowledge change does not require unbounded manual/global maintenance; cost normally follows the affected dependency/semantic neighborhood. |
| KA-I14 | RETAIN + CLARIFY | D5 | Optional probabilistic retrieval failure cannot silently bypass governing-authority safety or create false reconstruction success. |
| KA-I15 | RETAIN + EXPAND | H, D4, D8 | From durable state the architecture can state its live route/authority/reconstruction/qualification status and enough derived-view freshness/health to avoid false currentness. |

## 10. Proposed new invariants

### KA-I16: capture does not imply authority

Potentially useful captured or consolidated-candidate knowledge does not become accepted project authority merely because it is stored, summarized, indexed or repeatedly retrieved. Authority promotion is explicit.

Evidence: D3, D4, D7.

### KA-I17: intended semantic continuity is not forced to equal carrier continuity

When the project deliberately declares that a durable knowledge object/workstream/subject remains the same across label/path/representation change, the architecture can preserve that continuity and its provenance without treating the new carrier as an unrelated truth object.

Evidence: O, D1, D2, D6.

## 11. Requirements that changed most materially

The following Phase-B assumptions changed enough that candidate designers must not rely on the original wording alone:

```text
KA-R02
    repository-native entry
        -> stable project-controlled entry

KA-R04
    full broad orientation before narrow consequential work
        -> broad orientation for generic continuation;
           task-shaped minimum safe orientation for narrow governed work

KA-R08
    receipt for every reconstruction
        -> mandatory where consequence/qualification/migration requires observability

KA-R09
    source resolution + consumption
        -> source resolution + consumption + action-contract binding/conformance

KA-R13 / R14 / R16
    generic authority/supersession/history
        -> action-shaped source-set authority + replacement-vs-update + selective temporal semantics

KA-R17 / R18
    loss-aware traceable summary
        -> multidimensional view-contract fidelity + proportionate source-unit provenance

KA-R21
    rebuildable or not
        -> declared rebuildability strength appropriate to representation

KA-R30 / R41
    acceptance-property wording
        -> explicit qualification-process requirements

KA-R31 / R33 / R34
    context-budget scaling
        -> lifecycle economics, active-surface pressure and dependency-local fan-out
```

## 12. Requirements whose evidence became weaker or more calibrated

The reconciliation does not simply strengthen everything.

### 12.1 Broad orientation failure claim is weaker

BL-003 shows that the drifted current map did **not** prevent broad project reconstruction when the model had strong tree/search access and was willing to read deeply. Therefore the redesign case for KA-R04/R07 is primarily reliability, efficiency and default-routing quality rather than proof that broad reconstruction is otherwise impossible.

### 12.2 Collaboration-process discoverability is stronger than historical failure alone implied

BL-002-B and BL-002U show that the repository-native collaboration process can be recovered efficiently by a fresh strong model. KA-R10/D5 activation requirements therefore target reliability/repeatability, not an assertion that current process knowledge is generally undiscoverable.

### 12.3 Exact-source hierarchy is more recoverable than historical Cockpit integration suggested

BL-004 demonstrates strong source-strength reasoning under the historical snapshot. Exact implementation/provenance activation remains important, but the architecture should not assume that models inherently collapse all source layers unless mechanically forced.

### 12.4 Authority activation alone is insufficient

BL-001 changes the opposite direction: even successful governing-source discovery/consumption can produce an incorrect/incomplete task output. This strengthens KA-R09/I05 around action-contract fidelity.

## 13. Requirements primarily grounded in owner/project values rather than external empirical proof

Some requirements are legitimate constitutional choices even when external literature cannot prove them optimal:

```text
one explicit project-development authority
public/private authority delegation
old authority remains until qualified switch
provider-independent durable continuity
self-hosting evolution
owner-visible migration preservation
```

These should not be disguised as universal scientific facts. They are project-governance choices with strong internal rationale.

## 14. Proposed V0.2 boundary summary

If accepted, the requirement boundary becomes:

```text
50 KA-R requirements
    original 45 retained in some form
    5 explicit additions: KA-R46..KA-R50

17 KA-I invariants
    original 15 retained/refined
    2 explicit additions: KA-I16..KA-I17
```

The important point is not the count. The revised boundary is **less mechanism-specific** in some places and **more semantically precise** in others.

It removes the hidden assumption that every consequential task must first reconstruct the whole project, while adding distinctions the external evidence shows were missing: stable identity, multi-axis views, capture/promotion boundaries, selective temporal semantics and recurring active-surface consolidation.

## 15. Owner-review questions before freezing V0.2

No target architecture decision is needed from the owner at this stage. The owner-review decision is narrower:

1. Does the owner accept the major calibration that **generic continuation requires broad orientation, but narrow consequential work may use a smaller action-shaped safe orientation** rather than mandatory full Tier A first?
2. Does the owner accept adding KA-R46..KA-R50 and KA-I16..KA-I17 as architecture-neutral requirements/invariants?
3. Does the owner want any requirement to remain stronger than the evidence currently supports, as an explicit project value rather than an empirical claim?
4. Does the owner want the requirement set kept intentionally broad enough that radically different successor families remain eligible?

Unless the owner changes the direction, the recommended answer to question 4 is yes.

## 16. Next boundary after owner acceptance

After owner acceptance/amendment:

```text
freeze reconciled requirements V0.2
    -> expose the previously withheld owner paper/video
       as incremental evidence, not as the initial design anchor
    -> evaluate what it adds, contradicts or fails to address
    -> construct multiple neutral candidate architecture families
    -> compare them against V0.2 requirements + stress tests + lifecycle economics
    -> only then narrow toward a target architecture
```

The owner paper/video remains withheld **until** this reconciliation is accepted or amended.

```text
RESEARCH130=PROVISIONAL_REQUIREMENTS_RECONCILIATION_COMPLETE
ORIGINAL_REQUIREMENTS_DELETED=0
PROPOSED_REQUIREMENTS_V02=50
PROPOSED_INVARIANTS_V02=17
TARGET_ARCHITECTURE=NOT_SELECTED
OWNER_REVIEW=REQUIRED_BEFORE_FREEZE
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
NEXT=OWNER_REVIEW_AND_FREEZE_OR_AMEND_REQUIREMENTS_V02
```