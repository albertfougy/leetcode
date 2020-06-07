def balancedStringSplit(s):
    count = balance = 0
    for char in s:
        if char == "R":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            count += 1
    return count


def test_1():
    assert balancedStringSplit("RLRRLLRLRL") == 4


def test_2():
    assert balancedStringSplit("RLLLLRRRLR") == 3


def test_3():
    assert balancedStringSplit("LLLLRRRR") == 1


def test_4():
    assert balancedStringSplit("RLRRRLLRLL") == 2
