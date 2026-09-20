"""Restricted shared unique-value unit: declarations only."""


def unique_values(values):
    result = []
    for value in sorted_values(values):
        if value not in result:
            result = result + [value]
    return result
