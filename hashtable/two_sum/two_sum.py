class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for i , num in enumerate(nums):
            if num in cache:
                return [cache[num], i]
            else:
                cache[target - num] = i
