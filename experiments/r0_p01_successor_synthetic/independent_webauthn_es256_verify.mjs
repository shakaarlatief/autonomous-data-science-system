/**
 * Verification-only WebAuthn ES256 assertion candidate for R0-P01.
 *
 * Trust inputs are supplied separately by the scorer. This module does not
 * import the owner harness, historical RP implementation, synthetic worker,
 * browser APIs, or key-generation/signing routines. It verifies public
 * evidence only. It does not attest a credential ceremony, owner presence,
 * origin of a recorded receipt, or any terminal event lifecycle.
 */
import {createHash, createPublicKey, verify as verifySignature} from 'node:crypto';

const EXPECTED_PROTOCOL = 'ADS-R0-P01-RUN-BOUND-STATEMENT-V01';
const EXPECTED_ORIGIN = 'http://localhost:8765';
const EXPECTED_RPID = 'localhost';
const EXPECTED_FIELDS = Object.freeze([
  'acceptance_id', 'claim_nonce', 'context', 'decision', 'envelope_digest',
  'issued_at', 'project_id', 'protocol', 'semantic_base_digest',
  'shown_digest', 'signer_set_version',
].sort());
const B64URL = /^[A-Za-z0-9_-]+$/;
const P256_ORDER = BigInt('0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551');
const sha256 = x => createHash('sha256').update(x).digest();
const b64 = x => Buffer.from(x).toString('base64url');
class InvalidInput extends Error {
  constructor(code) { super(code); this.code = code; }
}
function assertValid(test, code) {
  if (!test) throw new InvalidInput(code);
}
function decodeUrl(text, code, maxBytes = 10240) {
  assertValid(typeof text === 'string' && text.length > 0 &&
    text.length <= maxBytes * 2 && B64URL.test(text), code);
  const bytes = Buffer.from(text, 'base64url');
  assertValid(bytes.length <= maxBytes && b64(bytes) === text, code);
  return bytes;
}
function canonical(value) {
  if (value === null || typeof value === 'boolean') return JSON.stringify(value);
  if (typeof value === 'string') {
    // Canonical JSON must never silently replace an unpaired UTF-16 surrogate.
    for (let index = 0; index < value.length; index++) {
      const code = value.charCodeAt(index);
      if (code >= 0xd800 && code <= 0xdbff) {
        assertValid(index + 1 < value.length, 'INVALID_UNICODE');
        const next = value.charCodeAt(++index);
        assertValid(next >= 0xdc00 && next <= 0xdfff, 'INVALID_UNICODE');
      } else assertValid(!(code >= 0xdc00 && code <= 0xdfff), 'INVALID_UNICODE');
    }
    return JSON.stringify(value);
  }
  if (typeof value === 'number') {
    assertValid(Number.isFinite(value), 'INVALID_NUMBER');
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) return '[' + value.map(canonical).join(',') + ']';
  assertValid(value && typeof value === 'object' &&
    Object.getPrototypeOf(value) === Object.prototype, 'INVALID_JSON_TYPE');
  return '{' + Object.keys(value).sort().map(
    k => canonical(k) + ':' + canonical(value[k])
  ).join(',') + '}';
}
function statementBytes(value) {
  assertValid(value && typeof value === 'object' && !Array.isArray(value),
    'INVALID_STATEMENT');
  const actual = Object.keys(value).sort();
  assertValid(actual.length === EXPECTED_FIELDS.length &&
    actual.every((key, index) => key === EXPECTED_FIELDS[index]),
    'STATEMENT_FIELDS');
  assertValid(EXPECTED_FIELDS.every(k => typeof value[k] === 'string'),
    'STATEMENT_TYPE');
  assertValid(value.protocol === EXPECTED_PROTOCOL, 'PROTOCOL_DOMAIN');
  assertValid(/^[0-9a-f]{64}$/.test(value.claim_nonce), 'CLAIM_NONCE');
  assertValid(['ACCEPT', 'AMEND', 'REJECT'].includes(value.decision), 'DECISION');
  for (const name of ['envelope_digest', 'shown_digest', 'semantic_base_digest']) {
    assertValid(/^[0-9a-f]{64}$/.test(value[name]), 'STATEMENT_DIGEST');
  }
  return Buffer.from(canonical(value), 'utf8');
}

/**
 * A small JSON scanner validates string escapes, complete grammar, and
 * duplicate keys in every object BEFORE JSON.parse handles the values.
 * A browser clientDataJSON need not use sorted property order or whitespace.
 */
function rejectDuplicateKeys(text) {
  let p = 0;
  const ws = () => { while (p < text.length && /[\x20\t\r\n]/.test(text[p])) p++; };
  function readString() {
    assertValid(text[p] === '"', 'CLIENT_JSON_GRAMMAR');
    const first = p++;
    while (p < text.length) {
      const ch = text[p++];
      if (ch === '"') {
        const raw = text.slice(first, p);
        try { return JSON.parse(raw); } catch { throw new InvalidInput('CLIENT_JSON_GRAMMAR'); }
      }
      if (ch === '\\') {
        assertValid(p < text.length, 'CLIENT_JSON_GRAMMAR');
        const escaped = text[p++];
        if (escaped === 'u') {
          assertValid(/^[0-9a-fA-F]{4}$/.test(text.slice(p, p + 4)),
            'CLIENT_JSON_GRAMMAR');
          p += 4;
        } else assertValid('"\\/bfnrt'.includes(escaped), 'CLIENT_JSON_GRAMMAR');
      } else assertValid(ch.charCodeAt(0) >= 32, 'CLIENT_JSON_GRAMMAR');
    }
    throw new InvalidInput('CLIENT_JSON_GRAMMAR');
  }
  function value(depth) {
    assertValid(depth < 32, 'CLIENT_JSON_DEPTH');
    ws();
    if (text[p] === '{') {
      p++; ws(); const keys = new Set();
      if (text[p] === '}') { p++; return; }
      while (true) {
        const key = readString();
        assertValid(!keys.has(key), 'CLIENT_DUPLICATE_KEY');
        keys.add(key);
        ws(); assertValid(text[p++] === ':', 'CLIENT_JSON_GRAMMAR');
        value(depth + 1); ws();
        if (text[p] === '}') { p++; break; }
        assertValid(text[p++] === ',', 'CLIENT_JSON_GRAMMAR'); ws();
      }
    } else if (text[p] === '[') {
      p++; ws();
      if (text[p] === ']') { p++; return; }
      while (true) {
        value(depth + 1); ws();
        if (text[p] === ']') { p++; break; }
        assertValid(text[p++] === ',', 'CLIENT_JSON_GRAMMAR');
      }
    } else if (text[p] === '"') readString();
    else {
      const match = /^(?:true|false|null|-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)/.exec(text.slice(p));
      assertValid(match !== null, 'CLIENT_JSON_GRAMMAR');
      p += match[0].length;
    }
  }
  value(0); ws();
  assertValid(p === text.length, 'CLIENT_JSON_GRAMMAR');
}
function clientData(bytes, expectedChallenge) {
  let text;
  try { text = new TextDecoder('utf-8', {fatal: true}).decode(bytes); }
  catch { throw new InvalidInput('CLIENT_UTF8'); }
  rejectDuplicateKeys(text);
  let data;
  try { data = JSON.parse(text); }
  catch { throw new InvalidInput('CLIENT_JSON_GRAMMAR'); }
  assertValid(data && typeof data === 'object' && !Array.isArray(data),
    'CLIENT_SHAPE');
  const keys = Object.keys(data).sort();
  assertValid(
    (keys.join(',') === 'challenge,crossOrigin,origin,type' &&
      data.crossOrigin === false) ||
    keys.join(',') === 'challenge,origin,type',
    'CLIENT_SHAPE'
  );
  assertValid(data.type === 'webauthn.get', 'CLIENT_TYPE');
  assertValid(data.origin === EXPECTED_ORIGIN, 'CLIENT_ORIGIN');
  assertValid(data.challenge === expectedChallenge, 'CLIENT_CHALLENGE');
}
function checkDer(signature) {
  assertValid(signature.length >= 8 && signature.length <= 72 &&
    signature[0] === 0x30 && signature[1] === signature.length - 2,
    'SIGNATURE_DER');
  let pos = 2;
  for (let index = 0; index < 2; index++) {
    assertValid(pos + 2 <= signature.length && signature[pos++] === 2,
      'SIGNATURE_DER');
    const len = signature[pos++];
    assertValid(len >= 1 && len <= 33 && pos + len <= signature.length,
      'SIGNATURE_DER');
    const bytes = signature.subarray(pos, pos + len);
    pos += len;
    assertValid((bytes[0] & 0x80) === 0 &&
      (len === 1 || bytes[0] !== 0 || (bytes[1] & 0x80) !== 0),
      'SIGNATURE_DER');
    const number = BigInt('0x' + bytes.toString('hex'));
    assertValid(number > 0n && number < P256_ORDER, 'SIGNATURE_SCALAR');
  }
  assertValid(pos === signature.length, 'SIGNATURE_DER');
}
function verifyPublic(request) {
  assertValid(request && typeof request === 'object' &&
    !Array.isArray(request), 'REQUEST_SHAPE');
  assertValid(Object.keys(request).sort().join(',') ===
    'enrolled_credential,proof,statement','REQUEST_FIELDS');
  const statement = statementBytes(request.statement);
  const cred = request.enrolled_credential;
  const proof = request.proof;
  assertValid(cred && typeof cred === 'object' &&
    Object.keys(cred).sort().join(',') === 'credential_id,kind,public_id,spki_der' &&
    cred.kind === 'WEBAUTHN_ES256', 'TRUSTED_CREDENTIAL');
  const id = decodeUrl(cred.credential_id, 'TRUSTED_CREDENTIAL_ID', 1024);
  const der = decodeUrl(cred.spki_der, 'TRUSTED_PUBLIC_KEY', 1024);
  assertValid(id.length >= 1 && der.length > 0, 'TRUSTED_CREDENTIAL');
  assertValid(cred.public_id ===
    'WEBAUTHN-ES256-SPKI-SHA256-HEX:' + sha256(der).toString('hex'),
    'TRUSTED_PUBLIC_ID');
  let key;
  try {
    key = createPublicKey({key: der, format:'der', type:'spki'});
    assertValid(key.asymmetricKeyType === 'ec' &&
      key.asymmetricKeyDetails?.namedCurve === 'prime256v1' &&
      key.export({format:'der', type:'spki'}).equals(der), 'TRUSTED_PUBLIC_KEY');
  } catch (e) {
    if (e instanceof InvalidInput) throw e;
    throw new InvalidInput('TRUSTED_PUBLIC_KEY');
  }
  assertValid(proof && typeof proof === 'object' &&
    Object.keys(proof).sort().join(',') ===
    'authenticator_data,client_data_json,credential_id,kind,signature_der,synthetic_non_owner' &&
    proof.kind === 'WEBAUTHN_ES256' &&
    proof.synthetic_non_owner === true, 'PROOF_SHAPE');
  // This is a synthetic-only component profile. The final browser scorer
  // must adopt its own evidence schema before F2 and cannot inherit this
  // synthetic marker as a real-credential requirement.
  assertValid(proof.credential_id === cred.credential_id, 'CREDENTIAL_ID');
  const auth = decodeUrl(proof.authenticator_data, 'AUTHENTICATOR_DATA', 1024);
  assertValid(auth.length === 37, 'AUTHENTICATOR_DATA');
  assertValid(auth.subarray(0, 32).equals(sha256(Buffer.from(EXPECTED_RPID))),
    'RP_ID_HASH');
  const flags = auth[32];
  assertValid((flags & 0x05) === 0x05 && (flags & 0xc0) === 0,
    'PRESENCE_AND_VERIFICATION_FLAGS');
  const signCount = auth.readUInt32BE(33);
  const client = decodeUrl(proof.client_data_json, 'CLIENT_DATA', 2048);
  const expectedChallenge = b64(sha256(statement));
  clientData(client, expectedChallenge);
  const signature = decodeUrl(proof.signature_der, 'SIGNATURE_DER', 128);
  checkDer(signature);
  let valid;
  try {
    valid = verifySignature('sha256',
      Buffer.concat([auth, sha256(client)]), key, signature);
  } catch { throw new InvalidInput('SIGNATURE_DER'); }
  return {
    verdict: valid ? 'VALID' : 'INVALID',
    reason: valid ? 'VERIFIED' : 'SIGNATURE_REJECTED',
    expected_statement_sha256: sha256(statement).toString('hex'),
    trusted_public_id: cred.public_id,
    sign_count: signCount,
    synthetic_non_owner: true,
  };
}

if (process.argv.length !== 3 || process.argv[2] !== '--verify-only')
  throw new Error('verification-only synthetic WebAuthn public JSON CLI required');
try {
  const chunks = []; let length = 0;
  for await (const chunk of process.stdin) {
    length += chunk.length;
    assertValid(length <= 30000, 'REQUEST_TOO_LARGE');
    chunks.push(chunk);
  }
  const text = new TextDecoder('utf-8', {fatal: true})
    .decode(Buffer.concat(chunks));
  // The trusted statement/credential and submitted proof must have an
  // unambiguous wire interpretation, not just unambiguous clientDataJSON.
  rejectDuplicateKeys(text);
  process.stdout.write(JSON.stringify(verifyPublic(JSON.parse(text))) + '\n');
} catch (error) {
  if (error instanceof InvalidInput)
    process.stdout.write(JSON.stringify({verdict:'INVALID',reason:error.code}) + '\n');
  else process.stdout.write(JSON.stringify({verdict:'ERROR',reason:'VERIFIER_EXCEPTION'}) + '\n');
}
