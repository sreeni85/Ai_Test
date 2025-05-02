import time
import random
import pytest

@pytest.mark.fast
def test_fast():
    """A fast test that always passes."""
    time.sleep(0.1)  # Simulate a short runtime
    assert True

@pytest.mark.slow
def test_slow():
    """A slow test that always passes."""
    time.sleep(2)  # Simulate a longer runtime
    assert True

@pytest.mark.flaky
def test_flaky():
    """A flaky test that randomly passes or fails."""
    time.sleep(0.5)  # Simulate a moderate runtime
    assert random.choice([True, False])