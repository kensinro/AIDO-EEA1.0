from aido_eea.decision import adjudicate_claim
from aido_eea.models import ClaimObject, ClaimType, ClauseStatus, ContractClause, EvidenceContract, ClaimState

def make_claim():
    c=EvidenceContract("BOUND",ClaimType.ASSOCIATIVE,[ContractClause("rmin","bounded",True,True),ContractClause("rfull","current claim full",False,True)])
    return ClaimObject("B","source","bounded claim",ClaimType.ASSOCIATIVE,contract=c,clause_status={"rmin":ClauseStatus.SATISFIED,"rfull":ClauseStatus.SATISFIED})

def test_current_claim_rfull_protected_from_hypothetical_escalation():
    c=make_claim()
    c.dependencies.append("hypothetical stronger c+ needs more evidence")
    assert adjudicate_claim(c).state == ClaimState.ENTITLED

def test_qualified_boundary():
    c=make_claim(); c.clause_status["rfull"]=ClauseStatus.UNKNOWN
    assert adjudicate_claim(c).state == ClaimState.QUALIFIED

def test_abstain_requires_explicit_nonadjudicability():
    c=make_claim(); c.clause_status["rmin"]=ClauseStatus.UNKNOWN
    assert adjudicate_claim(c).state == ClaimState.NOT_ENTITLED
    c.critical_evidence_unavailable=True
    assert adjudicate_claim(c).state == ClaimState.ABSTAIN

def test_contradiction_precedes_abstain():
    c=make_claim(); c.critical_evidence_unavailable=True; c.contradiction_set=["direct incompatible evidence"]
    assert adjudicate_claim(c).state == ClaimState.CONTRADICTED
