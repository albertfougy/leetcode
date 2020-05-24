# 136. Single  Number

# Given a non-empty array of integers, every element appears twice 
# except for one. Find that single one.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ Using set DS to find number """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber2(self, nums: List[int]) -> int:
        sngle = 0
        for num in range(len(nums)):
            sngle ^= num
        return num


if __name__ == "__main__":
    print(Solution().singleNumber([4,1,2,1,2]))

