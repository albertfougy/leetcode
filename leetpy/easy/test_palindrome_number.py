def isPalindrome(x):
    return str(x) == str(x)[::-1]


def test_1():
    assert isPalindrome(121) is True


def test_2():
    assert isPalindrome(-121) is False


def test_3():
    assert isPalindrome(10) is False
