import copy
import json
from collections import defaultdict, deque
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def topo(nodes, edges):
    indeg={n:0 for n in nodes}
    adj=defaultdict(list)
    for a,b in edges:
        if a not in indeg or b not in indeg:
            return False, []
        adj[a].append(b); indeg[b]+=1
    q=deque(sorted(n for n,d in indeg.items() if d==0))
    order=[]
    while q:
        n=q.popleft(); order.append(n)
        for m in sorted(adj[n]):
            indeg[m]-=1
            if indeg[m]==0: q.append(m)
    return len(order)==len(nodes), order

def reachable(edges, src, dst):
    adj=defaultdict(list)
    for a,b in edges: adj[a].append(b)
    seen={src}; stack=[src]
    while stack:
        n=stack.pop()
        for m in adj[n]:
            if m==dst: return True
            if m not in seen: seen.add(m); stack.append(m)
    return False

def registry_valid(rows):
    seen={}
    for r in rows:
        key=r["predicate_id"]
        sig=(r["definition_revision"],r["executable_definition_digest"])
        if key in seen and seen[key]!=sig:
            return False
        seen[key]=sig
    required={"WARRANT_F_BASE_DECISIONS","J3_REQUIREMENT_TRUTH"}
    for pid in ("EVIDENCE_VALIDITY_V1","EVIDENCE_FRESHNESS_V1"):
        matches=[r for r in rows if r["predicate_id"]==pid]
        if len(matches)!=1 or not required.issubset(set(matches[0]["consumers"])):
            return False
    return True

def graph_valid(graph, registry):
    nodes=graph["nodes"]; edges=[tuple(x) for x in graph["same_revision_edges"]]
    dag,order=topo(nodes,edges)
    precedence = all([
        reachable(edges,"LINEAGE_RESOLUTION","CURRENT_ACTIVE_REQUIREMENT_SET"),
        reachable(edges,"CURRENT_ACTIVE_REQUIREMENT_SET","J3_REQUIREMENT_TRUTH"),
        reachable(edges,"J3_REQUIREMENT_TRUTH","GENERATED_ORIENTATION"),
    ])
    forbidden=[
        ("WARRANT_F_META_ON_J3_SNAPSHOT","J3_REQUIREMENT_TRUTH"),
        ("GENERATED_ORIENTATION","J3_REQUIREMENT_TRUTH"),
        ("CONTROL_COMPILATION","J3_REQUIREMENT_TRUTH"),
        ("DELIVERY_EXECUTION","NATURAL_OWNER_SOURCE_FACTS"),
        ("REVIEW_ROUTING","J1_ACCEPTED_GOVERNING_MEANING"),
    ]
    forbidden_absent=all(x not in edges for x in forbidden)
    detective_safe=(("DETECTIVE_OBSERVATION","REVIEW_ROUTING") in edges and
                    ("DETECTIVE_OBSERVATION","J1_ACCEPTED_GOVERNING_MEANING") not in edges and
                    ("DETECTIVE_OBSERVATION","NATURAL_OWNER_SOURCE_FACTS") not in edges)
    return dag and precedence and forbidden_absent and detective_safe and registry_valid(registry), {
        "dag":dag,"topological_order":order,"precedence":precedence,
        "forbidden_same_revision_feedback_absent":forbidden_absent,
        "detective_routes_review_only":detective_safe,
        "predicate_registry_valid":registry_valid(registry)
    }

def main():
    graph=json.loads((ROOT/"graph.json").read_text())
    registry=json.loads((ROOT/"predicate_registry.json").read_text())["predicates"]
    controls=json.loads((ROOT/"negative_controls.json").read_text())["controls"]

    base_valid,base_details=graph_valid(graph,registry)
    feedback_valid=all(x["revision_delta"]>=1 for x in graph["next_revision_feedback"])

    control_rows=[]
    for c in controls:
        g=copy.deepcopy(graph); r=copy.deepcopy(registry)
        if c["kind"]=="add_same_revision_edge":
            g["same_revision_edges"].append(c["edge"])
            valid,_=graph_valid(g,r)
        elif c["kind"]=="duplicate_predicate":
            r.append(c["predicate"])
            valid,_=graph_valid(g,r)
        elif c["kind"]=="next_revision_edge":
            valid=(c["edge"]["revision_delta"]>=1 and graph_valid(g,r)[0])
        else:
            valid=False
        control_rows.append({"id":c["id"],"expected_valid":c["expected_valid"],"observed_valid":valid,"matches":valid==c["expected_valid"]})

    summary={
        "base_valid":base_valid,
        "next_revision_feedback_valid":feedback_valid,
        "negative_controls_all_match":all(x["matches"] for x in control_rows),
        "proof_checks":{
            "P1_same_revision_dag":base_details["dag"],
            "P2_lineage_active_j3_orientation_precedence":base_details["precedence"],
            "P3_meta_assurance_no_same_snapshot_feedback":base_details["forbidden_same_revision_feedback_absent"],
            "P4_feedback_revision_increment":feedback_valid,
            "P5_predicate_registry_unique":base_details["predicate_registry_valid"],
            "P6_shared_predicate_consumers":base_details["predicate_registry_valid"],
            "P7_generated_outputs_downstream":base_details["forbidden_same_revision_feedback_absent"],
            "P8_detective_review_only":base_details["detective_routes_review_only"],
        }
    }
    summary["outcome"]="D3_DEPENDENCY_PROOF_PASSES" if (
        summary["base_valid"] and summary["next_revision_feedback_valid"] and
        summary["negative_controls_all_match"] and all(summary["proof_checks"].values())
    ) else "D3_AMEND"
    result={"probe_id":"HYBRID_D3_DEPENDENCY_V01","base_details":base_details,"controls":control_rows,"summary":summary}
    (ROOT/"result.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(summary,sort_keys=True))

if __name__=="__main__":
    main()
