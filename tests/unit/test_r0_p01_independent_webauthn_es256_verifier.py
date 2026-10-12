"""Independent non-owner WebAuthn ES256 assertion verification boundary tests.

All proofs are synthetic P-256 signatures from an ephemeral signer worker.
These tests never use a hardware authenticator or real Windows Hello.
The tested verification-only component imports no owner RP and does not
derive its decisions from caller-provided verification labels.
"""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as historical
from experiments.r0_p01_successor_synthetic import run_bound_acceptance as rb

VERIFIER = (
    Path(__file__).parents[2]
    / "experiments/r0_p01_successor_synthetic/independent_webauthn_es256_verify.mjs"
)
TEMPLATE=json.loads(
    (Path(historical.HERE)/"clarification_vectors_v02.json").read_text(encoding="utf-8")
)["statement"]


def invoke(payload):
    return invoke_raw(json.dumps(payload,ensure_ascii=False))


def invoke_raw(raw):
    result=subprocess.run(
        ["node",str(VERIFIER),"--verify-only"],
        input=raw,capture_output=True,text=True,
        encoding="utf-8",timeout=10,
    )
    assert result.returncode==0,result.stderr
    response=json.loads(result.stdout)
    assert response["verdict"] in ("VALID","INVALID","ERROR")
    return response


def b64url(data: bytes)->str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def decode(text: str)->bytes:
    return base64.urlsafe_b64decode(text+"="*(-len(text)%4))


@pytest.fixture(scope="module")
def sample():
    if not shutil.which("node"):
        pytest.skip("Node built-in crypto is required")
    statement=rb.new_run_statement(TEMPLATE,claim_nonce="3"*64)
    with rb.SyntheticRunCrypto() as node:
        signer=node.call(
            "sign_es256",label="SYNTHETIC-NON-OWNER-INDEPENDENT-ES256-PRIMARY-001",
            statement=statement,
        )
        foreign=node.call(
            "sign_es256",label="SYNTHETIC-NON-OWNER-INDEPENDENT-ES256-FOREIGN-001",
            statement=statement,
        )
        assert signer["credential"]!=foreign["credential"]
        assert node.call(
            "verify_es256",statement=statement,
            credential=signer["credential"],proof=signer["proof"],
        )["valid"] is True
        yield statement,signer,foreign,node


def request(sample):
    message,signer,_,_=sample
    return {
        "statement":copy.deepcopy(message),
        "enrolled_credential":copy.deepcopy(signer["credential"]),
        "proof":copy.deepcopy(signer["proof"]),
    }


def edit_client(req,transform):
    original=decode(req["proof"]["client_data_json"])
    req["proof"]["client_data_json"]=b64url(transform(original))


def edit_auth(req,transform):
    req["proof"]["authenticator_data"]=b64url(
        transform(decode(req["proof"]["authenticator_data"]))
    )


def test_real_synthetic_es256_signature_verifies_and_binds_exact_statement(sample):
    req=request(sample)
    result=invoke(req)
    assert result["verdict"]=="VALID"
    assert result["reason"]=="VERIFIED"
    assert result["trusted_public_id"]==req["enrolled_credential"]["public_id"]
    assert result["sign_count"]==0
    assert result["synthetic_non_owner"] is True
    assert result["expected_statement_sha256"]==hashlib.sha256(
        historical.canonical(req["statement"])
    ).hexdigest()


def test_independent_foreign_public_signer_verifies_only_as_itself(sample):
    statement,_,foreign,node=sample
    req={
        "statement":copy.deepcopy(statement),
        "enrolled_credential":copy.deepcopy(foreign["credential"]),
        "proof":copy.deepcopy(foreign["proof"]),
    }
    assert invoke(req)["verdict"]=="VALID"
    assert node.call(
        "verify_es256",statement=statement,
        proof=foreign["proof"],credential=foreign["credential"],
    )["valid"] is True


@pytest.mark.parametrize("field,value",[
    ("claim_nonce","f"*64),
    ("decision","REJECT"),
    ("shown_digest","a"*64),
    ("semantic_base_digest","b"*64),
    ("envelope_digest","c"*64),
    ("issued_at","2099-01-01T00:00:00Z"),
    ("acceptance_id","R0-P01-B-S02"),
    ("project_id","ANOTHER-PROJECT"),
])
def test_syntactically_valid_change_in_signed_statement_invalidates_signature(
    sample,field,value,
):
    req=request(sample)
    req["statement"][field]=value
    assert rb.valid_shape(req["statement"])
    result=invoke(req)
    assert result["verdict"]=="INVALID"
    assert result["reason"]=="CLIENT_CHALLENGE"


def test_foreign_valid_signature_cannot_impersonate_enrolled_public_key(sample):
    _,_,foreign,_=sample
    req=request(sample)
    req["proof"]["signature_der"]=foreign["proof"]["signature_der"]
    assert invoke(req)["reason"]=="SIGNATURE_REJECTED"


def test_foreign_credential_id_cannot_select_a_different_enrolled_credential(sample):
    _,_,foreign,_=sample
    req=request(sample)
    req["proof"]["credential_id"]=foreign["credential"]["credential_id"]
    assert invoke(req)["reason"]=="CREDENTIAL_ID"


def test_spki_replacement_with_unchanged_trust_id_is_rejected(sample):
    _,_,foreign,_=sample
    req=request(sample)
    req["enrolled_credential"]["spki_der"]=foreign["credential"]["spki_der"]
    assert invoke(req)["reason"]=="TRUSTED_PUBLIC_ID"


def test_forged_public_id_with_valid_der_is_rejected(sample):
    req=request(sample)
    req["enrolled_credential"]["public_id"]="WEBAUTHN-ES256-SPKI-SHA256-HEX:"+"f"*64
    assert invoke(req)["reason"]=="TRUSTED_PUBLIC_ID"


@pytest.mark.parametrize("replacement,reason",[
    ("http://127.0.0.1:8765","CLIENT_ORIGIN"),
    ("https://localhost:8765","CLIENT_ORIGIN"),
    ("https://evil.invalid","CLIENT_ORIGIN"),
])
def test_wrong_client_origin_is_rejected_before_cryptographic_verification(
    sample,replacement,reason,
):
    req=request(sample)
    def convert(raw):
        document=json.loads(raw)
        document["origin"]=replacement
        return json.dumps(document,separators=(",",":")).encode()
    edit_client(req,convert)
    assert invoke(req)["reason"]==reason


def test_wrong_type_is_not_webauthn_assertion(sample):
    req=request(sample)
    def convert(raw):
        document=json.loads(raw)
        document["type"]="webauthn.create"
        return json.dumps(document,separators=(",",":")).encode()
    edit_client(req,convert)
    assert invoke(req)["reason"]=="CLIENT_TYPE"


def test_explicit_cross_origin_true_rejected(sample):
    req=request(sample)
    def convert(raw):
        document=json.loads(raw)
        document["crossOrigin"]=True
        return json.dumps(document,separators=(",",":")).encode()
    edit_client(req,convert)
    assert invoke(req)["reason"]=="CLIENT_SHAPE"


@pytest.mark.parametrize("field",["challenge","origin","type"])
def test_duplicate_client_json_key_is_rejected_before_json_parse_collapse(
    sample,field,
):
    req=request(sample)
    def convert(raw):
        data=json.loads(raw)
        duplicate=json.dumps(field)+":"+json.dumps(data[field])
        return raw[:-1]+b","+duplicate.encode()+b"}"
    edit_client(req,convert)
    assert invoke(req)["reason"]=="CLIENT_DUPLICATE_KEY"


def test_utf8_corrupt_client_json_is_rejected(sample):
    req=request(sample)
    req["proof"]["client_data_json"]=b64url(b'{"type":"webauthn.get","origin":"\xff"}')
    assert invoke(req)["reason"]=="CLIENT_UTF8"


def test_duplicate_nested_json_key_also_fails_closed(sample):
    req=request(sample)
    edit_client(req,lambda raw:raw[:-1]+b',"extra":{"x":1,"x":2}}')
    assert invoke(req)["reason"]=="CLIENT_DUPLICATE_KEY"


@pytest.mark.parametrize("flags",[
    0x00,0x01,0x04,0x40,0x85,
])
def test_authenticator_presence_uv_or_extension_flags_rejected(sample,flags):
    req=request(sample)
    def update(auth):
        altered=bytearray(auth);altered[32]=flags;return bytes(altered)
    edit_auth(req,update)
    assert invoke(req)["reason"]=="PRESENCE_AND_VERIFICATION_FLAGS"


def test_wrong_rp_id_hash_rejected(sample):
    req=request(sample)
    def update(auth):
        data=bytearray(auth)
        data[:32]=hashlib.sha256(b"another.invalid").digest()
        return bytes(data)
    edit_auth(req,update)
    assert invoke(req)["reason"]=="RP_ID_HASH"


@pytest.mark.parametrize("change",["length","signature_bit","malformed_der","scalar_zero"])
def test_bad_signature_der_or_cryptographic_signature_fails(sample,change):
    req=request(sample)
    signature=bytearray(decode(req["proof"]["signature_der"]))
    if change=="length":
        signature[1]^=1
    elif change=="signature_bit":
        signature[-1]^=1
    elif change=="malformed_der":
        signature[0]=0x31
    else:
        # Replacing the second positive DER scalar with zero keeps the shape
        # but is prohibited by the strict scalar domain check.
        signature[-1]=0
        if signature[-2]==0: signature[-2]=0
        # A deliberate all-zero scalar retaining DER length.
        offset=2
        first_len=signature[3]
        second_offset=4+first_len
        second_len=signature[second_offset+1]
        for i in range(second_offset+2,second_offset+2+second_len):
            signature[i]=0
    req["proof"]["signature_der"]=b64url(signature)
    result=invoke(req)
    assert result["verdict"]=="INVALID"
    if change=="signature_bit":
        assert result["reason"] in ("SIGNATURE_REJECTED","SIGNATURE_SCALAR")
    else:
        assert result["reason"] in ("SIGNATURE_DER","SIGNATURE_SCALAR")


@pytest.mark.parametrize("corruption",[
    "extra_statement","missing_statement","wrong_domain","nonce_shape",
    "bad_spki","bad_base64","missing_proof","untrusted_marker",
])
def test_proof_and_trust_input_shapes_fail_closed(sample,corruption):
    req=request(sample)
    if corruption=="extra_statement":
        req["statement"]["extra"]="untrusted"
    elif corruption=="missing_statement":
        del req["statement"]["claim_nonce"]
    elif corruption=="wrong_domain":
        req["statement"]["protocol"]="HISTORICAL-V02"
    elif corruption=="nonce_shape":
        req["statement"]["claim_nonce"]="z"*64
    elif corruption=="bad_spki":
        req["enrolled_credential"]["spki_der"]=b64url(b"not-a-spki")
        req["enrolled_credential"]["public_id"]="WEBAUTHN-ES256-SPKI-SHA256-HEX:"+hashlib.sha256(b"not-a-spki").hexdigest()
    elif corruption=="bad_base64":
        req["proof"]["client_data_json"]="x="
    elif corruption=="missing_proof":
        del req["proof"]["signature_der"]
    else:
        req["proof"]["synthetic_non_owner"]=False
    assert invoke(req)["verdict"]=="INVALID"


def test_wrong_verifier_cli_mode_is_refused_without_key_creation():
    process=subprocess.run(
        ["node",str(VERIFIER),"--sign"],
        capture_output=True,text=True,timeout=10,
    )
    assert process.returncode!=0
    assert "verification-only" in process.stderr


def test_no_import_of_harness_rp_synthetic_signer_or_private_key_functions():
    text=VERIFIER.read_text(encoding="utf-8")
    for forbidden in (
        "webauthn_server.mjs", "run_bound_crypto.mjs", "ssh-keygen",
        "generateKeyPairSync", "createPrivateKey", "crypto.sign(", "sign as ",
        "readFileSync", "writeFileSync", "http.createServer",
    ):
        assert forbidden not in text

@pytest.mark.parametrize("location",["request","statement","credential"])
def test_duplicate_trust_or_proof_keys_in_outer_request_fail_before_parse(
    sample,location,
):
    req=request(sample)
    text=json.dumps(req,separators=(",",":"),ensure_ascii=False)
    if location=="request":
        duplicate='"proof":'+json.dumps(req["proof"],separators=(",",":"))
        text=text[:-1]+","+duplicate+"}"
    elif location=="statement":
        value=req["statement"]["claim_nonce"]
        pair='"claim_nonce":"'+value+'"'
        assert text.count(pair)==1
        text=text.replace(pair,pair+","+pair,1)
    else:
        value=req["enrolled_credential"]["public_id"]
        pair='"public_id":"'+value+'"'
        assert text.count(pair)==1
        text=text.replace(pair,pair+","+pair,1)
    result=invoke_raw(text)
    assert (result["verdict"],result["reason"])==(
        "INVALID","CLIENT_DUPLICATE_KEY"
    )
