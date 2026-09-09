# Checkpoint 403: GitHub G1 Read-Only Expansion Live, Fresh-Host Qualification Next

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.30 LIVE / ELEVEN GITHUB READ-ONLY TOOLS / FRESH-HOST G1 QUALIFICATION NEXT
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve successful publication/activation and live local MCP qualification of seven additional G1 GitHub read-only actions, bringing the public Runtime Bridge GitHub read surface to eleven actions while keeping exact native-wrapper gaps explicit.
**Authority:** Validation 160 owns preview.30 release, active-loopback MCP and seven-call live-read evidence. Validation 159 remains authoritative for the first four actions' fresh-host qualification. Research 123 owns parity interpretation and continuation.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-21
**Conversation title:** 21 - GitHub Device Flow Recovery and Authorization Diagnosis
**Primary collaborator:** ChatGPT

Private runtime head `7af8600dd2213d2fc2e5aca3b3ef32b8fafeacc6` preserves immutable release `github-g1-readonly-expansion-v1`. The release targets `0.1.1-preview.30-github-g1-readonly`, `codexless-public-preview-v2`, 75 public tools, nine replaced/added files and one exact runtime dependency. The first manifest draft exceeded Runtime Release v2's 16-regression ceiling with 18 entries; the contract was not widened. The release was corrected to 16 regressions and prepared successfully. A synthetic test fixture that triggered the conservative secret scanner was likewise rewritten rather than weakening secret detection.

Prepublication verification returned the intended nine mismatches against preview.29. Publication operation `rm_bc3ee2e4f09d12ed8f92af6686663961` then succeeded without recovery, restart operation `rm_9c321da1381ec4ebd69657441d939be6` activated preview.30 without recovery, and postactivation verification returned `mismatchCount=0`. Direct loopback health reports version preview.30 with 75 tools. Protected GitHub authorization survived restart and remained authorized/non-expired.

A fresh stateless loopback MCP initialize/tools-list returned exactly 75 tools and exactly eleven `github.*` actions. The seven additions are `github.get_repo`, `github.get_repo_collaborator_permission`, `github.list_installed_accounts`, `github.list_repositories`, `github.list_repositories_by_affiliation`, `github.list_user_org_memberships`, and `github.list_user_orgs`.

All seven new actions were then live-invoked read-only against the stored GitHub App user authorization. `get_repo` returned the canonical public ADS repository; collaborator permission for `shakaarlatief` on that repository returned `admin`; installed-account enumeration returned one personal User account; both owner-filtered repository listing and owner-affiliation listing returned 12 repositories with the canonical ADS repository present and no continuation; organization membership and organization lists both returned count zero. Unrelated private repository names were not printed or preserved. No GitHub mutation and no credential exposure occurred.

Known gaps remain deliberate: `list_installations(manageable_only=true)` is still unqualified, `list_repositories(include_search_index_status=true)` remains fail-closed because the native enrichment output is hidden, and `get_repo(repository_url=...)` remains github.com-only until Enterprise routing is separately qualified. Native machine-readable outputs remain hidden behind `any`, so exact native-wrapper parity stays conservatively 0/89.

The active MCP now contains all eleven names, but this persistent ChatGPT conversation still projects only the earlier four GitHub actions. The next Research 123 gate is therefore fresh-host discovery/schema capture and exactly seven read-only live calls for the new G1 actions after Plugin refresh/rescan. G2 fetch/search/branch/commit/file reads must wait until that host gate is preserved.

```text
CHECKPOINT403=GITHUB_G1_READONLY_EXPANSION_LIVE
LIVE_RUNTIME_VERSION=0.1.1-preview.30-github-g1-readonly
LIVE_MCP_TOOL_COUNT=75
LIVE_GITHUB_READONLY_TOOLS=11
G1_NEW_TOOLS=7
G1_LIVE_READS=7_OF_7_PASS
PROTECTED_AUTHORIZATION_PRESERVED=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
MANAGEABLE_ONLY_TRUE=NOT_QUALIFIED
INCLUDE_SEARCH_INDEX_STATUS_TRUE=NOT_QUALIFIED
ENTERPRISE_REPOSITORY_URL=NOT_QUALIFIED
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
SAME_CHAT_NEW_TOOL_PROJECTION=STALE
RESEARCH123=ACTIVE
NEXT=FRESH_CHAT_GITHUB_G1_READONLY_SCHEMA_AND_LIVE_READ_QUALIFICATION
```
