class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majorityElementRec(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi-lo)//2
            left = majorityElementRec(lo, mid)
            right = majorityElementRec(mid+1, hi)
         
            if left == right:
                return left

            def helper(count):
                return sum(1 for i in range(lo, hi + 1) if nums[i] == count)

            left_count = helper(left)
            right_count = helper(right)

            return left if left_count > right_count else right

        return majorityElementRec(0, len(nums)-1)
