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

Claude / claude-01
    REVIEWER / CRITIC
    normal Claude Project with full repository access through the custom connector
    reads frozen target
    writes only the MC-0006 review message

Human project owner
    HUMAN_DECIDER if a material architecture/storage tradeoff remains
```

Claude Code is intentionally not the MC-0006 reviewer. It remains available for later, separately scoped execution-based verification and Windows-local deployment work if the architectural review identifies evidence questions that genuinely require command/filesystem execution.

## Read-only review rule

The architecture target is frozen at `4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c`.

Claude must not mutate the target during review. The only permitted Claude write surface is:

```text
docs/model_collaboration/threads/MC-0006/messages/**
```

This keeps review evidence separate from later implementation/disposition changes.

## Reviewer-environment decision

MC-0006 was initially routed to Claude Code because the review spans architecture plus implementation and later permanent deployment will require local execution.

Before the substantive review began, the project owner clarified that the normal Claude Project already has full repository access through a custom connector and requested an explicit comparison of Claude versus Claude Code for this exact task.

The resulting split is:

```text
normal Claude
    perform MC-0006 architectural/adversarial repository review

Claude Code
    perform later narrow execution-based verification where required
    assist with local Windows preflight/deployment only after MC-0006 findings are dispositioned
```

The environment-selection evidence is preserved in `messages/ENVIRONMENT_SELECTION.md`.

## Expected next action

Claude should read:

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

Where a conclusion depends materially on execution rather than static repository inspection, Claude should say so explicitly and identify the smallest execution check needed. It should not perform the permanent deployment itself.

## Blocking boundary

Disk cleanup and private-location planning may continue while Claude reviews.

Do not create/migrate the permanent Source Registry or write the permanent Source Vault until the review has been received and dispositioned.

## After Claude responds

ChatGPT should:

```text
1. verify Claude reviewed the exact frozen SHA;
2. classify every finding as accepted / rejected / deferred / human-choice;
3. distinguish structural defects from hardening preferences;
4. isolate any execution-dependent evidence gaps for narrow follow-up verification;
5. implement only accepted changes in a new mutation boundary;
6. revalidate affected source-substrate gates;
7. close MC-0006 with a durable RESOLUTION.md;
8. update current routing only if the review materially changes the active deployment boundary.
```
