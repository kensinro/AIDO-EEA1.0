from __future__ import annotations
import csv, json
from pathlib import Path
from aido_eea.validation import exact_accuracy, macro_f1, pairwise_agreement, fleiss_kappa
ROOT=Path(__file__).resolve().parent
def read(name):
    with (ROOT/name).open(encoding="utf-8-sig",newline="") as f: return list(csv.DictReader(f))
def summarize(rows,gold_col,ops):
    gold=[r[gold_col] for r in rows]
    pooled_g=[]; pooled_p=[]
    per={}
    for op in ops:
        pred=[r[op] for r in rows]
        per[op]={"accuracy":exact_accuracy(gold,pred),"macro_f1":macro_f1(gold,pred)}
        pooled_g+=gold; pooled_p+=pred
    pairs={}
    for i,a in enumerate(ops):
        for b in ops[i+1:]:
            pairs[f"{a} vs {b}"]=pairwise_agreement([r[a] for r in rows],[r[b] for r in rows])
    return {"per_operator":per,"pooled_accuracy":exact_accuracy(pooled_g,pooled_p),"pooled_macro_f1":macro_f1(pooled_g,pooled_p),"pairwise_agreement":pairs,"mean_pairwise_agreement":sum(pairs.values())/len(pairs),"fleiss_kappa":fleiss_kappa([[r[o] for o in ops] for r in rows])}
ops=["GPT-5.6 Sol","Claude","Gemini"]
t3=read("T3_STATE_MATRIX_LOCKED.csv"); t6=read("T6_R1_STATE_MATRIX_LOCKED.csv"); t8=read("T8_R1_STATE_MATRIX_LOCKED.csv"); tr=read("T8_R1_TRANSITION_MATRIX_LOCKED.csv")
out={"T3":summarize(t3,"Gold",ops),"T6_R1":summarize(t6,"expected_state",ops),"T8_R1":summarize(t8,"expected_state",ops)}
out["T8_R1"]["complete_transition_path_accuracy"]=sum(r["all_three_correct"].lower()=="true" for r in tr)/len(tr)
recovery=[r for r in t8 if r["condition"]=="ADD" and r["expected_state"]=="ENTITLED"]
rc=sum(r[o]=="ENTITLED" for r in recovery for o in ops); rt=len(recovery)*len(ops)
mask=[r for r in t8 if r["condition"]=="MASK"]; fc=sum(r[o]=="CONTRADICTED" for r in mask for o in ops); ft=len(mask)*len(ops)
direct=[r for r in t8 if r["condition"]=="ADD" and r["expected_state"]=="CONTRADICTED"]; dc=sum(r[o]=="CONTRADICTED" for r in direct for o in ops); dt=len(direct)*len(ops)
out["T8_R1"]["supportive_recovery"]={"correct":rc,"total":rt,"rate":rc/rt}
out["T8_R1"]["false_contradicted_under_masking"]={"count":fc,"total":ft,"rate":fc/ft}
out["T8_R1"]["direct_incompatible_evidence"]={"correct":dc,"total":dt,"independent_base_scenarios":len(direct),"rate":dc/dt}
print(json.dumps(out,indent=2,ensure_ascii=False))
