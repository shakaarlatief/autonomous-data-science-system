# Checkpoint 097: Post-V0 Product Vision Concretized as an Interactive Methodological Workspace

**Date:** 2026-08-19  
**Stage:** Post-Prototype-V0 system/product clarification before next architecture design

## Context

Prototype V0 is complete and strongly falsified the current P0 implementation strategy on its held-out benchmark. The project then returned to the broader system-level question rather than immediately implementing a smaller P0.

A key discussion clarified the intended end-user system in much more concrete terms.

The user described the desired experience from the perspective of starting a real data-science project such as a forecasting assessment or a broad portfolio project. Today, much of the process-navigation burden sits with the human: remembering which EDA checks exist, which statistics and visualizations might matter, which validation alternatives to consider, which model families to compare, what has already been tried, and what should be revisited later.

The intended Autonomous Data Science System should progressively take over that methodological-navigation burden while keeping the project interactive, inspectable, and professionally organized.

## Main clarification

The desired product is not:

```text
upload files -> one LLM solves everything -> final answer
```

The desired product is closer to:

```text
professional interactive project workspace
    + broad reusable methodological knowledge
    + persistent project understanding
    + recommendations and option-space navigation
    + empirical execution
    + evidence/provenance
    + living reports
    + user discussion / selection / override
```

The system should make it unnecessary for the user to repeatedly remember every useful question to ask a general-purpose LLM.

The user should still be able to remain deeply involved, inspect recommendations, browse alternatives, choose analyses, request additional depth, reject suggestions, and discuss decisions.

## EDA as the concrete reference example

EDA exposes the problem clearly.

A generic instruction such as "do EDA" or "do advanced EDA" does not define a stable or comprehensive analytical process. Different LLM runs may produce different subsets, and the user often has to manually request additional items such as:

```text
shape and schema
sample rows
variable roles and dtypes
missingness
uniqueness/cardinality
descriptive statistics
mean/median/quantiles/extremes
distributions
histograms
boxplots
correlations
subgroup comparisons
time patterns
outlier diagnostics
data-quality checks
leakage investigations
many other conditional analyses
```

The future system should instead maintain a broad methodological option space and organize it into concepts such as:

```text
baseline / near-universal analyses
recommended for this project
other applicable analyses
not currently applicable analyses
```

The user should be able to browse the full catalog when desired.

## Methodological knowledge as a system asset

The discussion sharpened the meaning of the project's long-running idea of reusable data-science knowledge.

The system should not depend solely on an LLM recalling methods from model memory. It should gradually maintain an explicit, evolving catalog of:

```text
methods
diagnostics
visualizations
tests
model families
validation strategies
feature strategies
assumptions
preconditions
alternatives
failure modes
follow-up investigations
cost / expected value
project-stage relevance
```

A method should ultimately be more than a name. It may carry purpose, applicability, prerequisites, outputs, limitations, alternatives, and relationships to other investigations.

This catalog is not literally exhaustive because data science is open-ended, but it should become broad and inspectable enough that the system's knowledge and recommendation failures can be distinguished.

## Recommendation versus catalog distinction

A useful product distinction emerged:

```text
RECOMMENDED
    what the system currently thinks deserves attention

RELEVANT OPTION SPACE
    everything currently judged applicable

FULL KNOWLEDGE CATALOG
    everything the system knows, searchable even if not recommended
```

This supports both usability and evaluation.

For example, if a useful method was omitted, the project can distinguish whether:

```text
the system did not know it;
it knew it but judged it inapplicable;
it knew it was applicable but ranked it too low;
it recommended it but the user declined it.
```

## One LLM versus one-chat misunderstanding resolved

The discussion explicitly corrected a possible misinterpretation of the V0 conclusion.

"One strong LLM reasoner" does not mean the target system becomes one prompt and one chat.

The broader system may still own:

```text
persistent project state
methodological knowledge
context selection
artifact provenance
experiment storage
execution controls
reproducibility
reports
human-interaction state
```

while one or more LLMs provide flexible reasoning where appropriate.

The number of reasoning models is not what makes the product a system.

Foundation 013 remains the governing system-level statement that the LLM is one reasoning component inside the wider system.

## Important V0 scaling lesson

The user correctly challenged any extrapolation that B1 and P0 token or reliability differences must remain linear as project complexity grows.

No such extrapolation is justified.

V0 provides observations at one benchmark complexity level, not scaling laws.

A particularly important distinction is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

A future system may retain a very large project memory while retrieving only a small relevant context for an individual reasoning decision.

Therefore P0's token failure is evidence against repeated large-state injection, not evidence against persistent project memory itself.

## Interaction model

The envisioned system can support configurable human involvement:

```text
GUIDED
system proposes, user selects, system executes

SEMI-AUTONOMOUS
system runs safe/high-confidence work and pauses at important decisions

MORE AUTONOMOUS
system proceeds under an agreed project constitution and escalates where human judgment or authority adds value
```

The product should not equate autonomy with a black-box final-answer workflow.

## Non-linear scientific process

Interface sections such as EDA, Features, Validation, Models, Experiments, Evaluation, and Report are useful for navigation, but the underlying system should remain non-linear.

Findings may reopen earlier work. A later business clarification can alter the target. Error analysis can create new EDA questions. Feature changes can require validation reruns.

The system should organize the project without forcing a rigid wizard.

## Evaluation insight

The user also clarified that mature system performance cannot always be summarized by one scalar benchmark.

A professional interactive system should be evaluated with a mixture of:

```text
quantitative coverage and precision measures
critical omissions
unnecessary recommendations
human reminder burden
human intervention burden
state-recall failures
methodological violations
repeated work
reproducibility
expert qualitative judgment
usability / navigation quality
```

A particularly promising method is **project replay**:

```text
completed historical project
    -> restore only original starting inputs
    -> let the system navigate from scratch
    -> compare what it surfaced, missed, recommended, remembered, and repaired
```

Existing completed projects can therefore become both knowledge sources and realistic regression/evaluation environments.

## Technical feasibility

The product is considered technically feasible with ordinary application technologies. Candidate implementation classes include a professional web frontend, a Python service/execution layer, durable project storage, analytical engines, isolated workers, interactive visualization, provider-neutral LLM adapters, artifact storage, and report rendering.

No stack choice is accepted yet.

Responsibilities and user experience should be specified before selecting technology.

## Promotion

The discussion is important enough to promote beyond this checkpoint.

Created:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

Foundation 017 is now the durable detailed source for:

```text
the professional interactive workspace vision;
methodological option-space navigation;
recommended vs relevant vs full-catalog views;
the role of the methodological knowledge brain;
project memory versus LLM-context separation;
configurable interaction/autonomy;
living reports;
project replay evaluation;
post-V0 product-design questions.
```

## Continuity implication

The earlier request for a standardized new-chat continuation prompt should be treated as part of project continuity rather than something the user must remember manually.

The canonical continuity procedure should contain one stable default prompt instructing a new session to reconstruct the project from repository state before changing anything.

## Next step

Do not implement a V1 architecture yet.

The immediate post-V0 discussion should continue clarifying the desired product/system contract, especially:

```text
what the professional workspace should expose;
what methodological knowledge objects should contain;
how recommendation and applicability should work;
what is automatic versus user-controlled;
what project state must persist;
how context selection should work;
how completed projects become replay evaluations;
which system responsibilities genuinely require explicit machinery beyond a strong baseline LLM workflow.
```

Only after this product target is sufficiently clear should the project choose the smallest architecture worth prototyping next.
