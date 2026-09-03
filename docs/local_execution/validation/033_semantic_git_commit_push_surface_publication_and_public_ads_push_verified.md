# Semantic Git commit/push surface published and public ADS push verified

**Date:** 2026-09-03
**Status:** `PASS / PUBLIC_ADS_HEAD_PUBLISHED`
**Scope:** Preserve the guarded publication and first successful use of the new bounded semantic Git commit/push surface, including the exact public ADS commit chain, fresh-chat discovery validation, and exact-head non-force push.
**Authority:** Bounded local-execution evidence. This proves the observed publication/discovery/push behavior for the tested surface and exact ADS branch. It does not yet generalize semantic Git to arbitrary repositories or branches.
**Declared references:** `checkpoint:276`, `path:docs/research/113_codex_codexless_upstream_ecosystem_architecture_research_program.md`, `path:docs/research/116_flexible_multi_repository_codexless_authority_and_runtime_repository_architecture.md`, `path:docs/local_execution/OPERATIONS.md`

## 1. Repository publication commits

A formal Codex task created two logical commits after the existing local Checkpoint 274 commit:

```text
c0b9101  Preserve archive-unarchive reacquisition checkpoint
1b9bbd2  Preserve guided Proceed in Chat roundtrip
94e7bf7  Open Codex upstream ecosystem research
```

The resulting exact local HEAD was:

```text
94e7bf7a011c202d2c9def718e3f2eefd066f1b8
```

The aggregate public repository-integrity gate passed on that exact HEAD before publication.

The initial formal-Codex push attempt failed at the Windows Git credential/askpass boundary. No credentials, Git configuration, ACLs, branches, remotes, or permissions were changed to work around that failure.

## 2. New bounded semantic Git tools

A guarded Codexless candidate introduced:

```text
codex.git_commit_paths
codex.git_push_ff_only
```

The candidate retained fixed ADS repository/branch semantics and intentionally did not expose caller-controlled command, cwd, branch, remote, URL, refspec, force flag, credentials, Git configuration, or permission profile.

`git_commit_paths` accepts only:

```text
expectedHead
message
paths[]
```

and verifies exact branch/upstream, empty initial index, no active merge/rebase/cherry-pick/revert state, repository-relative/protected-path rules, exact staging set, `git diff --cached --check`, and exact parent/index postconditions.

`git_push_ff_only` accepts only:

```text
expectedHead
```

and verifies fixed branch/upstream, tracked/index cleanliness, no active merge/rebase/cherry-pick/revert state, current HEAD equality, refreshed origin ancestry, exact ADS repository-integrity PASS, exactly one ordinary non-force push through the host Git environment, and refreshed remote-tracking equality afterward. It never automatically retries an uncertain push.

## 3. Guarded live publication

The candidate was published to the live Codexless installation through an exact-hash, backup, syntax-check and rollback activation procedure.

Publication preflight:

```text
SEMANTIC_GIT_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.7
EXPECTED_PUBLIC_TOOL_COUNT=50
```

Candidate/live hashes after publication:

```text
mcp-server-factory.mjs
AE1DD37B9BA8750050CA5B60EE940401885A2ED8B838DFFAE4B49FB1456767BB

surface-contracts.mjs
A64B195F58BA46F6A89D1B75F74E130630FEC790D9DDA1132A6803E85A538025
```

Live activation result:

```text
SEMANTIC_GIT_PUBLICATION_RESULT=PASS
```

## 4. Fresh-chat discovery validation

After the controlled Codexless restart, tunnel reconnect, ChatGPT developer-MCP refresh, and a fresh disposable conversation, read-only discovery established:

```text
server version       0.1.1-preview.7
surface              codexless-public-preview-v1
live MCP tool count  50
```

Both new public tools were present and callable by name.

The fresh conversation independently verified that the published schemas expose no arbitrary command, cwd, branch, remote, URL, refspec, force flag, credentials, Git configuration, permission profile, or authority selector.

A separate host-projection observation is preserved in Validation 034: the live MCP server enumerated 50 tools while the ChatGPT connector resource projection exposed 46 callable resources in that fresh chat. The semantic commit/push tools were included in the 46 and remained callable.

## 5. Exact semantic push

The fresh disposable chat invoked only:

```text
codex.git_push_ff_only(
    expectedHead = 94e7bf7a011c202d2c9def718e3f2eefd066f1b8
)
```

Observed result:

```text
push branch    v1-source-vault-bootstrap-resume
old remote     5ba2563...
new remote     94e7bf7...
integrity      PUBLIC_REPOSITORY_INTEGRITY=PASS
retried        false
```

Postflight verification established:

```text
local HEAD
94e7bf7a011c202d2c9def718e3f2eefd066f1b8

origin/v1-source-vault-bootstrap-resume
94e7bf7a011c202d2c9def718e3f2eefd066f1b8
```

Final tracked/index status:

```text
## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume
```

The existing protected `.tmp/pytest-*` directories continued to emit read-only permission warnings. They were not cleaned or modified.

## 6. Accepted bounded conclusion

For the tested exact ADS contract:

```text
semantic exact-path commit tool publication   PASS
semantic exact-head push tool publication     PASS
fresh ChatGPT discovery                       PASS
host credential path usable by push tool      PASS
repository integrity before push              PASS
single non-force push                         PASS
remote exact-head postflight                   PASS
no retry                                       PASS
```

This does not yet generalize the semantic Git surface to other repositories or arbitrary branches. Research 116 owns that next design question.
