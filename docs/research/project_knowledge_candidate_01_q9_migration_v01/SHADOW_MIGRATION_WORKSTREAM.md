# Shadow Candidate 01 Semantic Source: Knowledge-Architecture Migration Workstream

**Status:** SHADOW-ONLY SUCCESSOR SOURCE / NOT CURRENT PROJECT AUTHORITY
**Purpose:** Self-host Candidate 01's own migration, rollback and future authority-switch preparation without performing the switch.

<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->
{
  "kind": "ARCHITECTURE_MIGRATION",
  "semantic_id": "PKA-C01-MIGRATION",
  "authority_class": "candidate",
  "shadow_only": true,
  "state": "ACTIVE",
  "parent": "WS-PKA-CURRENT",
  "migration_phase": "M6_SHADOW_RECONCILIATION",
  "migration_source_commit": "fe40740e62dabc41e538b2b604e84f5e9167e92d",
  "current_operational_authority": "CURRENT_CONTINUITY_ARCHITECTURE",
  "successor_authority_state": "SHADOW_ONLY",
  "qualification": {
    "final_qualified_passes": 0,
    "frozen_item_count": 67,
    "target_selection_allowed": false
  },
  "authority_switch_requested": false,
  "required_switch_conditions": [
    "FULL_REQUIREMENTS_QUALIFICATION",
    "OWNER_TARGET_ACCEPTANCE",
    "ROLLBACK_PROOF",
    "PUBLIC_REPOSITORY_INTEGRITY_PASS"
  ],
  "rollback": {
    "mode": "EXPORTER_BASED",
    "requires_lossless_legacy_compatibility": true,
    "compatibility_paths": [
      "docs/current_routing.json",
      "docs/CURRENT_STATE.md"
    ]
  },
  "next_action": "Prove semantic migration parity, reverse-reference safety, lossless legacy export, switch-precondition blocking, and self-hosted continuation without changing authority.",
  "provenance": [
    "research:144",
    "research:146",
    "research:163",
    "checkpoint:508"
  ]
}
<!-- PKA-STRUCTURED-DECLARATION-END -->
