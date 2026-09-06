# Validation 088: Private Integrity Enumeration Candidate and Publication Preflight Qualified

**Date:** 2026-09-06
**Status:** PASS / AB-020 CANDIDATE QUALIFIED / GUARDED PUBLICATION NEXT
**Scope:** Qualify the bounded correction for the private-runtime semantic-Git integrity enumeration edge before adding new Office-file implementation paths, and clean superseded untracked qualification residue from both repositories without losing durable evidence.

## Source-control cleanup

The user-visible Source Control residue was inspected rather than bulk-committed. Every listed item in the public repository was protected `.tmp` qualification output from already-preserved PDF/Astra experiments. Every listed item in the local-runtime repository was protected `.tmp` staging/publication output from already-completed hybrid-PDF publication work.

Those superseded temporary artifacts were removed. No tracked repository file, user source file, credential, source-vault artifact or accepted implementation evidence was deleted. After cleanup:

```text
public tracked changes    0
public untracked changes  0
private tracked changes   0 before AB-020 candidate work
private untracked changes 0 before AB-020 candidate work
```

The durable experiment and publication evidence remains in public checkpoints/validations and private reviewed candidate history, so collaborators without local-machine access do not depend on temporary staging directories.

## AB-020 failure mechanism

The private `runtime-private-bootstrap` integrity policy previously called:

```text
git ls-files --cached -z
```

through the same generic `command/exec` output channel used for normal bounded commands. The repository currently has 411 tracked paths whose NUL-delimited enumeration is 32,753 bytes, only 15 bytes below the generic 32 KiB capture ceiling. Checkpoint 323 had already reproduced the failure at 412 paths / 32,841 bytes.

The defect is therefore an integrity-transport coupling, not a Git limitation and not a reason to weaken the secret/binary/content gates.

## Candidate correction

The qualified candidate keeps the public semantic-Git contract unchanged and replaces only the private bootstrap enumeration implementation. The policy now launches one server-owned read-only Node scanner through the already-authorized command sandbox. That scanner internally performs the complete `git ls-files --cached -z` enumeration with its own explicit 4 MiB bounded buffer, inspects every tracked path/content entry inside the same read-only process, and returns only a compact JSON receipt to Codexless.

The scanner preserves the existing policy checks:

```text
obvious secret-bearing path rejection
workspace containment
regular-file / symlink rejection
real-path containment
2 MiB per-file inspection ceiling
50 MiB aggregate tracked-content ceiling
binary/NUL rejection
obvious secret-like content rejection
```

It adds explicit bounds of 4 MiB for tracked-path enumeration and 20,000 tracked files. Scanner failure, malformed JSON, or result truncation fails closed as `RUNTIME_BOOTSTRAP_INTEGRITY_UNCERTAIN`. The generic 32 KiB `command/exec` envelope is not widened.

## Private preservation

The candidate and its focused regression were preserved and pushed in the private runtime repository at:

```text
7e70bd05e4da76ff1ad260b2b1cbdc5c1d65a3fb
```

The private semantic push itself still passed under the old live integrity code because no new tracked path had yet been added:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

Qualified candidate hashes:

```text
semantic-git.mjs
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02

flexible-authority-regression.mjs
c863608e93a1f57bcd767353c255c2ccdc7412b2807f738079cbd004bd68a3a5
```

## Regression evidence

The focused candidate suite passes 8/8. A new regression creates a tracked-path set whose direct NUL-delimited `git ls-files` output exceeds 32,768 bytes, then proves the policy still returns `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS` while the outer semantic-Git call receives only the compact scanner receipt.

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
```

## Guarded publication preflight

A protected `.tmp` publication helper was prepared with exact old/new hashes, private candidate HEAD binding, running preview.16 / 60-tool health checks, atomic backup/rollback behavior and no restart. Its no-publish preflight passed:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=60
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=60
PUBLIC_SURFACE_REGISTRATION=PASS tools=60
AB020_PRIVATE_INTEGRITY_PUBLICATION_PREFLIGHT=PASS
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
STAGED_PUBLIC_REGRESSIONS=PASS scripts=3
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
```

Live baseline and candidate hashes are bound exactly:

```text
live semantic-git before
f9b65e6245beb903afe9805eb9091dced907cac5bc49fcb9e41ec299cafec96f

candidate semantic-git
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

## Result

```text
SOURCE_CONTROL_TMP_CLEANUP                PASS
AB020_BOUNDED_SCANNER_CANDIDATE           PASS
OLD_32KIB_FAILURE_REPRODUCTION_COVERED    PASS
GENERIC_COMMAND_OUTPUT_CAP_UNCHANGED      PASS
PRIVATE_CANDIDATE_PRESERVED_AND_PUSHED    PASS
GUARDED_PUBLICATION_PREFLIGHT             PASS
LIVE_INSTALLATION_MODIFIED                NO
RESTART_PERFORMED                         NO
NEXT                                      HOST PUBLICATION + CONTROLLED RESTART
```
