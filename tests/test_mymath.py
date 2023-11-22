from mymath import add, substract


def test_addition():
    assert 4 == add.add(2, 2)


def test_substraction():
    assert 4 == substract.substract(8, 4)
