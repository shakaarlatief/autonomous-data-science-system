# Checkpoint 276: Codex and Codexless Upstream Ecosystem Research Opened, Source Vault Paused

**Date:** 2026-09-03  
**Status:** Active research-direction checkpoint; v16 baseline preserved and upstream ecosystem study opened  
**Checkpoint class:** PRESERVATION_METHOD  
**Project stage:** Comprehensive Codex/Codexless upstream research before further local architecture changes  
**Scope:** Preserves the successful v16 live-viewer publication/test, the native Codex Desktop presentation comparison, the deliberate pause of v17 and Source Vault ingestion, retirement of obsolete MC-0009, opening of Research 113 and MC-0010, and the new evidence-driven upstream research route.  
**Authority:** Historical direction/continuity checkpoint. Research 113 governs the active research program; current continuation is governed by `docs/CURRENT_STATE.md` and `docs/current_routing.json`.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-16`  
**Conversation title:** `16 - Codex Live Task Viewer Publication and Source Vault Continuation`  
**Primary collaborator:** ChatGPT  
**Branch:** `v1-source-vault-bootstrap-resume`

## Meaningful state transition

The previous active substantive route was reviewed ingestion of the frozen 20-entry Source Vault corpus. During recovery from the interrupted Checkpoint 275 reconciliation, ADS developed and validated an early Desktop deeplink and a live Rich Task Card viewer.

That work produced a new architectural observation: the local system is now substantial enough, and the upstream Codex/Codexless ecosystem active enough, that extending the local implementation without a comprehensive upstream reassessment would be premature.

The project owner therefore explicitly changes the active route to:

```text
codexless-upstream-ecosystem-research
```

This is a deliberate Level-2 pause, not abandonment of Source Vault work.

## v16 publication and live behavior preserved

The guarded v16 publication succeeded on the live Codexless installation.

```text
resource      ui://toolwire/codex-task-card-v16.html
version       0.1.1-preview.7
toolCount     48
```

The live hashes matched the prepared candidate exactly.

After the controlled Codexless restart, tunnel reconnect, ChatGPT plug-in refresh, and a fresh disposable test chat, the card updated automatically while a multi-step Codex task ran.

Accepted bounded result:

```text
live transport / polling             PASS
automatic card refresh               PASS
streamed command output              PASS
terminal state transition            PASS
broad activity coverage              PRESENT
Desktop-parity presentation          NOT YET PASS
```

## Native Desktop reference changed the renderer question

A separate disposable local project was used to record a normal Codex Desktop task from start through completion.

The comparison showed that Desktop presents:

```text
ordinary user-visible Codex narration
compact evolving command actions
compact file-read actions
structured file-edit/change summaries
live output attached to the running command
prominent approval surfaces
normal final assistant response
```

rather than the flat event-log presentation used by v16.

The planned v17 direction was therefore to move toward a semantic evolving task transcript. However, implementation is now intentionally paused while Research 113 determines how much of that semantic model already exists upstream.

## Why broader upstream research is warranted

Initial current-source inspection already shows meaningful upstream evolution:

```text
Thread -> Turn -> Item is explicit App Server structure
history can be paged without resuming
thread status notifications exist
connection-scoped unsubscribe/unload behavior is documented
experimental same-turn steering exists
persistent thread queues exist
structured command/file-change item lifecycle exists
approval reviewer / auto-review surfaces exist
subagent and parent/ancestor thread semantics have expanded
```

The public Codexless project also has active work around same-turn steering, native progress, Browser elicitation, and lifecycle-state consolidation.

These observations are candidates, not adopted changes. They justify the research phase.

## Obsolete collaboration retired

The deferred MC-0009 Claude thread concerned only the already-resolved question of bounded local Git feasibility through semantic MCP actions.

It never received a Claude Message 001 and no longer provides useful outstanding work after ADS experimentally verified bounded semantic fetch and strict-fast-forward pull.

By explicit project-owner decision:

```text
MC-0009 live obligation      RETIRED
MC-0009 thread directory     REMOVED
replacement obligation       MC-0010
```

Historical validation records may retain textual provenance that MC-0009 existed at the time, but it is no longer a live routing target or required repository path.

## New multi-model research route

MC-0010 opens a current-context parallel Claude research contribution.

It is intentionally not blind to the current ADS design. Claude should know the current Codexless architecture and independently search the upstream ecosystem for:

```text
features ADS can reuse
limitations ADS already encountered
stronger alternatives
new ideas
obsolete assumptions
security/reliability risks
relevant issues / PRs / discussions
```

ChatGPT research does not wait idly for Claude, but a material final architecture reconciliation should consider the separate Claude report when available.

## Source Vault remains preserved

No Source Universe/Vault payload, original source corpus, storage coordinate, credential, or recovery state is changed by this checkpoint.

The preserved next Source Vault action remains reviewed ingestion of the frozen 20-entry first corpus, followed by working-store audit and recovery proof.

It is now intentionally paused while the project-owner-selected Codex/Codexless research phase is active.

## Checkpoint 275 interruption remains open historical residue

This checkpoint does not erase the Checkpoint 275 publication/finalization problem.

```text
Checkpoint 274    locally committed / not known pushed
Checkpoint 275    uncommitted preservation set
.tmp residue      known interruption residue
origin sync       not claimed
```

The new research work must not falsely describe that older boundary as already cleanly published.

## Exact continuation

```text
1. execute Research 113's comprehensive upstream survey
2. maintain the upstream-vs-ADS comparison matrix
3. open and route MC-0010 for a parallel current-context Claude research pass
4. preserve important topic clusters as durable research when warranted
5. do not implement v17 or replace accepted lifecycle mechanisms prematurely
6. reconcile the resulting architecture after evidence is sufficient
7. perform the planned repository-wide Codexless documentation/connectivity audit
8. return to Source Vault reviewed ingestion after this Level-2 phase closes unless project-owner routing changes again
```
