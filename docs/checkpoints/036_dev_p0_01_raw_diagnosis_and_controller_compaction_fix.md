# Checkpoint 36: `dev-p0-01` Raw Diagnosis and P0 Controller/Context Corrections

**Date:** 2026-08-09

## Purpose

Record the complete raw-artifact diagnosis of the first real-model P0 development trajectory and the two implementation corrections justified by that evidence before any second P0 run or held-out execution.

This checkpoint follows `dev-p0-01`, which exhausted the already frozen 250,000-token treatment envelope after 10 successful model calls.

No held-out H1/H2 treatment run has occurred.

---

## 1. Provider/API billing was not the termination cause

The complete run artifacts establish that all ten model generations completed normally:

```text
generation attempts: 10
generation failures: 0
terminal_generation_error: null
```

The tenth request itself completed and reported:

```text
input tokens: 56,855
output tokens: 246
total tokens: 57,101
```

After that completed response, cumulative observed treatment usage became:

```text
250,279 tokens
```

The P0 runner then recorded its own resource-budget exhaustion because the completed call had crossed the registered 250,000-token envelope.

Therefore the user's near-empty API-credit balance was not the cause of this trajectory's termination. The provider response completed successfully and the experiment stopped locally under its preregistered resource rule.

---

## 2. Exact project position at termination

`dev-p0-01` reached Phase 2 but did not reach final model lock.

The trajectory had already:

```text
read the project brief and README;
inspected train/validation temporal and repeated-entity structure;
inspected the inherited baseline implementation;
activated all four Version 0 knowledge components;
explicitly diagnosed inherited learned-preprocessing contamination;
selected a defensible future-month validation regime;
run a clean train-only model comparison;
selected a provisional logistic model;
completed Phase 1;
received the authoritative Phase 2 timing notice;
read that notice on model call 10.
```

The token ceiling was crossed immediately after the notice-read response, before another model turn could interpret the notice, update feature eligibility, re-evaluate without the invalid field, lock the repaired model, or perform final evaluation.

The Phase 1 report was methodologically strong and explicitly stated that inherited validation was excluded because preprocessing had been fitted on train plus validation.

---

## 3. Deterministic assertion interpretation

The deterministic result was:

```text
A0 benchmark self-validation: PASS
A1 no premature final-test value access: PASS
A2 no post-test development: PASS
A3 final model excludes invalid post-outcome feature: FAIL
A4 Phase 2 repair re-evaluation: FAIL (noncritical)
```

The A3/A4 failures are consequences of incomplete progression rather than evidence that P0 executed an illegitimate final model.

At termination:

```text
final_lock_report = null
no final-test values had been accessed
Phase 2 re-evaluation had not yet occurred
```

The run remains a behavior-evaluable completion/resource failure under the frozen protocol.

---

## 4. First implementation defect: same-turn motivator invalidation

The raw trajectory exposed a controller bug that deterministic unit tests had not covered.

The controller intended to validate an action against the runnable frontier visible when the model generated the response. However, the implementation first applied the response's state patch and only then checked whether the cited motivators were still current.

That creates a contradiction when a response legitimately resolves or satisfies the concern that motivated the response.

### First occurrence

A development-model-comparison response cited the blocking inherited-evaluation question `Q-0005` as a motivator while the same state patch marked `Q-0005` resolved based on the already inspected inherited code.

The controller then rejected the otherwise valid action with:

```text
Action cites non-current motivator IDs: Q-0005
```

The model had to repeat the substantive work on the next call.

### Second occurrence

A `phase_1_complete` response cited repair obligation `O-0003` while the same state patch marked that obligation satisfied based on the clean replacement evaluation already produced on the prior turn.

The controller again rejected the response because `O-0003` was no longer current after the patch.

The model repeated the Phase 1 completion on the next call.

### Resource impact

The two rejected provider calls themselves consumed:

```text
call 6: 24,659 tokens
call 8: 40,399 tokens
combined: 65,058 tokens
```

They also enlarged later context because their assistant outputs, harness errors, blocked ACTION audit objects, and subsequent state views remained in the continued conversation.

This is implementation friction, not a legitimate architectural requirement.

### Correction

`p0_controller.py` now validates `motivator_ids` against the **pre-patch** state/frontier that was visible when the response was generated.

Then it:

```text
applies the transactional state patch;
reopens affected existing knowledge instances;
records the ACTION with the original canonical motivator IDs;
activates newly applicable knowledge;
executes the common command.
```

This allows a response to resolve/satisfy its own motivating question or obligation without retroactively invalidating the action.

New client references created by the same patch are not treated as pre-existing motivators; motivators must be canonical IDs from the supplied current frontier.

Newly activated blockers can still prevent a phase transition because activation occurs before command dispatch.

---

## 5. Second implementation defect: audit history was repeated as current model state

The P0 state store is intentionally append-only for auditability. The original `compact_view`, however, serialized every state object and relation on every turn, including historical ACTION objects.

ACTION objects contain the complete common command. For Python actions this includes the full source program; for milestone actions it includes the full report.

By the end of `dev-p0-01`, the full state contained 10 ACTION objects whose serialized command content alone was approximately 10.5k characters.

Those historical actions were then repeated inside every subsequent `P0_STATE_VIEW` even though:

```text
they are controller-maintained audit records;
they are not current project semantics;
the assistant command and harness result already exist in the conversation;
the complete ACTION history is separately retained in p0_state.json and p0_state_history.json.
```

Closed questions and satisfied obligations were likewise repeated even after their durable semantic consequences had been captured as facts, evidence, or decisions.

---

## 6. Why this produced explosive token growth

Observed per-call total tokens were:

```text
call  1:  3,503
call  2:  5,687
call  3:  8,581
call  4: 12,490
call  5: 17,451
call  6: 24,659
call  7: 31,760
call  8: 40,399
call  9: 48,648
call 10: 57,101
```

The run used:

```text
input tokens: 242,743
output tokens: 7,536
total tokens: 250,279
```

Approximately 97% of observed treatment usage was therefore input/context rather than newly generated output.

The serialized `P0_STATE_VIEW` messages themselves grew from approximately:

```text
3.7k characters on the initial turn
29.7k characters before call 10
```

Because the provider continuation retains prior turns, each new full state snapshot coexisted with all previous state snapshots in the ongoing model context. The problem was therefore not merely that the *current* state grew; obsolete copies of earlier state plus large ACTION audit payloads accumulated across turns.

The frozen provider-continuation configuration is not being changed here. The correction is to make `P0_STATE_VIEW` actually satisfy its intended role as a compact current-state interface.

---

## 7. Model-facing state compaction correction

The complete P0 store remains unchanged for audit and dependency logic.

Only the model-facing projection is compacted.

The new current-state view excludes:

```text
all ACTION objects;
relations involving excluded ACTION objects;
RESOLVED questions;
SATISFIED obligations;
superseded/otherwise non-current workflow-control objects;
recent-change records for objects not present in the current model view;
knowledge-component prose whose instantiated question/obligation is no longer current.
```

It retains current:

```text
artifacts;
active/disputed facts;
provisional/supported/invalidated assumptions;
open/reopened/blocked questions;
current/stale/invalidated evidence;
provisional/supported/weakened/invalidated claims;
provisional/accepted/reopened decisions;
open/blocked obligations;
relations among retained objects;
runnable frontier;
a short filtered recent-change tail;
active knowledge whose instantiated concern is currently visible;
resource status.
```

The full audit state and history continue to contain every object, ACTION, relation, and state transition.

This is a representation-efficiency correction inside the pre-specified P0 state mechanism, not a reduction of treatment obligations or privileged knowledge.

---

## 8. Counterfactual size diagnostic on the exact raw trajectory

Applying the new model-view filtering mechanically to the already observed state snapshots, without changing any semantic state decisions, reduces total serialized `P0_STATE_VIEW` characters across the ten observed views from approximately:

```text
162,367
```

to:

```text
73,946
```

This is a reduction of approximately 54.5% in repeated state-view text on the exact observed trajectory.

This is only a diagnostic counterfactual, not a claim about the token usage of the next stochastic run. The next trajectory will differ because the motivator bug should also remove two wasted model turns and the resulting blocked-action history.

---

## 9. What is deliberately unchanged

The fixes do **not** change:

```text
B0 or B1 prompts;
the four privileged methodological knowledge components;
P0 state object or relation types;
benchmark semantics;
H1/H2 bundle identities;
semantic rubric;
blinded judge procedure;
continuation/falsification thresholds;
24-call ceiling;
250,000-token ceiling;
12-Python-attempt ceiling;
30,000 per-call output ceiling;
provider model or reasoning effort;
previous_response_id continuation;
all-turn reasoning context;
prospective protected-test gate.
```

The resource envelope is specifically **not** increased in response to the P0 failure.

---

## 10. Added regression tests

Two tests were added to `test_p0_controller.py`:

```text
same-turn closure of a pre-patch motivator does not invalidate the generated action;
model-facing state excludes audit-only ACTION payloads and closed control concerns while the full snapshot still retains them.
```

The previous suite contained 46 tests, so the expected total after these additions is:

```text
48 passed
```

No second paid P0 run should occur until the complete suite is green locally.

---

## 11. Next step

Run:

```text
git pull origin main
pytest
```

If all 48 tests pass, run a second P0 development trajectory under the **unchanged** frozen treatment resource envelope:

```text
dev-p0-02
```

That run should test whether the corrected controller can complete without the two observed artificial retry loops and with a genuinely compact current-state projection.

H1/H2 remain untouched until P0 development debugging is complete and the implementation is frozen for held-out execution.
