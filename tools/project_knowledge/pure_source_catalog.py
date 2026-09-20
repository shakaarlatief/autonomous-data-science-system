"""Restricted source-catalog units: declarations only."""


def catalog_entry(item):
    declaration = item["declaration"]
    return {
        "source_path": item["source_path"],
        "semantic_id": item["semantic_id"],
        "profile": item["profile"],
        "kind": declaration["kind"],
        "state": item["state"],
        "scope": normalize_scope(declaration["scope"]) if "scope" in declaration else {},
        "content_digest": item["content_digest"],
    }


def source_catalog(inputs):
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "sources": [catalog(item) for item in inputs
                    if item["authority_class"] == "canonical" and item["state"] != "SUPERSEDED"],
    }
