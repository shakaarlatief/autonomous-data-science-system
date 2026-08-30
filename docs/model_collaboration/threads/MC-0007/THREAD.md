# MC-0007 Thread: Source Universe Pre-Deployment Recovery Hardening

**Thread:** MC-0007  
**Status:** ACTIVE  
**Mode:** COORDINATED_HANDOFF  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Implementation base:** `65bf6198ea77565551e4c4dabe690ce204497d79`

## Purpose

Carry the accepted MC-0006 recovery-hardening findings through implementation and real local Windows verification without crossing into permanent Source Vault deployment.

## Roles

```text
ChatGPT / chatgpt-10
    TASK_OWNER
    accepted and bounded F1-F4
    reviews Claude Code implementation/evidence

Claude Code / claude-code-01
    IMPLEMENTER / VERIFIER
    owns the bounded code/test mutation
    runs provider-free local Windows verification
    writes one MC-0007 execution report

Human project owner
    HUMAN_DECIDER
    retains control over private storage locations and permanent deployment
```

## Frozen handoff

The implementation base is the repository state immediately after Claude's MC-0006 review:

```text
65bf6198ea77565551e4c4dabe690ce204497d79
```

The accepted contracts are defined by:

```text
docs/model_collaboration/threads/MC-0006/messages/002_chatgpt_task_owner_disposition.md
docs/model_collaboration/threads/MC-0007/BRIEF.md
```

Claude Code should not reinterpret the task as a new architecture exercise.

## Write ownership

Claude Code is the target write owner for only the paths declared in `STATE.json`.

The expected code surface is:

```text
src/ads_system/infrastructure/source_store.py
src/ads_system/application/source_universe.py
src/ads_system/source_cli.py
source-universe regression tests
```

The only additional Claude Code write surface is the MC-0007 `messages/**` report location.

## Verification boundary

Required:

```text
direct F1-F4 regressions
real local Windows execution
full provider-free pytest suite
disposable backup failure/retry exercise
clean git status at completion except the committed allowed changes/report
```

Not required in MC-0007:

```text
real permanent registry/vault creation
real permanent backup/restore
real Course 2 intake
real-corpus performance benchmark before disk cleanup/private storage preflight
```

## Blocking rule

The first permanent Source Registry / Source Vault write remains blocked while MC-0007 is active.

After Claude Code reports, ChatGPT must inspect the actual diff and execution evidence before closing MC-0007 or MC-0006.
