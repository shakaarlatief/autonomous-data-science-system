# Validation 140: GitHub G0 Windows Keyring Host Round Trip Qualified

**Date:** 2026-09-08
**Status:** PASS / WINDOWS CREDENTIAL MANAGER ROUND TRIP QUALIFIED / SYNTHETIC SECRET CLEANED
**Research:** Research 123
**Scope:** Qualify the exact `@napi-rs/keyring@2.0.0` Windows adapter against the normal user-session Credential Manager after the ordinary command sandbox proved unable to write because its token had no credential-set logon session.

## 1. Qualification boundary

The package had already been staged locally and imported successfully under Node on Windows x64. Constructor/API compatibility was confirmed for `Entry`, `getPassword`, `setPassword`, and `deletePassword`.

A sandboxed write then failed with Windows `ERROR_NO_SUCH_LOGON_SESSION`. That localized the remaining uncertainty to execution context rather than package loading or candidate API shape. One explicitly approved bounded normal-user-session execution was therefore used for the final host check.

The host check was not allowed to edit repository files, contact GitHub, inspect existing credentials, use a real GitHub token, print the synthetic secret, broaden unrelated authority, or skip cleanup verification.

## 2. Exact synthetic lifecycle

The process loaded the exact staged package, generated a cryptographically random account named with the `github-g0-synthetic-*` prefix under service `Codexless Runtime Bridge`, generated a random in-memory secret, and performed:

```text
set
-> read
-> compare in memory
-> delete in finally
-> verify absent
```

Terminal result:

```text
set                 true
readMatch           true
delete              true
absentAfterDelete   true
cleanupAttempted    true
```

The synthetic secret was never printed or persisted in project files. The credential entry was deleted and absence was verified before termination.

## 3. Interpretation

This closes the concrete Windows protected-store runtime discriminator from Checkpoint 382.

The G0 candidate now has evidence at all three relevant levels:

```text
candidate API/design regression              PASS 12 / 12
exact package import/API on Windows x64       PASS
normal user-session OS credential round trip  PASS
```

The earlier `ERROR_NO_SUCH_LOGON_SESSION` is retained as sandbox execution-context evidence, not as a keyring incompatibility.

## 4. Cleanup

The local staging-only package tree and npm cache were removed after the successful host qualification:

```text
.ads-private/codexless/github-g0-candidate/node_modules  removed
.tmp/npm-cache                                           removed
```

No generated package/binary material is preserved in Git.

## 5. Current boundary

The protected-token-store design is now implementation-qualified for the current Windows machine. The next step is to integrate the G0 modules into a main Codexless runtime candidate with the exact dependency/install packaging contract and regression coverage, still without live GitHub authorization or public `github.*` actions.

```text
VALIDATION140=PASS
NAPI_KEYRING_VERSION=2.0.0
WINDOWS_KEYRING_IMPORT=PASS
WINDOWS_CREDENTIAL_MANAGER_SET=PASS
WINDOWS_CREDENTIAL_MANAGER_READ_MATCH=PASS
WINDOWS_CREDENTIAL_MANAGER_DELETE=PASS
WINDOWS_CREDENTIAL_MANAGER_ABSENT_AFTER_DELETE=PASS
SYNTHETIC_SECRET_PRINTED=NO
LIVE_GITHUB_CREDENTIAL_USED=NO
GITHUB_NETWORK_CALL=NO
STAGING_SCRATCH_CLEANED=YES
NEXT=INTEGRATE_G0_INTO_MAIN_CODEXLESS_RUNTIME_CANDIDATE
```
