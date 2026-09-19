# Cockpit Design Exploration Resume Target

**Status:** ACTIVE SUCCESSOR SEMANTIC TARGET / EXECUTION NOT IMPLIED
**Purpose:** Give the paused next-generation Cockpit workstream a durable semantic target for its exact preserved frontend continuation.

The preserved resume anchor is:

```text
branch   v1-cockpit-design-exploration
head     04f2a907094b8023ac7377c399a6eef1a6e1da99
workflow 33268350178
job      99142293330
gate     V3 full
browser  84 / 84 PASS
```

This target does not resume or promote the Cockpit. Resume requires the project owner to explicitly return to frontend work, then verify the exact frozen head or create an explicit continuation from it and follow the recovery route in `docs/cockpit/README.md`. Production `/cockpit` remains untouched until a separate promotion boundary is earned.

<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->
{
  "schema_version": "1",
  "profile": "semantic_source.v1",
  "kind": "RESUME_TARGET",
  "authority_class": "canonical",
  "semantic_id": "COCKPIT:DESIGN-EXPLORATION-RESUME",
  "state": "ACTIVE",
  "scope": {
    "domain": "cockpit",
    "workstream": "WS-COCKPIT-DESIGN"
  },
  "provenance": [
    "checkpoint:267",
    "research:169",
    "research:170"
  ],
  "references": [
    "path:docs/cockpit/README.md",
    "path:docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md",
    "path:docs/cockpit/PHASE_C_DECISION_LEDGER.md"
  ]
}
<!-- PKA-STRUCTURED-DECLARATION-END -->
