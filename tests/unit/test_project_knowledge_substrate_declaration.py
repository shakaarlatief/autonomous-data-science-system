from __future__ import annotations

import json
import sys

import pytest

from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.declaration import BEGIN, END, parse_markdown, parse_native_json
from tools.project_knowledge.model import SubstrateError
from tools.project_knowledge.services.validation import validate_declaration


VALUE = {"schema_version": "1", "profile": "semantic_source.v1", "kind": "note", "authority_class": "canonical"}


def block(value=VALUE, newline="\n"):
    return (BEGIN + newline + json.dumps(value) + newline + END).encode()


@pytest.mark.parametrize("newline", ["\n", "\r\n"])
def test_g003_markdown_native_convergence_without_rewrite(newline):
    content = b"# Context" + newline.encode() + block(newline=newline) + b"\nProse"
    before = bytes(content)
    assert parse_markdown(content) == parse_native_json(json.dumps(VALUE).encode())
    assert content == before


@pytest.mark.parametrize("content", [b"", b"# Ordinary prose", b"{\"other\":true}"])
def test_clean_markdown_absence(content):
    assert parse_markdown(content) is None


@pytest.mark.parametrize("content", [b"{}", b"[]", b'{"kind":"ordinary"}', b'{"schema_version":"1"}'])
def test_native_undeclared_files_are_not_semantic_sources(content):
    assert parse_native_json(content) is None


@pytest.mark.parametrize("content,code", [
    (block() + block(), "MALFORMED_DECLARATION_MARKERS"),
    (END.encode(), "MALFORMED_DECLARATION_MARKERS"),
    (BEGIN.encode(), "MALFORMED_DECLARATION_MARKERS"),
    ((END + BEGIN).encode(), "MALFORMED_DECLARATION_MARKERS"),
    (block().replace(BEGIN.encode(), BEGIN.lower().encode()), "MALFORMED_DECLARATION_MARKERS"),
    (block().lower(), "MALFORMED_DECLARATION_MARKERS"),
    (block().replace(b"BEGIN -->", b"BEGIN-->"), "MALFORMED_DECLARATION_MARKERS"),
    (block().replace(b"BEGIN", b"START"), "MALFORMED_DECLARATION_MARKERS"),
    (block().replace(b"STRUCTURED-", b"STRUCTURED_"), "MALFORMED_DECLARATION_MARKERS"),
    (block().replace(b"<!--", b"<!-"), "MALFORMED_DECLARATION_MARKERS"),
    (block().replace(b"<!-- ", b""), "MALFORMED_DECLARATION_MARKERS"),
    (block() + END.encode(), "MALFORMED_DECLARATION_MARKERS"),
    (block().replace(b"{", b"{// comment\n", 1), "INVALID_JSON"),
    (block().replace(b"}", b"} trailing"), "INVALID_JSON"),
    (block().replace(b"}", b",}"), "INVALID_JSON"),
    (block().replace(b"canonical", b"\xff"), "INVALID_UTF8"),
    (block([]), "NON_OBJECT_DECLARATION"),
    (block(None), "NON_OBJECT_DECLARATION"),
    (block(1), "NON_OBJECT_DECLARATION"),
    (block({**VALUE, "profile": "unknown.v1"}), "UNKNOWN_PROFILE"),
    (block({**VALUE, "profile": {}}), "UNKNOWN_PROFILE"),
    (block({"kind": "note"}), "UNKNOWN_PROFILE"),
])
def test_g003_malformed_present_is_hard_failure(content, code):
    with pytest.raises(SubstrateError) as error:
        parse_markdown(content)
    assert error.value.code == code


@pytest.mark.parametrize("body", [
    '{"profile":"semantic_source.v1","profile":"semantic_source.v1"}',
    '{"profile":"semantic_source.v1","scope":{"x":1,"x":2}}',
    '{"profile":"semantic_source.v1","relations":[{"target":"one","target":"two"}]}',
    '{"profile":"semantic_source.v1","pr\\u006ffile":"semantic_source.v1"}',
])
def test_duplicate_keys_at_all_depths_in_both_carriers(body):
    for parser, content in [(parse_markdown, f"{BEGIN}\n{body}\n{END}".encode()), (parse_native_json, body.encode())]:
        with pytest.raises(SubstrateError) as error:
            parser(content)
        assert error.value.code == "DUPLICATE_JSON_KEY"


@pytest.mark.parametrize("constant", ["NaN", "Infinity", "-Infinity"])
def test_non_json_constants_rejected(constant):
    body = '{"profile":"semantic_source.v1","value":' + constant + '}'
    with pytest.raises(SubstrateError, match="Non-JSON"):
        parse_native_json(body.encode())


def test_orchestrator_schema_failure_and_absence():
    validator = SchemaValidator()
    raw, errors = validate_declaration(block({**VALUE, "surprise": 1}), "docs/source.md", validator)
    assert raw is not None and errors[0].code == "PROFILE_SCHEMA_VIOLATION"
    assert validate_declaration(b"ordinary", "docs/source.md", validator) == (None, ())


@pytest.mark.parametrize("fence", ["```", "~~~", "````", "~~~~"])
@pytest.mark.parametrize("newline", ["\n", "\r\n"])
def test_fenced_examples_are_documentation_and_real_declaration_still_parses(fence, newline):
    example = fence.encode() + b"json" + newline.encode() + block(newline=newline) + newline.encode() + fence.encode() + newline.encode()
    assert parse_markdown(example) is None
    assert parse_markdown(example + block()) == parse_markdown(block())
    assert parse_markdown(block() + b"\n" + example) == parse_markdown(block())


@pytest.mark.parametrize("body", [BEGIN.lower(), END, "<!- PKA-STRUCTURED-DECLARATION-START", BEGIN + "\nnot JSON\n" + END])
@pytest.mark.parametrize("fence", ["```text", "~~~text"])
def test_malformed_fenced_examples_do_not_activate(body, fence):
    assert parse_markdown((fence + "\n" + body + "\n" + fence[:3]).encode()) is None


@pytest.mark.parametrize("opening,interior,closing", [
    ("````md", "```\n", "````"),  # A shorter run cannot close the fence.
    ("~~~", "```\n", "~~~~"),  # Wrong character cannot close; longer can.
    ("  ```md", "```not-a-close\n", "   ```\t"),
    ("```", "~~~~\n", "```"),
])
def test_fence_delimiter_rules(opening, interior, closing):
    document = opening.encode() + b"\n" + interior.encode() + block() + b"\n" + closing.encode() + b"\n"
    assert parse_markdown(document) is None
    assert parse_markdown(document + block()) == parse_markdown(block())


def test_unclosed_fence_extends_to_eof():
    assert parse_markdown(b"```example\n" + block()) is None


def test_two_real_declarations_with_example_between_fail():
    with pytest.raises(SubstrateError) as error:
        parse_markdown(block() + b"\n```\n" + block() + b"\n```\n" + block())
    assert error.value.code == "MALFORMED_DECLARATION_MARKERS"


@pytest.mark.parametrize("begin", [" " + BEGIN, BEGIN + " ", "prose " + BEGIN, BEGIN + " prose", BEGIN.lower()])
def test_actual_marker_lines_must_be_exact_standalone(begin):
    with pytest.raises(SubstrateError) as error:
        parse_markdown(block().replace(BEGIN.encode(), begin.encode()))
    assert error.value.code == "MALFORMED_DECLARATION_MARKERS"


def test_fence_cannot_hide_invalid_body_of_live_declaration():
    with pytest.raises(SubstrateError) as error:
        parse_markdown((BEGIN + "\n```json\n{}\n```\n" + END).encode())
    assert error.value.code == "INVALID_JSON"


def test_native_unknown_profile_is_not_absence():
    with pytest.raises(SubstrateError) as error:
        parse_native_json(b'{"profile":"future.v2"}')
    assert error.value.code == "UNKNOWN_PROFILE"


def test_malformed_native_escaped_profile_is_not_absence():
    with pytest.raises(SubstrateError) as error:
        parse_native_json(b'{"pr\\u006ffile":"semantic_source.v1",}')
    assert error.value.code == "INVALID_JSON"


def test_json_resource_limit_failure_has_stable_diagnostic():
    limit = sys.get_int_max_str_digits()
    if limit == 0:
        pytest.skip("Interpreter integer-string limit is disabled")
    content = ('{"profile":"semantic_source.v1","number":' + "1" * (limit + 1) + '}').encode()
    with pytest.raises(SubstrateError) as error:
        parse_native_json(content)
    assert error.value.code == "INVALID_JSON"
