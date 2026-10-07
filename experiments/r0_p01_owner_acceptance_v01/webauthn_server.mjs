/** R0-P01 V02 probe. Built-ins only. Default invocation performs no ceremony.
 * --rpc: public verification / explicitly synthetic, non-owner test material.
 * --serve: localhost UI; registration is disabled until the owner-run controller
 * has recorded the attempt boundary and sent initialize. Never logs requests.
 */
import * as crypto from 'node:crypto';
import http from 'node:http';
import readline from 'node:readline';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import assert from 'node:assert/strict';

const ORIGIN = 'http://localhost:8765', RP = 'localhost';
const FIELDS = ['context','project_id','acceptance_id','envelope_digest','shown_digest',
  'decision','semantic_base_digest','signer_set_version','issued_at'].sort();
const sha = b => crypto.createHash('sha256').update(b).digest();
const b64 = b => Buffer.from(b).toString('base64url');
function strictJSON(text) {
  const value=JSON.parse(text);
  const tokens=text.match(/"(?:\\.|[^"\\])*"|[{}\[\],:]|true|false|null|-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/g);
  let i=0;
  function visit(depth=0) {
    if(depth>128)throw Error('JSON depth');
    const t=tokens[i++];
    if(t==='{') {
      const keys=new Set();
      while(tokens[i]!=='}') {
        const key=JSON.parse(tokens[i++]);if(keys.has(key))throw Error('duplicate JSON key');keys.add(key);
        if(tokens[i++]!==':')throw Error('JSON structure');visit(depth+1);
        if(tokens[i]!==',')break;i++;
      }
      if(tokens[i++]!=='}')throw Error('JSON structure');
    }else if(t==='[') {
      while(tokens[i]!==']'){visit(depth+1);if(tokens[i]!==',')break;i++;}
      if(tokens[i++]!==']')throw Error('JSON structure');
    }
  }
  visit();if(i!==tokens.length)throw Error('JSON structure');
  canonical(value);return value;
}
function decode(s) {
  if (typeof s !== 'string' || !/^[A-Za-z0-9_-]*$/.test(s)) throw Error('invalid base64url');
  const b = Buffer.from(s, 'base64url');
  if (b64(b) !== s) throw Error('noncanonical base64url');
  return b;
}
function compareCodepoints(a,b) {
  const aa=Array.from(a,c=>c.codePointAt(0)), bb=Array.from(b,c=>c.codePointAt(0));
  for(let i=0;i<Math.min(aa.length,bb.length);i++) if(aa[i]!==bb[i]) return aa[i]-bb[i];
  return aa.length-bb.length;
}
export function canonical(x) {
  if(x===null || typeof x==='boolean') return JSON.stringify(x);
  if(typeof x==='string') {
    for(let i=0;i<x.length;i++) {
      const c=x.charCodeAt(i);
      if(c>=0xd800 && c<=0xdbff) { const d=x.charCodeAt(++i); if(!(d>=0xdc00&&d<=0xdfff)) throw Error('surrogate'); }
      else if(c>=0xdc00 && c<=0xdfff) throw Error('surrogate');
    }
    return JSON.stringify(x);
  }
  if(typeof x==='number') {
    if(!Number.isFinite(x)) throw Error('nonfinite JSON');
    return JSON.stringify(x);
  }
  if(Array.isArray(x)) return '['+x.map(canonical).join(',')+']';
  if(x && Object.getPrototypeOf(x)===Object.prototype)
    return '{'+Object.keys(x).sort(compareCodepoints).map(k=>canonical(k)+':'+canonical(x[k])).join(',')+'}';
  throw Error('invalid JSON type');
}
function statementBytes(s) {
  if(!s || canonical(Object.keys(s).sort())!==canonical(FIELDS) || FIELDS.some(k=>typeof s[k]!=='string')) throw Error('statement shape');
  if(!['ACCEPT','AMEND','REJECT'].includes(s.decision)) throw Error('decision');
  for(const k of ['envelope_digest','shown_digest','semantic_base_digest']) if(!/^[0-9a-f]{64}$/.test(s[k])) throw Error('digest');
  return Buffer.from(canonical(s));
}
function publicKey(credential) {
  const der=decode(credential.spki_der);
  const key=crypto.createPublicKey({key:der,type:'spki',format:'der'});
  if(key.asymmetricKeyType!=='ec' || key.asymmetricKeyDetails.namedCurve!=='prime256v1') throw Error('not P-256');
  if(!key.export({format:'der',type:'spki'}).equals(der)) throw Error('SPKI encoding');
  if(credential.public_id!==undefined && credential.public_id!=='WEBAUTHN-ES256-SPKI-SHA256-HEX:'+sha(der).toString('hex'))throw Error('public identity');
  return key;
}
function clientData(proof,type,challenge) {
  const bytes=decode(proof.client_data_json);
  const c=strictJSON(new TextDecoder('utf-8',{fatal:true}).decode(bytes));
  if(c.type!==type || c.challenge!==challenge || c.origin!==ORIGIN) throw Error('client binding');
  return bytes;
}
function authenticator(proof) {
  const a=decode(proof.authenticator_data);
  if(a.length<37 || !a.subarray(0,32).equals(sha(Buffer.from(RP))) || !(a[32]&1) || !(a[32]&4)) throw Error('authenticator binding');
  return a;
}
export function verifyAssertion(statement,proof,credential) {
  try {
    const bytes=statementBytes(statement);
    if(proof.kind!=='WEBAUTHN_ES256' || proof.credential_id!==credential.credential_id || !decode(proof.credential_id).length) return {valid:false};
    const c=clientData(proof,'webauthn.get',b64(sha(bytes))), a=authenticator(proof);
    const valid=crypto.verify('sha256',Buffer.concat([a,sha(c)]),publicKey(credential),decode(proof.signature_der));
    return {valid,sign_count:a.readUInt32BE(33)};
  } catch { return {valid:false}; }
}
export function verifyRegistration(response,pending) {
  if(decode(pending.challenge).length!==32)throw Error('registration challenge');
  if(response.algorithm!==-7) throw Error('not ES256');
  clientData(response,'webauthn.create',pending.challenge);
  const a=authenticator(response), id=decode(response.credential_id);
  if(!(a[32]&0x40) || a.length<55 || !id.length) throw Error('registration structure');
  const n=a.readUInt16BE(53);
  if(n!==id.length || a.length<55+n || !a.subarray(55,55+n).equals(id)) throw Error('credential ID binding');
  const credential={kind:'WEBAUTHN_ES256',credential_id:response.credential_id,spki_der:response.spki_der};
  publicKey(credential);
  credential.public_id='WEBAUTHN-ES256-SPKI-SHA256-HEX:'+sha(decode(response.spki_der)).toString('hex');
  return credential;
}
export class CeremonyState {
  constructor(now=()=>Number(process.hrtime.bigint())/1e6,wallNow=()=>Date.now()) { this.now=now; this.wallNow=wallNow; this.pending=null; this.credential=null; this.events=[]; this.initialized=false; this.registrationCount=0; this.interruptions=0; this.job=null; }
  initialize(attempt,arm) {
    if(this.initialized || attempt!=='001' || arm!=='B') throw Error('attempt identity');
    this.initialized=true; this.attempt=attempt; this.arm=arm;
  }
  issue(type,statement=null) {
    if(!['registration','assertion'].includes(type))throw Error('ceremony type');
    if(!this.initialized || this.pending) throw Error('not ready');
    if(type==='registration') {
      if(this.credential || this.registrationCount>=2 || (this.registrationCount===1&&this.interruptions!==1)) throw Error('registration repeat forbidden');
      this.registrationCount++;
    } else if(!this.credential || !this.job) throw Error('no registered job');
    const now=this.now(),wall=this.wallNow();
    this.pending={type,attempt_id:this.attempt,arm:this.arm,issued_monotonic_ms:now,issued_at:new Date(wall).toISOString(),expires_at:new Date(wall+120000).toISOString(),deadline:now+120000,unused:true,
      challenge:type==='registration'?b64(crypto.randomBytes(32)):b64(sha(statementBytes(statement))),
      statement:statement?structuredClone(statement):null,acceptance_id:statement?.acceptance_id??null};
    this.events.push({type,status:'ISSUED',attempt_id:this.attempt,arm:this.arm,issued_at:this.pending.issued_at,expires_at:this.pending.expires_at,challenge:this.pending.challenge,acceptance_id:this.pending.acceptance_id});
    return structuredClone(this.pending);
  }
  take(type) {
    const p=this.pending;
    if(!p || p.type!==type) throw Error('no pending ceremony');
    this.pending=null; p.unused=false;
    p.submitted_elapsed_ms=this.now()-p.issued_monotonic_ms;p.submitted_at=new Date(this.wallNow()).toISOString();
    if(p.submitted_elapsed_ms>=120000) { this.cancelEvent(type,'TIMEOUT'); throw Error('expired'); }
    return p;
  }
  cancelEvent(type,reason) {
    const interruption=['OWNER_CANCELLED','OWNER_CANCELLED_OR_TIMEOUT','NotAllowedError','TIMEOUT'].includes(reason);
    const capability=['REQUIRED_RESPONSE_METHOD_UNAVAILABLE','ES256_UNAVAILABLE','NotSupportedError'].includes(reason);
    if(type==='registration'&&interruption)this.interruptions++;
    this.events.push({type,status:interruption?'SETUP_INTERRUPTED':capability?'NOT_REALIZABLE':'INCOMPLETE',reason,at_utc:new Date(this.wallNow()).toISOString()});
  }
  cancel(reason) {
    if(!this.pending) throw Error('no pending ceremony');
    const type=this.pending.type; this.pending=null; this.cancelEvent(type,reason);
  }
  register(response) {
    const p=this.take('registration');
    try {
      const credential=verifyRegistration(response,p);
      this.credential=credential; this.events.push({type:'registration',status:'VERIFIED',attempt_id:p.attempt_id,arm:p.arm,challenge:p.challenge,issued_at:p.issued_at,expires_at:p.expires_at,submitted_at:p.submitted_at,submitted_elapsed_ms:p.submitted_elapsed_ms,consumed:true,response:structuredClone(response),credential});
      return credential;
    } catch { this.events.push({type:'registration',status:'INVALID',reason:'registration verification failed'}); throw Error('registration verification failed'); }
  }
  assert(response) {
    const p=this.take('assertion'), result=verifyAssertion(p.statement,response,this.credential);
    this.events.push({type:'assertion',attempt_id:p.attempt_id,arm:p.arm,acceptance_id:p.acceptance_id,issued_at:p.issued_at,expires_at:p.expires_at,submitted_at:p.submitted_at,submitted_elapsed_ms:p.submitted_elapsed_ms,consumed:true,result});
    return result;
  }
  snapshot() {
    if(this.pending && this.now()>=this.pending.deadline) { const t=this.pending.type; this.pending=null; this.cancelEvent(t,'TIMEOUT'); }
    return {credential:this.credential,events:this.events,registration_count:this.registrationCount,interruptions:this.interruptions,job:this.job};
  }
}

// Ed25519 SSHSIG non-owner test material. Private KeyObjects stay in process
// memory; output is public key and proof only. Never an owner-key substitute.
const sshString=b=>{b=Buffer.from(b);const n=Buffer.alloc(4);n.writeUInt32BE(b.length);return Buffer.concat([n,b]);};
const syntheticKeys=new Map();
function syntheticWebAuthn(id,statement) {
  if(typeof id!=='string'||!id.startsWith('SYNTHETIC-NON-OWNER-'))throw Error('synthetic label required');
  const label='ES256:'+id;
  if(!syntheticKeys.has(label))syntheticKeys.set(label,crypto.generateKeyPairSync('ec',{namedCurve:'prime256v1'}));
  const pair=syntheticKeys.get(label),der=pair.publicKey.export({format:'der',type:'spki'});
  const credential={kind:'WEBAUTHN_ES256',credential_id:b64(Buffer.from(id)),spki_der:b64(der),public_id:'WEBAUTHN-ES256-SPKI-SHA256-HEX:'+sha(der).toString('hex')};
  const a=Buffer.alloc(37);sha(Buffer.from(RP)).copy(a);a[32]=5;
  const c=Buffer.from(JSON.stringify({type:'webauthn.get',challenge:b64(sha(statementBytes(statement))),origin:ORIGIN}));
  return {synthetic_non_owner:true,label:id,credential,proof:{kind:'WEBAUTHN_ES256',synthetic_non_owner:true,credential_id:credential.credential_id,authenticator_data:b64(a),client_data_json:b64(c),signature_der:b64(crypto.sign('sha256',Buffer.concat([a,sha(c)]),pair.privateKey))}};
}
function syntheticSSH(id,statement) {
  if(typeof id!=='string' || !id.startsWith('SYNTHETIC-NON-OWNER-')) throw Error('synthetic label required');
  if(!syntheticKeys.has(id)) syntheticKeys.set(id,crypto.generateKeyPairSync('ed25519'));
  const pair=syntheticKeys.get(id), raw=pair.publicKey.export({format:'der',type:'spki'}).subarray(-32);
  const pk=Buffer.concat([sshString('ssh-ed25519'),sshString(raw)]), ns='ads-r0-p01-acceptance', hash='sha512';
  const message=Buffer.concat([Buffer.from('SSHSIG'),sshString(ns),sshString(''),sshString(hash),sshString(crypto.createHash(hash).update(statementBytes(statement)).digest())]);
  const sig=Buffer.concat([sshString('ssh-ed25519'),sshString(crypto.sign(null,message,pair.privateKey))]);
  const version=Buffer.alloc(4);version.writeUInt32BE(1);
  const payload=Buffer.concat([Buffer.from('SSHSIG'),version,sshString(pk),sshString(ns),sshString(''),sshString(hash),sshString(sig)]);
  const armor='-----BEGIN SSH SIGNATURE-----\n'+payload.toString('base64').match(/.{1,70}/g).join('\n')+'\n-----END SSH SIGNATURE-----\n';
  return {synthetic_non_owner:true,label:id,credential:{kind:'SSH_ED25519',public_key:'ssh-ed25519 '+pk.toString('base64'),public_id:'SSH-ED25519-SHA256-HEX:'+sha(pk).toString('hex')},proof:{kind:'SSH_ED25519',sshsig:armor,synthetic_non_owner:true}};
}
function golden() {
  const dir=path.dirname(fileURLToPath(import.meta.url)), f=JSON.parse(fs.readFileSync(path.join(dir,'fixture.json'))),v=JSON.parse(fs.readFileSync(path.join(dir,'clarification_vectors_v02.json')));
  const deps=f.semantic_base.effects.toSorted((a,b)=>compareCodepoints(a.effect_id,b.effect_id));
  const base={grammar_version:f.semantic_base.grammar_version,predicate_semantics_version:f.semantic_base.predicate_semantics_version,dependencies:deps};
  const t=f.owner_trials.find(x=>x.trial_id==='S01');
  const envelope={schema:'R0-P01-ENVELOPE-V01',project_id:f.project_id,acceptance_id:'R0-P01-A-S01',item_id:t.trial_id,title:t.title,summary:t.summary,effects:t.effects,dependency_selector:{grammar_version:base.grammar_version,predicate_semantics_version:base.predicate_semantics_version,dependencies:deps.map(d=>({effect_id:d.effect_id,contract_revision:d.contract_revision}))}};
  const dh=o=>sha(Buffer.from(canonical(o))).toString('hex');
  const view=['R0-P01 OWNER VIEW V01','Project: '+f.project_id,'Trial: S01','Acceptance: '+envelope.acceptance_id,'Title: '+t.title,'Summary: '+t.summary,'Semantic base: '+dh(base),'Effects: '+t.effects.length,...t.effects.flatMap((e,i)=>['  ['+(i+1)+'] '+e.grammar+' '+e.effect_id,'  Subject: '+e.subject,'  Text: '+e.text]),'END R0-P01 OWNER VIEW V01',''].join('\n');
  const statement={context:f.statement_context,project_id:f.project_id,acceptance_id:envelope.acceptance_id,envelope_digest:dh(envelope),shown_digest:sha(Buffer.from(view)).toString('hex'),decision:'ACCEPT',semantic_base_digest:dh(base),signer_set_version:f.signer_set_version,issued_at:t.issued_at};
  for(const [k,obj] of [['semantic_base',base],['envelope',envelope],['statement',statement]]) { assert.deepEqual(obj,v[k]);assert.equal(canonical(obj),v['canonical_'+k+'_json']); }
  assert.equal(view,v.owner_view); assert.equal(sha(fs.readFileSync(path.join(dir,'fixture.json'))).toString('hex'),v.fixture_sha256);
  for(const [k,h] of Object.entries({semantic_base_digest:dh(base),envelope_digest:dh(envelope),shown_digest:statement.shown_digest,statement_sha256:dh(statement)})) assert.equal(h,v[k]);
  return {base,envelope,statement,golden:'PASS'};
}
function selftest() {
  const {statement}=golden(), pair=crypto.generateKeyPairSync('ec',{namedCurve:'prime256v1'}), id=b64(Buffer.from('SYNTHETIC-NON-OWNER-CREDENTIAL'));
  const credential={kind:'WEBAUTHN_ES256',credential_id:id,spki_der:b64(pair.publicKey.export({type:'spki',format:'der'}))};
  const a=Buffer.alloc(37);sha(Buffer.from(RP)).copy(a);a[32]=5;
  const c=Buffer.from(JSON.stringify({type:'webauthn.get',challenge:b64(sha(statementBytes(statement))),origin:ORIGIN}));
  const proof={kind:'WEBAUTHN_ES256',credential_id:id,authenticator_data:b64(a),client_data_json:b64(c),signature_der:b64(crypto.sign('sha256',Buffer.concat([a,sha(c)]),pair.privateKey))};
  assert.equal(verifyAssertion(statement,proof,credential).valid,true);
  let negatives=0;
  const boundProof=(client,auth=a)=>({...proof,client_data_json:b64(client),authenticator_data:b64(auth),signature_der:b64(crypto.sign('sha256',Buffer.concat([auth,sha(client)]),pair.privateKey))});
  for(const patch of [{type:'webauthn.create'},{origin:'http://127.0.0.1:8765'},{challenge:sha(statementBytes(statement)).toString('hex')},{challenge:b64(sha(statementBytes(statement)))+'='}]) {
    const client=Buffer.from(JSON.stringify({...JSON.parse(c),...patch}));assert.equal(verifyAssertion(statement,boundProof(client),credential).valid,false);negatives++;
  }
  const duplicate=Buffer.from(c.toString().replace('"type":"webauthn.get"','"type":"webauthn.create","type":"webauthn.get"'));
  assert.equal(verifyAssertion(statement,boundProof(duplicate),credential).valid,false);negatives++;
  for(const flags of [0,1,4]){const data=Buffer.from(a);data[32]=flags;assert.equal(verifyAssertion(statement,boundProof(c,data),credential).valid,false);negatives++;}
  const wrongRP=Buffer.from(a);sha(Buffer.from('other.invalid')).copy(wrongRP);assert.equal(verifyAssertion(statement,boundProof(c,wrongRP),credential).valid,false);negatives++;
  for(const field of FIELDS) { const s={...statement,[field]:field==='decision'?'REJECT':statement[field]+'x'};assert.equal(verifyAssertion(s,proof,credential).valid,false);negatives++; }
  for(const field of ['signature_der','authenticator_data','client_data_json','credential_id']) { const p={...proof,[field]:b64(Buffer.from('bad'))};assert.equal(verifyAssertion(statement,p,credential).valid,false);negatives++; }
  const badkey=crypto.generateKeyPairSync('rsa',{modulusLength:2048}).publicKey.export({type:'spki',format:'der'});
  assert.equal(verifyAssertion(statement,proof,{...credential,spki_der:b64(badkey)}).valid,false);
  // signCount is recorded, not gated, including zero and decreasing values.
  for(const count of [0,20,1]) { const data=Buffer.from(a);data.writeUInt32BE(count,33);const p={...proof,authenticator_data:b64(data),signature_der:b64(crypto.sign('sha256',Buffer.concat([data,sha(c)]),pair.privateKey))};assert.equal(verifyAssertion(statement,p,credential).sign_count,count); }
  let now=1000; const state=new CeremonyState(()=>now);state.initialize('001','B');
  let pending=state.issue('registration');
  const regdata=Buffer.concat([a,Buffer.alloc(16),Buffer.from([0,decode(id).length]),decode(id),Buffer.from([0])]);regdata[32]=0x45;
  const response={algorithm:-7,credential_id:id,spki_der:credential.spki_der,authenticator_data:b64(regdata),client_data_json:b64(Buffer.from(JSON.stringify({type:'webauthn.create',challenge:pending.challenge,origin:ORIGIN})))};
  state.register(response); assert.throws(()=>state.register(response)); assert.throws(()=>state.issue('registration'));
  state.job={}; state.issue('assertion',statement);assert.equal(state.assert(proof).valid,true);assert.throws(()=>state.assert(proof));
  state.issue('assertion',statement); now+=120000;assert.throws(()=>state.assert(proof));
  const interrupted=new CeremonyState(()=>now);interrupted.initialize('001','B');interrupted.issue('registration');interrupted.cancel('OWNER_CANCELLED');interrupted.issue('registration');interrupted.cancel('OWNER_CANCELLED');assert.throws(()=>interrupted.issue('registration'));
  let mono=1000,wall=5000;const skew=new CeremonyState(()=>mono,()=>wall);skew.initialize('001','B');skew.issue('registration');wall-=3600000;mono+=120000;skew.snapshot();assert.equal(skew.pending,null);assert.equal(skew.interruptions,1);
  const defect=new CeremonyState(()=>now);defect.initialize('001','B');defect.issue('registration');defect.cancel('TypeError');assert.throws(()=>defect.issue('registration'));
  for(const patch of [{algorithm:-257},{credential_id:b64(Buffer.from('wrong-id'))},{authenticator_data:b64(Buffer.alloc(37))}])assert.throws(()=>verifyRegistration({...response,...patch},pending));
  return {synthetic_non_owner:true,golden:'PASS',assertion_valid:'PASS',statement_mutations:9,structural_negatives:negatives-9+1,counter_policy:'PASS',registration_binding:'PASS',single_use_expiry_repeat:'PASS',monotonic_expiry:'PASS',defect_cannot_retry:'PASS'};
}

const HTML=String.raw`<!doctype html><meta charset="utf-8"><title>R0-P01 local owner client</title>
<style>body{font:16px sans-serif;max-width:960px;margin:30px auto}pre{white-space:pre-wrap;overflow-wrap:anywhere;border:1px solid #aaa;padding:16px}button{padding:12px;margin:8px}</style>
<h1>R0-P01 local owner client</h1><p>Probe only. Never enter a passphrase or other secret here.</p><p id="status">Waiting for the reviewed owner-run controller.</p>
<button id="register" hidden>Register the probe WebAuthn credential</button><pre id="view"></pre><div id="decisions" hidden><button data-decision="ACCEPT">ACCEPT</button><button data-decision="AMEND">AMEND</button><button data-decision="REJECT">REJECT</button></div><pre id="preview"></pre>
<script>
'use strict';let token=null,job=null,reviewStart=null,displayedAt=null,busy=false;
const enc=b=>btoa(String.fromCharCode(...new Uint8Array(b))).replaceAll('+','-').replaceAll('/','_').replace(/=+$/,'');
const dec=s=>Uint8Array.from(atob(s.replaceAll('-','+').replaceAll('_','/')),c=>c.charCodeAt(0));
async function post(url,body){const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json','X-Probe-Token':token},body:JSON.stringify(body)});const b=await r.json();if(!r.ok)throw Error(b.error);return b;}
const status=t=>document.getElementById('status').textContent=t;
const measuredNumber=s=>s===null||s.trim()===''?null:Number(s);
document.getElementById('register').onclick=async()=>{if(busy)return;busy=true;let issued=false;try{
 if(!window.PublicKeyCredential||!navigator.credentials){await post('/capability',{status:'NOT_REALIZABLE',reason:'WebAuthn API unavailable'});return;}
 const o=await post('/register/options',{});issued=true;o.challenge=dec(o.challenge);o.user.id=dec(o.user.id);
 const cred=await navigator.credentials.create({publicKey:o});const r=cred.response;
 if(typeof r.getPublicKey!=='function'||typeof r.getPublicKeyAlgorithm!=='function'||typeof r.getAuthenticatorData!=='function'||!r.getPublicKey()){await post('/cancel',{reason:'REQUIRED_RESPONSE_METHOD_UNAVAILABLE',capability:true});return;}
 if(r.getPublicKeyAlgorithm()!==-7){await post('/cancel',{reason:'ES256_UNAVAILABLE',capability:true});return;}
 const result=await post('/register/result',{algorithm:r.getPublicKeyAlgorithm(),credential_id:enc(cred.rawId),client_data_json:enc(r.clientDataJSON),authenticator_data:enc(r.getAuthenticatorData()),spki_der:enc(r.getPublicKey())});
 status('Verified public credential: '+result.public_id);
}catch(e){if(issued)await post('/cancel',{reason:e.name==='NotAllowedError'?'OWNER_CANCELLED_OR_TIMEOUT':e.name,capability:e.name==='NotSupportedError'}).catch(()=>{});status('Registration ended: '+e.name);}finally{busy=false;}};
for(const b of document.querySelectorAll('[data-decision]'))b.onclick=async()=>{if(busy||!job)return;busy=true;document.getElementById('decisions').hidden=true;const captured=performance.now(),capturedAt=new Date().toISOString(),semantic=(captured-reviewStart)/1000;let response=null,verified=false,failure=null,mechanical=null,verifiedAt=null;try{
 const o=await post('/decision',{decision:b.dataset.decision,semantic_review_seconds:semantic,displayed_at_utc:displayedAt,decision_at_utc:capturedAt});document.getElementById('preview').textContent=o.canonical_statement;
 await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
 const cred=await navigator.credentials.get({publicKey:{challenge:dec(o.challenge),rpId:'localhost',allowCredentials:[{type:'public-key',id:dec(o.credential_id)}],userVerification:'required',timeout:120000}});
 response={kind:'WEBAUTHN_ES256',credential_id:enc(cred.rawId),client_data_json:enc(cred.response.clientDataJSON),authenticator_data:enc(cred.response.authenticatorData),signature_der:enc(cred.response.signature)};
 const result=await post('/assertion/result',response);verified=result.valid;mechanical=(performance.now()-captured)/1000;verifiedAt=new Date().toISOString();
}catch(e){failure=e.name;await post('/cancel',{reason:e.name}).catch(()=>{});mechanical=(performance.now()-captured)/1000;verifiedAt=new Date().toISOString();}
 status(verified?'Proof locally verified.':'Proof failed or interrupted.');
 // Friction is captured only after the deterministic verification endpoint.
 const rating=prompt('Friction rating 1 through 5 (non-secret)');const note=prompt('Short non-secret friction note');const interactions=prompt('Total user-visible interactions after display');const switches=prompt('Physical device switches');const edits=prompt('Manual metadata edits (including this event)');
 await post('/measurements',{semantic_review_seconds:semantic,mechanical_seconds:mechanical,displayed_at_utc:displayedAt,decision_at_utc:capturedAt,verified_at_utc:verifiedAt,interaction_count:measuredNumber(interactions),device_switches:measuredNumber(switches),manual_metadata_edits:measuredNumber(edits),friction_rating_1_to_5:measuredNumber(rating),friction_note:note,failure});
 job=null;busy=false;};
async function poll(){try{const s=await(await fetch('/state')).json();token=s.token;document.getElementById('register').hidden=!s.registration_allowed; if(s.job&&!busy&&(!job||job.acceptance_id!==s.job.acceptance_id)){job=s.job;document.getElementById('view').textContent=job.owner_view;document.getElementById('preview').textContent='';await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));reviewStart=performance.now();displayedAt=new Date().toISOString();document.getElementById('decisions').hidden=false;status('Review the complete exact view, then choose a decision.');}}catch{}setTimeout(poll,500);}poll();
</script>`;

const state=new CeremonyState(), token=b64(crypto.randomBytes(32));
const secretPattern=/-----BEGIN (?:OPENSSH |RSA |EC |ENCRYPTED )?PRIVATE KEY-----|(?:passphrase|password|recovery_secret|private_key)\s*[:=]|owner_(?:primary|recovery)_ed25519(?!\.pub)/i;
let server=null, completed=null, capability=null;
function dispatch(request) {
  switch(request.method) {
    case 'verify':return verifyAssertion(request.statement,request.proof,request.credential);
    case 'verify_registration':return verifyRegistration(request.response,request.pending);
    case 'synthetic_ssh':return syntheticSSH(request.label,request.statement);
    case 'synthetic_webauthn':return syntheticWebAuthn(request.label,request.statement);
    case 'golden':return golden();
    case 'canonical':return canonical(request.value);
    case 'selftest':return selftest();
    case 'initialize':if(!server)throw Error('not serving');state.initialize(request.attempt_id,request.arm);return {ready:true};
    case 'snapshot':return {...state.snapshot(),capability,completed};
    case 'job':
      if(!state.credential||state.job||state.pending)throw Error('not ready');
      statementBytes({...request.template,decision:'ACCEPT'});
      if(sha(Buffer.from(request.owner_view)).toString('hex')!==request.template.shown_digest)throw Error('view digest');
      state.job={template:request.template,owner_view:request.owner_view,acceptance_id:request.template.acceptance_id};completed=null;return {ready:true};
    case 'collect':{const r=completed;if(r){completed=null;state.job=null;}return r;}
    default:throw Error('unknown method');
  }
}
function serve() {
  server=http.createServer(async(req,res)=>{
    const send=(code,obj)=>{res.writeHead(code,{'Content-Type':'application/json','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});res.end(JSON.stringify(obj));};
    if(req.headers.host!=='localhost:8765')return send(403,{error:'host'});
    if(req.method==='GET'&&req.url==='/'){res.writeHead(200,{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store','Content-Security-Policy':"default-src 'self'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'"});return res.end(HTML);}
    if(req.method==='GET'&&req.url==='/state'){state.snapshot();return send(200,{token,registration_allowed:state.initialized&&!state.credential&&!state.pending&&!capability&&state.registrationCount<2&&(state.registrationCount===0||state.interruptions===1),job:state.job?.template&&!state.job.statement&&!completed?{owner_view:state.job.owner_view,acceptance_id:state.job.acceptance_id}:null});}
    if(req.method!=='POST'||req.headers.origin!==ORIGIN||req.headers['x-probe-token']!==token||req.headers['content-type']!=='application/json')return send(403,{error:'request binding'});
    try {
      let chunks=[],length=0;for await(const c of req){length+=c.length;if(length>1048576)throw Error('body limit');chunks.push(c);}
      const body=strictJSON(Buffer.concat(chunks).toString('utf8'));
      switch(req.url){
        case '/capability':if(!state.initialized||state.credential)throw Error('state');capability={status:'NOT_REALIZABLE',reason:body.reason};state.events.push({type:'capability',browser_user_agent:req.headers['user-agent']??null,...capability});return send(200,{recorded:true});
        case '/register/options':{const p=state.issue('registration');state.events.at(-1).browser_user_agent=req.headers['user-agent']??null;return send(200,{challenge:p.challenge,rp:{id:RP,name:'R0-P01 probe'},user:{id:b64(Buffer.from('R0-P01-001-B')),name:'probe-owner',displayName:'Probe owner'},pubKeyCredParams:[{type:'public-key',alg:-7}],timeout:120000,attestation:'none',authenticatorSelection:{userVerification:'required',residentKey:'preferred'}});}
        case '/register/result':return send(200,state.register(body));
        case '/decision':{
          if(!state.job||state.job.statement)throw Error('decision already captured');
          const statement={...state.job.template,decision:body.decision};statementBytes(statement);state.job.statement=statement;
          state.job.capture={semantic_review_seconds:body.semantic_review_seconds,displayed_at_utc:body.displayed_at_utc,decision_at_utc:body.decision_at_utc};
          const p=state.issue('assertion',statement);return send(200,{canonical_statement:canonical(statement),challenge:p.challenge,credential_id:state.credential.credential_id});}
        case '/assertion/result':{
          if(!state.job?.statement)throw Error('no assertion job');
          if(state.job.verification!==undefined)throw Error('first proof result already frozen');
          // An expired/consumed ceremony cannot mint an accepted proof record.
          // Retain the public submitted bytes separately, with a rejection receipt.
          let result;
          try {result=state.assert(body);state.job.proof=structuredClone(body);}
          catch {result={valid:false,ceremony_rejected:true};state.job.rejected_public_response=structuredClone(body);state.job.proof=null;}
          state.job.verification=result;return send(200,result);}
        case '/cancel':{
          if(state.pending)state.cancel(body.reason);
          if(body.capability){capability={status:'NOT_REALIZABLE',reason:body.reason};state.events.push({type:'capability',...capability});}
          if(state.job&&state.job.verification===undefined){state.job.verification={valid:false};state.job.failure=body.reason;}
          return send(200,{recorded:true});}
        case '/measurements':{
          if(!state.job?.statement||state.pending||completed)throw Error('measurement state');
          if(body.friction_note!==null&&typeof body.friction_note!=='string')throw Error('note');
          if(secretPattern.test(body.friction_note)){body.friction_note='[REDACTED SECRET-BOUNDARY VIOLATION]';body.secret_exposure=true;}
          completed={statement:state.job.statement,proof:state.job.proof??null,verification:state.job.verification??{valid:false},rejected_public_response:state.job.rejected_public_response??null,measurements:body};return send(200,{recorded:true});}
        default:return send(404,{error:'route'});
      }
    }catch{return send(400,{error:'local validation failed'});}
  });
  server.listen(8765,'localhost');server.on('error',()=>{process.stderr.write('R0-P01 localhost server unavailable\n');process.exitCode=1;});
}
if(process.argv.includes('--selftest')) console.log(JSON.stringify(selftest()));
else if(process.argv.includes('--golden')) console.log(JSON.stringify(golden()));
else if(process.argv.includes('--rpc')||process.argv.includes('--serve')) {
  if(process.argv.includes('--serve'))serve();
  const rl=readline.createInterface({input:process.stdin,crlfDelay:Infinity});
  rl.on('line',line=>{try{const r=dispatch(strictJSON(line));process.stdout.write(JSON.stringify({ok:true,result:r})+'\n');}catch{process.stdout.write(JSON.stringify({ok:false,error:'R0-P01 request validation failed'})+'\n');}});
  rl.on('close',()=>{server?.close();});
} else if(process.argv[1]===fileURLToPath(import.meta.url)) console.log('R0-P01: --golden / --selftest / --rpc / --serve (no ceremony without initialized owner controller)');
