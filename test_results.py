import pytest

from results import calculate_result


def test_passing_result():
    result = calculate_result([60, 70, 80])

    assert result == {
        "average": 70,
        "status": "Pass"
    }


def test_failing_result():
    result = calculate_result([20, 30, 40])

    assert result == {
        "average": 30,
        "status": "Fail"
    }


def test_negative_mark_is_rejected():
    with pytest.raises(ValueError):
        calculate_result([-10, 60])