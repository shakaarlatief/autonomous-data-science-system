# Foundation 019: Methodological Navigation Brain and Relevance Architecture

**Date:** 2026-08-19  
**Status:** Foundational product/system design hypothesis  
**Scope:** Long-term methodological-navigation layer; not a frozen V1 implementation

## Purpose

This foundation promotes the latest post-V0 reasoning about the system's methodological-navigation brain.

The intended system should not rely on a general-purpose LLM to remember an arbitrary subset of data-science methods and considerations on each run. At the same time, it should not reduce data science to a giant deterministic checklist.

The current design hypothesis is a broad, evolving, inspectable methodological knowledge system that can transform a large global knowledge universe into a small project-specific set of currently relevant concerns, methods, questions, frameworks, and actions.

The central product problem is:

> Given everything currently known about the project, what methodological knowledge matters now, what should be recommended, what is required for validity, what remains merely optional, and what should stay out of the current reasoning context?

This foundation extends Foundations 006, 007, 008, 013, 017, and 018. It is informed by Prototype V0's failure mode, especially the distinction between persistent system memory and the context sent to an LLM on every turn.

---

## 1. The brain is broader than a method catalog

A catalog containing only algorithms, statistical tests, and visualizations is insufficient.

Reusable methodological knowledge may include several qualitatively different kinds of units:

```text
METHODS
    histogram
    ECDF
    Random Forest
    rolling-origin validation
    RFECV

QUESTION TEMPLATES
    what does one row represent?
    what information exists at prediction time?
    what deployment population should validation represent?

DECISION FRAMEWORKS
    validation-strategy selection
    missing-data handling
    threshold selection

INVARIANTS / HARD RULES
    protected final evaluation must not influence development
    future information must not leak backward through preprocessing

FAILURE MODES
    preprocessing leakage
    misleading accuracy under class imbalance
    invalid random splitting under temporal deployment

INVESTIGATION PATTERNS
    missingness-through-time analysis
    subgroup error analysis
    temporal drift investigation

INTERPRETATION KNOWLEDGE
    what an ACF pattern can and cannot imply
    what a calibration curve can reveal

FOLLOW-UP / DEPENDENCY KNOWLEDGE
    a finding about temporal instability may make validation redesign relevant
    a feature-eligibility failure may invalidate downstream model evidence
```

The methodological brain should therefore be understood as a reusable reasoning-knowledge system, not merely a registry of callable functions.

---

## 2. Global knowledge should be separated from project-specific state

The same global knowledge unit should be reusable across many projects.

For example:

```text
GLOBAL KNOWLEDGE
Repeated entities require reasoning about the actual generalization regime.
```

is distinct from:

```text
PROJECT STATE
customer_id repeats in this dataset
future deployment includes known and new customers
```

and from:

```text
PROJECT RECOMMENDATION
Use chronological validation as the primary design and report known/new-customer subgroups.
```

The system should not copy the complete knowledge base into each project. Project-specific recommendations should be produced by combining global knowledge with project state, user intent, constraints, risk, cost, and current evidence.

---

## 3. Relevance should be staged rather than binary

A useful current conceptual progression is:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

These stages have different meanings.

### Known

The system knows the knowledge unit exists.

### Applicable

Basic prerequisites are satisfied. A method can be technically applicable without being worth doing.

### Relevant

The method, question, rule, or framework could materially help answer something that matters in the current project.

### Recommended

Given expected information value, project relevance, cost, risk, existing evidence, alternatives, and user preferences, the system judges that the work is worth doing now or soon.

### Required / blocking

A downstream action, claim, or deliverable cannot be defended until the issue is resolved or explicitly bounded.

Required is not merely a stronger recommendation. It arises from validity, project constraints, admissibility, or another non-negotiable dependency.

The system should also be able to represent:

```text
NOT CURRENTLY APPLICABLE
APPLICABLE BUT NOT RECOMMENDED
DEFERRED
SUPERSEDED
```

where useful.

---

## 4. Recommendation omissions must be explainable

The user should be able to inspect why a known method was not recommended.

For example:

```text
PCA

Status:
Applicable, but not recommended.

Reasons:
- low dimensionality;
- no current dimensionality bottleneck;
- interpretability is valued;
- selected models do not require orthogonal components;
- expected incremental value is low.

Could become more relevant if:
- dimensionality grows;
- multicollinearity materially affects a chosen model;
- latent low-dimensional structure becomes an explicit objective.
```

This distinction enables the system to separate several failure modes:

```text
the system did not know the method;
the system knew it but judged it inapplicable;
the system knew it was applicable but ranked it too low;
the system recommended it but the user skipped it.
```

These should be evaluated and improved separately.

---

## 5. Applicability and prioritization should be hybrid

The future system should not ask an LLM to rediscover every hard prerequisite from scratch.

Some conditions can be explicit and cheaply evaluated, for example:

```text
ACF requires an ordered sequence with meaningful temporal structure.
A chi-square independence test requires categorical/count structure and relevant frequency conditions.
Certain model families require scaling or specific input forms.
A final-test protection rule can be enforced deterministically when the information boundary is explicit.
```

Other questions require flexible semantic reasoning:

```text
Does grouped validation represent the actual deployment population?
Is a small performance improvement worth the added complexity here?
Does this unusual missingness pattern suggest a process change?
```

A candidate conceptual flow is therefore:

```text
PROJECT STATE
      |
      v
CHEAP EXPLICIT FILTERING
prerequisites / incompatibilities / hard rules
      |
      v
CANDIDATE KNOWLEDGE
      |
      v
LLM OR OTHER FLEXIBLE REASONING
semantic applicability / relevance / tradeoffs
      |
      v
PRIORITIZATION
      |
      v
REQUIRED / RECOMMENDED / RELEVANT / NOT NOW
```

This is a design class, not a selected implementation.

---

## 6. The methodological horizon

A useful current concept is the **methodological horizon**.

The global knowledge base may eventually contain thousands of units, while only a small subset is plausibly relevant to the current project state.

Conceptually:

```text
GLOBAL KNOWLEDGE
5,000 units
      |
      v
PROJECT-SPECIFIC RETRIEVAL / FILTERING
      |
      v
METHODOLOGICAL HORIZON
60 plausible units
      |
      v
reasoning / ranking
      |
      +-- 4 required
      +-- 11 recommended
      +-- 23 relevant
      +-- 22 lower-priority applicable
```

The horizon should change as the project changes.

Examples:

```text
timestamp discovered
    -> temporal EDA and validation knowledge enters the horizon

repeated entity IDs discovered
    -> entity-generalization knowledge enters the horizon

severe class imbalance discovered
    -> imbalance metrics, resampling, threshold, and calibration knowledge enters the horizon

probability quality becomes important
    -> calibration knowledge enters the horizon
```

The LLM should not receive the full global catalog. It should receive the small subset relevant to the current reasoning problem.

---

## 7. Project signals and recommendation rationale should be inspectable

The user should be able to inspect the signals that caused methodological areas to become relevant.

For example:

```text
PROJECT SIGNALS
- supervised classification
- binary target
- timestamp present
- repeated entity identifier
- three variables with missingness
- future prediction objective

RELEVANT KNOWLEDGE AREAS
- target balance
- temporal EDA
- repeated-entity structure
- missing-data analysis
- validation-regime reasoning
- feature availability

TOP RECOMMENDATIONS
1. inspect target prevalence through time
2. inspect repeated-entity distribution
3. characterize missingness through time
4. verify prediction-time feature availability
```

This makes the methodological brain auditable instead of presenting opaque suggestions.

---

## 8. Knowledge and execution templates are different

The system should separate methodological meaning from one library implementation.

For example:

```text
METHODOLOGICAL KNOWLEDGE
Compare class-conditional numeric distributions.

INVESTIGATION PLAN
columns = [...]
group = target
methods = histogram + ECDF + summary table

EXECUTION TEMPLATE
Python / pandas / Plotly / another implementation

RUN
reproducible execution with project-specific inputs and provenance
```

Likewise:

```text
Method knowledge: Random Forest
Execution implementation: scikit-learn wrapper
```

The methodological brain should remain portable across execution libraries and environments.

---

## 9. Recommendation ranking should remain interpretable

A single opaque score is not sufficient as the product abstraction.

Candidate ranking dimensions include:

```text
validity importance
expected information gain
downstream impact
uncertainty reduction
project relevance
risk
cost
redundancy with existing evidence
user learning value
reversibility
human preference
```

Example:

```text
Investigate prediction-time feature availability

Validity importance    CRITICAL
Information gain       HIGH
Downstream impact      HIGH
Cost                   LOW
Existing evidence      WEAK
Result                 REQUIRED
```

versus:

```text
Generate a 40-variable pairplot

Validity importance    LOW
Information gain       LOW-MODERATE
Clutter / cost         HIGH
Redundancy             HIGH
Result                 NOT RECOMMENDED
```

The exact ranking model remains open.

---

## 10. Knowledge units require provenance, scope, and maturity

Knowledge accumulation is not automatically good.

A reusable unit should eventually be able to carry concepts such as:

```text
provenance
scope
maturity
confidence in scope
known exceptions
known counterexamples
references
last review
challenge / validation history
```

For example:

```text
Title:
Repeated entities require generalization-regime reasoning

Type:
Question / decision principle

Scope:
Supervised predictive problems with repeated entities

Do NOT interpret as:
Always use GroupKFold

Relevant considerations:
- future observations of known entities?
- unseen entities?
- temporal ordering?
- deployment mixture?
- entity-history leakage?
```

This aligns with Foundation 008's principle of minimum justified generalization.

---

## 11. The catalog should be hierarchical for humans but cross-linked conceptually

For human navigation, a hierarchy such as this may be useful:

```text
Data Science Knowledge
├── Project Understanding
├── Data Understanding
├── EDA
│   ├── univariate
│   ├── bivariate
│   ├── multivariate
│   ├── missingness
│   ├── outliers
│   ├── temporal
│   └── subgroup
├── Validation
├── Feature Engineering
├── Feature Selection
├── Models
├── Diagnostics
├── Interpretation
├── Robustness
├── Evaluation
├── Reporting
└── Deployment
```

But many concerns are cross-cutting.

For example, class imbalance can affect:

```text
EDA
metrics
resampling
thresholding
calibration
model comparison
```

Therefore one folder tree is unlikely to be sufficient as the internal conceptual structure.

---

## 12. The brain should remain open-world

Explicit catalog coverage is one defense against omission, but it should not become a closed checklist.

A complementary strategy is open-ended reasoning:

```text
Given the current project state and retrieved methodological horizon,
is there an important analytical concern or option not represented here?
```

If flexible reasoning repeatedly discovers a useful concern absent from the catalog, that becomes a candidate knowledge gap.

The long-term learning loop may be:

```text
novel useful concern
    -> candidate knowledge gap
    -> review scope and evidence
    -> promote when justified
    -> future projects can retrieve it
```

This preserves open-world reasoning while making successful lessons reusable.

---

## 13. Relationship to Prototype V0

Prototype V0 should not be treated as a miniature implementation to scale directly.

V0 used only four methodological components and a path-sensitive activation mechanism. The held-out result showed that static B1 knowledge captured most of the semantic benefit, while P0's always-on structured context added severe token cost.

The current post-V0 interpretation is therefore:

```text
persistent methodological knowledge may still be valuable

but

full knowledge/state should not be injected into every reasoning call

and

narrow trigger paths should not be assumed to capture semantic relevance robustly
```

Foundation 019 therefore favors selective retrieval, explicit filtering where reliable, flexible reasoning where necessary, inspectable ranking, and a changing methodological horizon.

---

## 14. Next design problem

The next design step should go one level deeper into the reusable knowledge representation itself.

Use several deliberately different examples:

```text
Histogram
Missing-data investigation
Temporal validation
Random Forest
Prediction-time feature eligibility
```

For each, ask:

```text
What reusable information must the system know?
Which fields are shared across all units?
Which information is type-specific?
How are prerequisites and applicability represented?
How are alternatives, complements, failure modes, and follow-ups represented?
What can be deterministic versus interpreted by an LLM?
What belongs in the knowledge unit versus execution implementation?
```

The goal is not to force all knowledge into one universal schema. The exercise should reveal whether a common core plus typed extensions is appropriate.

No database, retrieval engine, or V1 implementation should be selected before this conceptual representation is sufficiently clear.