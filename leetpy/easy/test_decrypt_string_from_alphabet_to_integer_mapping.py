def freqAlphabets(s):
    alpha = [char for char in s]
    for i, char in enumerate(s):
        if char == "#":
            alpha[i - 2] = s[i - 2 : i]
            alpha[i - 1] = alpha[i] = ""
    decode = [chr(int(a) + 96) for a in alpha if a != ""]
    return "".join(decode)


def test_1():
    assert freqAlphabets("10#11#12") == "jkab"


def test_2():
    assert freqAlphabets("1326#") == "acz"


def test_3():
    assert freqAlphabets("25#") == "y"


def test_4():
    given = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    expected = "abcdefghijklmnopqrstuvwxyz"
    assert freqAlphabets(given) == expected

