from aido_eea.models import (
    ClaimObject,
    ClaimType,
    ClauseStatus,
    ContractClause,
    EvidenceContract,
)
from aido_eea.decision import adjudicate_claim
from aido_eea.models import ClaimState


def base_claim():
    contract = EvidenceContract(
        contract_id="C",
        claim_type=ClaimType.ASSOCIATIVE,
        clauses=[
            ContractClause("a", "minimum", True, True),
            ContractClause("b", "full only", False, True),
        ],
    )
    return ClaimObject(
        claim_id="X",
        claim_text_source="source",
        normalized_atomic_claim="normalized",
        claim_type=ClaimType.ASSOCIATIVE,
        contract=contract,
        clause_status={
            "a": ClauseStatus.SATISFIED,
            "b": ClauseStatus.SATISFIED,
        },
    )


def test_entitled():
    c = base_claim()
    assert adjudicate_claim(c).state == ClaimState.ENTITLED


def test_qualified():
    c = base_claim()
    c.clause_status["b"] = ClauseStatus.UNKNOWN
    assert adjudicate_claim(c).state == ClaimState.QUALIFIED


def test_not_entitled():
    c = base_claim()
    c.clause_status["a"] = ClauseStatus.UNSATISFIED
    assert adjudicate_claim(c).state == ClaimState.NOT_ENTITLED


def test_abstain_precedes_contract_state():
    c = base_claim()
    c.critical_evidence_unavailable = True
    assert adjudicate_claim(c).state == ClaimState.ABSTAIN


def test_contradiction_precedes_abstain():
    c = base_claim()
    c.critical_evidence_unavailable = True
    c.contradiction_set = ["direct incompatible evidence"]
    assert adjudicate_claim(c).state == ClaimState.CONTRADICTED
