# Open Questions

**Status:** Current canonical unresolved-question register  
**Last reconciled:** 2026-08-23  
**Reconciliation context:** Prototype V0 is complete. The post-V0 V1 object/methodological foundations, Project Cockpit interaction architecture, governed reusable-knowledge persistence/interchange, initial runtime selection, retrieval/Horizon chain, deterministic selective-context seam, and first real-model context-value result are established through Specification 014 v1.0 / Checkpoint 146. Specification 015 v0.1 / Checkpoint 150 adds a preserved failed first recommendation/action-value experiment. Specification 016 / Checkpoint 155 now provides a completed positive construct-validity result for a stronger dependency-backed `DEFER` versus `NOT_NOW` distinction on deliberately unambiguous microstates. The immediate unresolved downstream question is no longer whether that boundary can be represented at all, but whether a newly preregistered recommendation/action-value experiment using that explicit relation-backed construction demonstrates value from SELECTIVE methodological context beyond a strong GENERIC reasoner.

This document records important unresolved questions in current canonical form. Detailed reasoning belongs in foundations, research memos, specifications, checkpoints, experiment records, and Git history.

Existing identifiers are retained for continuity even when a question has been substantially reframed or partly answered. `Substantially answered` means a current governing direction exists while implementation, evaluation, or final-scope questions remain.

---

## System purpose, authority, and project constitution

### Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The purpose is project-relative: create the best defensible data-science process for the project's goals, constraints, deliverables, risk, and desired human involvement while preserving non-negotiable methodological integrity. Still open: system-level success criteria across heterogeneous project classes and how reliability, coverage, human-navigation burden, efficiency, reproducibility, and product usability should be combined.

### Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed, still open

Autonomy should vary with project intent, risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state rather than being one global mode. The final proposal/approval/automatic-action/escalation policy remains open.

### Q-003. What should the human's role be?

**Status:** Substantially refined, still open

Foundation 013 keeps the human concentrated on goals, semantics, consequential trade-offs, authoritative domain input, critique, approvals, and intervention where judgment adds value. Exact escalation and project-configurable control remain open.

### Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not finalized

Current epistemic core: semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity, preceded by admissibility and followed by risk-sensitive assurance. Exact operationalization across project classes remains open.

### Q-028. How should project intent be represented?

**Status:** Substantially refined, not finalized

Objectives, constraints, deliverables, human-control preferences, definitions, and project/model/operational distinctions remain the leading structure. Final schema and interaction model remain open.

### Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under broader validation

Prototype V0 and later V1 evidence remain compatible with them, but broader project diversity may expose missing distinctions or needed revision.

### Q-031. What belongs in the admissibility layer?

**Status:** Open at production depth

Legal, ethical, privacy, policy, safety, organizational, and explicit user constraints are conceptually distinct from methodological validity. Exact scope, representation, and authority remain unresolved.

### Q-032. How should risk-sensitive assurance be represented?

**Status:** Open at production depth

A practical model is still needed to link consequence/risk to verification, replication, robustness, subgroup analysis, human approval, monitoring, and documentation requirements.

### Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Open, coupled to Q-002/Q-008/Q-031/Q-032

The product/object model provides places for Constraints, Questions, Findings, Decisions, events, and approvals, but the complete policy/state representation remains unspecified.

---

## Project objects, state, evidence, and revision

### Q-008. How should project state be represented?

**Status:** Substantially advanced, not complete

Foundation 018 establishes Objects, Relations, Events, and Views plus a candidate project object model. The first V1 persistence slice implements only a bounded subset; the complete production schema remains open. Specification 016 adds evidence that a sequencing state becomes more objectively testable when an exact activating dependency/trigger relation is represented, but it does not yet define the production relation schema.

### Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

Candidate triggers include high risk, epistemic single points of failure, weak high-leverage assumptions, fragile consequential claims, governance requirements, and low-maturity knowledge. Operational policy remains open.

### Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Evidence sufficiency remains decision-specific and may depend on validity, uncertainty, independence, shared ancestry, risk, cost, and the probability that additional evidence changes the decision.

### Q-012. How should uncertainty and confidence be represented?

**Status:** Open

No final numerical, categorical, narrative, or structural representation is selected.

### Q-019. How should invalidation and repair work?

**Status:** Reframed after V0

P0's generic dependency reopening/support-reassessment machinery did not earn its cost as a general always-on architecture. The need remains for selective evidence-driven staleness/invalidation and targeted repair when assumptions or evidence change.

### Q-033. Should analytical Questions and Claims be primary state objects?

**Status:** Strongly supported conceptually, not frozen as universal orchestration law

Foundation 018 treats Questions, Findings, Claims, Evidence, and Decisions as central project objects, without claiming every workflow reduces to one Question/Claim state machine.

### Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

General completion should be obligation/question/deliverable driven and consider residual uncertainty, expected value of additional work, risk, and resource limits.

---

## Reusable methodological knowledge and methodological navigation

### Q-004. How should data-science knowledge be represented?

**Status:** Substantially answered at conceptual/V1 architecture level

Foundation 020 governs `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, collections, provenance/governance, retrieval/applicability/context structures, exact revisions, and separation from execution capability. Final taxonomies, authoring UX, full schema coverage, provenance ontology, and large-scale behavior remain open.

### Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially advanced through real reasoning; downstream recommendation value remains unresolved and is now the next empirical boundary

Accepted bounded path:

```text
large reusable knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded task-specific relevance selection
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> flexible LLM reasoning
```

Specification 014 v1.0 / Checkpoint 146 provide direct downstream evidence: SELECTIVE and FULL_HORIZON both achieved `1.000000` aggregate semantic quality while SELECTIVE used an aggregate input-token ratio of `0.334379`, a `66.56%` reduction, with no critical-obligation regressions.

Specification 015 then tested a further recommendation/action layer. It failed one exact-disposition gate, but the miss was shared by all three conditions and concentrated on `DEFER` versus `NOT_NOW`. Specification 016 subsequently isolated that semantic boundary and achieved `1.000000` exact disposition accuracy, `1.000000` exact DEFER trigger-pointer accuracy, and `1.000000` NOT_NOW null-pointer correctness across 36 live observations when the activating dependency relation was made explicit.

Therefore the selective reasoning-context seam remains supported, the immediate disposition construct problem is substantially narrowed, and the unresolved question returns to downstream system value: does SELECTIVE methodological knowledge materially improve recommendation/action behavior over a strong GENERIC reasoner once evaluator truth is made structurally defensible?

Still open:

```text
natural-language/project-state task interpretation
harder and heterogeneous project tasks
when richer semantic/LLM relevance is necessary
open-world discovery of concerns absent from explicit knowledge
final context-budget policy
how accepted reasoning becomes recommendation/action state
whether explicit methodological knowledge adds downstream recommendation value
```

### Q-006. How should relevant investigations be activated?

**Status:** Retrieval/Horizon/selective-context mechanics validated; relation-backed sequencing construct supported; production activation semantics remain open

P0's path-sensitive tag-trigger activation should not scale unchanged. Foundation 019 instead uses staged retrieval, applicability/context checks, bounded relevance selection, recommendation reasoning, and selective reasoning context.

Specification 015 exposed an ambiguous `DEFER` versus `NOT_NOW` distinction before activation could become durable project mutation. Specification 016 made that distinction structural and the frozen live diagnostic passed all hard gates:

```text
DEFER
    action already justified in the represented plan
    + exact unresolved supplied activating trigger
    + action becomes current next work after that trigger
    + exact defer_until_id

NOT_NOW
    current state/objective does not materially justify prioritizing the action
    + no represented supplied trigger activates it as current next work
    + null defer_until_id
```

Observed Specification 016 result:

```text
36 / 36 exact disposition classifications correct
18 / 18 DEFER pointers exact
18 / 18 NOT_NOW pointers null
```

This supports one design/evaluation constraint for future activation work: a DEFER-like sequencing state should not be treated as a bare low-priority label if deterministic distinction from NOT_NOW is expected. It should be backed by an explicit activating dependency/trigger relation.

Still open:

```text
project state -> current task/reasoning-function profile
open-world concern/action discovery
relevant concern -> recommendation strength
recommendation -> durable Question / Proposal / Investigation
human approval / automatic-action policy
production REQUIRED/BLOCKING semantics and scope
whether DEFER and NOT_NOW remain production enums or become derived views over explicit dependency relations
```

### Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially answered conceptually, taxonomy still open

Foundation 020 separates stable asset/revision identity, components, narrative facets, intrinsic kinds, reasoning functions, static relations, conditional rules, retrieval, applicability, context requirements, semantic checks, provenance, scope, and governance. Exact production enums and authoring conventions remain intentionally unfrozen.

### Q-018. How should knowledge packages interact?

**Status:** Substantially refined, not resolved at scale

Current architecture uses stable identities, typed semantic relations, conditional rules, reusable concepts, components, and collections rather than one giant package graph. Large-scale deduplication, cycles, conflicting soft guidance, and composition quality remain open.

### Q-022. How should external knowledge and source material be integrated?

**Status:** Substantially advanced, not complete

Specification 004 and D-031 establish deterministic interchange and governance safety. Still open: ingestion/review workflows for heterogeneous external sources and full provenance/source persistence.

### Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined, not finalized

Knowledge role, maturity, enforcement authority, scope confidence, provenance, challenge history, and operational coverage should remain distinct. Final production promotion/review/freshness lifecycle remains open.

### Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Structurally advanced through real reasoning; relation-backed sequencing is supported experimentally, but recommendation-state mapping remains open

The first executable path has bounded evidence through real model reasoning:

```text
project-relevant retrieval
    -> bounded explained MethodologicalHorizon
    -> explicit applicability/context checks
    -> explicit reasoning-function task profile
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured reasoning output
```

Checkpoint 146 shows that selective context preserved all frozen reasoning obligations while reducing provider input tokens by about two thirds on the first real-model benchmark.

Checkpoint 150 shows that the first downstream recommendation/action benchmark did not earn promotion. Its only hard-gate failure was a shared `DEFER`/`NOT_NOW` distinction, not a treatment-specific methodological omission.

Checkpoint 155 now shows that the stronger dependency-backed distinction is operationally separable on deliberately unambiguous live cases. This removes one immediate construct-validity blocker, but it does not yet justify mapping reasoner outputs into authoritative project objects or events.

Still unresolved:

```text
how production project objects/state derive requested reasoning functions
whether explicit task semantics remain expressive enough at larger scale
how semantic/LLM relevance participates when they are not
whether DEFER/NOT_NOW should both exist as production enums
how exact activating dependencies should be represented in Foundation 018 state
how recommendation strength becomes Proposal / Question / Investigation / Decision state
how activation behaves on harder, ambiguous, incomplete, and open-world project states
```

### Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved end to end

Foundation 008, Foundation 020, D-031, and Specification 004 establish scope-aware, revisioned, provenance-aware, candidate-versus-accepted governance principles. Automatic learning/promotion remains deliberately unimplemented.

---

## Retrieval, ranking, context construction, and reasoning quality

### Q-044. How should production retrieval, MethodologicalHorizon construction, and selective context work?

**Status:** Substantially answered for the first bounded chain through real reasoning; production scaling remains open

The initial chain is executable through the first downstream model gate:

```text
lexical retrieval                         Checkpoint 135
dense semantic comparator                 Checkpoint 137
complementary hybrid comparator            Checkpoint 139
explained one-hop/applicability Horizon    Checkpoint 141
selective MethodologicalContextPack        Checkpoint 143
real-model context-value gate              Checkpoint 146
```

The first selective gate reduced methodology-only canonical context by roughly 65% to 84%. The subsequent real-model gate preserved every frozen semantic obligation while reducing actual provider input tokens by `66.56%` in aggregate.

Specification 015 again observed descriptive SELECTIVE/FULL reasoner input-token ratio `0.443880`, but recommendation/action quality was the governing objective and the seam failed. Specification 016 addressed the downstream disposition construct rather than retrieval and therefore gives no evidence that retrieval should now be retuned.

Still open:

```text
production task-profile derivation
final Horizon/context budgets
larger and heterogeneous Horizon behavior
whether semantic/LLM relevance is needed beyond explicit reasoning functions
production semantic/fusion integration when a downstream deficiency requires it
reranking only if ordering becomes a measured problem
```

### Q-045. How should recommendation and reasoning quality be evaluated separately from knowledge coverage?

**Status:** Reasoning-quality separation validated; disposition construct validity supported; recommendation-value comparison remains unresolved

The executable failure decomposition distinguishes catalog, retrieval, applicability, relation-expansion, relevance/budget, context-selection, reasoner-obligation, recommendation-calibration, disposition-construct, and action-expansion failures.

Specification 014 established:

```text
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
critical regressions    none
aggregate input ratio   0.334379
```

Specification 015 added deterministic recommendation metrics and a blinded semantic judge. Frozen aggregate SELECTIVE behavior was strong:

```text
exact disposition accuracy      0.916667
semantic score                  0.991667
critical omissions              0
blocking false negatives        0
unsupported basis               0
under-recommendations           0
over-recommendations            0
unnecessary recommended cost    0
```

but `RA-G05` failed because `RA-02` exact disposition accuracy was `0.666667` rather than at least `0.80`. All three conditions converged on `NOT_NOW` where frozen truth expected `DEFER` for two noncritical expansion actions, while every RA-02 semantic score was `1.000000`.

Specification 016 then isolated the label boundary under explicit relation-backed evidence and observed:

```text
aggregate exact disposition accuracy    1.000000
all 12 variants                          3 / 3 correct
all 6 pair sides                         3 / 3 correct
expected-DEFER exact pointer accuracy    1.000000
expected-NOT_NOW null-pointer accuracy   1.000000
outcome                                  DISPOSITION_BOUNDARY_SUPPORTED
```

The historical Specification 015 cases are not rescored. Instead, both disputed RA-02 expected-DEFER examples are described as not admissible examples of unambiguous Specification 016 DEFER because the old fixture did not encode an exact activating dependency relation.

The next evaluation question is now:

```text
Can a new recommendation/action benchmark preserve this structurally defensible disposition truth?
Does SELECTIVE improve recommendation/action behavior over GENERIC once the disposition construct is no longer the main confound?
Can value be demonstrated on outcomes that matter, such as critical omissions, unjustified blocking, unnecessary actions, or clarification quality, rather than exact labels alone?
```

---

## Agent/runtime, execution, and interoperability

### Q-009. What agent or responsibility structure is useful?

**Status:** Substantially answered for initial V1; specialist/multi-agent structure remains open

D-032 selects a single-principal-reasoner-first runtime shape through an ADS-owned OpenAI Agents SDK adapter. Specialist agents should be introduced only if later evidence demonstrates a meaningful quality, responsibility-separation, durability, or context-efficiency benefit.

### Q-020. What should the execution environment look like?

**Status:** Open at production scale

Foundation 018 establishes shared reproducible run contracts and retains VS Code as the developer workbench. Local/remote/container/GPU/cloud execution remains an abstraction problem rather than a settled backend.

### Q-021. How should model and tool providers be selected?

**Status:** Open; runtime boundary selected, bounded model treatment reused for Specifications 014-016

D-032 selects runtime infrastructure, not the final LLM provider/model. Specifications 014, 015, and 016 deliberately used the same concrete frozen model/runtime treatment so adjacent experiment results remained attributable. The passed context-value gate, failed recommendation/action gate, and passed disposition diagnostic do not promote that treatment into a permanent production choice.

### Q-046. Which agent/runtime infrastructure, if any, should V1 adopt?

**Status:** Answered and closed for the initial V1 runtime selection

D-032 accepts OpenAI Agents SDK behind an ADS-owned `ReasoningRuntime` port with `openai-agents==0.19.4` as the validated starting package. Direct model calls remain the fallback/reference path; LangGraph remains a future durability escalation path.

### Q-047. What role should MCP, AG-UI, and A2A ultimately play?

**Status:** Partially answered, implementation open

Current direction:

```text
MCP     external tool/resource interoperability, not project memory
AG-UI   possible transport adapter around ADS-owned interaction/run events
A2A     defer until independently deployed remote agent systems are real
```

Final production MCP servers/tool catalog, AG-UI adapter choice, and any future A2A integration remain unselected.

---

## Persistence, interchange, and portability

### Q-026. How should repository and preservation structure evolve?

**Status:** Substantially answered for current development needs; still evolvable

The project uses canonical documents, foundations, research memos, specifications, checkpoints, experiment ledgers, a knowledge map, major-changes ledger, Git history, and explicit continuity/promotion/reconciliation procedures. Specifications 015 and 016 together demonstrate why frozen experiment contracts, complete raw result artifacts, positive and negative outcomes, and post-result interpretation should remain separately preservable.

### Q-043. When should the project move beyond Git and Markdown for development knowledge preservation?

**Status:** Open with explicit deferral criteria

Git + Markdown remains sufficient while routing, reconciliation, and consistency are manageable. More advanced infrastructure becomes justified only when retrieval failures, contradictory canonical state, dependency complexity, multiple concurrent writers, or reconciliation cost become material.

### Q-048. When is the governed reusable-knowledge persistence round-trip considered closed?

**Status:** Answered and closed for the current V1 governed seam

Checkpoint 127 records successful governed import/accept/export/pinning validation on SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18. Retrieval quality, Horizon construction, external ingestion, and authoring remain separate questions.

---

## Product interface and Project Cockpit

### Q-049. What should the primary active-work interface be?

**Status:** Substantially answered and promoted for V1 interaction architecture

Specification 008 promotes the Project Cockpit as the V1 primary immersive active-work model, with direct specialist views retained as alternative entry/inspection/record paths.

### Q-050. How should the Cockpit scale to large projects and feel under real spatial interaction?

**Status:** Substantially answered at interaction-architecture level; residual polish/open scale questions remain

The accepted interaction architecture includes 2D navigation/recovery, bounded zoom, native pinch capability, viewport-aware stage orientation, scalable Jump/search, compact/fold-away chrome, collision-safe floating surfaces, fullscreen, keyboard/reduced-motion support, and world-owned ambient depth. Remaining issues include tiny pinch polish, final semantic zoom/grouping, minimap, auto-layout, project-search backend, persistence of navigation state, and broader real-project scale validation.

### Q-051. What frontend stack and visualization system should be promoted?

**Status:** Partially narrowed, not final

React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest remain the leading frontend hypothesis. Formal final stack promotion and ECharts versus Plotly remain open.

### Q-052. What should the final Cockpit visual identity, stage taxonomy, layout, control architecture, and URL contract be?

**Status:** Open by design

Specification 008 is the interaction baseline. Final visual identity, stage taxonomy/widths, semantic zoom, auto-layout, minimap, graph/canvas/gesture library, public route contract, permanent chrome treatment, and canonical screenshot baseline remain intentionally unfrozen.

---

## Evaluation, resource allocation, and stopping

### Q-013. How should analysis depth and resource budgets work?

**Status:** Open; V0 provides strong cost evidence

Optional depth should depend on expected value, uncertainty, risk, project intent, and resource constraints while mandatory validity obligations remain mandatory.

### Q-014. How should the system decide when experimentation can stop?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant residual uncertainty, diminishing information value, unavailable discriminating evidence, or compatible resource limits.

### Q-015. How should project types be characterized?

**Status:** Substantially reframed

Use multidimensional project characterization rather than one exclusive project-type label. Exact representation remains open.

### Q-016. How should system quality itself be evaluated?

**Status:** Substantially advanced; broader V1 evaluation remains open

V0 completed a preregistered held-out falsification experiment. V1 now includes product/human evaluation, retrieval/Horizon benchmarks, runtime bakeoffs, cross-platform gates, accessibility checks, selective-context construction, a passed real reasoning-context-value comparison, a preserved failed recommendation/action experiment, and a completed positive construct-validity diagnostic derived from the exact failure mode. The progression reinforces that workflow execution success must remain distinct from experiment-gate success, narrow failures should be preserved rather than repaired post hoc, and a failed benchmark construct should be isolated before making another system-value claim.

### Q-017. How should real projects become regression tests?

**Status:** Substantially advanced conceptually

Foundation 017 proposes project replay from original starting inputs. Long-term privacy-safe extraction, diversity, benchmark maintenance, and comparison criteria remain open.

### Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

Foundation 019 provides candidate dimensions including validity importance, information gain, downstream impact, uncertainty reduction, risk, cost, redundancy, project intent, and human preference. No final ranking/scoring mechanism exists. Specification 015 showed that a sequencing-oriented label was too weakly grounded in its frozen RA-02 state to support the intended exact-label gate. Specification 016 shows that explicit dependency-backed sequencing can make that distinction reproducibly classifiable, but does not yet determine how real project priorities should be ranked or persisted.

### Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Prototype V0 completed; broader program open

The V0 synthetic churn benchmark and held-out protocol are historical evidence. V1 has added retrieval/Horizon/context/runtime gates, a passed real-model reasoning-context comparison, a failed recommendation/action benchmark, and a successful construct-validity diagnostic derived from that narrow failure. The next recommendation benchmark should preserve this stronger construction discipline while becoming harder on substantive recommendation value rather than merely repeating an easy semantic separation test. Larger changing project trajectories and heterogeneous real-project replay remain open.

---

## Prototype V0 questions retained for provenance

### Q-036. How should a new project be initialized?

**Status:** Narrow V0 mechanism answered; general product initialization remains open

V0 exposed a brief, stale README, datasets, and inherited baseline to test semantic correction. Foundation 017 and Cockpit work provide richer direction, but production initialization remains unimplemented.

### Q-040. What is the minimum end-to-end prototype that can falsify the core architecture?

**Status:** Answered for Prototype V0 and empirically resolved

Prototype V0 was implemented, run, judged, and strongly falsified the current P0 design. Future prototypes require new contracts rather than extending V0 indefinitely.

### Q-041. How should Prototype V0 be represented and implemented concretely?

**Status:** Answered and historical

Foundation 011 and the completed `prototype_v0/` implementation define the frozen historical treatment architecture.

### Q-042. What do real B0/B1 calibration runs show, and what common baseline protocol should be frozen before P0?

**Status:** Answered for Prototype V0

The development calibration and Foundation 012 preregistration are complete historical experiment-design evidence.

---

## Preservation and source integration

### Q-023. Should raw conversations be archived?

**Status:** Open and explicitly deferred

Raw transcripts may provide useful provenance but also contain duplication, sensitive conversational context, and obsolete reasoning. Current continuity must not depend on them.

### Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive

Automatic extraction may assist routing, reconciliation, contradiction detection, or promotion proposals, but automatic extraction must never imply automatic promotion into trusted methodological or project authority.

---

## Current highest-value unresolved questions

The questions most directly attached to active V1 execution are now:

```text
Q-005  does explicit methodological knowledge add downstream recommendation/action value beyond a strong generic reasoner once sequencing truth is structurally defensible?
Q-045  how should the next recommendation benchmark measure substantive value separately from disposition construct validity?
Q-006  should production sequencing remain a disposition, become an explicit dependency relation, or expose both as object/relation plus derived view?
Q-037  how should future accepted recommendations become durable project state without over-automation?
Q-029  how should real recommendation priority and sequencing be represented beyond the deliberately clear Specification 016 microstates?
Q-021  what model/provider configuration should eventually be selected beyond bounded experiment treatments?
Q-051  which frontend/chart choices deserve final stack promotion?
Q-052  how should final Cockpit visual/system details evolve on top of Specification 008?
```

The completed disposition diagnostic is governed and preserved by:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/checkpoints/152_disposition_semantics_failure_attribution_contract_frozen.md
docs/checkpoints/153_disposition_semantics_provider_free_gate_cross_platform_passed.md
docs/checkpoints/154_specification_016_live_boundary_frozen.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
experiments/disposition_semantics/results/spec016-live-20260823-run-32652636943/
```

Specification 015 and its frozen FAIL remain immutable historical evidence. The next live model call may occur only under a separately versioned and preregistered recommendation/action-value experiment that preserves the stronger relation-backed sequencing construction, is provider-free validated first, and does not post hoc alter Specification 015 or Specification 016.
