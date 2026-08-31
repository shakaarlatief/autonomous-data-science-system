# Permanent First-Corpus Prospective Comparison

**Date:** 2026-08-31  
**Status:** `ALL_MATCH / READY_FOR_REVIEWED_INGESTION`  
**Scope:** Public-safe evidence for the prospective comparison of the original VU Amsterdam Machine Learning corpus against the frozen first-corpus intake manifest before any permanent source ingestion.

## Result

The original first corpus was compared against:

```text
docs/source_universe/manifests/001_vu_machine_learning.json
```

The provider-free comparison completed successfully and reported:

```text
total manifest outcomes        20
MATCH                          20
DIFFERENT_ARTIFACT              0
MISSING_LOCAL_SOURCE            0
ADDITIONAL_LOCAL_SOURCE         0
non-MATCH outcomes              0
```

The private comparison report was written outside public Git. No source binary, exact private filesystem path, private registry content, backup payload, credential, or secret is preserved in this public record.

## Interpretation

The prospective fingerprints frozen before permanent ingestion reproduce exactly against the current original local first corpus. No mismatch normalization, alias repair, source substitution, or manifest extension is required for this intake.

The manifest's existing association-status semantics remain authoritative. A byte-level `MATCH` does not silently promote entries whose course association is recorded as `POSSIBLE` or `UNVERIFIED`; those uncertainty labels remain preserved exactly during ingestion.

The permanent Source Registry had already been migrated and verified before this comparison. Source ingestion had not started when the comparison was run.

## Next governed boundary

The reviewed first corpus may now proceed to the accepted ingestion operation using the frozen manifest and the resolved private Source Registry / Source Vault locations.

After ingestion, acceptance still requires:

```text
verify ingestion outcomes and registry counts
run working-store integrity audit
create deterministic verified local backup staging
client-side encrypt the verified backup
replicate to the separate Google Drive destination
retrieve the remote encrypted object into a fresh local recovery surface
reproduce the encrypted archive digest exactly
decrypt and restore into a clean target
run the restored integrity audit
preserve public-safe evidence
```

Course 2 remains blocked until the independent encrypted backup round trip and clean recovery proof succeed.
