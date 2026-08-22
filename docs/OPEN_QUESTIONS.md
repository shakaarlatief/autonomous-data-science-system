# Open Questions

**Status:** Current canonical unresolved-question register  
**Last reconciled:** 2026-08-22  
**Reconciliation context:** Prototype V0 complete; post-V0 V1 methodological/object foundations established; Project Cockpit interaction architecture promoted through Specification 008 / Checkpoint 126 with bounded post-promotion normal-window/pinch polish validated through Checkpoint 130 and accepted as good enough to continue; governed reusable-knowledge persistence/interchange round-trip closed across SQLite/Linux, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127; the initial runtime bakeoff is closed through Specification 005, Checkpoints 129/131/132/133 and D-032, selecting OpenAI Agents SDK behind an ADS-owned runtime port; production retrieval and MethodologicalHorizon work is now evidenced through the lexical baseline at Checkpoint 135, the dense-only comparator at Checkpoint 137, the complementary RRF hybrid comparator at Checkpoint 139, and the first accepted storage-neutral one-hop/applicability-aware MethodologicalHorizon at Specification 012 v1.0 / Checkpoint 141. The next active methodological boundary is relevance/prioritization and RH-C selective-context quality/cost.

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

**Status:** Substantially reframed after V0; active at relevance/selective-context boundary

Current direction is selective: global knowledge is narrowed through retrieval into a bounded explained MethodologicalHorizon; explicit deterministic checks handle accepted-current navigation, reliable prerequisites, hard negatives, and missing context; flexible reasoning should handle semantic relevance, trade-offs, synthesis, and open-world concern discovery only after a bounded context pack is assembled.

Checkpoint 141 now validates the first real Horizon and the distinction `unknown != false`. What remains unvalidated is the crucial next boundary: how relevance/prioritization chooses what belongs in task-specific reasoning context, how much irrelevant context remains, and whether a real reasoning vertical slice improves over simpler context construction.

### Q-006. How should relevant investigations be activated?

**Status:** Reframed after V0; retrieval and first Horizon validated, activation policy still open

P0's path-sensitive tag-trigger activation should not scale unchanged. Foundation 019 instead uses staged retrieval, explicit applicability/context checks, relevance/prioritization, and selective reasoning context.

Current executable evidence now covers:

```text
production lexical retrieval            Checkpoint 135
semantic complementarity                Checkpoints 137-139
one-hop relation expansion              Checkpoint 141
applicability / missing context          Checkpoint 141
```

Still open are relevance/prioritization, selective context assembly, recommendation/required-state transitions, and the exact mechanism by which a relevant methodological concern becomes a concrete investigation or action.

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

**Status:** Substantially advanced through the first MethodologicalHorizon; relevance/context selection remains active

Current direction:

```text
large global knowledge universe
    -> high-recall project-specific retrieval/filtering
    -> bounded explained MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

The first four structural pieces now have executable evidence through Checkpoints 135, 139, and 141: accepted-current retrieval, complementary semantic coverage, one-hop governed relation expansion, and three-valued applicability/missing-context handling. The next unresolved part is relevance/prioritization and selective context assembly, including how project state supplies the context predicates required to make those choices.

### Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved end to end

Foundation 008, Foundation 020, D-031, and Specification 004 establish scope-aware, revisioned, provenance-aware, candidate-versus-accepted governance principles. Automatic learning/promotion remains deliberately unimplemented.

---

## Retrieval, ranking, and context construction

### Q-044. How should production retrieval and MethodologicalHorizon construction work?

**Status:** Substantially answered through the first explained Horizon; relevance/budget/context policy remains active

Research 016 and Specification 009 established the frozen decomposition. The initial retrieval/Horizon sequence has now been executed rather than left hypothetical.

#### Production lexical baseline

Checkpoint 135:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
```

The lexical semantic miss is RH-S01 `class-imbalance`.

#### Exact dense semantic comparator

Checkpoint 137 preserves the FastEmbed 0.8.0 / `BAAI/bge-small-en-v1.5` experiment-only result:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
RH-S MRR                 0.75
```

Dense retrieval recovers `class-imbalance` at rank 1 but misses RH-S04 `ecdf`, which lexical retrieval had recovered at rank 1. Dense-only therefore did not earn replacement of lexical retrieval.

#### Complementary hybrid comparator

Checkpoint 139 / workflow run `32561118325`:

```text
Ubuntu PASS
Windows PASS
RH-S Recall@3            1.00
RH-S MRR                 0.875
RH-S critical omissions  0 / 4
RH-L Recall@3            1.00
RH-L MRR                 1.00
```

The channels are materially complementary on the frozen benchmark. This advances hybrid lexical + exact semantic retrieval as the leading current hypothesis, but does not permanently select FastEmbed, BGE, RRF `k=60`, a vector database, ANN, or embedding persistence.

#### First explained MethodologicalHorizon

Specification 012 v1.0 / Checkpoint 141 / workflow run `32561727632`:

```text
Ubuntu PASS
Windows PASS
RH-R relation cases       4 / 4 PASS
RH-A applicability cases  5 / 5 PASS
authoritative knowledge   unchanged
```

The accepted bounded seam is:

```text
stable/revision-transparent candidates
    -> accepted-current navigation reads
    -> outbound one-hop governed relation expansion
    -> TRUE / FALSE / UNKNOWN applicability evaluation
    -> POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    -> explained included/excluded MethodologicalHorizon
```

This answers the first retrieval, relation-expansion, and applicability-construction questions. It deliberately does not answer final relevance, recommendation, or context budgeting.

Still required:

```text
relevance / prioritization over the explained Horizon
bounded Horizon budget policy
RH-C selective context construction
exact required-revision coverage after context selection
irrelevant-context inclusion/cost
serialized size / token burden
omission quality
production semantic/fusion integration only when a real vertical slice requires it
reranking only if ordering becomes a measured downstream problem
```

Primary current evidence:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/research/019_first_methodological_horizon_application_seam.md

docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/specifications/012_v1_first_methodological_horizon_builder.md

docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md

experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
```

### Q-045. How should recommendation quality be evaluated separately from knowledge coverage?

**Status:** Active V1 question; coverage, retrieval, and applicability failure classes are now executable

The evaluation decomposition is now materially stronger than at Specification 009 freeze time. The system can distinguish:

```text
knowledge absent from catalog
known but not retrieved
retrieved through lexical and/or semantic channel
retrieved/seeded but rejected as INAPPLICABLE
retained but unresolved because MISSING_CONTEXT
relation-added to the Horizon
```

This means the first `KNOWN_NOT_RETRIEVED`, `INAPPLICABLE`, and `MISSING_CONTEXT` failure classes are executable rather than conceptual.

The remaining downstream distinction is:

```text
applicable but judged irrelevant
relevant but ranked too low / omitted by context budget
recommended but skipped
recommended incorrectly
required concern omitted
human/execution outcome after recommendation
```

The next relevance/RH-C gate should therefore measure ranking/context omission separately from upstream retrieval and applicability failures. Recommendation correctness should not be collapsed into retrieval recall.

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

D-032 selects the initial reasoning-runtime infrastructure, not the final LLM provider or model. Provider/model choice must remain separate from ADS domain semantics and should preserve deterministic fake-model testing and a replaceable adapter boundary. MCP is the selected direction for external tool/resource interoperability where appropriate, but the production server/tool catalog remains open.

### Q-046. Which agent/runtime infrastructure, if any, should V1 adopt?

**Status:** Answered and closed for the initial V1 runtime selection

Specification 005 was executed rather than resolved from framework documentation alone.

Evidence:

```text
Direct model calls
    Checkpoint 129
    cross-platform PASS
    viable minimum-dependency control/fallback

OpenAI Agents SDK 0.19.4
    Checkpoint 131
    AR-01 through AR-12 PASS
    Ubuntu PASS
    Windows PASS

LangGraph 1.2.10
    Checkpoint 132
    AR-01 through AR-12 capability envelope PASS
    Ubuntu PASS
    Windows PASS
    stronger explicit persisted execution/checkpoint durability
    larger dependency/operational surface and explicit interrupt-node replay semantics
```

Research 015 applied the Specification 005 stop rule. Microsoft Agent Framework and Google ADK 2.0 were not implemented because no current differentiator was judged likely to overturn the now-bracketed choice among minimum-dependency direct calls, the smaller complete agent-loop runtime, and the stronger durable-workflow runtime.

D-032 accepts:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

The decision is version-governed rather than permanent lock-in. Direct model calls remain the fallback/reference path. LangGraph remains a future escalation path if stronger long-running workflow durability, checkpoint history/time travel, or independently durable workflow stages become empirically necessary.

This closes only the initial runtime-infrastructure question. It does not select the final provider/model, multi-agent architecture, production runtime-state persistence schema, or production MCP catalog.

Primary evidence:

```text
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/research/014_langgraph_1_2_10_released_durability_comparator_audit.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md

docs/checkpoints/129_direct_model_call_runtime_control_cross_platform_gate_passed.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
docs/checkpoints/132_langgraph_durability_comparator_cross_platform_gate_passed.md

experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md
```

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

Checkpoint 127 and the final result artifact record successful validation of the richer governed import/accept/export/pinning round-trip on:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

Final gate:

```text
V1 governed knowledge roundtrip closure gate
run 32496856945
```

Two PostgreSQL portability defects were resolved before closure:

```text
1. overlong manually named migration constraint
2. Alembic migration revision identity longer than the default
   `alembic_version.version_num VARCHAR(32)` envelope
```

Migration 0002 now uses `0002_knowledge_interchange`, and a deterministic regression guard enforces unique Alembic revision IDs with length <= 32 characters.

The old PostgreSQL diagnostic workflow was removed after closure.

This answer is scoped to the current governed persistence/interchange seam. It does not close retrieval quality, MethodologicalHorizon construction, external ingestion, or knowledge-authoring questions.

Primary evidence:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

---

## Product interface and Project Cockpit

### Q-049. What should the primary active-work interface be?

**Status:** Substantially answered and promoted for V1 interaction architecture

Specification 008 now promotes the Project Cockpit as the V1 primary immersive active-work model, with direct specialist views retained as alternative entry/inspection/record paths. This closes the basic interface-direction question for V1 while leaving final visual identity and future capability depth open.

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

The seventh review judged pinch smoothness substantially improved, accepted Jump/search and stage orientation, requested moderately faster scale travel, and explicitly classified the remaining tiny occasional pinch hitch as non-blocking deferred polish. Pinch sensitivity was increased from `0.00135` to `0.0018` before Specification 008 promotion.

A later post-promotion human review found a shorter-normal-window Jump/composer collision and pinch scale travel that remained too conservative. Checkpoint 130 records the bounded implementation repair:

```text
Jump/search
    palette measures actual rendered composer geometry while open
    re-clamps on window resize, fullscreen changes, and composer resize
    lower results remain internally scrollable

pinch
    sensitivity 0.0018 -> 0.0024
    smoothing/coalescing/anchoring architecture unchanged
```

Automated validation head `ae83e920b3fa43ee8242bdb1ca2640d23a474c71` passed V1 frontend spike run `167 / 32503861255` on Ubuntu, Windows, Chromium interaction/accessibility, controlled direct-view visual regression, the normal-window Jump resize regression, and the faster anchored-pinch regression.

The subsequent real-browser/hardware retest accepted the repaired normal-window Jump behavior, fullscreen non-regression, and faster pinch feel as good enough to continue. The remaining tiny occasional pinch hitch stays explicitly deferred non-blocking polish.

Still open inside the broader Cockpit product program:

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

These are not blockers for the promoted basic interaction architecture.

### Q-051. What frontend stack and visualization system should be promoted?

**Status:** Partially narrowed, not accepted as final architecture

React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest remain the leading frontend hypothesis and have supported the Cockpit evidence through Checkpoint 130. Formal final stack promotion remains open. ECharts versus Plotly remains an empirical comparison. Tauri remains deferred.

### Q-052. What should the final Cockpit visual identity, stage taxonomy, layout, control architecture, and URL contract be?

**Status:** Open by design, no longer a prerequisite for basic interaction promotion

Human review strongly supports the current canvas-dominant spatial direction, restrained ambient world, viewport-aware orientation, compact/fold-away HUD, searchable Jump navigation, and compact right-edge map controls as useful current patterns. The final visual identity, stage taxonomy/widths, semantic zoom, auto-layout, minimap, graph/canvas/gesture library, public route contract, permanent stage-ruler treatment, permanent tool-rail styling, exact ambient styling, and canonical screenshot baseline remain intentionally unfrozen.

Specification 008 should be treated as the interaction baseline while these product-design questions evolve.

---

## Evaluation, resource allocation, and stopping

### Q-013. How should analysis depth and resource budgets work?

**Status:** Open; V0 provides strong cost evidence

V0 demonstrated that explicit machinery can consume more than twice the token budget without material reliability gain. Optional depth should depend on expected value, uncertainty, risk, project intent, and resource constraints while mandatory validity obligations remain mandatory.

### Q-014. How should the system decide when experimentation can stop?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant residual uncertainty, diminishing information value, unavailable discriminating evidence, or compatible resource limits.

### Q-015. How should project types be characterized?

**Status:** Substantially reframed

Use multidimensional project characterization rather than one exclusive project-type label. Exact representation remains open.

### Q-016. How should system quality itself be evaluated?

**Status:** Substantially advanced; broader V1 evaluation remains open

V0 completed a preregistered held-out falsification experiment. V1 additionally requires product/human evaluation, retrieval/horizon benchmarks, runtime bakeoffs, cross-platform gates, accessibility checks, and eventually project replay across heterogeneous real projects.

### Q-017. How should real projects become regression tests?

**Status:** Substantially advanced conceptually

Foundation 017 proposes project replay from original starting inputs. Long-term privacy-safe extraction, diversity, benchmark maintenance, and comparison criteria remain open.

### Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

Foundation 019 provides candidate dimensions including validity importance, information gain, downstream impact, uncertainty reduction, risk, cost, redundancy, project intent, and human preference. No final ranking/scoring mechanism exists.

### Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Prototype V0 completed; broader program open

The V0 synthetic churn benchmark and held-out protocol are completed historical evidence. The next evaluation program should broaden to retrieval/horizon quality, larger changing project trajectories, human-navigation burden, product usability, and project replay across project families.

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
Q-044  define relevance/prioritization and RH-C selective-context quality/cost over the validated explained Horizon
Q-045  extend executable coverage/retrieval/applicability separation into ranking, recommendation, required-concern, and outcome quality
Q-029  determine what prioritization dimensions earn an operational relevance policy
Q-051  determine which frontend/chart choices deserve final stack promotion
Q-052  evolve final Cockpit visual/system details on top of Specification 008
```

Q-046 is closed for the initial V1 runtime selection through Specification 005, Research 015, Checkpoint 133, and D-032. Q-048 is closed through Checkpoint 127. Q-049 and the basic interaction-architecture part of Q-050 are no longer active blocking questions because Specification 008 is promoted. The remaining Q-050 pinch hitch is deferred product polish rather than an architecture reopening.

Q-044 remains active, but its boundary has moved materially: production lexical retrieval, semantic complementarity, one-hop relation expansion, applicability/missing-context handling, and the first explained MethodologicalHorizon are now validated. The unresolved question starts at relevance/prioritization, Horizon budgeting, RH-C selective context, and downstream reasoning/recommendation quality.
