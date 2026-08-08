# Open Questions

This document records important unresolved questions.

The purpose is to prevent promising ideas from silently becoming assumptions and to ensure that unresolved design problems remain visible across chats and checkpoints.

Questions may later be answered, split, merged, reframed, or marked obsolete. Their history should remain traceable.

## Q-001. What exactly must the system accomplish to be considered successful?

**Status:** Partially answered

The project has now established a working primary purpose: the system should create the best data-science process for the particular project, where what "best" means depends on project goals, constraints, required outputs, and desired human involvement.

The remaining work is to turn that purpose into explicit success criteria, requirements, boundaries, and evaluation standards.

Relevant dimensions still include analytical quality, reliability, reproducibility, efficiency, generality, learning value, professional output quality, autonomy, and human control.

---

## Q-002. What degree of autonomy should the system have?

Should autonomy be fixed or configurable?

Possible distinctions include:

- fully autonomous routine work;
- automatic continuation unless a defined gate is reached;
- mandatory human approval for high-impact decisions;
- project-specific autonomy settings;
- and different autonomy levels for analysis, code changes, model selection, reporting, or deployment.

---

## Q-003. What should the human's role be?

Which questions genuinely benefit from human judgment?

How should the system distinguish:

- questions it can answer through analysis;
- questions it should research;
- questions it should experimentally test;
- questions it should escalate to the human;
- and questions where several valid options should be presented rather than resolved automatically?

---

## Q-004. How should data science knowledge be represented?

Promising possibilities include reusable decision modules, rules, structured documents, schemas, graphs, executable checks, or combinations of these.

The correct abstraction has not been selected.

---

## Q-005. How should explicit knowledge interact with open-ended LLM reasoning?

A central design problem is balancing reliability and flexibility.

Too much hard-coding may become unmanageable and brittle. Too much generative reasoning may recreate the weaknesses of a one-dimensional LLM workflow.

The boundary between hard constraints, decision frameworks, and open-ended reasoning must be developed.

---

## Q-006. How should relevant investigations be activated?

If the system eventually contains hundreds of possible checks or knowledge modules, it needs an efficient way to determine which ones matter for the current project.

Questions include:

- What creates a trigger?
- Are triggers deterministic, LLM-generated, learned, or hybrid?
- Can modules activate other modules?
- How are false-negative activations detected?
- How does the system avoid running too many irrelevant investigations?

---

## Q-007. What should a reusable decision module contain?

Possible fields include:

- activation conditions;
- questions to answer;
- rationale;
- required evidence;
- relevant diagnostics;
- possible strategies;
- common failure modes;
- human gates;
- dependencies;
- outputs;
- references;
- and examples.

It is not yet known whether this should be declarative, executable, or both.

---

## Q-008. How should project state be represented?

Potential state includes:

- problem definition;
- prediction timing;
- data version;
- facts discovered about the data;
- assumptions;
- active questions;
- decisions;
- evidence;
- experiments;
- rejected alternatives;
- invalidated results;
- uncertainty;
- human input;
- and next actions.

The storage technology and schema remain open.

---

## Q-009. What agent or responsibility structure is actually useful?

The initial discussion considered roles such as problem analyst, data analyst, experiment planner, coding agent, statistical reviewer, leakage reviewer, model reviewer, and decision synthesizer.

These are conceptual responsibilities, not accepted permanent agents.

Open questions include:

- How many roles are useful?
- Which should be separate?
- Which can be temporary?
- Which should be deterministic tools rather than LLM agents?
- Should different models be used for independent viewpoints?

---

## Q-010. When is independent review required?

Not every action deserves multiple reviewers.

The project needs a risk- and value-sensitive way to decide when to use:

- a lightweight critique;
- specialized methodological review;
- independent replication;
- multiple model providers;
- or human approval.

---

## Q-011. What counts as sufficient evidence for a decision?

The system must distinguish between:

- descriptive observations;
- statistically uncertain estimates;
- cross-validation comparisons;
- robustness checks;
- causal claims;
- theoretical arguments;
- domain assumptions;
- and LLM-generated hypotheses.

Different decision types may require different evidence standards.

---

## Q-012. How should uncertainty and confidence be represented?

Should the system record confidence numerically, categorically, narratively, or through evidence structure?

How should uncertainty propagate when later decisions depend on earlier uncertain conclusions?

---

## Q-013. How should analysis depth and resource budgets work?

A quick exploratory project should not require the same process as a production-critical or research-grade project.

Possible controls include:

- named depth modes;
- compute budgets;
- time budgets;
- maximum experiment counts;
- risk levels;
- human-defined priorities;
- and adaptive stopping rules.

The current direction is that named modes may be convenient presets rather than the fundamental representation. The deeper problem is how project intent, risk, uncertainty, and expected analytical value should determine where additional effort is spent.

---

## Q-014. How should the system decide when further experimentation is no longer worth the cost?

A mature process needs stopping criteria.

Examples include diminishing expected value, stable conclusions, uncertainty below a useful threshold, insufficient data to discriminate alternatives, or resource limits.

---

## Q-015. How should different project types be characterized?

The system needs enough project characterization to route reasoning correctly without creating an impossible taxonomy.

Potential dimensions include:

- supervised versus unsupervised;
- classification versus regression;
- IID versus temporal;
- grouped or panel structure;
- sequence or spatial structure;
- ranking or recommendation;
- causal versus predictive objective;
- online or reinforcement settings;
- and structured versus unstructured inputs.

The project should avoid prematurely assuming these are mutually exclusive categories.

---

## Q-016. How should system quality itself be evaluated?

The system should eventually be compared against meaningful baselines such as:

- a strong single-LLM end-to-end workflow;
- a human-guided LLM workflow;
- manually designed project pipelines;
- and perhaps alternative agent systems.

Evaluation should examine more than final predictive performance.

Potential criteria include missed issues, leakage prevention, decision quality, reproducibility, unnecessary work, robustness, report quality, cost, and human effort.

---

## Q-017. How should real projects become regression tests for the system?

If a project teaches the system a lesson, later versions should be tested to ensure the same failure does not return.

The project needs a way to preserve cases, expected behaviors, and failure conditions without overfitting the system to a small benchmark set.

---

## Q-018. How should the system handle interaction between modules?

Data science issues are not independent.

Examples include:

- missingness interacting with validation and selection bias;
- class imbalance interacting with metrics, thresholds, and calibration;
- temporal structure interacting with leakage, validation, and feature engineering;
- feature engineering interacting with preprocessing and interpretability.

The system must support dependencies and cross-triggering without becoming an unmanageable graph.

---

## Q-019. How should invalidation work?

If a later review discovers leakage, a bad split, an incorrect assumption, or a data bug, which downstream experiments and conclusions should be invalidated automatically?

This may require explicit dependency tracking between project artifacts.

---

## Q-020. What should the execution environment look like?

The system will eventually need safe and reproducible code execution.

Open questions include isolation, dependency management, data access, compute limits, artifact tracking, random-state control, failure recovery, and reproducibility.

No execution architecture has been selected.

---

## Q-021. How should model and tool providers be selected?

The system may or may not benefit from using multiple LLM providers.

Questions include:

- whether model diversity materially improves review;
- when a stronger reasoning model is worth additional cost;
- how provider-specific capabilities should be abstracted;
- and how changing future models should affect the system design.

---

## Q-022. How should external knowledge and source material be integrated?

The project currently has access to educational and technical source material outside the repository.

The permanent approach for references, derived knowledge, provenance, licensing, updating, and retrieval has not been decided.

---

## Q-023. Should raw conversations be archived, and if so, how?

Detailed conversations can contain valuable reasoning that may not survive even a careful memo.

At the same time, raw transcripts contain duplication, outdated ideas, and noise.

The project needs to decide whether raw archives are worth maintaining and how future systems should use them safely.

---

## Q-024. How much of knowledge capture should eventually be automated?

A future system could detect proposed principles, decisions, open questions, gaps, and design hypotheses during discussion and propose repository updates.

The project first needs experience with manual curation so that automation does not preserve the wrong things or prematurely canonize speculative ideas.

---

## Q-025. What maturity model should be used for ideas and knowledge?

An early concept discussed the progression:

```text
raw thought
  -> candidate idea
  -> active design hypothesis
  -> tested on examples
  -> accepted principle or decision
  -> challenged
  -> revised or superseded
```

This seems useful, but the exact statuses and transitions have not been standardized.

---

## Q-026. How should the repository structure evolve as the project grows?

The current documentation layout is intentionally small.

Future needs may include dedicated areas for knowledge modules, project cases, experiments, evaluation suites, architecture, implementation, sources, session records, and gap logs.

These should be introduced in response to actual needs rather than speculative completeness.

---

## Q-027. What belongs in the non-negotiable methodological quality floor?

**Current priority:** Highest

The system is intended to adapt its process to project intent, but not every methodological standard should become configurable.

The project must determine which requirements should hold across all project profiles and which can legitimately vary with goals, constraints, risk, depth, and resources.

Candidate quality-floor topics include:

- train, validation, and test integrity;
- leakage prevention;
- evaluation design appropriate to intended use;
- explicit consequential assumptions;
- evidence versus speculation;
- reproducibility of consequential experiments;
- material limitations and uncertainty;
- and escalation when critical information is missing.

The exact floor has not been defined.

---

## Q-028. How should project intent be represented?

A strong design hypothesis is to distinguish at least:

- objectives;
- constraints;
- deliverables;
- human-control preferences.

The project must determine whether these categories are sufficient, how they interact, what dimensions belong under each, and how conflicts should be resolved.

It must also decide whether project-level, model-level, and operational objectives need explicit separate representation.

---

## Q-029. How should the system prioritize analytical effort?

The system should not spend resources merely because more analysis is possible.

A future prioritization mechanism may need to consider:

- relevance;
- risk if ignored;
- uncertainty reduction;
- expected information value;
- computational cost;
- human cost;
- and likely downstream impact.

The project has not decided whether this should remain qualitative, become a formal scoring system, or use another adaptive strategy.
