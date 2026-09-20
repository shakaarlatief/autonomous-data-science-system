# MC-0019 Brief: W5 T1 Blind Subject-Placement Calibration

**Thread:** MC-0019
**Date opened:** 2026-09-20
**Review mode:** INDEPENDENT / BLIND PLACEMENT CALIBRATION
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact reviewer-fixture target:** `dcd01d865340c0d562c07f68307ef0a2c7ee2d75`
**Exact source-corpus boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Preferred Claude interaction:** fresh Claude conversation
**Authority:** Collaboration evidence only. This thread cannot freeze the production subject architecture or modify project authority by itself.
**Purpose:** Independently test whether the frozen W5 T1 controlled subject vocabulary is clear enough for a second capable model to place representative real ADS artifacts without seeing ChatGPT's candidate annotations, navigation scenarios, legacy Knowledge Map routing, or T1 result outputs.

## 1. Why this thread exists

Research 208 identified placement agreement as a useful T1 diagnostic. ChatGPT authored the initial T1 vocabulary and corpus annotations, so the primary experiment alone cannot establish that another collaborator would interpret the vocabulary similarly.

MC-0019 therefore performs a bounded blind placement pass over 24 representative carriers.

## 2. Allowed reading

Read:

```text
experiments/project_knowledge_subject_navigation_t1/subject_catalog_candidate.json
experiments/project_knowledge_subject_navigation_t1/reviewer_subset.json
```

Then read only the 24 source paths listed in `reviewer_subset.json`, each from the exact source-corpus boundary:

```text
4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
```

Use Git/exact-revision access if available. Do not substitute later working-tree content for those source artifacts.

## 3. Prohibited reading before freezing your answer

Do NOT read:

```text
experiments/project_knowledge_subject_navigation_t1/corpus_annotations.json
experiments/project_knowledge_subject_navigation_t1/navigation_scenarios.json
experiments/project_knowledge_subject_navigation_t1/result.json
experiments/project_knowledge_subject_navigation_t1/candidate_projection.json
experiments/project_knowledge_subject_navigation_t1/RESULT.md
docs/KNOWLEDGE_MAP.md
any later T1 interpretation/result research
```

Do not inspect Git diffs/commits that reveal those files' contents indirectly.

This restriction is for construct validity, not secrecy.

## 4. Placement task

For every path in `reviewer_subset.json`:

1. choose one or more **assignable** subjects from the candidate catalog;
2. choose exactly one `preferred_subject` when one subject is clearly the best default route;
3. use `null` when no unique preferred route exists;
4. provide confidence as `HIGH`, `MEDIUM`, or `LOW`;
5. optionally flag `missing_vocabulary` when the existing catalog cannot represent an important semantic neighborhood cleanly.

Do not assign the non-assignable parent nodes.

Do not invent new subject IDs inside the assigned set. A missing-vocabulary proposal is evidence for later redesign, not an implicit catalog edit.

Use primary semantic subject, not artifact family, file path, workstream state, authority class, lifecycle state or provenance depth as a substitute.

## 5. Required response format

Write exactly one message at:

```text
docs/model_collaboration/threads/MC-0019/messages/001_claude_blind_subject_placement.md
```

Start with normal collaboration provenance and confirmation that prohibited files were not read.

Then include exactly one machine-readable JSON code block of this form:

```json
{
  "source_boundary": "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef",
  "catalog_review_target": "dcd01d865340c0d562c07f68307ef0a2c7ee2d75",
  "reviewer": "Claude",
  "annotations": [
    {
      "path": "...",
      "subjects": ["..."],
      "preferred_subject": "... or null",
      "confidence": "HIGH|MEDIUM|LOW",
      "missing_vocabulary": []
    }
  ]
}
```

After the JSON block, briefly report:

- vocabulary terms that were hard to distinguish;
- cases where `preferred_subject=null` was necessary;
- any repeated missing-vocabulary pressure;
- any catalog label/definition ambiguity that could cause collaborator drift.

Do not compare against ChatGPT's answers. ChatGPT will perform that comparison only after your response is durably frozen.

## 6. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0019/messages/**
```

Do not modify the experiment fixtures, source documents, project state, routing, generated views, research results or architecture documentation.

```text
MC0019=OPEN
MODE=INDEPENDENT_BLIND_PLACEMENT
REVIEWER_FIXTURE_TARGET=dcd01d865340c0d562c07f68307ef0a2c7ee2d75
SOURCE_BOUNDARY=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
NEXT=CLAUDE_MESSAGE_001
```
