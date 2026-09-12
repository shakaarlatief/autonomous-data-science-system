# Validation 206: Semantic Git Managed Python Integrity and Public Publication Restored

**Date:** 2026-09-12
**Status:** PASS / PREVIEW.45 ACTIVE / BOUNDED PUBLIC PUSH RESTORED
**Research:** Research 124 operational support

## 1. Trigger

Research 124 Phase A was preserved locally, but `codex.git_push_ff_only` failed closed before publication even though the repository-owned aggregate integrity gate passed in the managed project environment.

The failure was isolated to interpreter selection inside the `ads-public` semantic-Git integrity policy:

```text
semantic push integrity gate
    -> invoked bare `python`
    -> host resolved Python 3.11
    -> repository requires Python >= 3.12
    -> global interpreter lacked `jsonschema`
    -> GIT_PUSH_FF_ONLY_INTEGRITY_FAILED
```

The same gate passed through the repository-managed interpreter at `.venv/Scripts/python.exe`. No raw `git push`, force push, integrity bypass, or weakened gate was used.

## 2. Repair design

The `ads-public` integrity policy now selects the repository-managed Python interpreter deterministically:

```text
Windows   .venv/Scripts/python.exe
POSIX     .venv/bin/python
```

The policy no longer falls back to a host-global bare `python`. If the managed environment is unavailable or invalid, the bounded push remains fail-closed.

A focused regression was added to assert that the integrity command uses the managed interpreter and never the bare global executable.

## 3. First release attempt and automatic recovery

The first release bundle, `semantic-git-managed-python-integrity-v1`, correctly contained the semantic-Git implementation change and focused regression. Its publication succeeded and preactivation verification reported zero file mismatches.

Activation then failed with:

```text
RUNTIME_REPLACEMENT_CONTRACT_MISMATCH
```

The one-shot supervisor automatically attempted recovery and reported:

```text
recoveryAttempted   true
recoverySucceeded   true
```

Read-only health confirmed the previous preview.44 runtime was restored.

The cause was a release-contract mismatch: the bundle declared a new preview.45 target version but did not replace `src/surface-contracts.mjs`, so the replacement runtime still advertised the previous preview.44 version. No partial failed runtime remained active.

## 4. Corrected immutable release

The corrected bundle is:

```text
releaseId          semantic-git-managed-python-integrity-v2
private source head 60bc19b9a9bbd32c5dff38f8be0dcd8be2b23a16
manifest SHA256    884e44715d8e028ee8149f7b868159839c89ca9d27811d93e092425f242145e8
target version     0.1.1-preview.45-semantic-git-managed-python-integrity
target surface     codexless-public-preview-v2
target tool count  172
files              3
```

The three replaced files are:

```text
src/semantic-git.mjs
src/surface-contracts.mjs
test/flexible-authority-regression.mjs
```

The private local-runtime source commit was published through its own bounded semantic push with:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

## 5. Publication and activation qualification

The v2 runtime release completed:

```text
prepare             prepared
publish             succeeded
preactivation verify verified / mismatchCount=0
restart activation  succeeded
postactivation verify verified / mismatchCount=0
```

Live health then reported:

```text
version        0.1.1-preview.45-semantic-git-managed-python-integrity
surfaceVersion codexless-public-preview-v2
toolCount      172
ok             true
```

The tool surface count therefore remained unchanged. This release repairs execution binding rather than widening caller authority.

## 6. Public ADS publication proof

After preview.45 activated, the previously blocked public semantic push was retried through the normal bounded tool exactly once at public HEAD:

```text
1504c1fc6fe23129c6e04f834030532d25f19e43
```

Runtime Bridge refreshed `origin`, proved the upstream was an ancestor, executed the repository integrity gate through the managed interpreter, and returned:

```text
integrity                 PUBLIC_REPOSITORY_INTEGRITY=PASS
hostProcess               true
retried                   false
postflightOk              true
remoteTrackingHeadBefore  15e27e87714dcb1875e2c2dcae1414a59f9cda33
remoteTrackingHeadAfter   1504c1fc6fe23129c6e04f834030532d25f19e43
headAfter                 1504c1fc6fe23129c6e04f834030532d25f19e43
```

Thus the Research 124 opening and Phase A commits were published without bypassing the safety gate.

## 7. Disposition

```text
VALIDATION206=PASS
RUNTIME_VERSION=0.1.1-preview.45-semantic-git-managed-python-integrity
SEMANTIC_GIT_ADS_PUBLIC_INTERPRETER=REPOSITORY_MANAGED
BARE_GLOBAL_PYTHON_FALLBACK=false
V1_ACTIVATION=FAILED_CONTRACT_MISMATCH_AUTO_RECOVERED
V2_ACTIVATION=PASS
POSTACTIVATION_MISMATCHES=0
PUBLIC_SEMANTIC_PUSH=RESTORED
PUBLIC_REPOSITORY_INTEGRITY=PASS
PUSH_RETRIES=0
RAW_PUSH_BYPASS=false
```