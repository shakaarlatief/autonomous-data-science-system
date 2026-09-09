# Checkpoint 404: GitHub G1 Fresh-Host Single Transport Failure, Targeted Recheck Next

**Date:** 2026-09-09
**Status:** FAIL PRESERVED / HOST PROJECTION 7 OF 7 / LIVE READS 6 OF 7 / TARGETED READ-ONLY RECHECK NEXT
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve the seven-action preview.30 fresh-host qualification exactly as observed, localize the sole `github.list_installed_accounts` failure using a post-failure local MCP discriminator, and reduce the next gate to one targeted read-only host requalification rather than rerunning six successful calls.
**Authority:** Validation 161 owns the fresh-host FAIL and post-failure local discriminator. Validation 160 remains authoritative for preview.30 publication, exact local schemas and initial seven-of-seven local-live qualification.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-21
**Conversation title:** 21 - GitHub Device Flow Recovery and Authorization Diagnosis
**Primary collaborator:** ChatGPT

The refreshed disposable ChatGPT conversation projected all seven new preview.30 G1 actions with bounded schemas. Calls 1, 2 and 4 through 7 succeeded exactly once and read-only. The canonical ADS repository resolved, collaborator permission is `admin`, both repository-listing routes returned 12 repositories with the canonical ADS repository present, and both organization reads returned count zero. No credential secret or arbitrary transport authority appeared and no GitHub mutation occurred.

The single Call 3 invocation, `github.list_installed_accounts`, failed before an application result with connector error `mcp_network_error / network_error / Connection failed.` The qualification correctly did not retry it and therefore ended `GITHUB_G1_READONLY_FRESH_HOST=FAIL`.

A post-failure read-only discriminator from this persistent conversation shows that protected GitHub authorization remains healthy and that a fresh stateless loopback MCP call to the same `github.list_installed_accounts` action succeeds with one installed account containing personal User `shakaarlatief`. This rules out treating the supplied failure as evidence that preview.30 action logic or stored authorization is broken. It does not establish the exact transport root cause. The failure remains conservatively localized to the fresh ChatGPT connector transport path for that invocation or another transient pre-application-result layer.

The next Research 123 gate is therefore exactly one targeted host requalification of `github.list_installed_accounts`. The other six successful fresh-host reads do not need to be repeated. If the original disposable chat still projects the action, a separately authorized follow-up in that same chat is sufficient; otherwise use one new disposable chat. No Plugin rescan, Runtime Bridge release or GitHub authorization change is currently justified.

```text
CHECKPOINT404=GITHUB_G1_FRESH_HOST_SINGLE_TRANSPORT_FAILURE
FRESH_HOST_G1_ACTIONS_PROJECTED=7_OF_7
FRESH_HOST_G1_SCHEMA_BOUNDEDNESS=PASS_7_OF_7
FRESH_HOST_G1_LIVE_READS=6_OF_7_PASS
FAILED_ACTION=github.list_installed_accounts
FAILED_ACTION_ERROR=mcp_network_error_network_error_connection_failed
POST_FAILURE_LOCAL_ACTION=PASS
PROTECTED_AUTHORIZATION_HEALTHY=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
RESEARCH123=ACTIVE
NEXT=TARGETED_HOST_LIST_INSTALLED_ACCOUNTS_REQUALIFICATION
```
