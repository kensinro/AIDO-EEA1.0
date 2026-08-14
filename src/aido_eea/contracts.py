from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .models import (
    ClauseStatus,
    ClaimObject,
    ContractClause,
    EvidenceContract,
)


@dataclass(frozen=True)
class ContractEvaluation:
    minimum_results: Dict[str, ClauseStatus]
    full_results: Dict[str, ClauseStatus]
    minimum_satisfied: bool
    full_satisfied: bool
    missing_minimum: List[str]
    missing_full: List[str]
    unknown_minimum: List[str]
    unknown_full: List[str]


def _required_clauses(
    contract: EvidenceContract,
    level: str,
) -> List[ContractClause]:
    if level == "minimum":
        return [c for c in contract.clauses if c.required_for_minimum]
    if level == "full":
        return [c for c in contract.clauses if c.required_for_full]
    raise ValueError(f"Unknown contract level: {level}")


def _evaluate_required(
    required: List[ContractClause],
    status_map: Dict[str, ClauseStatus],
) -> tuple[Dict[str, ClauseStatus], List[str], List[str], bool]:
    results: Dict[str, ClauseStatus] = {}
    missing: List[str] = []
    unknown: List[str] = []

    for clause in required:
        status = status_map.get(clause.clause_id, ClauseStatus.UNKNOWN)
        results[clause.clause_id] = status

        if status == ClauseStatus.UNSATISFIED:
            missing.append(clause.clause_id)
        elif status == ClauseStatus.UNKNOWN:
            unknown.append(clause.clause_id)

    satisfied = not missing and not unknown
    return results, missing, unknown, satisfied


def evaluate_contract(claim: ClaimObject) -> ContractEvaluation:
    if claim.contract is None:
        raise ValueError("ClaimObject.contract is required for adjudication.")

    min_required = _required_clauses(claim.contract, "minimum")
    full_required = _required_clauses(claim.contract, "full")

    min_results, min_missing, min_unknown, min_ok = _evaluate_required(
        min_required, claim.clause_status
    )
    full_results, full_missing, full_unknown, full_ok = _evaluate_required(
        full_required, claim.clause_status
    )

    return ContractEvaluation(
        minimum_results=min_results,
        full_results=full_results,
        minimum_satisfied=min_ok,
        full_satisfied=full_ok,
        missing_minimum=min_missing,
        missing_full=full_missing,
        unknown_minimum=min_unknown,
        unknown_full=full_unknown,
    )
