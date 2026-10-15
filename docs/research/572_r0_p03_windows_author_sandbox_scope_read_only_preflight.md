# Research 572: R0-P03 Windows author-sandbox scope, read-only preflight

**Date:** 2026-10-15
**Status:** ELEVATED_BACKEND_REQUIRED_BY_INSTALLED_DIAGNOSTICS / EXACT_SETUP_EFFECTS_UNRESOLVED / EXECUTION_NOT_AUTHORIZED_NOT_PERFORMED
**Scope:** Establish the prospective authorization/runtime scope for one synthetic model-free enforcement trial; inspect only existing artifacts, installed help/binary metadata, runtime/configuration and official documentation.
**Basis:** Clean `v1-source-vault-bootstrap-resume` at `e0a14048f2978d88881873c13781c9f609398881`; Research 571 / Validation 260 independently accepted; Research 567–570, Validation 209, Research 513/559 and Checkpoint 898 unchanged.
**Provenance:** Exposed native Desktop Codex/codex-01 investigates; ChatGPT/chatgpt-39, **39 - Architecture Qualification and Realization Readiness**, independently reviews and accepts. No fresh author/evaluator role.
**Authority:** Metadata and prospective plan only. No sandbox/setup launch, Windows ACL/account/trust/security mutation, new credentials, inference, source/task/gold/arm/scoring fixture, private repo change or checkpoint.

## Decision

The retained profile is **not authorization-ready for execution on the normal host**. Its backend was not explicitly selected, the complete expansion of `:minimal` and helper ACL targets is unavailable, and a dedicated home does not isolate machine-global sandbox accounts or policy. Do not resolve these uncertainties by activating setup.

Installed diagnostics require **elevated** for deny-read restrictions. The prospective command therefore pins that backend; this is an explicit refinement, not evidence that the original unpinned command would automatically select it. The exact original default-selection/control flow was not established from the packaged binaries. Neither `windows=null` from the earlier App Server response nor the current Desktop command identity supplies that missing fact.

The smallest next dependency is a **version-matched read-only setup/change manifest and supported rollback procedure**, including expanded runtime/read roots and effects on existing global principals, or an owner-designated disposable isolated Windows instance with recoverable state. Generic approval to “use a sandbox” is insufficient for unknown global effects. No security-sensitive operation is requested or executed by this artifact.

## Verified installed evidence

| Inspection | Actual result and scope |
|---|---|
| Git branch/HEAD/index/worktree | Requested branch and published HEAD; clean worktree and empty index before edits |
| npm package, CLI help and executable hash | Version **0.154.0**; sandbox help describes Windows restricted-token execution and supports named profile, cwd and managed-config inclusion. Binary SHA-256 **`be96b992178b1e467c225800da0d65f2c86d5eba1ef0b14632f65db381cbdfde`**, unchanged from Research 571 |
| Retained candidate bytes | `%TEMP%/ads-p03-author-inspect-yq2mrfjg/metadata-home/config.toml`, SHA-256 **`93ba549a45cbb6d03552cd70007726efc08fd4e98d23bae01ccd88c6025aa6b0`**; original configuration unchanged |
| Static binary diagnostics | Literal `deny-read overrides require the elevated Windows sandbox backend` at byte offsets **229220697, 233024969, 233620857, 233949489, 234099481, 238988184**. This is version-bound implementation evidence, not an exercised rejection |
| Static backend/setup metadata | Internal WindowsSandboxLevel variants disabled/restricted-token/elevated; setup modes elevated/unelevated. Helper payload field names include command_cwd, read_roots, write_roots, deny_read_paths, deny_write_paths, refresh_only and real_user. Diagnostics cover user create/update, DPAPI protection, credential-state writes, firewall rule add/verify and setup failure |
| `features list` under retained home | Removed legacy feature names elevated_windows_sandbox=false and experimental_windows_sandbox=false; windows_sandbox_service=false. No prefer_mxc literal found in binary; absence alone is not proof of every unsupported feature |
| Existing sandbox accounts, metadata only | `Get-LocalUser` found CodexSandboxOffline and CodexSandboxOnline, both enabled/password-required. Only names/enabled/password-required fields retained; no password/credential values requested or exposed, and no account changed |
| Checked machine configuration | `%ProgramData%/OpenAI/Codex/config.toml` and `requirements.toml` absent. This does not exclude every possible managed/cloud requirement source |
| Packaged helpers | Inspected vendor bin contains codex.exe and codex-code-mode-host.exe; no standalone setup/command-runner helper in that directory. Binary references helper preparation and `.sandbox-bin`; helper creation/location/use remain unexercised |

Only help was run for `doctor` and `debug`; no live doctor, setup, readiness, sandbox, command/exec or thread/turn API was invoked. The retained protocol schema advertises windowsSandbox/readiness and windowsSandbox/setupStart, but a schema name does not prove readiness has no side effects. No new App Server bootstrap was needed. Initial binary-context display failed with UnicodeEncodeError in the terminal; escaped JSON display then succeeded. No host execution or enforcement test was hidden by that display failure.

The [official Windows documentation](https://learn.chatgpt.com/docs/windows/windows-sandbox) describes legacy elevated setup using lower-privilege accounts, filesystem boundaries, firewall and policy changes, whereas unelevated lacks deny-read support. Its MXC one-command guidance is explicitly for CLI 0.162.0 and later; it does not qualify installed 0.154.0. Validation 209 records successful direct legacy-mode commands on 0.154.0 in September, but not this profile or a new home. That incident also shows runtime validation can scan beyond one chosen working directory. It is historical warning/evidence, not permission to repeat its launches or runtime quarantine.

The [permissions documentation](https://learn.chatgpt.com/docs/permissions) distinguishes command permissions from model/browser/connector/client traffic. The [managed-configuration documentation](https://learn.chatgpt.com/docs/enterprise/managed-configuration) explains higher-priority requirements; two absent files do not eliminate that obligation. The installed package provides a launcher and compiled binaries, not the version-matched helper source/control-flow or an exhaustive supported dry-run manifest. Static strings identify possible effects but cannot identify every path, ACE, principal operation or rollback sequence. Stop at that visibility limit.

## Expected effects and unresolved impact scope

| Resource | Expected or possible effect of a future elevated launch | Qualification now |
|---|---|---|
| Dedicated experiment home | Config, helper aliases/caches, state/log databases, installation metadata and sandbox state. The earlier temporary home already contains SQLite/log/state files despite zero model turns; helper-alias creation there was refused | Ordinary host writes expected. A non-Temp home is proposed, not created |
| Sandbox state/helper areas | Binary names `.sandbox`, `.sandbox-bin`, `.sandbox-secrets`, setup_marker.json, setup_error.json, sandbox_users.json and deny_read_acl_state.json; helper/runner preparation, locks and status records | Names verified; exact placement, lifetime and full write set not certified. Credential state must remain private, never copied into the public repo |
| Existing global identities | CodexSandboxOffline / CodexSandboxOnline; helper diagnostics admit account creation/update and protected credential-state operations | No assurance that a fresh home only reuses accounts without modifying them. Existing Desktop/other Codex sessions may depend on these accounts |
| OS policy | Elevated setup may create/update sandbox group membership, logon rights and firewall rules | Exact rule/group/SID set and change/rollback behavior unresolved; not authorized |
| Filesystem permissions | Read/execute grants, writable-root capability permissions and deny-read/write ACL operations on resolved paths; runtime validation may traverse configured runtime trees | Exact ACE masks, recursion, parent effects, `:minimal` roots and complete target manifest unresolved. Cannot promise effects are confined to synthetic directories |
| Sources/artifacts/harness | Source/harness read, artifact writes; junction must not grant access to forbidden backing files | Desired profile, no enforcement observed |
| Host environment | Process-local CODEX_HOME/TEMP/TMP selection; no saved global settings or trusted-root registration proposed | Restorable process environment is feasible; it does not undo accounts/ACL/firewall changes |

An isolated home separates configuration and logs, **not global security state**. Therefore “without affecting normal ADS development” is not established on this machine. No blanket setup/UAC approval, password renewal, new account, firewall change or ACL grant is inferred. An unexpected privileged operation must stop the trial rather than silently broaden authorization.

## Python runtime scope

Native read-only Python metadata found standalone **Python 3.13.1** at `%LOCALAPPDATA%/Programs/Python/Python313/python.exe`, SHA-256 **`03573716a7fcbd8b7fed8fe0163bbfbd3a852546920d6a666123f307c8dac7d9`**. This is existing installed software; nothing was installed or copied.

The ADS `.venv` has `autonomous_data_science_system.pth` pointing to the public repository's src directory. Its earlier `-I -B` sys.path still included that ADS path: isolated mode alone does not suppress site processing. **Do not use that venv for the proposed closed-world child.** Standalone `-I -S -B` metadata verified isolated=1, no_site=1, dont_write_bytecode=true, with only the standalone runtime/Lib/DLLs/expected zip path and no ADS src/site-package path. This was runtime introspection, not a repeated Research 571 test or sandbox trial.

The existing executable, python313.dll, python3.dll, vcruntime140.dll and vcruntime140_1.dll are present. The metadata imports json/pathlib/hashlib/runpy loaded standard-library files and DLLs/_hashlib.pyd. Proposed read exceptions cover those Python files, DLLs and Lib, with Lib/site-packages denied. Hashlib may additionally load runtime cryptography DLL dependencies; the OS loader needs system runtime access. The exact transitive DLL/system closure and `:minimal` expansion must be reviewed before launch. Do not respond to a missing dependency by granting the whole user profile, ADS checkout, ProgramData or global Temp.

## Concrete prospective layout, configuration and command — NOT EXECUTED

Proposed root **`C:/Projects_Data/ADS-P03-SYNTHETIC-AUTHOR-PREFLIGHT-001`** was checked absent. It is outside both ADS checkouts, is not created or registered, and requires owner designation/creation authorization. Refuse an existing root; never overwrite it. A coordinator, not the restricted child, would prepare only fabricated data:

```text
<TRIAL_ROOT>/
  home/                    dedicated CODEX_HOME; no copied auth or production state
  evidence/                coordinator receipts, synthetic stdout/stderr, pre/post metadata
  world/
    harness/probe.py        reviewed bounded child; immutable to child
    sources/allowed.json    fabricated permitted input
    sources/escape/         synthetic junction to <TRIAL_ROOT>/forbidden
    artifacts/              only intended child write directory, including local tmp/
    .git/HEAD               fabricated forbidden metadata, no ADS Git
  forbidden/               fake gold/key/design/transcript canaries, no actual sensitive data
```

The junction's exact target would be `<TRIAL_ROOT>/forbidden`, not a personal or protected directory. The harness/expectations must be coordinator-owned/read-only in the proposed policy so a child cannot rewrite its own expected result. No real gold, source world or independent answers are used.

The proposed configuration is the original permission design plus an explicit backend, read-only harness and standalone Python exceptions. **It is a new prospective variant, not the exact already-parsed configuration and not newly parse/enforcement-tested.** Render `PYTHON_ROOT` from `(Join-Path $env:LOCALAPPDATA 'Programs/Python/Python313').Replace('\','/')` into literal absolute TOML keys; TOML does not expand environment variables or placeholders:

```toml
default_permissions = "p03-synthetic-author"
approval_policy = "never"
web_search = "disabled"
[windows]
sandbox = "elevated"
[features]
windows_sandbox_service = false
[permissions.p03-synthetic-author.filesystem]
":root" = "deny"
":minimal" = "read"
":tmpdir" = "deny"
":slash_tmp" = "deny"
"<PYTHON_ROOT>/python.exe" = "read"
"<PYTHON_ROOT>/python313.dll" = "read"
"<PYTHON_ROOT>/python3.dll" = "read"
"<PYTHON_ROOT>/vcruntime140.dll" = "read"
"<PYTHON_ROOT>/vcruntime140_1.dll" = "read"
"<PYTHON_ROOT>/DLLs" = "read"
"<PYTHON_ROOT>/Lib" = "read"
"<PYTHON_ROOT>/Lib/site-packages" = "deny"
[permissions.p03-synthetic-author.filesystem.":workspace_roots"]
"sources" = "read"
"harness" = "read"
"artifacts" = "write"
[permissions.p03-synthetic-author.network]
enabled = false
```

After all missing impact/rollback information and authorization are resolved, the exact proposed PowerShell invocation is below. **NOT EXECUTED; preparation/config/probe files do not exist.** Verify executable/config/script hashes and managed-policy resolution first. Do not launch from the current sandbox investigator and assume it represents the ordinary owner launcher.

```powershell
$trialRoot = 'C:\Projects_Data\ADS-P03-SYNTHETIC-AUTHOR-PREFLIGHT-001'
$experimentHome = Join-Path $trialRoot 'home'
$world = Join-Path $trialRoot 'world'
$python = Join-Path $env:LOCALAPPDATA 'Programs\Python\Python313\python.exe'
$cli = Join-Path $env:APPDATA 'npm\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\bin\codex.exe'
$savedCodexHome = $env:CODEX_HOME
try {
    $env:CODEX_HOME = $experimentHome
    & $cli sandbox --include-managed-config --permission-profile p03-synthetic-author `
        --cd $world -- $python -I -S -B (Join-Path $world 'harness\probe.py')
    $trialExit = $LASTEXITCODE
} finally {
    $env:CODEX_HOME = $savedCodexHome
}
```

Do not redirect the launcher's TEMP/TMP into child-writable artifacts: that could expose helper/setup intermediates, and a `:tmpdir` deny could also conflict with the intended scratch grant. This bounded Python child needs no global temp operation; any explicit scratch files stay under artifacts/tmp. The launcher's/helper's actual temp use remains part of the missing effect manifest. If it requires a separate protected temp or other root, that is a revised manifest/authorization, not automatic widening. Owner/coordinator captures stdout/stderr, returns sanitized statuses/hashes and keeps any security metadata private. The configuration does not promise helper secrets cannot land in child-visible storage. Model-free setup can still generate/update local sandbox-account credentials; this is distinct from provider authentication and needs explicit owner authorization if required.

Permitted child checks: exact allowed read/search, artifact create/modify, isolated subprocess executing a tiny synthetic assertion, artifact/report readback. Negative checks: existing forbidden parent/absolute gold/key/design/transcript stand-ins; fake Git path; junction traversal; source/harness writes; outside-artifact output writes. Record actual PermissionError/Windows access-denied separately from tool-policy refusal, setup failure, missing targets and unexercised checks. A successful forbidden byte read or write falsifies its boundary. A setup failure is not a denial pass. No new network service, package install, unrestricted command survey or protected-owner-canary test is required for this first bounded file/process trial.

## Authorization, failure handling and cleanup

Current authorization covers this inspection and public preservation only. The future trial requires, in order:

1. **Effect resolution:** obtain the version-matched helper's expanded path/ACE/principal/firewall/logon-right change list, helper/state/credential/temp locations, refresh conditions and supported rollback. Do not use activation as a substitute for a read-only effect manifest. If unavailable, remain stopped on the normal host.
2. **Owner decision:** designate the exact new root and launcher identity; approve only the enumerated writes/setup/security changes and recovery method. No account/password/privilege/trust changes can be implicitly approved. If existing global sandbox accounts could be modified, protect other Codex development sessions through an owner-controlled maintenance/recovery arrangement or use a separate disposable Windows instance. A new home alone is insufficient.
3. **Preparation and preflight:** coordinator creates harmless fixtures and reviewed child, records expected outcomes/hashes and existing relevant metadata/ACLs/rules without publishing secrets. Verify actual managed restrictions, backend selection, runtime closure and unchanged normal ADS settings before one launch. Any extra path or privilege requirement stops the plan.

For an approved later trial, record launcher/helper/child identities, PIDs/timestamps, resolved configuration, setup status/error and child exit independently. A zero helper exit without completed setup, missing child receipt, timeout/interruption, setup_error or unsupported policy means **SETUP/EXECUTION_UNAVAILABLE**, not successful confinement. Do not auto-retry, switch to unelevated/full-access, run as administrator or repair ACLs to get a PASS. Identify and contain only the experiment's process tree through the owner-approved controller; do not stop unrelated Desktop/bridge processes automatically.

On failure preserve the dedicated home and private logs/state until reviewed. **Do not delete sandbox state first:** it may be needed to identify/reverse ACL/principal changes. Do not read or publish sandbox_users credential contents, delete shared sandbox accounts/firewall rules, restore broad ACL trees or transplant production .sandbox state. Exact rollback is **not verified here**; on a normal host, an owner/admin must apply a version-matched recovery procedure. On a separately designated disposable instance, a verified full-instance rollback can contain global changes. Without either, do not launch.

Only after processes are stopped, approved global effects are reversed/verified and needed receipts are retained may the owner remove the exact new experiment root. Resolve its absolute path, reject reparse-point roots/parents and remove junction entries without recursively following their targets; use literal paths in one PowerShell shell. No cleanup/delete/rollback command was executed or supplied as a blind remedy. Process environment restoration does not reverse persistent security changes.

## What a later result would establish; verification of this unit

A later successful trial could establish **bounded command-level** permitted read/write/build and actual negative file/output behavior for the pinned executable/configuration/OS identity. It would not qualify a model's tool inventory, fresh inherited context, alternative Desktop/bridge/browser/MCP/connector routes, provider transcripts, gold/key custody, independent evaluators, complete reference recovery, scientific freeze or B0–B4 results. Those remain separate gates.

This unit ran Git/CLI help and feature metadata, compiled-binary string/hash inspection, specific machine-config existence/metadata checks, named sandbox-account metadata and standalone Python runtime introspection. **No Research 570/571 tests, pytest, sandbox/setup, model inference or protected-canary reads were run.** No new implementation/test infrastructure or validation number is warranted. Repository-integrity and scoped preservation checks are recorded in the final handoff. Checkpoint 898, routing, Research 513/559, twelve-primary/nine-legacy requirements, 60/20 intent, source/currentness, independent reference/evaluation and zero false-authority gates remain unchanged. No commit or push; independent ChatGPT review precedes any security-sensitive authorization.

Postflight: all **six repository-integrity components PASS**, `PUBLIC_REPOSITORY_INTEGRITY=PASS`; **14 scoped preservation checks PASS** and `git diff --check`/new-document whitespace PASS. The first scope-check script hit a local cp1252 decoding error when reading UTF-8 collaboration state; the explicit UTF-8 rerun passed. HEAD/index/routing/checkpoint, prior collaboration provenance/history and retained candidate configuration bytes are unchanged. Only this research artifact plus four continuity/navigation files changed; the prospective root is still absent. These preservation results are not sandbox tests.
