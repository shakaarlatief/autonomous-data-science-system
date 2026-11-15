"""Execute four distinct R0-P03 navigation channels over one real ADS V03 pilot.

This is a full *engineering* run of B0/B1/B2/B3, never a scored R0-P03
admission. The 24 source files and experiment-only S1 semantics are identical
for all channels. B1/B3 metadata and B2 editorial links are explicitly
coordinator-authored and exposed to prior exploratory data. They are not
natural-owner J1/J2 facts, source-owner accepted formal annotations, blinded
answers, or permitted formal gold.

The B0 lexical baseline uses full original Git bytes, passage BM25 with
heading boosting and exact identifier boosting, with no per-file character
cap. The same documentary references, source-role distinctions, limited
read/search capability and J1/J2/J3 source-relative semantics are available
to every channel. Navigation channels return candidate rankings only;
none changes governing validity.
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
    v03_r0_p03_shared_core_runtime_v01 as shared,
    v03_r0_p03_unscored_mixed_source_cohort_readiness_v01 as prior,
)

HERE = Path(__file__).resolve().parent
RESULT = HERE / "v03_r0_p03_actual_navigation_channels_unscored_result_v01.json"
METADATA_PATH = HERE / "v03_r0_p03_real_navigation_arms_exposed_metadata_v01.json"
METADATA_SHA256 = "e605d20259372e7583a1e7c52f22740279e09bc1435e22fbd741d53563295034"
CATALOG_PATH = prior.ROOT / (
    "experiments/project_knowledge_subject_navigation_t1_v02/"
    "subject_catalog_candidate_v02.json"
)
CATALOG_SHA256 = "53c5cb65caccd1a9123f5d6da2e5738f618b383339c5bcfcf1d58fb9f5399495"
PILOT_ARMS = ("B0", "B1", "B2", "B3")
CHUNK_WORDS = 220
CHUNK_OVERLAP = 40
K1 = 1.2
B = 0.75
TOKEN = re.compile(r"[a-z0-9][a-z0-9_-]{1,}", re.I)
IDENTIFIER = re.compile(r"\b(?:D-\d{3}|G\d{3}|P03PKA-E\d\d-[\w-]+)\b", re.I)

# These are *public exposed engineering probes*, not the 12 independent
# primary tasks or the 9 protected legacy references. Their rankings have
# no correctness score and cannot be reused as formal hidden questions.
EXPOSED_DIAGNOSTIC_QUERIES = (
    "project knowledge architecture implementation migration contract",
    "historical subject navigation retrieval evaluation",
    "owner approval boundary governing decision",
    "cockpit implementation product interface",
    "source universe source vault ingestion evidence",
    "source refresh currentness stale regeneration",
    "source proof test execution reproducibility",
)


def canonical(value: Any) -> bytes:
    return prior.canonical(value)


def _original_json(path: Path, digest: str) -> dict:
    data = path.read_bytes()
    if sha256(data).hexdigest() != digest:
        raise ValueError("P03_ARM_FROZEN_INPUT_HASH_CONFLICT")
    return json.loads(data.decode("utf8"))


def tokens(text: str) -> list[str]:
    return [m.group().lower().replace("_", "-") for m in TOKEN.finditer(text)]


def _passages(text: str) -> list[tuple[list[str], bool]]:
    """Partition every source byte-derived token without truncation."""
    chunks = []
    # Splitlines preserves heading/boundary context and handles code as text.
    for block in re.split(r"\n[ \t]*\n", text):
        if not block.strip():
            continue
        words = tokens(block)
        heading = block.lstrip().startswith("#")
        if not words:
            continue
        stride = CHUNK_WORDS - CHUNK_OVERLAP
        for start in range(0, len(words), stride):
            chunk = words[start:start + CHUNK_WORDS]
            if chunk:
                chunks.append((chunk, heading))
            if start + CHUNK_WORDS >= len(words):
                break
    return chunks


class FullSourceBM25:
    """Transparent lexical source index over exact, full Git blob contents."""

    def __init__(self, core: shared.SharedCoreRuntime):
        self.core = core
        self.documents = {}
        self.passages = []
        self.df = Counter()
        raw_sources = core._sources
        roster = prior.source_roster()
        for row in raw_sources:
            path = row["source_path"]
            data = prior.git_blob(path, roster[path])
            if sha256(data).hexdigest() != row["source_sha256"]:
                raise ValueError("P03_ARM_BASE_SOURCE_BYTES_DIFFER")
            self.documents[path] = data.decode("utf8")
            for words, heading in _passages(self.documents[path]):
                counts = Counter(words)
                self.passages.append((path, counts, len(words), heading))
                self.df.update(counts)
        self.avgl = sum(n for _, _, n, _ in self.passages) / len(self.passages)
        self.total_source_bytes = sum(
            len(value.encode("utf8")) for value in self.documents.values()
        )
        self.documentary = self._documentary_path_mentions()
        self._call_count = 0

    def _documentary_path_mentions(self) -> list[dict]:
        links = []
        for source, body in sorted(self.documents.items()):
            for target in sorted(self.documents):
                if source != target and target in body:
                    links.append({
                        "source": source,
                        "target": target,
                        "status": "COMMON_LITERAL_DOCUMENTARY_MENTION_NON_GOVERNING",
                    })
        return links

    def rank(self, query: str) -> list[tuple[str, float]]:
        self._call_count += 1
        terms = tokens(query)
        if not terms:
            raise ValueError("P03_ARM_BLANK_QUERY")
        n = len(self.passages)
        best = dict.fromkeys(self.documents, 0.0)
        for path, counts, length, heading in self.passages:
            score = 0.0
            for term in set(terms):
                freq = counts.get(term, 0)
                if not freq:
                    continue
                idf = math.log(1.0 + (n-self.df[term]+0.5)/(self.df[term]+0.5))
                score += idf * (freq*(K1+1.0)) / (
                    freq+K1*(1.0-B+B*length/self.avgl)
                )
            if heading:
                score *= 1.12
            if score > best[path]:
                best[path] = score
        exact_ids = [x.casefold() for x in IDENTIFIER.findall(query)]
        if exact_ids:
            for path, body in self.documents.items():
                value = body.casefold()
                if any(k in value for k in exact_ids):
                    best[path] += 0.5
        return sorted(best.items(), key=lambda kv:(-kv[1],kv[0]))


class NavigationArm:
    """Four genuinely distinct non-governing ranking treatments over B0."""

    def __init__(self, arm: str):
        if arm not in PILOT_ARMS:
            raise ValueError("P03_ARM_UNKNOWN_OR_B4_NOT_FEASIBLE")
        self.arm = arm
        self.core = shared.SharedCoreRuntime(arm)
        self.bm25 = FullSourceBM25(self.core)
        self.meta = _original_json(METADATA_PATH, METADATA_SHA256)
        self.catalog = _original_json(CATALOG_PATH, CATALOG_SHA256)
        self._validate()
        self.operations = {"common_read":0,"common_search":0,"lexical_rank":0,
                           "subject_rank":0,"editorial_link_rank":0,"concern_rank":0}
        # Exercise the actual common lexical callable once per arm before
        # running the more efficient full-source passage index. Repeating a
        # Git-blob scan per ranking query would measure redundant I/O rather
        # than the distinct navigation channels under test.
        self.core.literal_search("source", limit=3)
        self.operations["common_search"] += 1

    def _validate(self) -> None:
        m = self.meta
        if (
            m["source_ref"] != prior.REF
            or m["status"] !=
                "EXPOSED_COORDINATOR_AUTHORED_ARM_SPECIFIC_PILOT_METADATA_UNSCORED"
            or set(m["b1"]["subjects_by_source"]) != set(self.bm25.documents)
            or set(m["b3"]["concerns_by_source"]) != set(self.bm25.documents)
            or self.catalog["experiment"] != "W5-T1-V02"
            or self.catalog["source_boundary"] !=
                "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"
        ):
            raise ValueError("P03_ARM_SOURCE_WORLD_OR_W5_CATALOG_MISMATCH")
        ids = {s["id"] for s in self.catalog["subjects"] if s["assignable"]}
        if not all(set(s).issubset(ids)
                   for s in m["b1"]["subjects_by_source"].values()):
            raise ValueError("P03_ARM_B1_UNKNOWN_OR_UNASSIGNABLE_SUBJECT")
        concerns = set(m["b3"]["concern_definitions"])
        if not all(set(c).issubset(concerns)
                   for c in m["b3"]["concerns_by_source"].values()):
            raise ValueError("P03_ARM_B3_UNKNOWN_CONCERN")
        documentary = {(e["source"],e["target"]) for e in self.bm25.documentary}
        pairs = set()
        for edge in m["b2"]["additional_editorial_about_links"]:
            pair = edge["source"],edge["target"]
            if (
                pair in pairs or pair in documentary
                or pair[0] not in self.bm25.documents
                or pair[1] not in self.bm25.documents
                or pair[0] == pair[1]
                or edge["claimed_relation"] !=
                "EXPERIMENTAL_EDITORIAL_ABOUT_ONLY"
            ):
                raise ValueError("P03_ARM_B2_DUPLICATE_NATIVE_OR_GOVERNING_EDGE")
            pairs.add(pair)

    def _subject_boost(self, terms: set[str]) -> dict[str, float]:
        self.operations["subject_rank"] += 1
        definitions = {s["id"]:s for s in self.catalog["subjects"]}
        matches = {}
        for item in self.catalog["subjects"]:
            if not item["assignable"]:
                continue
            concept = set(tokens(item["id"].replace("-", " ")+ " " + item["label"]))
            overlap = len(terms & concept)
            if overlap < 1:
                continue
            matches[item["id"]] = overlap / max(1,len(concept))
        return {
            path: sum(2.0*matches.get(key,0.0) for key in keys)
            for path,keys in self.meta["b1"]["subjects_by_source"].items()
        }

    def _concern_boost(self, terms: set[str]) -> dict[str,float]:
        self.operations["concern_rank"] += 1
        valid = self.meta["b3"]["concern_definitions"]
        hits = {}
        for key,description in valid.items():
            vocab = set(tokens(key.replace("-"," ")+ " " + description))
            hits[key] = len(vocab & terms) / max(1,len(terms))
        return {
            path: sum(1.7*hits[key] for key in keys)
            for path,keys in self.meta["b3"]["concerns_by_source"].items()
        }

    def _link_boost(self, baseline: list[tuple[str,float]]) -> dict[str,float]:
        self.operations["editorial_link_rank"] += 1
        places = {path:i for i,(path,_) in enumerate(baseline[:8])}
        delta = dict.fromkeys(self.bm25.documents,0.0)
        for edge in self.meta["b2"]["additional_editorial_about_links"]:
            if edge["source"] in places:
                rank = places[edge["source"]]
                delta[edge["target"]] += 2.0 / (1.0 + rank)
        return delta

    def rank(self, query:str, *, limit:int=8) -> list[dict]:
        if not (type(limit) is int and 1<=limit<=20):
            raise ValueError("P03_ARM_QUERY_RESULT_BUDGET")
        terms = set(tokens(query))
        self.operations["lexical_rank"] += 1
        baseline = self.bm25.rank(query)
        if self.arm=="B0":
            extra = dict.fromkeys(self.bm25.documents,0.0)
        elif self.arm=="B1":
            extra = self._subject_boost(terms)
        elif self.arm=="B2":
            extra = self._link_boost(baseline)
        else:
            extra = self._concern_boost(terms)
        ranked = sorted(
            ((path,score+extra.get(path,0.0)) for path,score in baseline),
            key=lambda x:(-x[1],x[0]),
        )
        return [
            {
                "source_path": path,
                "git_blob_oid": self.core._source_by_path[path]["git_blob_oid"],
                "source_ref": prior.REF,
                "score": round(score,6),
                "authority_from_navigation": False,
                "rank":i+1,
            }
            for i,(path,score) in enumerate(ranked[:limit])
        ]


def run() -> dict[str,Any]:
    instances = {arm:NavigationArm(arm) for arm in PILOT_ARMS}
    ids = {arm:i.core.common_contract_sha256 for arm,i in instances.items()}
    if len(set(ids.values())) != 1:
        raise ValueError("P03_ARM_COMMON_API_DIFFERENCE")
    baseline = instances["B0"]
    if baseline.bm25.total_source_bytes < 100000:
        raise ValueError("P03_ARM_ORIGINAL_GIT_SOURCE_CONTENT_UNEXPECTEDLY_SMALL")
    common_edges = sha256(canonical(baseline.bm25.documentary)).hexdigest()
    if len({sha256(canonical(i.bm25.documentary)).hexdigest()
            for i in instances.values()}) != 1:
        raise ValueError("P03_ARM_DOCUMENTARY_RELATIONS_NOT_SHARED")
    traces = []
    for q in EXPOSED_DIAGNOSTIC_QUERIES:
        values = {arm:instance.rank(q) for arm,instance in instances.items()}
        paths = {arm:[x["source_path"] for x in hits] for arm,hits in values.items()}
        traces.append({
            "exposed_engineering_query":q,
            "candidate_rankings":paths,
            "same_rank_as_b0":{
                arm:paths[arm]==paths["B0"] for arm in PILOT_ARMS
            },
            "source_revisions_verified_same_all_arms":all(
                row["source_ref"]==prior.REF
                for rows in values.values() for row in rows
            ),
            "not_a_correctness_score":True,
        })
    changed = {
        arm:sum(not trace["same_rank_as_b0"][arm] for trace in traces)
        for arm in PILOT_ARMS
    }
    # Real mechanisms must at least be behaviorally observable. Not a
    # quality or relevance claim, and neither is evidence of fair gold.
    if not all(changed[a]>0 for a in ("B1","B2","B3")):
        raise ValueError("P03_ARM_ADDITIONAL_NAVIGATION_HAS_NO_OBSERVED_EFFECT")
    metadata = METADATA_PATH.read_bytes()
    return {
        "schema_version":1,
        "classification":"EXPOSED_UNSCORED_REAL_GIT_DISTINCT_B0_B3_EXECUTION",
        "source_ref":prior.REF,
        "corpus_source_count":24,
        "common_core_sha256_by_arm":ids,
        "common_documentary_path_relation_digest":common_edges,
        "common_documentary_path_relation_count":len(baseline.bm25.documentary),
        "full_original_source_byte_count":baseline.bm25.total_source_bytes,
        "passage_bm25_chunk_count":len(baseline.bm25.passages),
        "character_limit_per_document":None,
        "arm_specific_exposed_metadata_sha256":sha256(metadata).hexdigest(),
        "distinct_mechanisms":{
            "B0":"FULL_SOURCE_PASSAGE_BM25_LEXICAL_AND_EXACT_IDENTIFIER",
            "B1":"B0_PLUS_W5_CONTROLLED_SOURCE_ADJACENT_SUBJECT_FACETS",
            "B2":"B0_PLUS_EXPLICIT_EXTRA_EDITORIAL_ABOUT_LINK_GRAPH",
            "B3":"B0_PLUS_INDEPENDENT_CROSSCUTTING_CONCERN_VOCABULARY",
        },
        "exposed_diagnostic_query_count":len(traces),
        "exposed_diagnostic_traces_not_scored":traces,
        "rankings_changed_vs_b0_count_not_accuracy":changed,
        "per_arm_query_operations":{a:i.operations for a,i in instances.items()},
        "neural_b4_current_environment":{
            "sentence_transformers_importable":bool(importlib.util.find_spec("sentence_transformers")),
            "transformers_importable":bool(importlib.util.find_spec("transformers")),
            "torch_importable":bool(importlib.util.find_spec("torch")),
            "admission_status":"NOT_IMPLEMENTED_OR_PREFREEZE_QUALIFIED",
            "formal_inclusion_decision":"REQUIRES_PREFREEZE_FEASIBILITY_DECISION",
        },
        "authority_boundaries":{
            "all_real_source_bytes_are_git_pinned":True,
            "shared_semantic_j1_j2_j3_source_relative_only":True,
            "author_of_arm_metadata":"EXPOSED_CHATGPT_COORDINATOR_NOT_SOURCE_OWNER",
            "metadata_and_query_exposure":"UNSUITABLE_FOR_FORMAL_BLINDED_REFERENCE",
            "source_owner_natural_authoring_qualified":False,
            "independent_reference_gold":False,
            "formal_source_sample_60_20_selected":False,
            "no_comparator_quality_scores_observed":True,
            "actual_formal_b0_b4_freeze":False,
            "formal_r0_p03":"INCOMPLETE",
        },
        "limitations":[
            "This is a real execution of B0-B3 differentiating navigation signals on the exact unscored 24-source Git pilot, not formal Research 513 admission.",
            "B1/B2/B3 pilot metadata are exposed coordinator source-adjacent claims, not qualifying natural-owner authored declarations or independent gold.",
            "The common documentary path mentions are lexical mentions, not validated semantic documentary authority or a full typed relations substrate.",
            "The same core source/semantic API is used by all four arms; the Ranker accesses exact Git bytes internally, not an isolated connector-only agent tool environment.",
            "B4 neural model availability was tested only for the current Python environment and remains a prospective prefreeze feasibility choice.",
            "The diagnostic queries precede final arm/source/gold freeze, have no answer key, and must not become the independent primary or legacy scoring packet.",
        ],
    }


def main() -> None:
    payload = run()
    raw = json.dumps(payload,indent=2,sort_keys=True,ensure_ascii=False)+"\n"
    if RESULT.exists():
        if RESULT.read_text("utf8")!=raw:
            raise RuntimeError("P03_ARM_IMMUTABLE_EXPLORATORY_RECEIPT_CONFLICT")
    else:
        with RESULT.open("x",encoding="utf8",newline="\n") as file:
            file.write(raw)
    print(json.dumps({
        "status":payload["classification"],
        "sources":payload["corpus_source_count"],
        "queries":payload["exposed_diagnostic_query_count"],
        "changed_rankings":payload["rankings_changed_vs_b0_count_not_accuracy"],
        "formal":payload["authority_boundaries"]["formal_r0_p03"],
    },sort_keys=True))


if __name__ == "__main__":
    main()
