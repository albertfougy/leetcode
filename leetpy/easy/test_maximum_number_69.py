def maximum69Number(num):
    digits = list(str(num))
    if "6" in digits:
        digits[digits.index("6")] = "9"
        return int("".join(digits))
    return num


def max69_simple(num):
    return int(str(num).replace("6", "9", 1))


def test_1():
    assert maximum69Number(9669) == 9969
    assert max69_simple(9669) == 9969


def test_2():
    assert maximum69Number(9996) == 9999
    assert max69_simple(9996) == 9999


def test_3():
    assert maximum69Number(9999) == 9999
    assert max69_simple(9999) == 9999
