# Checkpoint 405: GitHub G1 Fresh-Host Gate Closed, G2 Read-Only Next

**Date:** 2026-09-09
**Status:** PASS / G1 HOST COVERAGE 7 OF 7 / G2 READ-ONLY IMPLEMENTATION NEXT
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve the targeted `github.list_installed_accounts` host recheck PASS, compose it with Validation 161's already-preserved six successful G1 host reads, and close the G1 fresh-host gate without erasing the original connector network failure.
**Authority:** Validation 162 owns the targeted host recheck. Validation 161 remains authoritative for the original 7/7 projection, 6/7 live-read FAIL and network-error evidence. Validation 160 remains authoritative for preview.30 local MCP publication and 7/7 local-live qualification.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-21
**Conversation title:** 21 - GitHub Device Flow Recovery and Authorization Diagnosis
**Primary collaborator:** ChatGPT

The targeted requalification confirms `github.list_installed_accounts` is still projected and succeeds read-only with `schemaVersion=codexless.github-readonly.v1`, one account, and personal account `shakaarlatief` present as type `User`. No credential secret or GitHub mutation appeared. No Plugin rescan, Runtime Bridge restart or authorization change was required.

This closes the only unresolved live-read gate from Checkpoint 404. The combined G1 fresh-host evidence is now 7/7: six successful actions from the original qualification plus the separately authorized successful installed-accounts recheck. The original `mcp_network_error / network_error / Connection failed.` event remains preserved as a real transient connector-transport observation and is not rewritten into a false initial PASS.

Research 123 therefore advances from G1 to G2. The next intended read-only repository-git slice is compare/fetch/blob/commit/file plus code/branch/commit/repository/install-scope search. Issue, pull-request and Actions-specific reads remain assigned to their later slices.

Known gaps stay explicit: `manageable_only=true`, `include_search_index_status=true`, Enterprise repository-URL routing and hidden native output envelopes remain unqualified, so exact native-wrapper parity remains 0/89.

```text
CHECKPOINT405=GITHUB_G1_FRESH_HOST_GATE_CLOSED
G1_FRESH_HOST_PROJECTION=PASS_7_OF_7
G1_FRESH_HOST_LIVE_COVERAGE=PASS_7_OF_7
GITHUB_G1_INSTALLED_ACCOUNTS_HOST_RECHECK=PASS
ORIGINAL_TRANSPORT_FAILURE_PRESERVED=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
RESEARCH123=ACTIVE
NEXT=G2_FETCH_SEARCH_BRANCH_COMMIT_FILE_BLOB_COMPARE_READONLY_IMPLEMENTATION
```
