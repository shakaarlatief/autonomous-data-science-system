# Decisions

This document records explicit project-level decisions that have already been made.

A decision is stronger than an idea or design hypothesis. Decisions may still be revised later, but revisions should be explicit and should preserve the history of what changed and why.

## D-001. Create a dedicated project separate from individual data projects

**Status:** Accepted  
**Date:** 2026-08-07

The Autonomous Data Science System is maintained as its own project rather than inside the existing collection of individual data projects.

### Rationale

The system sits conceptually above individual projects. Individual projects may later be used to test, develop, and improve the system, but they are not the same artifact.

---

## D-002. Use a dedicated GitHub repository as the persistent home of the project

**Status:** Accepted  
**Date:** 2026-08-07

The repository `autonomous-data-science-system` is the persistent home of the project.

### Rationale

A project of this scope cannot safely depend on long chat histories or model memory. Version-controlled files provide durable state, provenance, history, and a way for future sessions or models to reconstruct the project.

---

## D-003. Keep the repository private for now

**Status:** Accepted  
**Date:** 2026-08-07

The repository is private during the early design stage.

### Rationale

The project is highly exploratory and many ideas are intentionally provisional. Public presentation can be reconsidered once the structure and goals are more mature.

---

## D-004. Treat chat as the design workspace and the repository as the source of truth

**Status:** Accepted  
**Date:** 2026-08-07

Free-form discussion can continue in chat, but stable project knowledge must be extracted into repository artifacts.

### Rationale

Chat is effective for exploration but unreliable as permanent project memory. Repository artifacts make continuity deliberate rather than accidental.

---

## D-005. Preserve important knowledge at multiple levels of detail

**Status:** Accepted  
**Date:** 2026-08-07

The project will preserve both concise canonical knowledge and detailed foundational reasoning.

### Rationale

Aggressive summarization can destroy important motivations, examples, distinctions, and reasoning. Keeping only raw conversations creates the opposite problem: too much unstructured material for efficient future use.

The current solution is layered preservation.

---

## D-006. Foundational design memos are first-class project artifacts

**Status:** Accepted  
**Date:** 2026-08-07

Important early discussions may be reconstructed into long-form design memos rather than compressed into only short principles or decisions.

### Rationale

Some of the earliest reasoning defines the intellectual foundation of the project. The reasoning itself may later be needed to challenge, revise, or understand an architectural choice.

---

## D-007. Historical conversation material is not automatically canonical

**Status:** Accepted  
**Date:** 2026-08-07

If raw conversations are archived later, they will be treated as historical provenance rather than the authoritative current specification.

### Rationale

Conversations contain speculative ideas, repetition, abandoned directions, and statements that may later become outdated.

---

## D-008. Establish an explicit new-chat continuity procedure

**Status:** Accepted  
**Date:** 2026-08-07

The project must support continuing in a new chat when the current conversation becomes too long or otherwise unusable.

A new session should reconstruct state from repository documents rather than requiring the user to manually explain the previous conversation.

### Rationale

Chat capacity is a predictable limitation and should be designed around from the beginning.

See `CONTINUITY.md`.

---

## D-009. Use checkpoints rather than trying to document every message immediately

**Status:** Accepted  
**Date:** 2026-08-07

Discussion should remain fluid. After substantial progress, a checkpoint should consolidate stable knowledge, detailed reasoning where necessary, open questions, and the next continuation point.

### Rationale

Updating many project files after every message would create excessive overhead and interfere with exploration. Checkpoints provide a practical balance between preservation and conversational flow.

---

## D-010. Treat the documentation methodology as provisional

**Status:** Accepted  
**Date:** 2026-08-07

The current repository structure and knowledge-preservation method are version 0.1, not a final architecture.

### Rationale

The project is expected to discover better ways to organize knowledge through actual use. The methodology for building the system should evolve in the same evidence-driven way as the target system.

---

## D-011. Do not select the implementation architecture yet

**Status:** Accepted  
**Date:** 2026-08-07

The project will not yet choose an agent framework, number of agents, LLM providers, orchestration framework, database, graph technology, rule engine, execution architecture, or other implementation stack.

### Rationale

Selecting technology before the system's goals, requirements, reasoning model, and evaluation criteria are sufficiently understood would create premature constraints.

---

## D-012. Do not attempt to design one complete fixed workflow for all data science projects

**Status:** Accepted at the conceptual level  
**Date:** 2026-08-07

The project rejects the idea that one globally fixed linear pipeline can adequately represent all data science projects.

### Rationale

Different projects require different questions, validation designs, assumptions, analyses, and modelling approaches. Findings discovered later may also require returning to earlier stages.

This decision does not yet specify the final alternative architecture.

---

## D-013. Use real projects to develop and test the system

**Status:** Accepted  
**Date:** 2026-08-07

Real or realistic data projects will be used as coverage tests for the system.

### Rationale

Trying to enumerate the complete universe of data science reasoning in advance is unlikely to succeed. Projects can expose missing questions, weak branches, unnecessary work, bad assumptions, and interactions that were not anticipated.

---

## D-014. Generalize project lessons when appropriate

**Status:** Accepted  
**Date:** 2026-08-07

When a project exposes a missing capability or reasoning failure, the system should determine whether the lesson is generalizable. If so, it should be incorporated into reusable system knowledge or process rather than patched only in that project.

### Rationale

This turns each project into both an analytical task and a source of system improvement.

---

## D-015. Keep the currently attached learning materials outside the repository for now

**Status:** Accepted for the current stage  
**Date:** 2026-08-07

The machine learning and time-series/econometrics source materials currently available in the ChatGPT project are not being copied into the GitHub repository yet.

### Rationale

The project has not decided how external knowledge sources, course material, references, or derived knowledge modules should be stored permanently. Copying material now would prematurely define a source architecture.

---

## D-016. Create Checkpoint 0 before continuing deeper system design

**Status:** Accepted and executed  
**Date:** 2026-08-07

The first repository artifacts capture the state reached during the initial design conversation before continuing to the next conceptual question.

### Rationale

The initial conversation already contains foundational ideas that should not be allowed to disappear as the chat grows.

---

## D-017. Define the primary purpose in project-relative terms

**Status:** Accepted  
**Date:** 2026-08-08

The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.

The project therefore does not define maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed as the universal objective of the system.

### Rationale

Different projects legitimately require different balances. A research project, production project, rapid exploratory analysis, learning-focused portfolio project, and high-stakes analytical project should not all optimize the same process characteristics.

Autonomy and predictive performance remain important capabilities, but they are means that should serve project intent rather than universal ends.

This decision does not yet define the exact project-intent schema or the non-negotiable methodological standards that must hold across all project profiles.

---

## D-018. Make checkpoint detection a proactive AI responsibility

**Status:** Accepted  
**Date:** 2026-08-08

The AI design collaborator should decide when repository preservation or a checkpoint is warranted during an active design conversation. The user should not need to request every update manually.

The AI should preserve material when substantial conceptual progress, a major transition, continuity risk, or another natural checkpoint makes preservation more valuable than further uninterrupted discussion.

### Rationale

The user should be able to focus on the substance of the project rather than on remembering when documentation maintenance is due. The repository is intended to protect the project from conversational loss, so the design collaborator should actively manage that continuity risk.

This does not authorize automatic promotion of ideas into accepted decisions. Maturity distinctions must still be respected.

See `DEVELOPMENT_METHOD.md` version 0.2.

---

## D-019. Use numbered, content-specific design-session names

**Status:** Accepted  
**Date:** 2026-08-08

Chats inside the `Autonomous Data Science System` ChatGPT project use the convention:

```text
NN - Main Topic / Stage
```

The sequence number preserves chronology and the content-specific title makes earlier sessions easier to locate.

### Rationale

A purely numbered convention becomes difficult to navigate as the project grows, while completely free-form names obscure chronological order. The hybrid convention provides both.

Session names are provenance and navigation metadata only. The repository must not depend on a chat retaining a specific title, and a single chat may contain multiple repository checkpoints.

---

## D-020. Make design-chat rotation a proactive AI responsibility

**Status:** Accepted  
**Date:** 2026-08-08

The AI design collaborator should decide when the active design conversation should move to a new chat. A new chat should be opened primarily because conversation capacity, context pressure, degraded continuity, or another practical session-boundary risk makes continuing in the current chat unsafe or inefficient, not merely because the conceptual subject changes or a new checkpoint is reached.

A single chat may therefore span many topics and many repository checkpoints when continuity remains healthy.

Before recommending a new chat, the AI should normally ensure that material reasoning has been preserved, `CURRENT_STATE.md` and the relevant canonical documents are current, and the next step is explicit. It should then give the user a suitable numbered, content-specific chat title and a minimal continuation instruction. The user should not need to manually reconstruct or re-explain the project.

The AI does not need an exact client-side context-limit meter to perform this responsibility. It should use the conversational context and continuity signals available to it and recommend rotation before meaningful context loss is likely. If a platform-specific limit becomes ambiguous and cannot otherwise be assessed, the AI may ask the user for relevant UI information, but screenshots should not be a routine requirement.

### Rationale

The goal of session management is reliable continuity, not creating many chats. Topic changes and checkpoints are useful documentation boundaries but are not, by themselves, reasons to fragment the working conversation. Proactive session rotation reduces the risk of reaching a context boundary unexpectedly and then requiring the user to recover the project manually.

See `CONTINUITY.md`.