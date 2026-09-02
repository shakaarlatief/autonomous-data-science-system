# Checkpoint 272: Codex Desktop Thread Handoff Verified, Deeplink Candidate Preflighted

**Date:** 2026-09-02  
**Status:** Verified infrastructure/continuity checkpoint with one prepared follow-up activation  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Post-Checkpoint-271 Codex formal-agent integration investigation; writer handoff verified; Desktop deeplink integration candidate ready for live activation  
**Scope:** Records the investigation proving that ADS creates genuine persistent Codex threads, separating persistence from Desktop sidebar cataloging, falsifying the `threadSource="user"` visibility hypothesis, verifying terminal thread/process release and same-thread continuation from another Codex client, isolating the Desktop catalog reconciliation trigger, and freezing the H6 canonical deeplink candidate before live activation.  
**Authority:** Historical verification and continuity provenance. Research 109 and Validations 022-026 govern the detailed experiment evidence. Current continuation is governed by `docs/CURRENT_STATE.md` and `docs/current_routing.json`. H6 is not accepted as live until a post-activation real Codex acceptance test succeeds.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-15`  
**Conversation title:** `15 - Codex Desktop Thread Handoff and Source Vault Continuation`  
**Primary collaborator:** ChatGPT  
**Branch:** `v1-source-vault-bootstrap-resume`

## Why this checkpoint exists

Checkpoint 271 closed the direct bounded Git synchronization investigation and returned the substantive ADS route to Source Vault reviewed ingestion.

The project owner then chose to investigate an adjacent operational integration question before resuming ingestion:

```text
Can a real Codex task started through ChatGPT/ADS become a normal human-visible
Codex conversation that the user can inspect and later continue from Codex itself?
```

The investigation produced a meaningful architectural result rather than a small implementation tweak. It separated three independent layers:

```text
Codex thread persistence
Codex writer/process ownership
Codex Desktop sidebar catalog reconciliation
```

and verified a reliable post-completion handoff mechanism.

## Formal Codex execution through ADS is real

A minimal formal Codex call through the normal ADS Agent lane completed successfully and persisted through standard Codex session/core state.

Therefore:

```text
ChatGPT -> ADS -> Codexless -> Codex App Server -> formal Codex model
```

creates a genuine Codex thread rather than a transient bridge-only result.

The initial failure to see the thread in Desktop `Recent` was therefore a discovery/catalog issue, not failure to create the thread.

## Desktop visibility hypothesis H1 was falsified

The first candidate added:

```text
threadSource = "user"
```

to `thread/start`.

A fresh real test showed:

```text
threadSource persisted     PASS
normal thread persistence  PASS
Desktop Recent visibility  FAIL
```

The hypothesis was rejected. The experimental override is not part of the accepted H6 direction.

## Desktop uses a distinct local catalog

Read-only inspection established that Codex core thread state and Codex Desktop's local sidebar catalog are separate persistence/discovery layers.

Valid ADS-created threads existed in normal Codex state while being absent from Desktop's `local_thread_catalog`.

The project explicitly rejected:

```text
manual local_thread_catalog insertion/update
session JSONL fabrication
legacy event fabrication
private Codex database repair merely to improve UI visibility
```

## Exact thread deeplink works independently of Recent

A valid ADS-created thread could be opened through:

```text
codex://threads/<thread-id>
```

including while absent from Desktop `Recent`.

This established deterministic exact-thread openability as a stronger integration seam than immediate sidebar registration.

## H3/H4 writer handoff is verified

Opening the external thread exposed a writer-ownership problem: the long-lived ADS formal-agent App Server retained effective ownership after the ADS turn completed.

H3 added terminal `thread/unsubscribe` only after result and resource receipt freeze and prevented read-only status inspection from resuming/reclaiming released threads.

Regression:

```text
THREAD_RELEASE_REGRESSION=PASS
```

On the tested Codex build, unsubscribe alone did not immediately release writer access. H4 therefore additionally recycles only the formal-agent App Server process once all known formal-agent tasks are safely terminal, receipt-complete, approval-free and unsubscribed.

Regression:

```text
PROCESS_RELEASE_REGRESSION=PASS
```

The real acceptance task then produced:

```text
turn completed             PASS
resource-receipt/ready     PASS
thread/released            PASS / unsubscribed
app-server/released        PASS
later ADS status read      PASS / no reclaim
```

The user then continued the released thread from another Codex client. Read-only persistence evidence confirmed the later turn advanced the same underlying Codex thread identity.

Accepted result:

```text
ADS formal Codex thread creation            PASS
terminal result/usage freeze                PASS
subscription release                        PASS
formal-agent process release                PASS
external client writer handoff              PASS
same-thread later continuation              PASS
read-only ADS status does not reclaim       PASS
simultaneous multi-client writing           NOT CLAIMED
```

## Desktop sidebar reconciliation remains independent

The catalog behavior was tested separately.

Creating/completing a genuine Desktop-native new thread repeatedly advanced Desktop's catalog synchronization state and imported previously missing ADS-created threads.

The following did not independently trigger adoption in bounded tests:

```text
open exact thread by deeplink
continue the already-open external thread
open the New Chat composer without sending
```

For the composer-only discriminator, both the Desktop catalog watermark and observation sequence remained unchanged and the fresh ADS thread remained absent.

Therefore the smallest reproduced reconciliation trigger on the tested build is:

```text
Desktop-native new-thread creation/completion
```

No supported explicit Desktop sidebar reindex API was identified.

## H6 candidate is frozen but not live

The accepted integration direction is to stop depending on immediate Desktop sidebar registration and expose the canonical exact-thread handoff directly on completed ADS Codex tasks.

Prepared H6 behavior:

```text
public threadId
public desktopThreadUrl = codex://threads/<threadId>
terminal task persistence preserves both
portable/text receipt prints exact URI
Rich Task Card exposes Open in Codex Desktop
H4 writer/process release remains intact
experimental threadSource="user" override removed
```

Validation:

```text
DESKTOP_DEEPLINK_REGRESSION=PASS
PROCESS_RELEASE_REGRESSION=PASS
node --check codex-agent-executor.mjs PASS
node --check agent-tools.mjs PASS
node --check agent-card-ui.mjs PASS
DESKTOP_DEEPLINK_ACTIVATION_PREFLIGHT=PASS
NO_FILES_MODIFIED=true
```

Critical boundary:

```text
H4 live runtime                      VERIFIED / ACTIVE
H6 candidate                         PREPARED / PREFLIGHTED
H6 activation                        NOT YET PERFORMED
post-H6 real acceptance              NOT YET PERFORMED
```

The repository must preserve this distinction so a later session does not confuse prepared local code with verified live behavior.

## Source Vault state remains unchanged

No Source Universe or Source Vault content changed during this investigation.

Checkpoint 271's substantive Source Vault route remains valid and will resume after the user-selected Codex integration work is closed.

Current Source Vault boundary remains:

```text
permanent Source Registry           MIGRATED / VERIFIED
Alembic head                        0003_source_universe
first permanent corpus compare      20 / 20 MATCH
source ingestion                    NOT STARTED
working-store integrity audit       PENDING
independent encrypted backup proof  PENDING
clean restore + restored audit      PENDING
Course 2                            BLOCKED
```

## Durable evidence route

```text
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/local_execution/validation/022_formal_codex_thread_persistence_and_desktop_visibility_baseline.md
docs/local_execution/validation/023_thread_source_user_visibility_hypothesis_falsified.md
docs/local_execution/validation/024_completed_codex_thread_writer_handoff_verified.md
docs/local_execution/validation/025_codex_desktop_catalog_reconciliation_trigger_isolated.md
docs/local_execution/validation/026_codex_desktop_deeplink_handoff_candidate_preflighted.md
```

Machine-specific candidate files, exact installed-file backups and host-specific diagnostics remain in ignored private operational state and are not required to understand the public experiment conclusion.

## Exact continuation

The next action is not another discovery experiment. It is the already-prepared bounded H6 acceptance sequence:

```text
1. activate the fail-closed H6 three-file candidate on the local Codexless installation
2. restart Codexless and Secure MCP Tunnel through the repository-owned procedure
3. reverify ADS authority/profile state
4. run one fresh minimal formal Codex task through the normal visible consent path
5. verify terminal output exposes threadId and codex://threads/<threadId>
6. verify Rich/portable handoff presentation
7. open the exact released thread through that handoff
8. verify same-thread continuation remains possible
9. preserve H6 success/failure
10. return to Source Vault reviewed ingestion after this integration gate closes
```

No direct Codex private catalog/session mutation is permitted as part of this continuation.
