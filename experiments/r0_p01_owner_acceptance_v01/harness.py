"""R0-P01 V02 bounded probe; stdlib only. Import/preflight never starts Attempt 001.

Owner execution is a separate, explicit --owner-run entry point requiring a
clean implementation freeze and a new evidence directory outside the repository.
No private-key path or subprocess diagnostic is put in public evidence.
"""
import argparse
import base64
import copy
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import re
import statistics
import struct
import subprocess
import sys
import tempfile
import time
from unittest import mock

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FROZEN_HEAD = 'fb19c4f9deebf1b667d64f2e4f82c68569ab2daf'
V1, V2, V2R = 'SIGNERS-P01-V1', 'SIGNERS-P01-V2', 'SIGNERS-P01-V2R'
CONTRACT_FILES = ('fixture.json', 'implementation_contract.md',
                  'implementation_contract_addendum_v02.md', 'clarification_vectors_v02.json',
                  'security_control_contract.md', 'result_contract.json', 'legacy_volume_inventory_rule.json')
IMPLEMENTATION_FILES = ('harness.py', 'webauthn_server.mjs', 'score.py')
STATEMENT_FIELDS = {'context', 'project_id', 'acceptance_id', 'envelope_digest', 'shown_digest',
                    'decision', 'semantic_base_digest', 'signer_set_version', 'issued_at'}
DECISIONS = ('ACCEPT', 'AMEND', 'REJECT')
TRUST_GRAMMARS = ('TRUST_ROOT_ROTATE', 'TRUST_ROOT_RECOVERY_ROTATE')


class IntegrityError(Exception):
    """Public error messages must never contain subprocess/owner input."""


class InventoryMismatch(IntegrityError):
    pass


class SetupInterrupted(Exception):
    pass


class SecretBoundaryError(IntegrityError):
    pass


class CapabilityUnavailable(Exception):
    pass


def strict_json(data):
    def pairs(items):
        out = {}
        for k, v in items:
            if k in out:
                raise IntegrityError('duplicate JSON key')
            out[k] = v
        return out
    def constant(_):
        raise IntegrityError('nonfinite JSON')
    return json.loads(data, object_pairs_hook=pairs, parse_constant=constant)


def canonical(obj):
    # Encoding rejects unpaired surrogates; all frozen signed values are ASCII.
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      allow_nan=False).encode('utf-8')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(obj):
    return sha(canonical(obj))


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def git(*args):
    p = subprocess.run(['git', '--no-optional-locks', *args], cwd=ROOT,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise IntegrityError('repository provenance unavailable')
    return p.stdout


def contracts():
    values = {}
    for name in CONTRACT_FILES:
        data = (HERE / name).read_bytes()
        relative = (HERE / name).relative_to(ROOT).as_posix()
        if data != git('cat-file', 'blob', FROZEN_HEAD + ':' + relative):
            raise IntegrityError('frozen contract byte mismatch')
        if name.endswith('.json'):
            values[name] = strict_json(data)
    return values


def inventory():
    r = strict_json((HERE / 'legacy_volume_inventory_rule.json').read_bytes())
    try:
        if r['source_byte_basis'] != 'GIT_BLOB_LF':
            raise ValueError()
        expected_oid = r['source_git_blob_oid']
        for revision in (r['source_last_changing_commit'], 'HEAD'):
            if git('rev-parse', revision + ':' + r['source_path']).decode().strip() != expected_oid:
                raise ValueError()
        blob = git('cat-file', 'blob', expected_oid)
        if len(blob) != r['source_bytes'] or sha(blob) != r['source_sha256']:
            raise ValueError()
        units = [u for a in strict_json(blob)['source_annotations'] for u in a['obligation_units']]
        sizes = [len(u['propositions']) for u in units]
        actual = {'projected_acceptance_count': len(units), 'projected_effect_count': sum(sizes),
                  'effects_per_acceptance_distribution': {str(i): sizes.count(i) for i in range(1, 5)},
                  'min_effects_per_acceptance': min(sizes), 'median_effects_per_acceptance': statistics.median(sizes),
                  'max_effects_per_acceptance': max(sizes)}
        if actual != r['frozen_inventory']:
            raise ValueError()
        return {'source_git_blob_oid': expected_oid, 'source_sha256': sha(blob),
                'source_bytes': len(blob), **actual}
    except (KeyError, ValueError, TypeError, IntegrityError):
        raise InventoryMismatch('inventory/source mismatch; prospective refreeze required') from None


def member(role, credential):
    return {'role': role, 'kind': credential['kind'], 'public_id': credential['public_id']}


def sorted_members(members):
    return sorted(copy.deepcopy(members), key=lambda m: (m['role'], m['kind'], m['public_id']))


def selector(f, trust=False):
    b = f['semantic_base']
    s = {'grammar_version': b['grammar_version'], 'predicate_semantics_version': b['predicate_semantics_version'],
         'dependencies': [{'effect_id': d['effect_id'], 'contract_revision': d['contract_revision']}
                          for d in sorted(b['effects'], key=lambda d: d['effect_id'])]}
    if trust:
        s['trust_root_subject'] = 'SYNTHETIC-SIGNER-SET'
    return s


def semantic_base(f, dependencies=None, envelope=None, version=V1, members=None):
    current = f['semantic_base']['effects'] if dependencies is None else dependencies
    ids = [d['effect_id'] for d in current]
    if len(ids) != len(set(ids)) or set(ids) != {'BASE-A', 'BASE-B'}:
        raise IntegrityError('missing/duplicate dependencies')
    b = {'grammar_version': f['semantic_base']['grammar_version'],
         'predicate_semantics_version': f['semantic_base']['predicate_semantics_version'],
         'dependencies': [{k: d[k] for k in ('effect_id', 'status', 'lineage_head', 'contract_revision')}
                          for d in sorted(current, key=lambda d: d['effect_id'])]}
    trust = envelope is not None and any(e['grammar'] in TRUST_GRAMMARS for e in envelope['effects'])
    if envelope is not None:
        wanted = selector(f, trust)
        if envelope['dependency_selector'] != wanted:
            raise IntegrityError('selector mismatch')
        if any(d['contract_revision'] != next(p['contract_revision'] for p in wanted['dependencies']
                                              if p['effect_id'] == d['effect_id']) for d in b['dependencies']):
            raise IntegrityError('pinned revision mismatch')
    if trust:
        if members is None:
            raise IntegrityError('missing trust state')
        b['signer_set'] = {'version': version, 'members_digest': digest(sorted_members(members))}
    return b


def envelope(f, arm, item, owner_primary=None, owner_recovery=None):
    if arm not in 'ABC' or len(arm) != 1:
        raise IntegrityError('arm identity')
    t = next((t for t in f['owner_trials'] if t['trial_id'] == item), None)
    trust = item in ('P5', 'P6')
    if t is not None:
        fields = {'acceptance_id': 'R0-P01-' + arm + '-' + item, 'item_id': item,
                  'title': t['title'], 'summary': t['summary'], 'effects': copy.deepcopy(t['effects'])}
    elif item == 'P0':
        fields = {'acceptance_id': 'R0-P01-' + arm + '-SEC-VALID_ACCEPTANCE', 'item_id': 'SECURITY_BASELINE',
                  'title': 'Security control baseline', 'summary': 'One-effect synthetic baseline for R0-P01 exact-binding controls.',
                  'effects': [{'effect_id': 'SEC-BASE-001', 'grammar': 'REQUIRE', 'subject': 'SYNTHETIC-SECURITY-BASELINE',
                               'text': 'Synthetic low-consequence security baseline effect for R0-P01 exact-binding qualification.', 'independently_acceptable': True}]}
    elif trust:
        if not owner_primary or not owner_recovery:
            raise IntegrityError('missing transition bindings')
        target_primary = owner_recovery if item == 'P6' or arm == 'A' else owner_primary
        target_recovery = owner_primary if item == 'P6' or arm == 'A' else owner_recovery
        recovery = item == 'P6'
        fields = {'acceptance_id': 'R0-P01-' + arm + '-SEC-' + ('RECOVERY_CREDENTIAL_DRY_RUN' if recovery else 'TRUST_ROOT_ROTATION_DRY_RUN'),
                  'item_id': 'RECOVERY_ROTATION' if recovery else 'TRUST_ROOT_ROTATION',
                  'title': 'Synthetic recovery rotation' if recovery else 'Synthetic trust-root rotation',
                  'summary': 'Synthetic prospective recovery trust-root rotation for R0-P01.' if recovery else 'Synthetic prospective ordinary trust-root rotation for R0-P01.',
                  'effects': [{'effect_id': 'TRUST-RECOVERY-001' if recovery else 'TRUST-ROTATE-001',
                               'grammar': TRUST_GRAMMARS[1 if recovery else 0], 'subject': 'SYNTHETIC-SIGNER-SET',
                               'text': ('Recover' if recovery else 'Rotate') + ' SIGNERS-P01-V1 -> ' + (V2R if recovery else V2) + '; PRIMARY: ' + target_primary['public_id'] + '; RECOVERY: ' + target_recovery['public_id'] + '.',
                               'independently_acceptable': True}]}
    else:
        raise IntegrityError('item identity')
    return {'schema': 'R0-P01-ENVELOPE-V01', 'project_id': f['project_id'], **fields,
            'dependency_selector': selector(f, trust)}


def issued_at(f, item):
    return {'P0': '2026-10-04T01:00:00Z', 'P5': '2026-10-04T01:01:00Z',
            'P6': '2026-10-04T01:02:00Z'}[item] if item in ('P0', 'P5', 'P6') else next(t['issued_at'] for t in f['owner_trials'] if t['trial_id'] == item)


def render(e, base_digest):
    lines = ['R0-P01 OWNER VIEW V01', 'Project: ' + e['project_id'], 'Trial: ' + e['item_id'],
             'Acceptance: ' + e['acceptance_id'], 'Title: ' + e['title'], 'Summary: ' + e['summary'],
             'Semantic base: ' + base_digest, 'Effects: ' + str(len(e['effects']))]
    for i, effect in enumerate(e['effects'], 1):
        lines.extend(['  [' + str(i) + '] ' + effect['grammar'] + ' ' + effect['effect_id'],
                      '  Subject: ' + effect['subject'], '  Text: ' + effect['text']])
    return ('\n'.join(lines + ['END R0-P01 OWNER VIEW V01']) + '\n').encode('utf-8')


def statement(f, e, base, view, decision, timestamp, version):
    if decision not in DECISIONS:
        raise IntegrityError('decision')
    return {'context': f['statement_context'], 'project_id': e['project_id'], 'acceptance_id': e['acceptance_id'],
            'envelope_digest': digest(e), 'shown_digest': sha(view), 'decision': decision,
            'semantic_base_digest': digest(base), 'signer_set_version': version, 'issued_at': timestamp}


def golden(f, vectors):
    b = semantic_base(f)
    e = envelope(f, 'A', 'S01')
    v = render(e, digest(b))
    s = statement(f, e, b, v, 'ACCEPT', issued_at(f, 'S01'), V1)
    for key, obj in (('semantic_base', b), ('envelope', e), ('statement', s)):
        if obj != vectors[key] or canonical(obj).decode() != vectors['canonical_' + key + '_json']:
            raise IntegrityError('golden object/byte mismatch')
    hashes = {'semantic_base_digest': digest(b), 'envelope_digest': digest(e), 'shown_digest': sha(v), 'statement_sha256': digest(s)}
    if v.decode() != vectors['owner_view'] or any(h != vectors[k] for k, h in hashes.items()) or sha((HERE / 'fixture.json').read_bytes()) != vectors['fixture_sha256']:
        raise IntegrityError('golden digest/fixture mismatch')
    return hashes


class NodeBridge:
    def __init__(self, serving=False):
        self.process = subprocess.Popen(['node', str(HERE / 'webauthn_server.mjs'), '--serve' if serving else '--rpc'],
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                        text=True, encoding='utf-8', env=no_agent_env())

    def call(self, method, **fields):
        self.process.stdin.write(json.dumps({'method': method, **fields}, ensure_ascii=False) + '\n')
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if not line:
            raise IntegrityError('local Node verifier unavailable')
        reply = strict_json(line)
        if not reply['ok']:
            raise IntegrityError('local Node validation failed')
        return reply['result']

    def close(self):
        if self.process.poll() is None:
            self.process.stdin.close()
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.terminate()
                self.process.wait(timeout=3)


def ssh_public(text):
    try:
        parts = text.split()
        blob = base64.b64decode(parts[1], validate=True)
        n = struct.unpack('>I', blob[:4])[0]
        if parts[0] != 'ssh-ed25519' or blob[4:4+n] != b'ssh-ed25519' or len(blob) != 4+n+4+32 or struct.unpack('>I', blob[4+n:8+n])[0] != 32:
            raise ValueError()
        return {'kind': 'SSH_ED25519', 'public_key': 'ssh-ed25519 ' + parts[1],
                'public_id': 'SSH-ED25519-SHA256-HEX:' + sha(blob)}
    except (ValueError, IndexError, struct.error):
        raise IntegrityError('invalid Ed25519 public key') from None


def valid_credential(c):
    if c['kind'] == 'SSH_ED25519':
        return ssh_public(c['public_key'])['public_id'] == c['public_id']
    if c['kind'] == 'WEBAUTHN_ES256':
        der = base64.urlsafe_b64decode(c['spki_der'] + '=' * (-len(c['spki_der']) % 4))
        return c['public_id'] == 'WEBAUTHN-ES256-SPKI-SHA256-HEX:' + sha(der)
    return False


def verify(s, proof, credential, node):
    try:
        if set(s) != STATEMENT_FIELDS or any(not isinstance(v, str) for v in s.values()) or s['decision'] not in DECISIONS:
            return False
        if any(not re.fullmatch('[0-9a-f]{64}', s[k]) for k in ('envelope_digest', 'shown_digest', 'semantic_base_digest')):
            return False
        if not proof or proof['kind'] != credential['kind'] or not valid_credential(credential):
            return False
        if credential['kind'] == 'WEBAUTHN_ES256':
            return node.call('verify', statement=s, proof=proof, credential=credential)['valid'] is True
        # These temporary files contain only public material and canonical proposals.
        with tempfile.TemporaryDirectory(prefix='r0-p01-public-verify-') as tmp:
            d = Path(tmp)
            (d / 'allowed').write_text('r0-p01 ' + credential['public_key'] + '\n', encoding='utf-8')
            (d / 'proof').write_text(proof['sshsig'], encoding='ascii')
            p = subprocess.run(['ssh-keygen', '-Y', 'verify', '-f', str(d / 'allowed'), '-I', 'r0-p01',
                                '-n', 'ads-r0-p01-acceptance', '-s', str(d / 'proof')], input=canonical(s),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=no_agent_env())
            return p.returncode == 0
    except (KeyError, ValueError, TypeError, UnicodeError, OSError, IntegrityError):
        return False


def no_agent_env():
    keep={'PATH','PATHEXT','SYSTEMROOT','WINDIR','COMSPEC','SYSTEMDRIVE','PROGRAMDATA','TEMP','TMP',
          'LOCALAPPDATA','APPDATA','USERPROFILE','USERNAME','USERDOMAIN','HOMEDRIVE','HOMEPATH',
          'TERM','LANG','LC_ALL'}
    env={key:value for key,value in os.environ.items() if key.upper() in keep}
    env['SSH_AUTH_SOCK']='R0-P01-AGENT-DISABLED-NONEXISTENT'
    env['PYTHONDONTWRITEBYTECODE']='1'
    return env


def record(f, arm, item, ledger, decision, proof, credential):
    e = envelope(f, arm, item, ledger.a_primary, ledger.a_recovery)
    b = ledger.base(e)
    view = render(e, digest(b))
    s = statement(f, e, b, view, decision, issued_at(f, item), ledger.version)
    return {'item': item, 'envelope': e, 'statement': s, 'canonical_statement': canonical(s).decode(),
            'statement_sha256': digest(s), 'owner_view': view.decode(), 'proof': copy.deepcopy(proof),
            'credential': copy.deepcopy(credential), 'renderer_profile': f['renderer_profile'], 'verifier_result':None}


class Ledger:
    def __init__(self, f, arm, primary, recovery, a_primary, a_recovery, scenario):
        self.f, self.arm, self.a_primary, self.a_recovery = f, arm, copy.deepcopy(a_primary), copy.deepcopy(a_recovery)
        self.scenario = scenario
        self.version = V1
        self.members = sorted_members([member('PRIMARY', primary), member('RECOVERY', recovery)])
        self.dependencies = copy.deepcopy(f['semantic_base']['effects'])
        self.consumed = set()
        self.entries = [{'sequence': 1, 'kind': 'GENESIS', 'version': V1, 'members': copy.deepcopy(self.members),
                         'provenance': 'EXPLICIT_SYNTHETIC_TOFU'}]
        self.effects = []

    def base(self, e):
        return semantic_base(self.f, self.dependencies, e, self.version, self.members)

    def authorized(self, credential, role):
        return valid_credential(credential) and member(role, credential) in self.members

    def target(self, item):
        if item == 'P6' or self.arm == 'A':
            return sorted_members([member('PRIMARY', self.a_recovery), member('RECOVERY', self.a_primary)])
        return sorted_members([member('PRIMARY', self.a_primary), member('RECOVERY', self.a_recovery)])

    def admit(self, rec, node):
        try:
            s, e, c = rec['statement'], rec['envelope'], rec['credential']
            if not verify(s, rec['proof'], c, node):
                return {'admitted': False, 'reason': 'INVALID_PROOF'}
            expected_e = envelope(self.f, self.arm, rec['item'], self.a_primary, self.a_recovery)
            view = render(e, digest(self.base(e)))
            expected_s = statement(self.f, e, self.base(e), view, s['decision'], issued_at(self.f, rec['item']), self.version)
            if e != expected_e or s != expected_s or rec['canonical_statement'] != canonical(s).decode() or rec['statement_sha256'] != digest(s) or rec['owner_view'] != view.decode():
                return {'admitted': False, 'reason': 'IDENTITY_OR_BASE_MISMATCH'}
            if s['acceptance_id'] in self.consumed:
                return {'admitted': False, 'reason': 'CONSUMED_ACCEPTANCE_ID'}
            role = 'RECOVERY' if rec['item'] == 'P6' else 'PRIMARY'
            if not self.authorized(c, role):
                return {'admitted': False, 'reason': 'CURRENT_ROLE_DENIED'}
            pre = {'version': self.version, 'members': copy.deepcopy(self.members)}
            seq = len(self.entries) + 1
            self.consumed.add(s['acceptance_id'])
            self.entries.append({'sequence': seq, 'kind': 'DECISION', 'record': copy.deepcopy(rec), 'trust_before': pre})
            if s['decision'] == 'ACCEPT':
                self.effects.extend(copy.deepcopy(e['effects']))
                if rec['item'] in ('P5', 'P6'):
                    self.members = self.target(rec['item'])
                    self.version = V2R if rec['item'] == 'P6' else V2
            return {'admitted': True, 'sequence': seq, 'version_after': self.version}
        except (KeyError, TypeError, ValueError, IntegrityError):
            return {'admitted': False, 'reason': 'MALFORMED_RECORD'}

    def historical(self, seq, node):
        row = self.entries[seq - 1]
        r = row['record']
        return verify(r['statement'], r['proof'], r['credential'], node) and member('RECOVERY' if r['item'] == 'P6' else 'PRIMARY', r['credential']) in row['trust_before']['members'] and r['statement']['signer_set_version'] == row['trust_before']['version']

    def compromise(self, affected, boundary, node):
        rows = []
        for entry in self.entries[1:]:
            valid = self.historical(entry['sequence'], node)
            review = valid and entry['sequence'] > boundary and entry['record']['credential']['public_id'] == affected
            rows.append({'sequence': entry['sequence'], 'historically_valid': valid,
                         'classification': 'REVIEW_REQUIRED' if review else 'HISTORICAL_UNCHANGED',
                         'resolving_owner': 'GOVERNING_OWNER' if review else None})
        return {'declaration': 'DECLARATION_TRUSTED_SYNTHETIC_INPUT', 'boundary': boundary, 'affected_public_id': affected, 'rows': rows}


def mutate_proof(proof):
    p = copy.deepcopy(proof)
    if p['kind'] == 'SSH_ED25519':
        lines = p['sshsig'].strip().splitlines()
        raw = bytearray(base64.b64decode(''.join(lines[1:-1]), validate=True))
        raw[0] ^= 1
        payload = base64.b64encode(raw).decode()
        p['sshsig'] = '-----BEGIN SSH SIGNATURE-----\n' + '\n'.join(payload[i:i+70] for i in range(0,len(payload),70)) + '\n-----END SSH SIGNATURE-----\n'
    else:
        raw = bytearray(base64.urlsafe_b64decode(p['signature_der'] + '=' * (-len(p['signature_der']) % 4)))
        raw[0] ^= 1
        p['signature_der'] = base64.urlsafe_b64encode(raw).decode().rstrip('=')
    return p


def controls_1_10(f, arm, p0, ledger, node):
    keys = f['security_controls'][:10]
    observations = {}
    if not p0 or p0['statement']['decision'] != 'ACCEPT' or not verify(p0['statement'], p0['proof'], p0['credential'], node):
        return {k:'FAIL' for k in keys}, {k:{'reason':'missing required valid ACCEPT baseline'} for k in keys}
    result = ledger.admit(p0, node)
    observations[keys[0]] = {'verify_valid': True, 'admission': result}
    outcomes = [result['admitted']]
    for index in range(1,10):
        s, proof = copy.deepcopy(p0['statement']), copy.deepcopy(p0['proof'])
        if index == 1:
            proof = mutate_proof(proof)
        elif index == 2:
            e = copy.deepcopy(p0['envelope']);e['effects'][0]['text'] += ' [MUTATED]';s['envelope_digest'] = digest(e)
        elif index == 3:
            view = p0['owner_view'].encode();s['shown_digest'] = sha(b'X' + view[1:])
        elif index == 4:
            s['decision'] = 'REJECT'
        elif index == 5:
            s['project_id'] = f['wrong_project_id']
        elif index == 6:
            s['acceptance_id'] = 'R0-P01-' + arm + '-SEC-ACCEPTANCE_ID_REPLAY_REJECTS'
        elif index == 7:
            deps = copy.deepcopy(f['semantic_base']['effects']);next(d for d in deps if d['effect_id']=='BASE-A')['lineage_head']='BASE-A-1'
            s['semantic_base_digest'] = digest(semantic_base(f, deps))
        elif index == 9:
            s['signer_set_version'] = 'SIGNERS-P01-V999-SYNTHETIC'
        valid = verify(s, proof, p0['credential'], node)
        passed = valid if index == 8 else not valid
        obs = {'verify_valid': valid, 'presented_statement': s, 'presented_proof': proof}
        if index == 6:
            replay = ledger.admit(p0, node);obs['second_admission'] = replay
            passed = passed and not replay['admitted'] and replay['reason'] == 'CONSUMED_ACCEPTANCE_ID'
        if index == 8:
            obs['separate_metadata'] = {'repository_note':'UNRELATED-P01-SYNTHETIC-LANDING'}
        observations[keys[index]] = obs
        outcomes.append(passed)
    return {k:'PASS' if ok else 'FAIL' for k,ok in zip(keys,outcomes)}, observations


def transition_controls(f, arm, make_ledger, p0, p5, p6, s01, node, negative_record=None, generate_negative=True):
    out, evidence = {}, {}
    rotation, recovery, compromise = (make_ledger(x) for x in ('ROTATION','RECOVERY','COMPROMISE'))
    for ledger in (rotation,recovery,compromise):
        if p0:
            ledger.admit(p0, node)
    rotkey,reckey,compkey = f['security_controls'][10:]
    candidate = rotation.a_recovery if arm == 'A' else rotation.a_primary
    before = (rotation.version, copy.deepcopy(rotation.members), len(rotation.entries))
    deny = not rotation.authorized(candidate, 'PRIMARY')
    untouched = before == (rotation.version, rotation.members, len(rotation.entries))
    r5 = rotation.admit(p5,node) if p5 else {'admitted':False}
    ok5 = len(rotation.entries)==3 and r5['admitted'] and p5['statement']['decision']=='ACCEPT' and rotation.version==V2 and deny and untouched
    out[rotkey] = 'PASS' if ok5 else 'FAIL'
    evidence[rotkey] = {'candidate_role_denied':deny,'predicate_left_state_unchanged':untouched,'candidate_public_id':candidate['public_id'],'admission':r5,'record':p5,'ledger':rotation.entries}
    negative = copy.deepcopy(negative_record)
    if p6 and negative is None and generate_negative:
        test = node.call('synthetic_ssh', label='SYNTHETIC-NON-OWNER-UNREGISTERED-RECOVERY', statement=p6['statement'])
        negative = copy.deepcopy(p6);negative['proof']=test['proof'];negative['credential']=test['credential']
    if p6 and negative is not None:
        nv = verify(negative['statement'],negative['proof'],negative['credential'],node)
        pre = (recovery.version, len(recovery.entries), set(recovery.consumed))
        na = recovery.admit(negative,node)
        unchanged = pre == (recovery.version,len(recovery.entries),recovery.consumed)
    else:
        nv,na,unchanged = False, {'admitted':False,'reason':'unexecuted'}, True
    r6 = recovery.admit(p6,node) if p6 else {'admitted':False}
    hist = len(recovery.entries)>=2 and recovery.historical(2,node)
    ok6 = r6['admitted'] and len(recovery.entries)==3 and p6['statement']['decision']=='ACCEPT' and recovery.version==V2R and nv and not na['admitted'] and na['reason']=='CURRENT_ROLE_DENIED' and unchanged and hist
    out[reckey] = 'PASS' if ok6 else 'FAIL'
    evidence[reckey] = {'negative_synthetic_non_owner_record':negative,'negative_verify_valid':nv,'negative_admission':na,'negative_left_state_unchanged':unchanged,'historical_p0_valid':hist,'admission':r6,'record':p6,'ledger':recovery.entries}
    r1 = compromise.admit(s01,node) if s01 else {'admitted':False}
    comparison = compromise.compromise(p0['credential']['public_id'],2,node) if p0 else {'rows':[]}
    expected = [(2,'HISTORICAL_UNCHANGED',None),(3,'REVIEW_REQUIRED','GOVERNING_OWNER')]
    ok13 = r1['admitted'] and [(r['sequence'],r['classification'],r['resolving_owner']) for r in comparison['rows']]==expected and all(r['historically_valid'] for r in comparison['rows'])
    out[compkey] = 'PASS' if ok13 else 'FAIL'
    evidence[compkey] = {'comparison':comparison,'ledger':compromise.entries}
    return out,evidence


SECRET_PATTERN = re.compile(r'-----BEGIN (?:OPENSSH |RSA |EC |ENCRYPTED )?PRIVATE KEY-----|(?:passphrase|password|recovery_secret|private_key)\s*[:=]|owner_(?:primary|recovery)_ed25519(?!\.pub)', re.I)


def redact(value):
    exposed = False
    def walk(v):
        nonlocal exposed
        if isinstance(v,str) and SECRET_PATTERN.search(v):
            exposed = True;return '[REDACTED SECRET-BOUNDARY VIOLATION]'
        if isinstance(v,dict):
            out={}
            for k,x in v.items():
                if re.search(r'passphrase|private_key|password|recovery_secret',k,re.I):
                    exposed=True;out[k]='[REDACTED SECRET-BOUNDARY VIOLATION]'
                else:
                    out[k]=walk(x)
            return out
        if isinstance(v,list):return [walk(x) for x in v]
        return v
    return walk(value),exposed


def trial_row(f, item):
    rc = strict_json((HERE/'result_contract.json').read_bytes())
    r={k:None for k in rc['trial_fields']}
    r.update(trial_id=item,success=False,friction_note='',manual_metadata_edits=None,
             infrastructure_receipts=[],record=None,admission=None,execution_status='UNEXECUTED')
    return r


def empty_arm(f, arm):
    return {'arm_id':f['arm_ids'][arm], 'realizability':None, 'setup_receipt':{'status':'INCOMPLETE','events':[]},
            'security_controls':{k:'NOT_APPLICABLE' if arm=='C' else 'FAIL' for k in f['security_controls']},
            'control_evidence':{k:{'reason':'unexecuted'} for k in f['security_controls']},
            'small_trials':[trial_row(f,x) for x in (['S01'] if arm=='C' else ['S01','S02','S03'])],
            'large_trial':trial_row(f,'L01'), 'secret_exposure':False,'manual_metadata_edits':None,
            'selection_eligible':False,'security_records':{}}


def provenance():
    files={}
    for name in CONTRACT_FILES+IMPLEMENTATION_FILES:
        data=(HERE/name).read_bytes()
        relative=(HERE/name).relative_to(ROOT).as_posix()
        try:blob_hash=sha(git('cat-file','blob','HEAD:'+relative))
        except IntegrityError:blob_hash=None  # permitted only for uncommitted pretrial implementation
        files[name]={'sha256':sha(data),'bytes':len(data),'byte_basis':'EXACT_WORKTREE_BYTES',
                     'git_blob_sha256':blob_hash,'git_blob_byte_basis':'GIT_BLOB_BYTES'}
    openssh=subprocess.run(['ssh','-V'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=no_agent_env())
    if openssh.returncode:raise IntegrityError('OpenSSH runtime unavailable')
    return {'repository_head':git('rev-parse','HEAD').decode().strip(), 'artifacts':files,
            'runtime_versions':{'python':sys.version.split()[0], 'node':subprocess.check_output(['node','--version'],text=True,env=no_agent_env()).strip(),
                                'openssh':(openssh.stdout+openssh.stderr).strip()},
            'implementation_freeze_required':True}


def preflight():
    c=contracts();f=c['fixture.json']
    hashes=golden(f,c['clarification_vectors_v02.json'])
    inv=inventory()
    node=NodeBridge()
    try:
        node.call('golden')
    finally:node.close()
    return {'pretrial_only':True,'golden':hashes,'inventory':inv}


def production_attempt_marker():
    return Path(os.environ['LOCALAPPDATA'])/'ADS-R0-P01'/'attempt-001.started.json'


def claim_attempt_001(marker, reviewed_head, evidence_directory):
    """Create once; even an incomplete claim consumes the attempt. Never clear it."""
    claim={'attempt_id':'001','protocol':'R0-P01-V01','contract_revision':'R0-P01-CONTRACT-V02',
           'reviewed_repository_head':reviewed_head,'evidence_directory':str(Path(evidence_directory).resolve()),
           'claimed_at_utc':utc()}
    marker=Path(marker)
    try:
        marker.parent.mkdir(parents=True,exist_ok=True)
        # Exclusive creation is the cross-process gate; no check-then-write race.
        # Flush the public claim before any snapshot or owner-sensitive action.
        with marker.open('xb') as stream:
            stream.write(canonical(claim)+b'\n')
            stream.flush()
            os.fsync(stream.fileno())
    except OSError:
        raise IntegrityError('Attempt 001 already claimed or durable claim unavailable') from None
    return claim


class Attempt:
    def __init__(self, output, reviewed_head, f):
        output=Path(output).resolve()
        if output==ROOT or ROOT in output.parents or output.exists():
            raise IntegrityError('evidence directory must be new and outside repository')
        if git('rev-parse','HEAD').decode().strip()!=reviewed_head or git('status','--porcelain=v1','--untracked-files=all').strip():
            raise IntegrityError('clean reviewed implementation freeze required')
        self.initial_provenance=provenance()
        if any(self.initial_provenance['artifacts'][n]['git_blob_sha256'] is None for n in IMPLEMENTATION_FILES):
            raise IntegrityError('implementation must be in the reviewed freeze')
        self.last_head=self.initial_provenance['repository_head']
        self.output=output;self.started=False
        self.raw={'schema_version':2,'protocol':'R0-P01-V01','contract_revision':'R0-P01-CONTRACT-V02','attempt_id':'001',
                  'provenance':copy.deepcopy(self.initial_provenance),'integrity':{'secret_exposure':False,'post_observation_tuning':False,'attempt_integrity_failure':False},
                  'arms':{a:empty_arm(f,a) for a in 'ABC'},'attempt_events':[]}

    def start(self):
        if self.started:raise IntegrityError('attempt already started')
        self.output.mkdir(parents=True,exist_ok=False)
        claim=claim_attempt_001(production_attempt_marker(),self.initial_provenance['repository_head'],self.output)
        self.started=True
        self.raw['attempt_events'].append({'event':'ATTEMPT_001_STARTED_BEFORE_OWNER_SENSITIVE_SETUP','at_utc':claim['claimed_at_utc']})
        self.preserve()

    def preserve(self):
        if not self.started:return
        try:
            current=provenance()
            unchanged=current['artifacts']==self.initial_provenance['artifacts'] and current['runtime_versions']==self.initial_provenance['runtime_versions']
            if current['repository_head']!=self.last_head:
                self.raw['attempt_events'].append({'event':'REPOSITORY_HEAD_OBSERVATION','repository_head':current['repository_head'],'artifacts_unchanged':unchanged,'at_utc':utc()})
                self.last_head=current['repository_head']
        except Exception:unchanged=False
        if not unchanged:
            self.raw['integrity']['post_observation_tuning']=True
            self.raw['integrity']['attempt_integrity_failure']=True
        safe,exposed=redact(self.raw)
        if exposed:
            safe['integrity']['secret_exposure']=True
            self.raw=safe
        # Append-only snapshots, no overwriting raw observations.
        index=len(list(self.output.glob('raw-*.json')))
        with (self.output/('raw-%04d.json'%index)).open('x',encoding='utf-8',newline='\n') as stream:
            json.dump(self.raw,stream,ensure_ascii=False,allow_nan=False,sort_keys=True,indent=2);stream.write('\n')


class OwnerSSH:
    def __init__(self):
        self.directory=Path(os.environ['LOCALAPPDATA'])/'ADS-R0-P01'/'arm-a'
        self.paths={role:self.directory/('owner_'+role+'_ed25519') for role in ('primary','recovery')}
        self.credentials={}

    def ensure_new(self):
        if any(p.exists() or p.with_suffix('.pub').exists() for p in self.paths.values()):
            raise IntegrityError('existing probe credential prevents fresh Attempt 001')

    def setup(self):
        self.directory.mkdir(parents=True,exist_ok=True)
        for role,p in self.paths.items():
            print('Native OpenSSH prompt: choose a non-empty probe passphrase. Never send it to chat.')
            result=subprocess.run(['ssh-keygen','-t','ed25519','-a','100','-f',str(p),'-C','R0-P01-owner-'+role],env=no_agent_env())
            if result.returncode:raise SetupInterrupted('native probe setup interrupted')
            self.check_encrypted_header(p)
            public=ssh_public(p.with_suffix('.pub').read_text(encoding='utf-8'))
            self.credentials[role]=public
        return self.credentials

    @staticmethod
    def check_encrypted_header(p):
        # Inspect only a partial armored public cipher/KDF header. OpenSSH wraps
        # at 70 columns, so decode only complete base64 groups (not the full key).
        with p.open('rb') as stream:
            if stream.readline().strip()!=b'-----BEGIN OPENSSH PRIVATE KEY-----':raise IntegrityError('key container')
            line=stream.readline().strip()
        prefix=base64.b64decode(line[:len(line)//4*4],validate=True)
        if not prefix.startswith(b'openssh-key-v1\0') or len(prefix)<23:raise IntegrityError('key container')
        n=struct.unpack('>I',prefix[15:19])[0]
        if n==0 or 19+n>len(prefix) or prefix[19:19+n]==b'none':raise IntegrityError('non-empty passphrase required')

    def sign(self,s,role):
        p=self.paths[role]
        self.check_encrypted_header(p)
        # Windows may expose a default agent even without SSH_AUTH_SOCK. Refuse
        # if either probe identity appears there; never load an identity ourselves.
        agent=subprocess.run(['ssh-add','-L'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if agent.returncode==0:
            identities=[]
            for line in agent.stdout.splitlines():
                try:identities.append(ssh_public(line)['public_id'])
                except IntegrityError:pass
            if any(c['public_id'] in identities for c in self.credentials.values()):raise IntegrityError('probe agent caching forbidden')
        if ssh_public(p.with_suffix('.pub').read_text(encoding='utf-8'))!=self.credentials[role]:raise IntegrityError('probe public credential changed')
        # A unique canonical statement file is probe-local, never in repository.
        name=self.directory/('statement-'+s['acceptance_id']+'.json')
        with name.open('xb') as stream:stream.write(canonical(s))
        print('Use the native OpenSSH prompt; the harness does not receive your passphrase.')
        result=subprocess.run(['ssh-keygen','-Y','sign','-f',str(p),'-n','ads-r0-p01-acceptance',str(name)],env=no_agent_env())
        if result.returncode:return None
        return {'kind':'SSH_ED25519','sshsig':Path(str(name)+'.sig').read_text(encoding='ascii')}


def prompt_public(label, integer=False):
    value=input(label+' (non-secret; blank if unavailable): ')
    if not value:return None
    if SECRET_PATTERN.search(value):raise SecretBoundaryError('secret-boundary violation')
    if integer:
        try:return int(value)
        except ValueError:return None
    return value


def owner_measurements(item=None):
    measurements={'interaction_count':prompt_public('User-visible interactions after display',True),
            'device_switches':prompt_public('Physical device switches',True),
            'manual_metadata_edits':prompt_public('Manual metadata edits',True),
            'friction_rating_1_to_5':prompt_public('Friction rating 1 through 5',True),
            'friction_note':prompt_public('Short friction note') or ''}
    measurements['infrastructure_receipts']=infrastructure_receipts(item)
    return measurements


def infrastructure_receipts(item):
    if item not in ('S01','S02','S03') or input('Task owner: record an infrastructure-only interruption receipt? YES or blank: ')!='YES':return []
    return [{'trial_id':item,'start_utc':prompt_public('Infrastructure interval start UTC'),
             'end_utc':prompt_public('Infrastructure interval end UTC'),'affected_component':prompt_public('Affected component'),
             'observable_event_or_error':prompt_public('Observable infrastructure-only event/error'),
             'classification':'EXTERNAL_INFRASTRUCTURE_ONLY','task_owner_receipt':True}]


def terminal_proof(f,arm,item,ledger,credential,ssh,role,node,on_observation=None):
    e=envelope(f,arm,item,ledger.a_primary,ledger.a_recovery);b=ledger.base(e);view=render(e,digest(b))
    sys.stdout.buffer.write(view);sys.stdout.buffer.flush()
    review_start=time.monotonic();displayed_at=utc()
    decision=input('Decision ACCEPT / AMEND / REJECT: ').strip()
    captured=time.monotonic();captured_at=utc()
    if decision not in DECISIONS:raise IntegrityError('invalid owner decision; no replacement proof permitted')
    s=statement(f,e,b,view,decision,issued_at(f,item),ledger.version)
    partial={'semantic_review_seconds':captured-review_start,'mechanical_seconds':None,
             'displayed_at_utc':displayed_at,'decision_at_utc':captured_at}
    if on_observation:on_observation(record(f,arm,item,ledger,decision,None,credential),False,partial)
    print(canonical(s).decode(),flush=True)
    proof=ssh.sign(s,role)
    valid=verify(s,proof,credential,node)
    end=time.monotonic();verified_at=utc()
    r=record(f,arm,item,ledger,decision,proof,credential)
    r['verifier_result']='VALID' if valid else 'INVALID'
    measured={**partial,'mechanical_seconds':end-captured,'verified_at_utc':verified_at}
    if on_observation:on_observation(r,valid,measured)
    measurements={**measured,**owner_measurements(item)}
    return r,valid,measurements


def browser_proof(f,item,ledger,node,on_observation=None):
    e=envelope(f,'B',item,ledger.a_primary,ledger.a_recovery);b=ledger.base(e);view=render(e,digest(b))
    template=statement(f,e,b,view,'ACCEPT',issued_at(f,item),ledger.version);template.pop('decision')
    node.call('job',template=template,owner_view=view.decode())
    print('Complete the displayed event in http://localhost:8765. No replacement event is permitted.')
    last_snapshot=None
    while True:
        completed=node.call('collect')
        if completed:break
        snap=node.call('snapshot')
        job=snap.get('job')
        if job and job.get('statement') and job!=last_snapshot:
            r=record(f,'B',item,ledger,job['statement']['decision'],job.get('proof'),snap['credential'])
            if r['statement']!=job['statement']:raise IntegrityError('browser statement construction mismatch')
            valid=verify(r['statement'],r['proof'],r['credential'],node)
            r['verifier_result']='VALID' if valid else 'INVALID'
            if on_observation:on_observation(r,valid,job.get('capture',{}))
            last_snapshot=copy.deepcopy(job)
        time.sleep(.2)
    s=completed['statement'];credential=node.call('snapshot')['credential']
    r=record(f,'B',item,ledger,s['decision'],completed['proof'],credential)
    r['ceremony_receipt']=[e for e in node.call('snapshot')['events'] if e.get('type')=='assertion' and e.get('acceptance_id')==s['acceptance_id']]
    if completed.get('rejected_public_response'):
        r['rejected_public_ceremony_response']=completed['rejected_public_response']
        r['ceremony_rejected']=True
    if r['statement']!=s:raise IntegrityError('browser statement construction mismatch')
    valid=verify(s,r['proof'],credential,node)
    r['verifier_result']='VALID' if valid else 'INVALID'
    if valid is not completed['verification']['valid']:raise IntegrityError('browser verifier conflict')
    if on_observation:on_observation(r,valid,completed['measurements'])
    failure=completed['measurements'].get('failure')
    if failure=='NotSupportedError':raise CapabilityUnavailable('WebAuthn assertion capability unavailable')
    if failure not in (None,'NotAllowedError'):raise IntegrityError('local WebAuthn client/state defect')
    completed['measurements']['infrastructure_receipts']=infrastructure_receipts(item)
    return r,valid,completed['measurements']


def run_arm(f,arm,primary,recovery,a_primary,a_recovery,ssh,node,attempt):
    data=attempt.raw['arms'][arm]
    make=lambda scenario:Ledger(f,arm,primary,recovery,a_primary,a_recovery,scenario)
    security,burden=make('BASE_SECURITY'),make('BURDEN')
    def event(item,ledger):
        def observe(rec,valid,measurements):
            if measurements.get('secret_exposure'):
                data['secret_exposure']=True;attempt.raw['integrity']['secret_exposure']=True
            if item in ('P0','P5','P6'):
                data['security_records'][item]=rec
                data.setdefault('security_measurements',{}).setdefault(item,{}).update(measurements)
            else:
                row=next((r for r in data['small_trials'] if r['trial_id']==item),data['large_trial'])
                row.update(measurements,record=rec,decision=rec['statement']['decision'],success=False,execution_status='IN_PROGRESS')
                # Partial observation does not advance the synthetic ledger.
                row['admission']=None
            attempt.preserve()
        if arm=='B' and item!='P6':return browser_proof(f,item,ledger,node,observe)
        role='recovery' if item=='P6' else 'primary'
        return terminal_proof(f,arm,item,ledger,recovery if item=='P6' else primary,ssh,role,node,observe)
    p0,_,m0=event('P0',security)
    data['security_records']['P0']=p0;data['security_measurements']={'P0':m0}
    first,obs=controls_1_10(f,arm,p0,security,node);data['security_controls'].update(first);data['control_evidence'].update(obs);attempt.preserve()
    records={}
    for item in ('S01','S02','S03','L01'):
        rec,valid,measurements=event(item,burden)
        row=next((r for r in data['small_trials'] if r['trial_id']==item),data['large_trial'])
        row.update(measurements,decision=rec['statement']['decision'],success=valid,execution_status='COMPLETE',record=rec,admission=burden.admit(rec,node))
        records[item]=rec;attempt.preserve()
    transitions={}
    for item,scenario in (('P5','ROTATION'),('P6','RECOVERY')):
        ledger=make(scenario);ledger.admit(p0,node)
        rec,_,measurements=event(item,ledger)
        transitions[item]=rec;data['security_records'][item]=rec;data['security_measurements'][item]=measurements;attempt.preserve()
    last,obs=transition_controls(f,arm,make,p0,transitions['P5'],transitions['P6'],records['S01'],node)
    data['security_controls'].update(last);data['control_evidence'].update(obs)
    edits=[data['setup_receipt'].get('manual_metadata_edits')]+[x.get('manual_metadata_edits') for x in data['small_trials']+[data['large_trial']]]+[m.get('manual_metadata_edits') for m in data['security_measurements'].values()]
    data['manual_metadata_edits']=sum(edits) if all(type(x) is int and x>=0 for x in edits) else None
    attempt.preserve()


def owner_run(output,reviewed_head):
    preflight();f=contracts()['fixture.json'];ssh=OwnerSSH();ssh.ensure_new()
    public_output=Path(output).resolve();private_directory=ssh.directory.resolve()
    if public_output==private_directory or public_output in private_directory.parents or private_directory in public_output.parents:
        raise IntegrityError('public evidence and private credential directories must be disjoint')
    attempt=Attempt(output,reviewed_head,f)
    node=NodeBridge()
    serving=None
    try:
        attempt.start()  # persisted BEFORE the first real key creation/native prompt
        credentials=ssh.setup();ap,ar=credentials['primary'],credentials['recovery']
        print('Primary public identifier:',ap['public_id']);print('Recovery public identifier:',ar['public_id'])
        if input('Confirm these initial probe trust identifiers (type CONFIRM): ')!='CONFIRM':raise IntegrityError('initial trust confirmation missing')
        setup_edits=prompt_public('Setup manual metadata edits',True)
        a=attempt.raw['arms']['A'];a['realizability']='REALIZABLE';a['setup_receipt']={'status':'COMPLETE','events':[{'type':'SSH_PUBLIC_SETUP','at_utc':utc(),'owner_confirmed':True}],
            'members':sorted_members([member('PRIMARY',ap),member('RECOVERY',ar)]),'credentials':[ap,ar],'owner_confirmed':True,'tofu':'EXPLICIT_SYNTHETIC_TOFU','manual_metadata_edits':setup_edits}
        attempt.preserve();run_arm(f,'A',ap,ar,ap,ar,ssh,node,attempt)
        serving=NodeBridge(serving=True);serving.call('initialize',attempt_id='001',arm='B')
        print('Open http://localhost:8765 in the owner browser and explicitly register the probe credential.')
        b=attempt.raw['arms']['B']
        while True:
            snap=serving.call('snapshot')
            if snap['credential'] or snap['capability'] or snap['interruptions']>=2 or any(e.get('status') in ('INVALID','INCOMPLETE') for e in snap['events']):break
            # Both first and second interruptions are preserved during setup.
            if snap['events']!=b['setup_receipt']['events']:
                b['setup_receipt'].update(status='SETUP_INTERRUPTED',events=snap['events']);attempt.preserve()
            time.sleep(.2)
        b['setup_receipt']['events']=snap['events']
        browser_versions=[e.get('browser_user_agent') for e in snap['events'] if isinstance(e.get('browser_user_agent'),str) and e['browser_user_agent']]
        if browser_versions:
            b['setup_receipt']['browser_runtime_user_agent']=browser_versions[-1]
            attempt.raw['provenance']['runtime_versions']['browser']=browser_versions[-1]
        if snap['credential']:
            bp=snap['credential'];print('WebAuthn public identifier:',bp['public_id'])
            if input('Confirm this initial probe trust identifier (type CONFIRM): ')!='CONFIRM':raise IntegrityError('initial trust confirmation missing')
            b['realizability']='REALIZABLE';b['setup_receipt'].update(status='COMPLETE',owner_confirmed=True,tofu='EXPLICIT_SYNTHETIC_TOFU',credentials=[bp,ar],members=sorted_members([member('PRIMARY',bp),member('RECOVERY',ar)]),manual_metadata_edits=prompt_public('B setup manual metadata edits',True))
            attempt.preserve()
            try:run_arm(f,'B',bp,ar,ap,ar,ssh,serving,attempt)
            except CapabilityUnavailable:
                b['realizability']='NOT_REALIZABLE';b['setup_receipt'].update(status='NOT_REALIZABLE',capability={'reason':'ASSERTION_ES256_UV_NOT_SUPPORTED'})
                for row in b['small_trials']+[b['large_trial']]:
                    if row.get('execution_status')=='IN_PROGRESS':row.update(execution_status='INTERRUPTED',success=False)
                attempt.preserve()
        elif snap['capability']:
            b['realizability']='NOT_REALIZABLE';b['setup_receipt'].update(status='NOT_REALIZABLE',capability=snap['capability']);attempt.preserve()
        elif any(e.get('status')=='INVALID' for e in snap['events']):raise IntegrityError('WebAuthn setup verification defect')
        else:
            b['setup_receipt']['status']='INCOMPLETE' if any(e.get('status')=='INCOMPLETE' for e in snap['events']) else 'SETUP_INTERRUPTED';attempt.preserve()
        c=attempt.raw['arms']['C'];c['realizability']='REALIZABLE';c['setup_receipt']={'status':'COMPLETE','events':[],'manual_metadata_edits':0}
        for item in ('S01','L01'):
            e=envelope(f,'C',item);base=semantic_base(f,envelope=e);view=render(e,digest(base))
            sys.stdout.buffer.write(view);sys.stdout.buffer.flush();start=time.monotonic();displayed_at=utc();decision=input('Comparator decision ACCEPT / AMEND / REJECT: ').strip();captured=time.monotonic();captured_at=utc()
            s=statement(f,e,base,view,decision,issued_at(f,item),V1);print(canonical(s).decode());expected='R0-P01 PLATFORM ATTEST '+e['acceptance_id']+' '+digest(s);print(expected,flush=True)
            row=c['small_trials'][0] if item=='S01' else c['large_trial']
            row.update(decision=decision,semantic_review_seconds=captured-start,execution_status='IN_PROGRESS',displayed_at_utc=displayed_at,decision_at_utc=captured_at,
                       comparator={'expected_line':expected,'observed_line':None,'line_equal':False,'user_role_observed':False,'task_owner_receipt':True,'platform_reference':None,'independently_repository_verifiable':False,'statement':s,'envelope':e,'owner_view':view.decode()})
            attempt.preserve()
            observed=prompt_public('Task-owner observation of the exact user-authored ChatGPT line')
            reference=prompt_public('Task-owner receipt: ChatGPT message/provenance reference')
            user_role=input('Task-owner receipt: observed user-authored role? type YES: ')=='YES'
            match=expected==observed and bool(reference) and user_role
            end=time.monotonic();row=c['small_trials'][0] if item=='S01' else c['large_trial']
            row.update(decision=decision,semantic_review_seconds=captured-start,mechanical_seconds=end-captured,success=bool(match),execution_status='COMPLETE',displayed_at_utc=displayed_at,decision_at_utc=captured_at,verified_at_utc=utc(),
                       comparator={'expected_line':expected,'observed_line':observed,'line_equal':expected==observed,'user_role_observed':user_role,'task_owner_receipt':True,'platform_reference':reference,'independently_repository_verifiable':False,'statement':s,'envelope':e,'owner_view':view.decode()})
            row.update(success=False,execution_status='IN_PROGRESS');attempt.preserve()
            row.update(owner_measurements(item));row.update(success=bool(match),execution_status='COMPLETE');attempt.preserve()
        edits=[r['manual_metadata_edits'] for r in c['small_trials']+[c['large_trial']]]
        c['manual_metadata_edits']=sum(edits) if all(type(x) is int and x>=0 for x in edits) else None
        attempt.raw['attempt_events'].append({'event':'OWNER_RUN_ENDED','at_utc':utc()});attempt.preserve()
    except (Exception,KeyboardInterrupt) as error:
        # Preserve first; no repair, replacement proof, or retry-to-green.
        if attempt.started:
            interrupted=isinstance(error,(SetupInterrupted,KeyboardInterrupt))
            if not interrupted:attempt.raw['integrity']['attempt_integrity_failure']=True
            if isinstance(error,SecretBoundaryError):attempt.raw['integrity']['secret_exposure']=True
            if interrupted:
                for data in attempt.raw['arms'].values():
                    if data['realizability'] is None:data['setup_receipt']['status']='SETUP_INTERRUPTED'
            for data in attempt.raw['arms'].values():
                for row in data['small_trials']+[data['large_trial']]:
                    if row.get('execution_status')=='IN_PROGRESS':row.update(execution_status='INTERRUPTED',success=False)
            attempt.raw['attempt_events'].append({'event':'OWNER_RUN_INTERRUPTED' if interrupted else 'OWNER_RUN_DEFECT','at_utc':utc()})
            attempt.preserve()
        raise IntegrityError('owner run stopped; preserved attempt requires independent review') from None
    finally:
        node.close()
        if serving:serving.close()


def synthetic_result_fixture():
    """In-memory test double ONLY. Never written as owner evidence or CLI output.

    Covers the same 7 proof events per arm using non-owner Ed25519/ES256 keys.
    Artificial measurements test scoring, not burden or owner realizability.
    """
    f=contracts()['fixture.json'];node=NodeBridge()
    raw={'schema_version':2,'protocol':'R0-P01-V01','contract_revision':'R0-P01-CONTRACT-V02','attempt_id':'001',
         'synthetic_pretrial_only':True,'provenance':provenance(),
         'integrity':{'secret_exposure':False,'post_observation_tuning':False,'attempt_integrity_failure':False},
         'arms':{a:empty_arm(f,a) for a in 'ABC'}}
    sample=contracts()['clarification_vectors_v02.json']['statement']
    try:
        def synthetic(label,s,kind='SSH_ED25519'):
            return node.call('synthetic_webauthn' if kind=='WEBAUTHN_ES256' else 'synthetic_ssh',label='SYNTHETIC-NON-OWNER-'+label,statement=s)
        ap=synthetic('QUALIFICATION-A-PRIMARY',sample)['credential'];ar=synthetic('QUALIFICATION-A-RECOVERY',sample)['credential']
        bp=synthetic('QUALIFICATION-B-PRIMARY',sample,'WEBAUTHN_ES256')['credential']
        for arm,primary in (('A',ap),('B',bp)):
            make=lambda scenario:Ledger(f,arm,primary,ar,ap,ar,scenario)
            data=raw['arms'][arm];data['realizability']='REALIZABLE'
            data['setup_receipt']={'status':'COMPLETE','events':[{'type':'SYNTHETIC_NON_OWNER_SETUP'}],
                'owner_confirmed':True,'tofu':'EXPLICIT_SYNTHETIC_TOFU','credentials':[primary,ar],
                'members':sorted_members([member('PRIMARY',primary),member('RECOVERY',ar)]),'manual_metadata_edits':0}
            measurements={'semantic_review_seconds':1.0,'mechanical_seconds':20.0,'interaction_count':2,
                          'device_switches':0,'manual_metadata_edits':0,'friction_rating_1_to_5':1,'friction_note':'SYNTHETIC NON-OWNER TEST DOUBLE'}
            def signed(item,ledger,decision='ACCEPT'):
                cred=ar if item=='P6' else primary
                label='QUALIFICATION-A-RECOVERY' if item=='P6' else 'QUALIFICATION-'+arm+'-PRIMARY'
                rec=record(f,arm,item,ledger,decision,None,cred)
                rec['proof']=synthetic(label,rec['statement'],cred['kind'])['proof']
                rec['verifier_result']='VALID' if verify(rec['statement'],rec['proof'],cred,node) else 'INVALID'
                return rec
            p0=signed('P0',make('BASE_SECURITY'));data['security_records']['P0']=p0
            first,obs=controls_1_10(f,arm,p0,make('BASE_SECURITY'),node)
            data['security_controls'].update(first);data['control_evidence'].update(obs)
            burden=make('BURDEN');s01=None
            for row in data['small_trials']+[data['large_trial']]:
                # Both non-ACCEPT owner decisions are cryptographically successful.
                decision='AMEND' if row['trial_id']=='S02' else 'REJECT' if row['trial_id']=='S03' else 'ACCEPT'
                rec=signed(row['trial_id'],burden,decision)
                row.update(measurements,decision=decision,record=rec,success=verify(rec['statement'],rec['proof'],primary,node),execution_status='COMPLETE',admission=burden.admit(rec,node))
                if row['trial_id']=='S01':s01=rec
            records={}
            for item,scenario in (('P5','ROTATION'),('P6','RECOVERY')):
                ledger=make(scenario);ledger.admit(p0,node);records[item]=signed(item,ledger)
                data['security_records'][item]=records[item]
            last,obs=transition_controls(f,arm,make,p0,records['P5'],records['P6'],s01,node)
            data['security_controls'].update(last);data['control_evidence'].update(obs)
            data['security_measurements']={item:copy.deepcopy(measurements) for item in ('P0','P5','P6')}
            data['manual_metadata_edits']=0
        return raw
    finally:node.close()


def attempt_claim_selftest():
    """Synthetic public claims only; no production namespace or owner setup."""
    with tempfile.TemporaryDirectory(prefix='SYNTHETIC-NON-OWNER-P01-CLAIM-') as directory:
        root=Path(directory)
        marker=root/'synthetic-non-owner-attempt-001.started.json'
        evidence_a,evidence_b=root/'evidence-a',root/'evidence-b'
        evidence_a.mkdir();evidence_b.mkdir()
        first=claim_attempt_001(marker,FROZEN_HEAD,evidence_a)
        original=marker.read_bytes()
        assert strict_json(original)==first and first['attempt_id']=='001'
        assert set(first)=={'attempt_id','protocol','contract_revision','reviewed_repository_head',
                            'evidence_directory','claimed_at_utc'}
        assert not redact(first)[1]
        assert not re.search(rb'PRIVATE KEY|passphrase|password|private_key|recovery_secret',original,re.I)
        for evidence in (evidence_a,evidence_b):
            try:claim_attempt_001(marker,FROZEN_HEAD,evidence)
            except IntegrityError:pass
            else:raise AssertionError('second Attempt 001 claim allowed')
            assert marker.read_bytes()==original
        # A new interpreter has no in-memory started state; no SSH files exist.
        child="""import sys
sys.path.insert(0,sys.argv[1])
import harness as h
try:
    h.claim_attempt_001(sys.argv[2],h.FROZEN_HEAD,sys.argv[3])
except h.IntegrityError:
    print('SECOND_ATTEMPT_001_START_ALLOWED=False')
else:
    raise AssertionError('fresh process allowed second Attempt 001')
"""
        check=subprocess.run([sys.executable,'-B','-c',child,str(HERE),str(marker),str(evidence_b)],
                             env=no_agent_env(),capture_output=True,text=True,check=True)
        assert check.stdout.strip()=='SECOND_ATTEMPT_001_START_ALLOWED=False'
        assert marker.read_bytes()==original and not list(root.rglob('*ed25519*'))
        # A partial claim left by interruption is also permanently fail-closed.
        partial=root/'synthetic-non-owner-partial.started.json';partial.touch(exist_ok=False)
        try:claim_attempt_001(partial,FROZEN_HEAD,evidence_b)
        except IntegrityError:pass
        else:raise AssertionError('partial claim was reused')
        assert partial.read_bytes()==b''
    return {'first_claim_and_persistence':'PASS','second_claim_different_evidence':'PASS',
            'fresh_process_rejection':'PASS','public_non_secret_contents':'PASS','partial_claim_rejection':'PASS',
            'SECOND_ATTEMPT_001_START_ALLOWED':False,'synthetic_non_owner':True}


def selftest():
    # Pretrial tests cannot resolve a production marker or start a real attempt.
    with mock.patch(__name__+'.production_attempt_marker',side_effect=AssertionError('production claim forbidden in selftest')), \
         mock.patch.object(Attempt,'start',side_effect=AssertionError('owner attempt forbidden in selftest')):
        result=_selftest()
        result['production_attempt_claim_guard']='PASS'
        return result


def _selftest():
    result=preflight();c=contracts();f=c['fixture.json']
    result['durable_attempt_claim']=attempt_claim_selftest()
    node=NodeBridge()
    try:
        s=c['clarification_vectors_v02.json']['statement']
        def synth(label,stmt=s):return node.call('synthetic_ssh',label='SYNTHETIC-NON-OWNER-'+label,statement=stmt)
        ap,ar=synth('PRIMARY')['credential'],synth('RECOVERY')['credential']
        make=lambda scenario:Ledger(f,'A',ap,ar,ap,ar,scenario)
        def signed(item,ledger,role='PRIMARY',decision='ACCEPT'):
            cred=ar if role=='RECOVERY' else ap
            r=record(f,'A',item,ledger,decision,None,cred)
            proof=synth(role,r['statement'])['proof'];r['proof']=proof
            assert verify(r['statement'],proof,cred,node)
            r['verifier_result']='VALID'
            return r
        p0=signed('P0',make('BASE_SECURITY'))
        outcomes,obs=controls_1_10(f,'A',p0,make('BASE_SECURITY'),node);assert set(outcomes.values())=={'PASS'}
        s01=signed('S01',make('BURDEN'))
        rot,rec=make('ROTATION'),make('RECOVERY');assert rot.admit(p0,node)['admitted'];assert rec.admit(p0,node)['admitted']
        p5,p6=signed('P5',rot),signed('P6',rec,'RECOVERY')
        last,_=transition_controls(f,'A',make,p0,p5,p6,s01,node);assert set(last.values())=={'PASS'}
        # Every admitted decision consumes once; stale signed statements consume nothing.
        for decision in DECISIONS:
            ledger=make('BURDEN');r=signed('S02',ledger,decision=decision)
            assert ledger.admit(r,node)['admitted'];assert not ledger.admit(r,node)['admitted']
            assert bool(ledger.effects)==(decision=='ACCEPT')
        stale=make('BURDEN');r=signed('S01',stale);stale.dependencies[0]['lineage_head']='BASE-A-1'
        assert not stale.admit(r,node)['admitted'] and not stale.consumed
        recovery_authority=make('BURDEN');r=signed('S01',recovery_authority,'RECOVERY');assert not recovery_authority.admit(r,node)['admitted']
        assert rot.admit(p5,node)['admitted'];assert rot.historical(2,node);assert not rot.admit(s01,node)['admitted']
        bad=copy.deepcopy(p0);bad['owner_view']+='x';assert not make('BASE_SECURITY').admit(bad,node)['admitted']
        for sample in [float('nan'),float('inf'),{'x':'\ud800'}]:
            try:canonical(sample)
            except (ValueError,UnicodeError):pass
            else:raise AssertionError('canonical invalid input')
        assert canonical({'z':1,'a':[True,'é']})==canonical({'a':[True,'é'],'z':1})
        utf8_vector={'\U00010000':'astral','\ue000':'bmp','a':['é','\n','"',True,1]}
        assert node.call('canonical',value=utf8_vector)==canonical(utf8_vector).decode()
        safe,exposed=redact({'note':'passphrase=synthetic-test-only'});assert exposed and 'synthetic-test-only' not in str(safe)
        assert not redact({'proof':p0['proof']})[1]
        full=synthetic_result_fixture()
        assert all(set(full['arms'][a]['security_controls'].values())=={'PASS'} for a in 'AB')
        for item in ('S01','L01'):
            e=envelope(f,'C',item);b=semantic_base(f,envelope=e);v=render(e,digest(b));s=statement(f,e,b,v,'ACCEPT',issued_at(f,item),V1)
            line='R0-P01 PLATFORM ATTEST '+e['acceptance_id']+' '+digest(s)
            assert line.startswith('R0-P01 PLATFORM ATTEST R0-P01-C-'+item+' ')
        result.update(synthetic_non_owner=True,controls_1_13_A_and_B='PASS',decision_consumption='PASS',stale_and_roles='PASS',historical_trust='PASS',canonicalization='PASS',secret_redaction='PASS',C_comparator_construction='PASS',webauthn=node.call('selftest'))
        return result
    finally:node.close()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--preflight',action='store_true');group.add_argument('--selftest',action='store_true');group.add_argument('--owner-run',action='store_true')
    parser.add_argument('--review-freeze-head');parser.add_argument('--output-directory')
    args=parser.parse_args()
    if args.owner_run:
        if not args.review_freeze_head or not args.output_directory:parser.error('owner-run requires reviewed freeze HEAD and outside-repository output directory')
        owner_run(args.output_directory,args.review_freeze_head)
    else:
        print(json.dumps(selftest() if args.selftest else preflight(),indent=2,sort_keys=True))


if __name__=='__main__':
    try:main()
    except IntegrityError:
        print('R0-P01 fail-closed: provenance, integrity or local verification failure.',file=sys.stderr);sys.exit(2)
