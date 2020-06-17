import pytest

@pytest.mark.skip
def test_skip():
    assert True

def test_dont_skip():
    assert True

def test_sum():
    assert 3+3 == 6