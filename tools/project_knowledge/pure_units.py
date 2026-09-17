"""Restricted G009 units: declarations only; no module initialization or imports."""


def inventory_entry(item):
    return {"source_path": item["source_path"], "semantic_id": item["semantic_id"],
            "profile": item["profile"], "content_digest": item["content_digest"]}


def source_inventory(inputs):
    return {"schema_version": "1", "authority_class": "derived",
            "sources": [entry(item) for item in inputs]}
