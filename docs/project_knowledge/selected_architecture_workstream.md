# Project-Knowledge Architecture Workstream

**Status:** ACTIVE SUCCESSOR SEMANTIC OWNER / CURRENT CONTINUITY REMAINS OPERATIONAL AUTHORITY
**Purpose:** Own the current Candidate 01 implementation/migration workstream semantics without copying the substantive architecture-selection decision or replacing current continuity.
**Governing decision:** D-035 in `docs/DECISIONS.md`
**Governing implementation contract:** Specification 028

This source owns the durable identity, active state, scope, objective, execution anchor, current stage and provenance of the selected project-knowledge architecture implementation/migration workstream.

It does **not** own the substantive rationale selecting Candidate 01. D-035 remains the natural owner of that decision. The Project Integration Boundary, Source Vault continuation and Cockpit continuation remain in their own natural canonical owners. Current compatibility surfaces remain separate, and this workstream does not own an operational-authority switch.

W1 through W4 are accepted. W5 remains in progress. Research 208 freezes the physical/authoring V0.2 subset, Research 209 accepts C1 implementation-closure granularity, Research 212 accepts the T3 selective per-item carrier contract while retaining one declaration per carrier, and Research 214 accepts the T4 historical-navigation evidence contract. Research 217 now accepts T1 after the V0.2 65-carrier experiment and independent MC-0020 blind calibration: controlled semantic subjects, source-owned membership, optional deterministic preferred routes, polyhierarchy and strict separation from structural/resolver facets are frozen. All empirical information-architecture gates are now closed; the next step is C1/T1/T3/T4 reconciliation, production-navigation realization selection and full W5 information-architecture freeze before broader current semantic migration begins. The workstream remains active for the continuing migration program while preserving:

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
  "execution_anchor": {
    "checkpoint": 554,
    "development_branch": "v1-source-vault-bootstrap-resume",
    "pull_request": null,
    "current_boundary": "project-knowledge-empirical-gates"
  },
  "stage": {
    "stage_id": "SPECIFICATION:028",
    "stage_state": "W5_EMPIRICAL_INFORMATION_ARCHITECTURE_GATES"
  },
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
