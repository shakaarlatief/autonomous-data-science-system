# R0-P02 Attempt 002 deterministic-core result

**Status:** RESULT OBSERVED / CANDIDATE FROZEN / DETERMINISTIC CORE PASS
**Candidate commit:** `83f9fad87e910b75299a3f478cf2b294d9d4ff7a`
**Scorer:** frozen `experiments/r0_p02_authority_admission_v01/score.py`
**Oracle:** frozen `experiments/r0_p02_authority_admission_v01/oracle.json`

## Execution integrity

The Attempt 002 candidate was independently reviewed, committed alone, pushed, and repository integrity passed before scoring.

The scorer was then executed exactly once for Attempt 002 with:

```text
python experiments/r0_p02_authority_admission_v01/score.py
```

Observed process exit code:

```text
0
```

## Observed scorer output

```json
{
  "case_count": 20,
  "deterministic_core": "PASS",
  "error_count": 0,
  "errors": [],
  "metamorphic_checks": 2,
  "protocol": "R0-P02-V01",
  "schema_version": 1
}
```

This artifact preserves the observed deterministic-core result only. It does not itself classify the full R0-P02 probe, select a physical architecture, or claim completion of the Research 514 live-host leg.
