def twoSum(nums, target):
    lookup = {}
    for index, num in enumerate(nums):
        remainder = target - num
        if remainder in lookup:
            return [lookup[remainder], index]
        else:
            lookup[num] = index


def test_1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    actual = twoSum(nums, target)
    assert actual == expected


def test_2():
    nums = [2, 5, 5, 11]
    target = 10
    expected = [1, 2]
    actual = twoSum(nums, target)
    assert actual == expected
