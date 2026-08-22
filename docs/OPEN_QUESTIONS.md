# Open Questions

**Status:** Current canonical unresolved-question register  
**Last reconciled:** 2026-08-22  
**Reconciliation context:** Prototype V0 complete; post-V0 V1 methodological/object foundations established; Project Cockpit interaction architecture promoted through Specification 008 / Checkpoint 126 with bounded post-promotion normal-window/pinch polish accepted through Checkpoint 130; governed reusable-knowledge persistence/interchange closed across SQLite/Linux, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127; the initial runtime bakeoff is closed through D-032 / Checkpoint 133, selecting OpenAI Agents SDK behind an ADS-owned runtime port; the first production retrieval and MethodologicalHorizon sequence is validated through Checkpoints 135/137/139/141; and the first deterministic RH-C relevance/selective-context gate passed without target or threshold changes and is promoted through Specification 013 v1.0 / Checkpoint 143. The next active methodological boundary is real downstream reasoning quality and model-specific context cost under a preregistered selective-context versus strong full-Horizon/simple-control comparison.

This document records important unresolved questions in current canonical form. Detailed reasoning belongs in foundations, research memos, specifications, checkpoints, experiment records, and Git history.

Existing identifiers are retained for continuity even when a question has been substantially reframed or partly answered. `Substantially answered` means a current governing direction exists while implementation, evaluation, or final-scope questions remain.

---

## System purpose, authority, and project constitution

### Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The primary purpose is project-relative: create the best defensible data-science process for the project's goals, constraints, deliverables, and desired human involvement while preserving non-negotiable methodological integrity. Still open: system-level success criteria across heterogeneous project classes and how reliability, coverage, human-navigation burden, efficiency, reproducibility, and product usability should be combined.

### Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed, still open

Autonomy should vary with project intent, risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state rather than being one global mode. The final proposal/approval/automatic-action/escalation policy remains open.

### Q-003. What should the human's role be?

**Status:** Substantially refined, still open

Foundation 013 establishes the current boundary: the human should concentrate on goals, semantics, consequential trade-offs, authoritative domain input, critique, approvals, and intervention where judgment adds value. Exact escalation and project-configurable control remain open.

### Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not finalized

Current epistemic core: semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity, preceded by admissibility and followed by risk-sensitive assurance. Exact operationalization across project classes remains open.

### Q-028. How should project intent be represented?

**Status:** Substantially refined, not finalized

Objectives, constraints, deliverables, human-control preferences, definitions, and project/model/operational distinctions remain the leading structure. Final schema and interaction model remain open.

### Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under broader validation

Prototype V0 and later design remain compatible with them, but broader project diversity may expose missing distinctions or needed revision.

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

Foundation 018 establishes Objects, Relations, Events, and Views plus a candidate project object model. The first V1 persistence slice implements only a bounded subset; the complete production schema remains open.

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

**Status:** Substantially advanced through selective-context construction; downstream reasoning effect now active

The current direction is selective:

```text
large reusable knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> bounded task-specific relevance selection
    -> selective MethodologicalContextPack
    -> flexible LLM reasoning
```

Validated executable boundaries now include:

```text
production lexical accepted-current retrieval          Checkpoint 135
semantic channel complementarity                       Checkpoints 137-139
one-hop relation expansion                             Checkpoint 141
TRUE/FALSE/UNKNOWN applicability + missing context     Checkpoint 141
deterministic task-profile selective context           Checkpoint 143 / Specification 013 v1.0
```

The first RH-C gate demonstrated exact revision coverage with approximately 65-84% canonical-context reduction on the frozen ten-asset stress corpus while keeping system omission decisions out of the model-facing pack.

What remains unvalidated is the next crucial boundary:

```text
does selective methodological context improve or preserve real reasoning quality
relative to a strong full-Horizon/simple control
under the same concrete model/runtime configuration?
```

Also still open are natural-language/project-state task interpretation, when richer semantic/LLM relevance becomes necessary, and open-world discovery of important concerns absent from the catalog.

### Q-006. How should relevant investigations be activated?

**Status:** Reframed after V0; retrieval/Horizon/selective-context mechanics validated, activation policy still open

P0's path-sensitive tag-trigger activation should not scale unchanged. Foundation 019 instead uses staged retrieval, explicit applicability/context checks, bounded relevance selection, and selective reasoning context.

Current executable evidence covers:

```text
retrieval                           Checkpoint 135
semantic complementarity           Checkpoints 137-139
one-hop relation expansion         Checkpoint 141
applicability / missing context     Checkpoint 141
selective task context              Checkpoint 143
```

Still open are:

```text
how production project state derives the current task profile
how a relevant concern becomes a concrete Question / Proposal / Investigation
recommendation and REQUIRED/BLOCKING transitions
how open-world concerns enter when explicit knowledge is incomplete
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

**Status:** Substantially advanced through the first selective MethodologicalContextPack; task-profile derivation and reasoning impact remain active

Current executable path:

```text
large global knowledge universe
    -> high-recall project-specific retrieval/filtering
    -> bounded explained MethodologicalHorizon
    -> explicit applicability/context checks
    -> explicit task-profile relevance selection
    -> selective task-specific MethodologicalContextPack
```

The first five structural pieces now have executable evidence through Checkpoints 135, 139, 141, and 143.

Still unresolved:

```text
how project objects/state determine requested reasoning functions
whether explicit task semantics are expressive enough at larger scale
how semantic/LLM relevance should participate when they are not
how the selected pack changes real model reasoning quality/cost
how reasoning outputs become recommendation, required concern, or action
```

### Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved end to end

Foundation 008, Foundation 020, D-031, and Specification 004 establish scope-aware, revisioned, provenance-aware, candidate-versus-accepted governance principles. Automatic learning/promotion remains deliberately unimplemented.

---

## Retrieval, ranking, and context construction

### Q-044. How should production retrieval, MethodologicalHorizon construction, and selective context work?

**Status:** Substantially answered through the first accepted selective-context seam; production scaling and task-profile derivation remain open

Research 016 / Specification 009 established the decomposition:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval
RH-R    relational Horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

The first sequence has now been executed end to end through RH-C.

#### Production lexical baseline

Checkpoint 135:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
```

#### Exact dense semantic comparator

Checkpoint 137 preserved an experiment-only FastEmbed/BGE comparator. It recovered the lexical `class-imbalance` miss but lost `ecdf` from the semantic top three, so dense-only did not replace lexical retrieval.

#### Complementary hybrid comparator

Checkpoint 139 / workflow `32561118325`:

```text
Ubuntu PASS
Windows PASS
RH-S Recall@3            1.00
RH-S MRR                 0.875
RH-S critical omissions  0 / 4
RH-L Recall@3            1.00
RH-L MRR                 1.00
```

This supports lexical+dense complementarity on the frozen benchmark without permanently selecting FastEmbed, BGE, RRF `k=60`, vector persistence, ANN, or a vector database.

#### First explained MethodologicalHorizon

Specification 012 v1.0 / Checkpoint 141 validates:

```text
stable/revision-transparent candidates
    -> accepted-current navigation reads
    -> outbound one-hop governed relation expansion
    -> TRUE / FALSE / UNKNOWN applicability
    -> POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    -> explained MethodologicalHorizon
```

#### First selective MethodologicalContextPack

Specification 013 v1.0 / Checkpoint 143 validates:

```text
explicit requested reasoning functions
    -> primary function matches
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets budget
    -> exact accepted-current selected-context reads
    -> ContextSelectionResult
    -> MethodologicalContextPack
```

On the deliberately wide ten-asset Horizon:

```text
RH-C01 ratio 0.20020477
RH-C02 ratio 0.16462054
RH-C03 ratio 0.34635417
RH-C04 ratio 0.28222057
```

Across every case:

```text
required stable-key coverage       1.00
required exact-revision coverage   1.00
irrelevant selected                0
unexplained omissions              0
```

This answers the first bounded RH-C construction question. It does not establish a final production relevance policy.

Still open:

```text
production task-profile derivation
final Horizon/context budgets
behavior on larger and more heterogeneous Horizons
whether semantic/LLM relevance is needed beyond explicit reasoning functions
production semantic-provider/fusion integration when a vertical slice requires it
reranking only if downstream ordering becomes a measured problem
exact provider-token burden under a concrete model
real reasoning quality under selective versus fuller context
```

Primary current evidence:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/research/019_first_methodological_horizon_application_seam.md
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md

docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md

docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md

experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

### Q-045. How should recommendation and reasoning quality be evaluated separately from knowledge coverage?

**Status:** Active V1 question; upstream failure classes plus context-selection omissions are executable

The evaluation decomposition can now distinguish:

```text
knowledge absent from catalog
known but not retrieved
retrieved through lexical and/or semantic channel
retrieved/seeded but INAPPLICABLE
retained but MISSING_CONTEXT
relation-added to the Horizon
Horizon candidate but NO_REASONING_FUNCTION_MATCH
relevant under the explicit policy but BUDGET_LIMIT
selected exact revision sent to reasoning
```

This materially separates coverage, retrieval, applicability, and context-selection failures.

The next missing layer is downstream reasoning/recommendation quality:

```text
selected context but reasoner misses an obligation
omitted context causes a real reasoning failure
full-Horizon context distracts the reasoner
relevant concern is recommended incorrectly or too weakly
required concern is not elevated to REQUIRED/BLOCKING
recommended work is skipped by human/system
human/execution outcome after recommendation
```

The next real reasoning vertical slice should therefore hold task evidence and model configuration fixed while comparing selective context against a strong full-Horizon/simple control. Recommendation correctness must remain separate from retrieval/context recall.

---

## Agent/runtime, execution, and interoperability

### Q-009. What agent or responsibility structure is useful?

**Status:** Substantially answered for initial V1; specialist/multi-agent structure remains open

Knowledge, capabilities, project semantics, and runtime actors remain separate. D-032 selects a single-principal-reasoner-first runtime shape through an ADS-owned OpenAI Agents SDK adapter. Specialist agents should be introduced only if later evidence demonstrates a meaningful benefit in quality, separation of responsibility, durability, or context efficiency. No multi-agent architecture is currently selected.

### Q-020. What should the execution environment look like?

**Status:** Open at production scale

Foundation 018 establishes shared reproducible run contracts for system-triggered and manual execution and retains VS Code as the developer workbench. Local/remote/container/GPU/cloud execution remains an abstraction problem rather than a settled backend.

### Q-021. How should model and tool providers be selected?

**Status:** Open; runtime boundary selected

D-032 selects the initial reasoning-runtime infrastructure, not the final LLM provider or model. The next reasoning vertical slice must choose one concrete model configuration for evaluation without prematurely declaring it the final provider/model. Provider/model choice must remain separate from ADS domain semantics and should preserve deterministic fake-model testing and a replaceable adapter boundary. MCP is the selected direction for external tool/resource interoperability where appropriate, but the production server/tool catalog remains open.

### Q-046. Which agent/runtime infrastructure, if any, should V1 adopt?

**Status:** Answered and closed for the initial V1 runtime selection

Specification 005 was executed rather than resolved from framework documentation alone.

D-032 accepts:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

Direct model calls remain the fallback/reference path. LangGraph remains a future escalation path if stronger long-running workflow durability, checkpoint history/time travel, or independently durable workflow stages become empirically necessary.

This does not select the final provider/model, multi-agent architecture, production runtime-state persistence schema, or production MCP catalog.

### Q-047. What role should MCP, AG-UI, and A2A ultimately play?

**Status:** Partially answered, implementation open

Current direction:

```text
MCP
    external tool/resource interoperability
    compatible with the selected runtime adapter
    not project memory or internal application bus

AG-UI
    possible transport adapter around ADS-owned interaction/run events
    not ADS domain semantics

A2A
    defer until independently deployed remote agent systems are genuinely needed
```

Final production MCP servers/tool catalog, AG-UI adapter choice, and any future A2A integration remain unselected.

---

## Persistence, interchange, and portability

### Q-026. How should repository and preservation structure evolve?

**Status:** Substantially answered for current development needs; still evolvable

The project uses canonical documents, foundations, research memos, specifications, checkpoints, experiment ledgers, a knowledge map, major-changes ledger, Git history, and explicit continuity/promotion/reconciliation procedures. This is development preservation, not the production project-state database.

### Q-043. When should the project move beyond Git and Markdown for development knowledge preservation?

**Status:** Open with explicit deferral criteria

Git + Markdown remains sufficient while routing, reconciliation, and consistency are manageable. More advanced infrastructure becomes justified only when retrieval failures, contradictory canonical state, dependency complexity, multiple concurrent writers, or reconciliation cost become material.

### Q-048. When is the governed reusable-knowledge persistence round-trip considered closed?

**Status:** Answered and closed for the current V1 governed seam

Checkpoint 127 records successful validation on:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

This answer is scoped to the current governed persistence/interchange seam. It does not close retrieval quality, MethodologicalHorizon construction, external ingestion, or knowledge-authoring questions.

---

## Product interface and Project Cockpit

### Q-049. What should the primary active-work interface be?

**Status:** Substantially answered and promoted for V1 interaction architecture

Specification 008 promotes the Project Cockpit as the V1 primary immersive active-work model, with direct specialist views retained as alternative entry/inspection/record paths. This closes the basic interface-direction question for V1 while leaving final visual identity and future capability depth open.

### Q-050. How should the Cockpit scale to large projects and feel under real spatial interaction?

**Status:** Substantially answered and promoted at the interaction-architecture level; latest bounded polish accepted as good enough to continue

Seven real-browser human reviews plus automated cross-platform/browser gates support:

```text
FiniteNavigableGridWorld != SemanticProjectPlane
2D navigation and recovery
bounded geometric zoom
native laptop pinch capability
viewport-aware stage orientation
scalable Jump/search
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen
keyboard/reduced-motion support
world-owned ambient depth
```

Checkpoint 130 records the later bounded normal-window Jump/composer collision repair and faster anchored pinch. The subsequent real-browser/hardware retest accepted the result as good enough to continue. The remaining tiny occasional pinch hitch stays deferred non-blocking polish.

Still open:

```text
remaining tiny pinch hitch polish
final pinch/zoom constants
final semantic zoom/grouping
final minimap decision
final graph/canvas or gesture dependency decision
final auto-layout strategy
production project-search backend
pan/zoom/HUD persistence contract
broader real-project scale validation
```

### Q-051. What frontend stack and visualization system should be promoted?

**Status:** Partially narrowed, not accepted as final architecture

React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest remain the leading frontend hypothesis and have supported the Cockpit evidence. Formal final stack promotion remains open. ECharts versus Plotly remains an empirical comparison. Tauri remains deferred.

### Q-052. What should the final Cockpit visual identity, stage taxonomy, layout, control architecture, and URL contract be?

**Status:** Open by design, no longer a prerequisite for basic interaction promotion

The final visual identity, stage taxonomy/widths, semantic zoom, auto-layout, minimap, graph/canvas/gesture library, public route contract, permanent stage-ruler treatment, permanent tool-rail styling, exact ambient styling, and canonical screenshot baseline remain intentionally unfrozen.

Specification 008 remains the interaction baseline while these product-design questions evolve.

---

## Evaluation, resource allocation, and stopping

### Q-013. How should analysis depth and resource budgets work?

**Status:** Open; V0 and RH-C provide strong cost evidence

V0 demonstrated that explicit machinery can consume more than twice the token budget without material reliability gain. RH-C demonstrated that the model-facing methodological payload can be reduced substantially before model reasoning while preserving frozen required revisions on a small stress corpus. Final context budgets still require model-specific evidence rather than byte-only proxies.

### Q-014. How should the system decide when experimentation can stop?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant residual uncertainty, diminishing information value, unavailable discriminating evidence, or compatible resource limits.

### Q-015. How should project types be characterized?

**Status:** Substantially reframed

Use multidimensional project characterization rather than one exclusive project-type label. Exact representation remains open.

### Q-016. How should system quality itself be evaluated?

**Status:** Substantially advanced; broader V1 evaluation remains open

V0 completed a preregistered held-out falsification experiment. V1 now also has runtime bakeoffs, retrieval/Horizon benchmarks, selective-context gates, cross-platform gates, accessibility checks, and human product review. The next direct reasoning experiment should test whether the selective context machinery earns value at the actual model-reasoning layer.

### Q-017. How should real projects become regression tests?

**Status:** Substantially advanced conceptually

Foundation 017 proposes project replay from original starting inputs. Long-term privacy-safe extraction, diversity, benchmark maintenance, and comparison criteria remain open.

### Q-029. How should analytical and methodological attention be prioritized?

**Status:** Substantially refined; first deterministic task-profile policy validated, broader prioritization remains open

Foundation 019 provides candidate dimensions including validity importance, information gain, downstream impact, uncertainty reduction, risk, cost, redundancy, project intent, and human preference.

Specification 013 v1.0 validates only a narrower policy:

```text
explicit requested reasoning functions
    -> primary matches
    -> required conceptual support
    -> hard budget
```

This is evidence that simple explicit task semantics can compress context on the frozen corpus. It is not a final relevance/ranking model. Still open are multidimensional prioritization, recommendation ranking, required/blocking transitions, task-profile derivation, and when semantic/LLM judgment should enter.

### Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Prototype V0 completed; broader program open

The V0 synthetic churn benchmark and held-out protocol are completed historical evidence. The next evaluation program should broaden to real reasoning under alternative context construction, larger changing project trajectories, human-navigation burden, product usability, and project replay across project families.

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

Foundation 011 and the completed `prototype_v0/` implementation define the frozen historical treatment architecture. It is no longer the active V1 architecture.

### Q-042. What do real B0/B1 calibration runs show, and what common baseline protocol should be frozen before P0?

**Status:** Answered for Prototype V0

The development calibration and Foundation 012 preregistration are complete historical experiment-design evidence.

---

## Preservation and source integration

### Q-023. Should raw conversations be archived?

**Status:** Open and explicitly deferred

Raw transcripts may provide valuable provenance but also contain duplication, sensitive conversational context, and obsolete reasoning. Current continuity must not depend on them.

### Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive

Automatic extraction may assist routing, reconciliation, contradiction detection, or promotion proposals, but automatic extraction must never imply automatic promotion into trusted methodological or project authority.

---

## Current highest-value unresolved questions

The questions most directly attached to active V1 execution are now:

```text
Q-005  test whether the accepted selective MethodologicalContextPack preserves or improves real reasoning versus a strong fuller-context control
Q-045  separate real reasoning/recommendation failures from catalog, retrieval, applicability, and context-selection failures
Q-029  determine when the narrow task-profile selector needs richer prioritization/semantic relevance
Q-021  choose one concrete model configuration for the bounded reasoning experiment without treating it as permanent provider selection
Q-051  determine which frontend/chart choices deserve final stack promotion
Q-052  evolve final Cockpit visual/system details on top of Specification 008
```

Q-046 remains closed for the initial V1 runtime selection through D-032 / Checkpoint 133. Q-048 remains closed through Checkpoint 127. Q-049 and the basic interaction-architecture part of Q-050 are not current blockers because Specification 008 is promoted.

Q-044 has materially advanced: the first bounded chain from retrieval through selective context is now executable. Its remaining uncertainty begins at production task-profile derivation, scaling to richer Horizons, final budgets, and whether more semantic relevance machinery is actually needed. The immediate experiment should therefore test downstream reasoning rather than continue tuning retrieval because it can be tuned.
