# Continuity

**Status:** Current canonical continuity procedure  
**Aligned development-method version:** 0.8  
**Last reviewed:** 2026-09-01

## Purpose

This document defines how the Autonomous Data Science System project continues across chats, sessions, models, branches, tool interruptions and context boundaries.

> A new collaborator must be able to reconstruct current project state from persistent repository artifacts without requiring the previous conversation or relying on model memory.

Long conversations are temporary working environments. Important knowledge must be durable, discoverable, correctly classified and routed to the right authority layer.

## Repository authority

The public `autonomous-data-science-system` repository remains the sole project-development repository and the durable authority for ADS code, architecture, specifications, decisions, checkpoints, public state and development history.

A private companion repository may preserve private knowledge needed for continuity, but it is not a second development repository and cannot silently override public project-development authority.

Conversation history may help, but must not override repository state. If repository artifacts disagree, resolve through status, scope, chronology, supersession and accepted authority. If material ambiguity remains, surface it explicitly rather than guessing.

## Separation of continuity concerns

Continuity reconstructs state from dedicated owners rather than duplicating volatile information inside this procedure:

```text
docs/README.md
    what repository/document families exist and what each is for

docs/current_routing.json
    compact machine-readable current pointer

docs/CURRENT_STATE.md
    current human-readable state and exact next step

docs/KNOWLEDGE_MAP.md
    evergreen subject library for broader/older knowledge

docs/CONTINUITY.md
    reconstruction, rotation and recovery procedure

docs/DEVELOPMENT_METHOD.md
    development, verification, preservation and reconciliation method
```

This file explains **how to use those surfaces**. It does not carry a copied current checkpoint, branch, review gate or latest test run.

## Private knowledge and operational-state continuity

Some operational facts are already resolved but cannot safely be committed to the public repository. Exact local filesystem paths and machine-specific storage coordinates are examples.

Continuity must distinguish:

```text
UNRESOLVED
    the project does not yet know or has not yet chosen the value

RESOLVED_PRIVATE
    the project already knows or has confirmed the value
    the exact value is intentionally withheld from public Git

UNAVAILABLE_TO_THIS_SURFACE
    the current chat/tool cannot read the private value directly
    this does not imply that the project value is unresolved
```

When `CURRENT_STATE.md` records a field as `RESOLVED_PRIVATE`, a new collaborator must not ask the human project owner to provide it again merely during reconstruction.

The accepted private-preservation architecture has two different private layers:

```text
PRIVATE COMPANION KNOWLEDGE REPOSITORY
    durable private project knowledge
    cross-chat reconstruction
    exact private paths and observations where appropriate
    knowledge only, not ADS development

LOCAL .ads-private STATE
    machine-local execution configuration
    direct command/runtime input
```

The governing companion-repository contract is:

```text
docs/private_companion/README.md
```

For the Source Vault bootstrap, the local operational-state contract is:

```text
docs/source_universe/LOCAL_PRIVATE_OPERATIONAL_STATE.md
```

The public repository remains authoritative for whether a value is resolved, what public gate passed or failed and what happens next. The private companion repository carries the durable private complement. The local `.ads-private` state carries execution-ready machine-local values.

Repository-first reconstruction is always **public-first**:

```text
1. reconstruct project state from the public ADS repository
2. determine whether the active public state references private knowledge
3. when relevant and accessible, retrieve the corresponding private companion state
4. use local .ads-private state when concrete local execution requires it
5. preserve the public/private authority boundary while continuing work
```

If a remote interaction surface cannot access the private companion repository or local state, preserve the public `RESOLVED_PRIVATE` status. Retrieve or request the exact value only when a concrete execution step actually requires it and no accessible private layer can provide it. Never silently downgrade a resolved private value to unknown because one tool cannot see it.

The private companion repository must never become a development fork. ADS code, tests, architecture, specifications, decisions, checkpoints and implementation evolution remain in the public repository.

### Public/private continuity anchor

When the private companion is deliberately reconciled to a public boundary, `CURRENT_PRIVATE_STATE.md` carries the public-safe synchronization anchor defined by Specification 026:

```text
Public continuity checkpoint
Public continuity commit
```

These values identify the public checkpoint and exact public commit against which the private continuity content was last reconciled. They contain no private path or secret.

Private continuity has an independent result:

```text
PRIVATE_CONTINUITY_INTEGRITY=PASS
PRIVATE_CONTINUITY_INTEGRITY=FAIL
PRIVATE_CONTINUITY_INTEGRITY=NOT_VERIFIED
```

`NOT_VERIFIED` means the current verification surface did not prove private freshness. It is not public failure and it does not make resolved private facts unresolved.

## Interaction/session naming

Visible conversations use the abstract convention:

```text
NN - Main Topic / Stage
```

The `/` in that notation means **main topic or stage**. It is not required literal punctuation. Use natural human wording for the descriptive title, including a conjunction such as `and` when that is clearer. A literal slash is used only when it is genuinely natural for the actual title. Historical exact titles are not rewritten merely for cosmetic punctuation consistency.

For example:

```text
14 - Codexless Write Validation and Source Vault Resume
```

is fully compliant with the convention.

Provider-local repository session IDs may use forms such as:

```text
chatgpt-13
claude-01
```

Canonical naming/provenance rules live in:

```text
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
```

Session identity is provenance/navigation metadata, not project authority.

### Automatic new-session allocation

Every newly opened persistent ADS conversation is a new interaction session for provenance, including a conversation opened only because the previous one hit a length/context limit while the underlying project stage remains unchanged.

A new session must **not** inherit the previous conversation's provider-local session ID or visible conversation title merely because `CURRENT_STATE.md` still records that previous session at reconstruction time.

During repository-first reconstruction of a new ADS conversation, the collaborator must proactively:

1. recognize that the interaction itself is new;
2. derive the next provider-local sequence number from the latest durable interaction provenance for that environment;
3. establish a fresh `NN - <natural descriptive title>` based on the active work reconstructed from the repository;
4. use that new session identity in the conversation immediately rather than continuing under the prior title;
5. once project-state alignment/authorization permits repository writes, update the live interaction context in `CURRENT_STATE.md` before substantive new durable work is attributed to the session.

The human project owner should not need to remind the collaborator to rotate the session ID/title after opening a continuation chat. This is part of the reconstruction procedure itself.

If the product UI cannot be renamed programmatically by the active tool surface, the repository must still establish and use the correct canonical title immediately; the UI limitation must never be used as a reason to reuse stale session provenance.

## Required new-session reconstruction

A new session must not begin by reading arbitrary recent files or trusting prior chat memory.

Bootstrap-critical authority is read directly in this order:

1. `README.md`
2. `docs/README.md`
3. `docs/CONTINUITY.md`
4. `docs/current_routing.json`
5. `docs/CURRENT_STATE.md`
6. `docs/KNOWLEDGE_MAP.md`
7. governing canonical documents/specifications routed by the current state
8. the current checkpoint/research boundary
9. specialized ledgers/manifests for the active topic
10. relevant private companion state when the public state explicitly indicates private knowledge is involved and the companion repository is accessible

`docs/CONTINUITY.md` is deliberately a direct mandatory first read. Bootstrap-critical authority must not depend on first discovering this procedure indirectly through `docs/README.md`.

Then use the subject library in `docs/KNOWLEDGE_MAP.md` to retrieve broader knowledge relevant to the task without needing to remember document numbers.

Structural reconstruction and semantic retrieval are deliberately separate jobs:

```text
docs/README.md    structure -> artifact role
CONTINUITY        bootstrap/recovery -> procedure
CURRENT_STATE     live state -> next action
KNOWLEDGE_MAP     subject -> relevant knowledge
```

The automatic new-session allocation rule above is part of this reconstruction. Prior session metadata found in `CURRENT_STATE.md` is evidence about the previous interaction, not permission to reuse it in the newly opened conversation.

When the current state reports a private value as already resolved, apply the private knowledge rule above before asking the project owner to repeat information.

## Standard continuation prompt

A provider-neutral continuation prompt may use:

> Continue the Autonomous Data Science System project from the repository. Treat the public `autonomous-data-science-system` repository as the sole project-development authority, not prior chat memory. First read README.md, docs/README.md, docs/CONTINUITY.md, docs/current_routing.json, docs/CURRENT_STATE.md, and docs/KNOWLEDGE_MAP.md. Reconstruct where the project currently stands, the important accepted conclusions and unresolved questions, and the next legitimate step. Treat this conversation as a new interaction session: proactively establish the next provider-local session ID and a fresh `NN - <natural descriptive title>` from the active repository state instead of reusing the previous session's title. Preserve `RESOLVED_PRIVATE` operational values as resolved even if this chat cannot see their exact local value. If the public state indicates that relevant private companion knowledge exists and the private repository is accessible, retrieve that private complement after the public reconstruction. Follow the project's development/preservation method. Do not make substantive project changes yet; first align with me on the current state.

The collaborator should expand through the Knowledge Map whenever the task touches older or adjacent knowledge.

## Public repository integrity

The canonical public integrity result is:

```text
PUBLIC_REPOSITORY_INTEGRITY=PASS|FAIL
```

The aggregate public gate covers the bounded contracts defined by Research 106 and Specifications 025/026, including family identity, prospective metadata, typed references, current-state/routing agreement and active-branch freshness, stable `current_boundary`, Knowledge Map integrity, checkpoint metadata and model-collaboration state.

A public `PASS` must come from the deterministic aggregate on the actual target. It must never be inferred because a workflow was intended to run or because individual files appear consistent by inspection.

The active development branch may be unprotected. A green GitHub Actions run is evidence, not proof that branch protection enforces the gate. Development and transition claims must describe the enforcement actually present.

## Chat-rotation preflight

A stronger deliberate-rotation result is:

```text
CHAT_ROTATION_PREFLIGHT=PASS|HOLD|FAIL
```

Interpretation:

```text
PASS
    public integrity passes and every continuity surface required for the rotation is verified sufficiently

HOLD
    public integrity passes, but required private continuity is NOT_VERIFIED or another non-failure transition obligation remains open

FAIL
    required public or verified-private integrity fails
```

`HOLD` is not repository corruption. It prevents a stronger rotation-ready claim until the outstanding continuity evidence is available.

## Proactive conversation rotation

Rotate a conversation before context quality becomes fragile. Typical signals include very long design sequences, repeated reconstruction difficulty, context-window warnings, or a natural stage boundary.

Before planned rotation:

1. preserve any meaningful checkpoint/open review state;
2. update `current_routing.json` and `CURRENT_STATE.md` if the live boundary changed;
3. ensure new durable knowledge is routed in the Knowledge Map when warranted;
4. preserve exact branch/commit/test/review state needed for continuation in the live state or governing evidence;
5. preserve material private continuity facts in the private companion repository when they cannot safely live publicly;
6. run the relevant public integrity gate on the actual target;
7. evaluate private continuity separately when required and accessible;
8. evaluate chat-rotation preflight and do not describe `HOLD` as `PASS`;
9. start the next conversation with repository-first reconstruction and automatic fresh session/title allocation.

If the boundary is unexpected, use the abnormal-interruption recovery procedure below instead of assuming the planned rotation sequence completed.

## Continuity across branches

Always distinguish:

```text
active development branch
promoted integration branch
main/default branch
historical experiment branches
```

The live branch/promotion pointer belongs in `docs/current_routing.json` and is explained in `docs/CURRENT_STATE.md`. Do not copy it into stable navigation documents unless a historical record specifically needs that exact context.

A new collaborator must not silently switch branches based on model memory.

Current-checkpoint freshness is branch-scoped: the active branch must point to its own maximum numbered checkpoint, while unrelated branches may legitimately preserve different checkpoint populations.

The private companion repository does not participate in ADS development branch selection. Its Git history is private-knowledge preservation history only.

## Checkpoint continuity

Checkpoints preserve meaningful project-state boundaries, not every commit.

Under the current Development Method, micro-iterations within one open review question are normally aggregated. Git preserves the exact implementation sequence; the checkpoint preserves the meaningful state transition.

When continuing an open checkpoint, distinguish:

```text
still the same review question
    bounded update/iteration may remain inside that checkpoint boundary

review interpretation/status/continuation changed materially
    create a new checkpoint
```

Historical closed checkpoints remain immutable except for explicit provenance/metadata repair that does not rewrite substantive history.

Checkpoint roles and metadata are defined by `docs/checkpoints/README.md`.

## Knowledge continuity

The global Knowledge Map is an evergreen semantic library, not a second current-state file.

Its continuity contract is:

```text
every numbered Foundation      routed to >=1 subject
every numbered Specification   routed to >=1 subject
every numbered Research record routed to >=1 subject
every numbered checkpoint      covered by >=1 semantic checkpoint range
important specialized indexes  remain globally reachable
```

A source may belong to multiple subjects. This is desirable when it improves retrieval.

Structural integrity is checked by:

```text
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

The map is navigation, not an authority database. A session still reasons from document status, scope, chronology and accepted contracts.

Private companion knowledge should be routed by stable public concepts/IDs rather than by duplicating the entire public Knowledge Map privately.

## Verification continuity

A new session must know not only whether tests passed, but **what verification tier actually ran**.

Preserve when relevant:

```text
verification tier  V0 / V1 / V2 / V3 / V4
exact tests/workflow run
implementation target SHA
human-review status
whether a broader gate is still required before acceptance/promotion
PUBLIC_REPOSITORY_INTEGRITY status when the integrity architecture is in scope
PRIVATE_CONTINUITY_INTEGRITY status when private reconciliation is in scope
CHAT_ROTATION_PREFLIGHT status when a deliberate rotation claim is in scope
```

Never describe a V1 targeted or V2 subsystem pass as a complete V3 integrated pass. Never describe `NOT_VERIFIED` or `HOLD` as `PASS`.

Risk-scaled verification is governed by `docs/DEVELOPMENT_METHOD.md`.

Cockpit selector/workflow:

```text
scripts/select_cockpit_verification.py
.github/workflows/cockpit-reintegration-fidelity.yml
```

## Model-collaboration continuity

When a collaboration thread is active, reconstruct it from:

```text
docs/model_collaboration/threads/<THREAD>/STATE.json
docs/model_collaboration/threads/<THREAD>/THREAD.md
docs/model_collaboration/REVIEW_INBOX.md
```

Important continuity fields include task owner, target-state writer, next expected actor, independence/exposure status, frozen review base, allowed secondary write surfaces and unresolved obligations.

A review tied to one immutable target must not be silently applied to a newer descendant.

Canonical collaboration method:

```text
docs/model_collaboration/README.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
```

## Recovery after unplanned context loss

When a chat ends unexpectedly without evidence of a partially executed mutation:

1. identify the public ADS repository and likely active branch;
2. perform the mandatory bootstrap reads, including `docs/CONTINUITY.md` directly;
3. establish a fresh provider-local interaction-session ID and conversation title for the newly opened recovery chat instead of reusing the ended session's metadata;
4. preserve any `RESOLVED_PRIVATE` values as resolved;
5. if the public state indicates relevant private companion knowledge and that repository is accessible, retrieve the private complement;
6. consult local private operational-state contracts only when concrete local execution requires machine-local values;
7. verify the current checkpoint exists rather than assuming the final chat message committed successfully;
8. inspect recent Git chronology when needed;
9. separate implementation state from documentation/provenance state;
10. detect stale routing/session metadata;
11. use the Knowledge Map to reconstruct older governing knowledge by subject;
12. preserve the exact surviving product/experiment boundary;
13. repair continuity metadata conservatively;
14. do not recreate substantive decisions from memory if the repositories already contain stronger evidence.

Important distinction:

```text
substantive preservation failure
    knowledge/implementation actually missing

routing/provenance drift
    knowledge exists but discovery or current pointers are stale

private-value visibility gap
    exact value is intentionally private or inaccessible to this surface
    public state still records whether it is resolved
```

Routing/provenance drift should be repaired, not treated as lost knowledge. A private visibility gap should not be mislabeled as unresolved project knowledge.

## Recovery after abnormal execution interruption

An outage, tool failure, unexplained task termination or user interruption can occur during a multi-step repository mutation after some durable writes have completed but before later writes, verification or reconciliation.

Do not trust the interrupted conversation's implication of completion and do not blindly rerun the entire intended plan.

Use this bounded recovery sequence:

1. inspect current branch HEAD before further mutation;
2. identify the last independently trusted durable boundary;
3. enumerate commits, files and actions that actually completed after that boundary;
4. compare completed work with the intended staged plan;
5. classify every apparent inconsistency as one of:
   - `EXPECTED / DEFERRED`
   - `KNOWN DEFECT / PLANNED REPAIR`
   - `INTERRUPTION RESIDUE`
   - `NEW UNPLANNED DEFECT`
6. repair only findings appropriate to the current stage;
7. rerun required verification rather than inheriting pre-interruption success claims;
8. preserve a recovery record when the interruption materially affects project continuity.

A user interruption is allowed and does not itself imply Git corruption. Completed Git operations remain durable. This protocol exists to prevent a partially completed logical workflow from being mistaken for a completed transition.

## Periodic reconciliation

At meaningful stage boundaries, verify separately:

```text
CURRENT_STATE / current_routing agree
active-branch current checkpoint is fresh
current_boundary is a stable semantic label
root README remains stable and non-duplicative
docs/README still describes the actual repository artifact families
KNOWLEDGE_MAP retains exhaustive subject coverage
important new research/specifications/foundations are topic-routed
checkpoint ranges cover newly created checkpoint numbers
canonical docs have not become stale
specialized ledgers remain linked
interaction provenance is coherent
resolved-private operational state is not being mistaken for unresolved state
private companion knowledge is not competing with public development authority
checkpoint metadata passes
collaboration obligations are discoverable
verification tier/status is represented accurately
public integrity is verified when the transition requires it
private continuity is evaluated separately when relevant
chat-rotation preflight is not overclaimed
```

Do not run the whole reconciliation after every small implementation commit.

## Version relationship

Development Method v0.8 strengthens the v0.7 information architecture without creating a second authority database:

```text
structure     docs/README.md
live state    CURRENT_STATE.md + current_routing.json
subject map   KNOWLEDGE_MAP.md
procedure     CONTINUITY.md
method        DEVELOPMENT_METHOD.md
public gate   repository-integrity aggregate
private gate  separate private-continuity evaluator
transition    chat-rotation preflight
```

The private companion repository remains a private knowledge complement and does not change public development authority.

Deep preservation and integrity rationale remains in:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/research/106_governed_repository_integrity_and_continuity_bootstrap_hardening.md
docs/research/107_post_outage_repository_integrity_recovery_audit.md
docs/specifications/025_v1_governed_repository_integrity_and_continuity_hardening.md
docs/specifications/026_v1_repository_integrity_recovery_amendment.md
```
