def subtractProductAndSum(n):
    p, s = 1, 0
    for d in str(n):
        p *= int(d)
        s += int(d)
    return p - s


def test_1():
    assert subtractProductAndSum(234) == 15


def test_2():
    assert subtractProductAndSum(4421) == 21
