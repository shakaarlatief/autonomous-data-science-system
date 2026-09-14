# Shadow Candidate 01 Semantic Source: Public / Private Continuity Boundary

**Status:** SHADOW-ONLY SUCCESSOR REPRESENTATION / NOT CURRENT PROJECT AUTHORITY
**Purpose:** Test explicit delegated private authority, non-leakage, bounded private dependency and consequence-sensitive degraded behavior against real ADS public/private continuity surfaces.

<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->
{
  "kind": "PUBLIC_PRIVATE_BOUNDARY_POLICY",
  "semantic_id": "PKA-PUBLIC-PRIVATE-CONTINUITY",
  "authority_class": "canonical",
  "shadow_only": true,
  "public_development_authority": "PUBLIC_ADS_REPOSITORY",
  "private_companion_role": "DELEGATED_PRIVATE_CONTINUITY_ONLY",
  "public_resolved_private_state": "RESOLVED_PRIVATE",
  "private_unavailable_state": "NOT_VERIFIED",
  "rules": {
    "public_only_task_private_unavailable": "ALLOW_PUBLIC_CONTINUATION_WITH_PRIVATE_NOT_VERIFIED",
    "private_required_task_private_unavailable": "BLOCK_REQUIRED_PRIVATE_UNVERIFIED",
    "private_required_task_private_anchor_fail": "BLOCK_PRIVATE_CONTINUITY_FAIL",
    "optional_retrieval_unavailable": "DEGRADED_OPTIONAL_NO_AUTHORITY_BYPASS",
    "public_projection_private_material": "REDACT_PRIVATE_ONLY_VALUES"
  }
}
<!-- PKA-STRUCTURED-DECLARATION-END -->
