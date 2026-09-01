# Direct Git ACL repair, network profile, and outer ChatGPT tool-safety boundary

**Date:** 2026-09-01  
**Status:** `DIRECT_GIT_PROFILE_PARTIAL / FILESYSTEM BLOCKER RESOLVED / INHERIT NETWORK ENABLED / OUTER CHATGPT TOOL-SAFETY BLOCKED FINAL FETCH DISPATCH`  
**Scope:** Preserve the post-015 direct-lane diagnostic sequence from host ACL confirmation through the final ChatGPT/OpenAI tool-safety block.  
**Authority:** Bounded local-execution evidence. This record does not classify a new Git-specific MCP architecture as accepted, does not alter Research 105 acceptance, and does not authorize Source Vault ingestion.  
**Declared references:** `research:105`, `checkpoint:270`, `path:docs/local_execution/validation/013_direct_lane_git_metadata_permission_profile_source_audit.md`, `path:docs/local_execution/validation/014_direct_git_profile_runtime_application_partial.md`, `path:docs/local_execution/validation/015_direct_git_profile_active_metadata_write_denied_windows_acl_investigation.md`, `path:docs/model_collaboration/threads/MC-0009/BRIEF.md`, `path:docs/CURRENT_STATE.md`

## 1. Why this record exists

Validation 015 ended with a strong but not yet host-confirmed hypothesis: the custom `ads-direct-git` profile was genuinely active and projected `.git` as writable, but an older persistent Windows deny ACE for the workspace capability SID could still be blocking `.git/FETCH_HEAD`.

The subsequent diagnostic work materially changed that state. The ACL hypothesis was confirmed on the host, the stale deny ACEs were narrowly removed, the filesystem failure disappeared, a separate network boundary was identified and widened only for the inherit profile, and the final `git fetch origin` attempt was then blocked before local execution by the outer ChatGPT/OpenAI tool-safety layer.

That sequence is significant enough to preserve as a first-class numbered local-execution validation record rather than leave only in collaboration routing context.

## 2. Host ACL inspection confirmed the stale workspace-capability deny

The host-side Codex capability state for the real ADS checkout reported:

```text
workspace capability SID
S-1-5-21-2829914423-880881765-1876937842-591403033

.git writable-root capability SID
S-1-5-21-2241125269-3269922455-1794855488-3921961636
```

Before repair, the `.git` ACL contained both the old workspace deny and the new `.git` allow:

```text
S-1-5-21-2829914423-880881765-1876937842-591403033:(DENY)(W,D,Rc,DC)
S-1-5-21-2829914423-880881765-1876937842-591403033:(OI)(CI)(IO)(DENY)(W,D,Rc,GW,DC)
S-1-5-21-2241125269-3269922455-1794855488-3921961636:(OI)(CI)(M)
```

`.git\FETCH_HEAD` inherited the workspace-SID deny while also inheriting Modify for the `.git`-specific capability:

```text
S-1-5-21-2829914423-880881765-1876937842-591403033:(I)(DENY)(W,D,Rc,DC)
S-1-5-21-2241125269-3269922455-1794855488-3921961636:(I)(M)
```

This host evidence confirmed the exact identity match predicted in validation 015. The contradiction between Codex reporting `.git` as a writable root and Windows denying `FETCH_HEAD` was therefore explained by persistent ACL state, not by profile-selection failure.

## 3. Narrow ACL repair succeeded

A first `icacls /remove:d` attempt processed zero files and made no change. The ACL was then edited through the Windows ACL object model with guards that selected only:

```text
explicit rules only
AccessControlType = Deny
identity = S-1-5-21-2829914423-880881765-1876937842-591403033
exact expected rule count = 2
```

The two explicit deny ACEs were removed from only:

```text
C:\Projects_Data\autonomous-data-science-system\.git
```

The post-repair `.git` ACL retained the dedicated writable-root capability:

```text
S-1-5-21-2241125269-3269922455-1794855488-3921961636:(OI)(CI)(M)
```

and no longer contained the two explicit workspace-SID deny ACEs.

The inherited deny disappeared from `.git\FETCH_HEAD` as well. `FETCH_HEAD` retained inherited Modify access for the `.git` writable-root capability.

No `.agents`, `.codex`, unrelated repository, Source Universe, credential, browser, or other host ACL was modified.

A pre-repair SDDL backup was preserved outside the repository in the user's temporary directory during the host operation.

## 4. First fetch after ACL repair crossed the former filesystem boundary

With `ads-direct-git` still active and no profile broadening yet, a direct model-free `codex.command_exec` call ran:

```text
git fetch origin
access=inherit
```

The previous failure:

```text
error: cannot open '.git/FETCH_HEAD': Permission denied
```

was gone.

The command instead progressed to GitHub network access and failed with:

```text
exit code: 128

fatal: unable to access
'https://github.com/shakaarlatief/autonomous-data-science-system.git/':
Failed to connect to github.com port 443 after 55 ms:
Could not connect to server
```

At that moment the direct inherit sandbox still reported:

```text
networkAccess: false
```

Immediate ACL verification showed:

```text
stale workspace-SID DENY on .git         absent
stale workspace-SID DENY on FETCH_HEAD   absent
.git writable-root capability Modify     present
FETCH_HEAD inherited Modify               present
```

Therefore the previous Windows filesystem blocker was resolved. This fetch did not complete end-to-end because it stopped at the network boundary, but it did get past the exact earlier `FETCH_HEAD` permission-denied point.

## 5. Network authority was enabled only for the inherit profile

The machine-local `ads-direct-git` profile was then changed only by adding network access while preserving its filesystem structure:

```text
extends = :workspace
explicit .git write
network.enabled = true
```

The host-side Codexless HTTP runtime was restarted with the same fixed profile and private override-file mechanism.

Model-free `project_context` then reported:

```text
active permission profile   ads-direct-git
extends                     :workspace
trusted ADS root            C:\Projects_Data\autonomous-data-science-system
.git writable root          present
override count              2
networkAccess               true
```

A separate `access=readOnly` probe still resolved to:

```text
permissionCeiling   ads-direct-git
permissionProfile   :read-only
authoritySource     host-profile-override
trustedAncestor     c:\projects_data\autonomous-data-science-system
```

A read-only `git ls-remote origin HEAD` could not connect to GitHub. This provided runtime evidence that the network widening was confined to inherited `ads-direct-git` authority and did not leak into the `:read-only` downscope.

## 6. Final direct fetch was blocked before Codex execution

After both relevant inner authority dimensions were presenting correctly:

```text
.git writable under ads-direct-git   PASS
inherit networkAccess=true           PASS
readOnly -> :read-only               PASS
trusted ADS root                     PASS
```

ChatGPT attempted the required direct model-free call:

```text
git fetch origin
access=inherit
```

The tool invocation was rejected before local dispatch with the user-visible ChatGPT/OpenAI message:

```text
Deze toolaanroep is geblokkeerd door de veiligheidscontroles van OpenAI.
Controleer nogmaals wat je verzendt.
```

This specific fetch therefore did not execute in Codex App Server and provides no new local Git transport result.

A subsequent generic `icacls .git` invocation was also blocked by the same outer tool-safety layer. No alternate shell wrapper or disguised command was used to route around the block.

No formal Codex model agent was launched, no `agent_start` or other formal agent operation was used, and no formal agent approval was requested.

## 7. Final repository state at the outer-safety boundary

The last reported local state after the blocked dispatch was:

```text
local HEAD
    063fdc99c76d7821efc58bb83823bcad33c068c5

origin/v1-source-vault-bootstrap-resume
    cb48c1ac539592e63b13cbc8e4e2413cb0b196a0

status
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 8]
```

The tracked working tree remained clean.

No `git pull --ff-only` was run because the prerequisite final fetch did not execute successfully.

No commit, push, merge, rebase, reset, Source Universe mutation, tunnel modification, or new filesystem-authority broadening occurred during the final dispatch attempt.

## 8. Layered diagnosis after this sequence

The diagnostic evidence now separates the stack as follows:

```text
ChatGPT reaches the local Codexless bridge                 PASS
model-free direct command execution                        PASS for permitted commands
ads-direct-git profile recognized and selected             PASS
trusted ADS-root binding                                   PASS
readOnly downscope                                         PASS
explicit .git write projection                             PASS
stale Windows workspace-capability deny diagnosis          CONFIRMED
narrow stale-deny ACL repair                               PASS
previous .git/FETCH_HEAD permission-denied failure         RESOLVED
inherit networkAccess=true                                 PASS
readOnly network widening absent                           PASS
final generic git fetch dispatch                           BLOCKED BEFORE LOCAL EXECUTION
blocking layer                                             ChatGPT/OpenAI outer tool safety
end-to-end direct Git fetch                                NOT YET PROVEN
```

The bounded overall classification therefore remains:

```text
DIRECT_GIT_PROFILE_PARTIAL
```

but the meaning is now narrower than in validation 015. The remaining unresolved boundary is no longer demonstrated to be Codex filesystem or network authority. The final experiment was prevented from reaching those inner layers by the outer ChatGPT tool-safety decision.

## 9. Relationship to MC-0009

MC-0009 was opened after the diagnostic evidence above existed, with its independent substantive ADS target deliberately frozen at:

```text
cb48c1ac539592e63b13cbc8e4e2413cb0b196a0
```

The MC-0009 neutral brief already records these observed facts so Claude can research the feasibility question without being shown a ChatGPT candidate architecture.

This validation record is a post-freeze preservation of the same experimental evidence. It does not change Claude's frozen substantive review target, does not introduce a preferred Git-specific MCP design into the independent evidence base, and does not alter the `BLIND_TO_CANDIDATE` intent of the first collaboration phase.

The next architectural question is whether a bounded semantic MCP Git action, a different existing primitive, or another supported mechanism can distinguish a generic-command tool-safety block from a categorical platform prohibition. MC-0009 is the governed independent-then-comparative research mechanism for that question.

## 10. Current continuation boundary

Do not infer from this record that direct local Git through ordinary ChatGPT is impossible, and do not infer that it is operationally accepted.

The evidence supports only:

```text
inner filesystem blocker        diagnosed and repaired
inner inherit-network boundary  explicitly widened and validated
outer generic-tool dispatch     blocked in the final experiment
formal Codex Git route          previously proven separately
```

Further architecture or tool-contract changes should remain behind MC-0009's independent research gate.

Source Vault ingestion remains paused and unchanged during this focused audit.
