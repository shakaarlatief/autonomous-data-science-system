# MC-0008 Resolution: Governed-Repository Metadata and Reference Integrity Architecture

**Date:** 2026-08-31  
**Status:** RESOLVED / ARCHITECTURE ACCEPTED FOR NORMAL ADS GOVERNANCE  
**Thread:** MC-0008  
**Review mode:** `INDEPENDENT_THEN_COMPARATIVE`  
**Frozen independent evidence target:** `7794951cbedd16f2fd1a27170946aa59b952e27a`  
**Claude independent proposal:** `messages/001_claude_independent_governed_document_integrity_proposal.md`, commit `dbb3336f1b33e2409b3b4d96aba2d862573a154e`  
**ChatGPT candidate:** `messages/002_chatgpt_task_owner_disposition_and_candidate_integrity_architecture.md`, commit `11a4520adaf83491f4e2063449ba9b4cbf631c2c`  
**Claude comparative review:** `messages/003_claude_comparative_governed_document_integrity_review.md`, commit `acb0f80932441cacd324cbda1b29b8a530f73743`  
**Final reconciliation:** `messages/004_chatgpt_final_reconciliation_and_accepted_integrity_architecture.md`

## 1. Collaboration result

MC-0008 completed the intended independent-then-comparative process without target-state implementation during review.

Claude's independent proposal was preserved before the ChatGPT candidate existed. ChatGPT then froze a separate task-owner candidate. Claude compared that candidate against its preserved independent position and returned `SUPPORT_WITH_5_BOUNDED_AMENDMENTS`.

All five comparative amendments are accepted in Message 004:

```text
MF1  full metadata inventory before exact schemas       ACCEPTED / COMPLETED
MF2  branch-scoped freshness                            ACCEPTED
MF3  explicit validator unit-test matrix                ACCEPTED
MF4  preventive-hardening framing                       ACCEPTED
MF5  public/private integrity claim separation          ACCEPTED
```

## 2. Evidence-driven metadata conclusion

The deterministic inventory confirmed substantial family variation across 24 Foundations, 24 Specifications, 105 Research records, 15 validation/evidence records and 31 collaboration messages.

Therefore the accepted design is family-aware and prospective. It does not impose a universal historical schema or mass-normalize old documents.

## 3. Accepted architecture

Normal ADS governance should now promote a bounded implementation with:

```text
unique numbered identities for Foundations / Specifications / Research / Checkpoints
prospective family metadata contracts
existing checkpoint contract retained
family-aware validation/evidence provenance
existing collaboration-message provenance contract retained and mechanically checked
safe declared-reference existence checks
CURRENT_STATE/current_routing synchronization plus branch-scoped freshness
short stable current_boundary category without embedded volatile artifact IDs
one aggregate PUBLIC_REPOSITORY_INTEGRITY gate over focused validators
separate PRIVATE_CONTINUITY_INTEGRITY status that may be NOT_VERIFIED
CHAT_ROTATION_PREFLIGHT composing the required public/private results
explicit deterministic regression/unit-test matrix
local pre-transition check obligation while branch protection remains disabled
```

The public GitHub branch is currently unprotected and required status checks are disabled, so CI is advisory until repository rules change. The development method must not call a workflow "blocking" merely because it exists.

## 4. Explicit non-goals

Not accepted for this V1 response:

```text
one universal Markdown schema
sidecar metadata for every document
central hand-maintained artifact registry
general dependency graph
semantic contradiction detector
vector index for integrity validation
mass historical rewrite
mandatory document generator
public-CI claims that private continuity is fresh
```

## 5. Continuity correction

The fresh ChatGPT conversation used to prove Codexless developer-MCP invocation was a disposable plugin-validation chat, not the next canonical persistent ADS session. The project owner intends to delete it.

The current canonical ChatGPT interaction remains `chatgpt-11`. The next persistent ChatGPT interaction must be opened through the standard repository-first continuation procedure before its canonical identity/title is minted.

Any current artifact that treats the disposable Codexless test chat as canonical `chatgpt-12` must be transparently corrected during the implementation/reconciliation phase. The technical Codexless read-path evidence remains valid.

## 6. Next governance boundary

MC-0008 is resolved as architecture review. It does not itself implement or canonize the mechanism.

Next:

```text
create the normal ADS research/design record
freeze the implementation specification
implement shared family-aware validators + tests + aggregate gate
repair current routing / CURRENT_STATE / Knowledge Map and known stale references
repair the private-companion continuity record separately
run the aggregate repository/chat-rotation preflight
only then declare the repository rotation-ready
```

Permanent Source Vault ingestion remains paused until the project-owner-selected repository-preservation work is completed and accepted.