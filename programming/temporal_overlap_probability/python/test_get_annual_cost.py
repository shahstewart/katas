import pytest
import random
from temporal_overlap_probability import get_annual_cost

def test_get_annual_cost():
    # day * prob * cost per downtime.
    target = 365 * 0.3608 * 1000  # prob is calculated with random state 42.

    random.seed(333)
    # assert the returned value is within the 5% variation threshold for 100 runs
    for i in range(1, 101):
        assert get_annual_cost() == pytest.approx(target, 0.05)
