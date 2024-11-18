import pytest
import calculations.statistics


def test_event_probability():
    result = calculations.statistics.event_probability(5, 10)
    assert result == 50.0


def test_event_probability_negative_input():
    with pytest.raises(ValueError) as error:
        calculations.statistics.event_probability(2, 0)
    assert str(error.value) == "Sample space size should be greater than zero"


def test_event_probability_outcomes_greater_than_space():
    with pytest.raises(ValueError) as error:
        calculations.statistics.event_probability(5, 3)
    assert str(error.value) == "Event outcomes should be lower or equal than" \
                               " sample space"

