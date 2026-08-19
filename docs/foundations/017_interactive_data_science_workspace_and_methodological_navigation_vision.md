# Foundation 017: Interactive Data Science Workspace and Methodological Navigation Vision

**Date:** 2026-08-19  
**Status:** Foundational product and system-experience vision  
**Scope:** Long-term Autonomous Data Science System, not a commitment to a specific V1 implementation stack

## Purpose

This foundation makes the intended end-user system substantially more concrete.

The project has always aimed to move beyond a single end-to-end LLM conversation. Prototype V0 tested one narrow candidate architecture for doing so. After V0, the product vision can now be stated more directly from the perspective of an actual data-science project.

The intended system is not primarily:

```text
upload project files
    -> ask an LLM to complete the project
    -> receive one final answer
```

The intended system is closer to a **professional interactive data-science operating environment** in which the system itself carries much of the methodological memory, project memory, option generation, organization, execution discipline, documentation, and process-navigation burden that otherwise has to be repeatedly supplied by a human through prompts.

A concise statement is:

> **The system should make high-quality data-science process navigation an explicit, reusable, inspectable capability, so the user does not need to repeatedly remember what to ask an LLM, while still remaining able to inspect, discuss, select, override, and guide the project interactively.**

This foundation refines the broader system-level vision in Foundation 013. It does not replace the principle that the LLM is one reasoning component inside the system rather than the complete system itself.

---

## 1. Target user experience

A user starts a new data-science project and provides the available project sources, for example:

```text
assignment or project brief
README / documentation
datasets
existing notebooks
baseline code
business or domain documentation
other relevant artifacts
```

The system ingests these sources and initializes a project workspace.

The default experience should not be an unstructured chat that immediately tries to solve everything. Instead, the user should enter a professional project environment that makes the evolving analytical process visible and manageable.

Conceptually:

```text
+-------------------+---------------------------+--------------------+
| PROJECT           | CURRENT WORKSPACE         | SYSTEM             |
|                   |                           |                    |
| Overview          | data / analysis / plots   | Recommendations    |
| Data              | decisions / results       | Questions          |
| EDA               | interactive execution     | Warnings           |
| Validation        |                           | Alternatives       |
| Features          |                           |                    |
| Models            |                           | Discuss / Ask      |
| Experiments       |                           |                    |
| Evaluation        |                           |                    |
| Report            |                           |                    |
| Decisions         |                           |                    |
| History           |                           |                    |
+-------------------+---------------------------+--------------------+
```

This sketch is a product concept, not a fixed frontend layout.

The important property is that the interface exposes **data-science objects and project state**, not merely a prettier chat window.

---

## 2. Project initialization should create shared understanding

At the start of a project, the system should establish a concise shared understanding of:

```text
project objective
intended deliverables
prediction / inference target if applicable
important constraints
available artifacts
dataset roles
known ambiguities
important unresolved questions
initial methodological risks
```

The system should also make the raw project material directly inspectable.

For a dataset, very basic inspection should be available immediately:

```text
row count
column count
column names
sample rows
stored dtypes
inferred semantic roles
numeric / categorical / datetime / identifier candidates
missing-value counts and percentages
unique values / cardinality
duplicates
basic descriptive statistics
mean / median / quantiles / extremes
memory / file information where useful
```

The purpose is not to treat these checks as a rigid universal pipeline. They are examples of low-cost, broadly useful project orientation.

---

## 3. EDA as a concrete example of the methodological-navigation problem

Exploratory data analysis illustrates the central product problem particularly well.

Today, a user may tell a general-purpose LLM:

```text
Do EDA.
```

or:

```text
Do advanced EDA and as many tests as possible.
```

These instructions are underspecified. Different runs may surface different subsets of possible analyses. To obtain a thorough result, the human often has to remember and repeatedly prompt for specific statistics, plots, data-quality checks, relationships, diagnostics, subgroup analyses, time-based checks, missingness analyses, and other methods.

The intended system should reduce this burden.

It should know a broad option space and organize it for the current project.

A useful interaction model is:

```text
BASELINE / NEAR-UNIVERSAL EDA
    low-cost checks useful for almost every relevant tabular project

RECOMMENDED FOR THIS PROJECT
    analyses the system currently judges high-value or necessary

OTHER APPLICABLE ANALYSES
    analyses that make methodological sense but are lower priority

NOT CURRENTLY APPLICABLE
    known analyses whose prerequisites or purpose do not match the project
```

For a temporal prediction dataset, the system might recommend:

```text
temporal coverage and gaps
target distribution through time
seasonality exploration
feature distributions through time
future-information / leakage checks
entity-level longitudinal structure
train / validation / test distribution comparison
```

while retaining lower-priority options such as:

```text
outlier diagnostics
nonlinear association measures
mutual information
multivariate visualization
robust distribution summaries
```

and explicitly marking some methods as inapplicable when their prerequisites are absent.

The user should then be able to interact naturally:

```text
Run everything recommended.
Also run mutual information.
Skip clustering.
Show all outlier-analysis options.
Why did you not recommend PCA?
What still matters before we leave EDA?
```

The system therefore acts as a **methodological navigator**, not as a one-click EDA script.

---

## 4. The methodological option space should be explicit and inspectable

The phrase "all possible analyses" cannot literally mean every analysis that could ever be invented. Data science is open-ended.

The useful operational interpretation is:

> **Maintain a broad, evolving, explicit catalog of known data-science methods, diagnostics, questions, visualizations, tests, model families, strategies, assumptions, alternatives, and decision frameworks, rather than relying on an LLM to recall an arbitrary subset from parametric memory on each run.**

The catalog should be inspectable by the user.

For example, a method object for a histogram might eventually contain concepts such as:

```text
name
purpose
applicable variable types
preconditions
what it can reveal
common interpretations
failure modes
important parameters
alternatives / complements
possible follow-up analyses
cost
expected outputs
relevant project stages
```

A missing-data family might contain:

```text
missingness by variable
missingness pattern analysis
missingness versus target
missingness through time
missingness by subgroup
missingness indicators
formal missingness tests where appropriate
strategy comparisons
production-time missingness implications
```

The same principle can expand across:

```text
EDA
data quality
feature engineering
feature selection
validation
classification
regression
time series / forecasting
clustering
causal analysis
hyperparameter optimization
calibration
threshold selection
interpretability
uncertainty
robustness
diagnostics
reporting
deployment
monitoring
```

This catalog is one candidate form of the project's long-term intellectual asset: an explicit and executable representation of good data-science process knowledge.

---

## 5. Three views of methodological knowledge

Comprehensiveness should not require overwhelming the user with hundreds of options at every step.

A useful separation is:

### Recommended

What the system currently thinks deserves attention, given the project state, expected value, risk, prerequisites, and user preferences.

### Relevant option space

Everything the system currently judges applicable, including lower-priority alternatives.

### Full knowledge catalog

Everything the system knows, searchable and browsable even when not currently recommended.

This separation has an important evaluation benefit. If a useful method is absent from the recommendation, the system can distinguish among:

```text
the system did not know the method;
the system knew it but judged it inapplicable;
the system knew it was applicable but ranked it too low;
the system recommended it but the user skipped it.
```

These are different failure modes and should be improvable separately.

---

## 6. The system should not force the user to know what to ask

A central motivation can be represented as follows.

### Current human + chat workflow

```text
human remembers a possible analysis
    -> prompts LLM
    -> LLM helps
    -> human remembers another consideration
    -> prompts again
    -> human tracks what has already happened
    -> human notices what was forgotten
    -> repeat
```

### Intended system workflow

```text
project sources
    -> system understands current project situation
    -> system retrieves / activates relevant methodological option space
    -> system organizes and prioritizes possibilities
    -> user inspects, chooses, discusses, or delegates
    -> system executes
    -> evidence is preserved
    -> project state changes
    -> newly relevant possibilities are surfaced
```

The human can remain deeply involved. The difference is that the user should no longer carry the primary burden of remembering every useful next question or methodological alternative.

---

## 7. System intelligence is broader than the LLM

The target system can be thought of as several interacting forms of intelligence:

```text
METHODOLOGICAL KNOWLEDGE
methods / alternatives / tests / assumptions / applicability / failure modes
        |
        v
PROJECT UNDERSTANDING
objective / data / constraints / findings / questions / decisions
        |
        v
REASONING AND PLANNING
what matters here? what could we do? what should be recommended?
        |
        v
EXECUTION
Python / SQL / models / tools / data
        |
        v
EVIDENCE
plots / tables / metrics / diagnostics / findings
        |
        v
PROJECT STATE UPDATE
```

The LLM is valuable inside reasoning and planning, interpretation, hypothesis formation, synthesis, and open-ended judgment.

However:

```text
method catalog != LLM memory
project state != conversation transcript
experiment store != prose answer
frontend != chat shell
```

This is why a one-reasoner implementation can still be a substantial system. The number of LLMs is not the defining property.

---

## 8. Guided, semi-autonomous, and autonomous interaction should be possible

Human involvement is part of project intent rather than a binary choice.

The same system could support modes such as:

### Guided

```text
system proposes analyses and alternatives
user selects / discusses
system executes selected work
```

### Semi-autonomous

```text
system automatically performs safe high-confidence basics
system executes clearly valuable analyses
system pauses at consequential methodological or domain decisions
```

### More autonomous

```text
system operates under an agreed project constitution
system continues through routine decisions
system escalates only when human judgment materially adds value or authority is required
```

These should eventually be richer preference profiles rather than simplistic mode labels.

Autonomy does not imply that the desired product is a black box that returns only a final result.

---

## 9. Workflow sections are useful, but the underlying project is non-linear

Interface sections such as:

```text
EDA
Features
Validation
Models
Experiments
Evaluation
Report
```

are useful for organization.

They should not imply a rigid pipeline.

Real projects loop:

```text
EDA
    -> model
    -> residual / error analysis
    -> new EDA question
    -> feature revision
    -> validation rerun
```

or:

```text
business clarification
    -> target definition changes
    -> earlier EDA partially becomes stale
    -> prior model evidence must be reconsidered
```

The interface can therefore be stage-oriented while the underlying system remains question-, evidence-, claim-, and dependency-aware.

---

## 10. Project memory and LLM context are different things

Prototype V0 exposed an important scaling distinction.

A mature system may need to remember very large amounts of project information:

```text
facts
questions
experiments
findings
artifacts
decisions
rejected alternatives
provenance
evidence links
historical changes
```

That does **not** mean every reasoning call should receive all of it.

Conceptually, the system could store:

```text
10,000 facts
5,000 evidence links
500 questions
200 decisions
complete artifact history
```

while one reasoning call receives only:

```text
current objective
current decision context
three relevant questions
a few relevant findings / evidence items
one applicable methodological framework
```

The distinction is:

```text
what the SYSTEM should remember
    !=
what the LLM must see on every turn
```

This is one of the strongest architectural lessons from V0's token failure.

V0 should not be interpreted as evidence against persistent state. It is evidence against an architecture that repeatedly serializes too much persistent state into every reasoning cycle.

---

## 11. Existing reference projects can seed the methodological brain

Detailed portfolio projects and prior analyses already contain useful methodological material.

For example, a project that deliberately compares many feature-selection approaches can be transformed from a project-specific record into reusable knowledge about:

```text
filter methods
wrapper methods
embedded methods
applicability
tradeoffs
assumptions
validation interaction
computational cost
failure modes
```

The correct long-term operation is not blind copying from an old project.

It is:

```text
project-specific lesson
    -> assess generality
    -> extract reusable methodological knowledge
    -> preserve scope / assumptions / provenance
    -> activate or retrieve it in future projects when relevant
```

This makes completed projects both useful outputs and inputs to system improvement.

---

## 12. Living reporting should be part of the project environment

The system should not wait until the end to reconstruct a report from conversation history.

As work proceeds, the system should be capable of maintaining structured project outputs such as:

```text
data description
methodological decisions
EDA findings
figures and tables
experiment registry
validation rationale
model comparisons
assumptions
limitations
important rejected alternatives
final conclusions
```

A report can then be rendered into appropriate final formats without losing provenance or forcing the LLM to rediscover what happened.

The exact report architecture remains open.

---

## 13. Candidate technical architecture class

This foundation does not select a stack, but the product is feasible with ordinary modern application technologies.

A plausible implementation class is:

```text
PROFESSIONAL WEB UI
    project navigation / data tables / plots / decisions / history
        |
INTERACTION + PLANNING LAYER
    recommendations / choices / questions / discussion
        |
METHODOLOGY KNOWLEDGE LAYER
    methods / tests / assumptions / alternatives / applicability
        |
PROJECT MEMORY
    facts / findings / questions / decisions / artifacts / provenance
        |
REASONING ENGINE
    one or more LLM calls where flexible reasoning helps
        |
EXECUTION ENGINE
    Python / SQL / statistical / ML libraries / external tools
        |
PROVENANCE + EXPERIMENT STORE
    inputs / outputs / versions / metrics / evidence
        |
REPORTING / ARTIFACT LAYER
```

Illustrative technologies could include:

```text
React / Next.js / TypeScript for the interface
FastAPI or another Python service layer
PostgreSQL for durable project state
DuckDB for interactive analytical querying
pandas / Polars / NumPy / SciPy / statsmodels / scikit-learn and domain libraries
Plotly or similar interactive visualization
isolated workers / containers for heavier execution
filesystem initially and object storage later for project artifacts
provider-neutral LLM adapters
HTML / Markdown / LaTeX / PDF rendering for reports
```

These are candidate tools, not accepted architecture decisions.

Responsibilities should be designed before technologies are selected.

---

## 14. The hardest problem is methodological navigation, not execution plumbing

Many mechanical capabilities are straightforward:

```text
calculate descriptive statistics
render a dataframe
plot a histogram
train a random forest
run a hypothesis test
fit a forecasting model
```

The harder system problem is:

```text
Given everything currently known about this project:

what analyses exist?
which are applicable?
which are necessary?
which are optional but valuable?
which are redundant?
which should happen now?
which should wait?
which assumptions are not satisfied?
which alternatives should the user know about?
which findings change later decisions?
what has already been tried?
what remains unresolved?
what level of human control is desired?
when is enough evidence available to move on?
```

This is the methodological-navigation brain of the system.

The main research problem is whether this brain can become broad, reliable, adaptive, inspectable, efficient, and genuinely better than requiring the user to repeatedly steer a general-purpose LLM manually.

---

## 15. Evaluation must be broader than one scalar score

Prototype V0 appropriately used tight quantitative criteria because it tested a narrow architectural hypothesis.

The mature product requires a broader evaluation model.

Useful quantitative measures may include:

```text
important-method coverage
recommendation precision
critical omissions
unnecessary recommendations
methodological violations
human interventions required
human reminder prompts required
repeated work
state-recall failures
time to defensible decision
reproducibility failures
claim / evidence integrity
```

But some product qualities require expert qualitative judgment:

```text
Was the recommendation sensible?
Was the option space complete enough?
Did the system explain why an option mattered?
Was the project easy to navigate?
Did the system understand what mattered?
Did the user have appropriate control?
Would the workflow be credible in professional data-science work?
```

A mature evaluation program should combine deterministic checks, behavioral measures, expert judgment, replay studies, and controlled experiments rather than insisting that all system quality collapse into one number.

---

## 16. Project replay should become a major evaluation method

Completed real projects provide valuable evaluation environments.

A project replay can be constructed by taking only the original starting inputs and withholding the later human reasoning and results.

Conceptually:

```text
completed historical project
    -> recover original project inputs
    -> remove later decisions / conclusions
    -> initialize system from original state
    -> let system navigate the project
    -> compare trajectory with known project experience
```

Questions include:

```text
Did the system surface the important analyses without prompting?
Did it recommend the right subset?
Did it explain why?
Did it expose useful alternatives?
Did it identify issues that originally required manual prompting?
Did it identify useful things the original project missed?
Did it remember findings later?
Did it repair the right downstream work after changes?
How often did the user need to say "what about X?"
How often did the user need to remind it of prior state?
Was the project easier and more professional to navigate?
```

A growing replay suite across classification, regression, forecasting, causal work, NLP, and other project types can complement synthetic controlled benchmarks.

This directly supports the project's existing principle that real project failures and lessons should become reusable system knowledge or behavioral regression cases when generalizable.

---

## 17. Implication of Prototype V0 for the next stage

Prototype V0 should not lead directly to either of these conclusions:

```text
Build a smaller P0 immediately.
```

or:

```text
Abandon the system and use a strong LLM with a good prompt.
```

The product vision is now concrete enough that the next design stage should first specify the desired operating experience and intelligence responsibilities more carefully.

Before selecting the next treatment architecture, the project should clarify questions such as:

```text
What does a professional project workspace expose?
What should initialize automatically?
What is a method / analysis option in system knowledge?
How is applicability represented?
What should be recommended versus merely available?
What should run automatically versus await user selection?
How does the user inspect the full option space?
What becomes persistent project state?
What is a finding, question, decision, claim, experiment, or artifact?
How does the system decide what context the LLM receives?
How do methodological options become newly relevant after evidence changes?
How should reports evolve alongside the project?
How should guided versus autonomous behavior be configured?
How should project replay evaluate whether the system reduces human process-navigation burden?
```

Only after this product/system contract is clearer should the project decide which backend architecture best implements it.

---

## 18. Relationship to the broader system vision

Foundation 013 remains authoritative for the LLM-system-human boundary.

The current high-level relationship is:

```text
              AUTONOMOUS DATA SCIENCE SYSTEM

                     PROJECT INTENT
                          |
                          v
                 persistent project state
                          |
            +-------------+-------------+
            |             |             |
            v             v             v
       knowledge       provenance     controls
       / methods       / evidence     / boundaries
            |             |             |
            +-------------+-------------+
                          |
                          v
                 context selection
                          |
                          v
                  one or more LLMs
                          |
                          v
                  selected actions
                          |
                          v
                  execution / tools
                          |
                          v
                       evidence
                          |
                          v
                 updated project state
                          |
                          v
                 continue / stop /
                 ask human / deliver
```

The exact boxes remain hypotheses.

The product-level destination, however, is now clearer: a professional interactive environment in which the system itself carries and exposes the data-science process rather than requiring the user to rebuild that process repeatedly through prompts.
