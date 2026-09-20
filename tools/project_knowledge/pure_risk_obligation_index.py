"""Restricted risk/obligation-index units: declarations only."""


def obligation_rows(item):
    declaration = item["declaration"]
    rows = []
    if item["profile"] == "governing_procedure.v1" and item["state"] == "ACTIVE":
        categories = [
            ("PRECONDITION", "preconditions"),
            ("PROHIBITION", "prohibitions"),
            ("POSTCONDITION", "required_postconditions"),
            ("FAIL_CLOSED", "fail_closed_conditions"),
        ]
        for category, field in categories:
            values = declaration[field]
            for ordinal in sequence_range(length(values)):
                rows = rows + [{
                    "source_path": item["source_path"],
                    "semantic_id": item["semantic_id"],
                    "category": category,
                    "ordinal": ordinal,
                    "constraint_id": None,
                    "requirement": values[ordinal],
                }]
        constraints = declaration["mandatory_constraints"]
        for ordinal in sequence_range(length(constraints)):
            constraint = constraints[ordinal]
            rows = rows + [{
                "source_path": item["source_path"],
                "semantic_id": item["semantic_id"],
                "category": "MANDATORY_CONSTRAINT",
                "ordinal": ordinal,
                "constraint_id": constraint["constraint_id"],
                "requirement": constraint["requirement"],
            }]
    if item["profile"] == "workstream.v1" and "expected_to_resume" in declaration:
        if (item["state"] in ["PAUSED", "BLOCKED"]
                and declaration["expected_to_resume"] == True
                and "return_condition" in declaration):
            rows = rows + [{
                "source_path": item["source_path"],
                "semantic_id": item["semantic_id"],
                "category": "RETURN_CONDITION",
                "ordinal": 0,
                "constraint_id": None,
                "requirement": declaration["return_condition"],
            }]
    return rows


def risk_obligation_index(inputs):
    risks = []
    obligations = []
    for item in inputs:
        if item["authority_class"] == "canonical" and item["state"] != "SUPERSEDED":
            declaration = item["declaration"]
            if "risk_or_reopen_triggers" in declaration:
                for trigger in unique(declaration["risk_or_reopen_triggers"]):
                    risks = risks + [{
                        "source_path": item["source_path"],
                        "semantic_id": item["semantic_id"],
                        "trigger": trigger,
                    }]
            obligations = obligations + obligations_for(item)
    risk_keyed = sorted_values([
        (row["trigger"], row["semantic_id"] if row["semantic_id"] != None else "",
         row["source_path"], row) for row in risks
    ])
    obligation_keyed = sorted_values([
        (row["source_path"], row["category"], row["ordinal"],
         row["constraint_id"] if row["constraint_id"] != None else "", row) for row in obligations
    ])
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "risks": [row for trigger, identity, path, row in risk_keyed],
        "obligations": [row for path, category, ordinal, constraint_id, row in obligation_keyed],
    }
