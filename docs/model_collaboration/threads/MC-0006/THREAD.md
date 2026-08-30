# MC-0006 Thread: Source Universe Architecture Review

**Thread:** MC-0006  
**Status:** ACTIVE  
**Review mode:** ADVERSARIAL_REVIEW  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Frozen review target:** `4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c`

## Purpose

Provide a read-only second-model challenge of the accepted Source Universe architecture and first permanent user-controlled Source Vault deployment before any permanent registry/vault write occurs.

## Roles

```text
ChatGPT
    TASK_OWNER
    later dispositions reviewer findings

Claude Code
    REVIEWER / CRITIC
    reads frozen target
    writes only the MC-0006 review message

Human project owner
    HUMAN_DECIDER if a material architecture/storage tradeoff remains
```

## Read-only review rule

The architecture target is frozen at `4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c`.

Claude must not mutate the target during review. The only permitted Claude write surface is:

```text
docs/model_collaboration/threads/MC-0006/messages/**
```

This keeps review evidence separate from later implementation/disposition changes.

## Expected next action

Claude Code should read:

```text
docs/current_routing.json
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0006/BRIEF.md
this THREAD.md
```

Then inspect the frozen target deeply, including the canonical Source Universe architecture, runbook, implementation, migrations/schema, CLI behavior, manifest/fingerprint evidence and tests.

The requested output is:

```text
docs/model_collaboration/threads/MC-0006/messages/001_claude_source_universe_architecture_review.md
```

## Blocking boundary

Disk cleanup and private-location planning may continue while Claude reviews.

Do not create/migrate the permanent Source Registry or write the permanent Source Vault until the review has been received and dispositioned.

## After Claude responds

ChatGPT should:

```text
1. verify Claude reviewed the exact frozen SHA;
2. classify every finding as accepted / rejected / deferred / human-choice;
3. distinguish structural defects from hardening preferences;
4. implement only accepted changes in a new mutation boundary;
5. revalidate affected source-substrate gates;
6. close MC-0006 with a durable RESOLUTION.md;
7. update current routing only if the review materially changes the active deployment boundary.
```
