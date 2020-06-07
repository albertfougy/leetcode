def removeDuplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
            i -= 1
        elif i > 0 and nums[i] == nums[i - 1]:
            nums.pop(i)
            i -= 1
        i += 1
    return len(nums)


def test_1():
    given = [1, 1, 2]
    expected = [1, 2]
    length = 2
    actual = removeDuplicates(given)
    assert given == expected
    assert actual == length


def test_2():
    given = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = [0, 1, 2, 3, 4]
    length = 5
    actual = removeDuplicates(given)
    assert given == expected
    assert actual == length
