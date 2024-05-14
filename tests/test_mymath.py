"""
tester functies
"""
from mymath import add


def test_addition():
    """
    test if addition works
    """
    assert 4 == add.add(2, 2)
