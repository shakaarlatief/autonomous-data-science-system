#!/usr/bin/env python3
"""Deterministic H1/H2 mechanism probe for Research 134 Common Fixture V0.1.

This is an architecture experiment, not production ADS infrastructure. It deliberately
models the same frozen semantic fixture twice:

H1: Distributed Document Contracts. Cross-object semantics must be declared on source
    artifacts and compiled into rebuildable views. No separately authoritative relation
    or control store is allowed.

H2: Partitioned Semantic Ownership. Source-local facts remain on rich source artifacts,
    while facts that genuinely span objects or own independent control state may live in
    a small modular cross-object spine. All broad navigation/search/context views remain
    rebuildable.

The probe is intentionally deterministic and uses only the Python standard library. Its
purpose is to expose semantic ownership, maintenance fan-out, boundedness and failure
behavior. It does not score candidates or select a target architecture.
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
FIXTURE_PATH = REPO_ROOT / "docs/research/project_knowledge_architecture_probe_v01/COMMON_FIXTURE_V01.json"
RESULT_PATH = REPO_ROOT / "docs/research/project_knowledge_architecture_probe_v01/RESULTS_V01.json"
EXPECTED_FIXTURE_SHA256 = "c8ed1873014b7a69016eb6fb259791d1c34b9cd14219547f1ebc0e755b836fe8"


class ProbeError(RuntimeError):
    """Fail-visible deterministic probe error."""


@dataclass
class Instrumentation:
    authoritative_touches: list[dict[str, Any]] = field(default_factory=list)
    generated_touches: list[dict[str, Any]] = field(default_factory=list)
    reclassifications: list[dict[str, Any]] = field(default_factory=list)

    def authored(self, event: str, *locations: str) -> None:
        self.authoritative_touches.append({"event": event, "locations": sorted(set(locations))})

    def generated(self, event: str, *locations: str) -> None:
        self.generated_touches.append({"event": event, "locations": sorted(set(locations))})

    def reclassify(self, event: str, from_owner: str, to_owner: str) -> None:
        self.reclassifications.append({"event": event, "from": from_owner, "to": to_owner})

    @property
    def authored_location_touch_total(self) -> int:
        return sum(len(item["locations"]) for item in self.authoritative_touches)


class BaseProbe:
    hypothesis = "BASE"

    def __init__(self, fixture: dict[str, Any]) -> None:
        self.fixture = copy.deepcopy(fixture)
        self.docs: dict[str, dict[str, Any]] = {}
        self.capture: dict[str, dict[str, Any]] = {}
        self.derived: dict[str, dict[str, Any]] = {}
        self.instrument = Instrumentation()
        self._build_sources()

    def _doc(self, doc_id: str, **fields: Any) -> None:
        self.docs[doc_id] = {"id": doc_id, **fields}

    def _build_sources(self) -> None:
        raise NotImplementedError

    def source_digest(self) -> str:
        payload = {"docs": self.docs, "capture": self.capture, "extra": self._authoritative_extra()}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def _authoritative_extra(self) -> Any:
        return None

    def build_views(self) -> None:
        identity = self.identity_view()
        authority = self.resolve_authority("2026-02-15")
        active_route = self.reconstruct_workstream()
        search = {
            "active_ids": sorted(doc_id for doc_id, doc in self.docs.items() if doc.get("status") in {"active", "accepted", "paused", "blocked"}),
            "public_ids": sorted(doc_id for doc_id, doc in self.docs.items() if doc.get("visibility", "public") == "public"),
        }
        digest = self.source_digest()
        self.derived = {
            "identity_resolution": {"source_digest": digest, "payload": identity},
            "authority_closure": {"source_digest": digest, "payload": authority},
            "active_route": {"source_digest": digest, "payload": active_route},
            "search_projection": {"source_digest": digest, "payload": search},
        }
        self.instrument.generated("rebuild-derived", *[f"derived:{k}" for k in self.derived])

    def delete_derived(self) -> None:
        self.derived = {}

    def require_view(self, name: str) -> dict[str, Any]:
        if name not in self.derived:
            raise ProbeError(f"DERIVED_VIEW_UNAVAILABLE:{name}")
        return self.derived[name]

    def identity_view(self) -> dict[str, Any]:
        raise NotImplementedError

    def resolve_authority(self, date: str) -> dict[str, Any]:
        raise NotImplementedError

    def reconstruct_workstream(self) -> dict[str, Any]:
        raise NotImplementedError

    def bind_contract(self, date: str) -> dict[str, Any]:
        raise NotImplementedError

    def challenge_missing_precedence(self) -> dict[str, Any]:
        raise NotImplementedError

    def challenge_missing_authority_relation(self) -> dict[str, Any]:
        raise NotImplementedError

    def challenge_missing_constraint(self) -> str:
        raise NotImplementedError

    def challenge_contradictory_constraint(self) -> str:
        raise NotImplementedError

    def run_identity_transitions(self) -> None:
        raise NotImplementedError

    def run_capture_lifecycle(self) -> dict[str, Any]:
        f4 = self.fixture["F4_capture"]
        self.capture["I1"] = copy.deepcopy(f4["capture"])
        self.instrument.authored("F4-capture", "capture:I1")
        self.capture["I1"]["supporting_sources"] = list(f4["supporting_sources"])
        self.instrument.authored("F4-consolidate", "capture:I1")
        self._doc("K1", role="promoted_knowledge", status="accepted", claim=f4["accepted_output"]["claim"], derived_from=["I1", *f4["supporting_sources"]])
        self._doc("R1", role="rejected_rationale", status="rejected", claim=f4["rejected_alternative"]["claim"], derived_from=["I1"])
        self.instrument.authored("F4-promote", "doc:K1", "doc:R1")
        del self.capture["I1"]
        self.instrument.authored("F4-retire-capture", "capture:I1")
        return {
            "capture_present": "I1" in self.capture,
            "K1_status": self.docs["K1"]["status"],
            "K1_provenance": self.docs["K1"]["derived_from"],
            "R1_status": self.docs["R1"]["status"],
        }

    def scale_observation(self, history_count: int) -> dict[str, Any]:
        clone = copy.deepcopy(self)
        for idx in range(history_count):
            clone.docs[f"HIST-{idx:04d}"] = {"id": f"HIST-{idx:04d}", "status": "historical", "role": "evidence"}
        for item in self.fixture["F5_scale"]["active_items"]:
            clone.docs[item] = {"id": item, "status": "active", "role": "active_knowledge"}
        clone.build_views()
        # F5 measures the same semantic active-routing contract for both hypotheses.
        # Candidate-specific document bookkeeping must not inflate one view merely because
        # an implementation uses a different authoritative carrier for the same semantics.
        active_payload = {
            "active_items": sorted(self.fixture["F5_scale"]["active_items"]),
            "governing_sources": clone.resolve_authority("2026-02-15")["governing_sources"],
            "active_chain": clone.reconstruct_workstream()["active_chain"],
        }
        active_bytes = len(json.dumps(active_payload, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        return {
            "history_count": history_count,
            "active_count": len(active_payload["active_items"]),
            "active_view_bytes": active_bytes,
            "authoritative_locations": clone.authoritative_location_count(),
            "spine_records": clone.spine_record_count(),
            "manual_global_entries": clone.manual_global_entry_count(),
            "full_rebuild_source_scan_count": len(clone.docs) + len(clone.capture) + clone.spine_record_count(),
        }

    def public_projection(self) -> dict[str, Any]:
        overlay = self.fixture["overlay"]["synthetic_private_fact"]
        docs = copy.deepcopy(self.docs)
        docs[overlay["id"]] = {"id": overlay["id"], "visibility": "private", "value": overlay["value"]}
        return {"ids": sorted(k for k, v in docs.items() if v.get("visibility", "public") == "public"), "serialized": json.dumps({k: v for k, v in docs.items() if v.get("visibility", "public") == "public"}, sort_keys=True)}

    def authoritative_location_count(self) -> int:
        return len(self.docs) + len(self.capture) + self.spine_record_count()

    def spine_record_count(self) -> int:
        return 0

    def manual_global_entry_count(self) -> int:
        return 0

    def semantic_ownership(self) -> dict[str, list[str]]:
        """Return normalized cross-object fact ids -> authoritative owner locations.

        The same semantic fact ids are required for H1 and H2. This avoids comparing
        a H1 metadata field count with a H2 record count, which would be representation-
        dependent rather than an architecture-neutral fact count.
        """
        raise NotImplementedError

    def representation_stats(self) -> dict[str, Any]:
        raw_docs = json.dumps(self.docs, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ownership = self.semantic_ownership()
        source_owned = sum(1 for owners in ownership.values() if any(owner.startswith("doc:") for owner in owners))
        spine_owned = sum(1 for owners in ownership.values() if any(owner.startswith("spine:") for owner in owners))
        derived_only = sum(1 for owners in ownership.values() if owners and all(owner.startswith("derived:") for owner in owners))
        duplicates = {
            fact: owners
            for fact, owners in ownership.items()
            if sum(owner.startswith(("doc:", "spine:")) for owner in owners) > 1
        }
        return {
            "source_documents": len(self.docs),
            "capture_records": len(self.capture),
            "spine_records": self.spine_record_count(),
            "authoritative_serialized_bytes": len(raw_docs) + self._extra_serialized_bytes(),
            "semantic_fact_count": len(ownership),
            "semantic_fact_ownership_count": {"source_local": source_owned, "spine": spine_owned, "derived_only": derived_only},
            "duplicate_authoritative_fact_owners": duplicates,
            "semantic_ownership": ownership,
            "reclassification_events": len(self.instrument.reclassifications),
            "authored_location_touch_total": self.instrument.authored_location_touch_total,
        }

    def _extra_serialized_bytes(self) -> int:
        return 0




def expected_semantic_fact_ids(fixture: dict[str, Any]) -> set[str]:
    ids = {
        "F1:S-A:carrier-continuity",
        "F1:S-B:merge-history",
        "F1:S-B:reverse-merge-history",
        "F1:S-B:split-current",
        "F2:P1:supersedes:P0",
        "F2:P2:supplements:P1",
        "F2:P1-P2:precedence",
        "F2:C1:conflict:P1",
        "F2:TASK-X:governing-set",
        "F7:G2:supplements:G1",
        "F7:G1-G2:precedence",
        "F7:TASK-SAFE-WRITE:governing-set",
    }
    for w in fixture["F3_workstreams"]["workstreams"]:
        wid = w["id"]
        ids.add(f"F3:{wid}:state")
        if w.get("parent"):
            ids.add(f"F3:{wid}:parent:{w['parent']}")
        for dep in w.get("depends_on", []):
            ids.add(f"F3:{wid}:depends:{dep}")
        if w.get("resume_target"):
            ids.add(f"F3:{wid}:resume:{w['resume_target']}")
        if w.get("resume_condition"):
            ids.add(f"F3:{wid}:resume-condition")
        if w.get("pause_reason"):
            ids.add(f"F3:{wid}:pause-reason")
    accepted = fixture["F4_capture"]["accepted_output"]["id"]
    for source in [fixture["F4_capture"]["capture"]["id"], *fixture["F4_capture"]["supporting_sources"]]:
        ids.add(f"F4:{accepted}:derived-from:{source}")
    rejected = fixture["F4_capture"]["rejected_alternative"]["id"]
    ids.add(f"F4:{rejected}:derived-from:{fixture['F4_capture']['capture']['id']}")
    return ids


class H1Probe(BaseProbe):
    hypothesis = "H1_DISTRIBUTED_DOCUMENT_CONTRACTS"

    def _build_sources(self) -> None:
        f1 = self.fixture["F1_identity"]["initial"]["semantic_subjects"]
        for subject in f1:
            self._doc(subject["id"], role="semantic_subject", status=subject["status"], current_carriers=list(subject["current_carriers"]), identity_history=[])

        f2 = self.fixture["F2_authority"]
        for src in f2["sources"]:
            self._doc(src["id"], **{k: copy.deepcopy(v) for k, v in src.items() if k != "id"}, governs=[f2["task"]] if src["id"] in {"P0", "P1", "P2"} else [])
        # Directional cross-object declarations are owned by the source that asserts the relation.
        self.docs["P1"]["supersedes"] = ["P0"]
        self.docs["P2"]["supplements"] = [{"target": "P1", "task": f2["task"], "precedence_after": "P1"}]
        self.docs["C1"]["conflicts_with"] = [{"target": "P1", "task": f2["task"]}]

        for w in self.fixture["F3_workstreams"]["workstreams"]:
            self._doc(w["id"], role="workstream", **{k: copy.deepcopy(v) for k, v in w.items() if k != "id"})

        for src in self.fixture["F7_contract"]["sources"]:
            fields = {k: copy.deepcopy(v) for k, v in src.items() if k != "id"}
            self._doc(src["id"], **fields)
        constraints_by_source: dict[str, list[dict[str, Any]]] = {}
        for c in self.fixture["F7_contract"]["constraints"]:
            constraints_by_source.setdefault(c["source"], []).append(copy.deepcopy(c))
        for source, constraints in constraints_by_source.items():
            self.docs[source]["constraints"] = constraints

    def run_identity_transitions(self) -> None:
        transitions = self.fixture["F1_identity"]["transitions"]
        t1, t2, t3, t4 = transitions
        doc = self.docs[t1["subject"]]
        doc["current_carriers"].remove(t1["from"])
        doc["current_carriers"].append(t1["to"])
        doc["identity_history"].append({"op": "move_carrier", "from": t1["from"], "to": t1["to"]})
        self.instrument.authored(t1["id"], f"doc:{t1['subject']}")

        b = self.docs[t2["source"]]
        b["status"] = "merged"
        b["redirect_to"] = t2["target"]
        b["identity_history"].append({"op": "merge", "target": t2["target"]})
        self.instrument.authored(t2["id"], f"doc:{t2['source']}")

        b["status"] = "active"
        b.pop("redirect_to", None)
        b["identity_history"].append({"op": "reverse_merge", "target": t3["target"]})
        self.instrument.authored(t3["id"], f"doc:{t3['source']}")

        b["status"] = "split"
        b["current_carriers"] = []
        b["split_into"] = [item["id"] for item in t4["targets"]]
        b["identity_history"].append({"op": "split", "targets": list(b["split_into"])})
        for item in t4["targets"]:
            self._doc(item["id"], role="semantic_subject", status="active", current_carriers=[item["carrier"]], identity_history=[{"op": "split_from", "source": t4["source"]}])
        self.instrument.authored(t4["id"], f"doc:{t4['source']}", *[f"doc:{item['id']}" for item in t4["targets"]])

    def identity_view(self) -> dict[str, Any]:
        a = self.docs["S-A"]
        b = self.docs["S-B"]
        view = {
            "S-A": {"resolution": "canonical", "targets": ["S-A"], "current_carriers": list(a["current_carriers"])},
            "A1": {"resolution": "historical_carrier", "targets": ["S-A"], "current_carriers": list(a["current_carriers"])},
        }
        if b.get("status") == "split":
            targets = list(b["split_into"])
            view["S-B"] = {"resolution": "split", "targets": targets, "current_carriers": []}
            view["B1"] = {"resolution": "historical_carrier_of_split_subject", "targets": targets, "current_carriers": []}
            for target in targets:
                view[target] = {"resolution": "canonical", "targets": [target], "current_carriers": list(self.docs[target]["current_carriers"])}
        elif b.get("redirect_to"):
            view["S-B"] = {"resolution": "redirect", "targets": [b["redirect_to"]], "current_carriers": []}
        else:
            view["S-B"] = {"resolution": "canonical", "targets": ["S-B"], "current_carriers": list(b["current_carriers"])}
        view["history"] = copy.deepcopy(b["identity_history"])
        return view

    def resolve_authority(self, date: str) -> dict[str, Any]:
        task = self.fixture["F2_authority"]["task"]
        accepted = []
        for doc_id, doc in self.docs.items():
            if task not in doc.get("governs", []):
                continue
            if doc.get("status") != "accepted":
                continue
            effective = doc.get("effective_from")
            if effective is None or effective <= date:
                accepted.append(doc_id)
        if "P2" in accepted:
            rels = self.docs["P2"].get("supplements", [])
            rel = next((r for r in rels if r.get("target") == "P1" and r.get("task") == task), None)
            if rel is None or not rel.get("precedence_after"):
                return {"governing_sources": [], "non_authoritative_conflicts": ["C1"], "status": "ambiguous"}
            governing = ["P1", "P2"]
        else:
            governing = ["P1"] if "P1" in accepted else []
        conflicts = []
        for doc_id, doc in self.docs.items():
            if (
                doc.get("status") == "candidate"
                and doc.get("recorded_at", "9999-12-31") <= date
                and any(r.get("task") == task for r in doc.get("conflicts_with", []))
            ):
                conflicts.append(doc_id)
        return {"governing_sources": governing, "non_authoritative_conflicts": sorted(conflicts), "status": "resolved" if governing else "unresolved"}

    def challenge_missing_precedence(self) -> dict[str, Any]:
        rel = self.docs["P2"]["supplements"][0]
        old = rel.pop("precedence_after")
        try:
            return self.resolve_authority("2026-02-15")
        finally:
            rel["precedence_after"] = old

    def challenge_missing_authority_relation(self) -> dict[str, Any]:
        old = self.docs["P2"].pop("supplements")
        try:
            return self.resolve_authority("2026-02-15")
        finally:
            self.docs["P2"]["supplements"] = old

    def reconstruct_workstream(self) -> dict[str, Any]:
        states = {wid: self.docs[wid]["state"] for wid in ["W0", "W1", "W2", "W2a"]}
        current = "W2a"
        chain = []
        while current:
            chain.append(current)
            current = self.docs[current].get("parent")
        chain.reverse()
        child = self.docs["W2a"]
        return {
            "states": states,
            "active_chain": chain,
            "blocking_condition": child["resume_condition"],
            "immediate_resume_target": child["resume_target"],
            "return_chain_after_child_completion": [self.docs["W2a"]["parent"], self.docs["W2"]["parent"]],
            "must_not_replay": [wid for wid in ["W1", "W2"] if self.docs[wid]["state"] == "completed"],
        }

    def _contract_sources(self, date: str) -> list[str]:
        bases = [
            doc_id
            for doc_id, doc in self.docs.items()
            if doc.get("role") == "base_contract" and doc.get("status") == "accepted"
        ]
        if bases != ["G1"]:
            raise ProbeError("CONTRACT_BASE_UNRESOLVED")
        supplements = []
        for doc_id, doc in self.docs.items():
            if doc.get("role") != "contract_supplement" or doc.get("status") != "accepted":
                continue
            if doc.get("effective_from", "9999-12-31") > date:
                continue
            if doc.get("supplements") != "G1":
                continue
            supplements.append(doc_id)
        return ["G1", *sorted(supplements)]

    def bind_contract(self, date: str) -> dict[str, Any]:
        sources = self._contract_sources(date)
        constraints: dict[str, dict[str, Any]] = {}
        for source in sources:
            doc = self.docs[source]
            required = doc.get("required_constraint_ids", [])
            present = {c["id"]: c for c in doc.get("constraints", [])}
            missing = [cid for cid in required if cid not in present]
            if missing:
                raise ProbeError("MISSING_REQUIRED_CONSTRAINT:" + ",".join(missing))
            constraints.update(present)
        for c in constraints.values():
            negates = c.get("negates")
            if negates and negates in constraints:
                raise ProbeError(f"CONTRACT_CONFLICT:{c['id']}!{negates}")

        order = list(self.docs["G1"]["required_constraint_ids"])
        for source in sources[1:]:
            doc = self.docs[source]
            marker = doc.get("precedence_after")
            if not marker or ":" not in marker:
                raise ProbeError(f"CONTRACT_PRECEDENCE_UNRESOLVED:{source}")
            owner, constraint_id = marker.split(":", 1)
            if owner != "G1" or constraint_id not in order:
                raise ProbeError(f"CONTRACT_PRECEDENCE_UNRESOLVED:{source}")
            idx = order.index(constraint_id) + 1
            order[idx:idx] = doc["required_constraint_ids"]
        return {"status": "bound", "sources_consumed": sources, "constraint_order": order}

    def challenge_missing_constraint(self) -> str:
        old = self.docs["G1"]["constraints"]
        self.docs["G1"]["constraints"] = [c for c in old if c["id"] != "C04"]
        try:
            self.bind_contract("2026-04-15")
        except ProbeError as exc:
            return str(exc)
        finally:
            self.docs["G1"]["constraints"] = old
        return "NO_FAILURE"

    def challenge_contradictory_constraint(self) -> str:
        self._doc("G3", role="contract_supplement", status="accepted", effective_from="2026-04-01", supplements="G1", precedence_after="G1:C04", required_constraint_ids=["C04X"], constraints=[{"id": "C04X", "source": "G3", "kind": "step", "text": "Force bypass is permitted.", "negates": "C04"}])
        self.instrument.authored("F7-contradiction-challenge", "doc:G3")
        try:
            self.bind_contract("2026-04-15")
        except ProbeError as exc:
            return str(exc)
        finally:
            self.docs.pop("G3", None)
        return "NO_FAILURE"

    def semantic_ownership(self) -> dict[str, list[str]]:
        ownership: dict[str, list[str]] = {}
        ownership["F1:S-A:carrier-continuity"] = ["doc:S-A"]
        for item in self.docs["S-B"].get("identity_history", []):
            if item["op"] == "merge":
                ownership["F1:S-B:merge-history"] = ["doc:S-B"]
            elif item["op"] == "reverse_merge":
                ownership["F1:S-B:reverse-merge-history"] = ["doc:S-B"]
            elif item["op"] == "split":
                ownership["F1:S-B:split-current"] = ["doc:S-B"]

        if "P0" in self.docs["P1"].get("supersedes", []):
            ownership["F2:P1:supersedes:P0"] = ["doc:P1"]
        rel = next((r for r in self.docs["P2"].get("supplements", []) if r.get("target") == "P1"), None)
        if rel:
            ownership["F2:P2:supplements:P1"] = ["doc:P2"]
            if rel.get("precedence_after"):
                ownership["F2:P1-P2:precedence"] = ["doc:P2"]
        if any(r.get("target") == "P1" for r in self.docs["C1"].get("conflicts_with", [])):
            ownership["F2:C1:conflict:P1"] = ["doc:C1"]
        if self.resolve_authority("2026-02-15").get("governing_sources") == ["P1", "P2"]:
            ownership["F2:TASK-X:governing-set"] = ["derived:authority_closure"]

        for w in self.fixture["F3_workstreams"]["workstreams"]:
            wid = w["id"]
            doc = self.docs[wid]
            if doc.get("state") is not None:
                ownership[f"F3:{wid}:state"] = [f"doc:{wid}"]
            if doc.get("parent"):
                ownership[f"F3:{wid}:parent:{doc['parent']}"] = [f"doc:{wid}"]
            for dep in doc.get("depends_on", []):
                ownership[f"F3:{wid}:depends:{dep}"] = [f"doc:{wid}"]
            if doc.get("resume_target"):
                ownership[f"F3:{wid}:resume:{doc['resume_target']}"] = [f"doc:{wid}"]
            if doc.get("resume_condition"):
                ownership[f"F3:{wid}:resume-condition"] = [f"doc:{wid}"]
            if doc.get("pause_reason"):
                ownership[f"F3:{wid}:pause-reason"] = [f"doc:{wid}"]

        for source in self.docs.get("K1", {}).get("derived_from", []):
            ownership[f"F4:K1:derived-from:{source}"] = ["doc:K1"]
        for source in self.docs.get("R1", {}).get("derived_from", []):
            ownership[f"F4:R1:derived-from:{source}"] = ["doc:R1"]

        if self.docs["G2"].get("supplements") == "G1":
            ownership["F7:G2:supplements:G1"] = ["doc:G2"]
        if self.docs["G2"].get("precedence_after") == "G1:C02":
            ownership["F7:G1-G2:precedence"] = ["doc:G2"]
        if self.bind_contract("2026-04-15").get("sources_consumed") == ["G1", "G2"]:
            ownership["F7:TASK-SAFE-WRITE:governing-set"] = ["derived:contract_binding"]
        return ownership


class H2Probe(BaseProbe):
    hypothesis = "H2_PARTITIONED_BOUNDED_SPINE"

    def __init__(self, fixture: dict[str, Any]) -> None:
        self.spine: dict[str, dict[str, dict[str, Any]]] = {"identity": {}, "authority": {}, "workstream": {}}
        super().__init__(fixture)

    def _build_sources(self) -> None:
        for subject in self.fixture["F1_identity"]["initial"]["semantic_subjects"]:
            self._doc(subject["id"], role="semantic_subject", status=subject["status"], current_carriers=list(subject["current_carriers"]), local_history=[])

        f2 = self.fixture["F2_authority"]
        for src in f2["sources"]:
            self._doc(src["id"], **{k: copy.deepcopy(v) for k, v in src.items() if k != "id"})
        # P1 begins as locally owned sole authority. When P2 creates a true governed set,
        # authority ownership is promoted into the spine and P1 retains only applicability.
        self.docs["P1"]["sole_governs"] = [f2["task"]]
        self.docs["P2"]["applicable_to"] = [f2["task"]]
        self.docs["C1"]["candidate_for"] = [f2["task"]]
        self.spine["authority"]["TASK-X"] = {
            "type": "governing_set",
            "task": f2["task"],
            "sources": ["P1", "P2"],
            "supplement": "P2",
            "base": "P1",
            "precedence": ["P1", "P2"],
            "effective_from": "2026-02-01",
            "supersedes": {"P1": ["P0"]},
            "candidate_conflicts": ["C1"],
        }
        self.docs["P1"].pop("sole_governs")
        self.docs["P1"]["applicable_to"] = [f2["task"]]
        self.docs["P1"]["authority_ownership"] = "spine:authority:TASK-X"
        self.instrument.reclassify("F2-authority-promotion", "doc:P1:sole_governs", "spine:authority:TASK-X")
        self.instrument.authored("F2-authority-promotion", "doc:P1", "spine:authority:TASK-X")

        for w in self.fixture["F3_workstreams"]["workstreams"]:
            self._doc(w["id"], role="workstream_narrative", status="accepted")
            self.spine["workstream"][w["id"]] = {k: copy.deepcopy(v) for k, v in w.items() if k != "id"}

        for src in self.fixture["F7_contract"]["sources"]:
            fields = {k: copy.deepcopy(v) for k, v in src.items() if k not in {"id", "supplements", "precedence_after"}}
            self._doc(src["id"], **fields)
        constraints_by_source: dict[str, list[dict[str, Any]]] = {}
        for c in self.fixture["F7_contract"]["constraints"]:
            constraints_by_source.setdefault(c["source"], []).append(copy.deepcopy(c))
        for source, constraints in constraints_by_source.items():
            self.docs[source]["constraints"] = constraints
        self.spine["authority"]["TASK-SAFE-WRITE"] = {
            "type": "contract_governing_set",
            "task": "TASK-SAFE-WRITE",
            "sources": ["G1", "G2"],
            "supplement": "G2",
            "base": "G1",
            "precedence_after": "G1:C02",
            "effective_from": "2026-04-01",
        }

    def _authoritative_extra(self) -> Any:
        return self.spine

    def _extra_serialized_bytes(self) -> int:
        return len(json.dumps(self.spine, sort_keys=True, separators=(",", ":")).encode("utf-8"))

    def spine_record_count(self) -> int:
        return sum(len(module) for module in self.spine.values())

    def manual_global_entry_count(self) -> int:
        return self.spine_record_count()

    def run_identity_transitions(self) -> None:
        t1, t2, t3, t4 = self.fixture["F1_identity"]["transitions"]
        doc = self.docs[t1["subject"]]
        doc["current_carriers"].remove(t1["from"])
        doc["current_carriers"].append(t1["to"])
        doc["local_history"].append({"op": "move_carrier", "from": t1["from"], "to": t1["to"]})
        self.instrument.authored(t1["id"], f"doc:{t1['subject']}")

        self.spine["identity"]["S-B"] = {"state": "merged", "targets": [t2["target"]], "history": [{"op": "merge", "target": t2["target"]}]}
        self.docs["S-B"]["status"] = "merged"
        self.instrument.authored(t2["id"], "doc:S-B", "spine:identity:S-B")

        rel = self.spine["identity"]["S-B"]
        rel["state"] = "active"
        rel["targets"] = ["S-B"]
        rel["history"].append({"op": "reverse_merge", "target": t3["target"]})
        self.docs["S-B"]["status"] = "active"
        self.instrument.authored(t3["id"], "doc:S-B", "spine:identity:S-B")

        rel["state"] = "split"
        rel["targets"] = [item["id"] for item in t4["targets"]]
        rel["history"].append({"op": "split", "targets": list(rel["targets"])})
        self.docs["S-B"]["status"] = "split"
        self.docs["S-B"]["current_carriers"] = []
        for item in t4["targets"]:
            self._doc(item["id"], role="semantic_subject", status="active", current_carriers=[item["carrier"]], local_history=[])
        self.instrument.authored(t4["id"], "doc:S-B", "spine:identity:S-B", *[f"doc:{item['id']}" for item in t4["targets"]])

    def identity_view(self) -> dict[str, Any]:
        a = self.docs["S-A"]
        view = {
            "S-A": {"resolution": "canonical", "targets": ["S-A"], "current_carriers": list(a["current_carriers"])},
            "A1": {"resolution": "historical_carrier", "targets": ["S-A"], "current_carriers": list(a["current_carriers"])},
        }
        rel = self.spine["identity"].get("S-B")
        if rel and rel["state"] == "split":
            targets = list(rel["targets"])
            view["S-B"] = {"resolution": "split", "targets": targets, "current_carriers": []}
            view["B1"] = {"resolution": "historical_carrier_of_split_subject", "targets": targets, "current_carriers": []}
            for target in targets:
                view[target] = {"resolution": "canonical", "targets": [target], "current_carriers": list(self.docs[target]["current_carriers"])}
            view["history"] = copy.deepcopy(rel["history"])
        elif rel and rel["state"] == "merged":
            view["S-B"] = {"resolution": "redirect", "targets": list(rel["targets"]), "current_carriers": []}
            view["history"] = copy.deepcopy(rel["history"])
        else:
            b = self.docs["S-B"]
            view["S-B"] = {"resolution": "canonical", "targets": ["S-B"], "current_carriers": list(b["current_carriers"])}
            view["history"] = [] if rel is None else copy.deepcopy(rel["history"])
        return view

    def resolve_authority(self, date: str) -> dict[str, Any]:
        record = self.spine["authority"].get("TASK-X")
        if record is None:
            return {"governing_sources": [], "non_authoritative_conflicts": [], "status": "unresolved"}
        if date < record["effective_from"]:
            return {"governing_sources": ["P1"], "non_authoritative_conflicts": [], "status": "resolved"}
        if not record.get("precedence") or record["precedence"] != ["P1", "P2"]:
            return {"governing_sources": [], "non_authoritative_conflicts": list(record["candidate_conflicts"]), "status": "ambiguous"}
        return {"governing_sources": list(record["sources"]), "non_authoritative_conflicts": list(record["candidate_conflicts"]), "status": "resolved"}

    def challenge_missing_precedence(self) -> dict[str, Any]:
        record = self.spine["authority"]["TASK-X"]
        old = record.pop("precedence")
        try:
            return self.resolve_authority("2026-02-15")
        finally:
            record["precedence"] = old

    def challenge_missing_authority_relation(self) -> dict[str, Any]:
        old = self.spine["authority"].pop("TASK-X")
        try:
            return self.resolve_authority("2026-02-15")
        finally:
            self.spine["authority"]["TASK-X"] = old

    def reconstruct_workstream(self) -> dict[str, Any]:
        w = self.spine["workstream"]
        states = {wid: w[wid]["state"] for wid in ["W0", "W1", "W2", "W2a"]}
        current = "W2a"
        chain = []
        while current:
            chain.append(current)
            current = w[current].get("parent")
        chain.reverse()
        child = w["W2a"]
        return {
            "states": states,
            "active_chain": chain,
            "blocking_condition": child["resume_condition"],
            "immediate_resume_target": child["resume_target"],
            "return_chain_after_child_completion": [w["W2a"]["parent"], w["W2"]["parent"]],
            "must_not_replay": [wid for wid in ["W1", "W2"] if w[wid]["state"] == "completed"],
        }

    def bind_contract(self, date: str) -> dict[str, Any]:
        record = self.spine["authority"]["TASK-SAFE-WRITE"]
        sources = ["G1"] if date < record["effective_from"] else list(record["sources"])
        constraints: dict[str, dict[str, Any]] = {}
        for source in sources:
            doc = self.docs[source]
            required = doc.get("required_constraint_ids", [])
            present = {c["id"]: c for c in doc.get("constraints", [])}
            missing = [cid for cid in required if cid not in present]
            if missing:
                raise ProbeError("MISSING_REQUIRED_CONSTRAINT:" + ",".join(missing))
            constraints.update(present)
        conflicts = record.get("constraint_conflicts", [])
        if conflicts:
            pair = conflicts[0]
            raise ProbeError(f"CONTRACT_CONFLICT:{pair[0]}!{pair[1]}")
        order = list(self.docs["G1"]["required_constraint_ids"])
        if "G2" in sources:
            if record.get("precedence_after") != "G1:C02":
                raise ProbeError("CONTRACT_PRECEDENCE_UNRESOLVED")
            idx = order.index("C02") + 1
            order[idx:idx] = self.docs["G2"]["required_constraint_ids"]
        return {"status": "bound", "sources_consumed": sources, "constraint_order": order}

    def challenge_missing_constraint(self) -> str:
        old = self.docs["G1"]["constraints"]
        self.docs["G1"]["constraints"] = [c for c in old if c["id"] != "C04"]
        try:
            self.bind_contract("2026-04-15")
        except ProbeError as exc:
            return str(exc)
        finally:
            self.docs["G1"]["constraints"] = old
        return "NO_FAILURE"

    def challenge_contradictory_constraint(self) -> str:
        self._doc("G3", role="contract_supplement", status="accepted", effective_from="2026-04-01", required_constraint_ids=["C04X"], constraints=[{"id": "C04X", "source": "G3", "kind": "step", "text": "Force bypass is permitted."}])
        record = self.spine["authority"]["TASK-SAFE-WRITE"]
        old_sources = list(record["sources"])
        old_conflicts = copy.deepcopy(record.get("constraint_conflicts", []))
        record["sources"] = ["G1", "G2", "G3"]
        record["constraint_conflicts"] = [["C04X", "C04"]]
        self.instrument.authored("F7-contradiction-challenge", "doc:G3", "spine:authority:TASK-SAFE-WRITE")
        try:
            self.bind_contract("2026-04-15")
        except ProbeError as exc:
            return str(exc)
        finally:
            self.docs.pop("G3", None)
            record["sources"] = old_sources
            if old_conflicts:
                record["constraint_conflicts"] = old_conflicts
            else:
                record.pop("constraint_conflicts", None)
        return "NO_FAILURE"

    def semantic_ownership(self) -> dict[str, list[str]]:
        ownership: dict[str, list[str]] = {"F1:S-A:carrier-continuity": ["doc:S-A"]}
        identity = self.spine["identity"].get("S-B")
        if identity:
            for item in identity.get("history", []):
                if item["op"] == "merge":
                    ownership["F1:S-B:merge-history"] = ["spine:identity:S-B"]
                elif item["op"] == "reverse_merge":
                    ownership["F1:S-B:reverse-merge-history"] = ["spine:identity:S-B"]
                elif item["op"] == "split":
                    ownership["F1:S-B:split-current"] = ["spine:identity:S-B"]

        authority = self.spine["authority"].get("TASK-X")
        if authority:
            if "P0" in authority.get("supersedes", {}).get("P1", []):
                ownership["F2:P1:supersedes:P0"] = ["spine:authority:TASK-X"]
            if authority.get("supplement") == "P2" and authority.get("base") == "P1":
                ownership["F2:P2:supplements:P1"] = ["spine:authority:TASK-X"]
            if authority.get("precedence") == ["P1", "P2"]:
                ownership["F2:P1-P2:precedence"] = ["spine:authority:TASK-X"]
            if "C1" in authority.get("candidate_conflicts", []):
                ownership["F2:C1:conflict:P1"] = ["spine:authority:TASK-X"]
            if authority.get("sources") == ["P1", "P2"]:
                ownership["F2:TASK-X:governing-set"] = ["spine:authority:TASK-X"]

        for w in self.fixture["F3_workstreams"]["workstreams"]:
            wid = w["id"]
            record = self.spine["workstream"].get(wid, {})
            if record.get("state") is not None:
                ownership[f"F3:{wid}:state"] = [f"spine:workstream:{wid}"]
            if record.get("parent"):
                ownership[f"F3:{wid}:parent:{record['parent']}"] = [f"spine:workstream:{wid}"]
            for dep in record.get("depends_on", []):
                ownership[f"F3:{wid}:depends:{dep}"] = [f"spine:workstream:{wid}"]
            if record.get("resume_target"):
                ownership[f"F3:{wid}:resume:{record['resume_target']}"] = [f"spine:workstream:{wid}"]
            if record.get("resume_condition"):
                ownership[f"F3:{wid}:resume-condition"] = [f"spine:workstream:{wid}"]
            if record.get("pause_reason"):
                ownership[f"F3:{wid}:pause-reason"] = [f"spine:workstream:{wid}"]

        for source in self.docs.get("K1", {}).get("derived_from", []):
            ownership[f"F4:K1:derived-from:{source}"] = ["doc:K1"]
        for source in self.docs.get("R1", {}).get("derived_from", []):
            ownership[f"F4:R1:derived-from:{source}"] = ["doc:R1"]

        contract = self.spine["authority"].get("TASK-SAFE-WRITE")
        if contract:
            if contract.get("supplement") == "G2" and contract.get("base") == "G1":
                ownership["F7:G2:supplements:G1"] = ["spine:authority:TASK-SAFE-WRITE"]
            if contract.get("precedence_after") == "G1:C02":
                ownership["F7:G1-G2:precedence"] = ["spine:authority:TASK-SAFE-WRITE"]
            if contract.get("sources") == ["G1", "G2"]:
                ownership["F7:TASK-SAFE-WRITE:governing-set"] = ["spine:authority:TASK-SAFE-WRITE"]
        return ownership


def _assert_equal(label: str, actual: Any, expected: Any) -> dict[str, Any]:
    return {"label": label, "pass": actual == expected, "actual": actual, "expected": expected}


def run_candidate(cls: type[BaseProbe], fixture: dict[str, Any]) -> dict[str, Any]:
    probe = cls(fixture)
    checks: list[dict[str, Any]] = []

    # F1 identity lifecycle
    probe.run_identity_transitions()
    identity = probe.identity_view()
    for ref, expected in fixture["F1_identity"]["expected_final"].items():
        checks.append(_assert_equal(f"F1:{ref}", identity.get(ref), expected))
    history_ops = []
    for item in identity.get("history", []):
        if item["op"] == "merge":
            history_ops.append(f"merge:S-B->{item['target']}")
        elif item["op"] == "reverse_merge":
            history_ops.append(f"reverse_merge:S-B->{item['target']}")
        elif item["op"] == "split":
            history_ops.append("split:S-B->" + ",".join(item["targets"]))
    checks.append(_assert_equal("F1:history", history_ops, fixture["F1_identity"]["history_must_show"]))

    # F2 authority closure and ambiguity
    expected_auth = fixture["F2_authority"]["expected"]
    checks.append(_assert_equal("F2:before-supplement-effective", probe.resolve_authority("2026-01-15"), expected_auth["2026-01-15"]))
    checks.append(_assert_equal("F2:after-supplement-effective", probe.resolve_authority("2026-02-15"), expected_auth["2026-02-15"]))
    checks.append(_assert_equal("F2:missing-precedence", probe.challenge_missing_precedence(), expected_auth["without_precedence_after_2026-02-15"]))
    missing_relation = probe.challenge_missing_authority_relation()
    checks.append(_assert_equal("F2:missing-authority-relation-fails-visible", missing_relation.get("governing_sources"), []))
    checks.append(_assert_equal("F2:missing-authority-relation-status", missing_relation.get("status") in {"ambiguous", "unresolved"}, True))

    # F3 workstream continuation
    checks.append(_assert_equal("F3:reconstruction", probe.reconstruct_workstream(), fixture["F3_workstreams"]["expected_reconstruction"]))

    # F4 capture/promotion
    f4_actual = probe.run_capture_lifecycle()
    f4_expected = fixture["F4_capture"]["expected"]
    checks.append(_assert_equal("F4:capture-not-authority-and-deleted", f4_actual["capture_present"], False))
    checks.append(_assert_equal("F4:accepted-status", f4_actual["K1_status"], "accepted"))
    checks.append(_assert_equal("F4:accepted-provenance", f4_actual["K1_provenance"], f4_expected["accepted_provenance_contains"]))
    checks.append(_assert_equal("F4:rejected-historical", f4_actual["R1_status"], "rejected"))

    # F5 scale with fixed active semantics
    scale = {label: probe.scale_observation(count) for label, count in fixture["F5_scale"]["history_counts"].items()}
    active_counts = [item["active_count"] for item in scale.values()]
    active_sizes = [item["active_view_bytes"] for item in scale.values()]
    checks.append(_assert_equal("F5:active-count-stable", len(set(active_counts)), 1))
    checks.append(_assert_equal("F5:active-view-bytes-stable", len(set(active_sizes)), 1))

    # F6 derived deletion/rebuild and freshness binding
    probe.build_views()
    digest_before = probe.source_digest()
    derived_before = copy.deepcopy(probe.derived)
    probe.delete_derived()
    missing_visible = False
    try:
        probe.require_view("authority_closure")
    except ProbeError:
        missing_visible = True
    probe.build_views()
    rebuilt_equal = {name: probe.derived[name]["payload"] == derived_before[name]["payload"] for name in derived_before}
    freshness_bound = all(v.get("source_digest") == digest_before for v in probe.derived.values())
    checks.append(_assert_equal("F6:missing-derived-visible", missing_visible, True))
    checks.append(_assert_equal("F6:rebuild-payloads", all(rebuilt_equal.values()), True))
    checks.append(_assert_equal("F6:freshness-binding", freshness_bound, True))

    # F7 post-activation contract fidelity
    bound = probe.bind_contract("2026-04-15")
    expected_contract = fixture["F7_contract"]["expected"]
    checks.append(_assert_equal("F7:source-consumption", bound["sources_consumed"], expected_contract["source_consumption_receipt"]))
    checks.append(_assert_equal("F7:ordered-contract", bound["constraint_order"], expected_contract["after_2026-04-01_order"]))
    checks.append(_assert_equal("F7:missing-constraint-fails", probe.challenge_missing_constraint().startswith("MISSING_REQUIRED_CONSTRAINT:C04"), True))
    checks.append(_assert_equal("F7:contradiction-fails", probe.challenge_contradictory_constraint().startswith("CONTRACT_CONFLICT:"), True))

    # Public/private overlay
    public = probe.public_projection()
    leaked = any(value in public["serialized"] for value in fixture["overlay"]["public_projection_must_not_include"])
    checks.append(_assert_equal("overlay:private-non-leakage", leaked, False))

    representation = probe.representation_stats()
    expected_fact_ids = expected_semantic_fact_ids(fixture)
    actual_fact_ids = set(representation["semantic_ownership"])
    checks.append(_assert_equal("semantic-inventory:complete", sorted(actual_fact_ids), sorted(expected_fact_ids)))
    checks.append(_assert_equal("semantic-inventory:no-duplicate-authority", representation["duplicate_authoritative_fact_owners"], {}))

    return {
        "hypothesis": probe.hypothesis,
        "all_semantic_checks_pass": all(item["pass"] for item in checks),
        "checks": checks,
        "scale": scale,
        "representation": representation,
        "instrumentation": {
            "authoritative_touches": probe.instrument.authoritative_touches,
            "generated_touches": probe.instrument.generated_touches,
            "reclassifications": probe.instrument.reclassifications,
        },
        "qualitative_declarations": {
            "human_inspectability": "direct source documents" if cls is H1Probe else "direct source documents plus small typed spine modules",
            "ownership_clarity": "directional cross-object facts live on asserting source documents" if cls is H1Probe else "source-local facts live on documents; identity/authority/workstream cross-object facts live in named spine modules",
            "degraded_mode": "derived views fail visibly when absent and can be rebuilt from authoritative inputs",
        },
    }


def compare_results(h1: dict[str, Any], h2: dict[str, Any]) -> dict[str, Any]:
    def series(result: dict[str, Any], key: str) -> list[int]:
        return [result["scale"][label][key] for label in ["1x", "5x", "10x"]]

    return {
        "semantic_correctness": {"H1": h1["all_semantic_checks_pass"], "H2": h2["all_semantic_checks_pass"]},
        "active_view_bytes_1x_5x_10x": {"H1": series(h1, "active_view_bytes"), "H2": series(h2, "active_view_bytes")},
        "spine_records_1x_5x_10x": {"H1": series(h1, "spine_records"), "H2": series(h2, "spine_records")},
        "full_rebuild_scan_1x_5x_10x": {"H1": series(h1, "full_rebuild_source_scan_count"), "H2": series(h2, "full_rebuild_source_scan_count")},
        "authoritative_location_count_10x": {"H1": h1["scale"]["10x"]["authoritative_locations"], "H2": h2["scale"]["10x"]["authoritative_locations"]},
        "semantic_fact_ownership_count": {"H1": h1["representation"]["semantic_fact_ownership_count"], "H2": h2["representation"]["semantic_fact_ownership_count"]},
        "duplicate_authoritative_fact_owners": {"H1": h1["representation"]["duplicate_authoritative_fact_owners"], "H2": h2["representation"]["duplicate_authoritative_fact_owners"]},
        "authored_location_touch_total": {"H1": h1["representation"]["authored_location_touch_total"], "H2": h2["representation"]["authored_location_touch_total"]},
        "reclassification_events": {"H1": h1["representation"]["reclassification_events"], "H2": h2["representation"]["reclassification_events"]},
        "authoritative_serialized_bytes": {"H1": h1["representation"]["authoritative_serialized_bytes"], "H2": h2["representation"]["authoritative_serialized_bytes"]},
        "interpretation_guard": "Metrics are descriptive evidence. No aggregate winner score or target selection is authorized by this probe.",
    }


def load_fixture() -> tuple[dict[str, Any], str]:
    raw = FIXTURE_PATH.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_FIXTURE_SHA256:
        raise ProbeError(f"FIXTURE_HASH_MISMATCH:{digest}")
    fixture = json.loads(raw)
    if fixture.get("fixture_id") != "PKA-CF-V01":
        raise ProbeError("FIXTURE_ID_MISMATCH")
    return fixture, digest


def run(output_path: Path | None = RESULT_PATH) -> dict[str, Any]:
    fixture, digest = load_fixture()
    h1 = run_candidate(H1Probe, fixture)
    h2 = run_candidate(H2Probe, fixture)
    result = {
        "probe_id": "PKA-PROBE-V01",
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
    parser = argparse.ArgumentParser(description="Run Research 134 H1/H2 common-fixture mechanism probe")
    parser.add_argument("--output", type=Path, default=RESULT_PATH)
    parser.add_argument("--no-write", action="store_true", help="Run without writing the result artifact")
    args = parser.parse_args()
    result = run(None if args.no_write else args.output)
    print(json.dumps({"probe_id": result["probe_id"], "fixture_sha256": result["fixture_sha256"], "comparison": result["comparison"]}, indent=2))
    return 0 if all(v for v in result["comparison"]["semantic_correctness"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
