"""Existing governed source grammar audit over the exposed historical 65.

Use native Specification 025/028 parsers. These are parseable source claims,
not independently adjudicated semantic gold or operative governance.
"""
from __future__ import annotations
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import tempfile

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import ANNOTATIONS, ROOT, load, source_at_revision
from experiments.r0_p03_navigation_probe.exploratory_hybrid_fusion_and_routing_v01 import PIN, SOURCE_SHA256
from experiments.r0_p03_navigation_probe.exploratory_reference_provenance_audit_v01 import RESULT as V01, git_blob_sha1
from experiments.r0_p03_navigation_probe.exploratory_reference_declaration_correction_v02 import RESULT as V02
from scripts.repository_integrity import FAMILY_CONTRACTS, RELATIONSHIP_FIELDS, read_header_fields, parse_declared_reference_field, existing_relationship_reference
from tools.project_knowledge.declaration import BEGIN, END, parse_markdown

IDENTIFIER = "EXPLORATORY_SOURCE_OWNED_DECLARATION_AUDIT_V03"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_governed_reference_audit_result_v03.json"
CONTRACT = "EXPLORATORY_GOVERNED_DECLARATION_REFERENCE_AUDIT_CONTRACT_V03.md"
V01_SHA = "e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299"
V02_SHA = "25b26e66e3bb03232d4ee7931e66aceb6bd6eaf28d2f5ae0ff207713c333831d"


def numbered_index(paths):
    index = {}
    for contract in FAMILY_CONTRACTS:
        for p in paths:
            path = Path(p)
            number = path.name.split("_", 1)[0]
            if path.parent.as_posix() == contract.directory.as_posix() and number.isdigit():
                key = contract.key, int(number)
                if key in index:
                    raise ValueError("nonunique sampled numbered identity")
                index[key] = p
    return index


def resolve_token(token, source, paths, index):
    family, colon, selector = token.partition(":")
    fragment = None
    if "#" in selector:
        selector, fragment = selector.split("#", 1)
    target = None
    if colon and family == "path":
        target = selector if selector in paths else None
    elif colon and family in {c.key for c in FAMILY_CONTRACTS} and selector.isdigit():
        target = index.get((family, int(selector)))
    state = "RESOLVED_IN_65" if target and target != source else (
        "SELF_REFERENCE" if target == source else "OUTSIDE_SAMPLED_65_OR_UNRESOLVED"
    )
    return {
        "target_original_token": token,
        "target_family": family if colon else "UNTYPED_IDENTITY",
        "target_selector": selector if colon else token,
        "target_fragment": fragment,
        "target_member_in_sample": target,
        "resolution_state": state,
    }


def header_witness(text, token):
    for n, line in enumerate(text.splitlines()[:100], 1):
        if line.startswith("## "):
            break
        if line.strip().startswith("**Declared references:**"):
            if (chr(96) + token + chr(96)) in line:
                return [(n, line)]
    raise ValueError("parsed declared token lacks original header source witness")


def structured_witness(text, token):
    lines = text.splitlines()
    starts = [i for i, line in enumerate(lines) if line == BEGIN]
    ends = [i for i, line in enumerate(lines) if line == END]
    # Specification 028 itself contains a second marker example inside an
    # ordinary Markdown fence. The native parser has already accepted the
    # actual declaration. The first original exact marker pair is its
    # recognized source block in these pinned originals.
    if not starts or not ends:
        raise ValueError("recognized structured declaration missing marker range")
    first = starts[0]
    end = next((n for n in ends if n > first), None)
    if end is None:
        raise ValueError("recognized structured declaration missing closing marker")
    exact = json.dumps(token, ensure_ascii=False)
    found = [(i + 1, lines[i]) for i in range(first + 1, end) if exact in lines[i]]
    if not found:
        raise ValueError("typed structured token lacks original source text witness")
    return found


def make_entry(source, raw, slot, token, witnesses, paths, index, profile=None, authority_class=None):
    return {
        "source_path": source,
        "source_sha256": sha256(raw).hexdigest(),
        "source_blob_sha1": git_blob_sha1(raw),
        "grammar_slot": slot,
        "raw_typed_token": token,
        "source_witnesses": [
            {"line_number": n, "original_line": line, "line_sha256": sha256(line.encode("utf-8")).hexdigest()}
            for n, line in witnesses
        ],
        "declared_profile": profile,
        "declared_authority_class": authority_class,
        "authority_qualified": False,
        **resolve_token(token, source, paths, index),
    }


def run():
    if sha256(V01.read_bytes()).hexdigest() != V01_SHA or sha256(V02.read_bytes()).hexdigest() != V02_SHA:
        raise ValueError("preceding V01/V02 evidence has changed")
    earlier = json.loads(V02.read_text(encoding="utf-8"))
    annotations = load(ANNOTATIONS)
    if annotations["source_boundary"] != PIN:
        raise ValueError("historical Git revision drift")
    sources = sorted(row["path"] for row in annotations["annotations"])
    if len(sources) != 65 or len(set(sources)) != 65:
        raise ValueError("historical source roster drift")
    paths = set(sources)
    originals = {p: source_at_revision(PIN, p) for p in sources}
    digest = sha256(json.dumps(
        [[p, sha256(originals[p]).hexdigest()] for p in sources],
        separators=(",", ":"), ensure_ascii=True,
    ).encode("ascii")).hexdigest()
    if digest != SOURCE_SHA256:
        raise ValueError("original historical source fingerprint changed")
    index = numbered_index(paths)
    entries = []
    headers = []
    profiles = []
    header_count = 0
    structured_count = 0
    with tempfile.TemporaryDirectory(dir=ROOT / ".venv") as tmp:
        scratch = Path(tmp) / "source.md"
        for source in sources:
            raw = originals[source]
            text = raw.decode("utf-8")
            scratch.write_bytes(raw)
            fields = read_header_fields(scratch)
            if "Declared references" in fields:
                tokens, problem = parse_declared_reference_field(fields["Declared references"])
                if problem:
                    raise ValueError(f"native header parser failed for {source}: {problem}")
                header_count += 1
                for token in tokens:
                    entries.append(make_entry(
                        source, raw, "SPEC025_DECLARED_REFERENCES", token,
                        header_witness(text, token), paths, index,
                    ))
            for field in sorted(RELATIONSHIP_FIELDS & fields.keys()):
                recognized = existing_relationship_reference(fields[field])
                headers.append({
                    "source": source, "header_field": field, "raw_value": fields[field],
                    "target_syntax": list(recognized) if recognized else None,
                    "authority_qualified": False,
                })
            declaration = parse_markdown(raw)
            if declaration is None:
                continue
            structured_count += 1
            obj = declaration.fields
            profile = str(obj["profile"])
            authority = str(obj.get("authority_class", "NOT_DECLARED"))
            profiles.append({
                "source": source, "profile": profile,
                "declared_authority_class": authority,
                "declared_semantic_id": obj.get("semantic_id"),
                "declared_state": obj.get("state"),
                "relations_slot_count": len(obj.get("relations", ())),
            })
            for slot in ("references", "provenance"):
                for token in obj.get(slot, ()):
                    if not isinstance(token, str):
                        raise ValueError("non-string token in native structured parser")
                    entries.append(make_entry(
                        source, raw, "SPEC028_" + slot.upper(), token,
                        structured_witness(text, token), paths, index, profile, authority,
                    ))

    entries.sort(key=lambda x: (x["source_path"], x["grammar_slot"], x["raw_typed_token"]))
    owned = {(x["source_path"], x["target_member_in_sample"])
             for x in entries if x["resolution_state"] == "RESOLVED_IN_65"}
    old = {tuple(pair) for pair in earlier["summary"]["source_coverage_by_projection"]["RAW_PATH_MENTIONS"]["edges"]}
    if len(old) != 110:
        raise ValueError("previous path-only graph drift")
    per_slot = Counter(x["grammar_slot"] for x in entries)
    in_slot = Counter(x["grammar_slot"] for x in entries if x["resolution_state"] == "RESOLVED_IN_65")
    old_forward = {a for a, b in old}
    old_reverse = {b for a, b in old}
    owned_forward = {a for a, b in owned}
    owned_reverse = {b for a, b in owned}
    stats = {
        "source_documents": len(sources),
        "header_declaring_documents": header_count,
        "structured_declaring_documents": structured_count,
        "source_owned_tokens": len(entries),
        "all_tokens_by_grammar_slot": dict(sorted(per_slot.items())),
        "in_corpus_tokens_by_grammar_slot": dict(sorted(in_slot.items())),
        "in_corpus_distinct_declared_pairs": len(owned),
        "in_corpus_pairs_also_in_old_110_path_graph": len(owned & old),
        "in_corpus_pairs_missing_from_old_path_graph": len(owned - old),
        "missing_from_old_path_graph": [{"source": a, "target": b} for a, b in sorted(owned - old)],
        "out_of_sample_or_unresolved_tokens": sum(
            x["resolution_state"] == "OUTSIDE_SAMPLED_65_OR_UNRESOLVED" for x in entries
        ),
        "tokens_with_preserved_fragments": sum(x["target_fragment"] is not None for x in entries),
        "old_empty_forward_sources_with_declared_in_corpus_references": sorted(owned_forward - old_forward),
        "old_empty_reverse_sources_with_declared_in_corpus_references": sorted(owned_reverse - old_reverse),
        "old_path_graph_directed_pairs": len(old),
    }
    return {
        "identifier": IDENTIFIER, "contract": CONTRACT,
        "classification": "EXPOSED_GOVERNED_PARSER_SOURCE_DECLARATION_AUDIT_NOT_GOLD",
        "historical_revision": PIN, "source_fingerprint_sha256": digest,
        "prior_v01_sha256": V01_SHA, "prior_v02_sha256": V02_SHA,
        "parsed_source_owned_entries": entries,
        "structured_profile_claims": profiles,
        "other_header_relationship_fields": headers,
        "summary": stats,
        "limitations": [
            "Existing parser acceptance is not complete schema/semantic/currentness validation.",
            "Source declarations from exposed 65 documents are not independent user gold.",
            "References and provenance are separate relation classes, not one authority claim.",
            "Missing target from sampled 65 is not missing target from repository.",
            "Fragment is preserved as a selector, not authenticated as accepted decision identity.",
            "Reviewer's provisional 29/10 and independently observed 31/12 require trace-level reconciliation.",
            "No original R0-P03 B0-B4 score, production implementation or physical target selection.",
        ],
        "formal_r0_p03_scored": False,
    }


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", action="store_true")
    args = ap.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print(json.dumps({
        "id": result["identifier"], "summary": result["summary"],
        "written": args.output,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
