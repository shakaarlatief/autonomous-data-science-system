"""Non-owner cryptographic sensitivity checks for the historical R0-P01 SSH path.

These tests exercise *actual* SSHSIG verification with ephemeral Ed25519 keys
created by the project's Node synthetic-signing endpoint. The private keys
remain inside the child process and are never stored in the repository, read
from the owner's machine, or used to claim an R0-P01 attempt.

A negative test that corrupts the SSHSIG magic header proves only that a
parser rejects malformed input. In contrast, the cases here preserve every
SSHSIG framing field and alter exactly the signature bytes or replace the
embedded public key while retaining another synthetic signer's signature.
A structurally sound but cryptographically invalid signature must be rejected.

These are regression tests against the *historical* verifier implementation,
not evidence that the unfinished successor F1/F2 implementation is frozen.
The conditional comparison here is independent of the B02 retry/attempt cap.
"""

from __future__ import annotations

import base64
import copy
import json
import shutil
import struct
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as original

CONTRACT = Path(original.HERE) / "clarification_vectors_v02.json"
FIXTURE = Path(original.HERE) / "fixture.json"
ARMOR_BEGIN = "-----BEGIN SSH SIGNATURE-----"
ARMOR_END = "-----END SSH SIGNATURE-----"


def _read_ssh_string(blob: bytes, offset: int) -> tuple[bytes, int, int]:
    """Return value, payload offset and next offset for a framed SSH string.

    The SSH binary encoding uses a 32-bit big-endian byte count and explicit
    byte boundaries. This strict parser demonstrates that the test mutation
    has *not* bypassed the verifier by breaking an enclosing length field.
    """
    if offset + 4 > len(blob):
        raise ValueError("truncated SSH string length")
    size = struct.unpack(">I", blob[offset : offset + 4])[0]
    first = offset + 4
    end = first + size
    if end > len(blob):
        raise ValueError("truncated SSH string payload")
    return blob[first:end], first, end


def _read_signature(armor: str) -> dict:
    """Independently parse SSHSIG V1 through its inner Ed25519 signature.

    The top-level payload includes the magic, version and five framed fields:
    public key, namespace, reserved bytes, hash algorithm, and the signature
    packet. The packet itself frames its algorithm and 64 signature bytes.
    All framing and trailing-byte checks are enforced before mutation.
    """
    lines = armor.strip().splitlines()
    if len(lines) < 3 or lines[0] != ARMOR_BEGIN or lines[-1] != ARMOR_END:
        raise ValueError("invalid SSHSIG armor")
    raw = base64.b64decode("".join(lines[1:-1]), validate=True)
    if raw[:6] != b"SSHSIG" or len(raw) < 10:
        raise ValueError("invalid SSHSIG magic")
    if struct.unpack(">I", raw[6:10])[0] != 1:
        raise ValueError("unsupported SSHSIG version")
    offset = 10
    fields = {}
    for name in ("public_key", "namespace", "reserved", "hash", "signature_packet"):
        value, begin, offset = _read_ssh_string(raw, offset)
        fields[name] = (value, begin, offset)
    if offset != len(raw):
        raise ValueError("trailing SSHSIG bytes")
    packet, packet_start, _ = fields["signature_packet"]
    algorithm, _, inner_end = _read_ssh_string(packet, 0)
    signature, sig_start, final = _read_ssh_string(packet, inner_end)
    if (
        algorithm != b"ssh-ed25519"
        or len(signature) != 64
        or final != len(packet)
        or fields["namespace"][0] != b"ads-r0-p01-acceptance"
        or fields["reserved"][0] != b""
        or fields["hash"][0] != b"sha512"
    ):
        raise ValueError("invalid Ed25519 SSHSIG framing")
    fields["raw"] = raw
    fields["signature"] = signature
    fields["signature_offset"] = packet_start + sig_start
    return fields


def _replace_bytes(armor: str, location: int, original_data: bytes, new_data: bytes) -> str:
    """Change one equal-length byte slice without modifying SSHSIG framing."""
    if len(original_data) != len(new_data):
        raise ValueError("new payload must have identical byte length")
    parsed = _read_signature(armor)
    raw = bytearray(parsed["raw"])
    if raw[location : location + len(original_data)] != original_data:
        raise ValueError("mutation location did not match the original data")
    raw[location : location + len(original_data)] = new_data
    encoded = base64.b64encode(raw).decode("ascii")
    result = (
        ARMOR_BEGIN + "\n"
        + "\n".join(encoded[i : i + 70] for i in range(0, len(encoded), 70))
        + "\n" + ARMOR_END + "\n"
    )
    _read_signature(result)
    return result


@pytest.fixture(scope="module")
def statement() -> dict:
    return json.loads(CONTRACT.read_text(encoding="utf-8"))["statement"]


@pytest.fixture(scope="module")
def fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def verifier():
    if not shutil.which("ssh-keygen") or not shutil.which("node"):
        pytest.skip("OpenSSH ssh-keygen and Node are required for cryptographic integration verification")
    node = original.NodeBridge()
    try:
        yield node
    finally:
        node.close()


@pytest.fixture(scope="module")
def signatures(statement, verifier):
    first = verifier.call(
        "synthetic_ssh",
        label="SYNTHETIC-NON-OWNER-CRYPTO-SENSITIVITY-PRIMARY",
        statement=statement,
    )
    second = verifier.call(
        "synthetic_ssh",
        label="SYNTHETIC-NON-OWNER-CRYPTO-SENSITIVITY-OTHER-SIGNER",
        statement=statement,
    )
    assert first["credential"] != second["credential"]
    assert _read_signature(first["proof"]["sshsig"])["signature"] != (
        _read_signature(second["proof"]["sshsig"])["signature"]
    )
    return first, second


def _forged_signature(proof: dict) -> dict:
    """Preserve the signer/header and flip one real Ed25519 signature bit."""
    result = copy.deepcopy(proof)
    parsed = _read_signature(result["sshsig"])
    signature = parsed["signature"]
    changed = signature[:-1] + bytes([signature[-1] ^ 1])
    result["sshsig"] = _replace_bytes(
        result["sshsig"], parsed["signature_offset"], signature, changed
    )
    assert _read_signature(result["sshsig"])["public_key"] == parsed["public_key"]
    return result


def _spoof_embedded_signer(proof: dict, claimed_public_key_blob: bytes) -> dict:
    """Put a trusted signer's public key inside a different signer's SSHSIG.

    Both identities use the same valid SSH Ed25519 public-key encoding length.
    The outer envelope, message and foreign signature remain unchanged. This
    is a cryptographic signature invalid under the *claimed* public key, not
    a malformed-armor or unknown-identity rejection.
    """
    result = copy.deepcopy(proof)
    parsed = _read_signature(result["sshsig"])
    foreign_key, begin, _ = parsed["public_key"]
    result["sshsig"] = _replace_bytes(
        result["sshsig"], begin, foreign_key, claimed_public_key_blob
    )
    assert _read_signature(result["sshsig"])["signature"] == parsed["signature"]
    assert _read_signature(result["sshsig"])["public_key"][0] == claimed_public_key_blob
    return result


def test_synthetic_positive_proof_verifies_with_actual_openssh(statement, signatures, verifier):
    first, second = signatures
    assert original.verify(statement, first["proof"], first["credential"], verifier)
    assert original.verify(statement, second["proof"], second["credential"], verifier)


def test_same_signer_well_formed_signature_bitflip_fails_cryptographically(
    statement, signatures, verifier
):
    first, _ = signatures
    baseline = _read_signature(first["proof"]["sshsig"])
    forged = _forged_signature(first["proof"])
    altered = _read_signature(forged["sshsig"])
    assert altered["raw"][: baseline["signature_offset"]] == (
        baseline["raw"][: baseline["signature_offset"]]
    )
    assert altered["signature"] != baseline["signature"]
    assert len(altered["raw"]) == len(baseline["raw"])
    assert original.verify(statement, first["proof"], first["credential"], verifier)
    assert not original.verify(statement, forged, first["credential"], verifier)


def test_foreign_signature_with_spoofed_allowed_public_key_fails(
    statement, signatures, verifier
):
    first, other = signatures
    allowed = _read_signature(first["proof"]["sshsig"])
    foreign = _read_signature(other["proof"]["sshsig"])
    assert original.verify(statement, other["proof"], other["credential"], verifier)
    candidate = _spoof_embedded_signer(
        other["proof"], allowed["public_key"][0]
    )
    forged = _read_signature(candidate["sshsig"])
    assert forged["public_key"][0] == allowed["public_key"][0]
    assert forged["signature"] == foreign["signature"]
    assert original.verify(statement, first["proof"], first["credential"], verifier)
    assert not original.verify(statement, candidate, first["credential"], verifier)


def test_exact_signed_statement_change_fails_with_original_signature(
    statement, signatures, verifier
):
    first, _ = signatures
    changed = copy.deepcopy(statement)
    changed["decision"] = "AMEND" if statement["decision"] == "ACCEPT" else "ACCEPT"
    assert original.verify(statement, first["proof"], first["credential"], verifier)
    assert not original.verify(changed, first["proof"], first["credential"], verifier)


def test_real_semantic_base_input_dependency_and_unrelated_revision_metamorphism(fixture):
    """Exercise the actual derivation rather than unused unrelated metadata."""
    baseline = original.digest(original.semantic_base(fixture))
    unrelated = copy.deepcopy(fixture)
    unrelated["semantic_base"]["source_revision"] = (
        unrelated["semantic_base"]["source_revision"] + "-UNRELATED-NON-OWNER"
    )
    assert original.digest(original.semantic_base(unrelated)) == baseline

    governed = copy.deepcopy(fixture)
    governed["semantic_base"]["effects"][0]["lineage_head"] += "-ALTERED"
    assert original.digest(original.semantic_base(governed)) != baseline


def test_legacy_mutated_magic_is_not_an_adequate_crypto_negative(signatures):
    """Demonstrate why a syntactically malformed negative alone is weak."""
    first, _ = signatures
    previous = original.mutate_proof(first["proof"])
    with pytest.raises(ValueError, match="magic"):
        _read_signature(previous["sshsig"])
    assert _read_signature(_forged_signature(first["proof"])["sshsig"])


def _parse_ecdsa_der(raw: bytes) -> tuple[bytes, bytes]:
    """Validate canonical short-form ASN.1 DER ECDSA Signature {r,s}.

    P-256 values are small enough for DER's short-form sequence and INTEGER
    lengths (the maximum sequence payload is 70 bytes). Checking the INTEGER
    sign rule, no excess leading zero and exact sequence length ensures that
    mutating a signature value does not inadvertently make the DER parser
    reject the payload before cryptographic verification is reached.
    """
    if len(raw) < 8 or raw[0] != 0x30 or raw[1] != len(raw) - 2:
        raise ValueError("invalid ECDSA DER sequence")
    offset = 2
    integers = []
    for _ in range(2):
        if offset + 2 > len(raw) or raw[offset] != 0x02:
            raise ValueError("invalid ECDSA INTEGER tag")
        length = raw[offset + 1]
        start = offset + 2
        end = start + length
        if length == 0 or end > len(raw):
            raise ValueError("invalid ECDSA INTEGER length")
        field = raw[start:end]
        if field[0] >= 0x80 or (
            len(field) > 1 and field[0] == 0 and field[1] < 0x80
        ):
            raise ValueError("non-canonical ECDSA INTEGER encoding")
        integers.append(field)
        offset = end
    if offset != len(raw):
        raise ValueError("trailing ECDSA bytes")
    return integers[0], integers[1]


@pytest.fixture(scope="module")
def webauthn_signatures(statement, verifier):
    primary = verifier.call(
        "synthetic_webauthn",
        label="SYNTHETIC-NON-OWNER-P256-CRYPTO-SENSITIVITY-PRIMARY",
        statement=statement,
    )
    attacker = verifier.call(
        "synthetic_webauthn",
        label="SYNTHETIC-NON-OWNER-P256-CRYPTO-SENSITIVITY-ATTACKER",
        statement=statement,
    )
    assert primary["credential"] != attacker["credential"]
    return primary, attacker


def test_synthetic_webauthn_positive_and_well_formed_der_negative(
    statement, webauthn_signatures, verifier
):
    primary, _ = webauthn_signatures
    assert original.verify(statement, primary["proof"], primary["credential"], verifier)
    proof = copy.deepcopy(primary["proof"])
    field = proof["signature_der"]
    raw = bytearray(base64.urlsafe_b64decode(field + "=" * (-len(field) % 4)))
    original_r, original_s = _parse_ecdsa_der(raw)

    # Last signature byte is within the encoded scalar, not the DER tag,
    # sequence length, INTEGER header or positive sign byte.
    raw[-1] ^= 0x01
    changed_r, changed_s = _parse_ecdsa_der(raw)
    assert original_r == changed_r and original_s != changed_s
    proof["signature_der"] = base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")
    assert not original.verify(statement, proof, primary["credential"], verifier)


def test_synthetic_webauthn_nonowner_signature_with_allowed_id_is_rejected(
    statement, webauthn_signatures, verifier
):
    primary, attacker = webauthn_signatures
    assert original.verify(statement, attacker["proof"], attacker["credential"], verifier)
    forged = copy.deepcopy(attacker["proof"])
    forged["credential_id"] = primary["credential"]["credential_id"]
    raw_sig = base64.urlsafe_b64decode(
        forged["signature_der"] + "=" * (-len(forged["signature_der"]) % 4)
    )
    _parse_ecdsa_der(raw_sig)
    # The challenge, rpIdHash, UV flags and assertion bytes are unchanged:
    # only the claimed transport credential ID is now the allowed owner's ID.
    # A signature made by the attacker's P-256 key must not verify against
    # the allowed public SPKI, even when the metadata identity appears valid.
    assert not original.verify(statement, forged, primary["credential"], verifier)
