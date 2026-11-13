from pathlib import Path
from hashlib import sha256
from collections import Counter
import sys,json,re
from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import original_contents, PIN
AUTHOR_FROZEN_ASSIGNMENT_ROWS = "development-governance|temporal-currentness,owner-approval-boundary\ndevelopment-governance|temporal-currentness,owner-approval-boundary\nevaluation-assurance|execution-reproducibility\ncockpit-implementation,cockpit-interaction|execution-reproducibility\ntooling-integrations,evaluation-assurance|execution-reproducibility\ntooling-integrations,development-governance|source-evidence-integrity\ndevelopment-governance,tooling-integrations|owner-approval-boundary,source-evidence-integrity\nproject-knowledge-architecture,evaluation-assurance|migration-compatibility\nproject-knowledge-architecture|migration-compatibility,owner-approval-boundary\nproject-knowledge-architecture|temporal-currentness,owner-approval-boundary\nproject-knowledge-architecture|migration-compatibility,source-evidence-integrity\ndevelopment-governance|owner-approval-boundary,temporal-currentness\nevaluation-assurance|execution-reproducibility\nknowledge-representation,evaluation-assurance|source-evidence-integrity\nknowledge-representation,evaluation-assurance|source-evidence-integrity\nknowledge-representation,evaluation-assurance|owner-approval-boundary\nevaluation-assurance|execution-reproducibility\ndevelopment-governance,evaluation-assurance|source-evidence-integrity\ndevelopment-governance,evaluation-assurance|execution-reproducibility,owner-approval-boundary\ndevelopment-governance|owner-approval-boundary,temporal-currentness\ndevelopment-governance,evaluation-assurance|source-evidence-integrity,owner-approval-boundary\nevaluation-assurance|execution-reproducibility\nretrieval-context,methodological-knowledge|source-evidence-integrity\nknowledge-representation,methodological-knowledge|temporal-currentness\nsource-universe,evaluation-assurance|source-evidence-integrity\ncockpit-product,cockpit-visual-language|migration-compatibility\nruntime-persistence,tooling-integrations|execution-reproducibility\ntooling-integrations,development-governance|owner-approval-boundary\nproject-knowledge-architecture,development-governance|migration-compatibility,source-evidence-integrity\nproject-knowledge-architecture|source-evidence-integrity\nproject-knowledge-architecture,retrieval-context|source-evidence-integrity\nproject-orchestration,evaluation-assurance|execution-reproducibility\nevaluation-assurance|execution-reproducibility\nknowledge-representation,evaluation-assurance|owner-approval-boundary,source-evidence-integrity\nevaluation-assurance|execution-reproducibility\nproject-knowledge-architecture,knowledge-representation|migration-compatibility,owner-approval-boundary\nknowledge-representation,evaluation-assurance|source-evidence-integrity\nknowledge-representation,evaluation-assurance|source-evidence-integrity\nknowledge-representation,evaluation-assurance|source-evidence-integrity\nknowledge-representation,evaluation-assurance|execution-reproducibility\nproject-knowledge-architecture,development-governance|migration-compatibility\nproject-knowledge-architecture,development-governance|owner-approval-boundary\nevaluation-assurance,development-governance|owner-approval-boundary,execution-reproducibility\nevaluation-assurance,development-governance|execution-reproducibility\nevaluation-assurance,development-governance|source-evidence-integrity\nevaluation-assurance|source-evidence-integrity\nevaluation-assurance,tooling-integrations|owner-approval-boundary\nevaluation-assurance,model-collaboration|source-evidence-integrity\nevaluation-assurance|source-evidence-integrity\ntooling-integrations|owner-approval-boundary\nretrieval-context,evaluation-assurance|source-evidence-integrity\nretrieval-context|temporal-currentness\nrecommendation-action|owner-approval-boundary\ntooling-integrations|owner-approval-boundary,execution-reproducibility\ndevelopment-governance|source-evidence-integrity,temporal-currentness\nproject-knowledge-architecture|migration-compatibility,source-evidence-integrity\nproject-knowledge-architecture|source-evidence-integrity\nproject-knowledge-architecture|source-evidence-integrity\nproject-knowledge-architecture|source-evidence-integrity\nproject-knowledge-architecture|temporal-currentness,owner-approval-boundary"
P=Path("experiments/r0_p03_navigation_probe")
baseline=json.loads((P/"route_b_primary_b0_baseline_result_v01.json").read_text(encoding="utf8"))
rows=[x for x in AUTHOR_FROZEN_ASSIGNMENT_ROWS.splitlines() if x]
assert len(rows)==60, len(rows)
assert len(baseline["build_sources"])==60
catalog_path=Path("experiments/project_knowledge_subject_navigation_t1_v02/subject_catalog_candidate_v02.json")
catalog_bytes=catalog_path.read_bytes()
catalog=json.loads(catalog_bytes)
vocabulary={v["id"] for v in catalog["subjects"] if v["assignable"]}
concerns={
"source-evidence-integrity":"Exact source artifacts, declared provenance, evidence sufficiency, or verification of original records",
"temporal-currentness":"Applicability over time, revised records, staleness, successor/effective-date distinction",
"execution-reproducibility":"Repeatable test/probe execution, attestation of test run state and retrievable results",
"owner-approval-boundary":"Required owner gate, permissible decision/effect, authorization limits and nonoperative scope",
"migration-compatibility":"Migration, successor compatibility, cutover boundaries or rollback of existing source/semantic carriers"
}
sources=original_contents(baseline["build_sources"])
old=json.loads(Path("experiments/project_knowledge_subject_navigation_t1_v02/corpus_annotations_v02.json").read_text())
prior={x["path"]:x for x in old["annotations"]}
out=[]
for p,line in zip(baseline["build_sources"],rows):
 subs,concs=line.split("|")
 subjects=subs.split(",") if subs else []
 topics=concs.split(",") if concs else []
 assert all(s in vocabulary for s in subjects),(p,subjects)
 assert all(t in concerns for t in topics),(p,topics)
 raw=sources[p];text=raw.decode("utf8")
 lines=text.splitlines()
 # Every editorial assignment carries an exact source-local witness, even
 # though interpreting that evidence as membership is a fallible author choice.
 topical=next(((n+1,l) for n,l in enumerate(lines[:90]) if l.startswith("**Scope:**")),
              next(((n+1,l) for n,l in enumerate(lines[:20]) if l.startswith("# ")),
                   (1,lines[0] if lines else "")))
 n,quote=topical
 h=next((l for l in lines if l.startswith("# ")),"")
 prior_assign=prior.get(p)
 out.append({
 "path":p,
 "source_git_revision":PIN,
 "source_sha256":sha256(raw).hexdigest(),
 "source_original_bytes":len(raw),
 "author_exposure":"coordinator_exposed_not_blind",
 "ownership":"EXPERIMENTAL_SOURCE_ADJACENT_ANNOTATION_NOT_SOURCE_AUTHORED",
 "subjects":subjects,
 "preferred_subject":subjects[0] if subjects else None,
 "concerns":topics,
 "primary_semantic_evidence":{
  "line":n,"verbatim_original_line":quote,"line_sha256":sha256(quote.encode()).hexdigest(),
  "original_heading":h
 },
 "historical_w5_same_path_annotation": (
   {"subjects":prior_assign["subjects"],"preferred_subject":prior_assign["preferred_subject"],
    "historical_revision":old["source_boundary"],"not_original_current_revision":True}
    if prior_assign else None),
 })
result={
 "id":"R0_P03_ROUTE_B_EXPOSED_SOURCE_ADJACENT_B1_B3_ANNOTATION_FREEZE_V01",
 "source_git_pin":PIN,
 "source_corpus":"route_b_primary_b0_baseline_result_v01.json",
 "source_vocabulary":"experiments/project_knowledge_subject_navigation_t1_v02/subject_catalog_candidate_v02.json",
 "vocabulary_sha256":sha256(catalog_bytes).hexdigest(),
 "subject_definition_count":len(vocabulary),
 "author_exposure":"EXPOSED_COORDINATOR_ALREADY_SAW_TWELVE_QUESTIONS_AND_BASELINE_RESULTS",
 "sampled_60_metadata_entries":out,
 "concern_vocabulary":{
  "status":"EXPERIMENTAL_PROPOSED_CROSS_CUTTING_NON_GOVERNING",
  "definitions":concerns
 },
 "cost":{
  "new_source_adjoining_subject_memberships":sum(len(x["subjects"]) for x in out),
  "new_source_adjoining_concern_memberships":sum(len(x["concerns"]) for x in out),
  "historically_annotated_carrier_overlap_at_prior_revision":sum(bool(x["historical_w5_same_path_annotation"]) for x in out),
  "all_source_subject_and_concern_assignments_exposed_coordinator_authored":True,
  "source_content_read_for_annotation":True
 },
 "limitations":[
  "Source-adjacent annotation is an experimental overlay, not governed source-owned metadata. No production source is edited.",
  "The coordinating annotator saw every twelve-task reference source and the B0 result before assigning subjects and concerns, so this is exploratory and can be biased.",
  "Source witness lines prove what the original carrier says, not that a selected subject or concern interpretation is correct.",
  "Historical W5 membership overlaps are informational only and source-bound to a different Git revision; no automatic promotion to current source-owned facts.",
  "The five concern IDs are task-independent proposed source-control concerns, not owner-governed accepted concern identities.",
  "A subject vocabulary contains no membership by itself; the 60 per-source experimental annotations are retained with carrier identity rather than in the catalog.",
  "No source is granted operative authority by its annotation; no independent relevance gold, heldout F1, or formal P03 score is obtained."
 ]
}
path=P/"route_b_primary_b1_b3_exposed_source_metadata_v01.json"
raw=(json.dumps(result,sort_keys=True,ensure_ascii=True,indent=2)+"\n").encode()
if path.exists():
 if path.read_bytes() != raw:
  raise ValueError("Source-adjacent authoring output differs from frozen original bytes")
else:
 with path.open("xb") as f:f.write(raw)
print("FROZEN_B1_B3_METADATA",len(raw),sha256(raw).hexdigest(),result["cost"],"VOCAB",result["vocabulary_sha256"])
