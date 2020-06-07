def getNoZeroIntegers(n):
    r = n
    while "0" in str(n - r) or "0" in str(r):
        r = r - 1
    return [n - r, r]


def test_1():
    assert getNoZeroIntegers(2) == [1, 1]


def test_2():
    assert getNoZeroIntegers(11) == [2, 9]


def test_3():
    assert getNoZeroIntegers(10000) == [1, 9999]


def test_4():
    assert getNoZeroIntegers(69) == [1, 68]


def test_5():
    assert getNoZeroIntegers(1010) == [11, 999]


def test_6():
    assert getNoZeroIntegers(4102) == [111, 3991]
