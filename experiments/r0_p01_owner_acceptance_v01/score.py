"""Independent R0-P01 V02 normalization, public-evidence checks and scoring.

Reads raw evidence without modifying it. Emits a separate derived result.
--selftest uses in-memory, explicitly synthetic/non-owner records only.
Inventory drift blocks classification; integrity defects classify INVALID.
"""
import argparse
import copy
import datetime as dt
import json
import math
import statistics
import sys

import harness as h


def number(value):
    return type(value) in (int,float) and math.isfinite(value) and value>=0


def count(value):
    return type(value) is int and value>=0


def timestamp(value):
    if not isinstance(value,str):raise ValueError('timestamp')
    t=dt.datetime.fromisoformat(value.replace('Z','+00:00'))
    if t.tzinfo is None:raise ValueError('timezone')
    return t


def infrastructure_exemption(row):
    required={'trial_id','start_utc','end_utc','affected_component','observable_event_or_error','classification','task_owner_receipt'}
    receipts=row.get('infrastructure_receipts',[])
    if row['trial_id']=='L01' or not isinstance(receipts,list) or not receipts:return False
    for r in receipts:
        try:
            if not isinstance(r,dict) or not required.issubset(r) or r['trial_id']!=row['trial_id'] or r['classification']!='EXTERNAL_INFRASTRUCTURE_ONLY' or r['task_owner_receipt'] is not True:return False
            if not isinstance(r['affected_component'],str) or not r['affected_component'] or not isinstance(r['observable_event_or_error'],str) or not r['observable_event_or_error']:return False
            if timestamp(r['end_utc'])<=timestamp(r['start_utc']):return False
        except (ValueError,TypeError,KeyError):return False
    return True


def normalize_trial(row,expected,rc):
    if not isinstance(row,dict) or not set(rc['trial_fields']).issubset(row) or row['trial_id']!=expected:
        raise h.IntegrityError('malformed trial identity/fields')
    if type(row['success']) is not bool or row['decision'] not in (*h.DECISIONS,None):raise h.IntegrityError('trial outcome vocabulary')
    for field in ('semantic_review_seconds','mechanical_seconds'):
        if row[field] is not None and not number(row[field]):raise h.IntegrityError('invalid elapsed measurement')
    for field in ('interaction_count','device_switches','manual_metadata_edits'):
        if row.get(field) is not None and not count(row[field]):raise h.IntegrityError('invalid count')
    rating=row['friction_rating_1_to_5']
    if rating is not None and (type(rating) is not int or not 1<=rating<=5):raise h.IntegrityError('invalid friction rating')
    if row['friction_note'] is not None and not isinstance(row['friction_note'],str):raise h.IntegrityError('friction note')
    if row.get('execution_status','COMPLETE') not in ('UNEXECUTED','IN_PROGRESS','INTERRUPTED','COMPLETE'):raise h.IntegrityError('execution status')
    if row.get('execution_status','COMPLETE')!='COMPLETE' and row['success']:raise h.IntegrityError('incomplete trial cannot succeed')
    return copy.deepcopy(row)


def complete_trial(row,rc):
    return row['success'] and all(row[k] is not None for k in rc['trial_fields']) and count(row.get('manual_metadata_edits'))


def arm_metrics(arm,rc):
    trials=arm['small_trials'];large=arm['large_trial']
    median=statistics.median([r['mechanical_seconds'] for r in trials]) if all(number(r['mechanical_seconds']) for r in trials) else None
    eligible=(arm['realizability']=='REALIZABLE' and all(v=='PASS' for v in arm['security_controls'].values())
              and len(trials)==3 and all(complete_trial(r,rc) for r in trials) and complete_trial(large,rc)
              and arm['manual_metadata_edits']==0 and arm['secret_exposure'] is False
              and median is not None and median<=60
              and all(r['mechanical_seconds']<=120 or infrastructure_exemption(r) for r in trials)
              and large['mechanical_seconds']<=120)
    viable=(arm['realizability']=='REALIZABLE' and arm['secret_exposure'] is False
            and all(arm['security_controls'][k]=='PASS' for k in rc['cryptographic_proof_viability']['required_controls'])
            and any(r['success'] for r in trials))
    return {'selection_eligible':bool(eligible),'proof_viable':bool(viable),'median_small_mechanical_seconds':median,
            'large_mechanical_seconds':large['mechanical_seconds']}


def classify(metrics,inv,integrity):
    if integrity:return {'classification':'INVALID','selected_arm':None,'reason':'ATTEMPT_INTEGRITY_FAILURE'}
    viable=[a for a in 'AB' if metrics[a]['proof_viable']]
    eligible=[a for a in 'AB' if metrics[a]['selection_eligible']]
    if not viable:return {'classification':'REOPEN','selected_arm':None,'reason':'NO_PROOF_VIABLE_CRYPTOGRAPHIC_ARM'}
    if not eligible:return {'classification':'AMEND','selected_arm':None,'reason':'VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY'}
    selected=eligible[0]
    if len(eligible)==2:
        a,b=metrics['A'],metrics['B']
        if abs(a['median_small_mechanical_seconds']-b['median_small_mechanical_seconds'])>=10:
            selected=min('AB',key=lambda x:metrics[x]['median_small_mechanical_seconds'])
        elif abs(a['large_mechanical_seconds']-b['large_mechanical_seconds'])>=15:
            selected=min('AB',key=lambda x:metrics[x]['large_mechanical_seconds'])
        else:selected='B'
    minutes=inv['projected_acceptance_count']*metrics[selected]['median_small_mechanical_seconds']/60
    breach=inv['projected_acceptance_count']>100 or minutes>90
    return {'classification':'AMEND' if breach else 'PASS_WITH_SELECTION','selected_arm':selected,
            'projected_owner_mechanical_minutes':minutes,'volume_gate_breached':breach,
            'reason':'VOLUME_GATE' if breach else 'ELIGIBLE_SELECTED_WITHIN_VOLUME_GATES'}


def setup_credentials(arm):
    receipt=arm['setup_receipt']
    if receipt.get('status') not in ('COMPLETE','NOT_REALIZABLE','SETUP_INTERRUPTED','INCOMPLETE') or receipt.get('owner_confirmed') is not True or receipt.get('tofu')!='EXPLICIT_SYNTHETIC_TOFU':
        raise h.IntegrityError('resolved crypto arm without confirmed genesis')
    creds=receipt.get('credentials')
    if not isinstance(creds,list) or len(creds)!=2 or not all(h.valid_credential(c) for c in creds):raise h.IntegrityError('public setup credentials')
    members=h.sorted_members([h.member('PRIMARY',creds[0]),h.member('RECOVERY',creds[1])])
    if receipt.get('members')!=members or creds[0]['public_id']==creds[1]['public_id']:raise h.IntegrityError('public trust binding')
    return creds


def verify_evidence(raw,f,node,pretrial=False):
    a=raw['arms']['A'];b=raw['arms']['B']
    a_material=setup_credentials(a) if a['realizability']=='REALIZABLE' else None
    for arm in 'AB':
        data=raw['arms'][arm]
        if data['realizability']!='REALIZABLE' and data['setup_receipt'].get('owner_confirmed') is not True:
            if any(row['success'] for row in data['small_trials']+[data['large_trial']]) or any(v=='PASS' for v in data['security_controls'].values()):raise h.IntegrityError('unresolved/unavailable arm claims completed proof')
            continue
        primary,recovery=setup_credentials(data)
        if arm=='A' and (primary['kind']!='SSH_ED25519' or recovery['kind']!='SSH_ED25519'):raise h.IntegrityError('arm A kind')
        if arm=='B' and primary['kind']!='WEBAUTHN_ES256':raise h.IntegrityError('arm B kind')
        if arm=='B' and not pretrial:
            events=data['setup_receipt'].get('events',[])
            registrations=[e for e in events if e.get('type')=='registration' and e.get('status')=='VERIFIED']
            if len(registrations)!=1:raise h.IntegrityError('registration receipt missing')
            event=registrations[0]
            for key in ('issued_at','submitted_at','expires_at'):timestamp(event[key])
            if event.get('attempt_id')!='001' or event.get('arm')!='B' or event.get('consumed') is not True or not number(event.get('submitted_elapsed_ms')) or event['submitted_elapsed_ms']>=120000:raise h.IntegrityError('registration lifecycle')
            registered=node.call('verify_registration',response=event['response'],pending={'challenge':event['challenge']})
            if registered!=primary:raise h.IntegrityError('registration public binding')
        if a_material is None or recovery!=a_material[1]:raise h.IntegrityError('heterogeneous recovery binding')
        ap,ar=a_material
        make=lambda scenario:h.Ledger(f,arm,primary,recovery,ap,ar,scenario)
        records=data.get('security_records',{})
        p0=records.get('P0')
        if p0 and (p0['credential']!=primary or (p0['proof'] or {}).get('synthetic_non_owner') and not pretrial):raise h.IntegrityError('baseline credential provenance')
        actual,observations=h.controls_1_10(f,arm,p0,make('BASE_SECURITY'),node)
        burden=make('BURDEN');s01=None
        for row in data['small_trials']+[data['large_trial']]:
            rec=row.get('record');verified=False
            if rec:
                if rec['credential']!=primary or rec['item']!=row['trial_id'] or rec['statement']['decision']!=row['decision'] or (rec['proof'] or {}).get('synthetic_non_owner') and not pretrial:raise h.IntegrityError('burden identity/provenance')
                verified=h.verify(rec['statement'],rec['proof'],primary,node)
                if rec.get('verifier_result') not in (None,'VALID' if verified else 'INVALID'):raise h.IntegrityError('preserved verifier result conflict')
                admission=burden.admit(rec,node)
                if row.get('admission') is not None and row['admission']!=admission:raise h.IntegrityError('burden admission conflict')
                if verified and not admission['admitted']:raise h.IntegrityError('valid burden record consistency/authority failure')
                if row['trial_id']=='S01':s01=rec
            expected_success=verified and row.get('execution_status','COMPLETE')=='COMPLETE'
            if row['success'] is not expected_success:raise h.IntegrityError('claimed burden verification conflict')
        for item,cred in (('P5',primary),('P6',recovery)):
            rec=records.get(item)
            if rec and (rec['credential']!=cred or (rec['proof'] or {}).get('synthetic_non_owner') and not pretrial):raise h.IntegrityError('transition credential provenance')
        neg=data.get('control_evidence',{}).get(f['security_controls'][11],{}).get('negative_synthetic_non_owner_record')
        if neg and (not (neg.get('proof') or {}).get('synthetic_non_owner') or not records.get('P6') or neg['statement']!=records['P6']['statement']):raise h.IntegrityError('recovery test-double identity')
        last,last_observations=h.transition_controls(f,arm,make,p0,records.get('P5'),records.get('P6'),s01,node,negative_record=neg,generate_negative=False)
        actual.update(last)
        observations.update(last_observations)
        for key in f['security_controls']:
            preserved=data.get('control_evidence',{}).get(key)
            if preserved=={'reason':'unexecuted'}:
                actual[key]='FAIL'
            elif preserved!=observations[key]:raise h.IntegrityError('control observation/evidence conflict')
        if actual!=data['security_controls']:raise h.IntegrityError('claimed control outcome conflict')
        recorded_edits=[data['setup_receipt'].get('manual_metadata_edits')]+[r.get('manual_metadata_edits') for r in data['small_trials']+[data['large_trial']]]+[m.get('manual_metadata_edits') for m in data.get('security_measurements',{}).values()]
        total=sum(recorded_edits) if all(count(x) for x in recorded_edits) else None
        if total!=data['manual_metadata_edits']:raise h.IntegrityError('metadata edit total conflict')
    # C has no crypto authority. A terminal string alone cannot establish user role.
    for row in raw['arms']['C']['small_trials']+[raw['arms']['C']['large_trial']]:
        receipt=row.get('comparator')
        success=False
        if receipt:
            e=h.envelope(f,'C',row['trial_id']);base=h.semantic_base(f,envelope=e);view=h.render(e,h.digest(base));s=h.statement(f,e,base,view,row['decision'],h.issued_at(f,row['trial_id']),h.V1)
            expected='R0-P01 PLATFORM ATTEST '+e['acceptance_id']+' '+h.digest(s)
            if receipt['statement']!=s or receipt['envelope']!=e or receipt['owner_view']!=view.decode() or receipt['expected_line']!=expected or receipt['independently_repository_verifiable'] is not False:raise h.IntegrityError('comparator construction')
            if receipt.get('line_equal') is not (receipt['observed_line']==expected) or receipt.get('platform_reference') is not None and not isinstance(receipt['platform_reference'],str):raise h.IntegrityError('comparator observation conflict')
            success=receipt['observed_line']==expected and receipt.get('user_role_observed') is True and receipt.get('task_owner_receipt') is True and bool(receipt.get('platform_reference'))
        if row['success'] is not bool(success and row.get('execution_status','COMPLETE')=='COMPLETE'):raise h.IntegrityError('comparator provenance conflict')


def score(raw,pretrial=False):
    result={'derived_only':True,'raw_sha256':None,'classification':None,'selected_arm':None,
            'protocol':'R0-P01-V01','contract_revision':'R0-P01-CONTRACT-V02'}
    node=None
    try:
        result['raw_sha256']=h.digest(raw)
        if not isinstance(raw,dict):raise h.IntegrityError('raw object')
        _,exposure=h.redact(raw)
        declared=raw.get('integrity',{})
        if exposure or any(declared.get(k) is True for k in ('secret_exposure','post_observation_tuning','attempt_integrity_failure')):
            result.update(classification='INVALID',reason='ATTEMPT_INTEGRITY_FAILURE');return result
        c=h.contracts();f,rc=c['fixture.json'],c['result_contract.json']
        h.golden(f,c['clarification_vectors_v02.json'])
        inv=h.inventory()
        identity={'schema_version':2,'protocol':'R0-P01-V01','contract_revision':'R0-P01-CONTRACT-V02','attempt_id':'001'}
        if any(raw.get(k)!=v for k,v in identity.items()) or set(raw.get('arms',{}))!=set('ABC'):raise h.IntegrityError('raw identity')
        if raw.get('synthetic_pretrial_only') and not pretrial:raise h.IntegrityError('synthetic test double is not owner evidence')
        p=raw['provenance'];current=h.provenance()
        versions=p.get('runtime_versions')
        if not isinstance(p['repository_head'],str) or not h.re.fullmatch('[0-9a-f]{40}',p['repository_head']) or h.git('cat-file','-t',p['repository_head']).strip()!=b'commit':raise h.IntegrityError('repository identity')
        if not isinstance(versions,dict) or not {'python','node','openssh'}.issubset(versions) or any(not isinstance(v,str) or not v for v in versions.values()):raise h.IntegrityError('runtime provenance')
        if set(p['artifacts'])!=set(current['artifacts']):raise h.IntegrityError('artifact identity')
        for name,actual in current['artifacts'].items():
            bound=p['artifacts'][name]
            if any(bound.get(k)!=actual[k] for k in ('sha256','bytes','byte_basis','git_blob_byte_basis')):raise h.IntegrityError('artifact bytes changed')
            relative=(h.HERE/name).relative_to(h.ROOT).as_posix()
            try:blob_hash=h.sha(h.git('cat-file','blob',p['repository_head']+':'+relative))
            except h.IntegrityError:blob_hash=None
            if bound.get('git_blob_sha256')!=blob_hash or blob_hash is None and not pretrial:raise h.IntegrityError('artifact/head binding')
        result['verification_runtime_versions']=current['runtime_versions']
        normalized=copy.deepcopy(raw)
        safe,exposed=h.redact(normalized)
        if exposed:raise h.IntegrityError('secret boundary')
        integrity=raw['integrity']
        required=('secret_exposure','post_observation_tuning','attempt_integrity_failure')
        if any(type(integrity.get(k)) is not bool for k in required):raise h.IntegrityError('integrity vocabulary')
        for arm in 'ABC':
            data=normalized['arms'][arm]
            if not set(rc['required_arm_fields']).issubset(data) or data['arm_id']!=f['arm_ids'][arm]:raise h.IntegrityError('arm identity/required fields')
            if data['realizability'] not in ('REALIZABLE','NOT_REALIZABLE',None) or type(data['secret_exposure']) is not bool or type(data['selection_eligible']) is not bool:raise h.IntegrityError('arm vocabulary')
            if data['manual_metadata_edits'] is not None and not count(data['manual_metadata_edits']):raise h.IntegrityError('metadata count')
            if data['realizability'] is None and data['setup_receipt'].get('status') not in ('SETUP_INTERRUPTED','INCOMPLETE'):raise h.IntegrityError('unresolved setup classification')
            if set(data['security_controls'])!=set(f['security_controls']) or any(v not in (('NOT_APPLICABLE',) if arm=='C' else ('PASS','FAIL')) for v in data['security_controls'].values()):raise h.IntegrityError('security keys/values')
            expected=['S01'] if arm=='C' else ['S01','S02','S03']
            if len(data['small_trials'])!=len(expected):raise h.IntegrityError('small packet')
            data['small_trials']=[normalize_trial(row,key,rc) for row,key in zip(data['small_trials'],expected)]
            data['large_trial']=normalize_trial(data['large_trial'],'L01',rc)
        if any(integrity[k] for k in required) or any(raw['arms'][a]['secret_exposure'] for a in 'ABC'):
            result.update(classification='INVALID',reason='ATTEMPT_INTEGRITY_FAILURE');return result
        node=h.NodeBridge();verify_evidence(normalized,f,node,pretrial)
        metrics={a:arm_metrics(normalized['arms'][a],rc) for a in 'AB'}
        metrics['C']={'selection_eligible':False,'proof_viable':False}
        for arm in 'ABC':
            metrics[arm].update(realizability=normalized['arms'][arm]['realizability'],setup_status=normalized['arms'][arm]['setup_receipt'].get('status'))
        result.update(classify(metrics,inv,False),arms=metrics,inventory=inv)
        if pretrial:result['synthetic_pretrial_only']=True
        return result
    except h.InventoryMismatch:
        result.update(classification=None,blocked=True,reason='INVENTORY_SOURCE_MISMATCH_REFREEZE_REQUIRED');return result
    except (h.IntegrityError,KeyError,ValueError,TypeError,IndexError,AttributeError):
        result.update(classification='INVALID',reason='RESULT_IDENTITY_PROVENANCE_OR_EVIDENCE_DEFECT');return result
    finally:
        if node:node.close()


def selftest():
    c=h.contracts();f,rc=c['fixture.json'],c['result_contract.json'];inv=h.inventory()
    raw={'schema_version':2,'protocol':'R0-P01-V01','contract_revision':'R0-P01-CONTRACT-V02','attempt_id':'001',
         'synthetic_pretrial_only':True,
         'provenance':h.provenance(),'integrity':{'secret_exposure':False,'post_observation_tuning':False,'attempt_integrity_failure':False},'arms':{a:h.empty_arm(f,a) for a in 'ABC'}}
    before=copy.deepcopy(raw)
    assert score(raw,pretrial=True)['classification']=='REOPEN';assert raw==before
    bad=copy.deepcopy(raw);bad['integrity']['secret_exposure']=True;assert score(bad)['classification']=='INVALID'
    bad=copy.deepcopy(raw);bad['provenance']['repository_head']='0'*40;assert score(bad,pretrial=True)['classification']=='INVALID'
    bad=copy.deepcopy(raw);bad['arms']['A']['large_trial']['mechanical_seconds']=-1;assert score(bad,pretrial=True)['classification']=='INVALID'
    def metric(eligible=False,viable=False,small=20,large=30):return {'selection_eligible':eligible,'proof_viable':viable,'median_small_mechanical_seconds':small,'large_mechanical_seconds':large}
    assert classify({'A':metric(),'B':metric()},inv,False)['classification']=='REOPEN'
    assert classify({'A':metric(viable=True),'B':metric()},inv,False)['classification']=='AMEND'
    assert classify({'A':metric(True,True),'B':metric()},inv,False)['classification']=='PASS_WITH_SELECTION'
    for a,b,winner in [(20,30,'A'),(30,20,'B'),(20,29,'B')]:
        assert classify({'A':metric(True,True,a),'B':metric(True,True,b)},inv,False)['selected_arm']==winner
    assert classify({'A':metric(True,True,20,10),'B':metric(True,True,21,25)},inv,False)['selected_arm']=='A'
    assert classify({'A':metric(True,True,20,25),'B':metric(True,True,21,10)},inv,False)['selected_arm']=='B'
    assert classify({'A':metric(True,True),'B':metric(True,True)},inv,True)['classification']=='INVALID'
    assert classify({'A':metric(True,True,60),'B':metric()},inv,False)['classification']=='AMEND'
    assert classify({'A':metric(True,True),'B':metric()},dict(inv,projected_acceptance_count=101),False)['classification']=='AMEND'
    arm=h.empty_arm(f,'A');arm['realizability']='REALIZABLE';arm['security_controls']={k:'PASS' for k in f['security_controls']};arm['manual_metadata_edits']=0
    for row in arm['small_trials']+[arm['large_trial']]:
        row.update(decision='REJECT',semantic_review_seconds=1,mechanical_seconds=20,interaction_count=1,device_switches=0,manual_metadata_edits=0,success=True,execution_status='COMPLETE',friction_rating_1_to_5=1)
    assert arm_metrics(arm,rc)['selection_eligible']
    arm['large_trial']['success']=False;assert not arm_metrics(arm,rc)['selection_eligible'];arm['large_trial']['success']=True
    arm['small_trials'][0]['mechanical_seconds']=121;assert not arm_metrics(arm,rc)['selection_eligible']
    receipt={'trial_id':'S01','start_utc':'2026-10-06T00:00:00Z','end_utc':'2026-10-06T00:01:00Z','affected_component':'synthetic infrastructure','observable_event_or_error':'synthetic outage','classification':'EXTERNAL_INFRASTRUCTURE_ONLY','task_owner_receipt':True}
    arm['small_trials'][0]['infrastructure_receipts']=[receipt];assert arm_metrics(arm,rc)['selection_eligible']
    arm['small_trials'][1]['mechanical_seconds']=121;assert not arm_metrics(arm,rc)['selection_eligible']  # median still counts interruption
    arm['small_trials'][1]['mechanical_seconds']=20;arm['large_trial']['mechanical_seconds']=121;arm['large_trial']['infrastructure_receipts']=[dict(receipt,trial_id='L01')];assert not arm_metrics(arm,rc)['selection_eligible']
    arm['large_trial']['mechanical_seconds']=20;arm['small_trials'][2]['interaction_count']=None;assert not arm_metrics(arm,rc)['selection_eligible']
    synthetic=h.synthetic_result_fixture();saved=copy.deepcopy(synthetic)
    scored=score(synthetic,pretrial=True)
    assert scored['classification']=='PASS_WITH_SELECTION' and scored['selected_arm']=='B',scored
    assert synthetic==saved
    assert score(synthetic)['classification']=='INVALID'  # cannot masquerade as owner evidence
    forged=copy.deepcopy(synthetic);forged['arms']['A']['security_controls'][f['security_controls'][2]]='FAIL'
    assert score(forged,pretrial=True)['classification']=='INVALID'
    forged=copy.deepcopy(synthetic);forged['arms']['A']['small_trials'][0]['record']['owner_view']+='x'
    assert score(forged,pretrial=True)['classification']=='INVALID'
    return {'synthetic_pretrial_only':True,'raw_immutability':'PASS','normalization':'PASS','integrity_and_provenance':'PASS',
            'classifications':['INVALID','REOPEN','AMEND','PASS_WITH_SELECTION'],'selection_thresholds_and_tie':'PASS',
            'large_success_and_missing_measurements':'PASS','infrastructure_exception_and_median':'PASS','volume_gates':'PASS','C_ineligible':'PASS',
            'A_B_full_public_evidence_reverification':'PASS','synthetic_cannot_be_owner_evidence':'PASS','conflicting_controls_or_view':'PASS'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('raw',nargs='?');parser.add_argument('--selftest',action='store_true');args=parser.parse_args()
    if args.selftest:result=selftest()
    else:
        if not args.raw:parser.error('raw evidence file required, or --selftest')
        with open(args.raw,'rb') as stream:raw=h.strict_json(stream.read())
        result=score(raw)
    print(json.dumps(result,ensure_ascii=False,allow_nan=False,sort_keys=True,indent=2))


if __name__=='__main__':main()
