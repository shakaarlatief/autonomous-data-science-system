# Specification 020 Live Artifact Manifest

This directory preserves the exact extracted result bundle from the governed Specification 020 live run before scientific interpretation or tuning.

```text
run_id            32701999678
job_id            97355284139
artifact_id       9510887324
artifact_name     v1-blocking-calibration-82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a-1
source_sha        82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a
run_attempt       1
run_conclusion    success
artifact_zip_sha256 / GitHub digest
                  35ed6b472eac22090e563bbafee30aab1b666c00453ebcfd8cd0a832b79be678
```

Contained-file SHA256 values:

```text
23bc014200e346855682ac45f1bb97e80377915f4b68c3b990a33a4f51338a3f  RESULT.md
3b0e2460bdf8a6da8b2ab15c3c4c3e4c79d051ac459338afb4ddf4324f6015cf  reasoner_attempts.jsonl
9dee436a89536020f0e679d28e9d2294b03a0ea30754b4aa3d4e3c63e2af8810  reasoning_plan.json
d1b5be27bae21d5c8a93361a233bab4dec380de01978d08c643b5f650feb169a  result.json
```

The manifest records transport/provenance only. Scientific interpretation belongs in a separate stable result record and checkpoint.
