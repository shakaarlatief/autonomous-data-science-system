# Research 588: R0-P03 owner-side fake recipient Prepare OpenSSL stderr repair

**Date:** 2026-10-18
**Status:** OWNER_PREPARE_NATIVE_PROGRESS_FAILURE_REPRODUCED_AND_PATCHED / REGRESSIONS_PASS / OWNER_RETRY_NOT_YET_OBSERVED
**Scope:** Repair one actual owner-reported Windows PowerShell 5.1 OpenSSL key-generation interruption before the first fake public recipient certificate was exported. Do not bypass the owner-only identity and protected-folder control, silently reuse a potentially partial folder, or weaken real R0-P03 reference-custody gates.
**Basis:** Research 587 at published HEAD 0a2a305d4033b95c0fdc64cbed711cbd5b88e794 and exact owner PowerShell error at script line 259 after the user executed Prepare under ordinary desktop PowerShell.
**Provenance:** Owner-reported command/error; exposed ChatGPT coordinator implemented and tested model-free corrective source changes. The actual owner Prepare retry and new certificate transfer are not yet observed.
**Authority:** Narrow repair and tests only. Research 513/559/576, Checkpoint 898, current routing and Specification 028 unchanged.

## Reproduced cause and owner-side consequences

The owner correctly invoked scripts/r0_p03_fake_public_recipient.ps1 with Action Prepare. OpenSSL emitted ordinary RSA generation progress to stderr (runs of dots, plus symbols and asterisks). The script previously invoked the native program directly with PowerShell stderr redirection and ErrorActionPreference set to Stop. Under Windows PowerShell 5.1, native stderr may be exposed as a NativeCommandError record even when the process is otherwise generating the requested key successfully. The shell terminated that script line before the subsequent exit-code check and successful public-certificate export.

This did NOT prove that OpenSSL itself exited unsuccessfully. It also did not prove a completed keypair: the owner did not receive FAKE_PUBLIC_CERT_PREPARED=PASS or a certificate path/digest. A new owner-protected LocalAppData directory was created before the failing line, and may contain a partially or completely generated disposable key/certificate. The exact generated folder is not known to or accessed by the coordinator; no deletion or ACL changes were attempted. The owner must NOT treat this partial state as successfully provisioned, and must not assume the original execution did nothing.

## Minimal correction

Replace the direct PowerShell native command invocation with a purpose-specific Invoke-FakeCertificateGeneration helper using System.Diagnostics.ProcessStartInfo:

- Exact same installed Git OpenSSL executable, fake recipient RSA-2048/certificate options, owner-protected output destination, seven-day validity and no production passwords.
- Redirect stdout and stderr through asynchronous drains without forwarding OpenSSL progress into the terminating PowerShell error pipeline.
- Bound the process to 25 seconds, terminate it if that limit is exceeded, and fail closed on a real nonzero exit code or process-start error.
- Retain existing post-generation protected-folder, owner/SYSTEM-only ACL and exported-public-certificate checks. No path, identity, security, key type, exception policy for the whole script, owner-store format, Receive/Verify semantics or real-gold controls are changed.

Tests now additionally invoke the exact helper function extracted from the script's own PowerShell AST with throwaway key/certificate paths inside ignored ADS test scratch. Success asserts real fake PEM files were generated with OpenSSL's progress output consumed, and a deliberate nonexistent destination causes a genuine nonzero exit that is rejected rather than mistaken for success. These isolated tests neither run Prepare nor create or inspect owner LocalAppData folders. An explicit regression guard rejects reintroduction of the old direct-native stderr redirection.

## Next owner operation

After source repair, automated tests and guarded Git publication, the owner may perform ONE controlled Prepare invocation from ordinary **non-elevated** Windows PowerShell, again using the published script. It generates a NEW GUID-named fake recipient directory rather than touching the uncertain old partial one. Do not choose the original unknown folder, automatically discover/move local keys, or change its ACL. Once the new run emits FAKE_PUBLIC_CERT_PREPARED=PASS, record only the fake public certificate location/digest and status; the private key and actual protected path are not inputs to the independent Temporary Chat.

The earlier incomplete owner directory is a disposable fake-only artifact and may be inventoried for planned owner cleanup separately, but cleanup is NOT part of this repair. If Prepare fails again, stop and reconcile exact error before further retries.

No genuine author output, real gold, independent model, temporary chat delivery, recipient receipt, new R0-P03 tasks, arm construction or score was produced in this repair.

**Disposition:** KEYGEN_NATIVE_STDERR_PATH_PATCHED_AND_TESTED; OWNER_PUBLIC_CERT_PREPARE_RETRY_PENDING; REAL_REFERENCE_CUSTODY_NOT_QUALIFIED; R0_P03_SCORE_NOT_RUN; CHECKPOINT_898_UNCHANGED.
