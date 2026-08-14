from aido_eea.validators import displayed_precision_tolerance, check_percentage


def test_precision_tolerance():
    assert displayed_precision_tolerance("88%") == 0.5
    assert displayed_precision_tolerance("88.0%") == 0.05
    assert displayed_precision_tolerance("88.00%") == 0.005


def test_percentage_boundary_epsilon():
    result = check_percentage(95, 100, 95.05, 0.05)
    assert result.passed


def test_percentage_fail():
    result = check_percentage(95, 100, 95.2, 0.05)
    assert not result.passed
