# Project-Development Knowledge Blind Baseline Protocol

**Date:** 2026-09-12
**Status:** RESEARCH 124 BASELINE PROTOCOL V0.1 / PILOT REQUESTS FROZEN / NO TRIALS RUN YET
**Research owner:** Research 124
**Source corpus:** `docs/research/PROJECT_KNOWLEDGE_FAILURE_CORPUS.md`
**Purpose:** Measure selected pre-diagnosis project-development knowledge behaviors in fresh model sessions before successor-mechanism probes or broad external research.

## 1. What blind means here

This is not a clinical double-blind experiment. It is a controlled project-development baseline.

A tested collaborator is blind to:

```text
the evaluator failure-corpus row selected for the scenario
the expected failure mechanism
the preferred architectural remedy (none is selected)
the evaluator scoring rubric
later repository descendants that diagnose the historical incident
other baseline trial outputs
```

The tested collaborator may know that it is running a bounded repository task and must preserve a result receipt. Knowing that a task is evaluated is acceptable. Knowing the expected failure/remedy is not.

## 2. Historical-snapshot rule

Each pilot request names one exact Git commit as its **sole project-evidence snapshot**.

The tested collaborator must:

```text
use repository evidence only as it existed at that exact commit
not inspect descendant commits for project facts
not inspect current Research 124, the failure corpus, baseline protocol, baseline result files or later diagnosis records
not use web/external sources
not use prior-chat/project memory as evidence
```

If its available tools cannot reliably access the exact commit, it must return:

```text
SNAPSHOT_ACCESS_UNAVAILABLE
```

and stop rather than silently substituting current HEAD.

The result artifact itself may be written to current HEAD after reasoning is complete. That write surface is transport/evidence preservation only and is not project evidence for the task.

## 3. Fresh-session rule

Every trial uses a new disposable conversation with no preceding trial in that conversation.

For the initial pilot:

```text
model environments    ChatGPT only
replicates             one per environment per scenario initially
repeat policy          add a second fresh ChatGPT replicate when:
                       - a result is borderline/ambiguous;
                       - a critical dispatch case passes/fails for reasons that appear stochastic.
```

The first pilot therefore begins with 4 trials: 4 scenarios x 1 ChatGPT environment.

Claude and other model environments are intentionally out of scope for this baseline by explicit project-owner decision. A later cross-model study would require a separate owner-approved protocol rather than being assumed as part of this pilot.

## 4. Source-read integrity

The tested collaborator may navigate as broadly as it judges necessary **inside the frozen snapshot**. We do not prescribe which files it must read because that would disclose the expected route.

It must include in the result receipt:

```text
all repository files/artifacts materially used
how it accessed the frozen snapshot
whether any source read failed
whether it deliberately left relevant areas unread
```

A self-reported source list is not a perfect execution trace. For this pilot it is sufficient to detect obvious authority/route choices. If source-read observability proves important, Research 124 may later add a stronger harness.

## 5. Result preservation

The user gives each fresh trial one unique `RESULT_PATH` under:

```text
docs/research/project_knowledge_baselines/results/
```

After reasoning is complete, the tested collaborator may create exactly that one result file and commit/push it. It must not modify project state, routing, Research 124, requests or any other path.

Required result format:

```text
Scenario ID
Environment / model if visible
Frozen snapshot SHA
Result path
Snapshot access method
Sources materially consulted
Read/access failures
Final answer to the task
Uncertainty / areas not checked
Self-reported approximate tool/read effort if available
```

The trial must preserve its answer **before** reading any evaluator material. It must never amend the answer after seeing the rubric or another result.

## 6. Pilot scenarios

### BL-001 - Operational governing-procedure activation

```text
Frozen snapshot    a570f0d87b77960ae0715b291de0d5f6e884e4d0
Historical parent  KF-SD-01 / KF-AS cross-label
Question           Does a fresh collaborator resolve and consume the governing operational
                   procedure before giving exact ordered restart/reconnect guidance?
```

Evaluator success signals, hidden from trial request:

```text
resolves docs/local_execution/OPERATIONS.md as exact-order authority
actually consumes it before producing ordered instructions
reproduces the governing sequence rather than a generic restart recipe
avoids confident substitution when exact project order is unresolved
```

A source-discovery success without actual procedure consumption is not full success.

### BL-002 - Repository-native model-collaboration dispatch

```text
Frozen snapshot    1a422c79dc67384426ad10e28c2fc6845147f9e0
Historical parent  KF-SD-03
Question           Does a fresh collaborator recognize that bring-Claude-into-this-work
                   is governed by an existing repository-native collaboration process?
```

Evaluator success signals:

```text
recognizes/inspects the model-collaboration protocol and pending inbox/state
uses repository-carried task context rather than making the human relay a giant prompt
notices existing collaboration obligations/routing before inventing a new process
clearly distinguishes repository authority from chat-local handoff text
```

The exact thread number or final routing disposition is not pre-scored because the snapshot still contains an older pending Claude obligation and the owner has not supplied the later decision to defer it.

### BL-003 - Broad project orientation under drifted global navigation

```text
Frozen snapshot    f355994c538e0b9b28b5a3c2a5814252ffea1939
Historical parent  KF-RD-01
Question           Can a fresh collaborator form broad project orientation without prior filenames
                   when the then-current global Knowledge Map had become Cockpit-heavy?
```

Evaluator success signals:

```text
orientation extends materially beyond the immediate Cockpit route
identifies multiple enduring project domains and their governing/deep sources
uses repository structure/search intelligently rather than assuming one global map is complete
makes uncertainty/coverage gaps visible rather than claiming exhaustive understanding cheaply
```

Scoring should emphasize breadth + authority awareness + cost, not whether the answer reproduces one exact topic taxonomy word-for-word.

### BL-004 - Exact-source fidelity before holistic Cockpit integration

```text
Frozen snapshot    2d425c76c385961cdd7f986c17ed83437a3d3806
Historical parent  KF-AS-01 / KF-CS-01
Question           Before implementing the first holistic integrated Cockpit, does a fresh
                   collaborator identify the need to consume exact accepted source implementations
                   and provenance rather than reconstructing visual behavior from prose summaries?
```

Evaluator success signals:

```text
finds exact accepted target/source evidence for major held mechanisms where available
separates semantic decision summaries from executable visual/interaction source fidelity
proposes reuse/port/composition or source-level comparison rather than free reimplementation
states gaps where no single accepted whole-product implementation exists
```

The trial is planning-only. It must not implement or mutate the historical snapshot.

## 7. Scoring dimensions

Each result is scored qualitatively on the same dimensions:

```text
S1  task/situation recognition
S2  governing-source discovery
S3  governing-source consumption
S4  authority/source-strength selection
S5  final task correctness / fidelity
S6  uncertainty calibration
S7  broad-vs-narrow context appropriateness
S8  read/tool cost and irrelevant-context burden
```

Per dimension:

```text
PASS       required behavior clearly present
PARTIAL    materially present but incomplete / fragile / overly costly
FAIL       absent, contradicted or replaced by generic inference
N/A        dimension genuinely not applicable
```

No aggregate numeric score is required in the pilot. The purpose is mechanism characterization, not leaderboard ranking.

## 8. Failure attribution

A failed trial should not automatically be attributed to the model or the repository.

Post-run evaluation should distinguish:

```text
snapshot/source absence
navigation/discoverability failure
situation-dispatch failure
authority-resolution failure
source consumed but reasoning incorrect
uncertainty/calibration failure
tool-access limitation
test-protocol contamination or ambiguity
```

This preserves the Research 124 principle that different mechanism classes should not be flattened into one activation score.

## 9. Contamination checks

A trial is invalid rather than failed if:

```text
it reads the failure corpus, this evaluator protocol or another trial result before answering
it uses a descendant commit as project evidence
it receives the evaluator success signals in the user prompt
it continues from a conversation that already discussed the source incident/remedy
snapshot access was unavailable and the model substituted current HEAD
```

A model may independently discover later ideas from the frozen snapshot itself. That is legitimate and not contamination.

## 10. Pilot stopping rule

After the initial 4 trials:

```text
if the four ChatGPT scenarios produce clear, stable mechanism evidence
    -> preserve the baseline and move to external research / targeted mechanism questions

if one scenario is borderline, ambiguous or appears stochastic
    -> run a targeted second fresh ChatGPT replicate only for that scenario

if protocol contamination/access problems dominate
    -> fix the harness before drawing architectural conclusions
```

Do not expand immediately into dozens of scenarios merely because the failure corpus contains 22 rows.

## 11. Request artifacts and initial execution matrix

The four frozen task requests are:

```text
docs/research/project_knowledge_baselines/requests/BL-001_operational_restart_authority.md
docs/research/project_knowledge_baselines/requests/BL-002_model_collaboration_dispatch.md
docs/research/project_knowledge_baselines/requests/BL-003_broad_project_orientation.md
docs/research/project_knowledge_baselines/requests/BL-004_cockpit_source_fidelity.md
```

Initial result paths are reserved as:

```text
docs/research/project_knowledge_baselines/results/BL-001_chatgpt_a.md
docs/research/project_knowledge_baselines/results/BL-002_chatgpt_a.md
docs/research/project_knowledge_baselines/results/BL-003_chatgpt_a.md
docs/research/project_knowledge_baselines/results/BL-004_chatgpt_a.md
```

Trials should run sequentially enough that each result commit can be synchronized before the next writer commits. This avoids turning the baseline into a concurrent-write test.

The short human relay for each fresh disposable conversation should identify only:

```text
repository + coordination branch
one request path
one unique RESULT_PATH
instruction to follow the request exactly
```

It should not include the evaluator rubric or summarize the historical failure the scenario represents.

## 12. Relation to external research and withheld owner source

No broad external literature search and no owner paper/video exposure should occur until the pilot baseline is either completed or explicitly classified infeasible with a preserved reason. This protects the pre-external-evidence behavioral baseline from additional conceptual priming.

```text
BASELINE_PROTOCOL_VERSION=0.1
PILOT_SCENARIOS=4
PILOT_ENVIRONMENTS=CHATGPT_ONLY
INITIAL_TRIALS=4
TARGET_ARCHITECTURE_REMEDY_DISCLOSED=false
EXTERNAL_RESEARCH_STARTED=false
WITHHELD_OWNER_SOURCE_EXPOSED=false
```
