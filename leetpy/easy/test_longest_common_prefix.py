def longestCommonPrefix(strs):
    str_list = [list(s) for s in strs]
    zipped = tuple(zip(*str_list))
    prefix = ""
    for z in zipped:
        if len(set(z)) > 1:
            break
        else:
            for i in set(z):
                prefix += i
    return prefix


def test_1():
    given = ["flower", "flow", "flight"]
    expected = "fl"
    actual = longestCommonPrefix(given)
    assert actual == expected


def test_2():
    given = ["dog", "racecar", "car"]
    expected = ""
    actual = longestCommonPrefix(given)
    assert actual == expected


def test_3():
    given = ["aca", "cba"]
    expected = ""
    actual = longestCommonPrefix(given)
    assert actual == expected
