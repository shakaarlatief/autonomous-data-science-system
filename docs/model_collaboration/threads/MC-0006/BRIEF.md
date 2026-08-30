# MC-0006 Brief: Source Universe Architecture and Permanent Vault Deployment Review

**Thread:** MC-0006  
**Date opened:** 2026-08-30  
**Review mode:** ADVERSARIAL_REVIEW  
**Exact frozen target:** `4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c`  
**Target branch:** `v1-source-vault-bootstrap-resume`  
**Reviewer environment:** normal Claude Project / `claude-01` with full repository access through the custom connector  
**Purpose:** Conduct a read-only second-model review of the accepted Source Universe substrate, its permanent user-controlled deployment process, and the boundary from durable source evidence into the later Methodological Knowledge Universe before the first permanent private vault write.

## Why this review exists

The Source Universe architecture was developed and validated before multi-model review became a normal available project-development mode. Claude reviewed the collaboration method, Cockpit work, and repository information architecture in other threads, but there has not yet been a dedicated Claude review of the Source Universe architecture and permanent Source Vault deployment process.

The project owner has normal Claude with full repository access through a custom connector and also has Claude Code available locally. Before the substantive review began, the two environments were explicitly compared for this task. The chosen split is: normal Claude performs the read-only architecture/repository review; Claude Code is reserved for later narrow execution-based verification and Windows-local deployment work when actual command/filesystem evidence is required.

This is a high-leverage point for a bounded adversarial review because the architecture is already concrete and tested, while irreversible user-controlled storage decisions have not yet been made.

This review must not become a generic redesign exercise. Challenge the existing design where evidence warrants it, distinguish actual defects from preferences, and identify the smallest safe corrections if any are needed before deployment.

## Review target

Review the repository exactly as it existed at:

```text
4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c
```

The target is immutable for this review. Do not modify Source Universe implementation, canonical architecture, runbooks, current routing, or other target state while reviewing it.

Read the canonical Source Universe architecture, accepted specification/foundation/research chain, permanent bootstrap runbook, first-corpus validation evidence, source manifest/fingerprints, implementation, schema/migrations, CLI behavior, and relevant tests from that frozen target.

## Architecture questions to challenge

Assess at least the following.

1. **Source identity and exact-artifact model**
   - Are logical source identity, exact bytes/artifacts, encounters/ingestion provenance, collections, locators, versions/variants, and uncertainty separated correctly?
   - Can the model preserve same-name/different-bytes and same-bytes/different-encounter cases without losing meaning?

2. **Content-addressed storage and integrity**
   - Is exact-byte hashing/content addressing used safely and coherently?
   - Are deduplication, integrity auditing, orphan detection, corruption detection, and recovery semantics adequate?
   - Are write ordering, atomicity, partial-failure and crash-recovery risks handled well enough for the permanent deployment?

3. **Registry and vault separation**
   - Is SQLite + private content-addressed object storage an appropriate first permanent deployment architecture?
   - Is the separation between Source Registry, Source Vault, original source folder, backup, and clean restore target sound?

4. **Prospective comparison and intake governance**
   - Is the frozen-manifest/fingerprint comparison before ingestion the right mechanism?
   - Are `MATCH`, `DIFFERENT_ARTIFACT`, `MISSING_LOCAL_SOURCE`, and `ADDITIONAL_LOCAL_SOURCE` handled without silent normalization or provenance loss?

5. **Backup and disaster recovery**
   - Does the backup/restore design actually prove recoverability rather than merely copying files?
   - Is the definition of an independent backup strong enough?
   - Are registry snapshot consistency, object completeness, manifest verification, and clean-restore audit sufficient?

6. **Privacy and public/private boundary**
   - Are source binaries, private paths, private registry snapshots and backup payloads kept out of public Git reliably?
   - Is the public-safe evidence model sufficient to prove deployment without leaking private source content or machine-local information?

7. **Source Universe versus Knowledge Universe**
   - Is the boundary conceptually correct: Source Universe preserves durable evidence; Methodological Knowledge Universe contains reusable interpreted methodological knowledge?
   - Does the current architecture preserve enough provenance for later source -> extracted evidence -> accepted knowledge construction, revision and contradiction handling?
   - Is any missing provenance/relationship layer a must-fix before source ingestion, or can it safely be added later without re-ingesting exact bytes?

8. **Operational robustness on a local Windows-first deployment**
   - Review path handling, filesystem semantics, permissions, symlinks/reparse points, file mutation during hashing/copying, locking/concurrent writers, SQLite durability, temporary files and interrupted operations.
   - Separate realistic first-deployment risks from theoretical hardening that can wait.

9. **Scalability and migration path**
   - Would the current design scale cleanly from the first educational corpus to many courses and broader methodological sources?
   - Is migration to object/cloud storage later possible without changing source identity/provenance semantics?
   - Identify the first likely scaling failure and the trigger that should cause redesign.

10. **Permanent bootstrap runbook**
    - Is the execution order safe and efficient?
    - Are all destructive/irreversible or privacy-sensitive boundaries preceded by appropriate checks?
    - Is Course 2 correctly blocked until working-store audit, verified independent backup, clean restore and restored audit succeed?

11. **Security and trust assumptions**
    - Identify any path traversal, malicious-file, digest, database, backup, restore, or untrusted-input assumptions that matter for the intended source corpus.
    - Do not demand enterprise security controls unless the actual threat model justifies them.

12. **Complexity and maintenance tax**
    - Is any part over-engineered for the current problem?
    - Is any apparently simpler alternative materially safer or easier while preserving exact provenance and recoverability?

## Execution-evidence boundary

The normal Claude reviewer has full repository access but is not being used as the local execution environment for MC-0006.

For any finding where static repository inspection is materially insufficient, especially backup/restore behavior, crash/partial-failure resilience, concurrent-writer behavior or Windows-specific filesystem semantics, explicitly classify the evidence gap and state the smallest targeted execution check needed.

Do not convert MC-0006 into a deployment session. Any such execution check should be performed later through a separately scoped Claude Code or other execution-agent task after the architectural review is preserved.

## Required review output

Write one durable review message at:

```text
docs/model_collaboration/threads/MC-0006/messages/001_claude_source_universe_architecture_review.md
```

The message should include:

```text
exact SHA reviewed
review conclusion
strongest parts of the architecture
findings classified as:
    MUST_FIX_BEFORE_DEPLOYMENT
    SHOULD_FIX_EARLY
    WATCHPOINT
    ACCEPTABLE_TRADEOFF / NO_CHANGE
for every finding:
    concrete evidence
    consequence
    smallest justified correction
source->knowledge boundary assessment
permanent-bootstrap assessment
execution-dependent evidence gaps, if any
strongest simpler alternative, if one exists
first likely 10x-scale failure
explicit answer: safe to proceed with permanent deployment as designed, yes/no/yes-with-preconditions
```

Do not optimize for agreement with ChatGPT. Do not invent disagreement either.

## Blocking semantics

This review is **non-blocking for disk cleanup, free-space investigation, and selection of candidate private locations**.

It **does block the first permanent Source Registry/Vault write** until ChatGPT has dispositioned any Claude findings and the project owner has been told whether the deployment design remains safe to execute.
