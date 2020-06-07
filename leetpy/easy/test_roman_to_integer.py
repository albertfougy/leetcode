def romanToInt(s):
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    numeric = [numerals.get(char) for char in s]
    total = 0
    for index, n in enumerate(numeric):
        if index < (len(numeric) - 1) and numeric[index + 1] > n:
            total -= n
        else:
            total += n
    return total


def test_1():
    numeral = "III"
    expected = 3
    actual = romanToInt(numeral)
    assert actual == expected


def test_2():
    numeral = "IV"
    expected = 4
    actual = romanToInt(numeral)
    assert actual == expected


def test_3():
    numeral = "IX"
    expected = 9
    actual = romanToInt(numeral)
    assert actual == expected


def test_4():
    numeral = "LVIII"
    # L = 50, V = 5, III = 3
    expected = 58
    actual = romanToInt(numeral)
    assert actual == expected


def test_5():
    numeral = "MCMXCIV"
    # M = 1000, CM = 900, XC = 90, IV = 4
    expected = 1994
    actual = romanToInt(numeral)
    assert actual == expected
