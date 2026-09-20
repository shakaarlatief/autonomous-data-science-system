# W5 T4: Historical Navigation Preservation Experiment

**Status:** Frozen non-authoritative research fixture before execution
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Authority:** Research fixture only. The live Knowledge Map remains operationally available and unchanged.

## Purpose

T4 tests what minimum evidence must survive when the legacy `docs/KNOWLEDGE_MAP.md` eventually stops being the live navigation surface.

The experiment compares the full legacy Markdown routing structure with a compact evidence candidate containing only:

```text
subject topic ID
human label
short 'Use for' description
explicit artifact paths
compact checkpoint-number ranges -> subjects
specialized domain index paths
exact source boundary + source SHA-256
```

The candidate is evidence, not substantive project authority and not a claim of future rebuildability after the legacy input retires.

## Cold-navigation test

`evaluate.py` first verifies exact parity against the frozen source-boundary Knowledge Map. It then answers frozen subject and checkpoint queries from the compact evidence only, simulating the live Knowledge Map being withheld.

A flat artifact-path inventory is also characterized. It contains paths but no deterministic subject membership or checkpoint-topic ranges, so it cannot preserve the same historical routing contract.

## Output

Run:

```powershell
.\.venv\Scripts\python.exe -m experiments.project_knowledge_historical_navigation_t4.evaluate
```

to materialize non-authoritative `result.json` and `RESULT.md`.
