#!/usr/bin/env python3
"""Relation-lifecycle discriminator for Research 124 architecture hypotheses.

This is a deterministic research probe, not production ADS infrastructure. It consumes
one hash-frozen representation-neutral fixture and models it twice:

H1 keeps every authoritative relation declaration source-local. A relation with no
semantically distinguished endpoint must still be placed under one endpoint through a
deterministic tie-break. Global views are derived.

H2 applies a narrow admission rule. Ordinary directional relations stay source-local,
while a relation may enter a first-class relation spine only when the frozen fixture says
it requires stable identity, owns an independent lifecycle and provenance, and has no
natural endpoint owner.

The probe compares correctness, ownership naturalness, write coupling, concurrency,
admission selectivity and derived-view rebuildability. It deliberately emits no winner
score and cannot select the project architecture.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = REPO_ROOT / "docs/research/project_knowledge_architecture_probe_v02/RELATION_LIFECYCLE_FIXTURE_V02.json"
RESULT_PATH = REPO_ROOT / "docs/research/project_knowledge_architecture_probe_v02/RESULTS_V02.json"
EXPECTED_FIXTURE_SHA256 = "ece094762e3fe4f064640004da3f2293aa39168268af183df6f1347ba7f4b4c0"


class ProbeError(RuntimeError):
    """Fail-visible deterministic probe error."""


@dataclass
class Instrumentation:
    authoritative_touches: list[dict[str, Any]] = field(default_factory=list)
    stale_rejections: list[dict[str, Any]] = field(default_factory=list)

    def touch(self, event: str, *locations: str) -> None:
        self.authoritative_touches.append({"event": event, "locations": sorted(set(locations))})

    def stale(self, event: str, relation_id: str, expected: int, actual: int) -> None:
        self.stale_rejections.append({"event": event, "relation_id": relation_id, "expected_revision": expected, "actual_revision": actual})


class BaseRelationProbe:
    hypothesis = "BASE"

    def __init__(self, fixture: dict[str, Any]) -> None:
        self.fixture = copy.deepcopy(fixture)
        self.endpoints = {item["id"]: {**copy.deepcopy(item), "container_write_revision": 1, "source_local_relations": {}} for item in fixture["endpoints"]}
        self.evidence = {item["id"]: copy.deepcopy(item) for item in fixture["evidence"]}
        self.derived: dict[str, dict[str, Any]] = {}
        self.instrument = Instrumentation()
        control = copy.deepcopy(fixture["simple_directional_control"])
        self.endpoints[control["source"]]["source_local_relations"][control["fixture_key"]] = control
        self.stale_attempt_result: dict[str, Any] | None = None
        self._initialize_independent_relation(copy.deepcopy(fixture["independent_relation"]["initial"]))

    def _initialize_independent_relation(self, relation: dict[str, Any]) -> None:
        relation["timeline"] = [self._timeline_entry("proposed", relation["recorded_at"], relation)]
        self._store_new_relation(relation)

    @staticmethod
    def _timeline_entry(op: str, recorded_at: str, relation: dict[str, Any]) -> dict[str, Any]:
        state = {k: copy.deepcopy(v) for k, v in relation.items() if k != "timeline"}
        return {"op": op, "recorded_at": recorded_at, "state": state}

    def _store_new_relation(self, relation: dict[str, Any]) -> None:
        raise NotImplementedError

    def _get_relation(self, relation_id: str) -> dict[str, Any]:
        raise NotImplementedError

    def _relation_location(self, relation_id: str) -> str:
        raise NotImplementedError

    def owner_observation(self) -> dict[str, Any]:
        raise NotImplementedError

    def h2_admission_observation(self) -> dict[str, Any]:
        raise NotImplementedError

    def spine_record_count(self) -> int:
        return 0

    def relation_authority_payload(self) -> Any:
        raise NotImplementedError

    def _touch_relation_write(self, event: str, relation_id: str, *, new_relation_id: str | None = None) -> None:
        raise NotImplementedError

    def source_digest(self) -> str:
        payload = {
            "endpoints": self.endpoints,
            "evidence": self.evidence,
            "relation_authority": self.relation_authority_payload(),
        }
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def apply_transition(self, transition: dict[str, Any]) -> dict[str, Any]:
        relation = self._get_relation(transition["relation"])
        expected = transition["expected_revision"]
        actual = relation["revision"]
        if expected != actual:
            self.instrument.stale(transition["id"], relation["id"], expected, actual)
            result = {"error": "STALE_RELATION_REVISION", "authoritative_mutation": False, "expected_revision": expected, "actual_revision": actual}
            self.stale_attempt_result = result
            return result

        op = transition["op"]
        if op == "dispute":
            relation["revision"] = transition["new_revision"]
            relation["status"] = transition["status"]
            relation["recorded_at"] = transition["recorded_at"]
            relation["evidence_ids"].extend(transition["append_evidence"])
            timeline_op = "disputed"
        elif op == "accept":
            relation["revision"] = transition["new_revision"]
            relation["status"] = transition["status"]
            relation["recorded_at"] = transition["recorded_at"]
            relation["authority_transition_at"] = transition["authority_transition_at"]
            relation["effective_from"] = transition["effective_from"]
            relation["evidence_ids"].extend(transition["append_evidence"])
            timeline_op = "accepted"
        elif op == "verify":
            relation["revision"] = transition["new_revision"]
            relation["status"] = transition["status"]
            relation["recorded_at"] = transition["recorded_at"]
            relation["qualification"] = transition["qualification"]
            relation["evidence_ids"].extend(transition["append_evidence"])
            timeline_op = "verified"
        elif op == "create_successor_and_schedule_supersession":
            relation["revision"] = transition["new_revision"]
            relation["status"] = "superseded"
            relation["recorded_at"] = transition["recorded_at"]
            relation["superseded_by"] = transition["superseded_by"]
            relation["superseded_effective_from"] = transition["superseded_effective_from"]
            successor = copy.deepcopy(transition["successor"])
            successor["timeline"] = [self._timeline_entry("accepted", successor["recorded_at"], successor)]
            self._store_new_relation(successor)
            timeline_op = "supersession_scheduled"
        else:
            raise ProbeError(f"UNKNOWN_TRANSITION:{op}")

        relation["timeline"].append(self._timeline_entry(timeline_op, transition["recorded_at"], relation))
        self._touch_relation_write(transition["id"], relation["id"], new_relation_id=transition.get("superseded_by") if op == "create_successor_and_schedule_supersession" else None)
        return {"status": "applied", "relation_id": relation["id"], "revision": relation["revision"]}

    def run_lifecycle(self) -> list[dict[str, Any]]:
        results = []
        for transition in self.fixture["independent_relation"]["transitions"]:
            if transition["op"] == "stale_update_attempt":
                before = copy.deepcopy(self._get_relation(transition["relation"]))
                result = self.apply_transition(transition)
                after = self._get_relation(transition["relation"])
                result["state_unchanged"] = before == after
                results.append(result)
            else:
                results.append(self.apply_transition(transition))
        return results

    def snapshot_at(self, relation_id: str, date: str) -> dict[str, Any] | None:
        relation = self._get_relation(relation_id)
        entries = [item for item in relation["timeline"] if item["recorded_at"] <= date]
        if not entries:
            return None
        return copy.deepcopy(entries[-1]["state"])

    @staticmethod
    def lifecycle_status_at(snapshot: dict[str, Any], date: str) -> str:
        if snapshot.get("status") == "superseded":
            effective = snapshot.get("superseded_effective_from")
            if effective and date < effective:
                return "accepted_pending_supersession"
            return "superseded"
        return snapshot["status"]

    @classmethod
    def relation_effective_at(cls, snapshot: dict[str, Any] | None, date: str) -> bool:
        if snapshot is None:
            return False
        status = cls.lifecycle_status_at(snapshot, date)
        if status not in {"accepted", "accepted_pending_supersession"}:
            return False
        effective_from = snapshot.get("effective_from")
        return bool(effective_from and effective_from <= date)

    def all_relation_ids(self) -> list[str]:
        raise NotImplementedError

    def query_at(self, date: str) -> dict[str, Any]:
        current = []
        snapshots: dict[str, dict[str, Any] | None] = {}
        for relation_id in self.all_relation_ids():
            snapshot = self.snapshot_at(relation_id, date)
            snapshots[relation_id] = snapshot
            if self.relation_effective_at(snapshot, date):
                missing = [eid for eid in snapshot.get("evidence_ids", []) if eid not in self.evidence]
                if missing:
                    return {"status": "unresolved_missing_relation_evidence", "missing_evidence_ids": sorted(missing), "relation_id": relation_id}
                current.append(relation_id)

        r1 = snapshots.get("R-ABC-1")
        result: dict[str, Any] = {"current_applicable_relation_ids": sorted(current)}
        if r1:
            result["R-ABC-1_lifecycle_status"] = self.lifecycle_status_at(r1, date)
            result["R-ABC-1_effective"] = self.relation_effective_at(r1, date)
            if r1.get("superseded_by") and date >= r1.get("recorded_at", "9999-12-31") and date < r1.get("superseded_effective_from", "0000-01-01"):
                result["known_successor"] = r1["superseded_by"]
        r2 = snapshots.get("R-ABC-2")
        if r2 and r2.get("recorded_at") <= date and date >= r2.get("effective_from", "9999-12-31"):
            result["R-ABC-2_lifecycle_status"] = self.lifecycle_status_at(r2, date)
            result["R-ABC-2_effective"] = self.relation_effective_at(r2, date)
        return result

    def history_ops(self, relation_id: str) -> list[str]:
        return [item["op"] for item in self._get_relation(relation_id)["timeline"]]

    def endpoint_semantic_revisions(self) -> dict[str, int]:
        return {key: value["semantic_revision"] for key, value in sorted(self.endpoints.items())}

    def endpoint_container_write_revisions(self) -> dict[str, int]:
        return {key: value["container_write_revision"] for key, value in sorted(self.endpoints.items())}

    def build_views(self) -> None:
        member_index: dict[str, list[str]] = {}
        history: dict[str, list[str]] = {}
        for relation_id in self.all_relation_ids():
            relation = self._get_relation(relation_id)
            for member in relation["members"]:
                member_index.setdefault(member, []).append(relation_id)
            history[relation_id] = self.history_ops(relation_id)
        for member in member_index:
            member_index[member].sort()
        digest = self.source_digest()
        self.derived = {
            "member_relation_index": {"source_digest": digest, "payload": member_index},
            "current_relation_view": {"source_digest": digest, "payload": self.query_at("2026-05-21")},
            "relation_history_projection": {"source_digest": digest, "payload": history},
        }

    def delete_views(self) -> None:
        self.derived = {}

    def require_view(self, name: str) -> dict[str, Any]:
        if name not in self.derived:
            raise ProbeError(f"DERIVED_VIEW_UNAVAILABLE:{name}")
        return self.derived[name]

    def missing_evidence_challenge(self) -> dict[str, Any]:
        challenge = self.fixture["missing_evidence_challenge"]
        removed = self.evidence.pop(challenge["remove_evidence_id"])
        try:
            return self.query_at(challenge["query_date"])
        finally:
            self.evidence[challenge["remove_evidence_id"]] = removed

    def scale_observation(self, count: int) -> dict[str, Any]:
        raise NotImplementedError

    def final_relation_summary(self, relation_id: str) -> dict[str, Any]:
        relation = self._get_relation(relation_id)
        keys = ["revision", "status", "scope", "qualification", "evidence_ids", "superseded_by", "superseded_effective_from", "supersedes", "effective_from"]
        return {key: copy.deepcopy(relation[key]) for key in keys if key in relation and relation[key] is not None}

    def relation_semantic_facts(self) -> dict[str, str]:
        facts: dict[str, str] = {}
        for endpoint in ["S-A", "S-B", "S-C", "S-D"]:
            facts[f"endpoint:{endpoint}:intrinsic"] = f"doc:{endpoint}"
        control = self.fixture["simple_directional_control"]
        facts["relation:SR-D-A:depends_on"] = f"doc:{control['natural_owner']}"
        for relation_id in ["R-ABC-1", "R-ABC-2"]:
            relation = self._get_relation(relation_id)
            owner = self._relation_location(relation_id)
            facts[f"relation:{relation_id}:identity"] = owner
            facts[f"relation:{relation_id}:members"] = owner
            facts[f"relation:{relation_id}:lifecycle"] = owner
            facts[f"relation:{relation_id}:temporal"] = owner
            facts[f"relation:{relation_id}:provenance"] = owner
        return facts

    def representation_stats(self) -> dict[str, Any]:
        facts = self.relation_semantic_facts()
        source_local = sum(owner.startswith(("doc:", "sidecar:")) for owner in facts.values())
        spine = sum(owner.startswith("spine:") for owner in facts.values())
        authoritative_location_touch_total = sum(
            len(event["locations"]) for event in self.instrument.authoritative_touches
        )
        return {
            "normalized_semantic_fact_count": len(facts),
            "source_local_fact_count": source_local,
            "spine_fact_count": spine,
            "fact_ownership": facts,
            "spine_record_count": self.spine_record_count(),
            "owner_observation": self.owner_observation(),
            "admission": self.h2_admission_observation(),
            "endpoint_semantic_revisions": self.endpoint_semantic_revisions(),
            "endpoint_container_write_revisions": self.endpoint_container_write_revisions(),
            "authoritative_touch_events": copy.deepcopy(self.instrument.authoritative_touches),
            "authoritative_location_touch_total": authoritative_location_touch_total,
            "stale_rejections": copy.deepcopy(self.instrument.stale_rejections),
        }


class H1Probe(BaseRelationProbe):
    hypothesis = "H1_DISTRIBUTED_DOCUMENT_CONTRACTS_V02"

    def __init__(self, fixture: dict[str, Any]) -> None:
        self.relation_owner: dict[str, str] = {}
        # Use the strongest H1 form allowed by the frozen boundary: a source-owned
        # relation sidecar. This avoids unfairly forcing relation-only lifecycle edits
        # into the endpoint's intrinsic document while preserving the key H1 property
        # that every authoritative declaration is owned by one source/endpoint.
        self.source_sidecars: dict[str, dict[str, Any]] = {}
        super().__init__(fixture)
        for endpoint_id in self.endpoints:
            self.source_sidecars.setdefault(endpoint_id, {"write_revision": 1, "relations": {}})

    @staticmethod
    def _choose_owner(relation: dict[str, Any]) -> str:
        # The fixture deliberately declares no natural endpoint owner. H1 therefore
        # needs a deterministic placement rule to remain source-local.
        return sorted(relation["members"])[0]

    def _store_new_relation(self, relation: dict[str, Any]) -> None:
        owner = self._choose_owner(relation)
        self.relation_owner[relation["id"]] = owner
        sidecar = self.source_sidecars.setdefault(owner, {"write_revision": 1, "relations": {}})
        sidecar["relations"][relation["id"]] = relation

    def _get_relation(self, relation_id: str) -> dict[str, Any]:
        owner = self.relation_owner.get(relation_id)
        if owner is None:
            raise ProbeError(f"RELATION_NOT_FOUND:{relation_id}")
        return self.source_sidecars[owner]["relations"][relation_id]

    def _relation_location(self, relation_id: str) -> str:
        return f"sidecar:{self.relation_owner[relation_id]}:relations"

    def all_relation_ids(self) -> list[str]:
        return sorted(self.relation_owner)

    def relation_authority_payload(self) -> Any:
        return {
            "source_sidecars": copy.deepcopy(self.source_sidecars),
            "endpoint_local_relations": {
                endpoint: copy.deepcopy(data["source_local_relations"])
                for endpoint, data in sorted(self.endpoints.items())
            },
        }

    def _touch_relation_write(self, event: str, relation_id: str, *, new_relation_id: str | None = None) -> None:
        owner = self.relation_owner[relation_id]
        self.source_sidecars[owner]["write_revision"] += 1
        self.instrument.touch(event, f"sidecar:{owner}:relations")

    def owner_observation(self) -> dict[str, Any]:
        independent = {}
        for relation_id in ["R-ABC-1", "R-ABC-2"]:
            independent[relation_id] = {
                "owner": self._relation_location(relation_id),
                "owner_selection_basis": "lexicographically-smallest-symmetric-member",
                "semantically_natural": False,
                "reason": "fixture declares symmetric ternary membership and no natural endpoint owner",
            }
        relation_only_touches = sum(
            1
            for event in self.instrument.authoritative_touches
            if any(location == "sidecar:S-A:relations" for location in event["locations"])
        )
        authority_locations = sorted({item["owner"] for item in independent.values()})
        return {
            "independent_relations": independent,
            "arbitrary_endpoint_owner_count": 2,
            "relation_only_source_owned_touch_events": relation_only_touches,
            "independent_relation_authority_locations": authority_locations,
            "independent_relation_authority_location_count": len(authority_locations),
            "dedicated_relation_authority_locations": 0,
            "source_sidecar_write_revisions": {
                endpoint: data["write_revision"] for endpoint, data in sorted(self.source_sidecars.items())
            },
        }

    def h2_admission_observation(self) -> dict[str, Any]:
        return {
            "not_applicable_to_h1": True,
            "false_positive_admissions": 0,
            "false_negative_admissions": 0,
        }

    def scale_observation(self, count: int) -> dict[str, Any]:
        # Materialize rather than arithmetically assume the scaled source-local case.
        clone = copy.deepcopy(self)
        owner = self.fixture["simple_directional_control"]["source"]
        for idx in range(count):
            relation_id = f"SIMPLE-{idx:03d}"
            clone.endpoints[owner]["source_local_relations"][relation_id] = {
                "id": relation_id,
                **copy.deepcopy(self.fixture["simple_relation_scale"]["template"]),
                "source": owner,
                "target": "S-A",
            }
        source_local_count = sum(len(data["source_local_relations"]) for data in clone.endpoints.values()) + sum(
            len(data["relations"]) for data in clone.source_sidecars.values()
        )
        return {
            "additional_simple_relations": count,
            "source_local_relation_count": source_local_count,
            "relation_spine_records": 0,
            "false_positive_spine_admissions": 0,
        }


class H2Probe(BaseRelationProbe):
    hypothesis = "H2_MINIMAL_RELATION_SPINE_V02"

    def __init__(self, fixture: dict[str, Any]) -> None:
        self.relation_spine: dict[str, dict[str, Any]] = {}
        super().__init__(fixture)

    @staticmethod
    def qualifies_for_spine(relation: dict[str, Any]) -> bool:
        return bool(
            relation.get("stable_relation_identity_required")
            and relation.get("independent_lifecycle")
            and relation.get("relation_specific_provenance")
            and relation.get("natural_endpoint_owner") is None
        )

    def _store_new_relation(self, relation: dict[str, Any]) -> None:
        if not self.qualifies_for_spine(relation):
            raise ProbeError(f"RELATION_DOES_NOT_QUALIFY_FOR_SPINE:{relation.get('id')}")
        self.relation_spine[relation["id"]] = relation

    def _get_relation(self, relation_id: str) -> dict[str, Any]:
        try:
            return self.relation_spine[relation_id]
        except KeyError as exc:
            raise ProbeError(f"RELATION_NOT_FOUND:{relation_id}") from exc

    def _relation_location(self, relation_id: str) -> str:
        return f"spine:{relation_id}"

    def all_relation_ids(self) -> list[str]:
        return sorted(self.relation_spine)

    def relation_authority_payload(self) -> Any:
        return copy.deepcopy(self.relation_spine)

    def spine_record_count(self) -> int:
        return len(self.relation_spine)

    def _touch_relation_write(self, event: str, relation_id: str, *, new_relation_id: str | None = None) -> None:
        locations = [f"spine:{relation_id}"]
        if new_relation_id:
            locations.append(f"spine:{new_relation_id}")
        self.instrument.touch(event, *locations)

    def owner_observation(self) -> dict[str, Any]:
        independent = {}
        for relation_id in ["R-ABC-1", "R-ABC-2"]:
            independent[relation_id] = {
                "owner": self._relation_location(relation_id),
                "owner_selection_basis": "relation-owns-its-independent-lifecycle",
                "semantically_natural": True,
                "reason": "relation satisfies frozen first-class admission rule",
            }
        authority_locations = sorted({item["owner"] for item in independent.values()})
        return {
            "independent_relations": independent,
            "arbitrary_endpoint_owner_count": 0,
            "relation_only_source_owned_touch_events": 0,
            "independent_relation_authority_locations": authority_locations,
            "independent_relation_authority_location_count": len(authority_locations),
            "dedicated_relation_authority_locations": len(independent),
        }

    def h2_admission_observation(self) -> dict[str, Any]:
        probe = self.fixture["h2_admission_rule_probe"]
        false_negatives = [rid for rid in probe["qualifying_relation_ids"] if rid not in self.relation_spine]
        control = self.fixture["simple_directional_control"]
        control_as_relation = {
            "stable_relation_identity_required": control["relation_identity_required"],
            "independent_lifecycle": control["independent_lifecycle"],
            "relation_specific_provenance": control["relation_specific_provenance"],
            "natural_endpoint_owner": control["natural_owner"],
        }
        false_positives = [control["fixture_key"]] if self.qualifies_for_spine(control_as_relation) else []
        return {
            "qualifying_relation_ids": sorted(probe["qualifying_relation_ids"]),
            "admitted_relation_ids": sorted(self.relation_spine),
            "nonqualifying_control_in_spine": bool(false_positives),
            "false_positive_admissions": len(false_positives),
            "false_negative_admissions": len(false_negatives),
        }

    def scale_observation(self, count: int) -> dict[str, Any]:
        # Materialize ordinary relations through the same admission rule. Qualifying
        # relations would be visible as false positives and grow the relation spine.
        clone = copy.deepcopy(self)
        template = self.fixture["simple_relation_scale"]["template"]
        owner = self.fixture["simple_directional_control"]["source"]
        false_positive = 0
        for idx in range(count):
            relation_id = f"SIMPLE-{idx:03d}"
            relation = {
                "id": relation_id,
                "stable_relation_identity_required": template["stable_relation_identity_required"],
                "independent_lifecycle": template["independent_lifecycle"],
                "relation_specific_provenance": template["relation_specific_provenance"],
                "natural_endpoint_owner": template["natural_owner"],
                "source": owner,
                "target": "S-A",
            }
            if clone.qualifies_for_spine(relation):
                false_positive += 1
                clone.relation_spine[relation_id] = relation
            else:
                clone.endpoints[owner]["source_local_relations"][relation_id] = relation
        source_local_count = sum(len(data["source_local_relations"]) for data in clone.endpoints.values())
        return {
            "additional_simple_relations": count,
            "source_local_relation_count": source_local_count,
            "relation_spine_records": len(clone.relation_spine),
            "false_positive_spine_admissions": false_positive,
        }


def _check(label: str, actual: Any, expected: Any) -> dict[str, Any]:
    return {"label": label, "pass": actual == expected, "actual": actual, "expected": expected}


def run_candidate(cls: type[BaseRelationProbe], fixture: dict[str, Any]) -> dict[str, Any]:
    probe = cls(fixture)
    checks: list[dict[str, Any]] = []
    transition_results = probe.run_lifecycle()

    for date, expected in fixture["expected_queries"].items():
        checks.append(_check(f"temporal:{date}", probe.query_at(date), expected))

    expected_final = fixture["expected_final"]
    checks.append(_check("final:endpoint-semantic-revisions", probe.endpoint_semantic_revisions(), expected_final["endpoint_semantic_revisions"]))
    r1_summary = probe.final_relation_summary("R-ABC-1")
    r2_summary = probe.final_relation_summary("R-ABC-2")
    checks.append(_check("final:R-ABC-1", {k: r1_summary[k] for k in expected_final["R-ABC-1"]}, expected_final["R-ABC-1"]))
    checks.append(_check("final:R-ABC-2", {k: r2_summary[k] for k in expected_final["R-ABC-2"]}, expected_final["R-ABC-2"]))
    checks.append(_check("final:history", probe.history_ops("R-ABC-1"), expected_final["history_ops"]))
    checks.append(_check("stale:error", probe.stale_attempt_result["error"], expected_final["stale_attempt"]["error"]))
    checks.append(_check("stale:no-authoritative-mutation", probe.stale_attempt_result["authoritative_mutation"], expected_final["stale_attempt"]["authoritative_mutation"]))
    stale_transition = next(item for item in transition_results if item.get("error") == "STALE_RELATION_REVISION")
    checks.append(_check("stale:state-unchanged", stale_transition.get("state_unchanged"), True))

    missing = probe.missing_evidence_challenge()
    checks.append(_check("missing-evidence:status", missing.get("status"), fixture["missing_evidence_challenge"]["expected_status"]))
    checks.append(_check("missing-evidence:id", missing.get("missing_evidence_ids"), [fixture["missing_evidence_challenge"]["remove_evidence_id"]]))

    probe.build_views()
    digest = probe.source_digest()
    before = copy.deepcopy(probe.derived)
    probe.delete_views()
    missing_view_visible = False
    try:
        probe.require_view("current_relation_view")
    except ProbeError as exc:
        missing_view_visible = str(exc) == "DERIVED_VIEW_UNAVAILABLE:current_relation_view"
    probe.build_views()
    checks.append(_check("derived:missing-visible", missing_view_visible, True))
    checks.append(_check("derived:rebuild-equal", {k: v["payload"] for k, v in probe.derived.items()}, {k: v["payload"] for k, v in before.items()}))
    checks.append(_check("derived:freshness-bound", all(item["source_digest"] == digest for item in probe.derived.values()), True))

    scale = {label: probe.scale_observation(count) for label, count in fixture["simple_relation_scale"]["counts"].items()}
    if cls is H2Probe:
        checks.append(_check("admission:false-positive", probe.h2_admission_observation()["false_positive_admissions"], 0))
        checks.append(_check("admission:false-negative", probe.h2_admission_observation()["false_negative_admissions"], 0))
        checks.append(_check("admission:spine-records-scale", [scale[label]["relation_spine_records"] for label in ["1x", "5x", "10x"]], fixture["simple_relation_scale"]["expected_h2_relation_spine_records"]))

    return {
        "hypothesis": probe.hypothesis,
        "all_semantic_checks_pass": all(item["pass"] for item in checks),
        "checks": checks,
        "transition_results": transition_results,
        "scale": scale,
        "representation": probe.representation_stats(),
        "derived_view_names": sorted(probe.derived),
    }


def compare_results(h1: dict[str, Any], h2: dict[str, Any]) -> dict[str, Any]:
    h1_owner = h1["representation"]["owner_observation"]
    h2_owner = h2["representation"]["owner_observation"]
    return {
        "semantic_correctness": {"H1": h1["all_semantic_checks_pass"], "H2": h2["all_semantic_checks_pass"]},
        "arbitrary_endpoint_owner_count": {"H1": h1_owner["arbitrary_endpoint_owner_count"], "H2": h2_owner["arbitrary_endpoint_owner_count"]},
        "relation_only_source_owned_touch_events": {"H1": h1_owner["relation_only_source_owned_touch_events"], "H2": h2_owner["relation_only_source_owned_touch_events"]},
        "h1_source_sidecar_write_revisions": h1_owner.get("source_sidecar_write_revisions", {}),
        "independent_relation_authority_location_count": {"H1": h1_owner["independent_relation_authority_location_count"], "H2": h2_owner["independent_relation_authority_location_count"]},
        "dedicated_relation_authority_locations": {"H1": h1_owner["dedicated_relation_authority_locations"], "H2": h2_owner["dedicated_relation_authority_locations"]},
        "authoritative_location_touch_total": {"H1": h1["representation"]["authoritative_location_touch_total"], "H2": h2["representation"]["authoritative_location_touch_total"]},
        "endpoint_container_write_revisions": {"H1": h1["representation"]["endpoint_container_write_revisions"], "H2": h2["representation"]["endpoint_container_write_revisions"]},
        "semantic_fact_ownership": {
            "H1": {"source_local": h1["representation"]["source_local_fact_count"], "spine": h1["representation"]["spine_fact_count"]},
            "H2": {"source_local": h2["representation"]["source_local_fact_count"], "spine": h2["representation"]["spine_fact_count"]},
        },
        "h2_admission": h2["representation"]["admission"],
        "relation_spine_records_1x_5x_10x": {"H1": [h1["scale"][k]["relation_spine_records"] for k in ["1x", "5x", "10x"]], "H2": [h2["scale"][k]["relation_spine_records"] for k in ["1x", "5x", "10x"]]},
        "interpretation_guard": "Descriptive discriminator only. No aggregate score, automatic winner, target selection or migration authority is produced.",
    }


def load_fixture() -> tuple[dict[str, Any], str]:
    raw = FIXTURE_PATH.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_FIXTURE_SHA256:
        raise ProbeError(f"FIXTURE_HASH_MISMATCH:{digest}")
    fixture = json.loads(raw)
    if fixture.get("fixture_id") != "PKA-RL-V02":
        raise ProbeError("FIXTURE_ID_MISMATCH")
    return fixture, digest


def run(output_path: Path | None = RESULT_PATH) -> dict[str, Any]:
    fixture, digest = load_fixture()
    h1 = run_candidate(H1Probe, fixture)
    h2 = run_candidate(H2Probe, fixture)
    result = {
        "probe_id": "PKA-RL-PROBE-V02",
        "fixture_id": fixture["fixture_id"],
        "fixture_sha256": digest,
        "candidate_results": {"H1": h1, "H2": h2},
        "comparison": compare_results(h1, h2),
    }
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Relation-Lifecycle Discriminator V0.2")
    parser.add_argument("--output", type=Path, default=RESULT_PATH)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()
    result = run(None if args.no_write else args.output)
    print(json.dumps({"probe_id": result["probe_id"], "fixture_sha256": result["fixture_sha256"], "comparison": result["comparison"]}, indent=2))
    return 0 if all(result["comparison"]["semantic_correctness"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
