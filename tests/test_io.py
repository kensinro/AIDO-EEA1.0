from pathlib import Path
from aido_eea.io import load_claim
from aido_eea.decision import adjudicate_claim
from aido_eea.models import ClaimState


def test_example_loads_and_qualifies():
    path = Path(__file__).parents[1] / "examples" / "example_claim.json"
    claim = load_claim(path)
    decision = adjudicate_claim(claim)
    assert decision.state == ClaimState.QUALIFIED
