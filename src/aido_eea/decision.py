from __future__ import annotations

from .contracts import evaluate_contract
from .models import AuditDecision, ClaimObject, ClaimState, DecisionTrace


def adjudicate_claim(claim: ClaimObject) -> AuditDecision:
    """
    Apply the canonical five-state EEA decision rule.

    Important:
    - This function does not perform semantic claim extraction.
    - It does not decide whether evidence is scientifically true.
    - It adjudicates a governed ClaimObject from explicit contract/clause inputs.
    """
    evaluation = evaluate_contract(claim)

    contradiction_present = bool(claim.contradiction_set)
    abstention_triggered = bool(
        claim.critical_evidence_unavailable or claim.non_adjudicable_reason
    )

    reasons: list[str] = []

    if contradiction_present:
        state = ClaimState.CONTRADICTED
        reasons.append(
            "Directly incompatible evidence is present in contradiction_set."
        )
    elif abstention_triggered:
        state = ClaimState.ABSTAIN
        reason = claim.non_adjudicable_reason or "Critical evidence is unavailable."
        reasons.append(reason)
    elif evaluation.full_satisfied:
        state = ClaimState.ENTITLED
        reasons.append("Full evidence contract is satisfied.")
    elif evaluation.minimum_satisfied:
        state = ClaimState.QUALIFIED
        reasons.append(
            "Minimum evidence contract is satisfied but full contract is incomplete."
        )
        if evaluation.missing_full:
            reasons.append(
                "Unsatisfied full-contract clauses: "
                + ", ".join(evaluation.missing_full)
            )
        if evaluation.unknown_full:
            reasons.append(
                "Unknown full-contract clauses: "
                + ", ".join(evaluation.unknown_full)
            )
    else:
        state = ClaimState.NOT_ENTITLED
        reasons.append(
            "The stated formulation does not satisfy the minimum evidence contract."
        )
        if evaluation.missing_minimum:
            reasons.append(
                "Unsatisfied minimum-contract clauses: "
                + ", ".join(evaluation.missing_minimum)
            )
        if evaluation.unknown_minimum:
            reasons.append(
                "Unknown minimum-contract clauses: "
                + ", ".join(evaluation.unknown_minimum)
            )

    trace = DecisionTrace(
        claim_id=claim.claim_id,
        minimum_clause_results=evaluation.minimum_results,
        full_clause_results=evaluation.full_results,
        minimum_satisfied=evaluation.minimum_satisfied,
        full_satisfied=evaluation.full_satisfied,
        contradiction_present=contradiction_present,
        abstention_triggered=abstention_triggered,
        reasons=reasons,
    )

    return AuditDecision(
        claim_id=claim.claim_id,
        state=state,
        trace=trace,
        permitted_wording=claim.permitted_wording,
        prohibited_wording=claim.prohibited_wording,
        human_disposition=claim.human_disposition,
    )
