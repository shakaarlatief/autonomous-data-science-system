# Research 125: Cross-Disciplinary External Evidence for Project Knowledge Architecture

**Date:** 2026-09-13
**Status:** ACTIVE / PHASE-1 CROSS-DISCIPLINARY EVIDENCE SYNTHESIS / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Build an independent external evidence field for Research 124 by examining information science, digital preservation, organizational memory, design rationale, human factors, software architecture, reproducible derived state, temporal data, and modern LLM memory/retrieval research. The goal is to expand the project-development knowledge-architecture design space rather than search for one ready-made solution.
**Authority:** Supporting evidence research under Research 124. This record does not select the target architecture, does not replace current project-development knowledge authority, and does not make external frameworks authoritative over ADS.
**Declared references:** `research:124`, `checkpoint:463`, `foundation:014`, `path:docs/KNOWLEDGE_MAP.md`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Why this research exists

Research 124 has now completed its internal failure corpus, historical ChatGPT baseline, and owner clarification that the redesign is a whole-architecture inquiry rather than a defect-patching exercise.

The next question is not:

```text
which external product looks most like our current repository?
```

It is:

> **What mature ideas from multiple disciplines should change how we think about durable project understanding, semantic organization, provenance, consolidation, activation, temporal truth, derived views, and task-shaped reconstruction?**

The evidence search therefore deliberately spans both AI and non-AI fields. At least one major evidence stream had to come from disciplines that solved long-lived knowledge, records, safety, or architecture-description problems before current LLM systems existed.

## 2. Evidence discipline

Every source below is treated as an analogy or transferable design principle only to the extent justified by its original domain.

```text
external framework observed
    !=
ADS successor architecture selected

useful vocabulary or mechanism
    !=
requirement to adopt its implementation technology

empirical result in another domain
    !=
direct proof for LLM project-development behavior
```

The research distinguishes:

```text
PRIMARY STANDARD / OFFICIAL MODEL
    normative or institutional reference material

PEER-REVIEWED RESEARCH
    empirical or conceptual work published in established venues

OFFICIAL ENGINEERING GUIDANCE
    practitioner architecture guidance from a responsible platform/vendor

RECENT AI RESEARCH
    relevant modern memory/retrieval work whose authority and stability are weaker than mature standards
```

## 3. Knowledge identity, semantic organization, and multiple views

### 3.1 W3C SKOS: concepts can have identity independent of labels

**Source:** W3C, *SKOS Simple Knowledge Organization System Reference*.

URL: https://www.w3.org/TR/skos-reference/

**Evidence class:** PRIMARY STANDARD / W3C Recommendation.

SKOS defines a `Concept` as an idea or notion, a unit of thought. Concepts can have preferred, alternative, and hidden labels, while semantic relationships such as broader, narrower, and related connect concepts independently of any one textual label.

**Plausible transfer to Research 124:** Important project knowledge may benefit from identity that is not identical to the filename or current title of the artifact containing it. The same durable concept can plausibly survive renaming, representation change, or multiple views while preserving a stable semantic identity.

**Transfer limit:** This does not imply that ADS should use RDF, SKOS, or a formal ontology. SKOS is evidence for separating conceptual identity from labels and for explicit semantic relations, not a target implementation decision.

### 3.2 IFLA Library Reference Model: organize information around user tasks and relationships

**Source:** IFLA, *IFLA Library Reference Model*, current repository edition surfaced in 2024.

URL: https://repository.ifla.org/rest/api/core/bitstreams/7d23aa55-1f85-490f-b500-6170285585a6/content

**Evidence class:** PRIMARY DOMAIN REFERENCE MODEL.

IFLA LRM distinguishes user tasks including Find, Identify, Select, Obtain, and Explore. Explore is explicitly relationship-driven and contextual: users may browse, make unexpected connections, and become familiar with a collection for future use.

**Plausible transfer:** Project-knowledge architecture should be evaluated by the different tasks collaborators perform, not by whether one structure is elegant in isolation. Broad orientation, exact evidence retrieval, authority resolution, historical reconstruction, and exploratory discovery are different task classes and may deserve different routes or views.

**Transfer limit:** Bibliographic entities and library users are not project-development knowledge. LRM contributes task-centered modeling and relationship-aware exploration, not a project ontology to copy.

### 3.3 Flamenco: faceted navigation allows several organizational axes at once

**Source:** UC Berkeley, *Flamenco Search Interface Project*.

URL: https://flamenco.berkeley.edu/

**Evidence class:** RESEARCH SYSTEM / INFORMATION RETRIEVAL AND HCI.

Flamenco combines hierarchical faceted metadata with free-text search so users can refine and expand queries while maintaining context in a large information space.

**Plausible transfer:** The successor should not assume that one hierarchy must simultaneously carry subject, chronology, authority, workstream, evidence depth, and artifact type. Multiple orthogonal facets may be more robust than forcing every knowledge item into one tree.

**Transfer limit:** Flamenco is primarily a navigation/interface result. It does not solve project authority, provenance, supersession, or required-source activation.

### 3.4 Furnas et al.: vocabulary mismatch is fundamental

**Source:** Furnas, Landauer, Gomez, and Dumais, *The Vocabulary Problem in Human-System Communication*, Communications of the ACM, 1987.

DOI: https://doi.org/10.1145/32206.32212

**Evidence class:** PEER-REVIEWED CLASSIC HCI/IR RESEARCH.

The study found surprisingly large variability in spontaneous word choice for the same targets. Systems that require users to guess one exact term are therefore fragile.

**Plausible transfer:** Exact filenames, one canonical subject label, or a single controlled vocabulary should not be the only route to project knowledge. Aliases, lexical search, semantic relationships, structured metadata, and possibly embeddings can complement one another.

**Transfer limit:** Human naming variability is not the same as LLM retrieval behavior. The result supports multiple lexical access paths, not any specific retrieval stack.

### 3.5 ISO/IEC/IEEE 42010 and SEI Views & Beyond: one underlying thing can require multiple concern-shaped views

**Sources:**
- ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise - Architecture description*. https://www.iso.org/standard/74393.html
- Software Engineering Institute, *Views and Beyond Collection*. https://www.sei.cmu.edu/library/views-and-beyond-collection/

**Evidence class:** INTERNATIONAL STANDARD + ESTABLISHED SOFTWARE-ARCHITECTURE GUIDANCE.

ISO 42010 distinguishes an architecture from its architecture description and formalizes viewpoints/model kinds used to address different concerns. SEI's Views & Beyond treats views as a fundamental organization principle and emphasizes choosing relevant views based on anticipated use.

**Plausible transfer:** A project-knowledge substrate may support several task-shaped projections rather than one monolithic universal document. A current-state view, semantic-domain view, provenance view, workstream view, and evidence view could all be projections over overlapping underlying knowledge.

**Transfer limit:** Architecture-description practice concerns documenting software/system architectures, not maintaining all project-development knowledge. The transferable principle is concern-shaped representation, not its exact documentation templates.

## 4. Provenance, preservation, and future interpretability

### 4.1 W3C PROV-O: provenance is a relationship model, not a footnote

**Source:** W3C, *PROV-O: The PROV Ontology*.

URL: https://www.w3.org/TR/prov-o/

**Evidence class:** PRIMARY STANDARD / W3C Recommendation.

PROV-O models Entity, Activity, and Agent plus explicit relationships such as `wasGeneratedBy`, `wasDerivedFrom`, `used`, `wasAttributedTo`, `wasRevisionOf`, and `hadPrimarySource`.

**Plausible transfer:** Research 124 should consider provenance, derivation, revision, responsibility, and primary-source relationships as first-class machine-readable relations rather than relying only on narrative references between files.

**Transfer limit:** PROV-O does not define ADS authority levels, promotion rules, task routing, or canonical-source policy. It supplies vocabulary and a modeling precedent.

### 4.2 OAIS: preserving bytes is not preserving meaning

**Source:** CCSDS 650.0-M-3, *Reference Model for an Open Archival Information System (OAIS)*, Issue 3, December 2024.

URL: https://ccsds.org/Pubs/650x0m3.pdf

**Evidence class:** PRIMARY INTERNATIONAL PRESERVATION REFERENCE MODEL.

OAIS distinguishes a content object from the Representation Information required to make it understandable. Representation Information can include structural, semantic, software, algorithmic, and instructional material. OAIS also requires Preservation Description Information around reference, context, provenance, fixity, and access rights. Separately, Descriptive Information can act as an index/access aid and is generally derived from deeper preserved information.

**Plausible transfer:** Durable project knowledge must preserve enough context and semantics for a future collaborator to interpret it, not merely keep Markdown bytes alive. The separation between deeply preserved information and derived descriptive access aids is especially relevant to source-authoritative plus rebuildable-view designs.

**Transfer limit:** OAIS is designed for long-term archival preservation, not an actively changing software/research project. Its categories should inform requirements, not be imported wholesale.

### 4.3 PREMIS: preservation events and responsibility can be explicit

**Source:** Library of Congress, *PREMIS Data Dictionary for Preservation Metadata, Version 3.0*.

URL: https://www.loc.gov/standards/premis/v3/

**Evidence class:** PRIMARY PRESERVATION METADATA STANDARD.

PREMIS models Objects, Events, Rights, and Agents, including identifiers, event outcomes, links between events and objects, and agent roles. Version 3 also supports intellectual-entity-level representation within the object model.

**Plausible transfer:** Important transformations of project knowledge, such as consolidation, migration, promotion, supersession, regeneration, or repair, could have explicit event/provenance records instead of being inferable only from Git diffs or prose.

**Transfer limit:** PREMIS optimizes preservation metadata, not active reasoning or project navigation.

### 4.4 Records Continuum: current use and preservation need not be separate life phases

**Sources:**
- Society of American Archivists, *records continuum*. https://dictionary.archivists.org/entry/records-continuum.html
- Frings-Hessami, Archival Science work on the Records Continuum Model and its Create, Capture, Organise, Pluralise dimensions.

**Evidence class:** ESTABLISHED ARCHIVAL THEORY / PEER-REVIEWED SYNTHESIS.

The records-continuum perspective treats creation, capture, organization, and broader reuse as overlapping dimensions rather than a simple linear transition from active record to archive.

**Plausible transfer:** Project history does not need to become semantically dead once immediate work closes. Knowledge can simultaneously serve current work, provenance, accountability, and later reinterpretation. Preservation requirements can be designed at capture time rather than added only after work finishes.

**Transfer limit:** This is archival/recordkeeping theory. It should widen our reasoning about lifecycle and reuse, not prescribe repository mechanics.

## 5. Organizational memory and conversation-born rationale

### 5.1 Ackerman and Halverson: organizational memory is both object and process

**Source:** Ackerman and Halverson, *Considering an Organization's Memory*, CSCW 1998.

URL: https://web.eecs.umich.edu/~ackerm/pub/98b24/cscw98.om.html

**Evidence class:** PEER-REVIEWED CSCW RESEARCH.

Their ethnographic analysis argues that organizational memory is better understood through both stored artifacts and the work processes through which memory is created, interpreted, and used.

**Plausible transfer:** Research 124 should avoid reducing project memory to a storage repository. Capture, consolidation, routing, activation, interpretation, and escalation are part of the memory architecture.

**Transfer limit:** Organizational work groups differ from LLM-mediated software projects, but the object-plus-process distinction transfers cleanly at the conceptual level.

### 5.2 Answer Garden: stored knowledge can escalate to a knowledgeable actor

**Source:** Ackerman and Malone, *Answer Garden: A Tool for Growing Organizational Memory*, ACM COIS 1990, plus later field-study work.

DOI: https://doi.org/10.1145/91474.91485

**Evidence class:** PEER-REVIEWED CSCW / ORGANIZATIONAL MEMORY.

Answer Garden combined retrieval of recorded answers with routing to people when the repository could not answer the question.

**Plausible transfer:** Fail-visible escalation is a legitimate memory-system behavior. The project-development knowledge architecture should be allowed to say that required knowledge is absent, ambiguous, or needs owner/domain input rather than forcing every gap through probabilistic synthesis.

**Transfer limit:** Human expert routing is not identical to ADS escalation. The useful idea is graceful escalation when memory is incomplete.

### 5.3 Design-rationale research: capture reasoning with low disruption

**Sources:**
- Conklin and Yakemovic, *A Process-Oriented Approach to Design Rationale*, Human-Computer Interaction 6, 1991. https://doi.org/10.1080/07370024.1991.9667172
- Bracewell, Wallace, Moss, and Knott, *Capturing design rationale*, Computer-Aided Design 41(3), 2009. https://doi.org/10.1016/j.cad.2008.10.005

**Evidence class:** PEER-REVIEWED DESIGN-RATIONALE RESEARCH.

IBIS-style work captures issues, options, arguments, and decisions as reasoning unfolds. Conklin and Yakemovic report an industrial trial capturing more than 2,300 requirements/design decisions; DRed was designed as a simple, unobtrusive graph of issues, options, and pro/con arguments in aerospace engineering.

**Plausible transfer:** Important conceptual discussion does not need to wait until it naturally fits a final Research, Foundation, or Specification artifact. A successor may need a low-friction capture layer followed by deliberate distillation/promotion into durable synthesis.

**Transfer limit:** Structured rationale capture creates maintenance and interaction cost. If capture is burdensome, people and models will bypass it. Raw dialogue structure should not automatically become project authority.

## 6. Activation, forcing functions, and resume reliability

### 6.1 NASA checklist research: availability is weaker than workflow integration

**Source:** Degani and Wiener, *Human Factors of Flight-Deck Checklists: The Normal Checklist*, NASA Contractor Report 177549, 1990/1991.

URL: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19910017830.pdf

**Evidence class:** GOVERNMENT HUMAN-FACTORS RESEARCH.

The report examines checklist functions, format, design, length, usage, human limitations, organizational culture, and production pressure, noting that improper use or non-use can contribute to accidents.

**Plausible transfer:** Merely storing a correct procedure is weaker than embedding required checks in the workflow and designing them for actual use conditions. This directly supports treating governing-source activation as a sociotechnical/control problem, not only a retrieval problem.

**Transfer limit:** Aviation safety behavior is not evidence about LLM cognition. The transfer is about process design and forcing functions.

### 6.2 FDA human factors: design should reduce dependence on manuals and retraining

**Source:** U.S. FDA, *Human Factors and Medical Devices*.

URL: https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/human-factors-and-medical-devices

**Evidence class:** OFFICIAL SAFETY/USABILITY GUIDANCE.

FDA frames human-factors engineering around minimizing use-related risk and explicitly lists reduced reliance on manuals, reduced training/retraining, and reduced use error among beneficial outcomes.

**Plausible transfer:** A robust project-development environment should make correct behavior easier through system/interface structure rather than depending on the collaborator remembering that documentation exists.

**Transfer limit:** Medical-device regulation is not project-knowledge design. The relevant transfer is the design philosophy of reducing reliance on memory/manual lookup for critical behavior.

### 6.3 Goal-memory and interruption research: resume cues matter

**Sources:**
- Altmann and Trafton, *Memory for goals: an activation-based model*, Cognitive Science 26(1), 2002. https://doi.org/10.1207/s15516709cog2601_2
- Dodhia and Dismukes, *Interruptions create prospective memory tasks*, Applied Cognitive Psychology 23(1), 2009. https://doi.org/10.1002/acp.1441

**Evidence class:** PEER-REVIEWED COGNITIVE SCIENCE / HUMAN FACTORS.

Altmann and Trafton model goal retrieval in terms of activation and associative priming, including the importance of cues. Dodhia and Dismukes show how interruption can impair encoding of an intention to resume and later interpretation of resumption cues.

**Plausible transfer:** Explicit resume targets, return conditions, parent relationships, and distinctive resumption cues are better design primitives than expecting an interrupted collaborator to reconstruct latent intent from prose history.

**Transfer limit:** These are human cognitive models. They justify explicit externalized cues for human/project workflows but do not prove equivalent internal mechanisms in LLMs.
