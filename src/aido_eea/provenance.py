from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable, Dict, List

from .models import EvidenceObject


def sha256_file(path: str | Path) -> str:
    path = Path(path)
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def group_by_lineage(evidence: Iterable[EvidenceObject]) -> Dict[str, List[str]]:
    """
    Group evidence by lineage_group.

    Evidence without an explicit lineage group is placed in a group named
    after its own evidence_id. This helper does not infer independence.
    """
    groups: Dict[str, List[str]] = {}
    for item in evidence:
        key = item.lineage_group or item.evidence_id
        groups.setdefault(key, []).append(item.evidence_id)
    return groups
