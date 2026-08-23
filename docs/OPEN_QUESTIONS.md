# Open Questions

**Status:** Current canonical unresolved-question register  
**Last reconciled:** 2026-08-23  
**Reconciliation context:** Prototype V0 is complete. V1 has established the project/object foundations, Project Cockpit interaction architecture, governed knowledge persistence/interchange, runtime boundary, retrieval/Horizon/selective-context chain, real reasoning-context evidence, preserved negative and incomplete recommendation/action evidence, dependency-backed sequencing evidence, and now a bounded governed autonomous live-experiment launcher. Specification 018 passed cross-platform provider-free CI and an end-to-end owner issue -> launcher -> workflow_dispatch -> independent probe gate without a manual Actions UI click or provider call. Specification 017 remains incomplete historical evidence and its implementation remains unpromoted. The next high-value scientific boundary is a new preregistered recommendation/action-value experiment with exact supplied-context provenance owned by the system.

This document records important unresolved questions in current canonical form. Detailed reasoning belongs in foundations, research memos, specifications, checkpoints, experiment records, and Git history.

---

## Highest-value unresolved questions

### Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Selective reasoning-context seam supported; downstream recommendation value remains unresolved

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

Specification 014 showed `1.000000` frozen semantic quality for SELECTIVE and FULL_HORIZON with a SELECTIVE/FULL input-token ratio of `0.334379`.

Specification 015 did not establish recommendation/action value. Specification 016 repaired the construct-validity question around sequencing by requiring an explicit activating dependency. Specification 017 then attempted the downstream value comparison under that stronger construction, but its live run was incomplete before a matched quality comparison could be evaluated.

Still open:

```text
whether selective methodological knowledge adds recommendation/action value beyond a strong generic reasoner
natural-language/project-state -> task-profile derivation
harder heterogeneous/changing project states
open-world concern/action discovery
final context-budget policy
production recommendation/persistence semantics
```

### Q-006. How should relevant investigations be activated?

**Status:** Retrieval/Horizon/selective-context mechanics validated; dependency-backed sequencing supported; production activation semantics remain open

P0's path-sensitive trigger/frontier machinery should not return unchanged. Current evidence supports staged retrieval/applicability/relevance followed by selective reasoning.

Supported bounded sequencing constraint:

```text
DEFER-like sequencing
    should be backed by an explicit activating dependency/trigger
    when deterministic separation from NOT_NOW is expected
```

Still open:

```text
project state -> requested reasoning functions
open-world concern/action generation
recommendation -> durable Proposal / Question / Investigation
human approval / automatic-action policy
production REQUIRED/BLOCKING semantics and scope
production sequencing relation model
```

### Q-008. How should project state be represented?

**Status:** Substantially advanced, not complete

Foundation 018 establishes Objects, Relations, Events, and Views. Specification 016 provides evidence that sequencing becomes more testable when an exact activating relation is represented. Specification 017 used experiment-owned trigger pointers but did not define production relation persistence.

Still open:

```text
complete production object/relation schema
accepted recommendation -> project object/event mapping
sequencing/dependency persistence
staleness/invalidation semantics
approval and authority state
```

### Q-021. How should model and tool providers be selected?

**Status:** Open; runtime boundary selected, experiment model treatment intentionally fixed

D-032 selects OpenAI Agents SDK behind an ADS-owned `ReasoningRuntime` as the initial runtime boundary. Specifications 014-017 reused one concrete model/runtime treatment to avoid confounding adjacent experiments. It is not a final provider/model decision.

### Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

Candidate dimensions include validity importance, information gain, downstream impact, uncertainty reduction, risk, cost, redundancy, project intent, and human preference.

Specification 016 supports explicit dependency-backed sequencing as a useful construct. Specification 017 did not complete the downstream system-value comparison, so no final recommendation ranking/disposition policy is justified.

### Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Structurally advanced through real reasoning; recommendation-state mapping remains open

Current bounded path:

```text
project-relevant retrieval
    -> explained MethodologicalHorizon
    -> explicit applicability/context checks
    -> explicit task reasoning functions
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured reasoning output
```

The next production boundary is not retrieval tuning. It is how justified reasoning/recommendations become inspectable durable project state without over-automation.

### Q-044. How should production retrieval, MethodologicalHorizon construction, and selective context work?

**Status:** Substantially answered for the first bounded chain through real reasoning; production scaling remains open

Evidence chain:

```text
Checkpoint 135   lexical retrieval
Checkpoint 137   dense complementary signal
Checkpoint 139   hybrid comparator
Checkpoint 141   explained Horizon; unknown != false
Checkpoint 143   selective exact-revision context
Checkpoint 146   real-model selective-context value
```

No current downstream evidence justifies returning to retrieval/reranking/vector tuning.

Still open:

```text
production task-profile derivation
larger heterogeneous Horizon behavior
final budgets
when richer semantic/LLM relevance becomes necessary
production semantic/fusion infrastructure only when measured deficiency requires it
```

### Q-045. How should recommendation and reasoning quality be evaluated separately from knowledge coverage and provenance?

**Status:** Reasoning-quality separation validated; recommendation evaluator advanced; provenance boundary newly exposed

Specification 014 separated reasoning quality from context size. Specification 015 added deterministic recommendation metrics and a blinded semantic judge. Specification 016 isolated and validated the dependency-backed sequencing construct.

Specification 017 additionally exposed that this distinction is necessary:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

The system already knows exact supplied `stable_key@revision_id` identities and context digests. A model-authored `methodological_basis` field duplicated that provenance and caused 19 GENERIC invalid structured attempts by attracting reasoning-function labels even though GENERIC supplied zero knowledge revisions.

Next evaluation design should separate:

```text
SYSTEM-OWNED PROVENANCE
    exact context/revision identity
    treatment digest

MODEL-OWNED CONTENT
    dispositions
    dependency pointers
    scopes
    clarifications
    rationales
```

Any model-authored knowledge citation layer should be evaluated as a distinct optional capability rather than treated as the authoritative context provenance channel.

### Q-053. How should authorized live experiments be launched autonomously and safely?

**Status:** Bounded V1 mechanism answered and supported; broader approval/orchestration policy remains open

Specification 018 now establishes and validates the first governed control plane:

```text
owner-created [ADS LIVE] issue
    -> repository-controlled launch authorization
    -> exact owner identity checks
    -> exact source SHA
    -> exact successful CI run IDs
    -> conservative duplicate check
    -> allowlisted workflow_dispatch
    -> independently validating target workflow
```

End-to-end provider-free evidence:

```text
implementation source   27e7bc84b5f63d65d43de9a5bd27d1fdc0677071
provider-free CI        32660168566
launcher run            32660333663
probe run               32660340429
probe job               97245432893
outcome                 GOVERNED_LAUNCHER_SUPPORTED
```

The launcher receives no provider credential. Issue text cannot supply executable workflow/ref/SHA/command/model/prompt/secret configuration. The target workflow independently checks its exact source SHA and confirmation before any provider call.

Remaining open questions are broader than the bounded launcher itself:

```text
production human approval/escalation policy
project-level authorization UX
authorization expiry/revocation lifecycle
provider-backed result/status presentation in the Cockpit
retention and cleanup policy for launch issues and completed authorizations
multi-user / organization authorization if the project later requires it
```

The scientific content of an experiment remains separate from this control plane. A provider-backed authorization is permitted only after that experiment's own contract is frozen and its exact implementation head is green.

---

## System purpose, authority, and project constitution

### Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The purpose is project-relative: create the best defensible data-science process for the project's goals, constraints, deliverables, risk, and desired human involvement while preserving non-negotiable methodological integrity. Cross-project success criteria combining reliability, methodological coverage, human-navigation burden, efficiency, reproducibility, and product usability remain open.

### Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed, still open

Autonomy should vary with project intent, risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state rather than being one global mode. Final proposal/approval/automatic-action/escalation policy remains open.

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

**Status:** Open

The product/object model provides places for Constraints, Questions, Findings, Decisions, events, and approvals, but the complete policy/state representation remains unspecified.

---

## Project objects, evidence, revision, and completion

### Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

Candidate triggers include high risk, epistemic single points of failure, weak high-leverage assumptions, fragile consequential claims, governance requirements, and low-maturity knowledge. Operational policy remains open.

### Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Evidence sufficiency remains decision-specific and may depend on validity, uncertainty, independence, shared ancestry, risk, cost, and probability that additional evidence changes the decision.

### Q-012. How should uncertainty and confidence be represented?

**Status:** Open

No final numerical, categorical, narrative, or structural representation is selected.

### Q-019. How should invalidation and repair work?

**Status:** Reframed after V0

P0's generic dependency reopening/support-reassessment machinery did not earn its cost as a universal always-on mechanism. Selective evidence-driven staleness/invalidation and targeted repair remain necessary.

### Q-033. Should analytical Questions and Claims be primary state objects?

**Status:** Strongly supported conceptually, not frozen as universal orchestration law

Foundation 018 treats Questions, Findings, Claims, Evidence, and Decisions as central project objects without claiming every workflow reduces to one Question/Claim state machine.

### Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

Completion should be obligation/question/deliverable driven and account for residual uncertainty, expected value of additional work, risk, and resource limits.

---

## Reusable knowledge and governance

### Q-004. How should data-science knowledge be represented?

**Status:** Substantially answered at conceptual/V1 architecture level

Foundation 020 governs `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, collections, provenance/governance, retrieval/applicability/context structures, exact revisions, and separation from execution capability. Final taxonomies, authoring UX, full schema coverage, provenance ontology, and large-scale behavior remain open.

### Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially answered conceptually, taxonomy still open

Stable asset/revision identity, components, narrative facets, intrinsic kinds, reasoning functions, static relations, conditional rules, retrieval, applicability, context requirements, semantic checks, provenance, scope, and governance remain distinct. Exact production enums remain intentionally unfrozen.

### Q-018. How should knowledge packages interact?

**Status:** Substantially refined, not resolved at scale

Current architecture uses stable identities, typed semantic relations, conditional rules, reusable concepts, components, and collections rather than one giant package graph. Large-scale deduplication, cycles, conflicting soft guidance, and composition quality remain open.

### Q-022. How should external knowledge and source material be integrated?

**Status:** Substantially advanced, not complete

Specification 004 and D-031 establish deterministic interchange and governance safety. Ingestion/review workflows for heterogeneous external sources and full provenance/source persistence remain open.

### Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined, not finalized

Knowledge role, maturity, enforcement authority, scope confidence, provenance, challenge history, and operational coverage should remain distinct. Final production promotion/review/freshness lifecycle remains open.

### Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved end to end

Foundation 008, Foundation 020, D-031, and Specification 004 establish scope-aware, revisioned, provenance-aware, candidate-versus-accepted governance principles. Automatic learning/promotion remains deliberately unimplemented.

---

## Agent/runtime, execution, and interoperability

### Q-009. What agent or responsibility structure is useful?

**Status:** Substantially answered for initial V1; specialist/multi-agent structure remains open

D-032 selects a single-principal-reasoner-first runtime shape through an ADS-owned OpenAI Agents SDK adapter. Specialist agents should be added only if later evidence demonstrates a meaningful benefit.

### Q-020. What should the execution environment look like?

**Status:** Open at production scale

Foundation 018 establishes reproducible run contracts and retains VS Code as the developer workbench. Local/remote/container/GPU/cloud execution remains an abstraction problem rather than a settled backend.

### Q-046. Which agent/runtime infrastructure, if any, should V1 adopt?

**Status:** Answered and closed for initial V1 runtime selection

D-032 accepts OpenAI Agents SDK behind an ADS-owned `ReasoningRuntime` port with `openai-agents==0.19.4` as the validated starting package. Direct model calls remain fallback/reference; LangGraph remains a future durability escalation path.

### Q-047. What role should MCP, AG-UI, and A2A ultimately play?

**Status:** Partially answered, implementation open

```text
MCP     external tool/resource interoperability, not project memory
AG-UI   possible transport adapter around ADS-owned interaction/run events
A2A     defer until independently deployed remote agent systems are real
```

---

## Persistence, portability, and project preservation

### Q-026. How should repository and preservation structure evolve?

**Status:** Substantially answered for current development needs; still evolvable

The project uses canonical documents, foundations, research memos, specifications, checkpoints, experiment ledgers, raw artifacts, KNOWLEDGE_MAP, MAJOR_CHANGES, Git history, and explicit continuity/promotion/reconciliation procedures. Specifications 015-017 demonstrate why failed and incomplete experiments must remain separately versioned from production promotion.

### Q-043. When should the project move beyond Git and Markdown for development knowledge preservation?

**Status:** Open with explicit deferral criteria

Git + Markdown remains sufficient while routing, reconciliation, and consistency remain manageable. More complex infrastructure should be justified by observed retrieval, contradiction, dependency, concurrency, or automation costs.

### Q-048. When is the governed reusable-knowledge persistence round-trip considered closed?

**Status:** Answered and closed for the current V1 governed seam

Checkpoint 127 records successful governed import/accept/export/pinning validation on SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18.

---

## Product interface and Project Cockpit

### Q-049. What should the primary active-work interface be?

**Status:** Substantially answered and promoted for V1 interaction architecture

Specification 008 promotes the Project Cockpit as the V1 primary immersive active-work model, with direct specialist views retained as alternative entry/inspection/record paths.

### Q-050. How should the Cockpit scale to large projects and feel under real spatial interaction?

**Status:** Substantially answered at interaction-architecture level; residual polish/scale questions remain

Accepted interaction architecture includes 2D navigation/recovery, bounded zoom, native pinch capability, viewport-aware stage orientation, scalable Jump/search, compact/fold-away chrome, collision-safe floating surfaces, fullscreen, keyboard/reduced-motion support, and world-owned ambient depth.

### Q-051. What frontend stack and visualization system should be promoted?

**Status:** Partially narrowed, not final

React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest remain the leading frontend hypothesis. Final stack and chart-library promotion remain open.

### Q-052. What should the final Cockpit visual identity, stage taxonomy, layout, control architecture, and URL contract be?

**Status:** Open by design

Specification 008 is the interaction baseline. Final visual identity, stage taxonomy/widths, semantic zoom, auto-layout, minimap, graph/canvas/gesture library, public route contract, permanent chrome treatment, and canonical screenshot baseline remain unfrozen.

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

V0 completed a preregistered held-out falsification experiment. V1 now includes product/human evaluation, retrieval/Horizon benchmarks, runtime bakeoffs, cross-platform gates, accessibility checks, selective-context construction, a passed real reasoning-context comparison, a preserved failed recommendation/action experiment, a successful construct-validity diagnostic, and an incomplete relation-backed recommendation/action experiment that exposed a provenance-instrumentation boundary.

### Q-017. How should real projects become regression tests?

**Status:** Substantially advanced conceptually

Foundation 017 proposes project replay from original starting inputs. Privacy-safe extraction, diversity, benchmark maintenance, and comparison criteria remain open.

### Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Prototype V0 completed; broader program open

V1 has progressively separated retrieval, context, reasoning, recommendation calibration, disposition construct validity, provenance, and system-value questions. After the current bounded program, evaluation should increasingly use changing project trajectories and heterogeneous real-project replay rather than indefinitely refining synthetic microstates.

---

## Historical prototype questions retained for provenance

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

## Active boundary

Current governing result sources:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
docs/checkpoints/157_relation_backed_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/158_specification_017_live_boundary_frozen.md
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
experiments/relation_backed_recommendation_action_value/V1_RELATION_BACKED_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/relation_backed_recommendation_action_value/results/spec017-live-20260823-run-32656446705/
```

The immediate task is preservation-only integration of this evidence without promoting the experiment implementation, followed by a governed autonomous live-launcher design and a separately preregistered recommendation/action experiment with system-owned provenance. Specifications 015-017 remain immutable historical evidence.
