def isNumber(s):
    try:
        s = float(s)
        return True
    except Exception:
        return False


def test_1():
    assert isNumber("0") is True


def test_2():
    assert isNumber(" 0.1 ") is True


def test_3():
    assert isNumber("abc") is False


def test_4():
    assert isNumber("1 a") is False


def test_5():
    assert isNumber("2e10") is True


def test_6():
    assert isNumber(" -90e3   ") is True


def test_7():
    assert isNumber(" 1e") is False


def test_8():
    assert isNumber("e3") is False


def test_9():
    assert isNumber(" 6e-1") is True


def test_10():
    assert isNumber(" 99e2.5 ") is False


def test_11():
    assert isNumber("53.5e93") is True


def test_12():
    assert isNumber(" --6 ") is False


def test_13():
    assert isNumber("-+3") is False


def test_14():
    assert isNumber("95a54e53") is False
