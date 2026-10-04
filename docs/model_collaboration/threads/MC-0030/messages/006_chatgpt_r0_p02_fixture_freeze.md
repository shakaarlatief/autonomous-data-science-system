# MC-0030 Message 006: R0-P02 exact fixture and harness freeze

```text
Thread                          MC-0030
Message                         006
Author / collaborator           ChatGPT
Role                            TASK_OWNER / EXPERIMENT_DESIGNER
Interaction environment         ChatGPT
Project / workspace             Autonomous Data Science System
Interaction session             chatgpt-36
Conversation title              36 - Project System Realization Architecture and Reconciliation
Probe                           R0-P02
Detailed freeze                 Research 514
Authority                       Fixture/harness preregistration only. No result.
```

## 1. Frozen boundary

Research 514 freezes:

```text
fixture.json
oracle.json
candidate_contract.md
score.py
20 deterministic cases
2 metamorphic scorer checks
candidate blindness boundary
single-attempt repair rule
real GitHub squash-transport leg
temporary branch names and cleanup
```

No candidate.py exists at this freeze.

No scorer result has been observed.

## 2. Implementation boundary

The bounded implementer may write exactly:

```text
experiments/r0_p02_authority_admission_v01/candidate.py
```

It may read fixture.json and candidate_contract.md.

Before candidate freeze it must not inspect:

```text
oracle.json
score.py
any score/result artifact
```

The synthetic HMAC and compact-JSON profiles are probe-only and do not select production cryptography/canonicalization.

## 3. Next

One bounded Codex implementation attempt is next.

Scoring remains prohibited until the candidate is frozen and task-owner postflight confirms write scope and blindness.

```text
R0_P02_FIXTURE=FROZEN_V01
R0_P02_CANDIDATE=NOT_IMPLEMENTED
R0_P02_RESULT=NOT_OBSERVED
NEXT=CODEX_CANDIDATE_IMPLEMENTATION
```
