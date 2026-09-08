# Validation 128: GitHub Connector Capability-Parity Baseline and Coexistence Recheck

**Date:** 2026-09-08
**Status:** PASS / 89-ACTION GITHUB BASELINE PRESERVED / NEGATIVE CHALLENGE STABLE / SAME-CONVERSATION COEXISTENCE STILL UNAVAILABLE
**Research:** Research 123
**Scope:** Preserve the two fresh GitHub-only connector qualifications performed from phone/mobile web and the live same-conversation Codexless developer-MCP coexistence recheck performed in `chatgpt-19`.

## 1. Same-conversation coexistence recheck

The project owner was using normal ChatGPT mobile web. In the persistent `chatgpt-19` conversation, the custom developer-MCP connector was projected and callable. A fresh `codex.account_preflight` call returned:

```text
status        ok
account       ok
quota         ok
rateLimits    ok
cleanup       ok
```

The GitHub connector was not projected in that same conversation. Tool discovery returned the Codexless developer-MCP namespace only.

This reproduces the practical boundary already preserved by Validation 034: the current host should not be assumed to permit simultaneous native GitHub-connector execution and developer-MCP execution in one conversation.

The result is a host/integration observation, not proof of a permanent platform-wide impossibility.

## 2. First fresh GitHub-only qualification

A separate fresh conversation with GitHub access performed a capability-parity qualification using only the GitHub-connected surface.

The live projection contained:

```text
89 GitHub actions
```

The qualification exercised a real remote development workflow against `shakaarlatief/autonomous-data-science-system` while keeping `main` unchanged.

Safe temporary state:

```text
temporary branch   github-connector-capability-qualification-20260908
temporary PR       #81 / closed / unmerged / draft
temporary issue    #82 / closed as completed
main               unchanged
```

Material live-qualified capability included:

```text
repository / installation discovery
public and authorized repository reads
branch listing/search/create
commit history/exact lookup/compare
file and blob reads
file create/update/delete commits
raw Git blob/tree/commit construction
non-forced branch ref advancement
PR create/read/update/close
PR changed files / patches / diff
PR comments and comment edits
review submissions and inline review comments
review-thread read/reply/edit/resolve/unresolve
PR and review-comment reactions
ready/draft transitions
PR label assignment/removal
issue create/read/search/update/comment
issue assignee and label mutation
issue lock/unlock/close
workflow run/job/step/log reads
workflow artifact listing
combined commit status
```

The raw Git path was successfully exercised as:

```text
create_blob
-> create_tree
-> create_commit
-> update_ref(force=false)
```

This proves the connector is capable of a push-equivalent remote Git development workflow without a local checkout.

## 3. Merge capability interpretation

`merge_pull_request` was exposed with:

```text
merge_method = merge | squash | rebase
expected_head_sha optional guard
```

It was intentionally not invoked in this qualification because the test instructions prohibited merging into the real development branch. The test therefore provides no merge failure evidence.

Project history already contains successful GitHub-connected merge workflows. The correct classification is:

```text
MERGE_ACTION=EXPOSED
MERGE_IN_THIS_TEST=NOT_ATTEMPTED
MERGE_FAILURE_IN_THIS_TEST=NO
```

## 4. Second fresh negative-capability challenge

A second fresh GitHub-only conversation explicitly challenged the first qualification's negative conclusions.

Result:

```text
projected actions       89
new actions discovered  0
```

Intent-specific rediscovery did not reveal another route for:

```text
branch/ref deletion
tag mutation
release mutation
workflow_dispatch
repository_dispatch
workflow-run cancellation
whole-run rerun
workflow enable/disable/delete
Check Runs / Check Suites objects
GitHub Discussions
collaborator listing/admin beyond named-user permission lookup
repository label-definition CRUD
milestone CRUD
repository settings mutation
branch-protection/ruleset mutation
Actions secrets / variables / environments
webhooks
security-alert administration
repository lifecycle/admin
organization/team administration
deploy keys
Pages administration
Packages/container registry administration
Codespaces administration
```

The generic GitHub `fetch` action remained allowlisted GET-only. Live GETs for Releases and Rulesets succeeded; an allowed branch-protection GET reached GitHub but returned `403 Resource not accessible by integration`. No generic REST POST/PATCH/PUT/DELETE or generic GraphQL mutation surface appeared.

## 5. Conservative negative classification

The correct wording for absent capability is:

```text
NOT_OBSERVED_IN_THIS_PROJECTION
```

not permanent `NOT_EXPOSED` at connector-wide/global scope.

Two independent fresh qualifications projecting the same 89 actions are strong evidence about the currently observed surface. They do not prove that another future connector version, permission context, installation type, host projection, or more narrowly triggered intent can never expose additional actions.

## 6. Parity baseline disposition

The observed native GitHub connector is materially broader than a read-only integration. The minimum ADS-side parity target must preserve the practical development authority actually observed, not an older generic documentation description.

The parity baseline therefore includes:

```text
all 89 currently observed actions
read/search fidelity
authorization and repository-scope semantics
pagination/cursor/continuation behavior
structured failure distinctions
direct file commits
raw Git objects and branch-ref advancement
PR/review/thread/comment/reaction workflows
issue lifecycle workflows
Actions/CI reads, logs, artifacts and exposed reruns
merge authority as exposed
```

Capabilities that were not observed in either fresh projection are optional future supersets rather than current parity requirements.

## 7. Connector terminology disposition

The project owner selected `Codexless Runtime Bridge` as the forward-looking canonical name for the custom ChatGPT connector. `ADS` remains reserved for the complete Autonomous Data Science System.

This validation does not claim that the live ChatGPT display name, tunnel name, package metadata, runtime labels, or historical records have already been renamed. Historical exact names remain evidence. Any live rename requires separate implementation and qualification.

```text
GITHUB_CONNECTOR_ACTION_BASELINE=89
NEGATIVE_CHALLENGE_NEW_ACTIONS=0
SAME_CONVERSATION_GITHUB_PLUS_DEVELOPER_MCP=NOT_CURRENTLY_AVAILABLE
GITHUB_PARITY_RESEARCH=OPEN
CODEXLESS_RUNTIME_BRIDGE_NAME=ACCEPTED_FORWARD_TERMINOLOGY
VALIDATION128=PASS
```
