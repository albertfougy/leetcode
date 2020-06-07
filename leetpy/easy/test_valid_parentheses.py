def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if stack:
                top_element = stack.pop()
            else:
                top_element = ""
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


def test_1():
    given = "()"
    actual = isValid(given)
    assert actual is True


def test_2():
    given = "()[]{}"
    actual = isValid(given)
    assert actual is True


def test_3():
    given = "(]"
    actual = isValid(given)
    assert actual is False


def test_4():
    given = "([)]"
    actual = isValid(given)
    assert actual is False


def test_5():
    given = "{[]}"
    actual = isValid(given)
    assert actual is True
