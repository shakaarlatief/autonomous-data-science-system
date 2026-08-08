# Foundation 010: Minimum Falsification Prototype and Experimental Contract

## Purpose

This foundation defines the smallest end-to-end experimental prototype that can test whether the core semantic architecture of the Autonomous Data Science System is worth its added complexity.

The project has deliberately avoided implementation until its conceptual claims became falsifiable. Checkpoints 2 through 9 developed candidate theories for epistemic integrity, admissibility, risk-sensitive assurance, dependency-aware project state, progressive initialization, knowledge activation, reusable knowledge representation, knowledge evolution, and behavioral evaluation.

The next step is not a production implementation. It is a controlled experiment.

The central question is:

> **Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?**

The prototype should test this question while minimizing unrelated architecture.

---

## 1. The semantic spine is the object under test

Version 0 should implement only enough machinery to exercise the following loop:

```text
PROJECT STATE
      ↓
KNOWLEDGE ACTIVATION
      ↓
QUESTIONS / OBLIGATIONS / CONSTRAINTS
      ↓
RUNNABLE ACTIONS
      ↓
EXECUTION
      ↓
EVIDENCE
      ↓
STATE UPDATE
      ↓
DEPENDENCY IMPACT / REOPENING
```

The prototype is not intended to test multi-agent coordination, large-scale retrieval, production infrastructure, automatic knowledge learning, external research, deployment monitoring, or provider routing.

The intellectual claim under test is whether this semantic spine adds reliability beyond a strong general-purpose reasoning model.

---

## 2. Falsifiable hypotheses

### H1. Structured state

Explicit typed project state should improve the system's ability to preserve distinctions among facts, assumptions, questions, evidence, claims, decisions, obligations, actions, and artifacts.

A failure of this hypothesis would occur if ordinary free-form reasoning maintains these distinctions equally reliably under project changes and long dependency chains.

### H2. Knowledge activation

State-triggered reusable knowledge should make material methodological concerns appear more reliably and at the appropriate time than relying on one model to recall every concern from general instructions.

A failure would occur if a static high-quality prompt provides equivalent coverage and selectivity.

### H3. Prospective safeguards

Explicit safeguards should prevent some invalid actions before execution, especially around protected evaluation information and information-boundary violations.

A failure would occur if the same model with ordinary instructions avoids those actions just as reliably without the safeguard machinery.

### H4. Dependency-aware correction

When a material assumption, source, feature, or evidence item changes, explicit dependencies should allow the system to reopen affected conclusions while preserving unrelated valid work.

A failure would occur if an ordinary LLM workflow repairs downstream state just as completely and precisely.

### H5. State-driven action selection

Questions and obligations should provide a useful basis for deciding what work is necessary next and should reduce both premature downstream work and unjustified analytical activity.

A failure would occur if the structured system creates comparable or greater wasted work than a simple baseline.

---

## 3. Experimental conditions

The first experiment should use the same underlying strong LLM, the same data and files, the same Python execution capability, and comparable resource limits across conditions.

Three conditions are preferable to only two because they isolate two distinct sources of possible improvement.

### Condition B0: strong generic baseline

The model receives the project, tools, and a strong general instruction to complete the work professionally and autonomously, investigate semantics, avoid leakage, choose appropriate validation, document assumptions, and preserve the final test for final evaluation.

It may maintain ordinary free-form notes but receives no typed project-state machinery and no explicit reusable knowledge components.

### Condition B1: static-knowledge baseline

This condition is identical to B0 except that the small methodological knowledge set used by the prototype is included explicitly in the prompt as static guidance.

This is an important control. If B1 performs as reliably as the structured prototype, then the benefit may come mainly from better prompting rather than project-state and activation architecture.

### Condition P0: structured prototype

P0 uses the same model and project material, plus:

```text
minimal typed project state
small manually authored knowledge set
activation / applicability handling
deterministic prospective safeguards where precise
simple state-derived runnable frontier
dependency-aware invalidation and reopening
traceable state-change history
```

No additional reviewer model, specialist agent roster, or hidden model call should be used merely to increase reasoning capacity.

---

## 4. Exact project request

The initial user-facing task should be approximately:

> Review the inherited customer-churn baseline and produce a defensible improved model for predicting whether an active customer will churn during the next 30 days. Use the provided training and validation information for development. Preserve the provided test set as final evaluation evidence and use it only after development decisions are complete. Investigate the existing workflow rather than assuming it is correct.

The task is intentionally broad enough to require data-science judgment but narrow enough to support a controlled evaluator.

The first prototype does not need operational threshold optimization, missing-data strategy selection, fairness analysis, deployment monitoring, or production integration.

---

## 5. Visible initial project files

Every condition receives the same visible material at the beginning of Phase 1.

```text
project_brief.md
README.md
train.csv
validation.csv
test.csv
baseline_model.py
```

### `project_brief.md`

This is the current project request and should state:

```text
Prediction target:
churn during the next 30 days

Prediction timing:
at the beginning of each monthly scoring cycle

Development:
use training and validation information

Final test:
reserved for one final evaluation after development
```

The file should not specify the correct validation algorithm.

### `README.md`

The README is intentionally stale in two ways.

It says:

```text
Each row represents one customer.
```

It also describes `account_state_code` as a current CRM field available for monthly scoring.

The README should contain an old modification date or other provenance indicating that it may not be current, but it should remain plausible enough that treating it as evidence is reasonable.

### CSV files

The files expose the following columns in the development variant:

```text
customer_id
snapshot_month
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
account_state_code
churn_next_30d
```

The system is not told directly that rows are customer-month snapshots.

### `baseline_model.py`

The inherited baseline should be executable but methodologically flawed.

It should:

```text
use the provided training and validation data;
include account_state_code as a predictor;
fit a learned numerical transformation using information
from both train and validation before evaluating validation;
train a simple baseline classifier;
report validation performance.
```

The initial script should not access the final test set so that final-test contamination remains a separate prospective behavior.

---

## 6. Synthetic data-generating process

The first benchmark family should be synthetic or semi-synthetic so that evaluator truth is known exactly.

### Entity process

Generate approximately 4,000 customers over 24 monthly periods.

Customers enter at different months. Most are present early, while a meaningful minority enter during later validation and test periods. Each customer can therefore contribute several monthly snapshots until churn or the end of the observation window.

This guarantees:

```text
repeated customer IDs
future observations of known customers
new customers appearing later
```

and creates a deployment regime containing both known and newly observed entities.

### Predictive variables

Reasonable features include:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Each customer may have a latent risk term. Time-varying features should contain useful but imperfect information about churn.

A conceptual target model can be based on a logistic hazard such as:

```text
logit P(churn_it = 1)
    = intercept
    + customer_risk_i
    + support_effect
    + late_payment_effect
    + negative_usage_change_effect
    + charge_effect
    + noise
```

The intercept should produce a realistic moderate minority outcome rate rather than a perfectly balanced target.

The exact numerical coefficients are implementation parameters, but they should be fixed and versioned once the case generator is created.

### The post-outcome field

`account_state_code` is the deliberate information-legitimacy trap.

In the historical analytical table, the field should be strongly associated with churn because it is backfilled by a downstream CRM process after the monthly outcome is known.

The initial stale README claims it is available at scoring time.

The hidden evaluator truth is that it is not legitimately available at the beginning-of-month prediction moment.

The field name is intentionally less obvious than `cancellation_reason` so that the benchmark tests information provenance rather than lexical recognition.

### Temporal partitions

Use temporal partitions such as:

```text
train:       months 1-16
validation:  months 17-20
test:        months 21-24
```

The natural validation and test periods should contain a mixture of previously seen and newly entering customers.

This makes a pure unseen-entity split an incomplete representation of deployment. Repeated IDs should therefore activate generalization reasoning but should not mechanically imply GroupKFold.

---

## 7. Hidden evaluator truth

The evaluator knows facts that the system must infer, investigate, or learn later.

The hidden world includes:

```text
one row is a customer-month snapshot;
customer IDs repeat legitimately across months;
production predicts future monthly snapshots;
production includes both known and newly observed customers;
account_state_code is not available at prediction time;
the final test is protected final evaluation evidence;
the inherited baseline preprocessing is contaminated;
the numerical validation score printed by the inherited
baseline may be computationally correct while not being
valid evidence for clean model comparison.
```

The evaluator must distinguish hidden truth from what the system was entitled to know at each moment.

Initial reliance on an apparently authoritative but stale source should not automatically be judged as a failure if the system preserves the associated assumption and revises it when stronger evidence arrives.

---

## 8. Three-phase experimental protocol

The project should unfold through controlled milestones rather than a fixed action sequence.

### Phase 1: initial development

The system receives the initial project files and works autonomously until it believes it has enough evidence for a provisional model and validation position.

It must submit a provisional milestone before final test use.

The milestone should communicate, in whatever form is appropriate to the condition:

```text
current interpretation of row semantics
accepted or provisional validation logic
status of inherited baseline evidence
feature-eligibility assumptions
provisional candidate model / evidence
important unresolved questions
```

The evaluator does not prescribe the internal order used to reach this milestone.

### Phase 2: authoritative state change

After the provisional milestone, the evaluator reveals a new file:

```text
crm_field_timing_notice.md
```

The notice should state authoritatively that `account_state_code` is populated after the monthly churn outcome is completed and is retrospectively backfilled into the analytical warehouse. It is not available at the beginning-of-month scoring moment represented by the project.

This is the central dynamic state-change event.

The system must reconsider affected work.

### Phase 3: final evaluation

Once the system has repaired development state and explicitly indicates that development decisions are complete, the evaluator authorizes one final test evaluation.

After final test outcomes are inspected, further iterative model tuning should be considered a violation of the protected-final-evaluation contract unless the system explicitly abandons the role of that test as independent final evidence and weakens claims accordingly.

---

## 9. Required semantic behavior

The evaluator should not require one exact workflow or model.

It should require the following substantive outcomes.

### Row semantics

The system should detect that repeated customer IDs conflict with the README statement that each row represents one customer.

It should not silently preserve both propositions as true.

It should establish or defensibly infer that observations are monthly customer snapshots before relying on row-level independence assumptions.

### Generalization / validation

The system should recognize that timestamps, repeated customers, and a future prediction objective make the generalization regime material.

It should relate validation design to future deployment rather than mechanically mapping repeated IDs to a grouped split.

Acceptable approaches can include the provided forward temporal validation, rolling-origin variants, or another justified temporal/entity design that represents the intended mixture of known and new customers.

### Inherited baseline evidence

The system should inspect the inherited workflow sufficiently to discover that a learned transformation was fitted using validation information.

The reported validation number may remain a computational artifact, but it should not remain accepted as clean comparative evidence.

### Protected final test

Before Phase 3 authorization, test outcomes must not influence feature design, model selection, preprocessing decisions, threshold decisions, or other development choices.

P0 should prospectively block such an action if proposed.

### Feature timing revision

Before the authoritative notice, the system may treat `account_state_code` as eligible if that interpretation is reasonably supported by visible sources, or it may explicitly keep eligibility unresolved.

After the notice, the feature must no longer be accepted as a legitimate deployment predictor for the represented prediction moment.

### Dependency repair

If models, evidence, decisions, or claims depend on `account_state_code`, the system should identify and reconsider those dependencies after the notice.

Unrelated valid work should remain current.

### Claim validity

Final claims about deployable model performance must depend only on evidence generated under the repaired feature set and an accepted validation/final-test process.

---

## 10. Prohibited behavior

Some failures should count as critical regardless of predictive performance.

Critical examples include:

```text
using protected final-test outcomes during iterative development;
retaining account_state_code in the final deployable model
after the authoritative timing notice;
continuing to treat contaminated inherited validation evidence
as clean support for final model comparison;
producing a final deployment-performance claim that still
depends materially on invalidated evidence;
ignoring a known blocking contradiction while making downstream
claims that require it to be resolved.
```

The evaluator should also detect over-enforcement. For example, a system should not reject all entity overlap merely because customer IDs repeat if deployment legitimately contains known customers.

---

## 11. Acceptable alternative outcomes

The acceptance envelope should permit multiple defensible analytical paths.

The system may choose different model families, preprocessing methods, temporal validation implementations, and feature subsets.

It may exclude `account_state_code` before the Phase 2 notice if it already establishes that timing is uncertain or illegitimate.

It may also use the feature provisionally in Phase 1 if the available evidence justifies that assumption, provided the dependency is repairable when the authoritative source changes the project state.

The experiment therefore evaluates epistemic behavior rather than agreement with one expected model.

---

## 12. Minimal P0 state vocabulary

The first structured prototype should preserve distinctions that are directly exercised by the case while avoiding a comprehensive state ontology.

The minimum candidate object types are:

```text
ARTIFACT
FACT
ASSUMPTION
QUESTION
EVIDENCE
CLAIM
DECISION
OBLIGATION
ACTION
```

These nine types have concrete experimental roles.

`ASSUMPTION` is necessary for testing the later feature-timing revision.

`EVIDENCE` and `CLAIM` must remain distinct because a numerical result may remain computationally correct after losing its legitimate evidential role.

`DECISION` must remain separate from `CLAIM` because selecting a model is different from asserting a proposition about it.

`ACTION` is necessary for prospective safeguards.

`ARTIFACT` is necessary for roles such as protected final test.

The exact serialization format is intentionally deferred.

---

## 13. Minimal relation vocabulary

Version 0 does not need the complete dependency ontology.

A small candidate relation set is:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

The most important experimental distinction is between `DEPENDS_ON` and `SUPPORTS`.

If a conclusion hard-depends on an assumption that becomes invalid, reopening is normally required.

If one supporting evidence path disappears but independent support remains, the conclusion should be reassessed rather than blindly destroyed.

This is enough to test under-propagation and over-propagation.

---

## 14. Minimal reusable knowledge set

The first knowledge library should be intentionally tiny.

### K-INFO-001: Protected Final Evaluation

Role:

```text
hard information-legitimacy safeguard
```

Meaning:

```text
Outcome information from an artifact designated as
independent final evaluation must not influence development
choices before final evaluation.
```

Typical output:

```text
block proposed action
explain conflict
suggest validation / OOF evidence as alternative
```

### K-INFO-002: Learned Transformation Evaluation Boundary

Role:

```text
hard methodological invariant
```

Meaning:

```text
A learned transformation used in evaluation must be fitted
only from information legitimate for the corresponding
training portion.
```

The component should be method-agnostic rather than tied only to scaling.

### K-INFO-003: Prediction-Time Feature Eligibility

Role:

```text
information-legitimacy question / safeguard
```

Meaning:

```text
A predictive feature is legitimate only if the information
it represents is available under the prediction conditions
being claimed.
```

This component may require interpretive applicability because field timing is often semantically uncertain.

### K-VAL-001: Generalization-Regime Question

Role:

```text
question template / decision principle
```

Activation hints:

```text
repeated entities
timestamps
future prediction
partition overlap
```

Question:

```text
What generalization regime must evaluation estimate?
```

The component should explicitly resist rules such as `repeated IDs -> GroupKFold` without intended-use reasoning.

This small set is enough to test deterministic safeguards plus interpretive knowledge activation.

---

## 15. Minimal orchestration

Version 0 should not attempt optimal planning.

A sufficient initial policy is:

```text
1. Satisfy executable hard blockers.
2. Resolve blocking questions that prevent consequential work.
3. Among remaining legitimate actions, choose a plausibly
   high-value next action using the LLM's contextual judgment.
```

The purpose is to test whether state constrains planning usefully, not whether the project has already solved general resource allocation.

---

## 16. Minimal capabilities

The prototype only needs to:

```text
read project files;
inspect tabular data with Python;
inspect inherited code;
run simple preprocessing/model evaluation;
propose and execute actions;
update structured project state;
receive the Phase 2 authoritative notice.
```

It does not need web research, cloud execution, multi-agent delegation, deployment, monitoring, external services, or automatic knowledge learning.

---

## 17. Evaluator outputs

The evaluator should produce a vector of behavioral outcomes rather than one early scalar score.

A useful initial evaluation table is:

| Dimension | Core question |
|---|---|
| Semantic correction | Did the system detect and resolve the row-unit contradiction? |
| Validation reasoning | Did it establish a defensible deployment-relevant generalization regime before trusting model comparisons? |
| Preprocessing integrity | Did it identify inherited learned-transformation contamination? |
| Test integrity | Did protected test outcomes remain outside development? |
| Feature legitimacy | Did the system handle the later timing notice correctly? |
| Repair completeness | Were all materially affected downstream objects reconsidered? |
| Repair precision | Was unrelated valid work preserved? |
| Claim validity | Did final claims depend only on current valid evidence? |
| Detection latency | Were critical concerns discovered before large amounts of dependent work accumulated? |
| Analytical efficiency | How much work lacked a material question, obligation, decision, or deliverable justification? |
| Human effort | If human interaction exists later, was it necessary and high-value? |
| Project utility | Did the final valid process still produce a useful predictive result? |

Critical integrity failures should not be compensated by small predictive-performance advantages.

---

## 18. Resource parity

All conditions should use the same underlying model family and equivalent data/code access.

Resource fairness should be based on total consumed reasoning/execution budget rather than requiring the same number of internal operations.

The experiment should record at least:

```text
LLM calls
input/output tokens where measurable
Python/tool calls
wall-clock time
model-training count
```

A short development calibration stage may be used to set a budget large enough for B0 to complete the project without routine budget exhaustion.

The budget and evaluation rules must then be frozen before held-out comparison.

No condition should receive an uncounted specialist-review model or hidden reasoning budget.

---

## 19. Development and held-out variants

The first case used to build the prototype should not be the only evaluation case.

### Development case

Use the column names and documentation described in this foundation.

This case is available for implementation debugging and evaluator calibration and should not be treated as decisive evidence of generalization.

### Held-out surface variant H1

Preserve the same underlying mechanisms but rename major fields and rewrite project documentation. For example:

```text
customer_id          -> member_key
snapshot_month       -> scoring_period
account_state_code   -> lifecycle_flag
```

Use a different synthetic random seed.

### Held-out surface variant H2

Use another naming/documentation variant such as:

```text
customer_id          -> account_ref
snapshot_month       -> observation_period
account_state_code   -> profile_code
```

The hidden timing mechanism and dependency challenge remain semantically equivalent.

Minor DGP coefficients may vary while preserving the evaluator's core mechanisms.

This reduces lexical benchmark overfitting.

---

## 20. Run protocol

A small calibration stage should occur on the development case before any held-out conclusion.

A reasonable first protocol is:

```text
Calibration:
3 runs per condition on the development case.
Used only to debug the evaluator, set resource budgets,
and identify ambiguous acceptance rules.

Held-out evaluation:
5 paired runs per condition on H1.
5 paired runs per condition on H2.
```

This produces ten held-out runs per condition.

Where stochastic seeds are controllable, paired conditions should use equivalent data and run seeds. Where exact LLM seed control is unavailable, the same dataset instance and evaluator event timing should still be used.

The purpose of this first sample is falsification and architectural comparison, not publication-grade statistical inference.

---

## 21. Critical-run failure definition

A run should be marked as having a critical integrity failure if any of the following remains true at the relevant milestone:

```text
protected test outcomes influenced iterative development;
final deployable model uses account_state_code after the timing notice;
final model-selection claim relies materially on the contaminated
inherited validation evidence;
final deployment-performance claim relies on invalidated evidence;
a blocking semantic contradiction remains unresolved while the
system nevertheless makes a conclusion that requires it to be settled.
```

Architecture-induced false blocking should also be recorded, especially if P0 incorrectly rejects a legitimate evaluation merely because entities repeat or prevents the authorized final test in Phase 3.

---

## 22. Falsification logic

The experiment should be capable of producing evidence against the structured architecture.

### Strong falsification signal

If B1, which has the same methodological knowledge statically available, matches P0 across critical integrity behavior, repair completeness, repair precision, and held-out surface variants while using materially less state-management and reasoning cost, then explicit state/activation machinery is not justified for this case family.

The correct response would be to simplify the architecture or narrow the claim about where structured state is useful.

### Architecture-induced failure

If P0 repeatedly creates false blockers, duplicate obligations, unnecessary reopening, or case-specific rules that are not required by B1, that is evidence against the design even if it prevents some errors.

### Weak evidence

Higher AUROC alone does not justify the architecture.

Likewise one lucky clean run does not establish reliability.

### Continuation signal

The strongest reason to continue beyond Version 0 would be a repeated held-out pattern in which P0 materially reduces critical methodological failures or stale downstream conclusions, detects them earlier, or repairs them more precisely than B1 without unacceptable additional cost or systematic false blocking.

A particularly compelling result would be one where B1 demonstrates the relevant knowledge verbally but fails inconsistently to propagate it through a changing project while P0 remains behaviorally reliable because the dependency and safeguard machinery makes the consequence explicit.

### Numerical decision threshold

The exact quantitative continuation threshold should not be selected before a calibration run reveals the natural variance and cost scale of the chosen LLM. However, it must be frozen before held-out H1/H2 evaluation.

The calibration stage must not be used to rewrite the benchmark toward P0's observed behavior.

---

## 23. What Version 0 explicitly excludes

The first prototype should not include:

```text
multi-agent architecture
provider routing
vector database
graph database
large reusable knowledge library
automatic knowledge extraction / promotion
full admissibility implementation
full risk and assurance system
external web research
production deployment infrastructure
monitoring
user interface
workflow engine
background scheduling
```

These may become future experiments only if the semantic spine first justifies itself.

---

## 24. Manual or mocked behavior is acceptable

Version 0 is allowed to use manually authored knowledge components, a manually authored hidden evaluator world, a deliberately scheduled Phase 2 notice, a simple file-based project state, or other prototype conveniences.

These are not failures of the experiment because automatic knowledge acquisition and industrial scalability are not the hypotheses under test.

The governing question is:

> **Does the semantic machinery itself create enough additional reliability to deserve further engineering?**

---

## 25. Why the prototype uses one LLM

Using several agents in Version 0 would confound the experiment.

If a multi-agent system outperformed the baseline, the cause might be extra inference calls, role specialization, repeated critique, provider diversity, or structured state.

Using the same strong model across B0, B1, and P0 isolates the architectural treatment more cleanly.

This does not imply that the final system should contain one agent.

Agent structure remains an open implementation question.

---

## 26. Reliability rather than raw intelligence

The prototype is based on an important distinction.

A strong contemporary LLM already knows conceptually that test leakage, preprocessing contamination, and future-information leakage are methodological problems.

The architecture is not primarily trying to teach the model those textbook facts.

It is testing whether explicit state and safeguards make it operationally harder to:

```text
forget a relevant rule;
bypass it during execution;
contradict an earlier assumption without noticing;
continue using stale evidence;
fail to reopen a dependent decision;
or overstate a claim after evidence changes.
```

The core value proposition is therefore **reliability of reasoning over time**, not raw intellectual capability.

---

## 27. Recommended implementation order after this contract

Once this experimental contract is accepted, implementation should proceed experiment-first rather than framework-first.

The next work should specify and then build only:

```text
1. synthetic case generator and visible project files;
2. hidden evaluator truth and acceptance assertions;
3. B0 and B1 baseline harness;
4. minimal P0 state representation;
5. four reusable knowledge components;
6. prospective action gate;
7. dependency invalidation / reopening;
8. simple state-derived action selection;
9. evaluator and run logging.
```

The order intentionally puts the benchmark world and evaluator before the autonomous prototype so that the system is not judged using a benchmark invented after its behavior is observed.

---

## 28. Main unresolved implementation questions

This foundation narrows the experiment substantially but does not select the implementation stack.

Still unresolved are:

```text
exact Python object / serialization format for state;
exact status vocabulary;
exact action-gate interface;
LLM API/provider used for the experiment;
exact tool-loop implementation;
model-call and token-budget instrumentation;
evaluator implementation for semantic assertions;
exact numerical continuation threshold after calibration;
repository structure for prototype code and cases.
```

These should be solved as prototype engineering decisions rather than reopened as broad architectural debates.

---

## 29. Current strongest conclusion

The project has reached the point where implementation can begin without pretending that the architecture is already validated.

The first implementation should be treated as an experiment designed to disprove unnecessary complexity.

A concise statement is:

> **Prototype V0 should implement the smallest semantic spine capable of being compared fairly with a strong static-prompt LLM baseline on a dynamic, partially observable churn project with known evaluator truth. The architecture earns expansion only if it makes important methodological behavior materially more reliable.**
