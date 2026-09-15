"""L2: strict carrier extraction. Schema validation belongs to orchestration."""

import json
import re

from .model import Profile, RawDeclaration, SubstrateError


BEGIN = "<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->"
END = "<!-- PKA-STRUCTURED-DECLARATION-END -->"
# Recognize malformed attempts too; never downgrade a present marker to absence.
_MARKER_INTENT = re.compile(r"(?:<!--\s*)?PKA[\s_-]*STRUCTURED[\s_-]*DECLARATION", re.I)
_FENCE_OPEN = re.compile(r" {0,3}(`{3,}|~{3,})(.*)\Z")


def _decode(content: bytes) -> str:
    try:
        return content.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise SubstrateError("INVALID_UTF8", "Declaration carrier must be UTF-8") from error


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise SubstrateError("DUPLICATE_JSON_KEY", f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _invalid_constant(value):
    raise SubstrateError("INVALID_JSON", f"Non-JSON numeric constant: {value}")


def _json_object(text: str):
    try:
        return json.loads(text, object_pairs_hook=_unique_object, parse_constant=_invalid_constant)
    except SubstrateError:
        raise
    except (ValueError, RecursionError) as error:
        raise SubstrateError("INVALID_JSON", "Declaration must contain strict JSON") from error


def _declaration(value) -> RawDeclaration:
    if not isinstance(value, dict):
        raise SubstrateError("NON_OBJECT_DECLARATION", "Declaration must be a JSON object")
    try:
        Profile(value.get("profile"))
    except (ValueError, TypeError) as error:
        raise SubstrateError("UNKNOWN_PROFILE", "Declaration needs a supported explicit profile") from error
    return RawDeclaration(value)


def parse_markdown(content: bytes) -> RawDeclaration | None:
    """Recognize standalone declaration lines outside ordinary Markdown fences.

    Fences follow the backtick/tilde length and closing rules: up to three
    leading spaces, matching fence character, closing run at least as long as
    the opener, and only whitespace after a closer. An unclosed fence extends
    to EOF. Once a declaration opens, its body is strict JSON, not Markdown;
    a fence inside that body cannot hide malformed JSON or a missing end.
    """
    text = _decode(content)
    fence: str | None = None
    body: list[str] | None = None
    complete = False
    for line in text.splitlines(keepends=True):
        marker_line = line.removesuffix("\n").removesuffix("\r")
        if body is None or complete:
            if fence is not None:
                if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}[ \t]*", marker_line):
                    fence = None
                continue
            opener = _FENCE_OPEN.fullmatch(marker_line)
            if opener and (opener[1][0] != "`" or "`" not in opener[2]):
                fence = opener[1]
                continue
        if _MARKER_INTENT.search(marker_line):
            if marker_line == BEGIN and body is None:
                body = []
            elif marker_line == END and body is not None and not complete:
                complete = True
            else:
                raise SubstrateError("MALFORMED_DECLARATION_MARKERS", "Expected one pair of exact standalone declaration marker lines outside fences")
        elif body is not None and not complete:
            body.append(line)
    if body is None:
        return None
    if not complete:
        raise SubstrateError("MALFORMED_DECLARATION_MARKERS", "Declaration is missing its end marker")
    return _declaration(_json_object("".join(body)))


def parse_native_json(content: bytes) -> RawDeclaration | None:
    """An explicit profile opts a JSON object into this substrate.

    Unrelated JSON is not a governed source. An explicit profile claim is never
    silently ignored; compatibility carriers are not modified by this reader.
    """
    text = _decode(content)
    try:
        candidate = json.loads(text)
    except (ValueError, RecursionError):
        # Decode key tokens so escaped spellings cannot hide a malformed claim.
        keys = re.finditer(r'("(?:[^"\\]|\\.)*")\s*:', text)
        claimed = False
        for key in keys:
            try:
                claimed = claimed or json.loads(key.group(1)) == "profile"
            except ValueError:
                continue
        if not claimed:
            return None
    else:
        if not isinstance(candidate, dict) or "profile" not in candidate:
            return None
    value = _json_object(text)
    if not isinstance(value, dict) or "profile" not in value:
        return None
    return _declaration(value)
