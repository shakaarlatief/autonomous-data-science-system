# R0-P02 Candidate Implementation Contract

Status: FROZEN INPUT CONTRACT / NO RESULT

Implement exactly one file later:

    experiments/r0_p02_authority_admission_v01/candidate.py

The candidate must expose:

    evaluate_fixture(fixture: dict) -> dict

Constraints:

- Python standard library only.
- Deterministic.
- No repository/file reads inside evaluate_fixture.
- No file writes inside evaluate_fixture.
- No network.
- No model calls.
- No Git subprocesses.
- Do not inspect oracle.json while authoring candidate.py.
- Do not hard-code case_id -> expected outcome mappings.
- The fixture's TEST_HMAC_SHA256 profile is synthetic probe machinery only and must not be represented as production owner cryptography.
- PROBE_JSON_V01_SORTED_KEYS_COMPACT_UTF8_TEST_ONLY is test canonicalization only. It does not select the production canonicalization standard.

Required output shape:

    {
      "schema_version": 1,
      "protocol": "R0-P02-V01",
      "cases": [
        {
          "case_id": "...",
          "outcome": "...",
          "latestness": "...",
          "semantic_state_digest": "<64 lowercase hex or null>",
          "chain_head_digest": "<64 lowercase hex or null>"
        }
      ]
    }

Cases must appear in fixture order.

Outcome semantics must be computed from the fixture's operation kind and state transitions, not from the case identifier.

The implementation should contain reusable internal primitives for:

- compact sorted-key UTF-8 probe canonicalization;
- SHA-256 digesting;
- synthetic HMAC statement signing/verification;
- semantic-base digest over declared dependencies only;
- signed-statement project/acceptance/decision binding;
- ledger-entry chaining and sequence verification;
- duplicate acceptance detection;
- semantic admission/conflict behavior;
- checkpoint/witness verification;
- interruption recovery classification.

The candidate is architecture-probe code only. It is not production implementation.
