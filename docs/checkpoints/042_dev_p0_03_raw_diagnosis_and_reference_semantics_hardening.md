# Checkpoint 42: `dev-p0-03` Raw Diagnosis and P0 Reference-Semantics Hardening

**Date:** 2026-08-09

## Purpose

Record the complete diagnosis of the third real-model P0 development trajectory and the implementation corrections justified by that trajectory before any fourth P0 run or held-out execution.

No held-out H1/H2 treatment run has occurred.

---

## 1. Terminal outcome

`dev-p0-03` used the unchanged frozen treatment envelope:

```text
24 successful model calls
250,000 observed treatment tokens
12 Python execution attempts
30,000 max output tokens per call
2 additional generation retries
```

Terminal result:

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 14
Generation attempts: 14
Generation failures: 0
Input tokens: 250,015
Output tokens: 10,219
Total observed tokens: 260,234
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: False
```

The run stopped locally because the fourteenth completed provider call crossed the registered token ceiling. There were no provider-generation failures.

---

## 2. Exact project position at termination

The run reached revised Phase 2 development but did not successfully lock the final model.

Action sequence:

```text
1. read project brief
2. read README
3. attempt train metadata inspection; rejected because a same-patch question client ref was also listed as a motivator
4. repeat train metadata inspection successfully
5. inspect temporal/entity structure with Python
6. attempt inherited-baseline read; rejected because an earlier client-ref alias was reused in a relation
7. repeat inherited-baseline read successfully
8. run leakage-safe development comparison
9. run regularization / temporal robustness analysis
10. complete Phase 1
11. read authoritative Phase 2 timing notice
12. re-evaluate eligible-feature models after removing account_state_code
13. attempt final lock; rejected because an earlier client-ref alias was reused in a relation
14. repeat final-lock patch with canonical IDs; common phase gate then blocked on a newly created redundant support-reassessment obligation
```

At termination:

```text
project phase: PHASE_2_REVISED_DEVELOPMENT
phase_1_report: present
final_lock_report: absent
final_report: absent
```

The run had already produced valid replacement Phase 2 development evidence without `account_state_code`; final lock was blocked by controller/state-interface friction rather than by missing model re-evaluation.

---

## 3. Deterministic result

```text
A0 benchmark self-validation: PASS
A1 no premature final-test value access: PASS
A2 no development after final-test feedback: PASS
A3 final model excludes post-outcome feature: FAIL because no final lock report existed
A4 Phase 2 re-evaluation: FAIL under the current evaluator because final lock was absent, although a legitimate Phase 2 development execution occurred
```

The critical failure is therefore mechanically tied to failure to reach final lock. There was no premature test access and no invalid final model was executed.

---

## 4. Substantive analytical behavior before termination

The run remained methodologically strong in the work it completed.

Phase 1:

```text
future monthly churn objective established;
protected final evaluation represented;
repeated customer-month structure and temporal split inspected;
provided future validation regime selected rather than mechanical GroupKFold;
inherited baseline preprocessing contamination explicitly diagnosed;
leakage-safe train-only preprocessing used for development comparison;
logistic regression selected provisionally;
Phase 1 report completed.
```

Phase 2:

```text
authoritative notice established account_state_code as post-outcome and unavailable at scoring;
old feature timing semantics were disputed;
Phase 1 model decision was reopened;
Phase 1 evidence was invalidated;
repair obligations were created;
a fresh six-feature eligible-model comparison was executed;
replacement evidence favored logistic regression.
```

So the third run did not reveal a methodological collapse before the budget stop.

---

## 5. Context-efficiency improvement was substantial

Per-call total-token usage in `dev-p0-03`:

```text
call  1:  3,009
call  2:  4,250
call  3:  5,885
call  4:  7,301
call  5:  9,879
call  6: 13,176
call  7: 15,475
call  8: 19,411
call  9: 22,427
call 10: 25,276
call 11: 27,753
call 12: 31,483
call 13: 35,618
call 14: 39,291
```

Cumulative usage:

```text
3,009
7,259
13,144
20,445
30,324
43,500
58,975
78,386
100,813
126,089
153,842
185,325
220,943
260,234
```

Against `dev-p0-02`, the first twelve common call positions were cheaper by approximately:

```text
call 1:  13%
call 2:  20%
call 3:  24%
call 4:  35%
call 5:  38%
call 6:  38%
call 7:  40%
call 8:  34%
call 9:  35%
call 10: 38%
call 11: 39%
call 12: 38%
```

Model-facing P0 state views ranged from about 2.0k to 9.7k characters, substantially below the prior runs. The second context-compaction correction therefore worked materially.

This makes the remaining failed calls especially important: resource use is no longer dominated by the original full-state serialization defect.

---

## 6. Reference failure 1: same-patch client ref listed as supplemental motivator

On call 3 the response created a new question using client ref:

```text
Q2
```

The response also listed:

```text
Q-0001
Q2
O-0002
```

as motivators for the metadata-inspection action.

`Q-0001` and `O-0002` were legitimate pre-existing current motivators. `Q2` was an additional same-response question. The controller rejected the entire action because `Q2` was not yet a canonical current-state ID:

```text
Action cites non-current motivator IDs: Q2
```

The next call repeated the metadata action without `Q2` and succeeded.

The rejected call cost 5,885 tokens.

### Correction

The runnable-frontier invariant remains unchanged: at least one valid pre-patch current motivator must justify every action, including the highest-priority blocker when one exists.

However, a same-patch client ref may now appear as a **supplemental** motivator when the response already contains a valid pre-patch motivator. It is mapped to its canonical ID for the ACTION audit record after the patch is accepted.

A response whose only motivator is created in the same patch is still rejected. Thus the controller becomes tolerant of harmless co-created references without allowing an action to manufacture its own justification retroactively.

---

## 7. Reference failures 2 and 3: earlier client-ref aliases remained brittle

The controller introduced `last_patch_client_ref_map` after `dev-p0-02`, but the third run showed that exposing a mapping for one turn is insufficient.

### Call 6

An earlier accepted patch had created:

```text
F3 -> F-0003
```

Several turns later the model reused `F3` in a relation. The canonical object `F-0003` was visible in state, but the controller still required the model to perform manual alias translation and rejected:

```text
Unknown state object ID: 'F3'
```

The next call repeated the action with `F-0003` and succeeded.

Rejected-call cost:

```text
13,176 tokens
```

### Call 13

Phase 2 created:

```text
D4 -> D-0004
F7 -> F-0007
```

The next final-lock patch reused `D4` in a relation. Even though the private state view exposed the mapping, the state store still did not accept the alias and rejected:

```text
Unknown state object ID: 'D4'
```

Call 14 repeated the final-lock patch using `D-0004`.

Rejected-call cost:

```text
35,618 tokens
```

Together with call 3, the three reference-interface failures consumed:

```text
5,885 + 13,176 + 35,618 = 54,679 tokens
```

and also enlarged all later continuation context.

### Correction

Model-created client refs are now treated as persistent controller-level aliases for the canonical IDs assigned to accepted objects.

The controller:

```text
retains the accepted client-ref -> canonical-ID map across turns;
exposes the small persistent alias map in the private P0 state view;
deterministically canonicalizes earlier aliases in later status updates and relation endpoints;
preserves same-patch client-ref resolution for newly created objects;
updates aliases only after an accepted transactional patch.
```

This changes no project semantics and adds no methodological knowledge. It makes the state interface robust to the model remembering the label it originally supplied.

---

## 8. New final-lock blocker: support reassessment of an OBLIGATION target

Call 14 corrected the alias and successfully applied most of the final-lock state patch. It:

```text
created current revised evidence E-0003;
created accepted final-model decision D-0005;
superseded the old seven-feature decision D-0003;
satisfied the two real Phase 2 support-reassessment obligations O-0004 and O-0005;
linked current evidence and the feature-exclusion decision to the new final decision.
```

However, when `D-0003` became `SUPERSEDED`, generic SUPPORTS-loss propagation noticed that `D-0003` had previously `SUPPORTS`-linked to the broad deliverable obligation `O-0001`. It therefore created:

```text
O-0006:
Reassess O-0001 because supporting object D-0003 is no longer current.
priority:repair
```

The same patch had already created a replacement decision that supported the deliverable, but O-0006 did not exist when the model generated the response and could not be satisfied in that patch. The final-lock gate then blocked:

```text
Final model cannot lock while repair concerns remain open: O-0006
```

This is a semantic mismatch in the generic support-reassessment mechanism.

`SUPPORTS` is defined as non-exclusive evidential support. A CLAIM or DECISION can require reassessment when one evidential support path disappears. An OBLIGATION is different: its current force is represented by OPEN/SATISFIED/BLOCKED lifecycle status. Losing a decision that happened to support the broad project deliverable does not create a second methodological question about whether the deliverable obligation still exists.

### Correction

The operational controller now reconciles any generic support-loss reassessment whose **target is an OBLIGATION** by immediately closing that redundant secondary reassessment before phase-gate evaluation.

The audit trail still records creation and closure. Legitimate support-loss reassessments targeting substantive decisions/claims remain unchanged; in particular, the two Phase 2 obligations created when E-0001 and E-0002 stopped supporting D-0003 are still real repair blockers and must be satisfied explicitly.

This correction is generic to relation/type semantics and does not encode churn-specific or held-out-specific knowledge.

---

## 9. One state-graph quality issue is deliberately not repaired automatically

The model created Q-0006 ('Does the CRM timing notice change prediction-time eligibility?') with a hard `DEPENDS_ON` edge to the old model decision D-0003. Later, superseding D-0003 caused dependency propagation to reopen Q-0006 even though the timing question had already been answered.

This is a questionable model-authored hard-dependency edge. It did not cause the registered critical failure because Q-0006 was not a repair-priority blocker, and the primary semantic evaluator does not see P0-only internal state.

No automatic rule is added from this single observation. It remains evidence that relation quality is itself a behavior to monitor. Broadly rewriting model-authored dependency graphs here would risk overfitting development behavior before held-out testing.

---

## 10. What remains unchanged

The corrections do **not** change:

```text
B0 or B1 prompts;
the four privileged knowledge components;
P0 state object or relation vocabulary;
P0 hard-dependency propagation semantics;
protected-final-test safeguard;
benchmark semantics;
H1/H2 bundle identities;
semantic rubric or judge;
held-out ordering;
24-call ceiling;
250,000-token ceiling;
12-Python-attempt ceiling;
model or reasoning effort;
provider continuation configuration;
continuation/falsification thresholds.
```

All three failed P0 development runs remain part of the development record.

---

## 11. New regression coverage

Four tests were added to `test_p0_controller.py`:

```text
persistent client-ref aliases resolve in later patches;
same-patch client refs may be supplemental motivators when a valid pre-patch motivator exists;
a same-patch-only motivator cannot bypass the pre-patch runnable frontier;
support loss to an OBLIGATION target does not leave a redundant open repair blocker.
```

The prior suite contained 50 tests. Expected total after these additions:

```text
54 passed
```

No additional paid P0 run should occur until the complete suite is green locally.

---

## 12. Next step

Run:

```text
git pull origin main
pytest
```

If all 54 tests pass, inspect the implementation boundary once more and then authorize `dev-p0-04` under the same frozen resource envelope.

H1/H2 remain untouched until P0 development debugging is complete and the implementation is explicitly frozen for held-out execution.
