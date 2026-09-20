# MC-0020 Brief: W5 T1 V0.2 Blind Subject-Placement Calibration

**Thread:** MC-0020
**Date opened:** 2026-09-20
**Review mode:** INDEPENDENT / BLIND PLACEMENT CALIBRATION
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Exact reviewer-fixture target:** `f4308cc74b6d44640f399b6e9c102473382232df`
**Exact source-corpus boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Reviewer control:** fresh Claude Opus conversation, no reuse of MC-0019 conversation
**Authority:** Collaboration evidence only. This thread cannot freeze production subject architecture by itself.

## 1. Purpose

MC-0020 repeats the MC-0019 24-carrier blind placement test against the refined V0.2 subject contract.

The sample and source boundary are intentionally unchanged. The independent variable is the vocabulary contract:

```text
V0.1
    labels + hierarchy

V0.2
    labels + definitions + include/exclude guidance
    explicit substantive-content membership threshold
    explicit preferred-route rule
    new admissibility-authority subject
    legacy comparison hints removed from reviewer view
```

The goal is to determine whether the refinements materially improve placement consistency without forcing a central membership registry or collapsing semantic subjects into structural axes.

## 2. Allowed reading

Read only:

```text
experiments/project_knowledge_subject_navigation_t1_v02/subject_catalog_reviewer_v02.json
experiments/project_knowledge_subject_navigation_t1_v02/reviewer_subset_v02.json
```

Then read only the 24 source paths listed in `reviewer_subset_v02.json`, each from the exact source-corpus boundary:

```text
4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
```

Use exact Git/revision access. Do not substitute later working-tree content.

## 3. Prohibited reading before freezing Message 001

Do NOT read any path listed in `reviewer_subset_v02.json` under `prohibited_read_paths`.

In particular, do not read:

```text
ChatGPT V0.2 annotations
V0.2 navigation scenarios
V0.2 generated results/projections
the full candidate catalog with legacy_topics
V0.1 annotations/results/calibration outputs
MC-0019 Claude or ChatGPT placement/comparison messages
docs/KNOWLEDGE_MAP.md
Research 215/216 interpretation
```

Do not inspect Git diffs, commit file lists, searches or adjacent artifacts in a way that indirectly reveals those contents.

This restriction is for construct validity, not secrecy.

## 4. Placement task

For every path in the reviewer subset:

1. choose one or more **assignable** subjects from the reviewer catalog;
2. apply the catalog's substantive-content membership threshold to every assignment, including secondary subjects;
3. choose exactly one `preferred_subject` when one subject is the best default route;
4. use `null` only when two or more assigned subjects are genuinely co-primary;
5. provide confidence as `HIGH`, `MEDIUM`, or `LOW`;
6. optionally flag `missing_vocabulary` when the refined catalog still cannot represent an important semantic neighborhood cleanly.

Do not assign non-assignable parent nodes.

Do not invent subject IDs in the assigned set.

Do not use artifact family, file path, authority class, lifecycle, workstream, physical domain or resolver scope as substitute subject meaning.

## 5. Required response

Write exactly one message at:

```text
docs/model_collaboration/threads/MC-0020/messages/001_claude_v02_blind_subject_placement.md
```

Begin with collaboration provenance and confirm that prohibited files were not read.

Then include exactly one machine-readable JSON code block:

```json
{
  "source_boundary": "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef",
  "catalog_review_target": "f4308cc74b6d44640f399b6e9c102473382232df",
  "reviewer": "Claude Opus",
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

- any subject boundaries that remain hard to distinguish;
- any carrier for which the multi-membership threshold was still ambiguous;
- any case where `preferred_subject=null` was necessary;
- repeated missing-vocabulary pressure;
- whether `preferred_parent` was understood as display/default routing only;
- whether the definitions/include/exclude guidance materially helped placement.

Do not compare against V0.1 or ChatGPT annotations. ChatGPT will perform that comparison only after the response is durably frozen.

## 6. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0020/messages/**
```

Do not modify experiment fixtures, source documents, routing, current state, research, generated views or architecture docs.

```text
MC0020=OPEN
MODE=INDEPENDENT_BLIND_V02_PLACEMENT
REVIEWER_FIXTURE_TARGET=f4308cc74b6d44640f399b6e9c102473382232df
SOURCE_BOUNDARY=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
NEXT=CLAUDE_MESSAGE_001
```
