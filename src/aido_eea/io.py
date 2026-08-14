from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .models import (
    ClaimObject,
    ClaimType,
    ClauseStatus,
    ContractClause,
    EvidenceContract,
    EvidenceObject,
    HumanDisposition,
)


def _enum_value(value, enum_cls):
    if isinstance(value, enum_cls):
        return value
    return enum_cls(value)


def claim_from_dict(data: Dict[str, Any]) -> ClaimObject:
    contract_data = data.get("contract")
    contract = None
    if contract_data is not None:
        contract = EvidenceContract(
            contract_id=contract_data["contract_id"],
            claim_type=_enum_value(contract_data["claim_type"], ClaimType),
            clauses=[
                ContractClause(
                    clause_id=c["clause_id"],
                    description=c["description"],
                    required_for_minimum=c.get("required_for_minimum", True),
                    required_for_full=c.get("required_for_full", True),
                )
                for c in contract_data.get("clauses", [])
            ],
            inference_ceiling=contract_data.get("inference_ceiling", ""),
            notes=contract_data.get("notes", ""),
        )

    evidence = [
        EvidenceObject(
            evidence_id=e["evidence_id"],
            source=e["source"],
            role=e["role"],
            location=e.get("location"),
            version=e.get("version"),
            sha256=e.get("sha256"),
            lineage_group=e.get("lineage_group"),
            independence_class=e.get("independence_class"),
            supports=e.get("supports", []),
            contradicts=e.get("contradicts", []),
            metadata=e.get("metadata", {}),
        )
        for e in data.get("observed_evidence", [])
    ]

    return ClaimObject(
        claim_id=data["claim_id"],
        claim_text_source=data["claim_text_source"],
        normalized_atomic_claim=data["normalized_atomic_claim"],
        claim_type=_enum_value(data["claim_type"], ClaimType),
        scope_context=data.get("scope_context", {}),
        assertion_strength=data.get("assertion_strength", ""),
        contract=contract,
        observed_evidence=evidence,
        clause_status={
            k: _enum_value(v, ClauseStatus)
            for k, v in data.get("clause_status", {}).items()
        },
        assumptions=data.get("assumptions", []),
        dependencies=data.get("dependencies", []),
        contradiction_set=data.get("contradiction_set", []),
        falsification_triggers=data.get("falsification_triggers", []),
        critical_evidence_unavailable=data.get("critical_evidence_unavailable", False),
        non_adjudicable_reason=data.get("non_adjudicable_reason"),
        permitted_wording=data.get("permitted_wording"),
        prohibited_wording=data.get("prohibited_wording", []),
        human_disposition=_enum_value(
            data.get("human_disposition", HumanDisposition.PENDING.value),
            HumanDisposition,
        ),
        version_provenance=data.get("version_provenance", {}),
    )


def load_claim(path: str | Path) -> ClaimObject:
    path = Path(path)
    return claim_from_dict(json.loads(path.read_text(encoding="utf-8")))


def save_json(data: Dict[str, Any], path: str | Path) -> None:
    path = Path(path)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
