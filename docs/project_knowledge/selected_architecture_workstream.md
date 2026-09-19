# Project-Knowledge Architecture Workstream

**Status:** ACTIVE SUCCESSOR SEMANTIC OWNER / CURRENT CONTINUITY REMAINS OPERATIONAL AUTHORITY
**Purpose:** Own the current Candidate 01 implementation/migration workstream semantics without copying the substantive architecture-selection decision or replacing current continuity.
**Governing decision:** D-035 in `docs/DECISIONS.md`
**Governing implementation contract:** Specification 028

This source owns the durable identity, active state, scope, objective and provenance of the selected project-knowledge architecture implementation/migration workstream.

It does **not** own the substantive rationale selecting Candidate 01. D-035 remains the natural owner of that decision. It also does not yet own the Project Integration Boundary, Source Vault continuation, Cockpit continuation, current compatibility surfaces, or an operational-authority switch.

W1 begins by introducing this bounded live semantic owner while preserving:

```text
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```

<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->
{
  "schema_version": "1",
  "profile": "workstream.v1",
  "kind": "PROJECT_KNOWLEDGE_ARCHITECTURE_WORKSTREAM",
  "authority_class": "canonical",
  "semantic_id": "WS-PKA-CURRENT",
  "state": "ACTIVE",
  "scope": {
    "architecture": "PKA-CANDIDATE-01",
    "program": "project-knowledge-architecture"
  },
  "objective": "Implement and migrate the selected Candidate 01 project-development knowledge architecture under Specification 028 while current continuity remains operational authority until an explicit qualified switch.",
  "provenance": [
    "path:docs/DECISIONS.md#D-035",
    "research:176",
    "research:177",
    "specification:028",
    "checkpoint:542"
  ],
  "references": [
    "path:docs/project_knowledge/architecture/README.md"
  ]
}
<!-- PKA-STRUCTURED-DECLARATION-END -->
