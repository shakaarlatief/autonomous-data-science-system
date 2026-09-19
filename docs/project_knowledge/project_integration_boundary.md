# Project Integration Boundary

**Status:** ACTIVE SUCCESSOR SEMANTIC OWNER / CURRENT CONTINUITY REMAINS OPERATIONAL AUTHORITY
**Purpose:** Own the narrow project-wide promoted integration boundary required by Candidate 01 without creating a broad project-control registry.

The Project Integration Boundary owns exactly one durable project-wide semantic unit:

```text
promoted integration branch
+
exact promoted integration commit
```

It does not own the active development branch, active pull request, current checkpoint, current workstream boundary, latest specification, experiment outcome, or any other unrelated project-control fact. Those remain with their natural owners or current compatibility surfaces until their governed migration gates are reached.

It also does not own the policy that determines when Git development branches are created, continued, rotated, merged, archived, or retired. The existence of a promoted integration boundary must therefore not be interpreted as a branch-lifecycle policy; that separate deferred architecture question is tracked by AB-032.

The current live compatibility projection remains `docs/current_routing.json`. During W1 that compatibility surface is not overwritten by successor generation and remains part of the current operational continuity architecture.

<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->
{
  "schema_version": "1",
  "profile": "project_boundary.v1",
  "kind": "PROJECT_INTEGRATION_BOUNDARY",
  "authority_class": "canonical",
  "semantic_id": "PROJECT-INTEGRATION-BOUNDARY",
  "state": "ACTIVE",
  "scope": {
    "boundary": "promoted-v1-integration"
  },
  "promoted_branch": "v1-frontend-spike",
  "promoted_commit": "2480109fadeee1e480ef03b82e335aacdf9adf91",
  "provenance": [
    "research:153",
    "research:155",
    "research:185",
    "path:docs/current_routing.json",
    "path:docs/project_knowledge/captures/historical/w4_branch_boundary_scope.json",
    "path:docs/OPEN_ARCHITECTURE_BACKLOG.md#AB-032"
  ]
}
<!-- PKA-STRUCTURED-DECLARATION-END -->
