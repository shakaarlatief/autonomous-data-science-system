# Research 126: Knowledge Identity and Multi-Axis Organization Deep Dive

**Date:** 2026-09-13
**Status:** D1-D2 EVIDENCE DEEP DIVE COMPLETE / ARCHITECTURE-NEUTRAL IDENTITY AND VIEW CONSTRAINTS ESTABLISHED / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Deepen Research 125 discriminators D1 (stable knowledge identity) and D2 (multi-axis organization and views) using mature information-organization, archival, bibliographic, cultural-heritage and operational knowledge-base models. Determine what the evidence says about semantic identity versus files/labels, contextual groupings, multiple hierarchies, relation metadata and candidate identity boundaries without selecting an ontology, graph database, file schema or target implementation.
**Authority:** Supporting external-evidence research under Research 124. This record constrains later candidate comparison but does not create new project-development authority, replace current artifact families, or select a successor architecture.
**Declared references:** `research:124`, `research:125`, `checkpoint:463`, `checkpoint:464`, `path:docs/KNOWLEDGE_MAP.md`

## 1. Question under investigation

Research 125 established that concept identity can be independent of a label or document and that several concern-shaped views may coexist over one body of knowledge. D1 and D2 ask the deeper questions underneath that observation:

> **What are the things in project-development knowledge that may need stable identity, and which apparent structures are merely representations, labels, groupings or views over those things?**

The inquiry is intentionally earlier than technology choice. It does not begin with RDF, graph databases, front matter, Markdown, SQL or vector search.

The key distinctions to test are:

```text
semantic thing      != label
semantic thing      != file path
semantic thing      != one physical/digital carrier
semantic thing      != one hierarchy position
semantic thing      != navigation group
relationship        may or may not need its own metadata/lifecycle
view                may present the same thing differently for different tasks
```

## 2. Evidence method

The deep dive gives greatest weight to primary standards and operational models that have maintained identity and context across large, changing knowledge collections.

The main evidence families are:

```text
W3C SKOS
    concept identity, labels, semantic relations and cross-scheme mappings

Getty Art & Architecture Thesaurus (AAT)
    persistent concept IDs, polyhierarchy, organizational nodes and editorial evolution

IFLA Library Reference Model (LRM)
    entity versus appellation, multiple nomens, relationship-driven user tasks

ICA Records in Contexts (RiC-CM / RiC-O)
    record resource versus instantiation, contextual record sets,
    activities, concepts and relations with their own evidence/state metadata

CIDOC CRM
    identifiable information objects independent of physical carriers

Wikidata / Wikibase model
    stable entities, statement-level qualifiers/references/ranks and preservation
    of deprecated but historically useful claims
```

These domains differ substantially from ADS. Their value is convergence on identity and organization principles, not permission to import their full ontologies.

## 3. Concept identity is repeatedly separated from names and labels

### 3.1 SKOS

**Primary source:** W3C, *SKOS Simple Knowledge Organization System Reference*.

URL: https://www.w3.org/TR/skos-reference/

SKOS represents a `Concept` separately from lexical labels. One concept can have preferred, alternative and hidden labels. Broader, narrower and related relations connect concepts independently of those labels. SKOS also distinguishes exact, close, broader, narrower and related mappings between concept schemes; importantly, `closeMatch` is intentionally non-transitive to avoid compounded mapping errors.

**Transfer:** If a durable ADS concept survives a rename, abbreviation or terminology change, its project identity should not have to change merely because its display label changes. Similarity or mapping between two concepts should also not silently collapse them into one identity.

**Limit:** SKOS is deliberately lightweight and does not model ADS authority, workstreams, evidence or lifecycle.

### 3.2 Getty AAT

**Primary sources:** Getty Vocabulary Editorial Guidelines.

URLs:
- https://www.getty.edu/publications/vocabularies-editorial-guidelines/aat-guidelines/3_editorial_rules/3.2/
- https://www.getty.edu/publications/vocabularies-editorial-guidelines/aat-guidelines/3_editorial_rules/3.1/
- https://www.getty.edu/publications/vocabularies-editorial-guidelines/aat-guidelines/4_appendices/4.4/

AAT assigns each concept record a unique persistent `Subject_ID`. The human-readable label is generated for display and is not the system identity. IDs of deleted records are not reused. When records merge, mappings from old identifiers are preserved in releases.

This gives a concrete operational precedent for:

```text
concept identity
    != preferred term
    != qualifier
    != label
    != hierarchy path
```

AAT is also polyhierarchical. A concept may have multiple parents, while one parent is marked preferred as a **default for display or easy access**. Getty explicitly says the other parents remain valid for retrieval.

**Transfer:** A project may have one preferred/default navigation route without asserting that the route is the unique semantic home of the knowledge object.

## 4. Organizational structure is not necessarily semantic identity

Getty makes a particularly useful distinction between actual concept records and organizational levels. Facets, guide terms and hierarchy names structure the thesaurus, but are not themselves intended for indexing as concepts.

This matters for Research 124 because a navigation layer can contain useful organizational nodes that do not deserve the same lifecycle or identity semantics as the knowledge being organized.

Examples in ADS could include future generated constructs such as:

```text
"current work"
"recent evidence"
"Cockpit / provenance"
"paused workstreams"
"high-risk procedures"
```

A grouping like these might be a materialized view or navigation category rather than a first-class knowledge entity.

This is an important counterweight to ontology expansion:

> **Not everything that appears as a node in a user interface, directory, hierarchy or graph deserves durable semantic identity.**

## 5. Entity identity and appellation are explicitly separated in IFLA LRM

**Primary source:** IFLA, *IFLA Library Reference Model*.

URL: https://www.ifla.org/files/assets/cataloguing/frbr-lrm/ifla-lrm-august-2017_rev201712.pdf

LRM separates a thing (`Res`) from its appellations (`Nomen`). One res may have multiple nomens; the same literal string can refer to different res; equivalent nomens can differ in language, scheme, audience or context of use.

That distinction is deeper than allowing aliases. It says that the **reference object and the name used to reach it are different modeled things**.

LRM also distinguishes Work, Expression, Manifestation and Item and links them through explicit relationships. The exact bibliographic decomposition does not transfer directly to project knowledge, but it provides mature precedent for separating intellectual identity from expression and embodiment.

**Transfer:** Filename, heading, slug, human-friendly label and semantic identity should be treated as potentially different concerns. A file relocation or title change should not automatically imply a new knowledge identity when the project still regards the underlying thing as continuous.

## 6. Information identity can survive changes of carrier

### 6.1 ICA Records in Contexts

**Primary source:** International Council on Archives, *Records in Contexts Ontology (RiC-O) 1.1*.

URL: https://www.ica.org/standards/RiC/RiC-O_1-1.html

RiC distinguishes `RecordResource` from `Instantiation`. A Record Resource is retained information produced or acquired through activity; an Instantiation is a persistent inscription/carrier of that information. A Record Resource may have multiple instantiations simultaneously or through time, and an instantiation may later disappear while the record resource remains describable.

### 6.2 CIDOC CRM

**Primary source:** CIDOC CRM, class E73 Information Object.

URL: https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html

CIDOC CRM's E73 Information Object is an identifiable immaterial item with recognizable structure that does not depend on one physical carrier and can exist on more than one carrier simultaneously.

**Transfer:** Durable project knowledge and the current file that carries it are conceptually separable. This does not mean the file becomes unimportant: an exact artifact can still be the authoritative expression/evidence for a claim. It means the architecture should not assume that semantic continuity and carrier continuity are identical.

## 7. Multi-membership and contextual grouping are mature patterns

RiC's `RecordSet` is particularly relevant to D2. Records can be grouped because of shared provenance, activity, subject, structure or a researcher's purpose. A record may simultaneously belong to more than one Record Set, and its memberships can change through time and context.

AAT independently demonstrates the same structural idea through polyhierarchy: one concept can appear under multiple broader contexts while existing only once in the vocabulary.

The convergence suggests:

```text
one semantic object
    -> zero, one or many contextual groups
    -> zero, one or many hierarchy positions
    -> one preferred/default route may exist for presentation
```

This is substantially different from a file-tree ontology in which physical placement defines semantic parenthood.

**Research 124 implication:** subject, domain, authority state, chronology, workstream, evidence depth and privacy boundary should be investigated as orthogonal grouping/view dimensions rather than forced into one primary tree.

## 8. Relationships may themselves carry knowledge

RiC-O provides both simple binary relations and first-class Relation instances. A Relation instance may carry its own:

```text
description
certainty
date
state
location
source / evidence
```

RiC explicitly recommends the richer form when a direct binary relation is insufficient.

Wikidata provides an operationally similar lesson at statement level. A statement can carry qualifiers, references and rank. Preferred, normal and deprecated rank allow several sourced values to coexist while downstream queries can default to the currently preferred/normal view. Wikidata also distinguishes a historically correct value whose applicability ended from a claim that should be deprecated because it is considered wrong or superseded.

**Primary Wikidata sources:**
- https://www.wikidata.org/wiki/Help:Data_model
- https://www.wikidata.org/wiki/Help:Ranking
- https://www.wikidata.org/wiki/Help:Deprecation/en

**Transfer:** Some ADS relations may need more than source-node / predicate / target-node. Examples include:

```text
A supersedes B
workstream X returns to Y
finding F supports decision D
procedure P governs task class T
risk R reopens when condition C occurs
```

For such relations, date, state, certainty, source or authority may materially change the meaning.

**Important limit:** This does **not** justify reifying every edge or sentence. First-class relationship metadata should be reserved for relations whose own lifecycle, provenance or state matters to project reasoning.

## 9. Claim identity is a separate question from concept identity

The evidence is strongest for stable identity of enduring concepts/resources and weaker for turning every proposition into a first-class project object.

Wikidata demonstrates that statement-level metadata can be powerful when multiple sourced values, qualifiers and historical states matter. RiC demonstrates that relations deserve richer identity only when the direct edge is insufficient. Neither implies that every paragraph, sentence or extracted claim should receive a permanent ID.

A useful distinction for later candidate design is therefore:

```text
concept/resource identity
    strong external precedent

important assertion/decision/requirement identity
    plausible when it has independent lifecycle, authority or provenance

arbitrary sentence/fragment identity
    not justified by current evidence
```

This keeps D1 from turning into universal claim atomization before there is a demonstrated need.

## 10. Activities and workstreams may be entities distinct from their documentation

RiC models `Activity` separately from the records that document it. An Activity has purpose, process, context, change through time and possible subactivities; record resources may result from or document that activity.

The analogy is unusually relevant to ADS workstreams:

```text
Research 124 as an ongoing project activity/workstream
    !=
the Research 124 Markdown record
    !=
Checkpoint 464
    !=
the commits produced while executing it
```

Whether the successor should actually assign stable workstream entities is still an architecture question. The evidence establishes only that separating **activity identity** from **documentation of activity** is a mature and useful modeling move when continuation/control flow matters.

## 11. Candidate identity test for later architecture comparison

Research 126 does not freeze entity classes. It does establish an architecture-neutral test for deciding whether something is a plausible stable-identity candidate.

A thing becomes a stronger candidate for independent identity when several of the following are true:

```text
persistence
    it remains meaningfully the same when its label, path or representation changes

cross-context reference
    several artifacts, workstreams or views need to refer to the same thing

independent lifecycle
    it can be proposed, accepted, superseded, paused, merged, deprecated or retired
    independently of one carrier

multiple representations
    more than one file/view/expression can represent or describe it

relationship-bearing role
    important project relations attach to the thing itself rather than merely its current file

provenance need
    its origin, evidence or transformation history matters independently

identity-confusion risk
    conflating it with its label/carrier/group would create material loss or ambiguity
```

No fixed threshold is selected yet. Candidate architectures should show which classes pass this test and why.

## 12. Anti-test: what should normally *not* become a semantic entity

The external evidence also supports explicit restraint. The following should normally remain representations, labels or derived organization unless a concrete lifecycle/authority need proves otherwise:

```text
one UI card or navigation tile
a generated breadcrumb
an arbitrary paragraph or sentence
a temporary search result cluster
a display-only preferred path
a convenience heading
a cache entry or embedding row
a generated context packet
an organizational node whose only job is grouping/presentation
```

A file is also not automatically a semantic concept. Exact files can still require stable **artifact identity** for provenance or authority, but artifact identity and semantic knowledge identity are separate concerns.

## 13. Minimal candidate semantic families to compare later

The evidence justifies evaluating a small typed semantic substrate, but not selecting one. To prevent unconstrained ontology growth, later candidate architectures should first test whether a minimal set of roles can cover the project:

```text
SUBJECT / CONCEPT
    what the project is talking about

KNOWLEDGE UNIT
    an independently governed decision, requirement, finding, question,
    risk/limitation or other proposition-like unit when it passes the identity test

ACTIVITY / WORKSTREAM
    purposeful project work with lifecycle, dependencies and resume semantics

EVIDENCE / SOURCE
    material used to support, test or document knowledge

REPRESENTATION / ARTIFACT
    file, record, generated view or other concrete carrier/expression

RELATION
    usually lightweight, promoted to a richer object only when its own
    provenance/state/time/certainty matters
```

This is a **comparison envelope**, not the target ontology. A candidate with fewer types may be superior if it satisfies the requirements; a candidate with more types must earn the added complexity.

## 14. D2 view model: several projections over the same underlying identities

The evidence supports evaluating views such as:

```text
semantic view
    concepts / knowledge units and their subject relationships

authority view
    current / candidate / superseded / rejected / unresolved

workstream view
    active / paused / blocked / parent-child / dependency / return target

provenance view
    derived-from / evidence-for / generated-by / validated-by

temporal view
    applicable now / historically applicable / learned-recorded later

artifact view
    exact files, code, validations and representations

reconstruction view
    task-specific project -> domain -> governing source -> evidence traversal

privacy/access view
    public authority versus explicitly delegated private continuity facts
```

A view can select, order and emphasize the same underlying entities differently. This is closer to AAT's preferred-parent-as-display-default and RiC's context-specific sets than to duplicating one object into several independent truth systems.

## 15. A default route can exist without becoming semantic truth

One practical concern is whether multi-axis organization eliminates deterministic navigation. The evidence says no.

AAT designates one parent as preferred even though all parents remain valid for retrieval. IFLA LRM similarly allows preferred forms of nomen for a context without treating other nomens as different underlying entities.

Research 124 can therefore preserve a deterministic default reconstruction path while allowing richer semantic membership:

```text
one preferred route for ordinary continuation
    !=
one exclusive semantic parent
```

This distinction may be essential for combining reliable bootstrap behavior with broad semantic organization.

## 16. Identity merge and split are governance problems, not clerical edits

Stable identity introduces a new risk: deciding incorrectly that two records refer to the same thing.

Getty's vocabulary practice preserves merge mappings and warns editors to merge only when records truly represent the same entity. Wikidata and knowledge-organization systems similarly depend on careful entity resolution.

For ADS this means a successor with semantic IDs would need explicit semantics for:

```text
rename
    same identity, new label

move / regroup
    same identity, different view membership

merge
    two identities determined to represent one thing; aliases/redirects retained

split
    one prior identity determined to conflate distinct things

supersede
    old knowledge remains historically identifiable but is no longer current authority

replace representation
    semantic identity may remain while the carrier/artifact changes
```

These operations are conceptually different and should not be collapsed into file renames or deletes.

## 17. ADS thought experiments

The evidence can now be applied to concrete project cases without deciding implementation.

### 17.1 Human-only vs human-plus-LLM vs ADS system-mediated development

This subject appears historically in a checkpoint, canonically in a foundation and semantically in the Knowledge Map. The deep dive suggests that the project should at least test whether there is a durable **subject/concept identity** behind those representations.

It does **not** follow that the checkpoint and foundation are the same knowledge object. They may be different historical/canonical knowledge units about the same subject.

### 17.2 Governing operational procedure

A runbook may move or be rewritten while remaining the governing procedure for the same task class. Separating procedure identity from current path could allow the activation mechanism to bind to a governed semantic identity while still resolving the exact current authoritative representation before use.

### 17.3 Workstream continuation

A paused workstream can have several research files, checkpoints and validation records. Treating the workstream/activity as distinct from those artifacts could make parent/child/dependency/resume semantics clearer.

### 17.4 Historical checkpoint

A checkpoint file is an exact durable artifact. It may also document a historical project-state transition/event. The artifact and the historical event should not automatically be assumed identical if later architecture needs to relate several representations/evidence items to the same event.

These are candidate interpretations to test, not migrations to perform now.

## 18. D1-D2 architecture-neutral conclusions

The deep dive is strong enough to freeze the following as **evidence-backed design constraints for later comparison**, subject to the later requirements/evidentiary-provenance reconciliation:

```text
D1-C1  Labels, filenames and paths must not be assumed to be semantic identity.

D1-C2  A successor must be able to preserve stable identity across representation
       change where the project deliberately regards the underlying thing as continuous.

D1-C3  Artifact identity and semantic knowledge identity are distinct concerns.

D1-C4  Not every sentence, file, relation or navigation node deserves a semantic ID.
       Identity granularity must be justified by lifecycle, reference, provenance or
       ambiguity-reduction value.

D1-C5  Merge, split, rename, regroup, supersession and representation replacement
       require distinguishable semantics if stable semantic identities are introduced.

D1-C6  Relationships whose own state, time, certainty, provenance or authority matters
       must be representable more richly than an unqualified edge.

D2-C1  One semantic object may participate in multiple contextual groups or hierarchies.

D2-C2  A preferred/default route may exist for deterministic navigation without becoming
       the object's exclusive semantic parent.

D2-C3  Organizational/view nodes need not be semantic knowledge entities.

D2-C4  Semantic, authority, workstream, provenance, temporal, artifact and reconstruction
       views should be evaluated as orthogonal projections rather than independent truths.

D2-C5  Multi-view architecture must preserve one explicit project-development authority
       and must not multiply manual synchronization obligations without bound.
```

## 19. What remains unresolved after D1-D2

The evidence does **not** yet determine:

```text
whether stable IDs should be files, URIs, database keys or another project-owned identifier
whether semantic objects live in Markdown, JSON, SQLite, a graph store or a hybrid
which candidate semantic families are actually necessary
whether assertions/claims deserve first-class IDs beyond selected governed knowledge units
whether relationships are stored directly or generated from source metadata
how conversation-born reasoning becomes one of those knowledge units
how generated views stay current and rebuildable
how much structure remains economical at 5x / 10x scale
```

Those open points deliberately lead into D3, D4 and later D7/D8 rather than target synthesis.

## 20. Next evidence boundary

D1 and D2 are now sufficiently researched to stop broadening them indiscriminately. Additional ontology examples are unlikely to change the main architectural conclusions without a more specific unresolved question.

The next deep dive should move to:

```text
D3  conversation-born capture -> consolidation -> promotion
D4  canonical source versus rebuildable derived state
```

These two questions should be researched together because capture and consolidation become unsafe if the architecture cannot distinguish transient/derived synthesis from promoted project authority.

The owner-provided paper/video remains withheld.

```text
RESEARCH126_D1_D2=COMPLETE
STABLE_IDENTITY_INDEPENDENT_OF_LABEL_OR_PATH=EVIDENCE_BACKED
MULTI_MEMBERSHIP_AND_MULTI_VIEW=EVIDENCE_BACKED
RELATION_METADATA=CONDITIONALLY_JUSTIFIED
UNIVERSAL_CLAIM_ATOMIZATION=NOT_JUSTIFIED
ONTOLOGY_OR_GRAPH_DATABASE=NOT_SELECTED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=D3_D4_CAPTURE_CONSOLIDATION_SOURCE_DERIVED_DEEP_DIVE
WITHHELD_OWNER_SOURCE=STILL_WITHHELD
```