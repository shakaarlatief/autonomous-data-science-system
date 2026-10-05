# MC-0030 Message 011: Runtime Bridge recovery, refresh, and concurrency trigger

**Author:** ChatGPT / chatgpt-36
**Date:** 2026-10-05
**Thread:** MC-0030
**Status:** SUPPORTING RUNTIME RELIABILITY KNOWLEDGE PRESERVED / R0-P01 CONTINUES
**Detailed authority:** Research 519 / Checkpoint 855 / Validation 212

The R0-P01 freeze incident exposed three separate Runtime Bridge concerns and they are now explicitly separated.

First, interrupted semantic-commit staging now has a bounded purpose-specific recovery action:

    codex.git_recover_commit_index

The first public ADS use reconciled to the intended effect: exact staged P01 paths were removed from the index while working-tree content and HEAD remained preserved.

Second, when the new action was live on the MCP server but absent from the already-open ChatGPT projection, the owner used:

    Plug-ins
    -> Codexless Runtime Bridge
    -> ...
    -> Beheren
    -> Tools vernieuwen

and the new action became callable in the same conversation. This is the current same-chat schema-refresh procedure after a tool-surface change.

Third, intermittent `bridge concurrency limit reached (1)` / uncertain-result behavior remains open. It is not established as an every-operation failure and does not currently justify preempting R0-P01 for a speculative Runtime Bridge redesign.

The P01 freeze is durably local and remote at:

    5f41625ad3811b6d769a112885ea2afcbd48952f

Continuation rule:

    continue R0-P01 normally

    if the same concurrency / uncertain-completion pattern recurs
    during an ordinary semantic Git operation:
        stop further mutations
        reconcile state
        diagnose the Runtime Bridge lifecycle
        qualify the repair
        then resume

`Tools vernieuwen` is retained as a schema-projection refresh procedure, not a general concurrency workaround.

Next remains the bounded manual-Codex implementation of:

    harness.py
    webauthn_server.mjs
    score.py

with no real owner credential operation during implementation.
