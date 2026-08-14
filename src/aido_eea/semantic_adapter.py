from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class SemanticCandidate:
    source_anchor: str
    candidate_atomic_claim: str
    candidate_type: str | None = None
    candidate_scope: Dict[str, Any] | None = None
    confidence: float | None = None
    notes: List[str] | None = None


class SemanticAdapter(ABC):
    """
    EEA 2.0 extension interface.

    This adapter is intentionally outside the EEA 1.0 entitlement kernel.
    Implementations may propose candidates, but they must not issue final
    entitlement states or modify governed evidence contracts.
    """

    @abstractmethod
    def nominate_claims(self, text: str) -> List[SemanticCandidate]:
        raise NotImplementedError
