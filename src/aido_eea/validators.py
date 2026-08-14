from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class PercentageCheck:
    numerator: float
    denominator: float
    stated_percent: float
    computed_percent: float
    absolute_error: float
    tolerance: float
    passed: bool


def displayed_precision_tolerance(stated_percent_text: str) -> float:
    """
    Derive a conservative half-unit-in-the-last-displayed-place tolerance.

    Examples:
    "88%" -> 0.5 percentage points
    "88.0%" -> 0.05 percentage points
    "88.00%" -> 0.005 percentage points
    """
    s = stated_percent_text.strip().replace("%", "")
    if "." in s:
        decimals = len(s.split(".", 1)[1])
    else:
        decimals = 0
    return 0.5 * (10 ** (-decimals))


def check_percentage(
    numerator: float,
    denominator: float,
    stated_percent: float,
    tolerance: float,
) -> PercentageCheck:
    if denominator == 0:
        raise ValueError("denominator must be non-zero")
    if not all(isfinite(x) for x in [numerator, denominator, stated_percent, tolerance]):
        raise ValueError("all values must be finite")

    computed = 100.0 * numerator / denominator
    err = abs(computed - stated_percent)

    # Small epsilon prevents binary floating point edge effects at the boundary.
    passed = err <= tolerance + 1e-12

    return PercentageCheck(
        numerator=numerator,
        denominator=denominator,
        stated_percent=stated_percent,
        computed_percent=computed,
        absolute_error=err,
        tolerance=tolerance,
        passed=passed,
    )
