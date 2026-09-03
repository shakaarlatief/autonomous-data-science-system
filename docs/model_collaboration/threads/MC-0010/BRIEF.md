# MC-0010 Brief: Current Codex and Codexless Upstream Ecosystem Research

**Thread:** MC-0010  
**Date opened:** 2026-09-03  
**Review mode:** REVIEWED  
**Coordination branch:** `v1-source-vault-bootstrap-resume`  
**Opening repository head:** `c0b9101a82f688be25dfc6dbf565813d51cc51a5`  
**Intended reviewer environment:** fresh normal Claude Project interaction with repository access after the coordination branch contains this thread  
**Authority:** Current-context collaboration brief. It frames a parallel research contribution and does not make Claude or GitHub discussion content project authority.  
**Purpose:** Obtain a broad second-model investigation of the current OpenAI Codex/App Server and public Codexless ecosystem, explicitly informed by ADS's existing Codexless work, so final architecture decisions are not based on one research path.

## Why this thread exists

ADS has now spent substantial effort developing and validating a local Codexless integration. The system includes bounded local tools, explicit Codex escalation, Call Profile governance, Rich Task Cards, Desktop handoff, durable same-thread continuation, bounded Git synchronization, and a live task viewer.

A first v16 live-viewer test succeeded functionally, while a native Codex Desktop reference recording showed that the local renderer still lacks Desktop's semantic narrative hierarchy. Before implementing v17, the project owner saw the scale and activity of the public `openai/codex` issue/PR/discussion ecosystem and explicitly requested a much broader research phase.

This thread replaces the obsolete MC-0009 direct-Git feasibility research. MC-0009 never received a Claude response, its technical question was later resolved experimentally by ADS, and its thread has been retired.

## Exposure and independence

This is intentionally **not** a blind-to-candidate review.

Claude should understand the current ADS architecture and evidence before evaluating upstream alternatives. The goal is diversity of search, interpretation, criticism, and design ideas, not artificial independence.

Claude may inspect current coordination-branch material, including Research 105-113, Checkpoints 268-276, relevant local-execution validation records, runbooks, and current Codexless-related state.

Do not optimize for agreement with ChatGPT. Identify important upstream capabilities, risks, issues, proposals, or architectural alternatives even when they imply replacing or simplifying current ADS work.

## Minimum ADS read set

Read at least:

```text
docs/current_routing.json
docs/CURRENT_STATE.md
docs/DEVELOPMENT_METHOD.md
docs/KNOWLEDGE_MAP.md
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md
docs/research/111_archive_unarchive_reacquire_closes_codex_desktop_handoff.md
docs/research/112_guided_proceed_in_chat_shared_ready_and_repeatable_roundtrip.md
docs/research/113_codex_codexless_upstream_ecosystem_architecture_research_program.md
docs/checkpoints/276_codex_codexless_upstream_ecosystem_research_opened_source_vault_paused.md
docs/local_execution/OPERATIONS.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/model_collaboration/README.md
```

Then inspect the relevant validations and implementation evidence needed to test claims. Do not trust summaries when exact code/evidence can be inspected.

## Public research surfaces

Research at least:

```text
https://github.com/openai/codex
https://github.com/openai/codex/tree/main/codex-rs/app-server
https://github.com/openai/codex/issues
https://github.com/openai/codex/pulls
https://github.com/openai/codex/discussions
https://github.com/openai/codex/discussions/38868

https://github.com/liyana31811/Codexless
https://github.com/liyana31811/Codexless/pulls
```

Use current source, schemas, tests, issue/PR discussions, maintainer comments, and relevant commit/release history. Search by topic rather than reading every issue sequentially.

## Required research scope

Cover at least:

1. App Server Thread / Turn / Item semantics and event lifecycles.
2. Thread persistence, read/resume/fork, subscriptions, ownership, archive/unarchive, pagination, and cross-client behavior.
3. Same-turn steering, queued turns, settings, goals, projects, sections, memory, and recovery semantics.
4. User-visible reasoning summaries, plans, commands, file reads/changes, diffs, MCP calls, approvals, and how these support rich task rendering.
5. ApprovalsReviewer, auto-review/Guardian, permissions, sandboxing, and how those compare with ADS Call Profile and authority policy.
6. MCP Apps/resources/extensions, elicitation, UI lifecycle, and Browser integration.
7. Subagents/multi-agent behavior, review/compaction, parent-child thread semantics, and supervision opportunities.
8. Windows/WSL/Desktop issues, especially synchronization, resume, persistence, archive/unarchive, stale UI, and version compatibility.
9. Public Codexless architecture, tests, open/merged PRs, and divergence from ADS-local Codexless.
10. Community ideas and enhancement proposals that ADS has not considered.
11. Security, no-replay/idempotency, uncertainty, credential, and permission-boundary implications.
12. Features that may make current ADS mechanisms obsolete, simpler, stronger, or unnecessary.

## Evidence discipline

Classify important findings using the Research 113 hierarchy:

```text
A OFFICIAL_DOCUMENTATION
B OFFICIAL_SOURCE
C MERGED_UPSTREAM_CHANGE
D MAINTAINER_STATEMENT
E OPEN_PROPOSAL
F COMMUNITY_OBSERVATION
G ADS_EXPERIMENT
H INFERENCE
```

Do not present an issue report or open PR as an official guarantee.

## Required output

Write one durable report at:

```text
docs/model_collaboration/threads/MC-0010/messages/001_claude_current_codex_codexless_ecosystem_research.md
```

The report should contain:

```text
sources and dates/versions where material
research method
most important official capabilities found
important current issues / bugs / limitations
important open and merged PRs
important discussions/community ideas
comparison with ADS current behavior
things ADS already solves well
things upstream now solves or may replace
things ADS should simplify
things ADS should keep custom
new capabilities worth considering
risks / compatibility concerns
viewer/rendering implications
thread/supervision implications
approval/authority implications
Browser/MCP implications
multi-agent implications
ranked action matrix
unknowns requiring live experiments
strongest challenge to the current ADS architecture
strongest argument for keeping the current architecture
explicit KEEP / CHANGE / INVESTIGATE / MONITOR recommendations
```

Do not modify target-state implementation or canonical ADS documents. The report is collaboration evidence only.

## Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0010/messages/**
```

## Blocking semantics

ChatGPT may continue upstream research while Claude is unavailable.

MC-0010 is not a blocker for ordinary research collection. It should be considered before final architecture reconciliation or any broad replacement/promotion decision when the Claude contribution is practically available.

## Relationship to Source Vault and v17

Source Vault ingestion and v17 implementation are currently paused by project-owner routing while Research 113 is active.

Claude should not implement v17, mutate Source Vault, change Codexless, or widen local permissions as part of this thread.
