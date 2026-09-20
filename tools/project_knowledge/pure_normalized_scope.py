"""Restricted shared scope-normalization unit: declarations only."""


def normalized_scope(scope):
    result = {}
    for key in sorted_values(scope):
        value = scope[key]
        if is_text(value):
            result = {**result, key: value}
        else:
            result = {**result, key: unique(value)}
    return result
