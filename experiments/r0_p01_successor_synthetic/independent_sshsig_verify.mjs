/**
 * Independent SSHSIG Ed25519 verification candidate for R0-P01 F1.
 *
 * This executable has one operation: public-key verification. It cannot sign,
 * create keys, issue claims, alter an experiment, or invoke the owner harness.
 * No dependency on Python's canonicalizer, the OpenSSH verifier, or the
 * synthetic Node signing worker. All expected statement and trust-anchor
 * inputs must be supplied by a separately trusted scorer/controller.
 *
 * The SSHSIG framing and signed-message reconstruction follow OpenSSH
 * PROTOCOL.sshsig with strict, bounded, exact-field validation. Only the
 * specified Ed25519, sha512, namespace and empty-reserved profile is accepted.
 * This does not establish issuer authenticity, platform owner presence, or
 * durable receipt provenance. Node crypto is an independent verification
 * implementation from the owner harness's OpenSSH command, although both
 * use standard Ed25519 mathematics.
 */
import crypto from 'node:crypto';

const DOMAIN='ADS-R0-P01-RUN-BOUND-STATEMENT-V01';
const NAMESPACE='ads-r0-p01-claimed-run-v1';
const FIELDS=[
  'acceptance_id','claim_nonce','context','decision','envelope_digest',
  'issued_at','project_id','protocol','semantic_base_digest',
  'shown_digest','signer_set_version',
].sort();
const LIMIT=20000;
const ENVELOPE='-----BEGIN SSH SIGNATURE-----';
const END='-----END SSH SIGNATURE-----';
const encoder=x=>Buffer.from(x,'utf8');

function requireIt(condition, cause) {
  if (!condition) throw new Invalid(cause);
}
class Invalid extends Error {
  constructor(cause){super(cause);this.cause=cause;}
}
const sha=(alg,data)=>crypto.createHash(alg).update(data).digest();
const sshString=x=>{
  const bytes=Buffer.from(x);
  const length=Buffer.alloc(4);
  length.writeUInt32BE(bytes.length);
  return Buffer.concat([length,bytes]);
};

function encodeJsonString(value) {
  for(let i=0;i<value.length;i++){
    const c=value.charCodeAt(i);
    if(c>=0xd800&&c<=0xdbff) {
      requireIt(i+1<value.length,'INVALID_UNICODE');
      const d=value.charCodeAt(++i);
      requireIt(d>=0xdc00&&d<=0xdfff,'INVALID_UNICODE');
    } else {
      requireIt(!(c>=0xdc00&&c<=0xdfff),'INVALID_UNICODE');
    }
  }
  return JSON.stringify(value);
}

function canonical(value){
  if(typeof value==='string')return encodeJsonString(value);
  if(value===null||typeof value==='boolean')return JSON.stringify(value);
  if(typeof value==='number'){
    requireIt(Number.isFinite(value),'INVALID_NUMBER');
    return JSON.stringify(value);
  }
  if(Array.isArray(value))return '['+value.map(canonical).join(',')+']';
  requireIt(value&&typeof value==='object'&&
    Object.getPrototypeOf(value)===Object.prototype,'INVALID_CANONICAL_VALUE');
  return '{'+Object.keys(value).sort().map(k=>
    encodeJsonString(k)+':'+canonical(value[k])).join(',')+'}';
}

function statementBytes(value) {
  requireIt(value&&typeof value==='object'&&!Array.isArray(value),
    'INVALID_STATEMENT');
  const actual=Object.keys(value).sort();
  requireIt(actual.length===FIELDS.length&&
    actual.every((k,i)=>k===FIELDS[i]),'STATEMENT_FIELDS');
  for(const k of FIELDS)requireIt(typeof value[k]==='string','STATEMENT_TYPE');
  requireIt(value.protocol===DOMAIN,'PROTOCOL_DOMAIN');
  requireIt(/^[0-9a-f]{64}$/.test(value.claim_nonce),'CLAIM_NONCE');
  requireIt(['ACCEPT','AMEND','REJECT'].includes(value.decision),'DECISION');
  for(const field of ['envelope_digest','shown_digest','semantic_base_digest'])
    requireIt(/^[0-9a-f]{64}$/.test(value[field]),'SIGNED_DIGEST');
  return encoder(canonical(value));
}

function readString(bytes, cursor) {
  requireIt(cursor.index<=bytes.length-4,'TRUNCATED_SSH_STRING');
  const length=bytes.readUInt32BE(cursor.index);
  cursor.index+=4;
  requireIt(length<=bytes.length-cursor.index,'TRUNCATED_SSH_STRING');
  const value=bytes.subarray(cursor.index,cursor.index+length);
  cursor.index+=length;
  return value;
}
function exactEnd(bytes,cursor){
  requireIt(cursor.index===bytes.length,'TRAILING_SSH_BYTES');
}
function decodeArmor(text) {
  requireIt(typeof text==='string'&&text.length<=LIMIT,'INVALID_ARMOR');
  const normalized=text.replace(/\r\n/g,'\n').trimEnd();
  const lines=normalized.split('\n');
  requireIt(lines.length>=3&&lines[0]===ENVELOPE&&
    lines[lines.length-1]===END,'INVALID_ARMOR');
  const bodyLines=lines.slice(1,-1);
  requireIt(bodyLines.every(x=>x.length>0&&x.length<=80&&
    /^[A-Za-z0-9+/=]+$/.test(x)),'INVALID_ARMOR');
  const encoded=bodyLines.join('');
  requireIt(encoded.length>0&&encoded.length%4===0,'INVALID_BASE64');
  const bytes=Buffer.from(encoded,'base64');
  requireIt(bytes.toString('base64')===encoded,'NONCANONICAL_BASE64');
  return bytes;
}
function enrolledKey(publicKey, identity) {
  requireIt(typeof publicKey==='string'&&publicKey.length<500,'TRUSTED_KEY');
  const parts=publicKey.split(' ');
  requireIt(parts.length===2&&parts[0]==='ssh-ed25519','TRUSTED_KEY');
  const encoded=parts[1];
  requireIt(encoded.length%4===0&&/^[A-Za-z0-9+/]+={0,2}$/.test(encoded),
    'TRUSTED_KEY');
  const pk=Buffer.from(encoded,'base64');
  requireIt(pk.toString('base64')===encoded,'TRUSTED_KEY');
  const cursor={index:0};
  requireIt(readString(pk,cursor).equals(encoder('ssh-ed25519')),'TRUSTED_KEY');
  const raw=readString(pk,cursor);
  requireIt(raw.length===32,'TRUSTED_KEY');
  exactEnd(pk,cursor);
  requireIt(typeof identity==='string'&&identity===
    'SSH-ED25519-SHA256-HEX:'+sha('sha256',pk).toString('hex'),
    'TRUSTED_PUBLIC_ID');
  return {pk,raw};
}

function verify(request) {
  requireIt(request&&typeof request==='object'&&!Array.isArray(request),
    'INVALID_REQUEST');
  const keys=Object.keys(request).sort();
  requireIt(keys.join(',')===
    'enrolled_public_id,enrolled_public_key,proof,statement',
    'REQUEST_FIELDS');
  const message=statementBytes(request.statement);
  const trusted=enrolledKey(
    request.enrolled_public_key,request.enrolled_public_id
  );
  requireIt(request.proof&&typeof request.proof==='object'&&
    !Array.isArray(request.proof)&&request.proof.kind==='SSH_ED25519'&&
    typeof request.proof.sshsig==='string','PROOF_GRAMMAR');
  const packet=decodeArmor(request.proof.sshsig);
  requireIt(packet.length>=10&&packet.subarray(0,6).equals(encoder('SSHSIG')),
    'SSHSIG_MAGIC');
  requireIt(packet.readUInt32BE(6)===1,'SSHSIG_VERSION');
  const cursor={index:10};
  const embedded=readString(packet,cursor);
  const namespace=readString(packet,cursor);
  const reserved=readString(packet,cursor);
  const hashName=readString(packet,cursor);
  const signaturePacket=readString(packet,cursor);
  exactEnd(packet,cursor);
  requireIt(embedded.equals(trusted.pk),'EMBEDDED_SIGNER');
  requireIt(namespace.equals(encoder(NAMESPACE)),'WRONG_NAMESPACE');
  requireIt(reserved.length===0,'NONEMPTY_RESERVED');
  requireIt(hashName.equals(encoder('sha512')),'WRONG_HASH');
  const sigCursor={index:0};
  requireIt(readString(signaturePacket,sigCursor).equals(encoder('ssh-ed25519')),
    'WRONG_ALGORITHM');
  const signature=readString(signaturePacket,sigCursor);
  requireIt(signature.length===64,'SIGNATURE_LENGTH');
  exactEnd(signaturePacket,sigCursor);

  const signedPayload=Buffer.concat([
    encoder('SSHSIG'),
    sshString(namespace),
    sshString(reserved),
    sshString(hashName),
    sshString(sha('sha512',message)),
  ]);
  const spkiPrefix=Buffer.from('302a300506032b6570032100','hex');
  const publicKey=crypto.createPublicKey({
    key:Buffer.concat([spkiPrefix,trusted.raw]),format:'der',type:'spki'
  });
  const valid=crypto.verify(null,signedPayload,publicKey,signature);
  return {
    verdict:valid?'VALID':'INVALID',
    reason:valid?'VERIFIED':'SIGNATURE_REJECTED',
    expected_statement_sha256:sha('sha256',message).toString('hex'),
    trusted_public_id:request.enrolled_public_id,
  };
}

if(process.argv.length!==3||process.argv[2]!=='--verify-only')
  throw new Error('verification-only public JSON CLI required');
try{
  const chunks=[];
  let bytes=0;
  for await(const chunk of process.stdin){
    bytes+=chunk.length;
    requireIt(bytes<=30000,'REQUEST_TOO_LARGE');
    chunks.push(chunk);
  }
  const input=new TextDecoder('utf-8',{fatal:true})
    .decode(Buffer.concat(chunks));
  const result=verify(JSON.parse(input));
  process.stdout.write(JSON.stringify(result)+'\n');
}catch(error){
  if(error instanceof Invalid){
    process.stdout.write(JSON.stringify({
      verdict:'INVALID',reason:error.cause
    })+'\n');
  }else{
    // Avoid fabricating INVALID on operational failure.
    process.stdout.write(JSON.stringify({
      verdict:'ERROR',reason:'VERIFIER_EXCEPTION'
    })+'\n');
  }
}
