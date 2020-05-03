class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for i , num in enumerate(nums):
            if num in cache:
                return [cache[num], i]
            else:
                cache[target - num] = i

    # def twoSum(self, nums, target):
    #     h = {}
    #     for i, num in enumerate(nums):
    #         n = target - num
    #         if n not in h:
    #             h[num] = i
    #         else:
    #             return [h[n], i]
