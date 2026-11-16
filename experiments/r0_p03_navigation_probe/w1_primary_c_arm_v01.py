"""Primary W1 B0-B3 distinct navigation treatments, fixed before fresh tasks.

World W1 was precommitted before source selection. This module consumes the
60 exact Git source blobs and the single shared experiment-only V03 S1
authority/evidence envelope. The user-visible source-response envelope is
bounded identically for B0/B1/B2/B3. Added metadata never becomes J1/J2,
accepted lineage, implementation compliance or an evaluator's reference.

B1: historic Research 217 controlled subject/facet catalog, polyhierarchy,
    preferred subject, independently authored W1 source-adjacent memberships.
B2: additional source-carrier -> governing contract EDITORIAL ABOUT links,
    without claiming that the source realizes, complies with or supersedes
    the governing target, with duplicate documentary links forbidden.
B3: independent crosscutting concern vocabulary, source-adjacent assignment.
B0: exact same source/semantic/lexical methods, without any added navigation.

An optional B4 neural arm is not created by substituting classical LSA.
No hidden query, reference, legacy gold, heldout identity or score is read.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import importlib.util
import json
import math
from pathlib import Path
import re
from typing import Any

from experiments.r0_p03_navigation_probe import (
    w1_freeze_v01 as w1,
    v03_r0_p03_actual_navigation_channels_unscored_v01 as pilot,
)

HERE = Path(__file__).resolve().parent
METADATA = HERE / "w1_c_arm_authored_navigation_metadata.json"
METADATA_SHA = "ddee9beeace236eb8d987c62e69b0bb15fac4c501a81266ac6fbdfbb00450871"
CATALOG = pilot.CATALOG_PATH
CATALOG_SHA = pilot.CATALOG_SHA256
PILOT_ARMS = ("B0", "B1", "B2", "B3")
INITIAL_K = 6
MAX_K = 8
MAX_QUERY_CHARS = 160
MAX_EXCERPT_CHARS_PER_SOURCE = 2800
MAX_TOTAL_EXCERPT_CHARS = INITIAL_K * MAX_EXCERPT_CHARS_PER_SOURCE
MAX_LINES_PER_EXCERPT = 20
BM25_K1 = pilot.K1
BM25_B = pilot.B
TOKEN = pilot.TOKEN
IDENTIFIER = pilot.IDENTIFIER


def canonical(value: Any) -> bytes:
    return w1.canonical(value)


def tokens(text: str) -> list[str]:
    return pilot.tokens(text)


def literal_sha(path: Path, expected: str) -> dict:
    body = path.read_bytes()
    if sha256(body).hexdigest() != expected:
        raise ValueError("W1_ARM_INPUT_HASH_DRIFT:" + path.name)
    return json.loads(body.decode("utf8"))


def _raw_sources() -> tuple[dict[str, bytes], dict]:
    raw = {k:p.read_bytes() for k,p in w1.OUTPUTS.items()}
    pinned = {
        "manifest": "b3e7de396f303fad1e14fe575d712693a784ab6732ced6e5667919bafdc5842e",
        "substrate": "457390b693bddaaa62a0f536c6c4c4afa690bb61a5ece8fd44c9c7f0681347ac",
        "exclusions": "61bcc3f2be2e6090c836e5eedfbe5e0bd14407f2ffdac51f673887164427a033",
    }
    if any(sha256(raw[k]).hexdigest()!=v for k,v in pinned.items()):
        raise ValueError("W1_ARM_SOURCE_WORLD_DRIFT")
    manifest=json.loads(raw["manifest"].decode("utf8"))
    if (
        manifest["classification"]!="WORLD_W1_BUILD_FROZEN_HELDOUT_RULE_FROZEN_NOT_DRAWN"
        or manifest["build_source_count"]!=60
        or manifest["heldout_draw_status"]!="NOT_DRAWN_PROHIBITED_UNTIL_POST_C_ARM"
        or manifest["contract"]["source_git_revision"]!=w1.PIN
        or manifest["score"] is not None
        or manifest["primary_gold"] is not None
    ):
        raise ValueError("W1_ARM_FORMAL_SOURCE_WORLD_NOT_AT_EXPECTED_PREFREEZE")
    return raw,manifest


def _index_passages(fulltext: str) -> list[tuple[Counter[str],int,bool]]:
    # Exact original full content, same 220/40 token policy as the 24-source
    # engineering prototype. No 12k-character source truncation.
    return [(Counter(words),len(words),heading)
            for words,heading in pilot._passages(fulltext)]


class FrozenW1Index:
    """Unbiased shared original-blob lexical index used by *all* arms."""

    def __init__(self, raw: dict[str,bytes]):
        self.core = w1.W1CommonRuntime("B0",raw)
        self.documents=self.core.contents
        self.manifest=self.core.manifest
        self.rows=self.core.rows
        self.passages=[]
        self.df=Counter()
        for path in sorted(self.documents):
            for frequencies,length,heading in _index_passages(self.documents[path]):
                self.passages.append((path,frequencies,length,heading))
                self.df.update(frequencies)
        if not self.passages:
            raise ValueError("W1_ARM_EMPTY_BM25_INDEX")
        self.avglen=sum(p[2] for p in self.passages)/len(self.passages)
        self.original_byte_count=sum(len(v.encode("utf8")) for v in self.documents.values())
        self.source_line_count=sum(len(v.splitlines()) for v in self.documents.values())
        self.common_documentary_edges={
            (source,target)
            for source,body in self.documents.items()
            for target in self.documents
            if source!=target and target in body
        }
        self._last_cache_query=None
        self._last_cache_rank=None

    def lexical_rank(self, query:str) -> list[tuple[str,float]]:
        if query==self._last_cache_query and self._last_cache_rank is not None:
            return self._last_cache_rank.copy()
        query_terms=set(tokens(query))
        if not query_terms:
            raise ValueError("W1_ARM_NO_INDEXABLE_QUERY_TERMS")
        n=len(self.passages)
        idfs={
            term:math.log(1.0+(n-self.df[term]+0.5)/(self.df[term]+0.5))
            for term in query_terms
        }
        scores=dict.fromkeys(self.documents,0.0)
        for path,tf,length,heading in self.passages:
            # Source score is the best passage, never a source-length bonus.
            score=0.0
            for term,idf in idfs.items():
                freq=tf.get(term,0)
                if freq:
                    score+=idf*freq*(BM25_K1+1.0)/(
                        freq+BM25_K1*(1.0-BM25_B+BM25_B*length/self.avglen)
                    )
            if heading:
                score*=1.12
            if score>scores[path]:
                scores[path]=score
        exact_ids=[m.lower() for m in IDENTIFIER.findall(query)]
        if exact_ids:
            for path,body in self.documents.items():
                if any(key in body.casefold() for key in exact_ids):
                    scores[path]+=0.5
        result=sorted(scores.items(),key=lambda r:(-r[1],r[0]))
        self._last_cache_query=query
        self._last_cache_rank=result
        return result.copy()

    def literal_excerpt(self,path:str,query:str) -> dict:
        """Line-complete excerpts from the original source, not quoted truth."""
        lines=self.documents[path].splitlines()
        if not lines:
            raise ValueError("W1_ARM_EMPTY_ORIGINAL_SOURCE")
        terms=set(tokens(query))
        positions=[
            (sum(1 for term in terms if term in set(tokens(line))),i)
            for i,line in enumerate(lines)
        ]
        focus=max(positions,key=lambda q:(q[0],-q[1]))[1]
        # Deterministic bounded context around strongest lexical line.
        start=max(0,focus-5)
        selected=[]
        chars=0
        for i in range(start,min(len(lines),start+MAX_LINES_PER_EXCERPT)):
            line=lines[i]
            size=len(line)+1
            if size>MAX_EXCERPT_CHARS_PER_SOURCE:
                continue  # Don't quote a partial line as an exact assertion.
            if chars+size>MAX_EXCERPT_CHARS_PER_SOURCE:
                break
            selected.append({
                "line":i+1,"text":line,
                "line_sha256":sha256(line.encode("utf8")).hexdigest()
            })
            chars+=size
        if not selected:
            return {
                "source_path":path,"source_ref":w1.PIN,
                "git_blob_oid":self.rows[path]["git_blob_oid"],
                "complete_lines":[],"excerpt_characters":0,
                "source_full_read_available":True,
                "source_bounded_unknown":True,
            }
        return {
            "source_path":path,"source_ref":w1.PIN,
            "git_blob_oid":self.rows[path]["git_blob_oid"],
            "complete_lines":selected,"excerpt_characters":chars,
            "source_full_read_available":True,
            "source_bounded_unknown":True,
            "navigation_confers_governing_authority":False,
        }


class W1PrimaryArm:
    """Distinct controlled additions around one fully shared W1 read/search core."""

    def __init__(self,arm:str,index:FrozenW1Index,
                 meta:dict,catalog:dict):
        if arm not in PILOT_ARMS:
            raise ValueError("W1_ARM_NOT_BUILT_OR_UNKNOWN")
        self.arm=arm
        self.index=index
        self.core=w1.W1CommonRuntime(arm,{
            k:p.read_bytes() for k,p in w1.OUTPUTS.items()
        })
        self.meta=meta
        self.catalog=catalog
        self.operation_counts=Counter()
        self._validate()

    def _validate(self) -> None:
        m=self.meta
        rows=set(self.index.documents)
        catalog_ids={s["id"] for s in self.catalog["subjects"] if s["assignable"]}
        if (
            m["classification"]!="W1_PRETASK_EXPOSED_AUTHOR_CURATED_NON_GOVERNING_NAVIGATION"
            or m["original_source_git_ref"]!=w1.PIN
            or m["w1_manifest_sha256"]!=sha256(w1.OUTPUTS["manifest"].read_bytes()).hexdigest()
            or m["w1_substrate_sha256"]!=sha256(w1.OUTPUTS["substrate"].read_bytes()).hexdigest()
            or m["research217_catalog_sha256"]!=CATALOG_SHA
            or set(m["b1_subjects_by_source"])!=rows
            or set(m["b3_concerns_by_source"])!=rows
            or set(m["source_context_anchors"])!=rows
            or m["source_adjacent_coordinator_authorship"]["not_natural_owner_j2"] is not True
            or m["noncommon_authority"] is not False
            or m["primary_tasks"] is not None
            or m["formal_legacy_golden"] is not None
        ):
            raise ValueError("W1_ARM_METADATA_V03_SOURCE_OR_EXPOSURE_MISMATCH")
        for path,entry in m["b1_subjects_by_source"].items():
            subjects=entry["subjects"]
            if (
                not 1<=len(subjects)<=3 or len(set(subjects))!=len(subjects)
                or not set(subjects)<=catalog_ids
                or entry["preferred_subject"] not in subjects
            ):
                raise ValueError("W1_ARM_B1_INVALID_CONTROLLED_MEMBERSHIP")
        concern_vocab=set(m["concern_descriptions"])
        if concern_vocab & {s["id"] for s in self.catalog["subjects"]}:
            raise ValueError("W1_ARM_B3_RENAMED_B1_SUBJECT")
        for path,concerns in m["b3_concerns_by_source"].items():
            if not 1<=len(concerns)<=3 or not set(concerns)<=concern_vocab:
                raise ValueError("W1_ARM_B3_UNKNOWN_OR_UNBOUNDED_CONCERN")
        for path,anchor in m["source_context_anchors"].items():
            lines=self.index.documents[path].splitlines()
            i=anchor["source_line"]
            if (
                not 1<=i<=len(lines)
                or sha256(lines[i-1].encode("utf8")).hexdigest()!=anchor["source_line_sha256"]
                or anchor["source_ref"]!=w1.PIN
                or anchor["source_blob_oid"]!=self.index.rows[path]["git_blob_oid"]
                or anchor["witness_is_not_independent_label_verification"] is not True
            ):
                raise ValueError("W1_ARM_CURATORIAL_SOURCE_WITNESS_DRIFT")
        seen=set()
        for edge in m["b2_additional_editorial_links"]:
            pair=edge["source"],edge["governing_target"]
            if (
                pair in seen
                or pair in self.index.common_documentary_edges
                or pair[0]==pair[1]
                or pair[0] not in rows or pair[1] not in rows
                or self.index.rows[pair[1]]["stratum"]!="governing"
                or self.index.rows[pair[0]]["stratum"]=="governing"
                or edge["relation"]!="NON_GOVERNING_EDITORIAL_ABOUT_ONLY"
                or edge["claims_j1_j2_j3_implementation"] is not False
                or edge["source_owner_verified"] is not False
            ):
                raise ValueError("W1_ARM_B2_REDUNDANT_NOT_GOVERNING_OR_INVALID_EDGE")
            seen.add(pair)
        if len(seen)!=23:
            raise ValueError("W1_ARM_B2_EDITORIAL_EDGE_COUNT_DRIFT")

    def list_sources(self) -> list[str]:
        self.operation_counts["shared_list"]+=1
        return self.core.list_sources()

    def read(self,path:str) -> dict:
        self.operation_counts["shared_full_read"]+=1
        return self.core.read(path)

    def search(self,query:str,limit:int=5) -> list[dict]:
        self.operation_counts["shared_literal_search"]+=1
        return self.core.search(query,limit)

    def semantics(self) -> dict:
        self.operation_counts["shared_semantic_read"]+=1
        return self.core.semantics()

    def browse_subject(self,subject_id:str) -> dict:
        if self.arm!="B1":
            raise ValueError("W1_ARM_NO_SUBJECT_BROWSER")
        subjects={v["id"]:v for v in self.catalog["subjects"]}
        if subject_id not in subjects:
            raise ValueError("W1_ARM_UNKNOWN_SUBJECT_ID")
        parents={s["id"]:set(s["broader"]) for s in self.catalog["subjects"]}
        def ancestors(member:str) -> set[str]:
            seen=set()
            visit=list(parents.get(member,[]))
            while visit:
                node=visit.pop()
                if node not in seen:
                    seen.add(node)
                    visit.extend(parents.get(node,[]))
            return seen
        matched=[]
        for path,row in self.meta["b1_subjects_by_source"].items():
            found=[key for key in row["subjects"]
                   if key==subject_id or subject_id in ancestors(key)]
            if found:
                matched.append({
                    "source_path":path,"matching_memberships":found,
                    "preferred_subject":row["preferred_subject"],
                    "source_ref":w1.PIN,
                    "navigation_is_non_governing":True,
                })
        self.operation_counts["subject_browse"]+=1
        return {"subject_id":subject_id,"sources":sorted(
            matched,key=lambda r:r["source_path"]
        ),"relation":"W5_CONTROLLED_POLYHIERARCHY_NON_GOVERNING"}

    def browse_links(self,path:str) -> list[dict]:
        if self.arm!="B2":
            raise ValueError("W1_ARM_NO_EDITORIAL_BROWSER")
        if path not in self.index.rows:
            raise ValueError("W1_SOURCE_NOT_IN_FROZEN_BUILD")
        self.operation_counts["editorial_browse"]+=1
        return [x for x in self.meta["b2_additional_editorial_links"]
                if x["source"]==path]

    def browse_concern(self,tag:str) -> list[dict]:
        if self.arm!="B3":
            raise ValueError("W1_ARM_NO_CONCERN_BROWSER")
        if tag not in self.meta["concern_descriptions"]:
            raise ValueError("W1_ARM_UNKNOWN_CONCERN")
        self.operation_counts["concern_browse"]+=1
        return [
            {"source_path":path,"source_ref":w1.PIN,
             "navigation_is_non_governing":True}
            for path,values in self.meta["b3_concerns_by_source"].items()
            if tag in values
        ]

    def _subject_adjustment(self,terms:set[str]) -> dict[str,float]:
        self.operation_counts["subject_rank"]+=1
        matched={}
        for item in self.catalog["subjects"]:
            if not item["assignable"]:
                continue
            vocabulary=set(tokens(item["id"].replace("-"," ")+" "+item["label"]))
            matched[item["id"]]=len(terms & vocabulary)/max(1,len(vocabulary))
        return {
            path:sum(2.0*matched.get(subject,0.0) for subject in row["subjects"])
            for path,row in self.meta["b1_subjects_by_source"].items()
        }

    def _editorial_adjustment(self,baseline:list[tuple[str,float]]) -> dict[str,float]:
        self.operation_counts["editorial_rank"]+=1
        positions={path:i for i,(path,_) in enumerate(baseline[:12])}
        boost=dict.fromkeys(self.index.documents,0.0)
        for edge in self.meta["b2_additional_editorial_links"]:
            if edge["source"] in positions:
                boost[edge["governing_target"]]+=2.0/(1+positions[edge["source"]])
        return boost

    def _concern_adjustment(self,terms:set[str]) -> dict[str,float]:
        self.operation_counts["concern_rank"]+=1
        vocab=self.meta["concern_descriptions"]
        matched={
            tag:len(terms & set(tokens(tag.replace("-"," ")+" "+description)))
                /max(1,len(terms))
            for tag,description in vocab.items()
        }
        return {
            path:sum(1.7*matched[tag] for tag in assigned)
            for path,assigned in self.meta["b3_concerns_by_source"].items()
        }

    def rank(self,query:str,*,limit:int=INITIAL_K) -> list[dict]:
        if not isinstance(query,str) or not query.strip() or len(query)>MAX_QUERY_CHARS:
            raise ValueError("W1_ARM_INVALID_QUERY")
        if type(limit) is not int or not 1<=limit<=MAX_K:
            raise ValueError("W1_ARM_RESULT_LIMIT")
        self.operation_counts["lexical_rank"]+=1
        baseline=self.index.lexical_rank(query)
        if self.arm=="B0":
            bonuses={}
        elif self.arm=="B1":
            bonuses=self._subject_adjustment(set(tokens(query)))
        elif self.arm=="B2":
            bonuses=self._editorial_adjustment(baseline)
        else:
            bonuses=self._concern_adjustment(set(tokens(query)))
        ranked=sorted(
            ((p,score+bonuses.get(p,0.0)) for p,score in baseline),
            key=lambda item:(-item[1],item[0]),
        )
        return [{
            "rank":i+1,"source_path":p,"source_ref":w1.PIN,
            "git_blob_oid":self.index.rows[p]["git_blob_oid"],
            "navigation_score":round(score,6),
            "navigation_confers_authority":False,
        } for i,(p,score) in enumerate(ranked[:limit])]

    def context_pack(self,query:str,*,limit:int=INITIAL_K) -> dict:
        """Fixed read/context envelope for future independent scored sessions.

        A coordinator can generate answer packets after *fresh* task authorship.
        Generated packets do not interpret truth, cannot modify source authority,
        and must not substitute for the protected independent reference.
        """
        if type(limit) is not int or not 1<=limit<=INITIAL_K:
            raise ValueError("W1_ARM_CONTEXT_PACK_BUDGET")
        results=self.rank(query,limit=limit)
        snippets=[self.index.literal_excerpt(row["source_path"],query)
                  for row in results]
        size=sum(x["excerpt_characters"] for x in snippets)
        if size>MAX_TOTAL_EXCERPT_CHARS:
            raise ValueError("W1_ARM_CONTEXT_BUDGET_EXCEEDED")
        self.operation_counts["context_pack"]+=1
        return {
            "arm":self.arm,"query":query,"source_git_ref":w1.PIN,
            "common_source_semantic_digest":self.core.common_digest(),
            "source_candidates":results,"exact_source_line_snippets":snippets,
            "excerpts_total_characters":size,
            "per_source_excerpt_cap":MAX_EXCERPT_CHARS_PER_SOURCE,
            "total_excerpt_cap":MAX_TOTAL_EXCERPT_CHARS,
            "sources_count":len(snippets),
            "derived_index_or_ranking_confers_authority":False,
            "evidence_not_independent_gold":True,
        }

    def authored_metadata_cost(self) -> dict:
        if self.arm=="B0":
            counts={"authored_subject_memberships":0,"preferred_subject_routes":0,
                    "author_created_editorial_links":0,"authored_concern_memberships":0,
                    "authored_concern_definitions":0}
            selected={}
        elif self.arm=="B1":
            v=self.meta["b1_subjects_by_source"]
            counts={"authored_subject_memberships":sum(len(x["subjects"]) for x in v.values()),
                    "preferred_subject_routes":len(v),"author_created_editorial_links":0,
                    "authored_concern_memberships":0,"authored_concern_definitions":0}
            selected={"subjects_by_source":v,"catalog_hash":CATALOG_SHA}
        elif self.arm=="B2":
            v=self.meta["b2_additional_editorial_links"]
            counts={"authored_subject_memberships":0,"preferred_subject_routes":0,
                    "author_created_editorial_links":len(v),
                    "authored_concern_memberships":0,"authored_concern_definitions":0}
            selected={"links":v}
        else:
            v=self.meta["b3_concerns_by_source"]
            counts={"authored_subject_memberships":0,"preferred_subject_routes":0,
                    "author_created_editorial_links":0,
                    "authored_concern_memberships":sum(map(len,v.values())),
                    "authored_concern_definitions":len(self.meta["concern_descriptions"])}
            selected={"concerns":v,"vocabulary":self.meta["concern_descriptions"]}
        return {
            **counts,
            "incremental_navigation_metadata_bytes_utf8":len(canonical(selected))
                if selected else 0,
            "manual_annotation_minutes":"NOT_MEASURED_NOT_ASSUMED_FREE",
            "historical_research217_taxonomy_and_membership_cost":"UNQUANTIFIED_REQUIRED",
            "generated_vs_authored":"CURATED_TAGS_AUTHOR_AUTHORED; SOURCE_ANCHORS_DERIVED",
            "recurring_cost":"NOT_YET_MEASURED_ON_HELDOUT",
        }


def check_environment_b4() -> dict:
    """Prospective omission if neural B4 is not a comparably qualified arm."""
    available={
        name:importlib.util.find_spec(name) is not None
        for name in ("torch","sentence_transformers","transformers")
    }
    return {
        "policy":"B4_OMITTED_PROSPECTIVELY_AT_W1_PRIMARY_C_ARM_FREEZE",
        "omission_basis":"CURRENT_REPOSITORY_PYTHON_ENVIRONMENT_HAS_NO_QUALIFIED_NEURAL_PROVIDER_OR_EQUALIZED_EMBEDDING_RUNTIME",
        "change_after_freeze":"REQUIRES_EXPLICIT_NEW_PROSPECTIVE_FREEZE_BEFORE_ANY_TASK_OR_SCORE_NOT_AN_AUTOMATIC_SWITCH",
        "checked_local_python_packages":available,
        "external_provider_availability":"NOT_INDEPENDENTLY_QUALIFIED",
        "classical_lsa_is_not_neural_b4":True,
        "no_comparative_embedding_score_was_observed":True,
        "original_research513_conditional_b4_clause_kept":True,
        "neural_models_ruled_out_globally":False,
    }


def make_frozen() -> tuple[dict,dict,dict,dict[str,W1PrimaryArm]]:
    raw,manifest=_raw_sources()
    meta=literal_sha(METADATA,METADATA_SHA)
    catalog=literal_sha(CATALOG,CATALOG_SHA)
    index=FrozenW1Index(raw)
    arms={key:W1PrimaryArm(key,index,meta,catalog) for key in PILOT_ARMS}
    hashes={key:a.core.common_digest() for key,a in arms.items()}
    if len(set(hashes.values()))!=1 or len(index.documents)!=60:
        raise ValueError("W1_ARM_COMMON_WORLD_MISMATCH")
    base=arms["B0"]
    for key,a in arms.items():
        if key!="B0" and (
            a.core.list_sources()!=base.core.list_sources()
            or a.core.semantics()!=base.core.semantics()
            or a.core.read("docs/DECISIONS.md")!=base.core.read("docs/DECISIONS.md")
            or a.core.search("source",limit=3)!=base.core.search("source",limit=3)
        ):
            raise ValueError("W1_ARM_SHARED_SOURCE_AND_SEMANTICS_NOT_EQUAL")
    costs={key:a.authored_metadata_cost() for key,a in arms.items()}
    contract={
        "schema_version":1,
        "classification":"W1_PRIMARY_B0_B3_ARM_IMPL_AND_METADATA_PREFREEZE",
        "w1_rule_git":w1.RULE_COMMIT,
        "original_source_git":w1.PIN,
        "w1_manifest_sha256":sha256(raw["manifest"]).hexdigest(),
        "w1_substrate_sha256":sha256(raw["substrate"]).hexdigest(),
        "catalog_sha256":CATALOG_SHA,
        "additional_metadata_sha256":METADATA_SHA,
        "common_source_semantic_digest":next(iter(hashes.values())),
        "common_original_source_count":len(index.documents),
        "common_original_source_bytes":index.original_byte_count,
        "common_original_source_lines":index.source_line_count,
        "common_bm25_passage_count":len(index.passages),
        "common_documentary_path_mentions":len(index.common_documentary_edges),
        "common_capabilities":["source_list","exact_original_blob_read",
                               "literal_line_search","source_relative_evidence",
                               "non_governing_derived_orientation","bm25_full_text"],
        "per_arm_distinct_additions":{
            "B0":"NONE_COMMON_ONLY",
            "B1":"W5_18_SUBJECT_CONTROLLED_POLYHIERARCHY_WITH_PREFERRED_ROUTES",
            "B2":"SOURCE_CARRIER_TO_GOVERNING_EXTRA_EDITORIAL_ABOUT_LINKS",
            "B3":"CROSSCUTTING_CONCERNS_INDEPENDENT_OF_W5_SUBJECT_CATALOG",
        },
        "costs_not_quality_scores":costs,
        "equalized_context_budget":{
            "source_candidates_per_query":INITIAL_K,
            "source_excerpt_chars_per_candidate":MAX_EXCERPT_CHARS_PER_SOURCE,
            "total_source_excerpt_chars":MAX_TOTAL_EXCERPT_CHARS,
            "max_query_characters":MAX_QUERY_CHARS,
            "full_original_source_read_available_through_common_contract":True,
            "future_answerer_tool_call_budget":"MUST_BE_FROZEN_WITH_FRESH_SESSION_PACKETS_BEFORE_FORMAL_EXECUTION",
        },
        "b4":check_environment_b4(),
        "metadata_source_owner_authentication":"NOT_CLAIMED_EXPOSED_COORDINATOR_AUTHORED",
        "research559_legacy_nine":"NOT_YET_FROZEN_DO_NOT_BUILD_LEGACY_ARMS",
        "post_arm_freeze_primary_authoring":"NOT_YET_OCCURRED",
        "future_heldout_draw":"NOT_DRAWN",
        "protected_gold":"NONE",
        "formal_scored_attempts_used":0,
        "physical_target_selected":False,
        "production_authority_changed":False,
    }
    return contract,meta,catalog,arms


def main() -> None:
    contract,_,_,arms=make_frozen()
    print(json.dumps({
        "classification":contract["classification"],
        "source_count":contract["common_original_source_count"],
        "original_bytes":contract["common_original_source_bytes"],
        "passages":contract["common_bm25_passage_count"],
        "metadata_cost_counts":{
            name:{k:v for k,v in val.items() if isinstance(v,int)}
            for name,val in contract["costs_not_quality_scores"].items()
        },
        "b4":"OMIT_IF_NO_QUALIFIED_HOST_BEFORE_FREEZE",
        "pretask_no_formal_score":True,
    },sort_keys=True))


if __name__=="__main__":
    main()
