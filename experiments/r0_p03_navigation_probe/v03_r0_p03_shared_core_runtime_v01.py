"""Runnable, source-bound *common* R0-P03 B0-B4 access surface.

This is a real shared-core API for a 24-file, non-scored public Git witness
pilot. B0-B4 use the same entry points, source revision, source-line budgets,
lexical search and experimental (weak assurance) J1/J2/J3 facts. The arm names
only select equivalent facades; B1/B2/B3/B4 additions DO NOT exist here.

The source is Git rather than current filesystem; identities/authority do not
come from file paths or generated cache. All returned values are detached.
Deleting the in-memory derived orientation cache and rebuilding it must not
affect exact source evidence or accepted experimental semantic state.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_r0_p03_source_content_role_preflight_v01 as inspection,
    v03_r0_p03_unscored_mixed_source_cohort_readiness_v01 as pilot,
)

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "v03_r0_p03_shared_core_runtime_result_v01.json"
INSPECTION_SHA256 = "d1da9fb5a8dfe4f75d81a22eed1fb1725a737ac66bc49591c416c2631aa7d63b"
PUBLIC_REVISON = pilot.REF
ARM_LABELS = pilot.ARMS
MAX_READ_LINES = 40
MAX_LEXICAL_HITS = 20


def _json_copy(value: Any) -> Any:
    return deepcopy(value)


def _source_claims():
    """Verify the distinct content-observation result, not a worktree assumption."""
    raw = inspection.OUTPUT.read_bytes()
    if sha256(raw).hexdigest() != INSPECTION_SHA256:
        raise ValueError("P03_CORE_SOURCE_CONTENT_RECEIPT_DRIFT")
    observed = json.loads(raw.decode("utf8"))
    if (
        observed["source_git_revision"] != PUBLIC_REVISON
        or observed["source_count"] != 24
        or observed["independent_eligibility_referee_qualified"] is not False
        or observed["formal_60_20_source_set_selected"] is not False
    ):
        raise ValueError("P03_CORE_SOURCE_CONTENT_AUTHORITY_DRIFT")
    return observed


class SharedCoreRuntime:
    """Exact-source view of identical *common* capabilities for each arm label.

    This is neither the physical future architecture nor a substitute for
    separately authored, equalized B0-B4 implementations. Requests are
    deliberately bounded; invalid/unlisted source paths fail closed.
    """

    def __init__(self, arm: str) -> None:
        if arm not in ARM_LABELS:
            raise ValueError("P03_CORE_UNKNOWN_ARM")
        self.arm = arm
        seed = pilot.load_seed()
        self._sources = pilot.witness_records(seed)
        self._source_by_path = {
            row["source_path"]: row for row in self._sources
        }
        self._roster = pilot.source_roster()
        self._content = _source_claims()
        if set(self._source_by_path) != {
            row["source_path"] for row in self._content["content_role_evidence"]
        }:
            raise ValueError("P03_CORE_SOURCE_ROLE_CONTENT_MISMATCH")
        self._content_by_path = {
            row["source_path"]: row
            for row in self._content["content_role_evidence"]
        }
        self._semantic = pilot.source_relative_semantics()
        self._common = pilot.common_projection(self._sources, self._semantic)
        if len(pilot.project_arm_common(arm, self._common)) == 0:
            raise ValueError("P03_CORE_MISSING_COMMON_PROJECTION")
        self._orientation_cache: dict | None = None
        self._calls: dict[str, int] = {
            "read_source": 0,
            "literal_search": 0,
            "source_role_observation": 0,
            "experimental_semantics": 0,
            "derived_orientation": 0,
            "drop_derived": 0,
        }

    @property
    def common_contract_sha256(self) -> str:
        return sha256(pilot.project_arm_common(self.arm, self._common)).hexdigest()

    def source_role_observation(self, path: str) -> dict:
        self._calls["source_role_observation"] += 1
        if not isinstance(path, str) or path not in self._content_by_path:
            raise ValueError("P03_CORE_UNKNOWN_OR_FORBIDDEN_SOURCE_PATH")
        return _json_copy(self._content_by_path[path])

    def read_source(self, path: str, start: int, end: int) -> dict:
        """Return only exact Git source lines and externally checkable hashes."""
        self._calls["read_source"] += 1
        if not isinstance(path, str) or path not in self._source_by_path:
            raise ValueError("P03_CORE_UNKNOWN_OR_FORBIDDEN_SOURCE_PATH")
        if any(
            isinstance(v, bool) or not isinstance(v, int) for v in (start, end)
        ) or start < 1 or end < start or end-start+1 > MAX_READ_LINES:
            raise ValueError("P03_CORE_LINE_BUDGET_VIOLATION")
        row = self._source_by_path[path]
        if end > row["line_count"]:
            raise ValueError("P03_CORE_LINE_OUTSIDE_ORIGINAL_SOURCE")
        data = pilot.git_blob(path, self._roster[path])
        if sha256(data).hexdigest() != row["source_sha256"]:
            raise ValueError("P03_CORE_SOURCE_BYTES_MISMATCH")
        lines = data.decode("utf8", errors="strict").splitlines()
        selected = [
            {
                "line": i,
                "text": lines[i-1],
                "line_sha256": sha256(lines[i-1].encode("utf8")).hexdigest(),
            }
            for i in range(start, end+1)
        ]
        return {
            "source_ref": PUBLIC_REVISON,
            "source_path": path,
            "git_blob_oid": row["git_blob_oid"],
            "source_sha256": row["source_sha256"],
            "line_start": start,
            "line_end": end,
            "line_data": selected,
            "source_role_status": "INSPECTED_SOURCE_CLAIM_NOT_SEMANTICALLY_ADJUDICATED",
            "source_line_is_not_governing_acceptance": True,
        }

    def literal_search(self, query: str, *, limit: int = 10) -> list[dict]:
        self._calls["literal_search"] += 1
        if not isinstance(limit, int) or isinstance(limit, bool) or not (
            1 <= limit <= MAX_LEXICAL_HITS
        ):
            raise ValueError("P03_CORE_LEXICAL_BUDGET_VIOLATION")
        return _json_copy(pilot.exact_lexical_hits(
            query, self._sources, max_hits=limit
        ))

    def experimental_semantics(self) -> dict:
        """The identical weak-assurance accepted experimental evidence only."""
        self._calls["experimental_semantics"] += 1
        return _json_copy(self._semantic)

    def derived_orientation(self) -> dict:
        self._calls["derived_orientation"] += 1
        if self._orientation_cache is None:
            self._orientation_cache = {
                "authority_class": "DERIVED_NON_GOVERNING_EXPERIMENT_ONLY",
                "source_revision": PUBLIC_REVISON,
                "experimental_current_effects": list(self._semantic["current_effects"]),
                "weak_actor_assurance": True,
                "source_j3_sha256": self._semantic["receipt_sha256"],
                "governing_truth_is_not_in_cache": True,
            }
        return _json_copy(self._orientation_cache)

    def drop_derived(self) -> None:
        """Drop only this in-memory cache; no Git/source mutation or publication."""
        self._calls["drop_derived"] += 1
        self._orientation_cache = None

    def calls(self) -> dict[str, int]:
        return dict(self._calls)


def fixed_common_api_probe(arm: str) -> dict[str, Any]:
    """Equal *synthetic engineering* API requests, never the 12 primary tasks."""
    runtime = SharedCoreRuntime(arm)
    first = "docs/research/217_w5_t1_v02_controlled_subject_architecture_acceptance.md"
    code = "tools/project_knowledge/services/refresh.py"
    actions = {
        "source": runtime.read_source(first, 1, 12),
        "code": runtime.read_source(code, 1, 12),
        "source_role": runtime.source_role_observation(first),
        "lexical": runtime.literal_search("source", limit=7),
        "semantics": runtime.experimental_semantics(),
        "orientation": runtime.derived_orientation(),
    }
    base_digest = sha256(pilot.canonical(actions)).hexdigest()
    runtime.drop_derived()
    fresh = runtime.derived_orientation()
    if fresh != actions["orientation"]:
        raise ValueError("P03_CORE_DERIVED_CACHE_REBUILD_CHANGED_ORIENTATION")
    if runtime.experimental_semantics() != actions["semantics"]:
        raise ValueError("P03_CORE_DERIVED_CACHE_DROP_CHANGED_ACCEPTED_EVIDENCE")
    if runtime.read_source(first, 1, 12) != actions["source"]:
        raise ValueError("P03_CORE_DERIVED_DROP_CHANGED_SOURCE_BYTES")
    return {
        "common_contract_sha256": runtime.common_contract_sha256,
        "common_api_observation_sha256": base_digest,
        "source_line_and_revision_exact": True,
        "cache_drop_rebuild_equal": True,
        "call_count_by_method": runtime.calls(),
    }


def build() -> dict[str, Any]:
    source = _source_claims()
    results = {arm: fixed_common_api_probe(arm) for arm in ARM_LABELS}
    hashes = {arm: result["common_api_observation_sha256"]
              for arm, result in results.items()}
    common = {result["common_contract_sha256"] for result in results.values()}
    calls = [result["call_count_by_method"] for result in results.values()]
    if len(set(hashes.values())) != 1 or len(common) != 1 or len({
        tuple(sorted(c.items())) for c in calls
    }) != 1:
        raise ValueError("P03_CORE_COMMON_API_BEHAVIOR_OR_COST_DIFFERENT")
    if source["unreviewed_semantic_eligibility_count"] != 24:
        raise ValueError("P03_CORE_INDEPENDENT_ELIGIBILITY_NOT_PROVEN")
    return {
        "schema_version": 1,
        "status": "COMMON_API_RUNTIME_BEHAVIOR_EQUAL_ON_UNSCORED_24_SOURCE_PILOT",
        "source_git_revision": PUBLIC_REVISON,
        "original_role_source_count": 24,
        "source_content_receipt_sha256": INSPECTION_SHA256,
        "per_arm_equal_common_api_probes": results,
        "same_common_api_results_for_all_arm_labels": True,
        "same_common_request_counts_for_all_arm_labels": True,
        "literal_git_search_and_excerpt_read_implemented": True,
        "ephemeral_derived_cache_discard_and_rebuild_equal": True,
        "production_or_actual_arm_runtime_parity_qualified": False,
        "b1_b2_b3_b4_additions_implemented": False,
        "formal_60_20_selected": False,
        "hidden_gold_or_primary_tasks_generated": False,
        "legacy_65_source_packet_modified": False,
        "formal_r0_p03": "INCOMPLETE",
        "physical_architecture_selected": False,
        "limitations": [
            "All five facades call one shared common implementation; this tests actual common API behavior, not separate B0-B4 implementations or navigation advantages.",
            "The 24 pilot sources are not independently adjudicated semantic-eligibility or owner/currentness facts.",
            "Dropping this process-local cache is not a qualified test of deleting all future generated indexes or original repository views.",
            "No independent blind author, hidden gold, held-out carrier, B0-B4 arm-specific indexing, budgets or scored navigation outputs were exercised.",
        ],
    }


def main() -> None:
    result = build()
    raw = json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != raw:
            raise RuntimeError("P03_CORE_SHARED_RUNTIME_RESULT_IMMUTABLE_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as out:
            out.write(raw)
    print(json.dumps({
        "status": result["status"],
        "equal": result["same_common_api_results_for_all_arm_labels"],
        "arm_specific_runtimes_qualified": result[
            "production_or_actual_arm_runtime_parity_qualified"
        ],
        "formal": result["formal_r0_p03"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
