def findNumbers(nums):
    count = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            count += 1
    return count


def test_1():
    assert findNumbers([12, 345, 2, 6, 7896]) == 2


def test_2():
    assert findNumbers([555, 901, 482, 1771]) == 1

