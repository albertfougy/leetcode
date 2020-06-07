def atoi(s):
    s = s.lstrip()
    int_str = ""
    if s and (s[0] == "+" or s[0] == "-"):
        int_str += s[0]
        s = s[1:]
    for char in s:
        if char.isnumeric():
            int_str += char
        else:
            break
    try:
        int_str = int(int_str)
        if int_str >= 2 ** 31:
            return 2 ** 31 - 1
        if int_str <= -2 ** 31:
            return -2 ** 31
        return int_str
    except Exception:
        return 0


def test_1():
    assert atoi("42") == 42


def test_2():
    assert atoi("   -42") == -42


def test_3():
    assert atoi("4193 with words") == 4193


def test_4():
    assert atoi("words and 987") == 0


def test_5():
    assert atoi("-91283472332") == -2 ** 31


def test_6():
    assert atoi("91283472332") == 2 ** 31 - 1


def test_7():
    assert atoi("3.14159") == 3


def test_8():
    assert atoi("") == 0


def test_9():
    assert atoi("  -0012a42") == -12


def test_10():
    assert atoi(".1") == 0


def test_11():
    assert atoi("-") == 0


def test_12():
    assert atoi("+1") == 1
