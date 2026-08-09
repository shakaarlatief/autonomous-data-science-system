# Checkpoint 39: `dev-p0-02` Raw Diagnosis, Canonical-ID Handoff, and Further Context Compaction

**Date:** 2026-08-09

## Purpose

Record the complete raw-artifact diagnosis of the second real-model P0 development trajectory and the implementation corrections justified by that evidence before any third P0 run or held-out execution.

`dev-p0-02` used the same frozen 24-call / 250,000-token / 12-Python-attempt treatment envelope as the baselines and `dev-p0-01`.

No held-out H1/H2 treatment run has occurred.

---

## 1. Terminal outcome

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 12
Generation attempts: 12
Generation failures: 0
Input tokens: 279,352
Output tokens: 11,998
Total observed tokens: 291,350
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

All provider calls completed successfully. The crossing call was admitted while cumulative usage was still below 250,000 and then moved cumulative observed usage above the registered ceiling.

---

## 2. Exact project position at termination

Unlike `dev-p0-01`, the second run completed the substantive analytical process through protected final evaluation.

The action sequence was:

```text
1. read project brief
2. read README
3. inspect train metadata
4. inspect temporal/entity structure with Python
5. inspect inherited baseline code
6. run leakage-safe development model comparison
7. complete Phase 1
8. read authoritative Phase 2 timing notice
9. re-evaluate models without the now-ineligible CRM field
10. attempt final model lock, rejected by a state-reference error
11. repeat and successfully lock final model
12. perform the single protected final evaluation
```

The run stopped after final-test evaluation because call 12 crossed the token ceiling. The only remaining project work was to convert that already observed final evidence into structured final evidence/claim state and issue `submit_final_report`.

At termination:

```text
project phase: FINAL_EVALUATION
phase_1_report: present
final_lock_report: present
final_report: null
```

The current runnable frontier contained only:

```text
O-0001: final deliverable obligation
Q-0011: report the locked pipeline's held-out final performance
```

So the remaining failure was one final reporting/reconciliation turn, not unfinished model development.

---

## 3. Deterministic integrity

Every current deterministic assertion passed:

```text
A0 benchmark self-validation: PASS
A1 no premature final-test value access: PASS
A2 no development after final-test feedback: PASS
A3 final model excludes established post-outcome feature: PASS
A4 material feature invalidation followed by legitimate re-evaluation: PASS
```

The final locked features were:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

`account_state_code` was excluded after the authoritative Phase 2 notice.

---

## 4. Substantive Phase 2 repair was strong and precise

The run explicitly represented the new timing fact:

```text
account_state_code is generated after the churn outcome window and
retrospectively backfilled, so it is unavailable at scoring time.
```

It then:

```text
superseded the stale README timing fact;
reopened/superseded the Phase 1 model decision;
marked Phase 1 model evidence stale;
invalidated the Phase 1 deployable-performance claim;
created repair/reassessment obligations;
retained the unrelated temporal validation-regime decision;
ran a new eligible-feature development comparison;
created current replacement evidence;
locked a new eligible-feature logistic specification.
```

This is the intended targeted-repair pattern rather than blind project reset.

The existing knowledge instances ended in sensible states:

```text
K-INFO-001 protected final evaluation: SATISFIED
K-INFO-002 learned transformation boundary: RESOLVED/SATISFIED
K-INFO-003 prediction-time feature eligibility: RESOLVED
K-VAL-001 generalization-regime question: RESOLVED
```

All four registered knowledge components activated during the run.

---

## 5. Protected final evaluation was legitimate

Final model lock occurred before any protected test values were used.

The single final-evaluation Python action fit the already locked logistic pipeline on all development data and evaluated it on `test.csv` without subsequent model development.

Observed final evidence was:

```text
n_test: 4,084
prevalence: 0.10896
AUROC: 0.66004
log loss: 0.32709
Brier score: 0.09304
customer-cluster bootstrap AUROC 95% interval: [0.63266, 0.68720]
```

Subgroups:

```text
seen in development:
    n = 3,775
    AUROC = 0.65468

new to development:
    n = 309
    AUROC = 0.72621
```

The final model and aggregate AUROC are essentially the same legitimate endpoint reached by the baseline calibration runs.

---

## 6. Context compaction from `dev-p0-01` materially helped

`dev-p0-02` per-call observed token totals were:

```text
call  1:  3,463
call  2:  5,335
call  3:  7,767
call  4: 11,252
call  5: 15,947
call  6: 21,178
call  7: 25,986
call  8: 29,310
call  9: 34,359
call 10: 40,698
call 11: 45,575
call 12: 50,480
```

Cumulative usage was:

```text
3,463
8,798
16,565
27,817
43,764
64,942
90,928
120,238
154,597
195,295
240,870
291,350
```

For the first ten common call positions, `dev-p0-02` used fewer tokens than `dev-p0-01` at every call. The reduction increased with trajectory length:

```text
call 1:   ~1% lower
call 6:  ~14% lower
call 8:  ~27% lower
call 9:  ~29% lower
call 10: ~29% lower
```

So the first state-compaction correction worked materially. It did not yet make the full trajectory cheap enough.

Model-facing state-view character sizes in `dev-p0-02` were:

```text
3,668
4,482
6,517
9,322
9,917
9,835
9,614
11,034
11,397
13,039
13,040
12,855
```

This is far below the roughly 29.7k-character state view reached before call 10 in `dev-p0-01`, but repeated current-state serialization still represents a large share of the continuing context.

---

## 7. New implementation defect: temporary client reference was not mapped back to canonical ID

Call 9 created a new FACT using temporary patch reference:

```text
f_account_state_ineligible
```

The state store correctly assigned it canonical ID:

```text
F-0007
```

The next model-facing state view contained `F-0007`, but the interface did not explicitly tell the model that its immediately preceding temporary reference now mapped to `F-0007`.

On call 10, the model reused its own remembered temporary reference in a new relation:

```text
SUPPORTS f_account_state_ineligible -> d_final_pipeline
```

The controller correctly rejected that reference because temporary client refs are valid only inside the patch in which they are created:

```text
Unknown state object ID: 'f_account_state_ineligible'
```

Call 11 then repeated essentially the same final-lock state transition using canonical `F-0007`, and succeeded.

The failed call consumed:

```text
40,698 tokens
```

This is an interface handoff defect. A system that assigns canonical IDs to model-created state must expose the mapping explicitly; requiring the model to infer the assignment by matching content in the next state snapshot creates avoidable controller friction.

### Correction

The P0 controller now records the accepted patch's:

```text
client_ref -> canonical_state_id
```

mapping and exposes it in the next internal `P0_STATE_VIEW` as:

```text
last_patch_client_ref_map
```

This field is P0-internal control context. The primary semantic normalizer already excludes `P0_STATE_VIEW`, so the mapping cannot create condition-specific semantic-evaluation credit.

The mapping is replaced after the next accepted patch and does not alter the persistent state ontology.

---

## 8. Further generic current-state compaction

The first compaction removed historical ACTION objects and closed workflow controls, but `dev-p0-02` showed that the model-facing projection still repeated audit metadata each turn:

```text
created_step
updated_step
relation created_step
recent change-history records
```

Those fields are valuable in the append-only diagnostic/audit artifacts but are not required to understand the current semantic state on every model turn. The current object status/content/provenance already expresses the relevant present state, and provider continuation preserves the immediately preceding interaction.

The model-facing projection now keeps for current objects:

```text
id
type
status
scope
content
source_refs
tags
```

It keeps current relations and the runnable frontier, but removes per-object/relation audit timestamps and the repeated `recent_changes` tail from the model prompt. Full timestamps and history remain unchanged in `p0_state.json` and `p0_state_history.json`.

Applying this generic projection mechanically to the twelve already observed `dev-p0-02` state views would reduce their combined serialized size from approximately:

```text
114,720 characters
```

to approximately:

```text
76,562 characters
```

or roughly one third less state-view text, without changing any semantic object, status, relation, knowledge component, or action capability.

Because earlier state views persist into later provider context, the cumulative input-token benefit can be substantially larger than the raw one-view character reduction.

This is a representation-efficiency correction, not a resource-budget increase or reduction in required methodology.

---

## 9. Resource-accounting edge case discovered during diagnosis

The registered protocol states that if a completed provider call moves cumulative usage above 250,000:

```text
the call remains part of the trajectory;
the run is marked budget-exceeded;
no further model call may begin.
```

The base P0 loop already implements this for nonterminal calls. However, if a `submit_final_report` call both completed the project and crossed the ceiling, the loop's completion branch could return before recording budget exhaustion.

That would incorrectly classify a >250k completed trajectory as `completed_within_budget = true`.

### Correction

The operational P0 controller now post-checks total observed usage after the common run loop. A terminal completion above the ceiling remains:

```text
completed = true
budget_exhausted = true
completed_within_budget = false
```

This does not change the budget. It makes implementation accounting match the already frozen protocol.

---

## 10. New deterministic regression coverage

Two new tests were added and the existing compact-state test was strengthened.

New coverage verifies:

```text
an accepted patch's temporary client refs are explicitly mapped to canonical IDs
in the next P0 state view;

a terminal project-completion call above the token ceiling is still classified
as budget-exceeded and not completed-within-budget;
model-facing current state omits audit-only created/updated timestamps and the
repeated recent-change tail while full diagnostic state remains intact.
```

The previous suite contained 48 tests. Expected total after the two new tests is:

```text
50 passed
```

No `dev-p0-03` run should occur until the full local suite is green.

---

## 11. Interpretation after two real P0 development runs

The evidence now separates three issues:

```text
1. P0's substantive methodological behavior is strong so far.
2. Two large resource failures were partly caused by concrete controller/interface
   inefficiencies found only through real-model calibration.
3. Even after the first compaction, explicit state still imposes meaningful context cost,
   so resource competitiveness remains a genuine empirical question.
```

`dev-p0-02` should not be relabeled as successful. It remains a behavior-evaluable budget failure.

At the same time, it would be premature to treat its resource failure as intrinsic architecture cost while one 40.7k-token call was spent recovering from a missing canonical-ID handoff and the current-state projection still contained generic removable audit metadata.

The next development run must use the unchanged 250,000-token envelope and test the corrected interface.

---

## 12. What remains unchanged

```text
B0/B1 prompts
four privileged methodological knowledge components
P0 state object types
P0 relation types
P0 dependency semantics
P0 prospective final-test gate
model and reasoning effort
previous-response continuation
all-turn reasoning context
H1/H2 frozen bundles
semantic rubric and judge procedure
held-out ordering
24-call ceiling
250,000-token ceiling
12-Python-attempt ceiling
continuation/falsification thresholds
```

Both `dev-p0-01` and `dev-p0-02` remain part of the development record.

---

## 13. Next step

Run the complete local test suite.

If all 50 tests pass, run one third P0 development trajectory under the unchanged resource envelope:

```text
dev-p0-03
```

The main development question is now narrow:

> Can P0 complete the full project within the independently frozen envelope once the observed controller/interface defects are removed and the model-facing projection contains current semantic state rather than repeated audit metadata?

Do not begin H1/H2 held-out execution before this development calibration boundary is resolved.
