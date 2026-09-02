# Direct Git Investigation Lessons

**Status:** Durable cross-cutting lessons from the completed bounded direct-lane investigation  
**Date:** 2026-09-02  
**Scope:** Preserve the reusable methodological, diagnostic, operational, and safety lessons learned while determining whether the direct model-free ChatGPT -> bounded MCP -> Codex command/exec path could safely perform ordinary ADS Git synchronization.  
**Authority:** Retrospective evidence synthesis. Exact capability claims remain governed by the validation records and `SEMANTIC_PULL_ACCEPTANCE.md`; the canonical project-development method remains `docs/DEVELOPMENT_METHOD.md`.

## 1. Why this record exists

The direct Git investigation produced more durable knowledge than the narrow result that one Git pull eventually worked.

At several points, the observed evidence could easily have been summarized too early as:

```text
this path failed
therefore this capability is unavailable
```

That conclusion would have been wrong.

The project already had a safe formal Codex-agent route that could perform the necessary synchronization. Operationally, stopping there would have been defensible. Scientifically and architecturally, however, it would have answered a different question.

The actual question was:

```text
Can the direct bounded model-free route itself perform the required ADS synchronization
without turning into unrestricted shell / host authority?
```

The eventual answer is:

```text
YES
for the exact bounded semantic contracts that were frozen and verified.
```

The path to that answer is important because it exposed a reusable ADS investigation method for problems that cross multiple software, policy, runtime, operating-system, and repository layers.

## 2. The important turning point

The first generic direct Git attempt was blocked before local execution. A reasonable but premature interpretation was that the direct lane might simply be unsuitable for Git synchronization and that ADS should rely on the already-working formal Codex-agent route.

Additional research changed the interpretation.

The key clue was that an outer platform or tool-safety layer may reason differently about:

```text
broad arbitrary command capability
    versus
narrow semantic action with a strict schema and fixed operation
```

That led to a bounded semantic `git fetch origin` experiment using the same underlying Codex command execution path. It dispatched and executed successfully.

That result proved that the earlier generic-command block was not equivalent to a categorical statement that Git networking or Git metadata operations were impossible through the direct architecture.

The investigation therefore continued rather than promoting a route-specific failure into a capability-wide impossibility claim.

## 3. Core lesson: a failed path is not the same as an impossible capability

A failure establishes only what the experiment actually tested.

For example:

```text
generic command carrying git fetch origin
    blocked before local execution
```

supports:

```text
the tested generic-command dispatch was blocked
```

It does not, by itself, support:

```text
Git fetch is impossible through every bounded direct MCP contract
```

Likewise, the existence of a working fallback does not settle the feasibility question for the target path:

```text
formal Codex agent can perform the operation
```

proves an available operational route, but does not answer:

```text
can the direct model-free semantic route perform it safely?
```

ADS should therefore keep the **operational fallback question** separate from the **capability-feasibility question**.

## 4. Core lesson: identify the exact failing layer

The direct-lane investigation required distinguishing several layers that can produce superficially similar failures:

```text
ChatGPT / OpenAI outer safety and dispatch
MCP action contract and schema
Codexless public-surface registration and routing
Codex authority/profile resolution
network permission
Codex command/exec sandbox
Windows filesystem ACLs and capability identities
Git behavior
repository branch / upstream / cleanliness preconditions
```

A message such as `Permission denied`, a blocked tool call, a missing action, a network failure, and a dirty-tree refusal are not one class of failure merely because they all prevent the desired end result.

For a multi-layer system, investigation should ask:

```text
What is the last layer that is positively proven to have worked?
What is the first layer where the observed result diverges from the contract?
```

This framing dramatically reduces the hypothesis space.

## 5. Core lesson: a reported permission profile is not sufficient evidence of effective host authority

The accepted `ads-direct-git` profile could correctly report:

```text
.git writable
network enabled
```

while Windows still contained an applicable DENY access-control entry on `.git`.

The dedicated `.git` writable capability had `Modify`, but the overlapping DENY still prevented Git from opening `.git/FETCH_HEAD`.

Therefore:

```text
logical permission configuration
    is not automatically identical to
observed effective operating-system permission
```

When a sandboxed or capability-based system projects permissions into host ACLs or operating-system identities, ADS must verify the effective host state when the observed behavior contradicts the declared profile.

This is why `AUTHORITY_BOOTSTRAP.md` and `ACL_INTEGRITY_GATE.md` are separate gates.

## 6. Core lesson: runtime lifecycle matters

A correct state can later become incorrect without the project intentionally changing the accepted contract.

The `.git` DENY condition was repaired once and the repair was verified. Later, after further Codex/Codexless/sandbox lifecycle activity, the problematic DENY state appeared again.

That means:

```text
verified once
    does not imply
persistent across every restart / lifecycle transition
```

The exact lifecycle event that recreated the DENY was not isolated, so ADS does not claim a stronger causal mechanism than the evidence supports.

Instead the operational consequence is explicit:

```text
after relevant lifecycle change
    re-establish authority bootstrap
    run the read-only ACL integrity gate before direct Git mutation
```

A recurring state assumption that matters to safe execution must become a gate, not a memory.

## 7. Core lesson: operational reproducibility is part of architecture

The original restart shorthand:

```powershell
& $CodexlessLauncher
```

was not the complete ADS startup procedure.

A restarted process launched from a fresh PowerShell session fell back to the ordinary workspace profile because the parent process did not contain the required ADS-specific environment:

```text
CODEXLESS_PROFILE
CODEXLESS_CONFIG_OVERRIDES_FILE
CODEXLESS_DEFAULT_CWD
```

This exposed a broader architectural rule:

> If a system capability depends on runtime bootstrap state, the bootstrap and its post-start verification are part of the reproducible architecture.

The project therefore moved the operational knowledge from conversation memory into repository-owned procedures:

```text
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
```

A healthy process or open TCP port is not sufficient proof that the intended authority configuration is active.

## 8. Core lesson: fail-closed experiments are unusually informative

The investigation did not respond to failure by broadening authority until the operation happened to work.

It deliberately avoided using failure as justification for:

```text
danger-full-access
unrestricted host process exposure
arbitrary shell authority
force push
reset
rebase
checkout-based rollback
wrapper commands intended to evade safety
automatic ACL repair
silent fallback to a stronger execution lane
```

Instead the process repeatedly narrowed the question.

That created cleaner evidence because each experiment had a bounded interpretation.

A failed fail-closed experiment can be more useful than an overly permissive success: it can establish precisely which earlier layers worked and which layer first rejected the operation.

## 9. Core lesson: research before architecture changes can overturn a premature conclusion

The direct-lane result is a strong example of why external/source-level research can be necessary before changing architecture or declaring a capability impossible.

Research established that:

```text
Codex permissions support explicit profiles and inheritance
.git can be reopened narrowly inside the trusted workspace root
the Codexless host can apply fixed profile overrides
command/exec is model-free
semantic MCP actions can expose strict caller schemas
```

Community and implementation evidence also suggested that semantic action contracts can matter to outer dispatch behavior, while the official material did not establish a categorical prohibition on Git fetch itself.

That was enough to justify a bounded discriminating experiment.

Without that research, ADS could have stopped at a plausible but false conclusion:

```text
direct model-free Git synchronization is not possible
```

The reusable rule is not "always keep trying." It is:

> When the current evidence cannot distinguish a route-specific failure from a capability-wide limitation, targeted research is warranted before freezing the stronger conclusion.

## 10. Core lesson: negative results are evidence when they are localized

The first semantic pull failed at:

```text
.git/FETCH_HEAD
```

with a local sandbox/permission error.

That was not a useless failed run. Because the action had already passed several earlier boundaries, it established:

```text
semantic action discovery     PASS
outer ChatGPT dispatch        PASS
Codexless routing             PASS
correct authority selection   PASS
network-enabled profile       PASS
local command execution       REACHED
Git metadata filesystem write FAIL
```

The failure therefore removed entire classes of explanations from consideration.

Negative evidence should be preserved in terms of the layer it falsifies or isolates, rather than being summarized only as "the operation failed."

## 11. The layered diagnostic stack

For future cross-system problems, ADS should explicitly consider a stack such as:

```text
1. user intent / exact question
2. platform policy and outer dispatch
3. tool or action contract
4. transport / registration / routing
5. authority/profile selection
6. network capability
7. execution sandbox
8. host operating-system permissions / ACLs
9. underlying program semantics
10. repository or project preconditions
11. postcondition verification
```

Not every investigation will contain every layer, but naming the layers prevents evidence from one layer being incorrectly generalized to another.

## 12. Reusable discriminating-experiment method

The method that emerged from this investigation is:

```text
observe the exact failure
    ->
identify the last proven layer and first suspected failing layer
    ->
separate the target capability question from available fallback routes
    ->
research the relevant contracts / implementation / authoritative documentation
    ->
formulate competing explanations
    ->
design the smallest experiment that can distinguish those explanations
    ->
keep the experiment fail-closed and avoid unrelated authority widening
    ->
preserve both positive and negative evidence by layer
    ->
change only the layer actually implicated by the evidence
    ->
retest the same bounded contract
    ->
repeat verification when lifecycle-sensitive state may have changed
    ->
promote reproducible operational knowledge into durable procedures
```

This is stronger than repeated trial and error because every step should reduce uncertainty.

## 13. Capability-claim discipline

Future ADS investigations should use claim scopes such as:

```text
Observed:
    exact tested operation failed at layer X

Supported claim:
    the tested route/contract is blocked or defective at layer X

Not yet supported:
    the capability is impossible through every relevant route or contract
```

Likewise:

```text
Observed:
    fallback route Y succeeds

Supported claim:
    the required operational outcome is available through Y

Not yet supported:
    target route X is impossible or unnecessary to investigate
```

And after success:

```text
Observed:
    bounded contract X succeeds under verified preconditions

Supported claim:
    X is verified for that exact contract and authority boundary

Not yet supported:
    arbitrary neighboring operations are safe or accepted
```

This prevents both pessimistic overgeneralization and optimistic authority creep.

## 14. The empirical direct-synchronization chain

After the investigation and guarded repair, ADS proved the following chain:

```text
ChatGPT
    ->
bounded public MCP action
    ->
codex.git_pull_ff_only
    ->
Codexless
    ->
Codex App Server command/exec
    ->
ads-direct-git
    ->
network + bounded .git authority
    ->
git pull --ff-only
    ->
strict fast-forward
    ->
local ADS checkout synchronized
```

The accepted operation is fixed and fail-closed. It does not expose caller-controlled Git arguments.

The success was then repeated in a routine bounded synchronization after the experimental acceptance run. Repetition matters because it reduced the chance that the first success was an unexplained one-off condition.

## 15. What the result does and does not prove

Proven and accepted:

```text
fixed semantic git fetch origin contract
fixed semantic strict-fast-forward pull for the trusted ADS branch
model-free execution through Codex command/exec
clean-tree and branch/upstream fail-closed preconditions
bounded network + .git authority
readOnly downscope remains :read-only
postflight equality / cleanliness / ancestry verification
```

Not accepted merely because the pull succeeded:

```text
arbitrary Git commands
commit
push
force push
reset
checkout
rebase
merge commits
arbitrary refs / branches / remotes
public process execution
unrestricted host access
automatic ACL repair
```

A narrow success should stay narrow unless separately justified and verified.

## 16. Human persistence can improve scientific correctness

There was a real point where stopping the direct-lane investigation would have been operationally reasonable because a formal Codex-agent alternative already worked.

The project owner explicitly kept the original research question in focus: whether the **direct bounded model-free route itself** could work.

That insistence prevented substitution of:

```text
we have a workaround
```

for:

```text
we answered the question we actually set out to investigate
```

This is a useful human/system boundary lesson. The collaborator should surface uncertainty and safe stopping points, but the project owner may correctly identify that the unresolved question still has scientific or architectural value.

## 17. Practical future rule for ADS

When something appears impossible at a multi-layer boundary, do not automatically continue forever and do not automatically stop after the first plausible blocker.

Use this decision rule:

```text
if the failing layer is already identified and the governing contract clearly excludes the capability
    -> accept the bounded negative result

if the observed failure can still plausibly arise from several layers or contracts
    -> localize further

if authoritative/source research can distinguish those explanations at reasonable cost
    -> research before freezing architecture

if a small safe experiment can discriminate between the remaining explanations
    -> run that experiment fail-closed

if the desired outcome is achieved only by widening unrelated authority
    -> stop and redesign rather than normalize the widening
```

The goal is disciplined persistence, not persistence for its own sake.

## 18. Relationship to Source Vault continuation

This investigation was opened as a bounded prerequisite before permanent Source Vault ingestion resumed.

It did not mutate the Source Universe, original corpus, Source Registry contents, Source Vault payloads, backup payloads, or recovery state.

The Source Vault route remains governed by `docs/CURRENT_STATE.md` and `docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`.

The reusable lessons in this file should therefore be treated as Level-2 development knowledge extracted from the infrastructure investigation, not as a new Source Vault blocker.

## 19. Evidence chain

The detailed technical evidence remains in the stronger scoped records:

```text
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/local_execution/validation/013_direct_lane_git_metadata_permission_profile_source_audit.md
docs/local_execution/validation/014_direct_git_profile_runtime_application_partial.md
docs/local_execution/validation/015_direct_git_profile_active_metadata_write_denied_windows_acl_investigation.md
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md
docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md
docs/local_execution/validation/019_bounded_semantic_git_pull_ff_only_contract_frozen.md
docs/local_execution/validation/020_semantic_git_pull_ff_only_dispatched_local_fetch_head_denied.md
docs/local_execution/validation/021_semantic_git_pull_ff_only_verified_after_acl_repair.md
docs/local_execution/SEMANTIC_PULL_ACCEPTANCE.md
docs/local_execution/OPERATIONS.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
```

This synthesis exists so future collaborators do not have to reconstruct the general lessons by rereading the full experimental chronology every time.