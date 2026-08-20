# Open Questions

**Status:** Current canonical unresolved-question register  
**Last reconciled:** 2026-08-20  
**Reconciliation context:** Prototype V0 complete; post-V0 V1 architecture and product foundations established; first production persistence/interchange slices implemented; Project Cockpit second human review completed through Checkpoint 119

This document records important unresolved questions in current canonical form. Detailed reasoning belongs in foundations, research memos, specifications, checkpoints, experiment records, and Git history.

Existing identifiers are retained for continuity even when a question has been substantially reframed or partly answered. A status such as `Substantially answered` means the project has a current governing direction but still has implementation, evaluation, or scope questions to resolve.

---

## System purpose, authority, and project constitution

### Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The primary purpose is project-relative: create the best defensible data-science process for the project's goals, constraints, deliverables, and desired human involvement while preserving non-negotiable methodological integrity.

Still open: system-level success criteria across heterogeneous project classes and how reliability, coverage, human-navigation burden, efficiency, reproducibility, and product usability should be combined in evaluation.

### Q-002. What degree of autonomy should the system have?

**Status:** Substantially reframed, still open

Autonomy should vary with project intent, risk, admissibility, uncertainty, reversibility, authority, action type, and assurance state rather than being one global mode.

The final policy for automatic action, proposal, approval, escalation, and stopping remains open.

### Q-003. What should the human's role be?

**Status:** Substantially refined, still open

Foundation 013 establishes the current LLM-system-human boundary. The human should concentrate on goals, semantics, consequential trade-offs, authoritative domain input, critique, approvals, and intervention where judgment adds value.

The exact escalation policy and project-configurable control model remain open.

### Q-027. What belongs in the non-negotiable methodological quality floor?

**Status:** Substantially refined, not finalized

Current epistemic core: semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity, preceded by admissibility and followed by risk-sensitive assurance.

The exact operationalization across project classes remains open.

### Q-028. How should project intent be represented?

**Status:** Substantially refined, not finalized

Objectives, constraints, deliverables, human-control preferences, definitions, and project/model/operational distinctions remain the leading conceptual structure.

The final schema and interaction model remain open.

### Q-030. Are the five epistemic invariants complete and precise enough?

**Status:** Strong design hypothesis under broader validation

Prototype V0 and later product design are compatible with them, but broader project diversity may expose missing distinctions or needed revisions.

### Q-031. What belongs in the admissibility layer?

**Status:** Open at production depth

Legal, ethical, privacy, policy, safety, organizational, and explicit user constraints are conceptually distinct from methodological validity. Their exact scope, representation, and authority model remain unresolved.

### Q-032. How should risk-sensitive assurance be represented?

**Status:** Open at production depth

The project still needs a practical model linking consequence/risk to verification, replication, robustness, subgroup analysis, human approval, monitoring, and documentation requirements.

### Q-035. How should admissibility, risk, controls, approvals, and assurance participate in project state?

**Status:** Open, coupled to Q-002/Q-008/Q-031/Q-032

The product/object model provides places for Constraints, Questions, Findings, Decisions, events, and approvals, but the complete policy/state representation is not yet specified.

---

## Project objects, state, evidence, and revision

### Q-008. How should project state be represented?

**Status:** Substantially advanced, not complete

Foundation 018 establishes the current product-level separation of Objects, Relations, Events, and Views and a candidate object model around Project/Intent, Artifacts/Data, Questions/Assumptions/Findings/Claims, Proposals/Investigations/Runs/Evidence/Decisions, reporting, and history.

The first V1 persistence slice implements only a bounded subset. The complete production schema remains open.

### Q-010. When is independent review required?

**Status:** Substantially refined, not resolved

Candidate triggers include high risk, epistemic single points of failure, weak high-leverage assumptions, fragile consequential claims, governance requirements, and low-maturity knowledge.

The operational policy remains open.

### Q-011. What counts as sufficient evidence for a decision?

**Status:** Active

Evidence sufficiency remains decision-specific and may depend on validity, uncertainty, independence, shared ancestry, risk, cost, and the probability that more evidence changes the decision.

### Q-012. How should uncertainty and confidence be represented?

**Status:** Open

No final numerical, categorical, narrative, or structural representation has been selected.

### Q-019. How should invalidation and repair work?

**Status:** Reframed after V0

Prototype V0 showed that its generic dependency reopening/support-reassessment machinery did not earn its cost as a general always-on architecture, even though its repair behavior was precise.

The broader need remains: new evidence or changed assumptions must be able to make downstream claims, decisions, evidence, or report content stale or invalid. Future mechanisms should be targeted, selective, and evidence-driven rather than blindly recursive.

### Q-033. Should analytical Questions and Claims be primary state objects?

**Status:** Strongly supported conceptually, not frozen as universal orchestration law

Foundation 018 treats Questions, Findings, Claims, Evidence, and Decisions as central project objects. The project still avoids claiming that every workflow must be reducible to one Question/Claim state machine.

### Q-034. How should project completion be defined?

**Status:** Substantially refined, not resolved

General completion should be obligation/question/deliverable driven and should consider residual uncertainty, expected value of additional work, risk, and resource limits.

---

## Reusable methodological knowledge and methodological navigation

### Q-004. How should data-science knowledge be represented?

**Status:** Substantially answered at the conceptual/V1 architecture level

Foundation 020 now governs the durable conceptual representation: `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, collections, provenance/governance, retrieval/applicability/context structures, exact revisions, and separation from execution capability.

Still open: final knowledge-kind/function taxonomies, authoring experience, full production schema coverage, provenance ontology, and large-scale operational behavior.

### Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

**Status:** Substantially reframed after V0; active V1 question

The current direction is selective rather than always-on: global knowledge is retrieved/filtered into a bounded MethodologicalHorizon, explicit checks handle reliable prerequisites/hard rules, and flexible reasoning handles semantic relevance, trade-offs, synthesis, and open-world concern discovery.

The quality of selective context assembly remains to be measured.

### Q-006. How should relevant investigations be activated?

**Status:** Reframed after V0; active V1 question

P0's narrow path-sensitive tag-trigger activation should not be scaled unchanged. Foundation 019 instead treats activation as staged relevance and horizon construction driven by project state, retrieval, explicit applicability checks, and flexible reasoning.

The production retrieval/ranking mechanism remains unvalidated.

### Q-007. What should a reusable decision or knowledge unit contain?

**Status:** Substantially answered conceptually, taxonomy still open

Foundation 020 separates stable asset identity/revisions, components, narrative facets, intrinsic kinds, reasoning functions, static relations, conditional rules, retrieval, applicability, context requirements, semantic checks, provenance, scope, and governance.

Exact production enums and authoring conventions remain intentionally unfrozen.

### Q-018. How should knowledge packages interact?

**Status:** Substantially refined, not resolved at scale

The current architecture uses explicit stable identities, typed semantic relations, conditional rules, reusable concepts, components, and collections rather than one giant package graph.

Large-scale deduplication, cycle handling, conflicting soft guidance, and composition quality remain open.

### Q-022. How should external knowledge and source material be integrated?

**Status:** Substantially advanced, not complete

Specification 004 and D-031 establish deterministic reusable-knowledge interchange and governance safety. Knowledge still requires proposition-specific provenance, scope, authority, limitations, freshness, and revision identity.

Still open: ingestion/review workflows for heterogeneous external sources and full provenance/source persistence.

### Q-025. What maturity model should be used for ideas and reusable knowledge?

**Status:** Substantially refined, not finalized

Knowledge role, maturity, enforcement authority, scope confidence, provenance, challenge history, and operational coverage should remain distinct. The interchange/persistence layers already prevent candidate material from silently becoming accepted authority.

The final production promotion/review/freshness lifecycle remains open.

### Q-037. How should project state activate reusable knowledge and reasoning?

**Status:** Reframed after V0; active V1 methodological-horizon problem

Current direction:

```text
large global knowledge universe
    -> high-recall project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

The first real production horizon and context assembler have not yet been validated.

### Q-038. How should reusable knowledge quality and evolution be governed?

**Status:** Substantially refined, not resolved end to end

Foundation 008, Foundation 020, D-031, and Specification 004 establish scope-aware, revisioned, provenance-aware, candidate-versus-accepted governance principles. Automatic learning/promotion remains deliberately unimplemented.

---

## Retrieval, ranking, and context construction

### Q-044. How should production retrieval and MethodologicalHorizon construction work?

**Status:** Active V1 question

Still required:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion if justified
ranking/relevance evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
```

Do not select an embedding model, reranker, ANN service, or vector database from intuition. The benchmark must test omission quality, relevance, and context cost rather than retrieval speed alone.

### Q-045. How should recommendation quality be evaluated separately from knowledge coverage?

**Status:** Active V1 question

The system should distinguish at least:

```text
knowledge absent from catalog
known but not retrieved
retrieved but judged inapplicable
applicable but ranked too low
recommended but skipped
recommended incorrectly
required concern omitted
```

A practical benchmark and acceptance envelope remain to be designed.

---

## Agent/runtime, execution, and interoperability

### Q-009. What agent or responsibility structure is useful?

**Status:** Reframed; implementation deliberately unselected

Knowledge, capabilities, project semantics, and runtime actors remain separate. The current default is one principal reasoner plus tools, with specialist agents added only if evidence demonstrates a concrete benefit.

Specification 005 governs the runtime bakeoff.

### Q-020. What should the execution environment look like?

**Status:** Open at production scale

Foundation 018 establishes that system-triggered and manual execution should share reproducible run contracts and that VS Code remains the professional developer workbench. Local-first execution is a strong current hypothesis, but local/remote/container/GPU/cloud execution remains an abstraction problem rather than a settled backend.

### Q-021. How should model and tool providers be selected?

**Status:** Open; runtime evaluation contract exists

Provider choice remains separate from ADS domain semantics. Specification 005 requires provider/test substitution and permits a direct-model-call outcome if no runtime earns its complexity.

### Q-046. Which agent/runtime infrastructure, if any, should V1 adopt?

**Status:** Active V1 evaluation question

Specification 005 compares OpenAI Agents SDK, LangGraph, Microsoft Agent Framework, and Google ADK 2.0 against ADS-shaped requirements including domain isolation, tools, MCP, HITL, durable resume, context transparency, cancellation, retries, structured output, observability, and test substitution.

No candidate is accepted yet.

### Q-047. What role should MCP, AG-UI, and A2A ultimately play?

**Status:** Partially answered, implementation open

Current direction:

```text
MCP
    first-class external tool/resource interoperability candidate
    not project memory or internal application bus

AG-UI
    evaluate as a transport adapter around ADS-owned interaction/run events
    not ADS domain semantics

A2A
    defer until independently deployed remote agent systems are genuinely needed
```

The final production adapters remain unselected.

---

## Persistence, interchange, and portability

### Q-026. How should repository and preservation structure evolve?

**Status:** Substantially answered for current development needs; still evolvable

The project now uses canonical documents, foundations, research memos, specifications, checkpoints, experiment ledgers, a knowledge map, a major-changes ledger, Git history, and explicit continuity/promotion/reconciliation procedures.

This is the current development-preservation architecture, not the production project-state database architecture.

### Q-043. When should the project move beyond Git and Markdown for development knowledge preservation?

**Status:** Open with explicit deferral criteria

Git + Markdown remains sufficient while routing, reconciliation, and consistency are manageable. More advanced infrastructure becomes justified if retrieval failures, contradictory canonical state, dependency complexity, multiple concurrent writers, or reconciliation cost become material.

### Q-048. When is the governed reusable-knowledge persistence round-trip considered closed?

**Status:** Active implementation gate

Current persisted evidence is:

```text
SQLite round-trip: PASS
PostgreSQL 18 round-trip: FAIL
```

The first PostgreSQL failure was localized to an overlong manually named migration constraint. The identifier was shortened and revalidation was triggered, but closure requires a persisted corrected PostgreSQL PASS plus removal of temporary diagnostic machinery.

Do not infer closure from the earlier production persistence slice, which tested a different scope and already passed PostgreSQL.

---

## Product interface and Project Cockpit

### Q-049. What should the primary active-work interface be?

**Status:** Strong direction established; final design not frozen

Human review through Checkpoints 117-119 strongly supports the Project Cockpit as the primary immersive active-work environment, with direct specialist project views retained as alternative entry/inspection paths.

The Cockpit should combine a living project-process projection, native system interaction, and spatial focus into real analytical workspaces.

### Q-050. How should the Cockpit scale to large projects?

**Status:** Active Specification 007 v0.2 implementation question

The next spike must demonstrate:

```text
two-dimensional project navigation
later/right and lower work remaining reachable
compact/expandable Cockpit HUD
stage orientation at the top of the operating surface
collision-safe composer/context surfaces
true browser fullscreen
fit/reset/jump navigation
keyboard-accessible recovery
architecture compatible with later semantic zoom/grouping
```

No graph/canvas framework, minimap, auto-layout algorithm, or final semantic-zoom implementation is selected yet.

### Q-051. What frontend stack and visualization system should be promoted?

**Status:** Partially narrowed, not accepted as final architecture

React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest are the current leading frontend hypothesis and have already supported the first product slices.

Formal final promotion remains open. ECharts versus Plotly remains an empirical chart comparison. Tauri remains deferred.

### Q-052. What should the final Cockpit visual identity, stage taxonomy, layout, and URL contract be?

**Status:** Open by design

The stage-zone visual grammar has been positively validated, but the final visual identity, stage taxonomy, graph/canvas library, auto-layout algorithm, semantic-zoom behavior, and public route contract remain intentionally unfrozen pending the immersive-scale spike and further human review.

---

## Evaluation, resource allocation, and stopping

### Q-013. How should analysis depth and resource budgets work?

**Status:** Open; V0 provides strong cost evidence

V0 demonstrated that explicit machinery can consume more than twice the token budget without material reliability gain. Optional depth should therefore depend on expected value, uncertainty, risk, project intent, and resource constraints while mandatory validity obligations remain mandatory.

### Q-014. How should the system decide when experimentation can stop?

**Status:** Substantially refined, not resolved

Candidate stopping reasons include sufficient evidence, decision-irrelevant residual uncertainty, diminishing information value, unavailable discriminating evidence, or compatible resource limits.

### Q-015. How should project types be characterized?

**Status:** Substantially reframed

Use multidimensional project characterization rather than one exclusive project-type label. Exact representation remains open.

### Q-016. How should system quality itself be evaluated?

**Status:** Substantially advanced; broader V1 evaluation remains open

Prototype V0 completed a preregistered held-out falsification experiment with deterministic assertions, blinded semantic judging, process/outcome separation, strong controls, and resource accounting.

V1 now also requires product/human evaluation, retrieval/horizon benchmarks, runtime bakeoffs, cross-platform gates, accessibility checks, and eventually project replay across heterogeneous real projects.

### Q-017. How should real projects become regression tests?

**Status:** Substantially advanced conceptually

Foundation 017 proposes project replay from original starting inputs. Long-term privacy-safe extraction, diversity, benchmark maintenance, and comparison criteria remain open.

### Q-029. How should analytical effort be prioritized?

**Status:** Substantially refined, not resolved

Foundation 019 provides interpretable candidate dimensions such as validity importance, information gain, downstream impact, uncertainty reduction, risk, cost, redundancy, project intent, and human preference.

No final ranking/scoring mechanism exists.

### Q-039. How should behavioral reasoning regression cases and system evaluation be designed?

**Status:** Prototype V0 completed; broader program open

The V0 synthetic churn benchmark and held-out protocol are completed historical evidence. The next evaluation program should broaden to retrieval/horizon quality, larger changing project trajectories, human-navigation burden, product usability, and project replay across project families.

---

## Prototype V0 questions retained for provenance

### Q-036. How should a new project be initialized?

**Status:** Narrow V0 mechanism answered; general product initialization remains open

V0 exposed a brief, stale README, datasets, and inherited baseline to test semantic correction. Foundation 017 and the Cockpit research now provide a richer product direction, but the production initialization workflow remains unimplemented.

### Q-040. What is the minimum end-to-end prototype that can falsify the core architecture?

**Status:** Answered for Prototype V0 and empirically resolved

Prototype V0 was implemented, run, judged, and received a strong falsification signal for the current P0 design. The question is closed for V0; future prototypes require new contracts rather than extending this one indefinitely.

### Q-041. How should Prototype V0 be represented and implemented concretely?

**Status:** Answered and historical

Foundation 011 and the completed `prototype_v0/` implementation define the frozen historical treatment architecture. It is no longer the active V1 architecture.

### Q-042. What do real B0/B1 calibration runs show, and what common baseline protocol should be frozen before P0?

**Status:** Answered for Prototype V0

The development calibration and Foundation 012 preregistration are complete historical experiment design evidence.

---

## Preservation and source integration

### Q-023. Should raw conversations be archived?

**Status:** Open and explicitly deferred

Raw transcripts may provide valuable provenance but also contain duplication, sensitive conversational context, and obsolete reasoning. The current continuity design must not depend on them.

### Q-024. How much knowledge capture should be automated?

**Status:** Open and risk-sensitive

Automatic extraction may assist routing, reconciliation, contradiction detection, or promotion proposals, but automatic extraction must never imply automatic promotion into trusted methodological or project authority.

---

## Current highest-value unresolved questions

The questions most directly attached to active V1 execution are:

```text
Q-048  close the governed PostgreSQL knowledge round-trip honestly
Q-050  prove the Cockpit's two-dimensional immersive-scale interaction
Q-044  build and evaluate production retrieval / MethodologicalHorizon construction
Q-046  execute the agent-runtime bakeoff
Q-051  determine which frontend/chart choices deserve formal promotion
```

These are bounded by existing specifications and evidence gates rather than being open-ended technology-selection exercises.
