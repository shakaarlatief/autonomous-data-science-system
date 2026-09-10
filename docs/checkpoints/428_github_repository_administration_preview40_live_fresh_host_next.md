# Checkpoint 428: GitHub Repository Administration Preview40 Live, Fresh-Host Qualification Next

**Date:** 2026-09-10
**Status:** PASS / PREVIEW.40 LIVE / 156 PUBLIC TOOLS / 92 GITHUB TOOLS / TWO ADMIN READS LIVE / CREATE NO-WRITE GUARDED
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve live activation and local qualification of the first beyond-parity Repository Administration foundation without performing repository creation.
**Authority:** Validation 185 owns preview.40 implementation/publication/repair history, local-live read evidence, the create-repository no-write guard, and the fresh-host boundary. Validation 184 remains authoritative for the frozen three-action semantic design.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-21
**Conversation title:** 21 - GitHub Device Flow Recovery and Authorization Diagnosis
**Primary collaborator:** ChatGPT

Runtime Bridge preview.40 is live at 156 public tools / 92 GitHub tools and contains all three first-slice Repository Administration actions: `github.list_repository_collaborators`, `github.list_repository_invitations`, and `github.create_repository`.

The implementation preserves the frozen bounded authority contract. Both reads require installation-derived repository authority and fixed GitHub endpoints. Personal repository creation uses only authenticated-user identity, private-by-default visibility, false-by-default auto initialization, same-name serialization, identity revalidation and single-attempt mutation-aware transport. No arbitrary GitHub transport, organization creation, template/settings, ruleset or destructive lifecycle authority is exposed.

The focused administration suite passes 4/4. The initial v2 activation exposed one outer-runtime facade integration defect during live readback; no write occurred. Narrow v3 repair added the missing delegates and a regression for them. Immutable release `github-repository-administration-v3`, bound to local-runtime head `5846f02785c97df99c0ba8edc47f160a3710ef2b`, published and restarted successfully with postactivation verification at zero mismatches. Manifest SHA-256 is `a638f715565ebf939cdaa37ea9e1caeb743b1b5939423b68537da0346fd5e778`.

Direct local MCP qualification proves both new reads live on the canonical ADS repository: collaborator listing returns one collaborator and includes the authenticated user; invitation listing returns zero open invitations. A deliberately invalid repository name containing a space is rejected by schema validation before mutation dispatch. No schema-valid repository creation call has been issued.

The current persistent ChatGPT host remains stale and does not project the three new tools even though local MCP exposes them. The next boundary is a refreshed disposable fresh-host schema/read/no-write qualification. Positive `github.create_repository` remains 0/1 and requires separate explicit owner authorization for one exact repository name and visibility after that host gate.

```text
CHECKPOINT428=GITHUB_REPOSITORY_ADMINISTRATION_PREVIEW40_LIVE
LIVE_RUNTIME_VERSION=0.1.1-preview.40-github-repository-administration
LIVE_PUBLIC_TOOL_COUNT=156
LIVE_GITHUB_TOOL_COUNT=92
EXTENDED_REPOSITORY_ADMIN_IMPLEMENTED=3_OF_3
EXTENDED_REPOSITORY_ADMIN_LOCAL_LIVE_READS=PASS_2_OF_2
CREATE_REPOSITORY_NO_WRITE_GUARD=PASS
CREATE_REPOSITORY_POSITIVE_LIVE=0_OF_1
ADMINISTRATION_MUTATION_OCCURRED=false
SAME_CHAT_REPOSITORY_ADMIN_PROJECTION=STALE
NATIVE_ACTION_NAMES_IMPLEMENTED=89_OF_89
POSITIVE_LIVE_NATIVE_ACTIONS=84_OF_89
RESEARCH123=ACTIVE
NEXT=FRESH_HOST_REPOSITORY_ADMINISTRATION_SCHEMA_QUALIFICATION
```
