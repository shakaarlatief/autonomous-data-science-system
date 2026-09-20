"""Restricted shared temporal-control unit: declarations only."""


def has_temporal_control(declaration):
    return ("effective_from" in declaration or "effective_to" in declaration
            or "authority_from" in declaration or "authority_to" in declaration)
