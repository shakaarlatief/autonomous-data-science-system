# Validation 298: Wave0 owner-only comparison launcher import failure and bounded repair

**Date:** 2026-11-02
**Status:** OWNER_REPORTED_IMPORT_FAILURE_TWICE / FIXED_PYTHON_MODULE_LAUNCHER_FOCUSED_TESTED / REAL_COMPARISON_STILL_UNEXECUTED
**Scope:** Repair only the Python entrypoint problem observed in the first two owner-local attempts to create the Wave0 protected comparison, without touching existing first reviewer/challenger ciphertext, saved owner key, source archive, private findings, existing science gates or owner approval.
**Research:** 620 and 617–619.
**Specification:** 028 unchanged.
**Provenance:** Owner pasted actual interactive local Windows PowerShell output from two `-Action Compare` attempts of `scripts/r0_p03_s1_owner_wave0_private_compare.ps1` using the existing owner recipient ID. The actual ID was printed in the owner's message but is deliberately **not reprinted or preserved** here because the research state needs only the opaque existing-ID continuity, not its literal bytes.

## 1. Observed error, scope and why the input was not the cause

Both user attempts displayed the same traceback:

```text
File "C:\Projects_Data\autonomous-data-science-system\experiments\r0_p03_navigation_probe\s1_wave0_owner_private_compare.py", line 26
    from experiments.r0_p03_navigation_probe import ...
ModuleNotFoundError: No module named 'experiments'
S1_WAVE0_OWNER_PRIVATE_COMPARISON_HOLD=OWNER_PRIVATE_COMPARISON_OPERATION_FAILED
```

This occurs **before** the Python module's `cli()`, any private-key passphrase prompt, report decryption, source-status comparison or creation of the encrypted dossier. Root cause: PowerShell invoked `& $Python <absolute nested .py file> --action Compare ...`, causing Python to include the nested script folder rather than the repository root as the package-import search root. The resulting `ModuleNotFoundError` has nothing to do with the recipient ID or decryption credentials. This failure **does not demonstrate corruption, exposure or invalidity** of either previously authenticated reviewer/challenger CMS.

The import fails before any Python output write. Therefore the two reported invocations **could not have created** the new comparison CMS through this module. Nevertheless a separate, earlier owner-local output cannot be categorically ruled out without a local file-existence check; never blindly overwrite or repeat an already created dossier. No owner-private folder was inspected by the exposed coordinator.

## 2. Exact code repairs

Changed **only** the owner comparison launcher and its invented-only tests:

1. Added `$Module="experiments.r0_p03_navigation_probe.s1_wave0_owner_private_compare"` to `scripts/r0_p03_s1_owner_wave0_private_compare.ps1`. Retained the existing full path `$Tool` only for a local existence prerequisite.
2. Changed the actual execution argument array from a direct absolute Python script file path to `-B -m $Module`, invoking Python package-module resolution.
3. Wrapped the child process in `Push-Location -LiteralPath $Repo` / `Pop-Location` under nested `try/finally` to ensure that repository root is the active import base **and** the calling terminal's original current directory is restored.
4. Strengthened `SelfTest` to execute `python -B -m $Module --help` with repository-root working directory, without any owner protected report, key, passphrase or recipient. This fails closed with `OWNER_COMPARISON_MODULE_LAUNCH_FAILED` if the entrypoint or dependency imports fail.
5. Added a regression in `tests/unit/test_r0_p03_s1_wave0_owner_private_compare.py` that confirms the PowerShell invocation uses `-m` and root location, executes the exact module with `--help`, verifies the CLI options and requires the proactive `SelfTest` import check.

**No change:** The comparison Python algorithm, owner certificate/private key, cached first/second reports, exact source ZIP, proposal status, comparison report schema, original source files, answer/gold, branches, CI/CD and B0–B4 arms are unchanged.

## 3. Verification and remaining execution

Initial corrected focused run reported **6/6 pytest PASS in 5.02 seconds**, including the newly added module-launch regression and five prior fictional cryptographic/comparison tests. This establishes import-resolution correctness at the Python level and preserved synthetic protected-output behavior.

The first two attempted PowerShell AST syntax checks from the exposed Runtime Bridge timed out without any parser result. They are not evidence of failure or PASS. A later direct read-only attempt to execute the new `-Action SelfTest` through that bridge returned the host's PowerShell execution-policy security error **before loading the script**. No policy bypass was attempted and no owner-private report or key was accessed. The new owner-side `SelfTest` remains the required consequential **local owner-interactive** launcher check before any actual private comparison; do not certify owner execution until the owner supplies its markers. Prior to committing, also record actual repo integrity, diff and guarded publication checks separately.

## 4. Safe owner resumption

1. After verified publication, the owner runs the new `-Action SelfTest` in ordinary interactive PowerShell and expects `S1_WAVE0_OWNER_PRIVATE_COMPARISON_MODULE_LAUNCH=PASS` and `S1_WAVE0_OWNER_PRIVATE_COMPARISON_PREFLIGHT=PASS`.
2. Check **only in the owner terminal** whether the exact existing protected folder already contains `R0_P03_S1_WAVE0_OWNER_PRIVATE_COMPARISON.cms`. Do **not** share owner directory paths or private file content in the exposed coordinator. If it exists, HOLD and reconcile; do not rerun `Compare`. The two just reported import failures alone should not have created it.
3. If absent and `SelfTest` passes, rerun `Compare -RecipientId <existing original recipient ID>`, enter existing encrypted-key passphrase locally, then independently `Verify -RecipientId <same original ID>` only after Compare PASS. Return only safe status markers, no private paired findings.

No source/status admission or genuine targeted adversarial challenge is implied by this code repair.

```text
VALIDATION_298=REAL_OWNER_COMPARISON_IMPORT_FAILURE_REPAIRED_IN_PUBLIC_CODE
ROOT_CAUSE=ABSOLUTE_SCRIPT_EXECUTION_LOST_REPOSITORY_PACKAGE_IMPORT_ROOT
CORRECTION=PYTHON_MINUS_M_FROM_REPOSITORY_ROOT
SELFTEST_ACTUAL_IMPORT_PROBE=IMPLEMENTED
FOCUSED_FICTIONAL_TESTS=6_OF_6_PASS
OWNER_PRIVATE_COMPARISON_REAL_RUN=NOT_YET_COMPLETED
OWNER_COMPARE_FAILED_ATTEMPTS=2_BEFORE_PYTHON_CLI
OWNER_KEYS_AND_PROTECTED_REPORTS=NOT_READ_BY_EXPOSED_COORDINATOR
ACTUAL_ADVERSARIAL_CHALLENGE=PENDING
SOURCE_ADMISSIONS=ZERO
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
