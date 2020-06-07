def reverse(x):
    str_num = str(abs(x))
    inversion = int(str_num[::-1])
    if inversion.bit_length() >= 32:
        return 0
    if x < 0:
        return int(f"-{inversion}")
    else:
        return inversion


def test_1():
    assert reverse(123) == 321


def test_2():
    assert reverse(-123) == -321


def test_3():
    assert reverse(120) == 21


def test_4():
    assert reverse(1_534_236_469) == 0

