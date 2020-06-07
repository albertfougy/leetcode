def divisors(num):
    shapes = []
    for n in range(1, num + 1):
        if num % n == 0:
            t = (n, num // n)
            shapes.append(t)
    return shapes


def matrixReshape(nums, r, c):
    rows = len(nums)
    columns = max([len(n) for n in nums])
    flat = [item for sublist in nums for item in sublist]
    vector = rows * columns
    possible_shapes = divisors(vector)
    reshaped = []
    if (r, c) in possible_shapes:
        for i in range(r):
            start = i * c
            end = start + c
            reshaped.append(flat[start:end])
        return reshaped
    else:
        return nums


def test_reshape_1_x_4():
    nums = [[1, 2], [3, 4]]
    expected = [[1, 2, 3, 4]]
    actual = matrixReshape(nums, 1, 4)
    assert actual == expected


def test_reshape_2_x_4():
    nums = [[1, 2], [3, 4]]
    expected = [[1, 2], [3, 4]]
    actual = matrixReshape(nums, 2, 4)
    assert actual == expected


def test_reshape_4_x_1():
    nums = [[1, 2], [3, 4]]
    expected = [[1], [2], [3], [4]]
    actual = matrixReshape(nums, 4, 1)
    assert actual == expected


def test_reshape_3_x_2():
    nums = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 2], [3, 4], [5, 6]]
    actual = matrixReshape(nums, 3, 2)
    assert actual == expected
