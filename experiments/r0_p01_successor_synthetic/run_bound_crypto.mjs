/**
 * Non-owner R0-P01 successor signed-claim cryptographic test worker.
 *
 * Built-in Node crypto only. Keys are ephemeral KeyObjects retained in this
 * process; no private material is written to disk or emitted on stdout.
 * No browser service, hardware authenticator, user key, owner claim, or
 * production acceptance can be started by this worker.
 *
 * This is a synthetic test protocol. ES256 uses WebAuthn-shaped assertion
 * data and a fixed localhost RP binding, not a Windows Hello ceremony.
 */
import * as crypto from 'node:crypto';
import readline from 'node:readline';

const PROTOCOL='ADS-R0-P01-RUN-BOUND-STATEMENT-V01';
const SSH_NAMESPACE='ads-r0-p01-claimed-run-v1';
const RP='localhost', ORIGIN='http://localhost:8765';
const FIELDS=[
  'protocol','claim_nonce','context','project_id','acceptance_id',
  'envelope_digest','shown_digest','decision','semantic_base_digest',
  'signer_set_version','issued_at',
].sort();
const hash=b=>crypto.createHash('sha256').update(b).digest();
const b64=b=>Buffer.from(b).toString('base64url');
const sshStr=x=>{const b=Buffer.from(x);const n=Buffer.alloc(4);n.writeUInt32BE(b.length);return Buffer.concat([n,b]);};
const keys=new Map();
function sortedCanonical(x) {
  if(x===null || typeof x==='boolean')return JSON.stringify(x);
  if(typeof x==='string') {
    for(let i=0;i<x.length;i++) {
      const c=x.charCodeAt(i);
      if(c>=0xd800&&c<=0xdbff) {const d=x.charCodeAt(++i);if(!(d>=0xdc00&&d<=0xdfff))throw Error('surrogate');}
      else if(c>=0xdc00&&c<=0xdfff)throw Error('surrogate');
    }
    return JSON.stringify(x);
  }
  if(typeof x==='number'){if(!Number.isFinite(x))throw Error('nonfinite');return JSON.stringify(x);}
  if(Array.isArray(x))return '['+x.map(sortedCanonical).join(',')+']';
  if(x && Object.getPrototypeOf(x)===Object.prototype)
    return '{'+Object.keys(x).sort((a,b)=>a<b?-1:a>b?1:0).map(k=>sortedCanonical(k)+':'+sortedCanonical(x[k])).join(',')+'}';
  throw Error('unsupported JSON');
}
function statementBytes(s) {
  if(!s||sortedCanonical(Object.keys(s).sort())!==sortedCanonical(FIELDS)||
     FIELDS.some(k=>typeof s[k]!=='string')||s.protocol!==PROTOCOL||
     !/^[0-9a-f]{64}$/.test(s.claim_nonce)||!['ACCEPT','AMEND','REJECT'].includes(s.decision))
    throw Error('invalid signed run-bound statement');
  for(const k of ['envelope_digest','shown_digest','semantic_base_digest'])
    if(!/^[0-9a-f]{64}$/.test(s[k]))throw Error('invalid signed digest');
  return Buffer.from(sortedCanonical(s),'utf8');
}
function requireLabel(label) {
  if(typeof label!=='string'||!/^SYNTHETIC-NON-OWNER-[A-Z0-9-]{8,120}$/.test(label))
    throw Error('non-owner test label required');
}
function publicES256(credential) {
  if(credential?.kind!=='WEBAUTHN_ES256'||typeof credential.spki_der!=='string')
    throw Error('not a public ES256 credential');
  const der=Buffer.from(credential.spki_der,'base64url');
  if(b64(der)!==credential.spki_der)throw Error('noncanonical SPKI encoding');
  const key=crypto.createPublicKey({key:der,type:'spki',format:'der'});
  if(key.asymmetricKeyType!=='ec'||key.asymmetricKeyDetails.namedCurve!=='prime256v1')throw Error('not P-256');
  if(credential.public_id!=='WEBAUTHN-ES256-SPKI-SHA256-HEX:'+hash(der).toString('hex'))throw Error('SPKI public ID');
  return key;
}
function signSSH(label,statement) {
  requireLabel(label);
  const signed=statementBytes(statement);
  const id='SSH:'+label;
  if(!keys.has(id))keys.set(id,crypto.generateKeyPairSync('ed25519'));
  const pair=keys.get(id);
  const raw=pair.publicKey.export({format:'der',type:'spki'}).subarray(-32);
  const pk=Buffer.concat([sshStr('ssh-ed25519'),sshStr(raw)]);
  const digest=crypto.createHash('sha512').update(signed).digest();
  const msg=Buffer.concat([Buffer.from('SSHSIG'),sshStr(SSH_NAMESPACE),sshStr(''),sshStr('sha512'),sshStr(digest)]);
  const sig=Buffer.concat([sshStr('ssh-ed25519'),sshStr(crypto.sign(null,msg,pair.privateKey))]);
  const version=Buffer.alloc(4);version.writeUInt32BE(1);
  const packet=Buffer.concat([Buffer.from('SSHSIG'),version,sshStr(pk),sshStr(SSH_NAMESPACE),sshStr(''),sshStr('sha512'),sshStr(sig)]);
  const encoded=packet.toString('base64');
  const armor='-----BEGIN SSH SIGNATURE-----\n'+(encoded.match(/.{1,70}/g)||[]).join('\n')+'\n-----END SSH SIGNATURE-----\n';
  return {credential:{kind:'SSH_ED25519',public_key:'ssh-ed25519 '+pk.toString('base64'),public_id:'SSH-ED25519-SHA256-HEX:'+hash(pk).toString('hex')},
          proof:{kind:'SSH_ED25519',sshsig:armor,synthetic_non_owner:true},synthetic_non_owner:true};
}
function signES256(label,statement) {
  requireLabel(label);
  const bytes=statementBytes(statement);
  const id='ES256:'+label;
  if(!keys.has(id))keys.set(id,crypto.generateKeyPairSync('ec',{namedCurve:'prime256v1'}));
  const pair=keys.get(id),der=pair.publicKey.export({format:'der',type:'spki'});
  const credential={kind:'WEBAUTHN_ES256',credential_id:b64(Buffer.from(label)),spki_der:b64(der),public_id:'WEBAUTHN-ES256-SPKI-SHA256-HEX:'+hash(der).toString('hex')};
  const authenticator=Buffer.alloc(37);
  hash(Buffer.from(RP)).copy(authenticator);
  authenticator[32]=0x05; // synthetic UP and UV; NOT real authenticator evidence
  const client=Buffer.from(JSON.stringify({type:'webauthn.get',challenge:b64(hash(bytes)),origin:ORIGIN,crossOrigin:false}));
  const sig=crypto.sign('sha256',Buffer.concat([authenticator,hash(client)]),pair.privateKey);
  return {credential,proof:{kind:'WEBAUTHN_ES256',credential_id:credential.credential_id,
     authenticator_data:b64(authenticator),client_data_json:b64(client),
     signature_der:b64(sig),synthetic_non_owner:true},synthetic_non_owner:true};
}
function verifyES256(statement,proof,credential) {
  try {
    const expectedChallenge=b64(hash(statementBytes(statement)));
    if(proof?.kind!=='WEBAUTHN_ES256'||proof.credential_id!==credential.credential_id)return {valid:false};
    const auth=Buffer.from(proof.authenticator_data,'base64url');
    const rawClient=Buffer.from(proof.client_data_json,'base64url');
    const signature=Buffer.from(proof.signature_der,'base64url');
    for(const [encoded,decoded] of [[proof.authenticator_data,auth],[proof.client_data_json,rawClient],[proof.signature_der,signature]])
      if(typeof encoded!=='string'||b64(decoded)!==encoded)return {valid:false};
    if(auth.length!==37||!auth.subarray(0,32).equals(hash(Buffer.from(RP)))||(auth[32]&5)!==5)return {valid:false};
    const client=JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(rawClient));
    if(Object.keys(client).sort().join(',')!=='challenge,crossOrigin,origin,type'||
       client.type!=='webauthn.get'||client.origin!==ORIGIN||client.crossOrigin!==false||
       client.challenge!==expectedChallenge)return {valid:false};
    return {valid:crypto.verify('sha256',Buffer.concat([auth,hash(rawClient)]),publicES256(credential),signature)};
  } catch {return {valid:false};}
}
function dispatch(request) {
  switch(request.method) {
    case 'sign_ssh':return signSSH(request.label,request.statement);
    case 'sign_es256':return signES256(request.label,request.statement);
    case 'verify_es256':return verifyES256(request.statement,request.proof,request.credential);
    default:throw Error('unsupported non-owner method');
  }
}
if(process.argv.slice(2).join(' ')!=='--synthetic-rpc')throw Error('only explicitly synthetic RPC mode is supported');
for await(const line of readline.createInterface({input:process.stdin,crlfDelay:Infinity})) {
  try {const msg=JSON.parse(line);process.stdout.write(JSON.stringify({ok:true,result:dispatch(msg)})+'\n');}
  catch {process.stdout.write(JSON.stringify({ok:false,error:'synthetic input validation failed'})+'\n');}
}
