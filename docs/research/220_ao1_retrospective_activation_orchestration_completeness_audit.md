# Research 220: AO-1 Retrospective Activation / Orchestration Completeness Audit

**Date:** 2026-09-20
**Status:** AO-1 COMPLETE / AO-2 CAPABILITY-BOUNDARY SYNTHESIS NEXT / W5-F0 REMAINS PAUSED
**Program:** Research 219
**Audit base:** `c1794e44e8abc6e39c97201d850bc8d68608ba29`
**Current operational authority:** current continuity architecture
**Frozen W5 information-architecture baseline:** Research 218
**Machine-readable capability matrix:** `docs/research/project_knowledge_activation_orchestration/AO1_COMPLETENESS_MATRIX_V01.json`
**Backlog status snapshot:** `docs/research/project_knowledge_activation_orchestration/AO1_ARCHITECTURE_BACKLOG_STATUS_SNAPSHOT_V01.json`
**Open-question status snapshot:** `docs/research/project_knowledge_activation_orchestration/AO1_OPEN_QUESTION_STATUS_SNAPSHOT_V01.json`
**Scope:** Reconstruct the original activation/orchestration obligations and every current deferred mechanism materially related to them, compare those obligations with Candidate 01's implemented production substrate and accepted procedures, identify scheduling/implementation gaps, and establish the evidence boundary for AO-2 without selecting a control-plane architecture.
**Authority:** Research/audit result under Research 219. This record does not amend Research 218, retroactively invalidate W0-W4, select the successor orchestration bridge, or authorize an authority switch.

## 1. Why AO-1 needed to be retrospective rather than inventive

Research 219 opened because the project reproduced a known failure class while constructing the architecture intended to solve it: relevant durable knowledge existed, but the owner had to remember that it existed before it entered reasoning.

The wrong response would have been to immediately invent an intent router from the current conversation.

AO-1 instead asks:

```text
What did the original redesign actually require?
What mechanisms did Candidate 01 design?
What was genuinely implemented?
What was only qualified in a bounded experiment?
What remains a manual procedure?
What was explicitly deferred?
What was accidentally left unscheduled?
What must become operational before W6 or before ordinary W5 migration resumes?
```

## 2. Audit corpus

AO-1 inspected the current authoritative/deferred registers plus the architecture-design and qualification chain beginning with Research 124.

Primary corpus:

```text
docs/research/124_scalable_repository_knowledge_architecture_and_reconstruction_redesign.md
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/130_requirements_evidentiary_provenance_reconciliation.md
docs/research/144_whole_architecture_candidate_repository_native_semantic_sources.md
docs/research/145_candidate_01_requirements_v02_design_coverage_and_qualification_plan.md
docs/research/146_mc0016_adversarial_candidate_review_disposition_and_design_amendments.md
docs/research/159_whole_architecture_evidence_reconciliation_and_selection_blocker_audit.md
docs/research/165_q9_migration_authority_switch_rollback_result.md
docs/research/168_q1_q2_q5_integrated_fresh_collaborator_result_and_revision_binding_amendment.md
docs/research/170_q4_real_workstream_concurrency_interruption_result.md
docs/research/171_whole_architecture_evidence_reconciliation_v03_final_pre_q10_gap_selection.md
docs/research/175_q10_final_multidimensional_qualification_result.md
docs/research/177_selected_candidate_physical_architecture_and_repository_contract_v01.md
docs/research/178_chatgpt_independent_w0_implementation_architecture_design.md
docs/research/179_mc0017_reconciled_w0_implementation_architecture.md
docs/research/190_w0_deterministic_cli_surfaces_g014_result.md
docs/research/193_w0_complete_unit_suite_g017_and_w0_acceptance_result.md
docs/research/206_w5_future_knowledge_information_architecture_and_authoring_design.md
docs/research/208_w5_physical_authoring_v02_freeze_and_empirical_gate_program.md
docs/research/218_w5_final_information_architecture_reconciliation_and_target_freeze.md
docs/research/219_activation_orchestration_self_hosting_bootstrap_program.md
```

Current canonical/deferred control surfaces inspected:

```text
docs/OPEN_ARCHITECTURE_BACKLOG.md     all AB-001..AB-032 status rows
docs/OPEN_QUESTIONS.md                all current Q-* status rows
docs/DECISIONS.md                     especially D-024, D-032, D-034, D-035
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/model_collaboration/README.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/local_execution/OPERATIONS.md
docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
docs/project_knowledge/architecture/reconstruction_and_action.md
docs/research/PROJECT_KNOWLEDGE_FAILURE_CORPUS.md
```

Production implementation surface inspected:

```text
tools/project_knowledge/
schemas/project_knowledge/
tests/unit/test_project_knowledge_*
current persistent generated views
current CLI command inventory
```

A repository-wide signal scan over Research 124 onward plus the canonical registers was also used to locate `defer`, `reopen`, `future`, `not yet`, `remains open`, `trigger` and related wording. High-signal items were then inspected in context.

AO-1 does not claim that every historical sentence in all 557 numbered checkpoints was reread. The current registers and accepted research chain are specifically intended to carry unresolved obligations forward; where those surfaces pointed to deeper history, AO-1 followed the evidence.

## 3. Important methodological correction: maturity and urgency are different axes

Research 219's opening classification list mixed implementation maturity with scheduling urgency.

For AO-1 they are separated.

Implementation maturity:

```text
ALREADY_SOLVED
PARTIALLY_SOLVED
SUBSTRATE_EXISTS_BUT_BEHAVIOR_MISSING
DEFERRED_WITH_TRIGGER
UNSCHEDULED
OBSOLETE
```

Scheduling urgency:

```text
BOOTSTRAP_BLOCKER
REQUIRED_IN_BOOTSTRAP_STAGE
REQUIRED_BEFORE_W6
INTEGRATE_WHEN_RELEVANT
MONITOR
OPTIONAL_DEFERRED
OUT_OF_SCOPE_CURRENT
```

This matters because, for example, Git branch lifecycle is `UNSCHEDULED` but explicitly `REQUIRED_BEFORE_W6`, while autonomous Codex wakeup is `DEFERRED_WITH_TRIGGER` and `OPTIONAL_DEFERRED`.

## 4. AO-1 capability inventory

The matrix contains 31 capability families.

Current implementation-maturity distribution:

```text
ALREADY_SOLVED                         1
PARTIALLY_SOLVED                     13
SUBSTRATE_EXISTS_BUT_BEHAVIOR_MISSING 7
UNSCHEDULED                           7
DEFERRED_WITH_TRIGGER                 3
OBSOLETE                              0
TOTAL                                31
```

Current urgency distribution:

```text
BOOTSTRAP_BLOCKER             11
REQUIRED_IN_BOOTSTRAP_STAGE   11
REQUIRED_BEFORE_W6             1
INTEGRATE_WHEN_RELEVANT        4
MONITOR                        2
OPTIONAL_DEFERRED              2
TOTAL                          31
```

The result is not that Candidate 01 lacks substance. The result is that many critical semantic primitives exist, while the layer that causes those primitives to activate from ordinary project events remains incomplete.

## 5. The original redesign explicitly targeted cognitive activation

Research 124's baseline diagnosis was already:

```text
durability                  STRONG
structural integrity        STRONG
basic discoverability       STRONG BUT SCALING
high-recall reconstruction  PARTIAL
context efficiency          UNDER PRESSURE
hierarchical traversal      PARTIAL / DOMAIN-SPECIFIC
relationship semantics      PARTIAL
nested resume semantics     WEAK / PROSE-HEAVY
cognitive activation        WEAKLY VERIFIED
synthesis lifecycle         PARTIAL / MANUAL
```

Research 124 explicitly warned that structural validators do not prove that a fresh collaborator:

```text
formed an adequate project model
selected the correct authority
noticed a relevant known weakness
consumed the governing procedure before instructions
understood parent/child workstream continuation
avoided stale synthesis
used appropriate context
or knew what remained unread
```

Therefore the present Research 219 stage is not scope inflation. It returns to a requirement that existed before Candidate 01 was selected.

## 6. Frozen requirements that make the control-plane problem mandatory

The most direct Requirements V0.2 obligations are:

```text
KA-R02  stable project-controlled bootstrap
KA-R03  conversation/model independence
KA-R04  task-shaped safe orientation
KA-R05  progressive disclosure
KA-R06  active route reconstruction
KA-R07  governing/risk-bearing discovery without filename knowledge
KA-R08  observable reconstruction/authority receipts
KA-R09  consequential authority activation + action-contract fidelity
KA-R10  known-risk/evolution-trigger activation without human memory
KA-R25..29 workstream lifecycle / dependencies / interruption / concurrency
KA-R34  saturation/pressure observability
KA-R36  provider/tool portability
KA-R40  structural + behavioral qualification
KA-R41  multidimensional reconstruction qualification
KA-R42  degraded-mode safety
KA-R43..45 migration / old authority / self-hosting evolution
KA-R48  conversation-born capture / consolidation / promotion
KA-R50  recurring active-surface consolidation
```

The requirement that most directly matches the 2026-09-20 incident remains KA-R10:

> Material known risks/reopen triggers must activate when task/conditions intersect them; the architecture must not depend on a human remembering that such a warning exists.

## 7. Major AO-1 discovery: the reconstruction planner is selected architecture but not production implementation

This is the strongest concrete gap found by AO-1.

Specification 028 section 26 says the implementation **MUST** support:

```text
BROAD_CONTINUATION
NARROW_GOVERNED_TASK
EXPLORATORY_RESEARCH
```

and a reconstruction contract capable of carrying:

```text
task class
minimum safe orientation
must-load governing sources
optional/supporting evidence
negative/do-not-load guidance
freshness requirements
receipt requirements
fail/escalate conditions
```

Research 178 independently designed a production `reconstruction.py`, `ReconstructionContract`, reconstruction tests, and `reconstruct` CLI.

Research 179 then accepted:

```text
deterministic task-shaped reconstruction after explicit TaskIntent
PKA-W0-J1 activation/history regression
```

PKA-W0-J1 specifically required that a project-history/collaboration task surface relevant collaboration sources **without the human supplying a repository path**.

Yet the current production package has no `reconstruction.py`, no production `TaskIntent`/`ReconstructionContract`, no `reconstruct` CLI, and no production PKA-W0-J1 regression.

Specification 028 section 32 also requires V1-equivalent CLI surfaces for:

```text
resolve-authority <task-spec>
reconstruct <task-spec>
migration-audit
```

while the accepted G014 production CLI currently exposes only:

```text
validate
rebuild
refresh
check-freshness
```

### 7.1 Why W0 was still formally accepted

This finding must not be rewritten into a false historical claim.

Specification 028's executable W0 acceptance list PKA-G001..PKA-G017 did **not** include a reconstruction-planner gate. Research 193 correctly accepted W0 against the gates that were actually frozen.

The defect is therefore better described as:

```text
selected V1 logical contract
    + reconciled W0 implementation design obligation

not carried into

executable W0 gate schedule / production implementation
```

rather than:

```text
W0 secretly failed a gate that existed
```

This is a planning/scheduling/implementation gap requiring prospective reconciliation, not retroactive history rewriting.

## 8. Authority machinery exists but invocation is missing

Candidate 01's production authority layer is substantial.

It already provides:

```text
AuthorityQuery
deterministic authority resolution
AuthorityReceipt
source revision binding
scope discrimination
joint-authority semantics
private-state evidence
governing-procedure ActionContract
activated mandatory constraints
explicit constraint precedence
fail-visible unresolved statuses
```

Research 168 also demonstrated a real bounded fresh-collaborator case where the correct task path:

```text
resolved the Source Vault governing procedure
kept Course 2 BLOCKED
activated three known risk triggers
rejected a stale derived authority source
emitted an authority receipt
and preserved capture/promotion separation
```

But that proves:

```text
IF the interaction enters the correct task/reconstruction path
THEN authority/risk activation can succeed
```

not:

```text
ordinary owner intent reliably causes that path to run
```

The latter is the current gap.

## 9. Action-contract fidelity remains only partially operational

The production resolver activates structured procedure constraints and ordering.

However AO-1 did not find a general production execution-plan or final-guidance conformance stage that guarantees those activated constraints survive into the final instructions/action dispatch.

This distinction matters because the historical BL-001 failure showed:

```text
correct source activation
    !=
correct final action/guidance fidelity
```

AO-2 must therefore preserve both:

```text
ACTIVATE the governing contract
AND
ENFORCE / VERIFY conformance of what is about to be said or done
```

## 10. Risk/reopen substrate exists, but only for already-migrated declarations

Production supports:

```text
risk_or_reopen_triggers
risk_obligation_index
```

and the current generated index contains real Source Vault risks/obligations.

But AB-027's larger target has not been completed.

Deferred limitations and reopening conditions distributed across foundations, decisions, research, specifications, open questions and backlog items have not been reconciled into a current monitorable trigger surface.

This is why AB-027 itself could be durably present and still fail to activate.

## 11. Workstream semantics are real, but process orchestration is not

Candidate 01 has production and real-evidence support for:

```text
workstream identity
parent/child semantics
multiple dependencies
pause reason
return condition
resume target
readiness
active route projection
durable interruption receipts
stale update rejection
```

Research 170 provides strong real-source evidence for the workstream mechanics.

But the system does not yet generally recognize an owner event and decide:

```text
open child workstream
pause parent
route incident elsewhere
close child
resume exact parent
```

That higher-level orchestration remains procedural/model-driven.

## 12. Collaboration governance is mature; collaboration activation is not

D-034 and the canonical collaboration protocol already provide a strong method:

```text
SOLO
REVIEWED
INDEPENDENT_THEN_COMPARATIVE
COORDINATED_HANDOFF
ADVERSARIAL_REVIEW
exact immutable review targets
one target-state writer
deferred review gates
independence/contamination rules
durable thread provenance
```

Development Method also gives substantive routing guidance:

```text
ChatGPT / Claude    architecture, research, challenge, synthesis
Codex               bounded implementation / repair
ChatGPT             independent implementation review
```

and says especially consequential architecture should prefer independent capable-model reasoning.

The missing behavior is not 'invent collaboration rules'.

It is:

```text
recognize that the present event satisfies those rules
and activate the appropriate collaboration path without owner reminder
```

The Chat 27 AB-031 miss is direct evidence of that gap.

## 13. Manual Codex relay is not itself a defect

AB-003, AB-004 and AB-006 were deliberately demoted after the owner accepted manual ChatGPT-to-Codex prompt relay and native Codex Remote as a sufficient current operating model.

Therefore Research 219 must not silently turn:

```text
automatic Codex dispatch
autonomous ChatGPT wakeup
active-turn writer transfer
```

into new correctness requirements.

The control plane may decide that bounded implementation should route to Codex while actual transport remains manual owner relay.

This distinction protects owner choice and avoids solving optional convenience before the core activation problem.

## 14. Interaction continuity is only partially represented

Current continuity/provenance already handles:

```text
fresh provider-local session identity
conversation title
repository-first continuation
planned chat rotation
abnormal interruption recovery
collaboration-thread provenance
```

but there is no first-class non-authoritative interaction envelope that can say:

```text
this interaction contains unresolved unpromoted material
content is / is not recoverable
pending capture/review exists
return condition is X
last durable receipt is Y
```

without promoting the conversation itself.

The need is now stronger than speculative because the owner had to paste the Chat 26 conversation into Chat 27 to restore nuance that AB-031 had compressed.

## 15. Git lifecycle remains genuinely unscheduled

AB-032 remains open and explicitly distinguishes:

```text
branch-state knowledge
    current branch/commit carrying work

from

branch-lifecycle policy
    create / continue / rotate / merge / archive / retire
    publication cadence
    bounded local-only exceptions
    unpublished-commit accumulation
    remote reconciliation
    destructive-cleanup evidence
```

Current Git tooling and branch-state preservation do not answer that policy question.

AB-032 already says this should preferably be addressed before W6 or as part of AB-031.

AO-1 therefore marks it `REQUIRED_BEFORE_W6` and naturally integrated into Research 219's control-plane design.

## 16. Break-glass recovery has strong procedures but no event router

`docs/local_execution/OPERATIONS.md` provides exact runtime recovery authority. Runtime self-maintenance is live-qualified, and the GitHub parity program gives an independent public-repository access path.

Yet the owner still has to recognize:

```text
this is an operational incident
the primary workstream should pause
the recovery procedure should activate
an independent access path should be used
and the original workstream must later resume
```

Research 219 should integrate those already-good procedures rather than create new recovery prose.

## 17. Open Architecture Backlog audit

AO-1 machine-froze all 32 current AB items so the control-plane work does not accidentally treat every open item as equally relevant.

### 17.1 Core bootstrap items

```text
AB-022  authority routing / required-read enforcement     P0
AB-023  backlog vs open-question discoverability          P1
AB-024  high-recall reconstruction                        P0
AB-025  nested workstream / resume                         P1
AB-026  navigation saturation / hierarchy                 P1
AB-027  deferred risk / evolution triggers                 P1
AB-031  intent-driven interaction orchestration            P0
AB-032  Git branch lifecycle                               P2 / before W6
```

### 17.2 Adjacent mechanisms that should integrate when useful

```text
AB-008  MCP schema/projection lifecycle
AB-012  lower-level reviewer/auto-review behavior
AB-017  host authority taxonomy
AB-018  upstream Codex reconciliation
AB-019  exact capability/version probes
AB-021  developer-MCP privacy/consent characterization
AB-030  governed validation -> GitHub CI evidence publication
```

### 17.3 Explicitly optional direct-Codex conveniences

```text
AB-003  autonomous assistant wakeup
AB-004  active-turn writer transfer
AB-006  direct task recovery
```

These must remain deferred unless Research 219 discovers a new first-order need.

### 17.4 Other monitored interaction/runtime features

```text
AB-011 steer/follow-up queues
AB-013 spectator/cross-client sync
AB-014 long-thread history/restart APIs
AB-015 multi-agent/subagent lineage
```

These may inform later implementation but are not prerequisites for the core control plane.

## 18. Open Questions audit

AO-1 also machine-froze all 31 current open-question status rows.

The most directly relevant unresolved questions are:

```text
Q-003  What should the human's role be?
Q-006  How should relevant investigations be activated?
Q-010  When is independent review required?
Q-021  How should model and tool providers be selected?
Q-028  How should project intent be represented?
Q-054  How far should governed multi-model collaboration be mechanized?
```

Research 219 must not accidentally answer product-level versions of these questions while solving the narrower **project-development control plane**.

In particular:

```text
project-development intent routing
    != final ADS product ProjectIntent schema

project-development Claude/Codex routing
    != final analytical model-provider policy
```

but the project-development system can act as a live laboratory for those broader product questions.

## 19. Foundation 014's escalation triggers are now stronger evidence, not stale history

Foundation 014 deliberately deferred stronger infrastructure until evidence appeared such as:

```text
manual routing maintenance becoming unreliable
frequent failure to discover relevant existing knowledge
large dependency networks becoming unsafe in prose
reconciliation becoming too expensive
multiple concurrent collaborators needing stronger semantics
```

Research 124 already concluded several trigger classes were observed.

The Chat 27 activation miss adds another concrete instance.

This does not imply a graph/vector/database solution. It means the earlier defer-until-pressure condition is no longer a valid reason to postpone serious activation/orchestration work.

## 20. Architecture self-observation is still missing

The historical failure corpus is strong at preserving owner-caught incidents, but AO-1 found no operational mechanism that automatically records:

```text
ACTIVATION_MISS
ROUTING_MISS
KNOWN_TRIGGER_NOT_ACTIVATED
REPEATED_EXCEPTION
OWNER_REMINDER_REQUIRED
```

or their equivalents.

Without such evidence, the architecture can continue failing in exactly the domain it is intended to improve while only the owner notices the pattern.

AO-2 must decide what should become first-class evidence versus mere telemetry, and how to avoid creating a noisy self-monitoring bureaucracy.

## 21. Production navigation remains an important dependency, but not the control plane itself

T1/Research 217 and Research 218 froze the semantic-subject direction, while W5-F0 was supposed to implement:

```text
canonical subject catalog
source-owned semantic memberships
subject_index V2
cross-source navigation validation
```

AO-1 confirms this work is still useful because semantic/hierarchical navigation can improve activation candidate discovery.

But W5-F0 alone would not solve:

```text
when to invoke reconstruction
what event occurred
which risks are mandatory
whether Claude is required
whether architecture should reopen
whether a recovery workflow should run
what to preserve after the interaction
```

That is why W5-F0 remains paused rather than abandoned.

## 22. Specification 028 command-surface debt

The current production CLI intentionally accepted at G014 contains:

```text
validate
rebuild
refresh
check-freshness
```

while Specification 028's V1 command contract additionally requires equivalents of:

```text
resolve-authority
reconstruct
migration-audit
```

AO-1 records this as a current prospective implementation obligation.

The reconstruction and authority commands directly belong in the Research 219 control-plane program.

`migration-audit` may be implemented in the same stage or in later W5 migration work, but it must not disappear before W5 acceptance/cutover qualification.

## 23. AO-1 bootstrap blockers

The current matrix identifies eleven immediate blockers that AO-2/AO-3 must resolve at the architecture level:

```text
AO-C02  owner-intent / project-event interpretation
AO-C03  task-shaped reconstruction planner
AO-C04  consequential authority preflight
AO-C06  known-risk / reopen-trigger activation
AO-C07  evolution-trigger register / monitoring
AO-C08  frozen-architecture evolution protocol
AO-C10  intent-to-process routing
AO-C16  collaborator routing
AO-C21  reconstruction/activation observability
AO-C28  backlog/open-question relevance activation
AO-C30  successor control-plane bridge before authority switch
```

These are not eleven independent services. AO-2 should search for a small coherent architecture that closes several through one control loop.

## 24. What AO-1 does not elevate into blockers

AO-1 explicitly rejects scope inflation.

Not immediate blockers:

```text
automatic Codex dispatch
assistant autonomous wakeup
active-turn writer ownership transfer
shared spectator synchronization
same-turn steering
multi-agent UI/lineage
general host-machine authority
automatic scheduled Claude review
automatic canonical promotion
graph/vector/database infrastructure by default
```

These remain optional/deferred unless later evidence demonstrates that the core control plane cannot meet its goals without them.

## 25. Planning failure exposed by AO-1

The most important process lesson is that architecture qualification and implementation scheduling were not perfectly aligned.

Candidate 01 achieved a legitimate 67/67 logical qualification under the frozen scenarios. Later W0 implementation also legitimately passed all PKA-G001..G017 gates.

But a logical requirement can still remain physically unscheduled when:

```text
the logical architecture names it
the implementation design preserves it
the executable gate list omits it
and later migration work does not explicitly reintroduce it
```

The reconstruction planner is the concrete example.

This is itself a control-plane requirement:

> The project needs a way to reconcile `accepted design obligation -> implementation gate -> implementation evidence -> operational activation`, not merely preserve each layer separately.

AO-2 should therefore include **obligation-to-realization closure** as a control concern, even though Research 219's opening list did not name it separately.

## 26. AO-1 result

```text
AO_1_RETROSPECTIVE_COMPLETENESS_AUDIT=COMPLETE
CAPABILITY_ROWS=31
ARCHITECTURE_BACKLOG_ITEMS_SNAPSHOTTED=32
OPEN_QUESTION_ROWS_SNAPSHOTTED=31
RECONSTRUCTION_PLANNER_SELECTED_LOGICAL_CONTRACT=true
RECONSTRUCTION_PLANNER_PRODUCTION_IMPLEMENTATION=false
PKA_W0_J1_PRODUCTION_REGRESSION=false
RESOLVE_AUTHORITY_CLI=false
RECONSTRUCT_CLI=false
MIGRATION_AUDIT_CLI=false
CURRENT_AUTHORITY_RESOLVER=true
CURRENT_WORKSTREAM_ENGINE=true
CURRENT_RISK_INDEX=true
GENERAL_OWNER_INTENT_TO_ACTIVATION_LOOP=false
RESEARCH218=FROZEN_BASELINE_RETAINED
W5_F0=PAUSED_BEFORE_IMPLEMENTATION
AUTHORITY_SWITCH_ALLOWED=false
NEXT=AO_2_CAPABILITY_BOUNDARY_AND_FAILURE_TAXONOMY
```

## 27. AO-2 handoff

AO-2 should not immediately choose an implementation stack.

It should convert AO-1 into a smaller architecture-neutral requirement/failure model by answering:

```text
Which missing capabilities are actually one control-loop responsibility?
Which decisions require deterministic project logic?
Which parts may remain model-assisted?
Which signals must be monitored continuously or at governed boundaries?
Which event classes deserve first-class representation?
Which failures must fail closed?
Which processes can remain manual transport while routing becomes automatic?
Which deferred items stay outside this stage?
What is the smallest bridge that can become operational before authority switch?
How will the project prove that owner reminders are no longer a required control mechanism?
```

Only after AO-2 should AO-3 freeze a conceptual control-plane candidate.
