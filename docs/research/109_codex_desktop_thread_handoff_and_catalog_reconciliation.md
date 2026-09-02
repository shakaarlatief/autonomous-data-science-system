# Research 109: Codex Desktop Thread Handoff and Catalog Reconciliation

**Status:** CLOSED PRE-H6 DIAGNOSTIC RECORD / H4 VERIFIED / H6 PRE-ACTIVATION BOUNDARY; POST-H6 WORK CONTINUES IN RESEARCH 110
**Date:** 2026-09-02  
**Opened:** 2026-09-02  
**Closed for current diagnostic scope:** 2026-09-02  
**Scope:** Determine whether formal Codex threads created through the ADS Codexless bridge are genuine Codex threads, whether they can be discovered and continued in Codex Desktop or the Codex IDE surface, what prevents post-completion handoff, why Desktop `Recent` may omit externally created local threads, and what supported integration boundary ADS should use without fabricating Codex state.  
**Authority:** Bounded local-execution research. This record does not make Codexless or Codex Desktop project authority. It records empirical behavior and the accepted current integration direction. The live ADS project state remains governed by `docs/CURRENT_STATE.md` and `docs/current_routing.json`.

## 1. Why this investigation was opened

After Research 105 and Checkpoints 269-271 established a usable bounded ChatGPT -> Codexless -> local execution route, the project owner asked a narrower integration question:

```text
If ChatGPT invokes a real Codex model through ADS,
can that same Codex conversation also appear in the normal Codex application
so the user can inspect and continue it there?
```

The desired shape was not simultaneous multi-client control. The desired shape was sequential handoff:

```text
ChatGPT / ADS
    -> starts a formal Codex thread
    -> Codex completes the requested turn
    -> ADS freezes the result and usage receipt
    -> ADS releases ownership
    -> the same persisted Codex thread can be opened in Codex Desktop / IDE
    -> the user may continue that same thread later
```

This matters because it lets ADS use Codex as a delegated coding/reasoning worker while preserving a normal human-visible Codex conversation for inspection and continuation.

The investigation deliberately separated three different questions that initially looked like one problem:

```text
1. Does ADS create a genuine persistent Codex thread?
2. Can another Codex client take writer ownership after ADS finishes?
3. Does Codex Desktop immediately list that external thread in its Recent/sidebar catalog?
```

The final evidence showed that these are separate mechanisms.

## 2. Relevant execution architecture

The ADS Codexless bridge exposes two conceptually different paths.

### 2.1 Model-free local execution

```text
codex.command_exec
    -> official Codex App Server command/exec
    -> no Codex model turn
```

This is the bounded deterministic execution route used for local reads, tests and accepted semantic Git actions when authority permits.

### 2.2 Formal Codex Agent execution

```text
codex.agent_start
codex.agent_send
codex.agent_show
codex.agent_approve / reject / cancel
```

This route starts real metered Codex model work. It creates a formal Codex thread and turn, is subject to the Codex Call Profile / explicit consent policy, and returns the Codex result to ChatGPT through the bridge.

The investigation concerns only the second route.

## 3. First proof: ADS can invoke a real Codex model turn

A minimal read-only formal-agent task was dispatched through the normal ADS Codex Agent interface:

```text
Inspect the current repository and tell me the current Git branch.
Do not modify anything.
```

The call returned through the normal Codex task/consent path and completed successfully using the locally available Codex model.

Observed result:

```text
real Codex model turn     PASS
local ADS repository read PASS
final result returned     PASS
repository mutation       none
```

This established that the ADS bridge was not merely wrapping shell execution. It could create and supervise a real Codex model thread.

## 4. Persistence discovery: the ADS turn is a normal Codex session

The next question was whether that Codex result existed only inside the ADS bridge or was persisted as normal Codex history.

Read-only inspection of the standard Codex user data showed that the ADS-created formal thread was written under the ordinary Codex session/state locations, including the normal session JSONL history and core Codex SQLite state.

Public-safe location forms:

```text
%USERPROFILE%\.codex\sessions\...
%USERPROFILE%\.codex\state_5.sqlite
```

The session metadata identified the Codexless formal-agent origin while still using the normal Codex persistence substrate.

The important conclusion was:

```text
ChatGPT -> ADS -> Codexless -> Codex App Server
    does create a genuine persistent Codex thread
```

It is not merely a transient answer copied back into ChatGPT.

That reduced the problem substantially. The problem was now discovery and ownership, not thread existence.

## 5. Initial Desktop visibility failure

Although the ADS-created thread existed in ordinary Codex persistence, it initially did not appear in Codex Desktop `Recent`.

Baseline read-only evidence showed a complete-looking thread:

```text
session rollout exists
core thread row exists
completed turn exists
user input exists as a normal turn item
agent final response exists
thread is not archived
```

but the Desktop-visible local catalog did not contain the new thread.

The investigation therefore rejected the early assumption:

```text
not visible in Desktop
    therefore
not a real Codex thread
```

That implication is false. A real persisted Codex thread can exist while the Desktop sidebar has not yet cataloged it.

## 6. H1: explicit `threadSource = "user"`

The first narrow hypothesis was that ADS omitted a classification field required for Desktop discovery.

H1:

```text
thread/start with threadSource = "user"
    -> normal Desktop-visible user thread
```

A private candidate changed only the `thread/start` parameter set:

```javascript
const threadParams = {
  cwd: effectiveCwd,
  ephemeral: false,
  threadSource: "user",
};
```

The change was tested in isolation and then activated through a fail-closed host-maintenance procedure with exact file hashes, backup, syntax check and rollback behavior.

A new real Codex thread was then created through ADS.

Observed result:

```text
threadSource persisted as user    PASS
thread persisted normally         PASS
Desktop Recent visibility         FAIL
```

Therefore H1 was falsified as the explanation for the visibility problem.

The field was later removed from the H6 candidate because no evidence supported retaining it.

## 7. Legacy user-event hypothesis corrected

During the investigation, one possible explanation was that ADS-created threads lacked an older top-level user-message event used by the history path.

Further source inspection showed that current Codex persistence does not require that legacy event for normal completed-turn history. Durable user input is represented by the completed turn items.

Therefore:

```text
absence of a legacy EventMsg-style user event
    !=
proof of malformed current Codex thread persistence
```

This correction prevented the investigation from fabricating or patching legacy history records to make the thread look more like an assumed schema.

No Codex JSONL, SQLite thread row, history row or catalog row was manually edited at any point.

## 8. Desktop has a separate local thread catalog

The stronger discriminator came from inspecting the separate Codex Desktop database:

```text
%USERPROFILE%\.codex\sqlite\codex-dev.db
```

The relevant structure included a Desktop-oriented `local_thread_catalog` plus synchronization state.

At the time of the first inspection:

```text
core Codex state
    contained ADS threads

Desktop local_thread_catalog
    did not contain those ADS threads
```

This established a stronger architecture:

```text
Codex core thread persistence
    !=
Codex Desktop sidebar catalog
```

The investigation deliberately treated the Desktop catalog as private application state. It was inspected read-only only.

Direct insertion/update of `local_thread_catalog` was explicitly rejected as a solution.

## 9. Desktop-native control thread triggered catalog reconciliation

A genuine new local thread was created manually in Codex Desktop as a control.

After that Desktop-native thread completed, read-only inspection showed that the Desktop catalog synchronization state had advanced and previously missing ADS-created threads had been imported into the local catalog.

This effect reproduced again later.

The important observation was:

```text
before Desktop-native control thread
    valid ADS threads exist in core state
    missing from Desktop local catalog

after Desktop-native control thread
    Desktop catalog watermark advances
    observation sequence advances
    previously missing ADS threads are imported
```

The imported ADS rows retained their real ADS working-directory and Git context. They were not converted into fake Desktop-created threads.

This proved that Desktop could understand the external threads once its own reconciliation path examined them.

## 10. Direct deeplink discovery

The investigation then established that a valid external Codex thread can be opened directly through the canonical local Codex URI:

```text
codex://threads/<thread-id>
```

This worked even when the same thread was absent from Desktop `Recent`.

Therefore:

```text
sidebar discoverability
    is not required for
exact thread openability
```

This became a key integration seam later in H6.

## 11. Writer ownership problem

Once an ADS-created thread could be opened in Codex Desktop, a second independent problem appeared.

The Desktop UI indicated that the thread was already open or controlled by another application and could not accept input.

This localized the blocker to thread ownership / App Server lifecycle rather than persistence or Desktop parsing.

The Codexless formal-agent executor used one long-lived App Server process and retained its thread subscription after a turn completed. In addition, status refresh logic could call `thread/resume`, potentially reclaiming a thread merely while checking state.

This produced H3.

## 12. H3: unsubscribe completed threads

H3:

```text
After an ADS turn is terminal and its final result/resource receipt is frozen,
Codexless should unsubscribe from that thread exactly once.
Read-only status checks must not resume/reclaim the released thread.
An explicit later ADS follow-up may resume it again.
```

A private candidate added the official App Server lifecycle call:

```text
thread/unsubscribe
```

only after:

```text
terminal turn status
final result captured
resource/usage receipt captured
no pending approval
```

Focused regression verified:

```text
terminal result preserved             PASS
resource receipt captured first       PASS
thread/unsubscribe exactly once       PASS
later agent_show does not refresh     PASS
later agent_show does not resume      PASS
explicit later agent_send can resume  PASS
```

The H3 change was activated through the same exact-hash / backup / syntax-check / rollback host-maintenance pattern.

However, empirical Desktop behavior showed that `thread/unsubscribe` alone did not immediately release the writer lock on the tested Codex build.

That result led to H4.

## 13. H4: release the formal-agent App Server process

Empirical testing showed a stronger lifecycle relationship:

```text
thread unsubscribed
    but
formal-agent App Server process still alive
    -> external client may still see writer ownership

formal-agent App Server process terminated/recycled
    -> writer lock is released
```

H4 therefore extended the release policy:

```text
when all known ADS formal-agent threads are terminal,
have frozen resource receipts,
have no pending approvals,
and have been unsubscribed,
close/recycle only the formal-agent App Server process
```

Important constraints:

```text
frozen ADS task snapshots remain readable
agent_show on a released terminal task does not restart the App Server
an explicit later ADS follow-up may restart the App Server and resume the exact thread
model-free Codexless tools are not conceptually replaced by this lifecycle rule
```

Focused regression:

```text
PROCESS_RELEASE_REGRESSION=PASS
```

The H4 runtime was activated on the local Codexless installation.

## 14. Real H4 acceptance test

A minimal formal Codex task was run after H4 activation.

The returned task event sequence included:

```text
turn completed
resource-receipt/ready
thread/released          status = unsubscribed
app-server/released
```

A later read-only task-state inspection produced no new App Server activity and did not reclaim the thread.

The user then opened and continued the same released Codex thread from the Codex IDE surface and sent a harmless follow-up.

Read-only persistence inspection confirmed that the original thread identity remained the same and its update time advanced after the IDE follow-up.

Therefore the core handoff objective is empirically verified:

```text
ADS creates formal Codex thread          PASS
ADS turn completes                       PASS
result + usage frozen                    PASS
thread subscription released             PASS
formal-agent App Server released         PASS
another Codex client gains writer access PASS
later IDE turn stays on same thread       PASS
ADS status reads do not reclaim thread   PASS
```

This is the strongest accepted result from the investigation.

## 15. H5: isolate the Desktop sidebar reconciliation trigger

Writer handoff and sidebar discovery were now known to be independent.

The next investigation asked what actually causes Codex Desktop to adopt externally created local threads into `Recent`.

Several candidate triggers were tested.

### 15.1 Opening the exact thread by deeplink

```text
open codex://threads/<thread-id>
```

Result:

```text
thread opens          PASS
catalog adoption      NO
```

### 15.2 Continuing the deeplink-opened external thread in a Codex client

A later turn on the same external thread proved thread continuity but did not by itself cause Desktop local catalog adoption.

### 15.3 Reopening / focusing Codex Desktop

Simply bringing Desktop to the foreground or reopening the application did not provide a reliable fresh adoption event in the bounded tests.

### 15.4 Opening the Desktop New Chat composer without sending

A fresh ADS-created thread was deliberately left absent from `local_thread_catalog`. The user then clicked `New chat` / `Nieuwe chat` in Codex Desktop but sent nothing.

Read-only database inspection afterward showed:

```text
fresh ADS thread catalog row      absent
catalog watermark                 unchanged
observation sequence              unchanged
```

Therefore merely opening the composer is not the reconciliation trigger.

### 15.5 Creating/completing a Desktop-native new thread

This remained the smallest repeatedly observed trigger.

After a genuine Desktop-native thread creation/completion:

```text
catalog watermark        advanced
observation sequence     advanced
missing ADS threads      imported
```

The effect reproduced more than once.

Current bounded conclusion:

```text
Desktop-native new-thread creation/completion
    is the smallest reproduced reconciliation trigger
on the tested Codex Desktop build
```

No supported API for explicitly asking Desktop to rebuild/reindex its sidebar catalog was identified during this investigation.

## 16. Upstream compatibility interpretation

Upstream Codex reports/source inspection reviewed during the investigation describe the same general architecture class: a separate App Server can create a valid local thread that remains directly openable while an already-running Desktop instance does not immediately live-register it in the sidebar.

The project therefore treats the behavior as a Codex Desktop catalog/reconciliation limitation rather than evidence that ADS is creating invalid threads.

This distinction changes the correct engineering response.

Incorrect response:

```text
rewrite private Desktop SQLite catalog rows
fabricate session events
patch thread metadata until the sidebar happens to show it
```

Accepted response:

```text
preserve normal official Codex thread lifecycle
release ownership correctly
use a supported direct thread handoff URI
allow Desktop's own catalog synchronization to remain Desktop-owned
```

## 17. H6: canonical Desktop deeplink as the durable handoff seam

Because no supported sidebar reindex RPC was identified, H6 defines the clean integration fallback:

```text
Every completed formal ADS Codex task should expose:

threadId
codex://threads/<threadId>
```

The URI has already been empirically proven to open the exact ADS-created thread.

A private candidate was prepared with these changes:

```text
preserve H4 thread/process release behavior
remove the unsupported/unneeded experimental threadSource="user" override
expose threadId through the public Agent projection
expose desktopThreadUrl = codex://threads/<threadId>
preserve both fields in terminal task persistence
print the URI in terminal portable/text receipts
show Open in Codex Desktop in the Rich Task Card
```

Candidate validation:

```text
DESKTOP_DEEPLINK_REGRESSION=PASS
PROCESS_RELEASE_REGRESSION=PASS
node --check codex-agent-executor.mjs PASS
node --check agent-tools.mjs PASS
node --check agent-card-ui.mjs PASS
activation preflight PASS
```

The activation script is fail-closed and requires exact live/candidate hashes, timestamped backups, per-file syntax checks, and rollback of all touched files if activation fails.

### Critical current-state boundary

At the time this public record is written:

```text
H4 live runtime                         ACTIVE / VERIFIED
H6 deeplink candidate                   PREPARED / PREFLIGHTED
H6 live activation                      NOT YET PERFORMED
post-H6 real Codex acceptance test      NOT YET PERFORMED
```

A future collaborator must not infer H6 is live merely because its candidate and activation procedure exist.

## 18. Rejected or disproven approaches

The investigation deliberately preserves negative evidence because each failure narrowed the architecture.

```text
ADS thread is not real                              disproven
threadSource="user" causes Desktop visibility       disproven
legacy user event absence proves malformed thread  disproven
thread/unsubscribe alone frees writer immediately  incomplete on tested build
opening deeplink triggers sidebar reconciliation   no
continuing external thread triggers adoption       no in bounded test
opening New Chat composer triggers adoption        no
manually edit Desktop private catalog              rejected by design
fabricate/modify Codex session JSONL               rejected by design
```

## 19. Accepted operational lessons

### 19.1 Persistence, writer ownership and UI discovery are separate layers

```text
CORE THREAD PERSISTENCE
    does the Codex thread exist correctly?

WRITER OWNERSHIP / PROCESS LIFECYCLE
    which App Server/client currently controls it?

DESKTOP CATALOG / RECENT
    has Desktop indexed it for sidebar discovery?
```

A failure in one layer must not be interpreted as failure in all three.

### 19.2 Direct openability is a stronger integration seam than sidebar appearance

A canonical thread identifier plus supported deeplink is deterministic. Sidebar synchronization is currently Desktop-owned and may be delayed.

### 19.3 Read-only status must not accidentally reclaim released work

Observability logic can become a state mutation if it resumes a thread. Terminal snapshots must therefore be frozen and served locally after handoff rather than refreshing through App Server merely to answer status queries.

### 19.4 Process lifetime can be part of practical ownership semantics

On the tested build, unsubscribe and process lifetime had different effects. Correct release required the formal-agent App Server process to terminate/recycle after terminal work.

### 19.5 Do not repair third-party private state to improve presentation

The investigation had enough filesystem access to inspect Codex state, but intentionally did not mutate Codex private databases or session history. A UI catalog problem should remain visible rather than being hidden by unsupported database edits.

## 20. Relationship to ADS authority and Source Vault work

This investigation changes how ADS may hand off a delegated Codex task. It does not change project-development authority.

```text
public ADS repository   sole project-development authority
Codexless               replaceable bounded execution transport
Codex App Server        execution/session mechanism
Codex thread            operational conversation history
Codex Desktop / IDE     presentation and continuation client
```

No Source Universe state, Source Vault content, original source artifact, registry data, backup payload, credential or recovery state was changed by the thread-handoff experiments.

The substantive Source Vault continuation established at Checkpoint 271 remains valid. This investigation temporarily occupied the active interaction because the user chose to complete and preserve the Codex integration work before continuing.

## 21. Public/private preservation boundary

The public repository preserves:

```text
architecture
hypotheses
experiment chronology
verified behavior
negative evidence
accepted handoff design
activation state
continuation boundary
```

Machine-specific details remain outside public Git where they are not required for reproducibility, including exact user profile paths, local backup filenames and local private runtime identities.

Private ignored `.ads-private` material may retain exact candidate files, activation scripts, hashes and host-specific diagnostics needed for local execution. Those local files are supporting operational state, not the only record of the investigation.

## 22. Exact continuation

The next step for this investigation is deliberately narrow:

```text
1. activate the already-preflighted H6 three-file candidate through the fail-closed host procedure
2. restart Codexless / tunnel through the repository-owned operations procedure
3. reverify ADS authority state
4. start one fresh minimal formal Codex task through the normal consent path
5. verify terminal public state contains threadId + desktopThreadUrl
6. verify the Rich/portable Task Card exposes the exact Codex Desktop handoff
7. open the exact released thread through that handoff
8. confirm the user can continue the same thread after completion
9. preserve the final acceptance or failure result before returning to Source Vault ingestion
```

If H6 fails, preserve the failure and roll back through the prepared activation backups. Do not patch the Desktop catalog or Codex session database.

If H6 succeeds, the remaining known limitation is only automatic `Recent` registration of externally created local threads. The canonical deeplink remains the supported deterministic handoff surface unless upstream Codex later exposes a supported live-registration/reindex mechanism.
