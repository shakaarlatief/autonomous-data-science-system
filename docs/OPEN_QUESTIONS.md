# Open Questions

**Status:** Current canonical unresolved-question register  
**Last reconciled:** 2026-08-23  
**Reconciliation context:** Prototype V0 is complete. The post-V0 V1 object/methodological foundations, Project Cockpit interaction architecture, governed reusable-knowledge persistence/interchange, initial runtime selection, retrieval/Horizon chain, deterministic selective-context seam, and first real-model context-value result are established through Specification 014 v1.0 / Checkpoint 146. Specification 015 v0.1 / Checkpoint 150 adds a preserved failed first recommendation/action-value experiment. Specification 016 / Checkpoint 155 provides a completed positive construct-validity result for a stronger dependency-backed `DEFER` versus `NOT_NOW` distinction on deliberately unambiguous microstates. Specification 017 / Checkpoint 156 now freezes the next GENERIC-versus-SELECTIVE-versus-FULL_HORIZON recommendation/action-value experiment under that stronger relation-backed construction. Provider-free implementation is active; no Specification 017 live provider call has occurred. The immediate unresolved downstream question is whether SELECTIVE methodological context adds measurable recommendation/action value beyond a strong GENERIC reasoner once sequencing truth is structurally defensible.

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

Foundation 018 establishes Objects, Relations, Events, and Views plus a candidate project object model. The first V1 persistence slice implements only a bounded subset; the complete production schema remains open. Specification 016 adds evidence that sequencing becomes more objectively testable when an exact activating dependency/trigger relation is represented. Specification 017 now tests that relation-backed structure prospectively inside a recommendation/action result, but still stops before authoritative persistence or mutation.

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

**Status:** Substantially advanced through real reasoning; downstream recommendation value is the active Specification 017 empirical boundary

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

Specification 015 then tested a recommendation/action layer. It failed one exact-disposition gate, but the miss was shared by all three conditions and concentrated on `DEFER` versus `NOT_NOW`. Specification 016 isolated that construct and achieved `1.000000` exact disposition accuracy, `1.000000` exact DEFER trigger-pointer accuracy, and `1.000000` NOT_NOW null-pointer correctness across 36 live observations when the activating dependency was explicit.

Specification 017 is now preregistered to test the remaining system-value question. It freezes the same three conditions, the already-accepted selective sets, new prospectively relation-backed action truth, deterministic action/pointer metrics, and a condition-blinded semantic judge. Its advancement outcomes explicitly distinguish a promoted value signal from a safe ceiling/tie result:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Still open until Specification 017 is executed:

```text
whether SELECTIVE improves downstream recommendation/action behavior over GENERIC
whether FULL_HORIZON causes more unnecessary expansion than SELECTIVE
whether semantic quality or exact action calibration shows a preregistered positive value signal
```

Broader open questions remain:

```text
natural-language/project-state task interpretation
harder and heterogeneous project tasks
when richer semantic/LLM relevance is necessary
open-world discovery of concerns absent from explicit knowledge
final context-budget policy
how accepted reasoning becomes authoritative recommendation/action state
```

### Q-006. How should relevant investigations be activated?

**Status:** Retrieval/Horizon/selective-context mechanics validated; relation-backed sequencing construct supported; Specification 017 prospectively tests downstream action calibration; production activation remains open

P0's path-sensitive tag-trigger activation should not scale unchanged. Foundation 019 instead uses staged retrieval, applicability/context checks, bounded relevance selection, recommendation reasoning, and selective reasoning context.

Specification 016 supports one structural constraint for future activation: if a DEFER-like state is to be distinguished deterministically from NOT_NOW, it should be backed by an explicit activating dependency/trigger rather than a bare low-priority label.

Specification 017 now freezes this prospectively for all expected-DEFER actions. Every action decision includes `defer_until_id`; DEFER requires an exact supplied unresolved activating trigger, while `BLOCKING_REQUIRED`, `RECOMMENDED`, and `NOT_NOW` require a null pointer. The experiment still stops before creating `Proposal`, `Question`, `Investigation`, or other authoritative project objects.

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

**Status:** Structurally advanced through real reasoning; relation-backed sequencing supported; Specification 017 tests a bounded recommendation result but authoritative state mapping remains open

The executable path has bounded evidence through real model reasoning:

```text
project-relevant retrieval
    -> bounded explained MethodologicalHorizon
    -> explicit applicability/context checks
    -> explicit reasoning-function task profile
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured reasoning output
```

Checkpoint 146 shows selective context preserving all frozen reasoning obligations while reducing provider input tokens by about two thirds. Checkpoint 150 shows the first downstream recommendation/action benchmark failing one shared disposition gate. Checkpoint 155 shows the stronger dependency-backed distinction is operationally separable on deliberately unambiguous cases.

Specification 017 is the next bounded step: test whether that relation-backed recommendation result can be safe and add value. It explicitly prohibits authoritative project mutation, so even a future promotion outcome would still require a separate design for mapping accepted recommendation outputs into Foundation 018 objects, relations, and events.

Still unresolved:

```text
how production project objects/state derive requested reasoning functions
whether explicit task semantics remain expressive enough at larger scale
how semantic/LLM relevance participates when they are not
whether DEFER/NOT_NOW should both exist as production enums
how exact activating dependencies should be represented durably
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

Specifications 015 and 016 did not expose a retrieval deficiency. Specification 017 therefore keeps the accepted retrieval, Horizon, and selector mechanics fixed so downstream recommendation/action value can be attributed more cleanly.

Still open:

```text
production task-profile derivation
final Horizon/context budgets
larger and heterogeneous Horizon behavior
whether semantic/LLM relevance is needed beyond explicit reasoning functions
production semantic/fusion integration only when a downstream deficiency requires it
reranking only if ordering becomes a measured problem
```

### Q-045. How should recommendation and reasoning quality be evaluated separately from knowledge coverage?

**Status:** Reasoning-quality separation validated; disposition construct validity supported; Specification 017 now freezes the second recommendation-value comparison

The executable failure decomposition distinguishes catalog, retrieval, applicability, relation-expansion, relevance/budget, context-selection, reasoner-obligation, recommendation-calibration, disposition-construct, pointer, clarification, and action-expansion failures.

Specification 014 established:

```text
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
critical regressions    none
aggregate input ratio   0.334379
```

Specification 015 added deterministic recommendation metrics and a blinded semantic judge, but `RA-G05` failed because `RA-02` exact disposition accuracy was `0.666667` rather than at least `0.80`. The discrepancy was shared across conditions and semantically judged strong, which motivated Specification 016 rather than post-hoc relabeling.

Specification 016 then observed:

```text
aggregate exact disposition accuracy    1.000000
all 12 variants                          3 / 3 correct
all 6 pair sides                         3 / 3 correct
expected-DEFER exact pointer accuracy    1.000000
expected-NOT_NOW null-pointer accuracy   1.000000
outcome                                  DISPOSITION_BOUNDARY_SUPPORTED
```

Specification 017 now freezes a stronger evaluation contract. Deterministic metrics include exact disposition, critical omissions, under/over-recommendation, unnecessary cost, blocking-scope errors, clarification errors, defer-pointer errors, and basis provenance. The blinded judge evaluates methodological rationale separately. Positive value signals are preregistered, including exact or semantic improvement versus GENERIC and lower expansion burden versus FULL_HORIZON.

The active evaluation question is:

```text
Can SELECTIVE pass all absolute and non-inferiority gates?
Does it show at least one preregistered downstream value signal?
Or does a strong GENERIC reasoner remain equally good, yielding SAFE_BUT_NOT_DIFFERENTIATED?
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

**Status:** Open; runtime boundary selected, bounded model treatment reused for Specifications 014-017

D-032 selects runtime infrastructure, not the final LLM provider/model. Specifications 014, 015, and 016 deliberately used the same concrete frozen model/runtime treatment. Specification 017 freezes the same treatment again to preserve attribution while changing the recommendation construct. None of these experiments promotes the concrete model/provider configuration into a permanent production choice.

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

The project uses canonical documents, foundations, research memos, specifications, checkpoints, experiment ledgers, a knowledge map, major-changes ledger, Git history, and explicit continuity/promotion/reconciliation procedures. Specifications 015-017 demonstrate why failed experiments, diagnostic follow-ups, and new prospectively corrected contracts must remain separately versioned rather than editing historical evaluator truth in place.

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

V0 completed a preregistered held-out falsification experiment. V1 now includes product/human evaluation, retrieval/Horizon benchmarks, runtime bakeoffs, cross-platform gates, accessibility checks, selective-context construction, a passed real reasoning-context-value comparison, a preserved failed recommendation/action experiment, a completed positive construct-validity diagnostic derived from that failure, and a separately frozen second recommendation/action-value contract. The progression reinforces that workflow success is distinct from experiment success, historical evaluator truth is immutable, failure attribution should precede redesign, and a new claim requires a new preregistered contract.

### Q-017. How should real projects become regression tests?

**Status:** Substantially advanced conceptually

Foundation 017 proposes project replay from original starting inputs. Long-term privacy-safe extraction, diversity, benchmark maintenance, and comparison criteria remain open.

### Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

Foundation 019 provides candidate dimensions including validity importance, information gain, downstream impact, uncertainty reduction, risk, cost, redundancy, project intent, and human preference. No final ranking/scoring mechanism exists. Specification 016 shows that explicit dependency-backed sequencing can make one distinction reproducibly classifiable. Specification 017 now tests whether such structure plus selective methodology improves bounded action calibration, but still does not define the production prioritization model.

### Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Prototype V0 completed; broader program open

The V0 synthetic churn benchmark and held-out protocol are historical evidence. V1 has added retrieval/Horizon/context/runtime gates, a passed real-model reasoning-context comparison, a failed recommendation/action benchmark, a successful construct-validity diagnostic derived from that narrow failure, and a prospectively relation-backed second recommendation benchmark frozen before implementation. This is the intended pattern: preserve failures, isolate ambiguous constructs, then retest the system-level claim under a new contract rather than retroactively repairing the old result. Larger changing project trajectories and heterogeneous real-project replay remain open.

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
Q-005  does Specification 017 show downstream recommendation/action value from SELECTIVE beyond a strong GENERIC reasoner?
Q-045  can the frozen relation-backed evaluator cleanly separate action quality, pointer validity, semantic rationale, and expansion burden?
Q-006  should production sequencing remain a disposition, become an explicit dependency relation, or expose both as object/relation plus derived view?
Q-037  how should future accepted recommendations become durable project state without over-automation?
Q-029  how should real recommendation priority and sequencing scale beyond bounded benchmark microstates?
Q-021  what model/provider configuration should eventually be selected beyond bounded experiment treatments?
Q-051  which frontend/chart choices deserve final stack promotion?
Q-052  how should final Cockpit visual/system details evolve on top of Specification 008?
```

The active frozen experiment is governed by:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
```

Specifications 015 and 016 remain immutable historical evidence. No Specification 017 live model call may occur until its provider-free implementation is complete, the exact implementation head passes ordinary Ubuntu and Windows CI, and that pre-live boundary is preserved in a later checkpoint. After live execution, the complete raw artifact must be preserved before interpretation or design changes.
