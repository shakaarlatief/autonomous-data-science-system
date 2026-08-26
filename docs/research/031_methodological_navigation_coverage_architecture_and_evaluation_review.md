# Research 031: Methodological Navigation, Coverage, and State-Driven Evaluation Architecture

**Date:** 2026-08-24  
**Status:** Architecture and evaluation review after Specification 021 preservation  
**Authority:** Research only. This review does not freeze Specification 022, change accepted foundations, rescore Specifications 015-021, select a production ranking policy, or authorize a live experiment.  
**Design session:** 05  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 05 - Selective Context Promotion & Reasoning Vertical Slice

## Purpose

Checkpoint 185 established the next legitimate design boundary:

> Can ADS reduce the human burden of remembering and surfacing important methodological pathways across heterogeneous evolving data-science projects?

Research 030 clarified that this is not the same question as downstream disposition calibration over an action set that has already been supplied.

This review goes one level deeper. It defines the architecture and evaluation decomposition needed to test the central methodological-navigation value proposition without repeating the main limitation of Specifications 015, 019, and 021.

The central conclusion is:

```text
The next experiment should begin from project state,
not from an already enumerated methodological decision space.
```

The first successor experiment class should therefore test **state-to-methodological-horizon coverage**, with explicit decomposition of knowledge-universe coverage, retrieval/navigation coverage, applicability/missing-context handling, open-world recovery, and downstream use.

This review deliberately stops before freezing the exact benchmark, condition names, model treatment, metric thresholds, or advancement gates.

---

## 1. Starting boundary

The exact clean integration head used to start this review is:

```text
1e513241705c35dff385c485a5aa42dc54b5e434
```

Checkpoint 185 records:

```text
Specification 021      FAIL preserved
PR #66                 preservation-only merge completed
PR #55                 failed implementation closed without merge
next                    methodological-navigation / coverage architecture review
```

The clean integration head passed the applicable exact-head checks:

```text
Checkpoint metadata    32757099079  success
V1 frontend spike      32757098998  success
  Ubuntu build/tests                success
  Windows build/tests               success
  Chromium browser gate             success
  accessibility                     success
  visual regression                 success
```

The cleanup commit itself removed only the temporary Checkpoint 185 reconciliation helper files. The canonical routing state remains Checkpoint 185 with Specification 021 outcome `FAIL`.

---

## 2. The capability being tested must be stated precisely

Foundation 019 defines the methodological-navigation problem as:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Research 028 sharpens the system identity:

```text
The LLM reasons about the project.
The system owns the project.
```

The methodological-navigation layer connects those ideas:

```text
WHAT THE PROJECT IS
        ->
WHAT METHODOLOGICALLY MATTERS NOW
        ->
WHAT SHOULD ENTER REASONING AND ACTION CONSIDERATION
```

The defining user burden is not merely choosing among already-listed actions. A human data scientist repeatedly has to remember questions such as:

```text
What is one row?
What is the prediction moment?
Which features exist at prediction time?
Does validation represent deployment?
Are repeated entities handled consistently with the generalization target?
Could preprocessing leak future or held-out information?
Does missingness recur in production?
Is the chosen metric meaningful under the observed prevalence?
Do probabilities need calibration?
Has new evidence invalidated an earlier claim or decision?
```

A strong general-purpose model may know all of these concepts but still omit one in a particular project or at a particular time.

Therefore the intended system-level value is partly a **coverage and process-reliability** value proposition:

```text
important methodological path exists
    -> system can account for whether it was surfaced
    -> system can account for why it was included or excluded
    -> system can account for what remains unresolved
    -> project state changes can reactivate or stale the right concerns
```

This is stronger than ordinary prompt-response quality.

---

## 3. The architecture must preserve five separate evaluation layers

Research 030 proposed five layers. This review makes their boundaries operational.

### Layer A: Path discovery / coverage

Question:

> From project state alone, can the system surface the important methodological concerns, expert questions, methods, risks, safeguards, frameworks, and alternatives that should enter consideration?

Input should not contain the answer space.

Examples of valid outputs include:

```text
prediction-time feature eligibility
repeated-entity generalization regime
temporal validation
class-prevalence analysis
missingness-production alignment
calibration requirement
held-out-test protection
```

This is the first layer the successor experiment should target.

### Layer B: Applicability / relevance

Question:

> Once a methodological unit is surfaced, is it applicable, inapplicable, missing required context, or relevant enough to retain in the current project-specific Horizon?

The accepted three-valued applicability seam remains useful:

```text
POSSIBLY_APPLICABLE
INAPPLICABLE
MISSING_CONTEXT
```

However, broad semantic relevance remains separate from deterministic prerequisite checking.

### Layer C: Concrete option generation

Question:

> From relevant methodological concerns, can the system construct useful project-specific questions, investigations, proposals, method comparisons, or safeguards?

For example:

```text
Concern:
prediction-time feature eligibility

Possible project Question:
Are all candidate predictors available before the scoring event?

Possible Investigation:
Audit source timestamps and lineage against the prediction contract.
```

The methodological concern and the concrete project action are different objects.

### Layer D: Prioritization / disposition

Question:

> Given a concrete option set, which items should be recommended, deferred, treated as blocking, or left for later?

Specifications 015, 016, 019, 020, and 021 provide bounded evidence here. This layer should not dominate the next experiment.

### Layer E: Model-facing context value

Question:

> Given a known reasoning need, which exact knowledge revisions should be supplied to the model and does that selective context improve quality, cost, reliability, or another measured outcome?

Specifications 013 and 014 provide accepted bounded evidence here.

### Consequence

A single end-to-end score would hide failure attribution.

The architecture should be evaluated as a chain:

```text
universe coverage
    -> path discovery
    -> applicability/relevance
    -> option generation
    -> prioritization
    -> model-facing context use
```

with explicit attribution at every seam.

---

## 4. Three failure classes must never be collapsed

The most important evaluation distinction discovered in this review is:

```text
METHODOLOGICAL UNIVERSE GAP
    the relevant concern is not represented in the governed universe

NAVIGATION GAP
    the concern is represented, but the system failed to retrieve,
    activate, retain, or recognize it from the project state

REASONING / USE GAP
    the concern reached the model or downstream reasoning stage,
    but the reasoner failed to use it correctly
```

These imply different remedies.

### Universe gap

Possible remedy:

```text
knowledge engineering
source-backed addition or revision
relation/rule improvement
coverage-map expansion
```

### Navigation gap

Possible remedy:

```text
better retrieval signals
project-state summarization
relation expansion
applicability rules
semantic relevance reasoning
state-change routing
```

### Reasoning/use gap

Possible remedy:

```text
better model-facing projection
better reasoning instruction
better task decomposition
better downstream structured output
possibly a stronger model
```

A benchmark that reports only final recommendation accuracy cannot tell these apart.

---

## 5. Project state, not a prompt-written action menu, should be the primary experimental input

Foundation 018 already provides the conceptual project-object vocabulary required to construct architecture-representative state without building the entire future platform first.

A first benchmark can use synthetic but object-model-aligned project-state snapshots containing selected instances of:

```text
Objectives
Constraints
Deliverables
HumanPreferences
Definitions
Datasets
Variables
Questions
Assumptions
Findings
Claims
Decisions
Artifacts
Relations
Events
```

The state should contain project facts and history, not evaluator answers.

The main reasoner input should not include:

```text
explicit requested reasoning-function labels
oracle methodological stable keys
candidate methodological concern menu
candidate action menu
expected dispositions
hidden evaluator relations
```

This is the principal difference from Specification 021.

---

## 6. The correct benchmark unit is an evolving ProjectStateEpisode

A static microstate is useful for unit testing but insufficient for the long-term value proposition.

The benchmark unit should conceptually be:

```text
ProjectStateEpisode
    episode_id
    project objective / intended use
    snapshot_0
    state transition 1
    snapshot_1
    state transition 2
    snapshot_2
    ...
```

Each transition introduces, resolves, supersedes, or invalidates project facts.

Example:

```text
SNAPSHOT 0
binary churn prediction objective
basic tabular dataset

TRANSITION 1
future scoring objective clarified
monthly timestamp identified

TRANSITION 2
customer IDs shown to repeat

TRANSITION 3
positive prevalence found to be 4%

TRANSITION 4
three candidate features found to be populated after scoring time
```

Expected methodological behavior should change over the episode.

This enables evaluation of:

```text
newly activated concerns
correctly retired concerns
missing-context questions
stale recommendations
revalidation triggers
how quickly important paths appear after the triggering evidence exists
```

---

## 7. Re-navigation should first be tested by recomputation, not by incremental orchestration complexity

The long-term system should react to project-state changes. That does not imply that the first experiment needs a complex incremental event-routing engine.

The first architecture-representative test can deliberately use:

```text
snapshot changes
    -> recompute navigation from the current authoritative state
```

rather than:

```text
maintain a complex incremental frontier of affected nodes
```

Why:

1. the scientific question is whether the methodological paths can be surfaced from state;
2. full recomputation makes failures easier to attribute;
3. the benchmark will be small enough that efficiency is not the primary concern;
4. Prototype V0 already warned against premature orchestration complexity.

Incremental affected-neighborhood routing should be justified later only if recomputation becomes operationally expensive or introduces another measured problem.

---

## 8. The first successor benchmark needs a broader evaluation universe than the current ten-asset stress fixture

The current ten assets are:

```text
bagging
class-imbalance
ecdf
gradient-boosted-trees
histogram
missing-data
prediction-moment
prediction-time-feature-eligibility
random-forest
temporal-validation
```

They were deliberately useful for representation, retrieval, Horizon, selective-context, and recommendation experiments.

They are not sufficient to test broad process-navigation coverage.

A useful successor benchmark requires a controlled but more representative methodological micro-universe covering several lifecycle neighborhoods, for example:

```text
problem and target definition
unit of observation / dataset structure
prediction moment and feature availability
data leakage
missingness and data-quality regimes
class imbalance and metric selection
validation design
repeated-entity generalization
preprocessing isolation
model-family comparison
calibration / probability quality
threshold selection
final-test protection
uncertainty / subgroup robustness
```

The goal is not to build the full long-term knowledge universe before the experiment.

A reasonable first design should contain enough assets to create:

```text
relevant items
near-neighbor distractors
cross-cutting relations
inapplicable items
missing-context items
method alternatives
hard safeguards
question templates
```

while remaining small enough to audit manually.

The exact size should be chosen during Specification 022 design, not here.

---

## 9. Knowledge-universe construction and benchmark truth must be independently governed

A serious leakage risk exists if benchmark expected paths and treatment knowledge are authored as the same object at the same time.

The successor design should separate:

```text
TREATMENT METHODOLOGICAL UNIVERSE
    what ADS is allowed to know and navigate

EVALUATION COVERAGE ORACLE
    what the benchmark says materially matters in each state
```

They may reference the same canonical concepts, but the benchmark should not simply equate "present in the treatment catalog" with "expected answer."

A concern can be:

```text
represented and expected
represented but not expected in this state
not represented but expected
```

The third case is essential because it exposes a **catalog gap** instead of incorrectly blaming retrieval.

The source-backed knowledge-engineering principles in Research 028 remain applicable. The controlled universe should be frozen before provider execution and should not be strengthened after inspecting model failures.

---

## 10. The benchmark needs a hidden CoverageOracle, not a visible candidate menu

For each episode and snapshot, the benchmark should maintain a hidden oracle containing conceptually:

```text
CoverageOracleItem
    oracle_id
    canonical methodological concern
    importance class
    first_valid_snapshot
    last_valid_snapshot or resolution rule
    representable_by_stable_keys[]
    acceptable semantic variants[]
    expected applicability state
    missing-context question when applicable
    rationale
```

Possible importance classes might distinguish:

```text
CRITICAL_VALIDITY
HIGH_VALUE
USEFUL
OPTIONAL
```

Exact labels are not frozen.

The reasoner must never receive these oracle identities, importance labels, expected snapshot ranges, or evaluator rationales.

The oracle exists only for scoring and failure attribution.

---

## 11. Coverage must be evaluated semantically, not by exact wording alone

Open-ended methodological discovery cannot reasonably require one exact sentence.

For example, these may express the same path:

```text
check whether predictors are available at scoring time
verify prediction-time feature eligibility
audit feature availability against the prediction moment
```

Evaluation should therefore combine:

```text
canonical aliases / deterministic normalization where possible
blinded semantic matching where necessary
strict project-fact grounding
```

Semantic matching should determine whether an output covers an oracle concern, not whether the evaluator personally prefers the wording.

The semantic matcher/judge must not know treatment condition.

---

## 12. Path-discovery metrics should emphasize critical omissions and reliability

Average semantic quality is insufficient for Question A.

Candidate Layer-A measurements include:

```text
critical-path recall
weighted methodological coverage recall
per-episode minimum coverage
number of critical omissions
number of repeated omissions across repetitions
false activation / irrelevant concern count
coverage precision or noise ratio
newly-activated-path recall
retired-path persistence errors
```

A particularly important system-value metric is **worst-case omission reliability**.

If GENERIC and ADS have similar mean coverage but ADS substantially reduces the probability that one critical concern is forgotten, that may be meaningful value.

This is consistent with the product rationale: explicit system memory may be useful because a strong model already knows the concept but does not surface it reliably on every run.

---

## 13. Evolving episodes enable a time-to-surface metric

A state-driven system should surface a concern after the evidence that activates it becomes available, not three stages later.

For every oracle concern with an activation snapshot, define conceptually:

```text
surface_latency
    = first snapshot where concern is surfaced
      - first snapshot where concern is validly activated
```

Desired behavior:

```text
critical concern      low latency
not-yet-applicable    no premature activation
resolved concern      retires or changes status appropriately
```

This metric directly tests dynamic methodological navigation rather than one-shot recall.

---

## 14. Applicability and missing context need their own scoring

A high-recall system can become useless if it surfaces every possible method all the time.

Layer B should therefore measure at least:

```text
applicable concern retained
inapplicable concern excluded or explicitly rejected
missing-context concern preserved as unresolved
correct missing-context question surfaced
known negative evidence not collapsed into unknown
unknown not collapsed into false
```

The accepted Specification 012 distinction remains valuable:

```text
UNKNOWN != FALSE
```

The successor benchmark should extend this into more realistic project-state contexts without assuming that all semantic applicability can become deterministic.

---

## 15. Concrete option generation should be downstream of concern discovery

The first successor experiment should not require exact action menus as its primary input.

However, once a concern is surfaced, ADS should eventually be able to instantiate project objects such as:

```text
Question
Proposal
Investigation
Constraint
```

Examples:

```text
Concern:
class imbalance

Question:
What is positive prevalence overall and through time?

Concern:
validation realism

Proposal:
Compare chronological holdout and rolling-origin designs against the intended deployment cadence.
```

Layer C evaluation should later ask whether generated actions are:

```text
project-specific
grounded
non-duplicative
sufficiently complete
appropriately scoped
traceable to the concern and project evidence
```

This should not be collapsed into Layer-A coverage in the first experiment.

---

## 16. The generic control must be genuinely strong

The relevant comparison is not ADS versus a weak model that is told to do little.

A strong generic control should receive:

```text
same authoritative project state
same project objective and constraints
same common instruction to identify important methodological concerns
same output budget
same model
same reasoning effort
same repetition structure
no hidden evaluator hints
```

The generic model should be allowed to use its normal parametric methodological knowledge.

If ADS cannot provide measurable value against that baseline, the extra machinery has not earned its complexity for the tested seam.

---

## 17. Provider-call budget must be matched or explicitly accounted for

A future treatment may use an LLM inside the navigation stage itself.

If ADS receives extra model calls while GENERIC receives one call, observed gains could be caused by additional compute rather than by the explicit methodological system.

The first successor experiment should therefore prefer a treatment that can be built from already accepted non-provider navigation primitives:

```text
canonical project-state projection
    -> lexical / hybrid retrieval
    -> governed relation expansion
    -> deterministic applicability/context checks
    -> explained Horizon
    -> one strong reasoner call
```

with GENERIC using the same reasoner call budget.

If later experiments add a model-based state-to-needs or semantic navigation call, the generic control should receive a matched opportunity such as a reflection/second-pass call or the experiment should explicitly treat extra compute as part of the system intervention.

---

## 18. A diagnostic ORACLE_HORIZON condition would improve failure attribution

A future experiment may benefit from a third **diagnostic upper-bound** condition conceptually like:

```text
ORACLE_HORIZON
```

It would receive the exact benchmark-relevant methodological concerns or exact knowledge revisions for the current state, but not the evaluator's desired prose or actions.

Its purpose would not be to compete with ADS as a practical architecture.

Its purpose would be diagnostic:

```text
ADS misses concern, ORACLE_HORIZON succeeds
    -> navigation is likely the bottleneck

ADS and ORACLE_HORIZON both fail downstream
    -> downstream reasoning/use is likely the bottleneck
```

The exact inclusion of this condition should be decided during specification design.

---

## 19. The system should retain an open-world escape hatch

Foundation 019 explicitly states that the methodological brain should remain open-world.

A curated universe is a defense against omission, not a declaration that unrepresented concerns do not exist.

The reasoner should therefore be allowed to say, conceptually:

```text
Important concern not represented in the supplied Horizon:
...
```

Evaluation should distinguish:

```text
catalog-represented concern recovered through navigation
catalog-gap concern recovered through open-world reasoning
catalog-gap concern omitted entirely
```

Repeated useful open-world discoveries can later become governed candidate knowledge additions.

This preserves the learning loop:

```text
novel useful concern
    -> candidate knowledge gap
    -> source-backed review
    -> accepted revision when justified
```

---

## 20. Coverage accounting should become a system object or derived ledger, not merely prompt text

A mature ADS should be able to answer:

```text
Which important methodological concerns are currently represented?
Which are applicable?
Which are unresolved?
Which were explicitly ruled out?
Which have supporting evidence?
Which were resolved?
Which became stale after a project-state change?
Which expected area has no knowledge coverage?
```

This suggests a project-side **coverage ledger** or derived navigation projection.

It need not become a new fundamental Foundation-018 durable object family immediately.

A first implementation could be a recomputable view keyed by:

```text
project snapshot
knowledge revision
navigation evidence
current applicability/relevance status
project objects that address the concern
```

The distinction matters:

```text
methodological knowledge asset
    !=
project-specific coverage status
```

The former is reusable global knowledge. The latter is a current project interpretation.

---

## 21. Candidate benchmark episode families

The exact cases must be prospectively authored and frozen later. This review recommends heterogeneity rather than another set of narrowly similar microstates.

### Episode family 1: future binary prediction

Possible evolving facts:

```text
future churn objective
timestamp discovered
repeated customer entities
strong class imbalance
prediction-time feature mismatch
production missingness differences
```

Methodological neighborhoods:

```text
prediction moment
feature availability
temporal validation
repeated-entity generalization
class prevalence / metrics
missing-data production alignment
```

### Episode family 2: static tabular prediction without temporal deployment

Purpose:

```text
test that temporal methods are not activated merely because a date-like field exists
test ordinary leakage and validation concerns without forcing temporal semantics
test model/preprocessing relevance under genuinely static deployment
```

This is important for false-activation control.

### Episode family 3: probability-sensitive decision problem

Possible facts:

```text
ranked risk decisions
probability estimates used operationally
asymmetric error costs
threshold choice occurs after model comparison
```

Methodological neighborhoods:

```text
probability calibration
proper scoring rules
threshold selection
cost-sensitive evaluation
held-out selection boundaries
```

### Episode family 4: data-quality and measurement shift

Possible facts:

```text
missingness regime changes
new data-collection system introduced
subgroup-specific measurement differences
```

Methodological neighborhoods:

```text
missingness characterization
distribution shift
measurement validity
subgroup robustness
revalidation
```

The final benchmark should include both positive activation and deliberate non-activation cases.

---

## 22. Human burden should be represented through omission without cueing, not through a subjective survey alone

The central user problem is that the human currently has to remember to ask.

A useful experimental proxy is therefore:

```text
How many important concerns appear without any explicit human cue naming them?
```

The benchmark should intentionally avoid prompts such as:

```text
consider leakage
consider class imbalance
think about temporal validation
```

Those are exactly the cues ADS is intended to reduce the need for.

Additional human-facing evaluation can later measure:

```text
perceived usefulness
noise
explainability
trust
navigation clarity
```

but the first system-value benchmark should focus on whether the important path is surfaced at all.

---

## 23. Value may appear as lower variance and fewer catastrophic omissions, not higher average prose quality

A strong model may already produce high average-quality methodological reasoning.

Therefore the successor experiment should not require ADS to produce obviously more sophisticated prose.

Potential system value includes:

```text
higher critical-path recall
lower critical omission rate
lower between-repetition variance
faster activation after state changes
better missing-context recognition
better auditability of why something was omitted
stable exact knowledge provenance
```

This is a more architecture-representative hypothesis than "does adding two knowledge paragraphs make the model's recommendation rationale score higher?"

---

## 24. Noise and expansion remain real risks

A broad methodological universe can create a different failure mode:

```text
everything looks relevant
```

The benchmark must therefore penalize:

```text
irrelevant path activation
premature concerns
persistent resolved concerns
unbounded method expansion
duplicate or near-duplicate suggestions
unnecessary model-family sprawl
```

Coverage without control is not success.

The desired behavior is:

```text
high recall on materially important paths
    +
controlled current Horizon size
    +
inspectable exclusion/missing-context rationale
```

---

## 25. Recommended first successor experiment class

This review recommends that the next frozen experiment, if accepted after review, should be a bounded **Project-State-to-Methodological-Horizon Coverage Diagnostic**.

Its primary question would be conceptually:

> Given realistic heterogeneous project-state snapshots with no explicit methodological answer menu, does the ADS navigation path improve reliable coverage of important represented methodological concerns relative to a strong generic reasoner, without unacceptable irrelevant expansion, while correctly exposing catalog gaps and missing context?

The exact wording is not frozen.

The first experiment should primarily test Layers A and B:

```text
A. path discovery / coverage
B. applicability / missing context
```

Layer C may be observed descriptively but should not become the main advancement gate yet.

Layers D and E already have separate bounded evidence programs and should remain separately attributable.

---

## 26. Candidate treatment shape

A plausible first treatment path is:

```text
Foundation-018-aligned project state
    -> canonical state summary / retrieval query projection
    -> accepted retrieval seam
    -> accepted-current relation expansion
    -> deterministic applicability / context requirements
    -> explained MethodologicalHorizon
    -> strong LLM synthesis of current methodological concerns
    -> optional open-world gap check
```

A plausible generic control is:

```text
same project state
    -> same strong LLM
    -> direct open-ended methodological concern discovery
```

The exact system-side query construction is a design problem that must be frozen before implementation. It must not secretly encode the oracle concern list.

---

## 27. What should not be built before this experiment

Do not prematurely add:

```text
large graph databases
recursive project frontier machinery
complex event-driven incremental re-navigation
final production ranking model
final production disposition enums
multi-agent specialist routing
thousands of knowledge assets
automatic project mutation
automatic execution from navigation output
```

The first goal is to test whether explicit system-side methodological navigation earns its complexity on the upstream coverage seam.

---

## 28. What can be reused

Accepted components that can likely be reused without reopening them include:

```text
Foundation 018 project-object semantics
Foundation 020 knowledge-asset/revision semantics
accepted-current governed knowledge reads
lexical / hybrid retrieval evidence
one-hop relation expansion
three-valued applicability / missing-context handling
explained MethodologicalHorizon
exact revision provenance
ADS-owned ReasoningRuntime
provider-free and governed live-experiment discipline
```

The new work is the seam between realistic project state and those navigation primitives.

---

## 29. Questions that must be answered before Specification 022 is frozen

The next specification should not be frozen until the project deliberately decides:

```text
1. What exact project-state projection is visible to both conditions?
2. What size and methodological breadth should the controlled evaluation universe have?
3. How is the hidden coverage oracle constructed independently from treatment knowledge?
4. What is the first-condition set: GENERIC vs ADS only, or also ORACLE_HORIZON?
5. How are semantically equivalent concerns matched to oracle items?
6. How are catalog gaps scored separately from navigation failures?
7. How is irrelevant expansion penalized?
8. Which concern classes receive strict zero-tolerance omission treatment, if any?
9. How many evolving episodes and repetitions are needed for meaningful reliability evidence?
10. Does the first treatment use only non-provider navigation before one reasoner call, or include an LLM navigation call with matched compute controls?
11. What is descriptive only versus advancement-gating?
12. What outcome should represent safe but non-differentiated coverage performance?
```

These are specification questions, not implementation details.

---

## 30. Review conclusion

The Specification 021 `FAIL` does not motivate another supplied-action recommendation benchmark.

It motivates moving the experiment boundary upstream.

The most architecture-representative next question is:

```text
PROJECT STATE
    -> can ADS discover and account for the methodological paths
       that a strong generic model might know but inconsistently surface?
```

The preferred evaluation decomposition is:

```text
UNIVERSE COVERAGE
    -> NAVIGATION COVERAGE
    -> APPLICABILITY / MISSING CONTEXT
    -> OPTION GENERATION
    -> PRIORITIZATION
    -> MODEL-FACING CONTEXT VALUE
```

The first successor experiment should isolate the first two layers as much as possible, use evolving project-state episodes, retain a strong generic control, expose catalog gaps separately, preserve open-world reasoning, and measure reliability/critical omissions rather than only average semantic quality.

Specification 022 remains **not frozen** at the end of this review.