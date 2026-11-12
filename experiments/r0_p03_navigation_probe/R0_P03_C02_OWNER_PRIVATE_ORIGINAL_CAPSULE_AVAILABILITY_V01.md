# R0-P03 C02: owner-controlled direct-original availability and bounded independent verification handoff

**Date:** 2026-11-12
**Status:** C02_PHASE_B_LEDGER_ONLY_PRELIMINARY_COMPLETE / DIRECT_ORIGINAL_CAPSULE_CUSTODY_UNCONFIRMED / NO_NEW_SEARCH_AUTHORIZED
**Scope:** Establish whether the owner still retains earlier private exact historical original-source ZIP capsules, to avoid falsely equating ten ledger-only HOLDS with actual source-intrinsic insufficiency.
**Authority:** Research 640 / Validation 339 / Checkpoint 903 and original C01 historical export evidence. This is a new **owner-custody decision**, not a command to transfer private originals through public coordinator tools.

## Evidence already established

Actual source-free Phase B aggregate:

    BYTES=3616
    SHA256=7f7b9304507d1f44693e434b646598934567d394776e3588760e8b9241cc9a40
    STATUS=LEDGER_ONLY_PRELIMINARY
    C02_DISTINCT=8
    C02_DUPLICATE=2
    C02_UNCERTAIN=2
    C02_EVIDENCE_FEASIBILITY_HOLDS=10
    C02_DIRECT_ORIGINALS_AUTHENTICATED=0

Previously the C01 owner-side private exporter produced exact-original ZIP capsules and independent C01 adjudicator reports of 31 then six original historical source identities at the old pin `c57556a8bf993a1d327e9197acb7b7c745071cd8`. The **new C02 reviewer did not see those originals**. Private capsule retention by the owner is not established from the current Phase B receipt.

## Immediate safe owner custody check

Do not upload the private ZIP, any original source file, request JSON, case-specific path, or restricted ledger into public Git or this exposed coordination chat. In your **ordinary Windows PowerShell**, locate any previously exported `NEED_SOURCE_EXACT_ORIGINAL_BYTES_RESTRICTED.zip` files using the owner-private export output paths you previously retained. The exporter may have placed them in a profile-owned private LocalAppData directory, not Downloads. If multiple ZIPs share the same basename in different private locations, do not overwrite them or assume the first is the right one. Preserve all existing protected content and metadata unchanged.

For a located private ZIP, local-only checks can start with:

    $ZipPath = "PASTE_LOCALLY_THE_OWNER_PRIVATE_ZIP_PATH"
    $Info = Get-Item -LiteralPath $ZipPath -ErrorAction Stop
    $Digest = (Get-FileHash -LiteralPath $ZipPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "PRIVATE_SOURCE_ZIP_EXISTS=$($Info.Exists)"
    Write-Output "PRIVATE_SOURCE_ZIP_BYTES=$($Info.Length)"
    Write-Output "PRIVATE_SOURCE_ZIP_SHA256=$Digest"

The hash and length do **not** independently certify contents, archive manifest correctness or historical authority. Do not paste private filesystem paths or source-specific manifest details in this coordinating chat. A safe yes/no status about retained ZIP availability is sufficient to choose the next path.

## If actual old-pin ZIP capsules are retained

Keep the current independently qualified Phase A/B reviewer context if available. Provide any old-pin ZIP files directly in that **protected** Temporary Chat only after verifying source identity, role boundaries and no exposure to B0-B4 outputs or old scored gold. The reviewer must authenticate archive CRC, manifest roster, each original member length/SHA-256/Git blob SHA-1 and claimed pinned revision before relying on original text.

The reviewer can then perform **one finite direct-original C02 feasibility re-review** of the ten non-duplicate/uncertain needs: original historical status, source-specific authority and execution claims, genuinely missing witnesses, and revised counts per category. Never silently reword the questions, change Phase A duplicate labels, or declare any genuinely missing C01 operational witnesses to exist. The C02 evidence ceiling remains `47ed6344a9153dcf366769e95722840fbf1a8f8b`, but the older ZIPs cover only source identities from the earlier C01 historical pin and may be insufficient. Source-free outcomes and protected report are required separately. No scored source admission, gold or B0-B4 implementation follows automatically.

## If original capsules are missing

Stop claiming evidence sufficiency from the secondary C01 ledger. A **new explicit owner-scoped** choice is required before any original-source recovery: identify a finite indispensable source set, qualify its historical revision, use owner-private direct-source export, and let a separated reviewer actually inspect its bytes; **or** defer/re-scope the reference experiment prospectively. Do not route C01 private source queries through the exposed Runtime Bridge or reuse the old fixed-revision exporter against later C02 revisions. Do not restart the previous eight C01 indexed-lead fishing expedition.

## Distinct-slot deficit remains independent of source authenticity

Regardless of ZIP availability or evidence found, the two C02 duplicates leave at least two original distinct-slot vacancies (one orientation, one Project/Product). A later prospective owner-authorized supplementation/selection method is necessary if a twelve-distinct-primary fixture is retained. The two impact/evolution uncertainties are separately pending, and all primary source/answer qualification must still happen before scoring.

    PRIVATE_SOURCE_CAPSULES_RETAINED=UNKNOWN_OWNER_CHECK_REQUIRED
    PHASE_B_LEDGER_ONLY=COMPLETE
    NEW_DIRECT_ORIGINAL_REVIEW=NOT_STARTED
    NEW_INDEPENDENT_C02_QUESTION_AUTHOR=NOT_AUTHORIZED
    SCORE=NONE
