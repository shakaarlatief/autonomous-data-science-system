# MC-0017 Resolution: W0 Production Implementation Architecture Co-Design

**Thread:** MC-0017
**Status:** RESOLVED
**Date resolved:** 2026-09-15
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing contract:** Specification 028
**Result:** RECONCILED W0 IMPLEMENTATION ARCHITECTURE ACCEPTED / NO SPECIFICATION AMENDMENT / W0 IMPLEMENTATION NEXT

## Resolution

ChatGPT and Claude independently designed the production W0 implementation layer from the same pre-design substantive base before entering comparative review. The designs converged strongly and the comparison produced several material corrections and simplifications without reopening Candidate 01.

Accepted final direction includes:

```text
shallow layered tools/project_knowledge package with enforced dependency direction
immutable typed semantic/domain model with selective identity
no automatic semantic-ID minting
explicit complete-property-set JSON Schemas with strict unknown-property rejection
strict deterministic Markdown declaration parsing
COMMIT_SNAPSHOT and structurally non-authoritative WORKTREE_SNAPSHOT discovery modes
governed-source-only persistent source catalog plus bounded discovery diagnostics
named exact-match scope facets with resolution-level discrimination testing
deterministic authority closure with no retrieval-ranked disposition
flattened current identity lookup over authoritative transition history
workstream active-ready sets with no arbitrary lexical/file-order route priority
single full/incremental view-builder architecture with complete inputs per affected view
explicit generator implementation digest basis and framing
deterministic task-shaped reconstruction after explicit TaskIntent
PKA-W0-J1 activation/history regression with no new topology registry
capture scanner structurally separate from authority resolution
explicit semantic-unit disposition/provenance for promotion planning
layered public/private non-leakage validation without false proof claims
stable structured diagnostic vocabulary
read-only/staged-write CLI safety boundary
embedded Mermaid as canonical W0 architecture-diagram source
strengthened W0 regressions while preserving PKA-G001 through PKA-G017
```

Claude's comparative Message 003 recommended no further design round. ChatGPT accepted the remaining sharpenings in Message 004 and froze the integrated implementation design in Research 179.

No evidence requires a logical architecture reopen or H3/Object-Primary reopen. Specification 028 remains unchanged. W0 implementation may now begin, but existing continuity remains the only operational authority and W1 canonical migration remains blocked until W0 acceptance.

```text
MC0017=RESOLVED
RESEARCH179=ACCEPTED_W0_IMPLEMENTATION_ARCHITECTURE
LOGICAL_ARCHITECTURE_REOPEN_REQUIRED=false
H3_REOPEN_TRIGGERED=false
SPECIFICATION_028_AMENDMENT_REQUIRED_BEFORE_W0=false
FURTHER_CLAUDE_DESIGN_ROUND_REQUIRED=false
W0_IMPLEMENTATION=NEXT
W1_MIGRATION=BLOCKED_UNTIL_W0_ACCEPTANCE
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
```
