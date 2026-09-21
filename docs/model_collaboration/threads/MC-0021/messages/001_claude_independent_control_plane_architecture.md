# MC-0021 Message 001 — Claude Independent Activation/Orchestration Control-Plane Architecture

**Thread:** MC-0021
**Message:** 001
**Date:** 2026-09-21
**Collaborator:** Claude / fresh-claude-for-mc0021
**Role:** INDEPENDENT_REVIEWER / COUNTER_DESIGNER / CRITIC
**Review mode:** INDEPENDENT_THEN_COMPARATIVE / Phase 1 (independent)
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact independent substantive base:** `b649c1a846d3bf9274fd718e0efd8de9d63bd990`
**Candidate target deliberately not inspected:** `f73239ee486132a94701de80514ffd11480b9ecd`
**Authority:** Collaboration evidence only. This message does not change project authority, amend Research 218 or Requirements V0.2, open AO-9/AO-10, or alter W5/W6/W8 state.

## 0. Provenance and independence statement

Current-branch reads were limited to `docs/current_routing.json`, `docs/model_collaboration/REVIEW_INBOX.md` and the MC-0021 `BRIEF.md` / `THREAD.md` / `STATE.json`.

All substantive evidence was read at the exact independent base:

```text
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/219_activation_orchestration_self_hosting_bootstrap_program.md
docs/research/220_ao1_retrospective_activation_orchestration_completeness_audit.md
docs/research/221_ao2_control_plane_capability_boundary_and_failure_taxonomy.md
docs/research/project_knowledge_activation_orchestration/001_chat26_owner_source_interaction_orchestration_evidence.md
docs/research/project_knowledge_activation_orchestration/002_chat27_activation_self_hosting_bootstrap_evidence.md
docs/research/project_knowledge_activation_orchestration/003_chat28_continuation_reconstruction_activation_gap.md
docs/research/project_knowledge_activation_orchestration/AO2_CONTROL_BOUNDARY_AND_FAILURE_TAXONOMY_V01.json
docs/research/PROJECT_KNOWLEDGE_FAILURE_CORPUS.md
docs/OPEN_ARCHITECTURE_BACKLOG.md
docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
docs/project_knowledge/architecture/reconstruction_and_action.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
```

Research 222-226, the AO3-AO7 machine syntheses, Checkpoints 559-563 bodies and all descendant synthesis were not read, listed, diffed or searched. No candidate content was inferred from commit metadata.

Where I did not read a file named in BRIEF §4 (`AO1_COMPLETENESS_MATRIX_V01.json`, Foundation 014, Research 144/168/170/178/179/205, `whole_architecture.md`, `migration_and_cutover.md`, `OPEN_QUESTIONS.md`, `model_collaboration/README.md`), I relied on Research 220's and 221's explicit reconstruction of their content rather than claiming direct inspection. Every load-bearing claim below is traceable to a file I read directly. I flag the two places where this secondhand basis could materially change my conclusion.

## 1. Position in one page

I do not think the project's central problem is that the control plane is missing a loop, a router, a classifier or an index.

Every documented failure in the corpus has the same shape:

```text
the collaborator produced a fluent, plausible, consequential output
without ever having asked what the project required it to establish
before an output of that kind was safe
```

KF-SD-01 did not misroute. It never routed. KF-SD-03 did not choose the wrong collaboration mode. It never consulted the collaboration question. Chat 27 did not rank AB-027 too low. AB-027 was never a candidate. Chat 28 did not traverse the evidence packet shallowly. It did not traverse it.

This matters because it changes what must be built. A better router does not help a system whose defining failure is that the router is never invoked. Research 219 §11's candidate loop has eleven sequential stages, each of which is skippable by exactly the mechanism that produced every failure in the corpus. AO-2 §14's constraint 4 — *mandatory knowledge closure remains project-controlled* — is correct and is the whole game, but AO-1/AO-2 never ask the follow-on question: **project-controlled by whom, checked against what, and enforced at which chokepoint that already always runs?**

My preferred architecture therefore optimizes for one property above all others:

> The number of places where a probabilistic component can silently omit a mandatory step should be as close to zero as the evidence allows, and the remaining places should be attached to actions the project already cannot skip.

Everything else — event taxonomy, intent classification, collaboration scoring, semantic navigation — I treat as *enrichment*: valuable, model-assisted, and explicitly allowed to fail without the system becoming unsafe.

I also make one structural move that I believe is the most important disagreement I will have with any staged-AO design:

> Safety gating is driven by the shape of the **proposed output**, not by the classification of the **owner's input**.

AO-R1 makes event interpretation the head of the chain. That makes AO-F01 (`EVENT_MISCLASSIFICATION`) catastrophic: one wrong classification silently disables activation, authority, conformance, collaboration and preservation downstream. I want the safety property to survive a wrong event class.

## 2. Preferred architecture: two gates, source-declared predicates, one ledger

Working name: **CP-CLAIM-GATE**.

Three parts. Nothing else is mandatory.

### 2.1 Part one — source-declared activation predicates

Mandatory activation is a property of the knowledge that demands activation, not of a central registry.

Candidate 01 already has the right substrate. `governing_procedure.v1` (Spec 028 §17) declares *governed action classes / scope*. Governed sources may declare `risk_or_reopen_triggers` (§9). The generated `authority_index` and `risk_obligation_index` (§20) are the derived join.

The addition is small and stays inside the existing pattern: a governing/risk-bearing source declares **the observable condition under which it must be in context**, in a bounded predicate vocabulary evaluated against a small structured *situation descriptor*, not against free text.

```text
predicate operands (bounded, project-controlled vocabulary)
    proposed output contains ordered operational steps
    proposed output mutates repository state
    proposed output changes a frozen design element
    proposed action class     e.g. RUNTIME_RESTART, BRANCH_PUBLISH, PROMOTE
    target scope              e.g. tools/project_knowledge/**, docs/research/218*
    workstream identity / state
    environment / runtime availability
    declared trigger condition observed
    consequence class
```

Properties this buys, mapped to the BRIEF §5C constraints:

```text
no whole-repository read
    predicates are compiled into a derived index; evaluation reads a descriptor, not a corpus

no owner path hints
    the source declares its own applicability; the owner never names it

search rank is never authority
    retrieval nominates OPTIONAL supporting evidence only;
    MANDATORY closure comes from predicate evaluation

no giant manually maintained registry
    declarations are source-local, so maintenance is dependency-local (KA-R33)
    and the index is rebuildable (KA-R21)
```

This is the mechanism that closes KF-SD-01 at the input side: `OPERATIONS.md` declares that it governs `RUNTIME_RESTART` ordering, so any proposed output containing ordered runtime-restart steps mandatorily activates it, regardless of whether the collaborator classified the owner's message correctly.

### 2.2 Part two — two mandatory gates

**G-IN — Closure Claim.** Before consequential output, the actor emits a small structured claim:

```text
situation descriptor as evaluated
predicates that fired, and the sources they made mandatory
for each mandatory source: semantic_id, carrier path, exact source revision
                           (Spec 028 §18 descriptor), activated constraint IDs
authority resolution status (Spec 028 §25 status enum)
what was deliberately left latent, and why
unresolved uncertainty
```

**G-OUT — Contract fidelity.** Before the output is emitted or dispatched, the proposed guidance/action is checked against the constraints the claim activated: ordered constraint IDs in the asserted order, declared prohibitions absent, declared postconditions present.

G-OUT exists because the corpus proves the two failures are separable. KF-SD-01 and BL-001 are cases where the right source was resolved and the final instruction still inverted its order; KF-AS-01 and KF-CS-01 are cases where the correct exact source existed and a summary was used instead. AO-1 §9 names this gap precisely and finds no production stage that closes it. An entry-time reconstruction plan structurally cannot close it, because the consequential output often arrives many turns after entry on a topic nobody anticipated at entry.

Nothing between G-IN and G-OUT is mandatory or ordered. Process routing, collaboration suggestion, navigation, semantic retrieval and intent interpretation all sit in that space as enrichment.

### 2.3 Part three — one control evidence ledger

A single append-only ledger whose rows are claims, gate verdicts, overrides and a small set of typed exception rows. Self-observation is *queries over the ledger*, not a separate observer subsystem.

This collapses what AO-1/AO-2 imply would be several monitoring surfaces (activation-miss evidence, evolution-trigger monitoring, obligation closure, Git lifecycle drift, control observability) into one artifact with one authority class (`derived`/`evidence`, never `canonical`).

It also gives AO-F18 a **computable** definition, which is the single most valuable thing in this design:

```text
OWNER_REMINDER_DEPENDENCY is detected when the owner names a source or
mechanism that appears in the immediately preceding claim's latent or
not-evaluated set, or in neither set, and that is then used.
```

That converts the project's motivating frustration from an anecdote the owner has to notice into a regression assertion a test can make. Chat 27 and Chat 28 both become mechanically detectable after the fact, not only owner-caught.

### 2.4 Enforcement point — reuse, do not invent

The most dangerous thing this program can do is create a new discipline the owner must remember. AB-023 already records that recursive risk.

So CP-CLAIM-GATE attaches to chokepoints that already always run and already fail closed:

```text
interaction entry
    the existing repository-first continuation path already reads canonical
    surfaces; the claim is produced there as part of reconstruction

repository mutation / publication
    Spec 028 §34 already requires project-knowledge validation to become a
    component of the aggregate public repository-integrity gate, which is
    already fail-closed and already emits PUBLIC_REPOSITORY_INTEGRITY=PASS
```

No new ritual. The gate rides existing mandatory machinery.

## 3. Required topics A-M

### A. Control-loop shape

Not one closed loop and not staged escalation. **Two mandatory synchronous gates plus unordered enrichment**, with a separately-scheduled asynchronous observation pass over the ledger.

On every project event:

```text
maintain the situation descriptor        cheap, structural, no corpus read
```

Conditionally, when the proposed output is consequential:

```text
G-IN closure claim
G-OUT contract fidelity check
```

Asynchronously, at governed boundaries only:

```text
ledger queries: activation misses, owner-reminder events, predicate precision,
                obligation coverage, Git lifecycle drift, trigger observations
```

The reason I reject the eleven-stage pipeline is not that its stages are wrong — they are a good description of what a well-run interaction does. It is that making them a mandatory sequence creates eleven silent-skip sites and forces per-message work that KA-R30/R31 budgets will not absorb. Describing good behavior and enforcing safety are different jobs and should not share a mechanism.

I keep Research 219 §11's flow as **advisory process vocabulary**. I refuse it as a control contract.

### B. Model-assisted versus project-controlled boundary

AO-2 §7 draws this boundary correctly by category. I sharpen it by *direction*:

```text
MODEL-ASSISTED, ADVISORY, MAY BE WRONG WITHOUT HARM
    intent interpretation
    event-class hypothesis
    process suggestion
    collaboration suggestion
    semantic relevance / optional supporting evidence
    routing explanation

PROJECT-CONTROLLED, DETERMINISTIC, FAIL-CLOSED
    predicate evaluation over the situation descriptor
    mandatory source set
    authority resolution status
    activated constraint IDs and their order
    mutation permission
    required-review obligation existence
    promotion / authority transition
    claim verifiability checks
```

The asymmetry that makes this work: **advisory components may only add, never subtract.** A model may propose that more should be activated, that a second collaborator would help, that a different process fits. It may never conclude that a fired predicate does not apply. Removing a mandatory obligation is an explicit owner override, recorded as a ledger row.

On natural-language intent and the question/directive distinction: I treat the BRIEF §3 constraint as load-bearing architecture, not etiquette. A question is a request for analysis; only an explicit change request authorizes mutation. Mechanically this is enforced not by classifying the sentence but by the mutation-permission gate: **mutation requires an explicit authorization token in the situation descriptor, and inferred intent cannot supply it.** If the collaborator believes a change was requested and the owner believes a question was asked, the gate fails closed and asks. This makes AO-F01 non-catastrophic in the only direction where it is expensive.

### C. Activation versus search/reconstruction

Three layers, matching AO-2 §6, with clear authority:

```text
SEARCH           nominates optional supporting evidence; never mandatory
RECONSTRUCTION   establishes the bounded state required for safe work (Spec 028 §26)
ACTIVATION       predicate evaluation; the only source of MANDATORY closure
```

Against the four named anti-requirements: no whole-corpus read (predicate index); no owner path hints (source-declared applicability); no search-rank-as-authority (structurally separated — KA-R24 and KA-I14 already demand this and the predicate design satisfies it by construction); no giant manual registry (declarations are dependency-local).

Against the four falsification targets:

```text
Chat 17 / KF-SD-01
    proposed output contains ordered runtime-restart steps
    -> OPERATIONS.md predicate fires -> mandatory -> G-OUT checks step order
    closed by BOTH gates; this is the only corpus case that exercises both

Chat 23 / KF-SD-03
    proposed action class = OPEN_MODEL_COLLABORATION
    -> collaboration-protocol predicate fires -> MC-*/REVIEW_INBOX protocol mandatory
    closed at G-IN

Chat 27
    proposed output changes/challenges a frozen design element (Research 218)
    -> AB-027 + AB-031 + declared reopen triggers fire
    closed at G-IN

Chat 28
    task class = conceptual design inside an evidence-rich active program
    -> the active research record declares its own evidence packet as
       required supporting reconstruction for design-class tasks
    closed at reconstruction, not by activation
```

Chat 28 is the honest weak case and I want to say so plainly. The omitted files were non-authoritative source evidence, not governing authority — Source Evidence 003 §3 is right to resist classifying it as AO-F02. Making non-authoritative evidence *mandatory* is exactly how activation overreach starts. My answer is narrow: **an active research program may declare a required supporting-evidence set for named task classes within its own scope, and that declaration expires with the program.** That is a bounded, self-retiring obligation owned by the program that created it. It is not a general rule that evidence packets are mandatory.

### D. Authority and action fidelity

The substrate exists. AO-1 §8 documents `AuthorityQuery`, deterministic resolution, `AuthorityReceipt`, revision binding, scope discrimination, joint authority, private-state evidence, activated constraints, precedence and fail-visible statuses. Research 168 proves it works *when the correct path runs*.

Two failures remain and they need different answers.

**Authority bypass** is closed by G-IN: consequential output without a resolved status is a fail-closed condition, and the claim binds exact revisions using the Spec 028 §18 descriptor so freshness and private dependency are decidable rather than assumed.

**Contract fidelity loss** is closed by G-OUT, and only partially. For it to work, the governing procedure must have declared structured, identified, ordered constraints. Spec 028 §17 already requires exactly that of `governing_procedure.v1`, and already says the structured declaration is the sole normative machine contract while prose remains authoritative for rationale, with contradiction producing a semantic-drift finding. G-OUT is the consumer that clause was waiting for.

The consequence is a migration ordering claim I hold firmly: **the high-consequence operational runbooks must be among the first W5 migration units, not late ones.** `OPERATIONS.md` in particular. Until it carries structured ordered constraints, G-OUT has no opinion about the exact failure that opened AB-022. A gate that silently has no opinion looks like safety and is not.

### E. Process, workstream, recovery and Git routing

Process routing is advisory except where it is a gate. Only three process facts are gates: mutation permission, required-review obligation existence, and authority transition. Everything else — is this research or implementation, should a child workstream open, is this an incident — is a suggestion the owner or collaborator can override freely and cheaply.

On branch versus workstream, I accept the BRIEF's warning and go further: the relationship is **many-to-many**, not merely unequal. A branch may carry several workstream anchors; a workstream may span branches across rotation, promotion and recovery. `workstream.v1` already has `current_anchor` and revision binding (Spec 028 §15); the missing object is not a new registry but the join, which is derivable.

Git lifecycle (AB-032) then becomes predicates over `(branch, workstream states, unpublished qualified-commit count, staleness, divergence)` producing **ledger warnings**, never blocks — except the one case that is already fail-closed, publication integrity. I deliberately keep AB-032 off the critical path: it is P2, explicitly "preferably before W6," and bundling it into a P0 control responsibility inflates the minimum viable architecture without closing any corpus failure.

Interruption recovery follows Spec 028 §16 unchanged: completed work derives from durable receipts, never from a previous chat's plan. The ledger strengthens this because the claim tail *is* durable evidence of what was in flight.

Parent/child resume: a closing child resolves its declared `return_condition` to a `resume_target`. `RESUME_TARGET_LOSS` is a fail-visible-and-reconstruct condition, not a fail-closed one — the corpus (KF-CR-02) classifies this as a structural gap with no proven wrong outcome, and I decline to escalate it beyond the evidence.

### F. Collaboration and tool routing

The collaboration machinery is mature and I would add almost nothing to it. D-034, Specification 024's mode enum, the `REQUIRED`/`OPTIONAL` requirement values, the `BEFORE_TARGET_MUTATION` / `BEFORE_THREAD_RESOLUTION` / `BEFORE_PROMOTION` / `NONE` gate vocabulary and the `REQUIRED -> must name a real gate` constraint are all already correct and already accepted.

What is missing is narrow: **opening the obligation is currently a human act.**

So the proposal is small. Sources that own consequential design elements declare their own review obligations:

```text
a change to a frozen design element of class X
    -> requires INDEPENDENT_THEN_COMPARATIVE
    -> gate BEFORE_THREAD_RESOLUTION
```

Then:

```text
obligation existence   GATE, computed, fail-closed
collaborator choice    ADVISORY, suggested, owner may override
transport              UNCHANGED, manual relay remains fully acceptable
REVIEW_INBOX.md        GENERATED, not authored
```

Generating the inbox is worth calling out. `DEFERRED_REVIEW_AND_CATCHUP.md` already records that MC-0003 identified manual inbox/state drift as a real risk and lists deterministic inbox generation as evidence-backed future candidate #2. The inbox already declares itself a convenience index over authoritative per-thread state. Generating it costs almost nothing and removes an authored surface. This is the single cheapest item in my whole proposal and it directly closes KF-SD-03.

Manual transport stays manual. AO-2 §5 is right that manual transport is not manual orchestration, and AB-003/AB-004/AB-006 must stay deferred. Nothing here requires automatic dispatch, wakeup, or multi-agent machinery.

### G. Architecture evolution

Triggers are declared on the sources that own them (`risk_or_reopen_triggers`); observation rows land in the ledger; classification is an owner decision; a trigger opens evaluation and never mutates a frozen design. That much follows Research 219 §13 and AO-2 §11 and I have no quarrel with it.

My contribution is a mostly-deterministic discriminator for the distinction AO-1 §25 and Research 219 §13 both need and neither operationalizes:

```text
implementation contradicts the source's STRUCTURED contract
    -> CONFORMANCE DEFECT            deterministic, machine-detectable

prose and structured contract disagree
    -> CLARIFICATION                 already a Spec 028 §17 semantic-drift finding

the structured contract cannot express the required behavior at all
    -> AMENDMENT / SUPERSESSION / REOPEN candidate
                                     requires judgment; opens governed evaluation
```

"The contract cannot express it" is a far better reopen signal than "someone felt friction," and it is observable. It also gives repeated-exception detection a precise form: N distinct ledger rows where the same structured contract had to be overridden for the same reason is evidence, countable, and does not depend on the owner noticing a pattern.

One thing I want to name that AO-1/AO-2 do not: **an override must itself be evidence.** When the owner overrides a gate, that is a first-class ledger row with a reason. Overrides are the highest-signal data the system will ever produce about whether its predicates are calibrated, and a design that treats override as an escape hatch rather than as measurement will lose exactly the information it most needs.

### H. Interaction continuity and break-glass

Research 219 §15 proposes a ~12-field interaction envelope. I think that is over-scoped and I would not build it.

The claim ledger already records the durable anchor, workstream, what activated and what stayed latent. The only genuinely additional continuity facts are three:

```text
last durable receipt
unpromoted material exists?  yes/no + where it would go
return condition
```

Everything else in the §15 list (interaction ID, provider, environment, session, mode, external collaborators, pending review) either already exists in `INTERACTION_PROVENANCE_AND_NAMING` and the thread `STATE.json` files, or is derivable from the ledger tail.

I also keep the distinction Source Evidence 001 §10 and AB-031 both insist on, and would enforce it structurally: **interaction is known to exist ≠ interaction content is recoverable.** The ledger may assert the first. It may never assert the second, because no repository marker can recover chat text the provider no longer serves. Conversation state never becomes authority — enforced by authority class, since ledger rows are `evidence`/`derived` and Spec 028 §9 already forbids those from being read as governing authority.

Context rollover becomes an ordinary interruption: the ledger tail is the receipt, the fresh interaction reconstructs from durable state, and unresolved material is requested rather than assumed. That is Research 219 §15 and Source Evidence 001 §11's intent with far less new machinery.

Break-glass satisfies the independence rule by construction: the ledger and the recovery procedures live in the repository, which is the authority, reachable by any path that can read Git — including the independent GitHub route when the local Runtime Bridge is the failed component. The recovery path does not traverse the control plane. A degraded control plane means "fall back to today's procedure," not "stop."

### I. Successor control before W8

**Yes — but in exactly one authority relationship: advisory and veto, never generative.**

```text
PERMITTED
    read current-authority surfaces as input
    evaluate predicates; emit claims and gate verdicts
    compute review obligations
    refuse / fail closed
    suggest process, collaborator, navigation

PROHIBITED
    generate any surface that current authority consumes
    resolve an authority conflict
    be the source of any project fact
    supply content of any kind
```

Against the five named hazards:

```text
dual authority
    it produces no semantic content; a verdict is not a fact

authority laundering
    every verdict cites the current-authority source and exact revision it was
    computed from; nothing enters via the bridge that was not already authoritative

compatibility takeover
    it writes no compatibility surface; Spec 028 §30 / W3 shadow rules unchanged

self-enabling successor state
    predicates derive from current-authority sources, so the bridge cannot widen
    its own scope without an edit to current authority

new single point of failure
    a veto-only component that is down degrades the system to the status quo,
    which is the current operating authority anyway
```

That last asymmetry is the whole reason I am comfortable saying yes. A **generative** bridge that fails takes its outputs with it. A **veto-only** bridge that fails leaves exactly today's system running. The risk of turning it on early is therefore bounded by the risk of the system we already operate.

Spec 028 §43's invariants hold unchanged. `AO-F17 BRIDGE_AUTHORITY_LEAK` remains fail-closed and becomes easy to test, because the bridge's permitted output types are a closed set: any bridge output that is not a claim, verdict, obligation or suggestion is a leak by definition.

The honest cost: veto-only does not reduce owner-reminder dependency on the *helpful* side. It will not route to Claude for you; it will only refuse to let a required review be skipped. I accept that, because suggestions that are wrong are cheap and vetoes that are wrong are expensive, and I would rather spend the early migration learning whether the predicates are calibrated than learning whether the generator is trustworthy.

### J. Self-observation and obligation closure

All four of the BRIEF's cases become ledger queries rather than subsystems:

```text
owner had to remind it of an existing mechanism
    owner names a source in the prior claim's latent/unevaluated set

accepted requirement never reached implementation
    obligation-coverage join (below) has a MUST row with no gate and no deferral

control behavior cannot explain why something activated
    a claim exists with no predicate attribution -> CONTROL_OBSERVABILITY_GAP

branch/process drift recurs
    N ledger rows with the same drift signature
```

The obligation join deserves its own paragraph because it is, I think, the highest value-per-unit-complexity artifact available to this program.

Spec 028 already has executable gate identifiers (PKA-G001..G017, PKA-G101..G109). Requirements V0.2 has KA-R identifiers. What does not exist is the link. Add a `discharges:` declaration to each executable gate and generate:

```text
obligation ID -> specification clause -> executable gate ID
             -> implementation evidence -> operational activation proof
```

Then fail the aggregate integrity gate on any MUST-level obligation with no gate and no explicit recorded deferral.

Run retrospectively, this produces exactly the AO-1 §7 finding: Specification 028 §26 and §32 carry MUST obligations (reconstruction planner, `resolve-authority`, `reconstruct`, `migration-audit`) with no corresponding row in the PKA-G001..G017 gate list. That gap would have been visible as a generated table row at W0 acceptance time rather than discovered by a retrospective audit two waves later. AO-1 §7.1 is right that this is a scheduling gap and not a retroactively failed gate; the join is the mechanism that makes scheduling gaps visible prospectively without rewriting history, which is exactly what `SCHEDULE_RECONCILIATION` asks for.

Nothing in this is automatic architecture change. Observation produces evidence. Evidence opens evaluation. Evaluation is an owner decision.

### K. Efficiency and complexity

Smallest architecture that still satisfies the evidence:

```text
1  source-declared activation predicates + derived predicate index
2  G-IN closure claim
3  G-OUT contract fidelity check
4  one control evidence ledger
5  the obligation-coverage join
6  generated REVIEW_INBOX
```

Six things, four of which are derived views over declarations that already exist in Candidate 01's model. No new service, no daemon, no database, no graph store, no vector store, no scheduled worker, no second authority surface.

What I delete relative to the staged program's apparent direction:

```text
the eleven-stage mandatory loop          -> two gates + unordered enrichment
the separate 12-field interaction envelope -> three fields on the ledger
a separately authored evolution register  -> generated view over declared triggers
a 15-class machine event taxonomy         -> advisory vocabulary; gates read output shape
per-row control services (31 or 8)        -> one composable mechanism
```

On per-message cost: the situation descriptor is structural and cheap. Predicate evaluation reads an index, not a corpus. Claims are emitted only for consequential output. Ordinary `BROAD_CONTINUATION` and exploratory work should see close to zero added mandatory reads, which is what KA-R30/R31/R32 require.

The complexity I refuse to remove: exact revision binding, the fail-closed statuses, the structured action contract, and the separation of mandatory closure from retrieval. Those are load-bearing for correctness and every one of them is already frozen in Requirements V0.2 or Specification 028.

### L. Migration and self-hosting

CP-CLAIM-GATE is well suited to self-hosting precisely because it is veto-only. Its artifacts are additive: a predicate index, a ledger, two generated views. Rollback is deletion — nothing downstream depends on them for truth, because none of them may contain unique accepted truth (KA-I03, Spec 028 §20).

Across conversations and interruptions, continuity comes from the ledger tail, which lives in the authority. Across implementation waves, the obligation join is the mechanism that prevents a second reconstruction-planner-class gap. Across authority migration, Spec 028 §43's prohibition is preserved because the bridge emits no compatibility surface.

The one genuine self-hosting risk: the control plane governs the migration that builds the control plane. If its predicates are wrong, it will confidently gate its own construction. Mitigation is the same one the project already uses well — the bridge's own consequential changes remain subject to independent review under the existing MC-* protocol, and the ledger makes its own false-positive and false-negative rates measurable during the migration rather than after it.

### M. Implementation and qualification implications

```text
MUST BECOME EXECUTABLE
    predicate declaration schema + validation
    predicate index generation (deterministic, rebuildable)
    claim emission + claim verifiability check
    G-OUT ordered-constraint / prohibition / postcondition check
    ledger append + schema validation
    obligation-coverage join generation
    REVIEW_INBOX generation
    Spec 028 §26 reconstruction planner and §32 CLI surfaces

MAY REMAIN CONCEPTUAL FOR NOW
    full event taxonomy
    collaborator scoring
    Git lifecycle policy beyond warnings
    automatic dispatch of any kind

MUST BE INSPECTABLE
    every claim, verdict, override and predicate attribution
    the predicate index and its source declarations
    the obligation-coverage table

REQUIRES DETERMINISTIC TESTS
    predicate evaluation
    index rebuild determinism / incremental-full equivalence
    claim verifiability (cited constraint IDs exist at cited revisions)
    ordered-constraint conformance
    obligation-join completeness

REQUIRES REAL HISTORICAL REGRESSION
    the suite in §4.8 below

REQUIRES INDEPENDENT REVIEW
    the predicate vocabulary itself
    the bridge authority relationship
    any proposal to give the bridge generative capability

MUST FAIL CLOSED
    authority bypass
    contract fidelity loss
    premature authority promotion
    bridge authority leak
    mutation without explicit authorization
```

Accepted-obligation-to-realization gaps I can name from the base:

```text
Spec 028 §26 reconstruction planner       selected + designed (R178/179), not implemented
Spec 028 §32 resolve-authority CLI        required, not implemented
Spec 028 §32 reconstruct CLI              required, not implemented
Spec 028 §32 migration-audit CLI          required, not implemented
PKA-W0-J1 activation/history regression   accepted in R179, no production regression
AB-027 trigger reconciliation             substrate exists only for migrated declarations
KA-R09 contract fidelity                  activation implemented, conformance stage absent
KA-R10 trigger activation                 index exists, no activation path from ordinary events
```

I have not independently verified the middle two lines against the production tree; they rest on AO-1 §§7, 9, 10, 22 and are flagged accordingly.

## 4. Required challenge output

### 4.1 Strongest alternative architecture considered

**Planner-Only.** Do not build gates. Finish the Specification 028 §26 reconstruction planner properly, expose `reconstruct <task-spec>` per §32, make it mandatory at interaction entry, and make its `ReconstructionContract` the only permitted basis for consequential work. One mechanism. Already specified, already designed in Research 178/179, already accepted as a W0 obligation in §26's MUST, already has a documented missing-implementation finding, already carries must-load sources, negative sets, freshness requirements, receipt requirements and fail/escalate conditions.

It is a genuinely strong alternative and I want to be fair to it. It is smaller than my proposal. It requires no new concepts. It reuses a contract the project already froze. It closes Chat 27, Chat 28 and probably KF-SD-03. Research 168 already demonstrates that when the correct reconstruction path runs, authority resolution, risk activation, stale-source rejection and receipt emission all work.

I reject it as *sufficient* for one reason: it is entry-time-only. It cannot close KF-SD-01 or BL-001, where reconstruction succeeded and the final output still violated the contract that reconstruction had correctly activated. An entry-time plan cannot bind an output produced forty turns later on a topic nobody anticipated at entry. AO-1 §9 finds exactly this gap and finds no production stage that fills it.

So my position is not "planner instead of gates" or "gates instead of planner." It is: **build the planner first — it is already owed — and add G-OUT, which is the only genuinely new safety mechanism in this program.** If AO-9 shows the planner alone closes the corpus, G-IN collapses into the planner's receipt and only G-OUT survives as a distinct thing. I would accept that outcome.

The second alternative, pure event-driven rules with no model in the loop, I reject as insufficient — the triggering conditions in the corpus are semantic ("this is an architecture concern," "a recurring problem was reported") and rules over free text will miss or over-fire. But I take one lesson from it, and it is the lesson that shaped my design: the *veto* conditions can be rule-based, because they are predicates over output shape, which is far more tractable than intent.

### 4.2 Strongest criticism of the preferred architecture

G-OUT requires a machine-checkable representation of the proposed guidance. For prose — and KF-SD-01 is prose, an ordered restart instruction — checking conformance means either the actor emits its steps in structured form citing constraint IDs, or a model checks prose against the contract. The second reintroduces probabilistic judgment at precisely the safety boundary the gate exists to protect. The first constrains how the collaborator may write, which is intrusive and will be resisted in ordinary work.

Worse, G-OUT's coverage is bounded by `governing_procedure.v1` adoption. Today that adoption is small. Outside it, the gate has no opinion — and a gate that silently has no opinion is more dangerous than no gate, because it produces a `PASS` that a reader will over-trust.

I do not think this is fatal, but it forces two commitments I would hold the design to: the high-consequence runbooks migrate early, and **G-OUT must report `NO_CONTRACT_AVAILABLE` distinctly from `CONFORMANT`.** If the design ever collapses those two verdicts, it has become gate theater.

A second criticism I should state against myself: I have designed primarily against a corpus of owner-caught incidents. §14 of the failure corpus warns explicitly that owner-caught incidents are overrepresented, that successful silent retrieval is not sampled, and that no prevalence claim follows from row count. My architecture may therefore be well-fitted to the failures that got written down and poorly fitted to the distribution of real interactions. The negative controls in §4.8 are the only defense I have against that, and they are weak.

### 4.3 Three most dangerous failure modes

**1. Claim fabrication / gate theater.** The claim is self-reported by the same probabilistic component whose unreliability motivated the gate. A model that would have skipped the source will happily emit a claim saying it did not. AO-1 and AO-2 do not name this and it is the deepest problem in the entire program.

Partial mitigation: make claims *verifiable* rather than trusted. Bind exact revisions (Spec 028 §18) and check that cited constraint IDs actually exist in the cited source at the cited revision. That catches fabricated citation. It does not catch read-but-not-comprehended, and nothing does. KA-R08 already says a receipt is evidence of traversal and decision state, not proof of semantic understanding. The control plane must inherit that honesty explicitly and must never let a `PASS` be read as comprehension.

**2. Predicate set hardening into a required-read list.** Every miss adds a predicate; nothing ever removes one; eventually every event activates forty sources and the gate becomes a ritual that is either skipped or drowns the context. This is AO-F03 and it is precisely the failure mode of the current "Minimum reading for continuation" list that AB-024 already diagnoses — a static enumeration whose existence does not prove traversal.

Mitigation: predicates carry measured cost and precision in the ledger. A predicate that fires often and is never cited in the resulting output is evidence for retirement, and there must be a scheduled retirement pass, not only an addition pass. AO-2 has no such mechanism and I consider that a real omission.

**3. The control plane becomes the thing that must be remembered.** The system built to eliminate owner-reminder dependency introduces a component the owner must remember to invoke. AB-023 already names this recursion.

Mitigation: never create a new discipline. Attach to the interaction-entry read and the existing fail-closed aggregate integrity gate. If the design ever requires the owner to type a command to get the safety property, it has failed on its own terms.

### 4.4 Three highest-value simplifications

1. **Delete the mandatory multi-stage loop.** Two gates; everything else advisory and unordered. Removes nine silent-skip sites and most of the per-message cost.
2. **Delete the separate interaction envelope.** Three fields on the ledger replace a twelve-field schema.
3. **Make the evolution register generated, not authored.** AB-027's target should be a derived view over source-declared `risk_or_reopen_triggers`, not a new authored surface. An authored register is a second place to forget to update — the identical failure to the one it exists to prevent.

Honorable mention: generate `REVIEW_INBOX.md`. Nearly free, removes an authored surface, closes a drift risk MC-0003 already identified.

### 4.5 Anything in AO-1/AO-2 over-scoped or missing

**Over-scoped:**

- **AO-R1 as a gating responsibility.** Event interpretation at the head of the chain makes AO-F01 catastrophic. It should be advisory; safety should read output shape.
- **Eighteen failure classes.** More than the evidence supports. AO-F02 and AO-F18 are the same mechanism at different detection points. AO-F12 is AO-F02 restricted to trigger-bearing sources. AO-F13 and AO-F14 are both "declared ≠ realized" at different layers. I would argue for roughly eight classes with sub-labels. Eighteen classes will fragment the regression suite into eighteen thin tests, and thin tests on a small corpus are how a program convinces itself it is qualified.
- **AO-R4 bundling Git lifecycle** with process/workstream/recovery. AB-032 is P2 and separable; folding it into a P0 responsibility inflates the minimum architecture.
- **Thirty-one capability rows treated as a design input.** AO-2 §1 already recognizes the danger and collapses to eight. I would go further: the eight responsibilities are a good *checklist* and a poor *decomposition*, and AO-3 should be evaluated on whether it closes the corpus, not on whether it has a component per responsibility.

**Missing:**

- **Claim verifiability / self-report trust.** AO-2 §7 lists what must be inspectable but never asks who inspects it or against what. This is the single most important omission.
- **Predicate lifecycle and retirement.** Only addition is modeled. Over long horizons, retirement is the dominant maintenance question.
- **Negative controls.** Eighteen failure classes and no statement of where the system should be expected *not* to act. Without that, the qualification cannot distinguish a working control plane from a verbose one.
- **The cost-asymmetry policy.** Response classes exist per failure, but the architecture never states that operational-runbook classes should prefer false activation over missed activation while exploratory classes should prefer the reverse. That is an architecture-level policy, not a per-case judgment.
- **Override semantics.** Nothing says what happens when the owner disagrees with a gate. Override must be explicit, recorded, and treated as calibration evidence.
- **The AO-F18 detection rule.** AO-2 §9 makes owner-reminder dependency first-class, which is exactly right, but leaves it as a description. Without a mechanical definition it remains owner-caught, which is the thing it is trying to stop being.

### 4.6 What would falsify the preferred architecture

```text
F1  A historical regression run where claim + gate checking does not improve
    activation on the corpus replays relative to a strong planner-only baseline.
    This is the decisive comparison and AO-9 should run it explicitly.
    If the planner alone closes the corpus, G-IN is unearned complexity.

F2  Measured claim fabrication at a material rate even with revision binding —
    models citing real constraint IDs from sources they did not use.
    That collapses the self-report basis and forces an independent verifier,
    which changes the cost structure enough to reopen the whole design.

F3  Per-interaction overhead above KA-R30/R31 budgets on ordinary
    BROAD_CONTINUATION work.

F4  Predicate precision below a preregistered threshold — gates fire, activated
    sources are never used in the resulting output. That would indicate
    predicates over output shape are the wrong abstraction.

F5  G-OUT NO_CONTRACT_AVAILABLE dominating in practice, meaning structured
    contract coverage is too thin for the fidelity gate to be real.

F6  Evidence that the bridge's veto-only restriction makes it useless in
    practice — that the owner-reminder dependency is overwhelmingly on the
    suggestive side rather than the omission side. That would argue for an
    earlier generative role and against my §I position.
```

F1 and F2 are the ones I would run first. F6 is the one most likely to be true and that I am least able to assess from the base.

### 4.7 Successor control before W8 — exact authority relationship

Yes. Advisory and veto, never generative. Stated formally:

```text
INPUT AUTHORITY        current continuity architecture, unchanged
SEMANTIC AUTHORITY     current continuity architecture, unchanged
BRIDGE OUTPUT TYPES    claim | verdict | obligation | suggestion   (closed set)
BRIDGE MAY             refuse, compute, cite, suggest
BRIDGE MAY NOT         generate content, resolve conflict, assert fact,
                       write any surface current authority consumes
MUTATION AUTHORITY     unchanged; governed case by case
OVERRIDE               explicit, owner-held, recorded as evidence
DEGRADED MODE          bridge down == status quo ante; never a blocker
FAILURE OF THE ABOVE   AO-F17 BRIDGE_AUTHORITY_LEAK, fail closed
```

Spec 028 §43's `CURRENT_OPERATIONAL_AUTHORITY` and `AUTHORITY_SWITCH_ALLOWED=false` are untouched by anything above.

### 4.8 Minimal historical regression suite before implementation

Real cases, from the corpus and the source evidence. Not constructed.

```text
R1  KF-SD-01  chatgpt-17 restart order
              authority activation AND G-OUT ordering fidelity
              the only case exercising both gates

R2  KF-SD-03  chatgpt-23 collaboration-process activation
              obligation computed without owner reminder

R3  Chat 27   AB-027 / AB-031 activation on an architecture-concern event

R4  Chat 28   stage-evidence continuation depth, no owner path hints

R5  KF-AS-01  Cockpit fidelity — exact source vs semantic summary
              contract fidelity under compression

R6  KF-CR-01  abnormal interruption — intended vs durably completed

R7  AO-F14 retrospective: would the obligation join have flagged
    Spec 028 §26/§32 as unrealized at W0 acceptance?
    Cheapest high-value test in the suite; runs on real historical data.

R8  KF-KR-01  latent trigger rediscovery — trigger activates before the
              owner independently notices the symptom

NEGATIVE CONTROLS — mandatory, not optional

N1  ordinary low-consequence question; no gate should fire; measure added cost
N2  explicit owner override of a fired gate; recorded, respected, not re-fired
N3  a question that could be misread as a change request; mutation must not
    proceed on inferred intent
```

Without N1-N3 the suite measures verbosity, not control. I would treat a suite without negative controls as disqualifying.

I would also preregister thresholds before AO-9 runs, per the corpus §15 freeze discipline: the tested collaborator receives only the task/reconstruction surface for its scenario, never the evaluator corpus, and constructed variants must name their parent case and avoid implying the remedy.

### 4.9 Requirement / specification / backlog items to amend before implementation

**Requirements V0.2 — material gap found.** Requirements V0.2 is the acceptance boundary re-validated at W7 (Spec 028 §42). A capability that is not a requirement will not be qualified. Two capabilities the AO program treats as central are absent:

```text
PROPOSED (recommendation only; V0.2 is frozen and this thread cannot amend it)

KA-R51  control-plane self-evidence
        The architecture must record its own activation/routing/conformance
        outcomes in inspectable form sufficient to detect that correct behavior
        depended on a human reminder, and must not rely on the human noticing
        the pattern.
        Nearest existing: KA-R08 (receipts), KA-R34 (saturation observability).
        Neither covers control-behavior misses.

KA-R52  obligation-to-realization traceability
        An accepted MUST-level obligation must be traceable to an implementation
        gate, implementation evidence and operational activation, or to an
        explicit recorded deferral.
        Nearest existing: none. AO-2 §12 identifies this as a control concern
        precisely because Research 219's opening list omitted it — but it is
        also absent from the frozen requirements, which is the more consequential
        omission.

KA-R53  explicit override recording  (weaker; I would accept deferral)
        Where the architecture computes a mandatory obligation and a human
        overrides it, the override and its reason must be preserved as evidence.
```

**Specification 028 — no amendment required now, with one precise caveat.** §26 and §32 already MUST the reconstruction planner and the three missing CLI surfaces. AO-1 §7.1 is correct that this is a scheduling gap, not a failed gate, and the remedy is a prospective gate schedule rather than a spec change. So nothing blocks AO-9 or design work.

The caveat: §5 enumerates the project-knowledge roots creatable without another specification revision, and a persistent control ledger is not among them. §5 explicitly states that a new repository data store or second authoritative registry requires an explicit later decision. Therefore:

```text
design + historical regression (AO-9)     no amendment needed
implementing a persistent ledger artifact  requires an explicit §5 decision
                                           or an equivalent authority-class
                                           argument that it is a derived view
```

I would rather flag this precisely than either overclaim an amendment need now or discover the constraint during implementation.

**Backlog:**

```text
AB-027  amend framing: the deliverable should be a GENERATED view over
        source-declared triggers, not an authored register. As currently
        worded it risks creating the failure it exists to prevent.

AB-032  explicitly de-scope from the control-plane critical path.
        Warnings only; P2; before W6 as already stated.

AB-031  narrow. Its "candidate intent-to-process architecture" reproduces the
        long mandatory pipeline. Its §Non-decision boundary is already correct
        in refusing to select a router schema; I would additionally record that
        output-shape gating is a live alternative to intent-first routing.

AB-022/AB-024  record that G-OUT, not reconstruction depth, is the mechanism
        that closes the restart-order class. AB-022's acceptance direction
        currently ends at "collaborator reads that authority before giving exact
        operational steps," which the chatgpt-17 evidence shows is necessary
        but not sufficient.
```

**Deferred items I would leave untouched:** AB-003, AB-004, AB-006, AB-007, AB-011, AB-013, AB-014, AB-015. Nothing in my design needs them, and AO-1 §13 and §24 are right that promoting optional conveniences into correctness requirements would be a serious scope error.

## 5. What I am least confident about

Stated plainly, for the comparative phase:

1. Whether G-IN survives contact with a properly implemented reconstruction planner, or collapses into its receipt. F1 decides this and I would accept the collapse.
2. Whether veto-only is too weak to matter during the migration (F6). I cannot assess the balance of suggestive versus omissive owner reminders from the base evidence.
3. Whether the predicate vocabulary is expressible tightly enough to stay deterministic while covering the semantic triggers the corpus actually contains. This is the part of the design most likely to be wrong in detail.
4. The two lines in §M flagged as resting on AO-1's reconstruction rather than direct inspection of the production tree.

## 6. Boundary

```text
MC0021=OPEN
PHASE=CLAUDE_INDEPENDENT_CONTROL_PLANE_ARCHITECTURE
MESSAGE=001
INDEPENDENT_BASE=b649c1a846d3bf9274fd718e0efd8de9d63bd990
CANDIDATE_TARGET_NOT_INSPECTED=f73239ee486132a94701de80514ffd11480b9ecd
PREFERRED_ARCHITECTURE=CP-CLAIM-GATE
MANDATORY_GATES=2
NEW_PERSISTENT_ARTIFACTS=1_LEDGER_PLUS_DERIVED_VIEWS
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
RESEARCH218=NOT_REOPENED
SPECIFICATION_028=NOT_AMENDED
NEXT=CHATGPT_MESSAGE_002_COMPARISON_EXPOSURE
```

```text
INDEPENDENT_CONTROL_PLANE_REVIEW_CONTAMINATED: NO
PREFERRED_ARCHITECTURE_READY_FOR_COMPARISON: YES
SUCCESSOR_CONTROL_BEFORE_W8: YES
CURRENT_AUTHORITY_MUST_REMAIN_SOLE_SEMANTIC_AUTHORITY: YES
MATERIAL_REQUIREMENTS_GAP_FOUND: YES
MATERIAL_SPECIFICATION_028_AMENDMENT_REQUIRED_NOW: NO
```
