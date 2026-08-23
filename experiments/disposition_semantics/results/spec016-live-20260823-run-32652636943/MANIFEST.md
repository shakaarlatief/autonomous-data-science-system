# Specification 016 Live Result Manifest

**GitHub Actions run:** `32652636943`  
**Run attempt:** `1`  
**Artifact ID:** `9496624273`  
**Artifact name:** `v1-disposition-semantics-7db27fd35151c10cdb3562cdf4410fb8f4b09e8b-1`  
**Artifact ZIP SHA-256:** `edbdb797b433ee93d0c7e353cf7b214c93d004794ebdc58487e54fcace056660`  
**Frozen source head:** `7db27fd35151c10cdb3562cdf4410fb8f4b09e8b`  
**Source branch:** `v1-disposition-semantics-diagnostic`

## Frozen source identities

```text
Specification 016 Git blob
    a358d109d069b8499f99a96539f8642ab159b093

disposition_semantics_v1.json Git blob
    f159d418056721df0ab4823d068b862590bfbeb8

reasoning plan SHA-256
    a597b5d99970e4da23e66b19a7c3dab1a5d69d41ee2f9ed388ee60c8e40ef6bb
```

The Git blob identifiers above are immutable content digests for the exact specification and fixture checked out at the frozen source head.

## Downloaded artifact verification

The downloaded ZIP digest exactly matched the digest reported by GitHub Actions artifact metadata and by the upload step in workflow run `32652636943`.

Extracted-file SHA-256 values:

```text
RESULT.md
    02077d879f8bad9d6020006e0c1438419b06aec36117f0acbffdafed23cbac3d

reasoning_plan.json
    234675b066883ee51245fb2be65929c137bd8d6ebe508d4c6b285f7118b6c50e

reasoner_attempts.jsonl
    939e791846b9a2b590fbc345ac2c35a667fe88dcd56d72b589382362a2be1c09

result.json
    a16458ec83791a3a3b568121ce5757edc9143e7d3342cf51d65898677f272035
```

## Preservation layout

`artifact.zip` is the exact complete downloaded GitHub Actions artifact and remains the authoritative raw bundle. `RESULT.md` and `result.json` are duplicated outside the ZIP for direct inspection. The ZIP contains the complete frozen randomized plan and all 36 raw provider attempt records.

No prompt, fixture truth, threshold, model setting, repetition count, retry rule, or expected disposition was changed between the frozen pre-live head and this preserved result.
