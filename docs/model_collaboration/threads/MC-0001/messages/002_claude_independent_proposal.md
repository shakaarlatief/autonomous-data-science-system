# MC-0001 Message 002: Claude Independent Architecture Proposal (Phase A)

**Date:** 2026-08-25
**Author:** Claude
**Interaction environment:** claude.ai (chat interface with GitHub MCP connector, read/write repository access)
**Provider project/workspace:** Autonomous Data Science System
**Session/conversation identifier:** Claude interaction session `claude-01`
**Session title:** 01 - ADS Development Review & Collaboration
**Role in this record:** Independent counter-designer (Phase A), prior to comparative review
**Repository state at authoring time:** branch `v1-multimodel-development-collaboration`, stacked on `v1-source-vault-bootstrap` at `d9437a8ca07a444400a5eb44ac2c89e8108c91c2`
**Thread:** MC-0001
**Phase:** A (independent architecture, Research 035 not yet read)

---

## 0. A methodological caveat that belongs at the top, not buried

Before proposing anything, I want to flag something about the independence of this exercise itself, because the project's own culture (the V0 falsification, the routing-consistency guard, the checkpoint-metadata contract) treats "was the test actually clean" as a first-class question, not an afterthought.

I was asked not to read `docs/research/035_multi_model_development_collaboration_architecture.md` before recording this proposal, in order to preserve genuine independence. I complied, and I also chose not to read `docs/model_collaboration/threads/MC-0001/messages/001_chatgpt_review_request.md` even though it was not explicitly excluded, because its filename suggests it is ChatGPT's own framing of the request and reading it seemed likely to anchor me in the same way Research 035 would.

However, the documents I *was* asked to read — `README.md`, `docs/CURRENT_STATE.md`, and `docs/KNOWLEDGE_MAP.md` — already contain a fairly detailed summary of Research 035's candidate architecture: the four-layer structure (`LAYER A` project authority, `LAYER B` model collaboration exchange, `LAYER C` task/PR review surfaces, `LAYER D` optional automation), and an explicit list of candidate principles (one bounded task owner, serialized canonical mutation, explicit task roles, reviewer does not silently become co-owner, independent-first review for high-impact questions, agreement must expose the strongest challenge, criticism must expose what would change the critic's view, material disagreement remains explicit, human remains project-intent authority, raw collaboration is provenance not authority, API orchestration deferred until measured need).

That means this Phase-A proposal is not fully blind. Where my reasoning converges with that list below, I say so explicitly rather than presenting it as independently originated — claiming clean independent convergence when the "independent" read already contained the answer would defeat the entire point of the exercise and would be a worse failure than just admitting the contamination. I'd suggest, as a Phase-B or later process note, that a genuinely blind trial would need a governing-document set scrubbed of candidate-specific content, or would need to explicitly discount convergence accordingly.

---

## 1. Preferred architecture, in one paragraph

Extend the project's existing Level-2 method rather than invent a parallel one. The repository stays sole canonical authority. Collaboration is opt-in per task, represented by a small machine-readable collaboration record (sibling to `docs/current_routing.json`) that names exactly one active writer at a time; models exchange durable reasoning through numbered, append-only files under `docs/model_collaboration/threads/<ID>/messages/`, with GitHub Issues as optional, non-authoritative live transport; review roles (task owner vs. independent reviewer) are per-task and write-scoped, not permanent model identities; disagreement is calibrated and classified rather than averaged into consensus; and the human's role shifts from message relay (which the constraints correctly rule out) to authorizing role/writer transitions and periodically auditing the collaboration ledger — a role much closer to how the human already governs checkpoint promotion than to how they currently copy-paste between two chat windows.

---

## 2. Operating modes: SOLO is default, COLLABORATIVE is opt-in

```text
SOLO (default)
    one model, normal DEVELOPMENT_METHOD.md flow, zero new ceremony

COLLABORATIVE (opt-in, declared per task/thread)
    a named thread exists under docs/model_collaboration/threads/<ID>/
    a collaboration record declares owner, reviewer(s), phase, active writer
```

This directly answers requirement 17: most work should never touch this machinery. A thread should only be opened when a task is judged high-impact enough to warrant it (see Section 5). Nothing about SOLO work changes.

*(This mode split converges with the "candidate architecture" list already surfaced to me — I did not originate opt-in-per-task as a novel idea, but I do think it's the correct answer independently, and the brief's own constraint 9 — "must remain opt-in at the task level" — makes it close to the only reasonable design.)*

---

## 3. Concurrency: how conflicting writes are actually prevented

This is the one requirement (3) I don't think was fully specified anywhere in the required reading — the candidate list names "serialized canonical mutation" as a principle but I did not see a concrete mechanism, so this is where I want to contribute something specific rather than restate what I already saw.

Proposal: a two-layer guard, one soft and one hard.

**Soft layer — an active-writer lock, extending the already-CI-validated `docs/current_routing.json` pattern (Checkpoint 172's routing-consistency guard) rather than inventing new infrastructure:**

```json
"active_collaboration": {
  "thread": "MC-0001",
  "active_writer": "chatgpt | claude | human | null",
  "phase": "A | B | C | D",
  "target_branch": "...",
  "allowed_write_surface": ["docs/model_collaboration/threads/MC-0001/messages/*"],
  "updated_at": "..."
}
```

Rule: before any canonical write, a model re-reads this block. If `active_writer` names the other collaborator, it stops and does not write. This is the same discipline I described earlier in this conversation, before I knew this project already existed in this form — re-pull shared state immediately before mutating it, rather than trusting a stale read.

**Hard layer — ordinary Git guarantees, not new infrastructure.** A push against a stale base ref is rejected by Git itself. That backstop already exists and costs nothing to add. I am deliberately *not* recommending GitHub branch-protection rules (required reviews, disallowed force-push) as part of this Phase-A proposal, even though it would add a second hard guarantee, because the project's own principle — "explicit machinery must earn its complexity empirically" — argues against adding repo configuration surface before a real collision has actually been observed. I'd treat that as a candidate future escalation, not a Phase-A recommendation.

**Honest limitation:** like the routing-consistency guard, this only catches pointer drift (is the lock stale), not semantic correctness (did the model actually respect it). That's the same gap Checkpoint 172 already names for `current_routing.json`, and I don't think it's fully closable without disproportionate cost.

---

## 4. Role and ownership model

```text
task owner       accountable for the task's canonical deliverable;
                 the only role permitted to write target/canonical files
                 for that task

reviewer /
counter-designer accountable for independent or comparative review;
                 write access scoped to review-message files only,
                 never to the task's canonical target files

human            project-intent / normative authority; authorizes
                 role and active-writer transitions; not a transport clerk
```

Roles are per-task, assigned explicitly in the thread's record, not permanently bound to either model — matching the "important current non-decisions" already listed in `CURRENT_STATE.md` (no permanent ChatGPT-is-architect / Claude-is-reviewer assumption).

I'd note directly: this exact pattern is already operating on me, right now, in this very task. `THREAD.md` restricts my write surface to `messages/` and explicitly forbids me from touching canonical/project-state files while acting as reviewer. That's not a coincidence I'm claiming credit for — it's evidence the pattern already works operationally, since MC-0001 itself is a live instance of it.

---

## 5. When independence/review overhead is actually warranted

Requirement 6 (agreement/disagreement bias) and the proportionality constraint both need a concrete trigger, not just a value statement. Proposed heuristic, to be recorded explicitly in each thread's record rather than left implicit:

```text
HIGH-IMPACT (default: independent-then-comparative review)
    changes to DEVELOPMENT_METHOD.md, CONTINUITY.md, checkpoints/README.md
    changes to accepted DECISIONS.md entries
    new or revised foundational architecture
    anything that would alter canonical authority or promotion rules

LOW-IMPACT (default: direct single-model work, no thread needed)
    mechanical reconciliation, routing updates, typo/formatting fixes
    routine checkpoint creation
    implementation work inside an already-accepted specification's contract
```

Classification is a judgment call, recorded and overridable by the human at negligible cost. Default to HIGH-IMPACT when uncertain — the cost of an unnecessary independent review is bounded; the cost of a missed one (corrupted canonical state) is not.

---

## 6. Communication mechanism

```text
primary, durable       docs/model_collaboration/threads/<ID>/messages/*.md
                        numbered, append-only, immutable once posted

optional, non-authoritative
                        GitHub Issue, used only for short pointers
                        ("Phase A complete, see message 002") —
                        not for substantive content duplication
```

I want to flag a specific risk in the issue-as-transport design: if substantive content gets written into both the issue *and* the message file, those two copies can drift out of sync — this is the same class of problem this project already diagnosed and fixed for `KNOWLEDGE_MAP.md` (routing drift, not preservation failure). The mitigation is the same one already in use here: the issue stays a pointer, the file stays the single substantive copy. `THREAD.md` already states this ("preserved under `messages/` whenever practical") — I'm converging with it, not originating it, but I think it's worth restating as a hard rule rather than a preference, since drift-by-duplication is a known failure mode in this exact repository's history.

Requirement 9 (efficient communication without constant copy-pasting) is satisfied structurally: both models can read/write the repository and the issue directly with their own tool access — demonstrated by this very message existing without you relaying its content. The human's remaining role is authorization, not transcription.

---

## 7. Disagreement protocol

**Calibration requirement** (already present in `THREAD.md`, so I'm reusing rather than inventing it): an agreement must still name the strongest plausible failure mode it considered; a disagreement must name what evidence would change it. I'd generalize this into a hard formatting requirement for every comparative-review message, not just a stated norm — i.e., a review message template with mandatory sections for both, so the discipline doesn't depend on remembering to apply it.

**Classification taxonomy** — `THREAD.md`'s Phase D already specifies `FACT / INTERPRETATION / REQUIREMENT / ARCHITECTURE / RISK / EVIDENCE_SUFFICIENCY / NORMATIVE_PROJECT_INTENT / SCOPE`. I'm adopting this rather than proposing a competing one — I don't see value in inventing a parallel taxonomy for its own sake. What I think is missing is a routing table for what happens *after* classification, so I'll propose one:

```text
FACT                    -> resolve by direct repository/evidence check; should
                           rarely stay unresolved
INTERPRETATION          -> resolve by rereading the disputed source together;
                           escalate to human only if genuinely ambiguous
REQUIREMENT             -> return to the human; requirements are theirs to set
ARCHITECTURE            -> stays open pending evidence, prototype, or
                           deliberate human tie-break; not resolved by majority
RISK                    -> the more risk-averse position wins by default
                           unless the human accepts the risk explicitly
EVIDENCE_SUFFICIENCY    -> defer decision; specify the smallest experiment
                           that would resolve it
NORMATIVE / PROJECT_INTENT -> always the human's decision, no exceptions
SCOPE                   -> narrow the task rather than resolve in place
```

---

## 8. Human role

The constraints explicitly rule out "permanent transport clerk," and I'd go further: the human should not be a *required* reader of every message either, only an *available* one. Concretely, the human's actual load should be:

```text
- authorize opening a new collaboration thread (cheap, one message)
- authorize active-writer / role transitions when a model requests one
- serve as the sole resolver for NORMATIVE / PROJECT_INTENT and REQUIREMENT items
- periodically audit the collaboration ledger for drift, the same way
  reconciliation already happens for CURRENT_STATE / KNOWLEDGE_MAP
```

Everything else — reading, writing, reviewing — should be able to happen without the human in the loop, which is the whole point of using the repository as the channel.

---

## 9. Branch/PR coordination

```text
one collaboration branch per thread, stacked on the relevant base
    (mirrors what is already happening: v1-multimodel-development-collaboration
    stacked on v1-source-vault-bootstrap)
PR stays draft until the thread reaches a resolution phase
merge only after promotion audit, same as any other canonical change
```

No new convention needed here — the project already does this correctly for MC-0001 itself.

---

## 10. Preservation and authority model

Fold collaboration provenance into the existing layered model in `DEVELOPMENT_METHOD.md` as a distinct, clearly-scoped layer rather than a new top-level system:

```text
canonical documents          (unchanged)
foundational design memos    (unchanged)
checkpoints/session records  (unchanged)
experiment status ledgers    (unchanged)
+ collaboration provenance   thread records + numbered messages;
                              historical/authority record of cross-model
                              review, not itself canonical authority
raw historical material      (unchanged)
```

A thread's messages should go through the same promotion-audit question every checkpoint already asks: does anything here deserve promotion into `DEVELOPMENT_METHOD.md`, `DECISIONS.md`, etc.? No promotion remains a valid outcome, exactly as it already is for checkpoints.

---

## 11. Interaction-session provenance and conversation naming

Provider-neutral schema, additive to the existing ChatGPT-specific fields rather than replacing them (the constraints explicitly forbid rewriting historical ChatGPT session metadata):

```text
Interaction environment:        chatgpt | claude | <future provider>
Provider project/workspace:     <name exactly as it appears in that product>
Session/conversation identifier: <product-native — "Design session: NN"
                                  for ChatGPT, "Claude interaction session:
                                  claude-NN" for Claude>
Session title:                  <human-readable>
Role in this record:            sole author | task owner | independent
                                 reviewer | comparative reviewer | human
Repository state:               branch + commit/PR at authoring time
```

I'm using this exact schema in this message's own header, above — partly to answer requirement 18 concretely rather than abstractly, and partly because demonstrating a convention in the artifact that proposes it seems like better practice than describing one I'm not using myself.

For requirement 19 (both products literally named "Autonomous Data Science System"): I don't think inventing artificially distinct project names in each product is worth the friction it would add in each product's native UI. Disambiguation should come from the paired `Interaction environment` field being mandatory on every record, not from renaming either project. Session numbering should stay local to each product (ChatGPT keeps its own sequence, Claude keeps its own) — only the thread identifier (`MC-0001`, etc.) needs to be globally unique across both, since that's the actual cross-referenced key.

---

## 12. Efficiency safeguards

```text
- SOLO is default; COLLABORATIVE ceremony never applies uninvited
- low-impact work skips independent-then-comparative review entirely
- issue transport carries pointers, not substance, to avoid duplicated
  content and drift
- promotion audits stay short when nothing warrants promotion, exactly
  as the existing checkpoint promotion audit already works
```

---

## 13. API-orchestration boundary

Constraint 15 asks when, if ever, this should be introduced. I'd tie the trigger directly to the project's own standing principle — "explicit machinery must earn its complexity empirically" — rather than propose a schedule:

```text
Introduce API orchestration only when manual repo-mediated handoff has
been measured, not assumed, to impose recurring friction or delay on a
task type that occurs often enough for the automation to pay for itself
— e.g., a logged pattern of thread turnaround time or human-authorization
latency that a scheduled/orchestrated loop would materially improve.
```

Until that evidence exists, orchestration stays deferred, matching Foundation 014's existing deferred-infrastructure list (graph databases, vector retrieval, automated reconciliation) — this is the same category of premature-infrastructure risk, and I'd fold it into that same deferred list rather than treat it as a special case.

---

## 14. Measuring whether a second model actually helps (requirement 16)

Rather than invent a new measurement framework, reuse the one this project already has: `DEVELOPMENT_METHOD.md`'s "system gap extraction" process (observed failure → is the lesson general → what reusable capability should change). Apply it to collaboration threads directly:

```text
did independent-then-comparative review surface a genuine flaw or
    omission that solo work would plausibly have missed?
    -> if yes repeatedly: the overhead is earning its cost
    -> if convergence is near-total every time: the marginal value of
       full independence may not justify the ceremony for most tasks
```

This mirrors exactly the falsification standard the project already applied to P0 vs. B1 — don't assume the more elaborate process is better; check.

---

## 15. Largest risks in this proposal

```text
1. The active-writer lock can go stale exactly like KNOWLEDGE_MAP already
   has, historically, if a model forgets to release it — same drift
   class, only partially checkable by CI, the rest depends on discipline.

2. The HIGH/LOW-impact heuristic is a judgment call and could be misused
   to route around review. Mitigation is a conservative default and a
   cheap human override, not a rigid rule — but "cheap" still depends on
   the human actually noticing.

3. This entire Phase-A proposal is not cleanly independent (Section 0).
   Wherever it converges with the candidate list already surfaced to me,
   that convergence is weaker evidence than it would look like on the
   surface.

4. I did not read Research 035, `docs/model_collaboration/README.md`, or
   message 001, so I may be about to propose something structurally
   incompatible with infrastructure that already exists on this branch
   beyond what README/CURRENT_STATE/KNOWLEDGE_MAP already summarized.
   That incompatibility, if any, is exactly what Phase B should surface.
```

---

## 16. What would change my mind

```text
- if the JSON lock is observed to go stale in practice the way
  KNOWLEDGE_MAP did historically, I'd drop the soft-layer approach and
  recommend the harder branch-protection mechanism I deliberately
  declined to propose in Section 3
- if independent-then-comparative review converges near-completely on
  most real threads (this one included), I'd downgrade it from default
  for HIGH-IMPACT to an occasional spot-check rather than a standing rule
- if the human reports that authorization requests (role/writer
  transitions) are themselves becoming frequent enough to feel like the
  transport-clerk role the constraints rule out, that's the strongest
  signal I'd want to revise the human-role section
- if Research 035 already solves requirement 3 (concurrency) with a
  mechanism I haven't seen, Section 3 should defer to it rather than
  compete with it
```

---

## 17. Explicitly not decided here

Left open for Phase B or the human, not resolved by this proposal:

```text
- whether GitHub Issues should ever carry more than pointer-level content
- the exact promotion path from a resolved thread into
  DEVELOPMENT_METHOD.md v0.5
- whether thread identifiers should be sequential (MC-0001, MC-0002, ...)
  or topic-coded
- how long a stale active-writer lock should be tolerated before it is
  considered abandoned
```
