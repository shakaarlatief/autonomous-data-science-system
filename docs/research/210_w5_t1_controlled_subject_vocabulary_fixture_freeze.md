# Research 210: W5 T1 Controlled Subject Vocabulary Fixture Freeze

**Date:** 2026-09-20
**Status:** T1 FIXTURE FROZEN / EXECUTION NOT YET PERFORMED
**Selected architecture:** `PKA-CANDIDATE-01`
**Governing W5 design:** Research 208
**C1 qualification:** Research 209 / ACCEPTED
**Source boundary:** `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`
**Scope:** Freeze the first non-authoritative empirical corpus for W5 T1 before evaluating whether a controlled semantic-subject vocabulary provides useful grouping, polyhierarchy and preferred-route behavior over real ADS knowledge.
**Authority:** Research fixture freeze only. It does not freeze the production subject schema, modify canonical source declarations, start broad W5 migration, replace the legacy Knowledge Map, or change operational authority.

## 1. Question

Research 208 established that the current generated `subject_index.json` proves multi-axis emission but does not prove useful semantic subject grouping.

T1 asks:

> Can ADS use a small controlled authored semantic-subject vocabulary, distinct from resolver and structural facets, to organize real project knowledge with useful many-to-many grouping and without creating a central membership registry?

## 2. Candidate architecture under test

The candidate is deliberately lightweight:

```text
subject vocabulary
    controlled IDs and labels
    zero or more broader parents
    optional preferred parent
    legacy-topic correspondences for migration analysis
    NO source membership

source-side/candidate annotation
    zero or more assignable semantic subjects
    optional preferred subject
    null preferred subject allowed when no unique default route exists

other axes
    profile / kind / authority / lifecycle / workstream / privacy / time
    remain structural/derived facets

scope:*
    remains resolver/matching vocabulary
    not semantic-subject truth
```

The subject catalog itself is therefore vocabulary authority only in this experiment. It is not substantive project-content authority and cannot answer which source owns a project fact.

## 3. Frozen vocabulary

The fixture contains:

```text
6 non-assignable navigation parents
17 assignable semantic subjects
23 total vocabulary nodes
```

The assignable subjects are:

```text
system-identity
project-orchestration
knowledge-representation
evaluation-assurance
runtime-persistence
retrieval-context
recommendation-action
methodological-knowledge
source-universe
development-governance
project-knowledge-architecture
model-collaboration
tooling-integrations
cockpit-product
cockpit-interaction
cockpit-visual-language
cockpit-implementation
```

Two kinds of polyhierarchy are intentionally present:

```text
knowledge-representation
    -> ads-system
    -> methodological-engine

project-knowledge-architecture
    -> ads-system
    -> project-development

tooling-integrations
    -> runtime-and-tooling
    -> project-development

cockpit-implementation
    -> cockpit
    -> project-development
```

This tests the earlier requirement that one preferred route must not become one exclusive semantic parent.

## 4. Frozen corpus

The corpus contains 65 real carriers from the exact source boundary, spanning:

```text
project-global narrative/control surfaces
foundations
specifications
research
Source Universe
Project Cockpit
local execution
model collaboration
Methodological Knowledge Universe
current project-knowledge canonical owners
project-knowledge architecture documentation
```

The candidate memberships were authored by ChatGPT from the real source corpus. This is not an independent annotation study and no independence claim is made.

The corpus intentionally includes single-subject sources, cross-cutting sources with two or three subjects, three sources with no unique preferred route, historical/epistemic artifacts, current operational/domain sources and project-global architecture/control sources.

No production source is edited to carry these annotations.

## 5. Legacy comparator

The evaluator reads the exact source-boundary `docs/KNOWLEDGE_MAP.md` and extracts its authored `KM-TOPIC` memberships.

The legacy comparison is diagnostic, not a claim that the new vocabulary must reproduce the old taxonomy.

The comparison asks whether a candidate preferred route remains broadly continuous with legacy routing where concepts correspond, and whether bounded navigation scenarios can retain required sources while rejecting explicit distractors that broad legacy topics pull into the same neighborhood.

## 6. Navigation scenarios

Eight frozen scenarios cover:

```text
project-knowledge architecture
tooling/runtime integrations
Source Universe
model collaboration
Cockpit interaction
recommendation/action
retrieval/context
evaluation/assurance
```

Each scenario declares candidate subjects, legacy comparator topics, must-retrieve artifacts and must-not-retrieve distractors.

A scenario mechanically passes only when all required artifacts are retrieved and all explicit distractors are rejected. The scenarios are task-shaped rather than exhaustive relevance judgments.

## 7. Interpretation rules

No single metric is allowed to decide T1 automatically.

Strong evidence for the candidate would include no zero-member vocabulary leaves, few or no accidental singletons, non-trivial multi-subject participation without universal over-tagging, explicit no-unique-route cases remaining representable, strong continuity where legacy routing is still appropriate, strong task-shaped retrieval, and no need to use `scope:*` or artifact family as semantic subjects.

Failure or redesign signals include many singleton/empty subjects, one or two subjects absorbing most of the corpus, pervasive need for 3+ tags, preferred-route ambiguity on ordinary sources, candidate probes missing obvious must-retrieve sources, candidate vocabulary merely renaming folder/workstream/artifact axes, or any need for central source membership inside the vocabulary catalog.

## 8. Frozen experiment files

```text
experiments/project_knowledge_subject_navigation_t1/README.md
experiments/project_knowledge_subject_navigation_t1/subject_catalog_candidate.json
experiments/project_knowledge_subject_navigation_t1/corpus_annotations.json
experiments/project_knowledge_subject_navigation_t1/navigation_scenarios.json
experiments/project_knowledge_subject_navigation_t1/evaluate.py
```

The evaluator outputs are not yet present at this freeze.

## 9. Boundary

```text
T1_FIXTURE=FROZEN
T1_EXECUTION=NOT_STARTED
PRODUCTION_SUBJECT_SCHEMA=NOT_FROZEN
PRODUCTION_MEMBERSHIP_MODEL=NOT_FROZEN
LEGACY_KNOWLEDGE_MAP=STILL_LIVE
BROAD_W5_MIGRATION=PAUSED
CURRENT_OPERATIONAL_AUTHORITY=CURRENT_CONTINUITY_ARCHITECTURE
AUTHORITY_SWITCH_ALLOWED=false
NEXT=EXECUTE_T1_AND_INTERPRET_RESULT
```
