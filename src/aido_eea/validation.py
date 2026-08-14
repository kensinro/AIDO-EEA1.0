from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Sequence

from .models import ClaimState

CANONICAL_STATES: tuple[str, ...] = tuple(state.value for state in ClaimState)

def normalize_state_label(label: str) -> str:
    value = str(label).strip()
    if value == "NOT_ENTITLED":
        return ClaimState.NOT_ENTITLED.value
    return value

@dataclass(frozen=True)
class StateMetrics:
    state: str
    tp: int
    fp: int
    fn: int
    precision: float
    recall: float
    f1: float

def exact_accuracy(gold: Sequence[str], predicted: Sequence[str]) -> float:
    if len(gold) != len(predicted):
        raise ValueError("gold and predicted must have the same length")
    if not gold:
        raise ValueError("gold and predicted must be non-empty")
    return sum(normalize_state_label(g) == normalize_state_label(p) for g, p in zip(gold, predicted)) / len(gold)

def pairwise_agreement(a: Sequence[str], b: Sequence[str]) -> float:
    return exact_accuracy(a, b)

def confusion_matrix(gold: Sequence[str], predicted: Sequence[str], states: Sequence[str] = CANONICAL_STATES):
    if len(gold) != len(predicted):
        raise ValueError("gold and predicted must have the same length")
    states = tuple(normalize_state_label(s) for s in states)
    matrix = {g: {p: 0 for p in states} for g in states}
    for g, p in zip(gold, predicted):
        g = normalize_state_label(g)
        p = normalize_state_label(p)
        if g not in matrix:
            raise ValueError(f"unknown gold state: {g}")
        if p not in matrix[g]:
            raise ValueError(f"unknown predicted state: {p}")
        matrix[g][p] += 1
    return matrix

def per_state_metrics(gold: Sequence[str], predicted: Sequence[str], states: Sequence[str] = CANONICAL_STATES):
    states = tuple(normalize_state_label(s) for s in states)
    matrix = confusion_matrix(gold, predicted, states)
    out=[]
    for state in states:
        tp=matrix[state][state]
        fp=sum(matrix[g][state] for g in states if g != state)
        fn=sum(matrix[state][p] for p in states if p != state)
        precision=tp/(tp+fp) if tp+fp else 0.0
        recall=tp/(tp+fn) if tp+fn else 0.0
        f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
        out.append(StateMetrics(state,tp,fp,fn,precision,recall,f1))
    return out

def macro_f1(gold: Sequence[str], predicted: Sequence[str], states: Sequence[str] = CANONICAL_STATES) -> float:
    m=per_state_metrics(gold,predicted,states)
    return sum(x.f1 for x in m)/len(m)

def fleiss_kappa(rows: Sequence[Sequence[str]], states: Sequence[str] = CANONICAL_STATES) -> float:
    if len(rows) < 2:
        raise ValueError("at least two items are required")
    n_raters=len(rows[0])
    if n_raters < 2:
        raise ValueError("at least two raters are required")
    if any(len(row) != n_raters for row in rows):
        raise ValueError("all rows must contain the same number of ratings")
    states=tuple(normalize_state_label(s) for s in states)
    state_set=set(states)
    counts=[]
    for row in rows:
        row=[normalize_state_label(x) for x in row]
        if any(x not in state_set for x in row):
            raise ValueError("unknown state label")
        c=Counter(row)
        counts.append([c.get(s,0) for s in states])
    p_i=[]
    for rc in counts:
        p_i.append((sum(n*n for n in rc)-n_raters)/(n_raters*(n_raters-1)))
    p_bar=sum(p_i)/len(p_i)
    total=len(rows)*n_raters
    p_j=[sum(rc[j] for rc in counts)/total for j in range(len(states))]
    p_e=sum(x*x for x in p_j)
    if abs(1-p_e)<1e-15:
        return 1.0 if abs(1-p_bar)<1e-15 else 0.0
    return (p_bar-p_e)/(1-p_e)
