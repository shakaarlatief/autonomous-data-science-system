# Fresh Collaborator Request: Integrated Q1 + Q2 + Q5 Challenge V0.1

You are an independent fresh collaborator evaluating a frozen Candidate 01 shadow slice. Do not use prior conversation memory. Treat only the files listed below as project evidence for this task. Do not read `docs/CURRENT_STATE.md`, `docs/current_routing.json`, `docs/KNOWLEDGE_MAP.md`, Research 167+, Checkpoint 512+, any oracle file, any result from another collaborator, or any file not listed in **Allowed reads**.

## Allowed reads

1. `docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01/SHADOW_BOOTSTRAP_CORE.md`
2. `docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01/SHADOW_ACTIVE_WORKSTREAM.md`
3. `docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01/SHADOW_SOURCE_VAULT_WORKSTREAM.md`
4. `docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01/SHADOW_AUTHORITY_RISK_INDEX.json`
5. `docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01/SHADOW_CAPTURE_ENVELOPE.md`
6. `docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md`
7. `docs/source_universe/validation/003_permanent_source_registry_migrated.md`
8. `docs/source_universe/validation/004_permanent_first_corpus_prospective_compare_all_match.md`
9. `docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md`

## Task A: consequential current decision

From the bounded bootstrap, determine whether **Course 2 may be admitted now** under the current Source Vault state. Distinguish current governing authority from evidence and plausible historical distractors. Surface applicable known-risk/reopen triggers. State the safest next action and all material blockers. Do not perform any Source Vault write.

## Task B: stale authority-view failure

Evaluate `STALE-VIEW-COURSE2-01`. Determine whether that view may authorize Course 2 admission. If it cannot, fail visibly and state why. Do not silently repair its source binding or treat repeated/derived storage as authority.

## Task C: capture candidate

Identify at most one genuinely useful generalized insight produced by this reasoning that is not merely a copied source sentence. It must be source-traceable. Treat it as **captured candidate knowledge only**, not accepted authority. If no nontrivial insight exists, say so.

## Output

Write exactly one UTF-8 JSON object to:

`docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01/FRESH_COLLABORATOR_RESULT_V01.json`

Use this schema:

```json
{
  "collaborator": "<model/session description>",
  "reads": ["<exact allowed path>", "..."],
  "task_a": {
    "decision": "<string>",
    "governing_sources": ["<path>", "..."],
    "evidence_sources": ["<path>", "..."],
    "distractors_rejected": ["<path>", "..."],
    "activated_risks": ["<risk id>", "..."],
    "blockers": ["<string>", "..."],
    "next_safe_action": "<string>",
    "uncertainty": ["<string>", "..."]
  },
  "task_b": {
    "decision": "<string>",
    "stale_view_id": "STALE-VIEW-COURSE2-01",
    "reason": "<string>"
  },
  "authority_receipt": {
    "task": "COURSE2_ADMISSION_DECISION",
    "workstream": "<semantic id>",
    "governing_source": "<path>",
    "source_revision": "<sha256 from the shadow authority index>",
    "activated_risks": ["<risk id>", "..."],
    "decision": "<string>",
    "blockers": ["<string>", "..."],
    "uncertainty": ["<string>", "..."]
  },
  "capture_candidate": {
    "state": "CAPTURED_NON_AUTHORITATIVE",
    "statement": "<one generalized insight or empty string>",
    "source_basis": ["<path>", "..."],
    "promotion_recommendation": "<REVIEW_FOR_PROMOTION or DO_NOT_PROMOTE>"
  }
}
```

Do not include expected-answer labels from any external source. Do not create or modify any other file.
