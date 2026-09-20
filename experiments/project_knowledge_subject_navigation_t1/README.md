# W5 T1: Controlled Semantic-Subject Vocabulary Experiment

**Status:** Frozen non-authoritative research fixture before execution
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Authority:** Research fixture only. Nothing in this directory is canonical project knowledge or production navigation.

## Purpose

T1 tests whether a small controlled semantic-subject vocabulary can organize real ADS knowledge usefully without:

- reusing open-ended resolver `scope:*` values as subjects;
- turning artifact family, workstream, authority, lifecycle or provenance into subject truth;
- storing source membership centrally in the subject vocabulary;
- forcing one physical directory hierarchy to represent semantic organization;
- retrofitting speculative metadata into production sources.

## Frozen inputs

```text
subject_catalog_candidate.json
    vocabulary + parent graph + legacy-topic correspondences
    contains no membership

corpus_annotations.json
    65 real repository carriers
    non-authoritative candidate subject memberships
    ChatGPT-authored; independence is not claimed

navigation_scenarios.json
    eight must-retrieve / explicit-distractor navigation probes

evaluate.py
    deterministic fixture validator and evaluator
```

All source artifacts and the legacy Knowledge Map are read from the exact source boundary with Git, not from later working-tree state.

## Outputs

Running:

```powershell
.\.venv\Scripts\python.exe experiments/project_knowledge_subject_navigation_t1/evaluate.py
```

materializes:

```text
candidate_projection.json
result.json
RESULT.md
```

These are research outputs, not production generated views.

## Evaluation signals

T1 inspects:

- vocabulary integrity and acyclic polyhierarchy;
- absence of centrally stored membership in the vocabulary;
- corpus coverage;
- subject member-count distribution;
- zero-member and singleton subjects;
- multi-subject participation;
- explicit `NO_UNIQUE_PREFERRED_ROUTE` cases represented by null preferred subject;
- continuity with legacy Knowledge Map routing where comparable;
- eight task-shaped navigation probes against explicit distractors.

No single numerical threshold is preregistered as automatic architectural acceptance. The result must be interpreted for grouping quality, overfitting, authoring burden, portability and separation from resolver/structural facets.
