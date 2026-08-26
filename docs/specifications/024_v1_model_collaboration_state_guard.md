# Specification 024: V1 Model Collaboration State Coherence Guard

**Date:** 2026-08-25  
**Status:** Accepted V1 implementation contract  
**Outcome:** `COLLABORATION_STATE_GUARD_ACCEPTED`  
**Classified:** 2026-08-26  
**Scope:** Provider-neutral machine-readable coordination state for governed multi-model development tasks  
**Precondition at freeze:** MC-0001 architecture review resolved; exact mechanism not yet implemented at freeze time  
**Authority:** Accepted V1 implementation contract for the model-collaboration state coherence guard. The original MC-G01 through MC-G16 gates remain the frozen acceptance basis.

## 1. Purpose

MC-0001 established that prose-only ownership rules are insufficient for routine multi-model canonical development.

The first mechanical seam must make task ownership, target-state write ownership, allowed secondary write surfaces, lifecycle state, and next-actor routing machine-checkable without pretending to provide cryptographic model identity or a distributed mutex.

The required distinction is:

```text
collaboration-state coherence guard
    !=
security boundary / authenticated distributed lock
```

## 2. Non-goals

Specification 024 does not:

```text
authenticate whether ChatGPT or Claude made a Git commit
create separate provider credentials
build an API orchestrator
lock GitHub branches server-side
replace Git stale-write / SHA protection
make collaboration mandatory for SOLO tasks
turn current_routing.json into a global lock service
freeze permanent model specializations
```

## 3. Physical contract

The bounded implementation adds:

```text
schemas/model_collaboration_thread_state_v1.schema.json
scripts/check_model_collaboration_state.py
tests/unit/test_model_collaboration_state.py
.github/workflows/model-collaboration-state.yml
```

Collaborative threads that opt into the guard use:

```text
docs/model_collaboration/threads/MC-NNNN/STATE.json
```

`STATE.json` is thread execution/coherence state. It is not project-current routing and must not be embedded into `docs/current_routing.json`.

## 4. V1 state shape

The schema contains these top-level fields:

```text
schema_version
thread_id
review_mode
lifecycle_state
phase
target
task_owner
target_write_owner
participants
allowed_secondary_write_surfaces
next_expected_actor
independence
last_transition
```

### 4.1 Thread identity

```text
schema_version = 1
thread_id       = MC-NNNN
```

The validator verifies that the thread ID matches the directory containing `STATE.json`.

### 4.2 Review mode

V1 allowed values:

```text
SOLO
REVIEWED
INDEPENDENT_THEN_COMPARATIVE
COORDINATED_HANDOFF
ADVERSARIAL_REVIEW
```

A SOLO task normally does not need an MC thread, but the value is allowed so the schema does not artificially forbid a deliberately recorded solo control/baseline.

### 4.3 Generic lifecycle state

Use a small generic state vocabulary rather than encoding every possible review phase into the schema:

```text
OPEN
ACTIVE
WAITING
RESOLVED
UNRESOLVED
DEFERRED
CLOSED
```

The human-readable or task-specific substage lives in `phase` as a bounded non-empty identifier string.

This avoids schema churn when future collaboration patterns add a new intermediate step.

### 4.4 Target

`target` contains:

```text
branch
base_ref
description
write_paths[]
```

`write_paths` are repository-relative declared target-state surfaces.

They may contain simple glob markers such as `*` and `**`, but must not contain absolute paths, backslashes, empty segments, or `..` traversal.

`base_ref` records the repository ref/head from which the bounded task was opened.

### 4.5 Participants

Each participant contains:

```text
collaborator_id
interaction_environment
interaction_session
roles[]
```

V1 role vocabulary:

```text
TASK_OWNER
INDEPENDENT_REVIEWER
REVIEWER
CRITIC
COUNTER_DESIGNER
RESEARCHER
IMPLEMENTER
VERIFIER
HUMAN_DECIDER
```

Roles are vocabulary, not mandatory staffing slots.

Participant IDs must be unique.

### 4.6 Task owner and target write owner

`task_owner` references one declared participant.

`target_write_owner` references one declared participant while target-state mutation is active. It may be null only when no participant currently owns target-state mutation, including a closed thread.

This is separate from role.

### 4.7 Allowed secondary write surfaces

Each entry contains:

```text
collaborator_id
paths[]
```

It declares repository surfaces a collaborator may mutate while another participant retains target-state write ownership.

The validator rejects an allowed secondary surface that overlaps a declared target write path under the V1 conservative lexical overlap check.

This is the key correction to a single global `active_writer` model.

Known V1 scope limitation after direct review: the frozen contract does not check secondary-vs-secondary overlap between two simultaneous secondary writers. MC-0002 classified this as a real but non-blocking future extension because it was outside MC-G06 and is not currently exercised by the project.

### 4.8 Next expected actor

`next_expected_actor` is a collaborator ID or null.

For `CLOSED`, it must be null.

For active collaboration, it identifies the collaborator expected to act next, without granting that collaborator target-state write ownership by implication.

### 4.9 Independence

The `independence` object contains:

```text
status
review_base_ref
known_exposures[]
notes
```

V1 status vocabulary:

```text
NOT_APPLICABLE
BLIND_TO_CANDIDATE
PARTIALLY_INDEPENDENT
COMPARATIVE_ONLY
```

Known contamination is recorded, not erased.

### 4.10 Last transition

The `last_transition` object contains:

```text
transition_id
from_state
to_state
actor
reason
repository_head
```

`to_state` must equal the current `lifecycle_state`.

`actor` must reference a declared participant.

`repository_head` must be one lowercase 40-character Git SHA.

A complete event ledger is not required in V1. Git history plus the current transition record are sufficient for this bounded guard. If later use shows that a first-class transition log is needed, that should be justified empirically.

## 5. Validator semantics

The validator:

```text
1. validates JSON against the V1 schema;
2. validates thread ID vs directory name;
3. rejects undeclared task owners / write owners / next actors / transition actors;
4. rejects duplicate participant IDs;
5. validates normalized repository-relative path declarations;
6. rejects conservative lexical overlap between target and secondary write surfaces;
7. requires an active target_write_owner for OPEN/ACTIVE/WAITING unless the task explicitly has no target write paths;
8. requires target_write_owner = null and next_expected_actor = null for CLOSED;
9. requires last_transition.to_state == lifecycle_state;
10. requires THREAD.md to exist beside a guarded STATE.json;
11. produces deterministic human-readable errors and non-zero exit status on violation.
```

The validator does not inspect Git author identity and does not claim semantic authorization beyond the declared contract.

## 6. Self-hosted first use

MC-0002 is the first guarded thread.

It used:

```text
review mode            REVIEWED
ChatGPT                TASK_OWNER / IMPLEMENTER
target write owner     ChatGPT
Claude                 REVIEWER
Claude write surface   MC-0002 numbered review messages only
```

The state guard implementation itself was therefore exercised by the collaboration process it is intended to govern.

Claude's review was direct rather than another independent-then-comparative pass. This tested a lower-overhead collaboration pattern and avoided repeating the high subscription cost observed in MC-0001.

## 7. Frozen validation gates

```text
MC-G01  V1 JSON Schema accepts the valid MC-0002 state.
MC-G02  thread_id must match the containing MC-NNNN directory.
MC-G03  task_owner, target_write_owner, next_expected_actor, and transition actor reference declared participants.
MC-G04  participant IDs are unique and roles are from the V1 vocabulary.
MC-G05  all declared write paths are normalized repository-relative paths without traversal.
MC-G06  secondary write surfaces that overlap target-state surfaces are rejected.
MC-G07  OPEN / ACTIVE / WAITING state requires a target write owner when target.write_paths is non-empty.
MC-G08  CLOSED state requires null target_write_owner and null next_expected_actor.
MC-G09  last_transition.to_state equals lifecycle_state and repository_head is a valid lowercase SHA.
MC-G10  guarded threads require adjacent THREAD.md.
MC-G11  malformed/unknown enum values and extra schema fields fail closed.
MC-G12  unit tests cover valid state and the principal invalid-state classes above.
MC-G13  dedicated GitHub Actions validation passes on Ubuntu and Windows.
MC-G14  docs/current_routing.json remains free of collaboration-lock/state fields.
MC-G15  documentation explicitly states that the mechanism is a coherence guard, not an authenticated distributed lock.
MC-G16  Claude directly reviews the concrete implementation and either accepts it or identifies a bounded required revision.
```

## 8. Outcome classification

Final classification:

```text
COLLABORATION_STATE_GUARD_ACCEPTED
```

Evidence:

```text
pre-implementation freeze       9da382d4011ff112b75dec9c456143d798336336
corrected green pre-review head a9efc43d7c441c8283d2cd954cc6fa1abd021689
workflow run                    32902050014
Ubuntu                          PASS
Windows                         PASS
focused unit tests              26 PASS per platform
Claude direct review commit     9cf393f74e02e167d2f80c0381742ebd7e0c318e
Claude review                   MC-G01 through MC-G16 satisfied
```

Claude directly inspected the schema, validator, tests, workflow, and live state rather than relying only on CI. It recommended `COLLABORATION_STATE_GUARD_ACCEPTED` and identified only the disclosed secondary-vs-secondary overlap limitation described above.

No frozen gate was weakened after execution.

## 9. Promotion boundary

The successful Specification 024 classification triggered the normal promotion audit for:

```text
DEVELOPMENT_METHOD.md
CONTINUITY.md
checkpoints/README.md
checkpoint metadata validator
docs/model_collaboration/README.md
DECISIONS.md
MAJOR_CHANGES.md
```

The resulting governed multi-model method is promoted separately through the normal repository process. No API orchestration or unattended scheduled-review execution is accepted by this specification.