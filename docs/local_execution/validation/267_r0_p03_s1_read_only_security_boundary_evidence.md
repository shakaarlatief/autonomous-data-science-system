# Validation 267: Read-only Windows and Codexless S1 security-boundary observations

**Date:** 2026-10-20
**Status:** READ_ONLY_PLATFORM_AND_TOOL_OBSERVATIONS_CAPTURED / WORKSPACE_REFUSAL_CONFIRMED / REAL_OS_IDENTITY_AND_CONFIDENTIALITY_UNQUALIFIED
**Scope:** Independently observable non-secret system metadata and harmless rejection probes required to distinguish purpose-specific Runtime Bridge authority from real Windows principal, ACL and private-custody enforcement.
**Basis:** Research 598–599; Validations 264–266; live registered public ADS workspace; starting public HEAD `a9a44d6d2c922b0d389c1b16573eb7e3f20542f9`.
**Authority:** Read-only observation evidence. Not an actual private reviewer actor, ACL denial, Windows principal creation, protected ledger or scientific advancement.

## A. Reproducible, scoped preflight

Read-only semantic Git checks in the registered ADS workspace:

```text
branch                v1-source-vault-bootstrap-resume
HEAD                  a9a44d6d2c922b0d389c1b16573eb7e3f20542f9
index                 clean
worktree              clean
local/upstream         0/0
```

The interactive user identity, group membership list, SID, credential values, detailed ACL principals and private workspace filesystem paths were deliberately **not included** in the tool output.

The Windows read-only PowerShell probe, under the Runtime Bridge's authorized `readOnly` command mode, returned:

```text
OS_FAMILY=Windows
TOKEN_IS_ADMIN_MEMBER=False
TOKEN_AUTH_TYPE=NTLM
PROCESS_TOKEN_PRESENT=True
LOCAL_ACCOUNT_CMD_AVAILABLE=True
ICACLS_AVAILABLE=True
CIPHER_AVAILABLE=True
PUBLIC_WORKSPACE_ACL_RULE_COUNT=8
PUBLIC_WORKSPACE_ACL_INHERITANCE_PROTECTED=False
PUBLIC_WORKSPACE_ACL_HAS_DENY=False
PUBLIC_WORKSPACE_ACL_HAS_INHERITED_RULE=True
LOCAL_WINDOWS_USERS_ENUMERABLE=True
LOCAL_WINDOWS_USERS_COUNT=7
NO_PRIVATE_ACL_OR_CREDENTIALS_READ=True
```

An initial generic assembly-type lookup reported `DPAPI_SUPPORTED=False`; that does **not** establish DPAPI is absent. A narrower follow-up loaded `System.Security` and checked the managed type explicitly:

```text
DPAPI_MANAGED_TYPE_RESOLVABLE=True
LOCAL_USER_MANAGEMENT_CMD_AVAILABLE=True
SET_ACL_CMD_AVAILABLE=True
ICACLS_PRESENT=True
DPAPI_OPERATION_NOT_RUN=True
NO_ACCOUNT_OR_ACL_MUTATION=True
```

No encryption/decryption was invoked, no new Windows principal was created, and neither `Set-Acl` nor `icacls` was used to modify permissions. `Get-Acl` only inspected the **public development root**. None of these observations prove a correct restricted reviewer store or adequate cross-provider isolation.

## B. Runtime Bridge admission observations

A read-only `codex_workspace_authority({action:"show"})` returned a valid registry object with a revision, content hash and **11 workspace entries**. Paths and admission details were not disclosed in the public receipt. This proves a configured registry exists, but not that any admitted path is private against every role or other connector.

Two harmless `codex_command_exec` requests used `readOnly` and `echo`, with **no source file read and no repository mutation**:

| Probe | Actual response | Proper interpretation |
| --- | --- | --- |
| Fictional, nonexistent absolute Windows working directory outside registered roots | `ENOENT: no such file or directory, stat ...` | Filesystem/existence rejection. **Not** proof of workspace or ACL enforcement |
| Existing `C:\Windows` working directory outside admitted project roots | `Codexless workspace registry has no admitted root covering path` | **Actual Runtime Bridge registry admission rejection**; command was not executed. **Not** Windows ACL denial |

The observed public root remained registered and accepted for ordinary read-only Git commands. This positive control is distinct from the negative out-of-registry refusal.

**Important evidence classification:** Because the refusal happened *before execution* in the Runtime Bridge registry resolution path, no permission-denied OS file operation occurred. Calling it `WINDOWS_ACL_DENIAL=PASS` would be false. Likewise, the `ENOENT` negative probe cannot be used as proof of an implemented access-control policy.

## C. Qualifying what was observed

| Target gate | Current evidence | Status |
| --- | --- | --- |
| Exact read-only Git project access and branch origin | Positive commands and synchronized HEAD | OBSERVED |
| Current process carries one Windows token | WindowsIdentity/WindowsPrincipal metadata | OBSERVED |
| A distinct reviewer OS/service identity exists and is usable | No reviewer-specific identity established | NOT_QUALIFIED |
| Tool registry refuses unrelated existing working directory | `C:\Windows` harmless request | OBSERVED_REGISTRY_DENIAL_ONLY |
| OS denies an unauthorized reviewer principal actual read/write | No distinct principals, no deliberately protected fake resource | NOT_TESTED |
| Restricted journal confidential from blind author | No restricted destination/ACL/service or actual author route | NOT_TESTED |
| Journal head/count protected from same writer as journal | No independently protected anchor deployment | NOT_TESTED |
| DPAPI runtime API is available | Managed type resolved after loading assembly | CAPABILITY_ONLY |
| Real decryption, backup/readback, service restart or credential revocation | No state-changing actions | NOT_TESTED |
| Model-provider/session prior-exposure isolation | No actual separate review actor or session | NOT_TESTED |
| Source or gold protection and scientific gates | No source inspected or scored | UNCHANGED_HOLD |

## D. Refused shortcuts and next approved boundary

- No directory was registered or trusted automatically; no workspace registry write was attempted.
- No private file, registry key, keyring secret, user SID, credential value or old W5 source content was read or published.
- No account, filesystem ACL, encrypted store, service, tunnel, CI/CD, branch workflow or release mechanism was modified in this qualification step.
- The next **actual** ACL/service-denial test must be against an owner-approved **fictional disposable** resource, with independently distinguished principals and positive/negative controls, tested through the same route proposed for real reviewers.
- The resulting confidential ledger/anchor/readback is a separate qualification; even a successful two-principal OS test does not prove that Temporary Chat or a remote model can only see the permitted actor-facing world.

The companion `experiments/r0_p03_navigation_probe/S1_FICTIONAL_SECURITY_BOUNDARY_TRIAL_CANDIDATE.md` specifies the owner authorization and cleanup boundary. It was **not executed**. The S0 V0.4 synthetic method remains prospectively unaccepted.

```text
VALIDATION_267=READ_ONLY_EVIDENCE_CAPTURED
PUBLIC_GIT_PREFLIGHT=PASS
READ_ONLY_WINDOWS_IDENTITY_METADATA=OBSERVED
EXISTING_ADS_ACL_METADATA=OBSERVED_NOT_DENIAL
WORKSPACE_REGISTRY_SHOW=11_ENTRIES
OUT_OF_REGISTRY_EXISTING_CWD=REJECTED_BEFORE_COMMAND_EXECUTION
NONEXISTENT_CWD=ENOENT_NOT_SECURITY_DENIAL
WINDOWS_ACL_TWO_PRINCIPAL_TEST=NOT_PERFORMED
SERVICE_AUTH_REVIEWER_TEST=NOT_PERFORMED
CREDENTIAL_ACL_OR_RUNTIME_MUTATIONS=ZERO
HISTORICAL_SOURCE_READS=ZERO
S1_REAL_REVIEW_AND_CUSTODY=HOLD
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
