# Checkpoint 105: Refined Knowledge Representation Second Stress Test

**Date:** 2026-08-20  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 methodological-navigation and reusable-knowledge design  
**Scope:** Stress-tests the refined representation from Checkpoint 104 against the original five examples plus a new class-imbalance concern, with concrete rule, component, project-object, and derived-view behavior.  
**Authority:** Historical provenance and active design evidence. The test supports promotion of a conceptual representation direction but does not define a final ontology, schema, rules engine, persistence model, or V1 implementation.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## Why this checkpoint exists

Checkpoint 104 found that the first candidate representation from Checkpoint 102 did not survive unchanged. In particular, it introduced the need to test:

```text
intrinsic asset kind versus reasoning function
Asset -> Component -> NarrativeFacet granularity
stable semantic relations versus conditional methodological rules
separate retrieval/applicability/context layers
project Criterion Findings instead of a new Assessment object
revision-level provenance
```

The required second pass is now complete.

The test re-encodes:

```text
Histogram
Missing-data investigation
Temporal validation
Random Forest
Prediction-time feature eligibility
```

and adds a deliberately new concern:

```text
Class imbalance
```

The purpose is to determine whether the refined model generalizes beyond the examples that produced it.

---

## 1. Refined primitives used in this test

The test uses the following conceptual primitives without selecting physical schema syntax.

### KnowledgeAsset revision

```text
stable asset identity
revision identity
intrinsic kind
purpose
scope
governance/maturity
provenance
optional reasoning functions/traits
optional retrieval profile
optional applicability specification
optional context requirements
components
```

The provisional intrinsic kinds used in the test are:

```text
CONCEPT
METHOD
FRAMEWORK
QUESTION_TEMPLATE
RULE
INVESTIGATION_PATTERN
```

The exact taxonomy remains open.

### KnowledgeComponent

A component has stable identity within an owning asset when independent provenance, relation targeting, challenge, or revision semantics are useful but independent global retrieval is not.

Examples:

```text
method mechanism component
configuration-semantics component
interpretation-rule component
framework-local conditional rule
framework-local resolution guidance
```

### NarrativeFacet

Narrative explanation remains unaddressed prose when independent identity is not useful.

### KnowledgeRelation

A relation expresses a relatively stable semantic relationship such as:

```text
IS_A
PART_OF
ALTERNATIVE_TO
COMPLEMENTS
GOVERNED_BY
REQUIRES_CONCEPT
CAN_SATISFY
```

A relation may carry scope/conditions when the relationship itself is context-dependent, but it does not encode a procedural consequence.

### Conditional KnowledgeRule

A rule expresses guarded methodological reasoning conceptually as:

```text
WHEN
    condition expression

THEN
    activate / require / recommend / deprioritize /
    constrain / interpret / request clarification /
    require revalidation

FORCE
    hard validity
    strong guidance
    heuristic guidance
    informational

UNKNOWN BEHAVIOR
    ask
    defer
    block dependent claim/action
    make no inference

RATIONALE / SCOPE / PROVENANCE
```

Rules can be independent `RULE` assets or components inside another asset.

### Project knowledge references

Project Questions, Findings, Claims, Proposals, Investigations, Runs, Evidence, Constraints, and Decisions retain references to the knowledge asset/revision/component that influenced them where material.

### Criterion Finding

A structured Finding subtype/facet is used for subject-specific criterion verdicts:

```text
subject
criterion knowledge revision
verdict
conditions
supporting evidence
rationale
```

Unresolved state remains a Question rather than a fake verdict.

---

## 2. Missing Data full navigation reconstruction

The external `Missing_Data.md` artifact is used as the hardest branching specimen.

The tree begins by asking what is missing and then separates feature missingness from target-label missingness. Within feature missingness it branches on feature retention, production missingness, evaluation cleanliness, semantic variable type, row-removal consideration, and missingness uniformity. Within target missingness it separates training-label and test-label problems.

The reconstruction below shows that the tree can be generated without storing one monolithic workflow.

### Framework

```text
asset: framework.missing_data
kind: FRAMEWORK
purpose:
    organize reasoning about missing feature values and missing labels
    in relation to intended use, evaluation, treatment, and claims
```

### Reusable concepts

```text
concept.missing_feature_value
concept.missing_target_label
concept.production_missingness
concept.semantic_variable_type
concept.missingness_pattern
concept.clean_evaluation_sample
concept.complete_case
```

These concepts provide stable semantic targets for project facts and questions.

### Root question templates

```text
Q1  What is missing: feature values or target labels?
Q2  Is the affected feature worth keeping?
Q3  Can feature values be missing during intended production use?
Q4  Can validation/test data represent clean intended production?
Q5  Is row removal being considered?
Q6  Is missingness approximately uniform over relevant structure?
Q7  Is the feature semantically categorical or numerical?
Q8  Are target labels missing in training or evaluation data?
```

These instantiate ordinary Foundation 018 project `Question` objects.

### Cross-cutting legitimacy rule

The tree repeatedly relies on the principle that learned preprocessing should be fitted only from legitimate training information.

That rule is not owned exclusively by Missing Data:

```text
asset: rule.learned_preprocessing_training_information_only
kind: RULE
functions:
    hard validity constraint
    information-legitimacy safeguard

WHEN
    a preprocessing/imputation mechanism learns from data

THEN
    restrict fitting information to the legitimate training information set

FORCE
    hard validity
```

`framework.missing_data` is `GOVERNED_BY` this rule.

### Strategy and method references

The attached tree contains options such as:

```text
feature removal
row removal
mean imputation
median imputation
mode imputation
missing category
model-based imputation
missingness indicator
native missing-value model handling
training on labeled examples
missing-label prediction
semi-supervised learning
```

The representation does not require all of these to share one intrinsic kind.

For example:

```text
mean/median/mode imputation
    -> likely METHOD

row removal / feature removal
    -> likely ACTION or INVESTIGATION/decision pattern semantics
       represented provisionally through reusable strategy functions
       on a Pattern or Rule rather than forcing them into METHOD

native missing-value handling
    -> capability relation between model methods and the framework
```

This is useful evidence that `STRATEGY` should remain a reasoning function rather than one mandatory intrinsic asset kind.

### Conditional branch rules

#### Feature not worth keeping

```text
WHEN
    missing object = feature
    AND feature worth keeping = no

THEN
    recommend feature-removal strategy
    stop asking treatment questions for that feature unless reopened

FORCE
    project-specific decision guidance
```

#### Production missingness possible

```text
WHEN
    missing object = feature
    AND production missingness = possible

THEN
    activate handling strategies capable of missing inputs
    require evaluation processing consistent with the intended use
    keep the production-missingness concern active in validation reasoning

FORCE
    validity-sensitive guidance
```

The rule does not itself choose an imputation method.

#### Production intended clean, clean evaluation available

```text
WHEN
    missing object = feature
    AND intended production = clean
    AND clean validation/test sample = available

THEN
    activate comparison of training-data treatment strategies
    use validation evidence for strategy choice
    preserve final-test boundary for the chosen strategy
```

#### Production intended clean, evaluation still imperfect

```text
WHEN
    intended production = clean
    AND test sample still contains missing feature values

THEN
    activate sensitivity-reporting guidance
    constrain interpretation of complete-case and imputed test results
    do not represent either automatically as a perfect production estimate
```

#### Row removal under non-uniform missingness

```text
WHEN
    row removal is under consideration
    AND missingness pattern = non-uniform

THEN
    activate distribution-bias concern
    deprioritize row removal relative to plausible alternatives

FORCE
    methodological guidance, not universal prohibition
```

#### Semantic feature type

```text
WHEN
    feature semantic type = categorical

THEN
    activate categorical-compatible missing-value strategies

WHEN
    feature semantic type = numerical

THEN
    activate numerical-compatible missing-value strategies
```

These rules demonstrate why semantic type must be a project concept rather than raw stored dtype.

#### Missing training labels

```text
WHEN
    missing object = target label
    AND location = training

THEN
    activate labeled-only training as one candidate strategy
    activate missing-label-specific alternatives from the framework

IF
    missing-label pattern = non-uniform

THEN
    raise sample-bias concern for labeled-only training
```

#### Missing evaluation labels

The external tree explicitly says not to pretend imputed labels are known and to report uncertainty through best/worst cases.

Conceptually:

```text
WHEN
    missing object = target label
    AND location = final evaluation

THEN
    activate evaluation-uncertainty guidance
    prohibit treating unknown labels as observed truth
    activate lower/upper performance-bound reporting pattern

FORCE
    claim-validity constraint + reporting guidance
```

### How the user-facing tree is derived

The visible navigation can be generated as:

```text
activate Missing Data framework
        |
        v
surface unresolved root Question(s)
        |
        v
answer/finding updates project state
        |
        v
evaluate only rules whose dependencies changed
        |
        +--> activate next Questions
        +--> expose relevant Strategies/Methods
        +--> surface constraints/warnings
        +--> hide/deprioritize irrelevant branches
        |
        v
render current path as a decision tree/workspace view
```

The tree therefore becomes a projection of project state plus reusable knowledge rather than the canonical knowledge object itself.

### Result

The refined model reconstructs the essential branching semantics of the source tree without requiring one giant deterministic workflow asset.

---

## 3. Temporal Validation reconstruction

### Concepts

```text
concept.prediction_moment
concept.target_horizon
concept.retraining_cadence
concept.training_window_policy
concept.temporal_generalization_regime
concept.feature_availability_time
concept.label_availability_time
```

Project-specific values become Foundation 018 `Definition` objects referencing these concepts.

### Framework

```text
asset: framework.temporal_validation
kind: FRAMEWORK
purpose:
    reason about evaluation designs for temporally structured intended use
```

### Validity rule

```text
asset: rule.evaluation_represents_temporal_generalization
kind: RULE
functions:
    evidence requirement
    validity constraint

WHEN
    the intended claim concerns future/temporal generalization

THEN
    require evaluation evidence that sufficiently represents
    the intended temporal generalization regime

UNKNOWN
    if intended regime is unclear, open/retain a project Question
    and block strong deployment-generalization claims as appropriate
```

### Information-legitimacy rule

```text
asset: rule.no_future_information_in_simulated_prediction
kind: RULE
functions:
    hard information-legitimacy constraint

WHEN
    an evaluation simulates prediction at time t

THEN
    information unavailable by the represented prediction moment
    may not influence that simulated prediction
```

### Concrete validation methods

```text
method.chronological_holdout
method.rolling_origin
method.expanding_window
method.sliding_window
```

They remain separate Method assets rather than being hidden inside the Framework.

### Framework-local decision rules

Examples can activate candidates without deterministically selecting them:

```text
WHEN
    repeated model use through time is part of intended deployment
    AND performance stability through time matters

THEN
    increase relevance of repeated temporal evaluation methods
    such as rolling-origin or expanding-window designs
```

and:

```text
WHEN
    one future-like holdout period is sufficient for the current evidence goal
    AND data/compute constraints make repeated simulation low value

THEN
    chronological holdout may remain a reasonable candidate
```

These rules produce recommendation inputs rather than final decisions.

### Result

Temporal Validation cleanly separates:

```text
reusable concepts
hard validity rules
framework reasoning
concrete methods
project Definitions
project-specific Proposal/Decision
```

The refined model handles the example more clearly than the one-role contract from Checkpoint 102.

---

## 4. Prediction-Time Feature Eligibility project-chain test

### Global criterion

```text
asset: rule.prediction_time_feature_eligibility
kind: RULE
functions:
    hard validity constraint
    eligibility criterion
    claim constraint
    revalidation trigger

rule:
    a predictive feature must be computable from information
    legitimately available by the represented prediction moment,
    including relevant source and processing latency
```

### Supporting concepts

```text
concept.prediction_moment
concept.event_time
concept.availability_time
concept.processing_latency
concept.feature_lineage
```

### Project Question

```text
Question Q-17
subject: Variable customer_service_resolution
knowledge origin: prediction-time feature eligibility rule
question:
    Is this variable legitimately available by the project's prediction moment?
```

### Project Evidence

```text
Evidence E-21
source-system documentation says the field is populated after case closure

Evidence E-22
historical timestamps show availability after the scoring cutoff
```

### Project Finding

```text
Finding F-09
kind/facet: CRITERION_FINDING
subject: customer_service_resolution
criterion: rule.prediction_time_feature_eligibility @ revision R
verdict: INELIGIBLE
basis: E-21 + E-22
rationale:
    availability occurs after the represented prediction moment
```

### Optional project Claim

If the project needs to rely on or report the conclusion:

```text
Claim C-04
customer_service_resolution is not eligible for the current deployment claim
```

### Project Decision

```text
Decision D-11
exclude the current feature construction from model development
```

or another repair decision such as lag/recompute-as-of may be selected.

### Downstream revalidation rule

The project graph can support:

```text
WHEN
    a current Criterion Finding marks feature X INELIGIBLE

AND
    a Run used feature X

THEN
    evidence from that Run cannot support the intended deployment-performance claim
    without repair/revalidation

FORCE
    hard claim-validity consequence
```

The rule does not delete the historical Run. It changes what the Run's Evidence can legitimately support.

### Result

The existing Foundation 018 chain is sufficient. A new top-level `Assessment` object is not needed for this example.

The criterion-Finding pattern is materially useful and survives the test.

---

## 5. Histogram granularity test

```text
asset: method.histogram
kind: METHOD
purpose:
    inspect an empirical distribution through binning
```

### Components

```text
component.binning_semantics
    stable local identity
    explains effect of bin definition/width

component.normalization_semantics
    count / proportion / density behavior

component.interpretation_shape_depends_on_bins
    rule-like component
    apparent distribution shape can change with binning

component.extremes_not_automatic_invalidity
    interpretation/claim-limitation component
```

### Narrative facets

```text
examples of useful plots
human explanation of skew/multimodality
visual presentation notes
```

### Relations

```text
Histogram ALTERNATIVE_TO ECDF
    scope: distribution characterization

Histogram COMPLEMENTS summary statistics
```

### Promotion test

If `component.extremes_not_automatic_invalidity` later becomes relevant to boxplots, scatterplots, robust statistics, and outlier workflows, independent reuse would justify promotion to a broader Rule asset.

Until then, component identity is enough.

### Result

The three-level granularity model avoids both anonymous prose and asset explosion.

---

## 6. Random Forest granularity test

```text
asset: method.random_forest
kind: METHOD
```

### Global concept relation

```text
method.random_forest REQUIRES_CONCEPT concept.bagging
```

`Bagging` is now representable as a Concept rather than an undefined pseudo-role.

### Components

```text
component.mechanism
    bagging + feature randomization + tree aggregation

component.capabilities
    nonlinear relations / interactions / classification-regression support

component.hyperparameter_ensemble_size
component.hyperparameter_tree_complexity
component.hyperparameter_feature_randomization
component.hyperparameter_row_sampling

component.stochasticity_reproducibility
component.operational_parallelism
component.operational_memory_inference_cost
```

### Interpretation rule component

```text
component.feature_importance_not_causal
```

If the same rule is reused across other model-derived importance methods, it can be promoted to a broader Interpretation/Rule asset.

### Relations

```text
RandomForest ALTERNATIVE_TO GradientBoostedTrees
RandomForest COMPLEMENTS LogisticRegression
    scope: nonlinear benchmark against a simple baseline
```

### Execution

scikit-learn/Spark implementations remain `ExecutionCapability` entries outside the method knowledge.

### Result

The refined model cleanly represents mechanism, configuration semantics, reusable concepts, and implementation separation.

---

## 7. New-example generalization test: Class Imbalance

Class Imbalance was not one of the five examples that produced the refined model. It is deliberately added to test overfitting.

The concern spans:

```text
target understanding
metric interpretation
resampling
class weighting
threshold selection
calibration
subgroup/temporal stability
business error costs
```

A simple method asset is therefore insufficient.

### Concepts

```text
concept.class_prevalence
concept.decision_threshold
concept.false_positive_cost
concept.false_negative_cost
concept.probability_calibration
```

### Framework

```text
asset: framework.class_imbalance
kind: FRAMEWORK
purpose:
    reason about whether class prevalence and asymmetric consequences
    materially affect evaluation, modelling, thresholding, or claims
```

### Question templates

```text
How rare is the target class in the relevant population?
Is prevalence stable across time/subgroups?
Which errors matter for the project objective?
Does the intended decision require probabilities or class labels?
Does the evaluation metric reflect the decision problem?
```

### Interpretation rule

```text
WHEN
    one class is rare
    AND a metric can be dominated by the majority class

THEN
    constrain interpretation of that metric
    activate complementary class-sensitive evaluation
```

This is interpretation guidance, not a universal command to resample.

### Strategy/method references

```text
class weighting
under/over-sampling
SMOTE-like methods where applicable
threshold tuning
precision-recall evaluation
balanced metrics
probability calibration
```

The Framework can relate to these without asserting that all are always recommended.

### Cross-cutting relationship

Class Imbalance belongs in several human navigation collections:

```text
EDA
Evaluation
Models
Thresholding
Robustness
```

but the Framework remains one substantive reasoning asset. This independently supports the distinction:

```text
FRAMEWORK != KnowledgeCollection
```

### Result

The refined representation generalizes to a new cross-cutting methodological concern without requiring a new fundamental primitive.

---

## 8. Rule expressiveness test

The Missing Data and Temporal Validation cases show that useful methodological navigation requires more than static relations.

The minimum structured rule semantics used in this test were:

```text
predicate references
ALL
ANY
NOT
unknown
consequence category
force
unknown behavior
rationale/scope/provenance
```

This is sufficient for the tested branches if a predicate can refer either to:

```text
a mechanically known project fact/property
an answered Question
a current Finding/Definition
or a semantic check whose truth is supplied by flexible reasoning
```

### Important boundary

Rules should generally produce **reasoning effects**, not directly execute project decisions.

Preferred pattern:

```text
rule fires
    -> activate concern/question/method/strategy
    -> require or block a claim where validity demands it
    -> create recommendation inputs
    -> surface rationale
```

rather than:

```text
rule fires
    -> silently execute preprocessing/model choice
```

This keeps the system open-world and interactive.

### Multiple soft rules

Conflicting non-hard rules should not be resolved by hidden rule priority.

They should contribute inspectable recommendation factors such as:

```text
validity importance
information value
cost
risk
redundancy
project objective
human preference
```

The methodological relevance/ranking layer then resolves trade-offs.

Hard validity constraints can dominate incompatible soft recommendations within their declared scope.

### Cycles and chaining

Rule chaining should be limited to project-state consequences and horizon updates rather than unrestricted automatic execution.

A rule can activate another concern whose own applicability is then evaluated. This supports iterative reasoning without turning the knowledge base into an opaque expert-system program.

### Result

The conditional-rule primitive appears expressive enough for the tested navigation while remaining conceptually narrower than a general rules engine.

---

## 9. Retrieval and applicability test

The examples support the separation introduced in Checkpoint 104.

### RetrievalProfile

High-recall cues such as:

```text
timestamp present
missing values detected
binary target with severe prevalence skew
prediction objective stated
model family under consideration
```

bring assets into the methodological horizon.

### ApplicabilitySpec

Reliable explicit predicates/exclusions can cheaply remove impossible or clearly irrelevant candidates.

### ContextRequirements

Needed concepts/facts such as:

```text
prediction moment
target horizon
semantic variable type
production missingness regime
error-cost preference
```

may be unknown.

Unknown context should often create or retain Questions rather than mark the asset inapplicable.

### SemanticChecks

Questions such as:

```text
does temporal order materially define the generalization regime?
is this numerical column semantically quantitative?
is a modest performance gain worth additional operational complexity?
```

remain flexible-reasoning tasks.

### Result

The five plus one examples do not require collapsing retrieval and applicability back into one profile.

---

## 10. Provenance and revision behavior test

The refined representation assumes:

```text
stable asset id
    +
revision id
```

rather than destructive in-place knowledge mutation.

A project object that materially relies on knowledge should retain the revision reference used at the time.

For a component that materially affects reasoning:

```text
asset revision + component id
```

is sufficient unless the component is later promoted to its own asset.

For a relation or conditional rule whose meaning is independently reviewed/challenged, the relation/rule also needs recoverable provenance and revision semantics.

### Conflict example

If two scoped guidance rules disagree about a missing-data treatment:

```text
Rule A
    scope S1
    recommendation X

Rule B
    scope S2
    recommendation Y
```

that should not automatically be represented as one overwriting the other.

The system first tests whether scopes genuinely overlap. If they do, the conflict is explicit and may require review, evidence, or human authority.

### Supersession

If a reviewed revision supersedes an older rule:

```text
historical projects retain the old revision reference
new reasoning prefers the accepted current revision
active dependent reasoning may be flagged for re-evaluation when material
```

Exact invalidation mechanics remain an implementation/design question.

---

## 11. Second-stress-test verdict

The refined representation survives the second test substantially better than the Checkpoint 102 contract.

No new fundamental primitive was required by:

```text
Missing Data
Temporal Validation
Prediction-Time Feature Eligibility
Histogram
Random Forest
Class Imbalance
```

The most important surviving structural conclusions are now:

```text
1. KnowledgeAsset remains useful, but one semantic-role field does not.

2. Intrinsic asset kind and reasoning function should be separate dimensions.

3. Reusable methodological Concepts need first-class identity.

4. Asset -> Component -> NarrativeFacet is a better granularity model
   than Asset versus anonymous facet.

5. Static semantic relations and conditional methodological rules
   are distinct structures.

6. Rules should create reasoning/navigation effects rather than
   silently execute analytical decisions.

7. Retrieval cues, applicability predicates, context requirements,
   semantic checks, and project relevance are separate stages.

8. Global knowledge may instantiate, reference, constrain, interpret,
   or trigger project objects; there is no universal KnowledgeInstance mapping.

9. Foundation 018's Question -> Evidence -> Finding -> Claim/Decision
   chain can represent criterion assessments without a new universal
   Assessment object.

10. Historical project reasoning must pin the knowledge revision used.

11. Human-facing decision trees can be derived from reusable questions,
    facts, rules, strategies, relations, and project state.

12. The representation remains hybrid: structured where dependency and
    validity matter, semantic where interpretation and trade-offs remain contextual.
```

---

## 12. Remaining open design questions

The representation direction appears stable enough for foundational promotion, but several details should remain explicitly open:

```text
exact intrinsic asset-kind vocabulary
exact reasoning-function vocabulary
exact KnowledgeRelation taxonomy
exact component type vocabulary
condition-expression syntax
rule consequence vocabulary
how rules are indexed/retrieved physically
how relation/rule conflicts are governed operationally
how re-evaluation obligations propagate through active projects
whether some strategy/action patterns need an additional intrinsic kind
how criterion-Finding structure should be represented physically
```

These are implementation/ontology refinements rather than evidence against the core representation architecture.

---

## Promotion audit

### Foundation 020

Warranted.

The representation direction has now survived:

```text
five heterogeneous original examples
an explicit first contract
an adversarial attack
a second concrete reconstruction pass
an additional cross-cutting Class Imbalance example
```

A Foundation 020 should promote the durable architectural conclusions while preserving the exact taxonomies and physical schema as open questions.

### Foundation 018 clarification

Potentially warranted after Foundation 020 is written.

The current result does not require a new project object. It may later justify clarifying `Finding` to support structured criterion-verdict forms.

### Foundation 019

No contradiction found. Its methodological-horizon, hybrid applicability, and open-world principles remain compatible and are now made more concrete by the representation architecture.

### Principles

Several new principles may be worthy of promotion together with Foundation 020, especially:

```text
intrinsic knowledge form should be separated from reasoning function
static semantic relationships should be separated from conditional guidance rules
knowledge granularity should support assets, identifiable components, and narrative facets
rules should guide reasoning/project state rather than directly encode a rigid analytical pipeline
```

Whether these become numbered `PRINCIPLES.md` entries should be decided during Foundation 020 promotion rather than in this historical checkpoint.

### Current-state update

Warranted after Foundation 020 is created.

---

## Exact continuation point

Create Foundation 020 from the conclusions that survived both stress tests.

The foundation should:

```text
1. define the durable conceptual representation layers;
2. promote Asset -> Component -> NarrativeFacet granularity;
3. separate intrinsic asset kind from reasoning functions;
4. introduce reusable Concept semantics;
5. separate KnowledgeRelation from Conditional KnowledgeRule;
6. preserve hybrid retrieval/applicability/context reasoning;
7. define global-to-project influence without universal instantiation;
8. preserve criterion Findings rather than adding Assessment;
9. require revision-level provenance for historical interpretability;
10. preserve derived human-facing workflows and open-world reasoning;
11. explicitly leave physical schema, storage, retrieval, rules-engine,
    and exact taxonomy decisions open.
```

Only after Foundation 020 is promoted should the project decide the next architecture question.