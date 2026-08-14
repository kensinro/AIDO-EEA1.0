"""AIDO-EEA Python reference implementation."""

from .models import (
    ClaimType,
    ClaimState,
    ClauseStatus,
    HumanDisposition,
    ContractClause,
    EvidenceContract,
    EvidenceObject,
    ClaimObject,
    DecisionTrace,
    AuditDecision,
)
from .decision import adjudicate_claim
from .validation import CANONICAL_STATES, normalize_state_label, StateMetrics, exact_accuracy, pairwise_agreement, confusion_matrix, per_state_metrics, macro_f1, fleiss_kappa

__all__ = [
    "ClaimType",
    "ClaimState",
    "ClauseStatus",
    "HumanDisposition",
    "ContractClause",
    "EvidenceContract",
    "EvidenceObject",
    "ClaimObject",
    "DecisionTrace",
    "AuditDecision",
    "adjudicate_claim",
    "CANONICAL_STATES",
    "normalize_state_label",
    "StateMetrics",
    "exact_accuracy",
    "pairwise_agreement",
    "confusion_matrix",
    "per_state_metrics",
    "macro_f1",
    "fleiss_kappa",
]

__version__ = "0.2.0"
