# Research 080: Explicit Coordination-Branch Claude Trigger Hardening

**Date:** 2026-08-27  
**Status:** Operational collaboration-method evidence  
**Scope:** Hardens the short human-to-Claude relay prompt after a real routing ambiguity showed that repository-contained detail is not sufficient if the relay prompt does not tell Claude which branch contains the current collaboration state.  
**Authority:** Research evidence supporting a narrow operational hardening of the canonical model-collaboration prompt. It does not change Specification 024 or the current product-design checkpoint.

## 1. Observed failure mode

After a prior MC-0004 Claude trigger, Claude reported that the prompt omitted the branch name. Claude was able to recover only by inference:

```text
main did not contain current_routing.json
+
v1-cockpit-design-exploration had advanced
+
prior collaboration history suggested the likely branch
```

The inference happened to be correct, but the process was not deterministic.

The important distinction is:

```text
repository carries the detailed collaboration contract
    !=
relay prompt may omit the repository locator needed to find that contract
```

A short relay prompt is still desirable, but it must contain enough addressing information to reach the authoritative state without heuristic branch discovery.

## 2. Root cause

The existing standardized Claude catch-up trigger was:

```text
Check the repository and docs/model_collaboration/REVIEW_INBOX.md,
then proceed with the pending Claude reviews in order.
```

This was intentionally minimal, but it omitted two pieces of routing information that should never require inference:

```text
repository identity
coordination branch
```

The repository identity is often obvious from the connected project context, but relying on that is unnecessary. The branch omission is materially more dangerous because:

```text
default branch may be behind
routing files may exist only on the active development branch
multiple experimental branches may exist
blind/independent work may live on intentionally hidden branches
review targets may be immutable SHAs different from the coordination branch
```

MC-0004 currently demonstrates all of these conditions.

## 3. New relay rule

Every standardized human-to-Claude repository trigger should explicitly name:

```text
repository
coordination branch
```

The **coordination branch** is the branch from which Claude should read current routing, the review inbox, thread state, and the current request.

It is not necessarily the exact artifact/review target. A frozen request may direct Claude to inspect an immutable commit SHA or another bounded target after current state has been reconstructed.

Therefore:

```text
coordination branch
    tells Claude where current collaboration state lives

exact target ref / SHA
    tells Claude what evidence or artifact is actually being reviewed/designed against
```

These must not be conflated.

## 4. No-inference rule

Claude should not infer the coordination branch from:

```text
default branch contents
which branch has the newest commit
missing files on main
recent prior conversations
branch naming conventions
searching unrelated branches
```

If the named branch does not exist, or if authoritative routing on that branch materially contradicts the relay prompt, Claude should stop and report the mismatch rather than silently choose another branch.

This is especially important for independence-sensitive work, where exploratory branch discovery can itself leak candidate content.

## 5. Revised standardized trigger template

The canonical short template should be:

```text
Work in repository `<OWNER/REPO>`.
Coordination branch: `<EXPLICIT_BRANCH>`.

Read `docs/current_routing.json` and `docs/model_collaboration/REVIEW_INBOX.md`
from that exact branch, then follow the referenced thread/request files and
proceed with the pending Claude obligation(s) in order.

Do not infer or switch the coordination branch. If the named branch is missing,
or authoritative routing on that branch contradicts this prompt, stop and report
the mismatch instead of choosing another branch.
```

The placeholders must be resolved before the human sends the prompt. The project should never hand Claude the literal template with an unresolved branch placeholder.

## 6. Current MC-0004 filled trigger

For the current Conversation Workspace blind-design obligation:

```text
Work in repository `shakaarlatief/autonomous-data-science-system`.
Coordination branch: `v1-cockpit-design-exploration`.

Read `docs/current_routing.json` and `docs/model_collaboration/REVIEW_INBOX.md`
from that exact branch, then follow the referenced thread/request files and
proceed with the pending Claude obligation.

Do not infer or switch the coordination branch. If the named branch is missing,
or authoritative routing on that branch contradicts this prompt, stop and report
the mismatch instead of choosing another branch.
```

The inbox currently routes Claude to MC-0004 Message 007 and expected Message 008. The separate ChatGPT independent-design branch remains intentionally excluded by that request.

## 7. Additional wording correction

The old standard prompt said:

```text
pending Claude reviews
```

That is too narrow. MC-0004 now contains a pending **independent design contribution**, not merely a review.

The standardized wording should therefore use:

```text
pending Claude obligation(s)
```

This covers review, counter-design, research, verification, or other explicitly routed model contributions without weakening thread-specific contracts.

## 8. Governance disposition

This is a narrow operational hardening based on observed use.

It does not justify:

```text
a new collaboration specification
a new checkpoint
a branch-discovery automation layer
changing Specification 024
```

The existing repository-mediated architecture remains sound. The relay prompt simply becomes a deterministic locator into that architecture rather than requiring branch inference.
