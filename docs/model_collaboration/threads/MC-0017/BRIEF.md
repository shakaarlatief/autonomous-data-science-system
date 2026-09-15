# MC-0017 Brief: Independent W0 Production Implementation Architecture Design

**Thread:** MC-0017
**Date opened:** 2026-09-15
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Independent substantive base:** `1f09fc812e8d7b1f31771a8b545864b76ea61db0`
**Claude interaction:** existing persistent architecture-design session `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`

The session reuse is deliberate. This conversation has already carried the architecture-design lineage for MC-0011 through MC-0016 and has not hit its practical context limit. Preserving that Claude-local continuity is preferable here because the independent variable is exposure to ChatGPT's new W0 implementation design, not whether Claude remembers its own earlier reasoning.

**Authority:** Collaboration evidence only. D-035 selects Candidate 01 and Specification 028 is the frozen implementation/migration contract. This thread cannot switch operational authority or begin W1 migration.

**Purpose:** Obtain Claude's independent production W0 software/repository architecture before exposing ChatGPT's separately frozen W0 implementation design, then compare and reconcile the two before Codex implementation begins.

## 1. Independence rationale

Candidate 01 itself was already shaped through extensive ChatGPT/Claude collaboration, including MC-0011, MC-0013, MC-0014, MC-0015 and MC-0016. This thread is not another generic architecture review.

The genuinely new design layer is how the selected and qualified logical architecture should be realized as maintainable production W0 software under Specification 028.

ChatGPT has independently produced a W0 design after the base below. Claude must not see that design until Message 001 is frozen.

Reuse of the existing `claude-03` architecture-design conversation is intentional. Claude's own prior context from MC-0011 through MC-0016 is relevant design continuity, not contamination for this experiment. The independence claim is narrower: Claude must remain blind to ChatGPT's new W0 implementation design in Research 178 and descendant synthesis until Message 001 is frozen.

Substantive base:

```text
1f09fc812e8d7b1f31771a8b545864b76ea61db0
```

## 2. Current-branch routing boundary

From the current coordination branch, Claude may read only these routing/collaboration surfaces before Message 001 is frozen:

```text
docs/current_routing.json
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0017/BRIEF.md
docs/model_collaboration/threads/MC-0017/THREAD.md
docs/model_collaboration/threads/MC-0017/STATE.json
```

All substantive project/design reads must come from exact commit `1f09fc812e8d7b1f31771a8b545864b76ea61db0`.

Do not read descendant material before Message 001 is frozen, including:

```text
docs/research/178_chatgpt_independent_w0_implementation_architecture_design.md
Checkpoint 524 or later checkpoint bodies
current descendant CURRENT_STATE synthesis
any later MC-0017 ChatGPT comparison message
```

If the ChatGPT W0 design is exposed before Claude freezes its independent design, state `INDEPENDENT_W0_DESIGN_CONTAMINATED` rather than pretending the pass remained independent.

## 3. Governing sources at the independent base

At minimum inspect the exact-base versions of:

```text
docs/DECISIONS.md                      # especially D-035
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/144_whole_architecture_candidate_repository_native_semantic_sources.md
docs/research/145_candidate_01_requirements_v02_design_coverage_and_qualification_plan.md
docs/research/175_q10_final_multidimensional_qualification_result.md
docs/research/176_candidate01_owner_selection_and_implementation_migration_program_opening.md
docs/research/177_selected_candidate_physical_architecture_and_repository_contract_v01.md
docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
docs/README.md
docs/CONTINUITY.md
docs/model_collaboration/README.md
```

Use earlier MC-0013 through MC-0016 material when it helps recover why specific Candidate 01 choices exist. Do not assume the latest architecture can be understood only from summaries if the underlying collaboration reasoning matters.

Inspect relevant research prototype code at the exact base when useful, especially the Candidate 01 shadow/Q3/Q4/Q9/Q10 implementations, but treat them as evidence and algorithm examples rather than production architecture.

Do not restart broad web research unless a concrete implementation choice genuinely depends on external current evidence.

## 4. Independent design task

Design the W0 production implementation architecture you would actually build under Specification 028.

Do not optimize for agreement with Research 177's illustrative module list. Specification 028 fixes contracts and boundaries, but it deliberately leaves meaningful implementation decomposition open.

Address at least the following.

### A. Package and module architecture

Propose the actual Python/repository decomposition for `tools/project_knowledge/`.

Explain:

```text
module/layer boundaries
where I/O stops and semantic/domain logic begins
dependency direction
how circular dependencies are prevented
which parts should remain pure functions/value objects
whether a flat responsibility package or layered design is preferable
```

Do not put the subsystem into `src/ads_system/` unless you identify a genuine Specification 028 defect that must be amended first.

### B. Typed semantic model

Define the minimum internal representation for:

```text
selective semantic identity
authority class
profiles/kinds
scope
relations
source revisions
authority queries and receipts
workstreams + revisions/receipts
derived-view manifests
reconstruction contracts
captures/promotion state
```

Preserve selective identity. Do not quietly create a universal semantic-object model unless you can justify why that does not trigger the H3 reopening concern.

### C. Schema composition

Design the eight required profile schemas and any shared definitions.

Explain:

```text
what is genuinely common
how profile-specific fields stay separate
additionalProperties policy
versioning strategy
conditional validation
how schemas map into typed Python models
```

Look for places where Specification 028 may have over- or under-specified a profile.

### D. Markdown declaration parsing and source discovery

Design strict declaration extraction/parsing and repository discovery.

Answer:

```text
how governed sources are discovered without a manual central registry
how full rebuild avoids accidentally treating fixtures/generated/history as current authority
how changed-path incremental refresh identifies relevant sources
how native JSON carriers fit without two discovery systems drifting
how malformed marker structures and duplicate JSON keys fail
```

### E. Scope and authority semantics

Define implementable scope-matching semantics rather than saying only "match the scope."

Then design authority resolution for:

```text
REPLACE
SUPPLEMENT
SPECIALIZE
CORRECT
qualified JOINT_AUTHORITY
missing scope
conflicting authority
missing/stale authority
private-required unavailable authority
retrieval nominations that must not become authority
```

State the resolver algorithm and the minimum durable receipt.

### F. Identity transitions

Design current lookup plus history/provenance for:

```text
move/rename
representation replacement
merge
split
supersede
retire
redirect
```

The design should keep ordinary current lookup bounded without turning transition state into a universal manually maintained graph registry.

### G. Workstreams and concurrency

Design:

```text
DAG representation
parent/dependency semantics
pause/return/resume
active/blocked/completed/superseded states
interruption recovery
durable step receipts
expected-revision stale-write rejection
```

Specify what is pure semantic logic versus repository mutation orchestration.

### H. Derived-view engine

Design one architecture for:

```text
source catalog
identity index
authority index
workstream graph
subject index
risk/obligation index
current-state core JSON
current-state core Markdown
manifests
```

Explain how full rebuild and incremental refresh remain semantically equivalent rather than becoming two separate implementations.

Challenge whether every listed view should actually be persistently committed, while respecting Specification 028. If you think the specification should be amended, say so explicitly before implementation.

### I. Reconstruction planner

Design how a fresh collaborator gets task-shaped context for:

```text
BROAD_CONTINUATION
NARROW_GOVERNED_TASK
EXPLORATORY_RESEARCH
```

Distinguish free-text/model intent understanding from deterministic project-controlled closure.

Specify how must-load, optional, negative/do-not-load, freshness and receipt requirements are represented.

### J. Recent repository-self-model / Claude-history activation failure

A recent real failure occurred during this stage:

```text
The collaborator was asked whether Claude had already participated in Candidate 01 design.
Relevant Claude design history was durably preserved under docs/model_collaboration/threads/.
The collaborator initially answered as though Claude had mostly only participated in later qualification.
Only after the owner reminded the collaborator that the Claude threads themselves live in the repository did the collaborator inspect MC-0011 / MC-0013 / MC-0014 / MC-0015 / MC-0016 and correct the answer.
```

Important existing facts at the independent base:

```text
docs/README.md already describes docs/model_collaboration/ as a specialized governed domain
docs/CONTINUITY.md already requires docs/README.md early in bootstrap
docs/CONTINUITY.md already contains a model-collaboration continuity route
```

Therefore do **not** assume the failure proves a new topology registry is required.

Use it as design evidence. Ask:

> Does Candidate 01's planned source catalog + subject/navigation index + current/workstream/risk views + reconstruction planner already solve this class of failure when implemented correctly, or is some missing semantic self-model/topology concept actually needed?

If you propose a new mechanism, justify why existing Candidate 01 mechanisms cannot express it and why it would not recreate another hand-maintained global map.

Also propose the smallest W0 regression scenario that would falsify your answer.

### K. Capture/promotion

Design W0 production contracts for capture, review and promotion planning without performing real W1/W4 canonical promotion.

Preserve:

```text
capture is non-authoritative
promotion targets the natural canonical source
expected target revision is checked
accepted meaning/provenance survives capture archival/removal
```

### L. Public/private boundary

Design validation and resolver behavior for public/private dependencies without private leakage.

Preserve `RESOLVED_PRIVATE` semantics while failing visibly for consequential work that actually requires unavailable/stale private state.

### M. Validation and diagnostics

Propose the validation architecture across:

```text
local declaration/schema
cross-source identity/relation
authority/workstream semantics
public/private constraints
revision/freshness
view determinism
incremental/full equivalence
migration safety
```

Explain diagnostic structure and failure severity.

### N. CLI/application boundary

Design the CLI contracts required by Specification 028.

Explain which commands are read-only, staged-write, or future migration operations. Ensure no command can silently promote captures, mutate canonical authority, guess unresolved authority or switch operational authority.

### O. Architecture documentation and visualization

Design the durable repository architecture-documentation approach.

The owner wants both:

```text
one genuinely good whole-architecture overview
focused diagrams where detail would overload the overview
```

The visualization must live professionally in the repository, not only in chat.

Choose a diagram-source approach and explain how it stays version-controlled, reviewable and, where useful, renderable/reproducible.

Do not confuse a picture of physical files with the logical architecture itself.

### P. Test architecture and W0 gates

Map your implementation design to PKA-G001 through PKA-G017.

Identify:

```text
missing test class
weak gate
redundant gate
gate that should be amended before implementation
```

Do not weaken a gate merely because your preferred design makes it inconvenient.

### Q. Specification 028 amendment audit

End the substantive design with a concise list of any Specification 028 clauses you believe must be amended **before** W0 implementation.

Distinguish:

```text
REQUIRED_BEFORE_W0
SAFE_IMPLEMENTATION_FREEDOM
DEFER_TO_W1_OR_LATER
```

Do not reopen Candidate 01 merely because you prefer a different coding style. Reopen the logical architecture only if the production-design exercise exposes a genuine contradiction with the selected architecture/requirements.

## 5. Required conclusion

End Message 001 with:

1. your preferred W0 implementation architecture in compact form;
2. the three highest-risk implementation choices;
3. the strongest simplification you recommend;
4. the strongest place where more structure is actually necessary;
5. your disposition of the recent Claude-history activation failure;
6. whether Specification 028 requires amendment before coding;
7. whether Candidate 01/H3 should be reopened;
8. what you most want compared against ChatGPT's independent design after yours is frozen.

Then include exactly:

```text
INDEPENDENT_W0_DESIGN_CONTAMINATED: YES|NO
SPECIFICATION_028_AMENDMENT_REQUIRED_BEFORE_W0: YES|NO
LOGICAL_ARCHITECTURE_REOPEN_REQUIRED: YES|NO
H3_REOPEN_TRIGGERED: YES|NO
W0_IMPLEMENTATION_SAFE_AFTER_COMPARATIVE_RECONCILIATION: YES|NO
```

## 6. Required output

Write exactly one response at:

```text
docs/model_collaboration/threads/MC-0017/messages/001_claude_independent_w0_implementation_architecture.md
```

Include normal collaboration provenance and the exact independent base.

## 7. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0017/messages/**
```

Do not modify Specification 028, Research 144/177, Requirements V0.2, routing, current state, checkpoints, implementation code, tests, schemas or architecture docs.

## 8. After Message 001

After Message 001 is committed/pushed, ChatGPT will compare it with its independently frozen Research 178 design. Only then will the two designs be exposed comparatively and reconciled.

```text
MC0017=OPEN
MODE=INDEPENDENT_THEN_COMPARATIVE
PHASE=CLAUDE_INDEPENDENT_W0_IMPLEMENTATION_DESIGN
INDEPENDENT_BASE=1f09fc812e8d7b1f31771a8b545864b76ea61db0
CHATGPT_RESEARCH178=WITHHELD_UNTIL_MESSAGE_001_FROZEN
SPECIFICATION_028=FROZEN
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=CLAUDE_MESSAGE_001
```
