from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Dict, List, Optional


class ClaimType(str, Enum):
    DESCRIPTIVE = "descriptive"
    ASSOCIATIVE = "associative"
    PREDICTIVE = "predictive"
    PROGNOSTIC = "prognostic"
    ROBUSTNESS = "robustness"
    EXTERNAL_TRANSFER = "external_transfer"
    CAUSAL = "causal"
    MECHANISTIC = "mechanistic"
    CLINICAL_UTILITY = "clinical_utility"
    REPRODUCIBILITY = "reproducibility"
    NORMATIVE = "normative"
    OTHER = "other"


class ClaimState(str, Enum):
    ENTITLED = "ENTITLED"
    QUALIFIED = "QUALIFIED"
    ABSTAIN = "ABSTAIN"
    NOT_ENTITLED = "NOT ENTITLED"
    CONTRADICTED = "CONTRADICTED"


class ClauseStatus(str, Enum):
    SATISFIED = "SATISFIED"
    UNSATISFIED = "UNSATISFIED"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class HumanDisposition(str, Enum):
    ACCEPT = "ACCEPT"
    MODIFY = "MODIFY"
    VETO = "VETO"
    REQUEST_EVIDENCE = "REQUEST_EVIDENCE"
    REOPEN = "REOPEN"
    PENDING = "PENDING"


@dataclass(frozen=True)
class ContractClause:
    clause_id: str
    description: str
    required_for_minimum: bool = True
    required_for_full: bool = True


@dataclass(frozen=True)
class EvidenceContract:
    contract_id: str
    claim_type: ClaimType
    clauses: List[ContractClause]
    inference_ceiling: str = ""
    notes: str = ""


@dataclass(frozen=True)
class EvidenceObject:
    evidence_id: str
    source: str
    role: str
    location: Optional[str] = None
    version: Optional[str] = None
    sha256: Optional[str] = None
    lineage_group: Optional[str] = None
    independence_class: Optional[str] = None
    supports: List[str] = field(default_factory=list)
    contradicts: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ClaimObject:
    claim_id: str
    claim_text_source: str
    normalized_atomic_claim: str
    claim_type: ClaimType
    scope_context: Dict[str, Any] = field(default_factory=dict)
    assertion_strength: str = ""
    contract: Optional[EvidenceContract] = None
    observed_evidence: List[EvidenceObject] = field(default_factory=list)
    clause_status: Dict[str, ClauseStatus] = field(default_factory=dict)
    assumptions: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    contradiction_set: List[str] = field(default_factory=list)
    falsification_triggers: List[str] = field(default_factory=list)
    critical_evidence_unavailable: bool = False
    non_adjudicable_reason: Optional[str] = None
    permitted_wording: Optional[str] = None
    prohibited_wording: List[str] = field(default_factory=list)
    human_disposition: HumanDisposition = HumanDisposition.PENDING
    version_provenance: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DecisionTrace:
    claim_id: str
    minimum_clause_results: Dict[str, ClauseStatus]
    full_clause_results: Dict[str, ClauseStatus]
    minimum_satisfied: bool
    full_satisfied: bool
    contradiction_present: bool
    abstention_triggered: bool
    reasons: List[str] = field(default_factory=list)


@dataclass
class AuditDecision:
    claim_id: str
    state: ClaimState
    trace: DecisionTrace
    permitted_wording: Optional[str] = None
    prohibited_wording: List[str] = field(default_factory=list)
    human_disposition: HumanDisposition = HumanDisposition.PENDING

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["state"] = self.state.value
        data["human_disposition"] = self.human_disposition.value
        data["trace"]["minimum_clause_results"] = {
            k: v.value if isinstance(v, ClauseStatus) else v
            for k, v in self.trace.minimum_clause_results.items()
        }
        data["trace"]["full_clause_results"] = {
            k: v.value if isinstance(v, ClauseStatus) else v
            for k, v in self.trace.full_clause_results.items()
        }
        return data
