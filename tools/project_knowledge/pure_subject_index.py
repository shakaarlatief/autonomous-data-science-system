"""Restricted subject-index units: declarations only."""


def subject_memberships(item):
    declaration = item["declaration"]
    identity = item["semantic_id"]
    rows = [
        ("profile", item["profile"], identity if identity != None else "", item["source_path"]),
        ("kind", declaration["kind"], identity if identity != None else "", item["source_path"]),
    ]
    if "scope" in declaration:
        for facet in sorted_values(declaration["scope"]):
            value = declaration["scope"][facet]
            values = [value] if is_text(value) else unique(value)
            for member in values:
                rows = rows + [("scope:" + facet, member,
                                identity if identity != None else "", item["source_path"])]
    return rows


def subject_index(inputs):
    keyed = []
    for item in inputs:
        if item["authority_class"] == "canonical" and item["state"] != "SUPERSEDED":
            keyed = keyed + memberships(item)
    rows = []
    for axis, value, identity, path in sorted_values(keyed):
        rows = rows + [{
            "axis": axis,
            "value": value,
            "semantic_id": identity if identity != "" else None,
            "source_path": path,
        }]
    return {"schema_version": "1", "authority_class": "derived", "memberships": rows}
