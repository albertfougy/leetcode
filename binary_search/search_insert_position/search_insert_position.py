class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Given a sorted array and a target value, return the index if the target
        is found. If not, return the index where it would be if it were inserted in order.
        You may assume no duplicates in the array.
        Here are few examples.
        [1,3,5,6], 5 >> 2
        [1,3,5,6], 2 >> 1
        [1,3,5,6], 7 >> 4
        [1,3,5,6], 0 >> 0 
        '''
        # n = len(nums)
        # if n == 0 or target <= nums[0]: 
        #     return 0
        # if target > nums[n-1]: 
        #     return n
        # left, right = 0, n-1
        # while left < right:
        #     mid = (left+right)//2
        #     if target == nums[mid]: 
        #         return mid
        #     if target > nums[mid]: 
        #         left = mid+1
        #     else: 
        #         right = mid-1
        # if target > nums[left]: 
        #     return left+1
        # else: 
        #     return left

# 1st Refactor
    # def searchInsert2(self, nums: List[int], target: int) -> int:
    #     left=0
    #     right=len(nums)-1
    #     while left<=right:s
    #         mid=int((left+right)/2)
    #         if nums[mid]==target:
    #             return mid
    #         elif nums[mid]>target:
    #             right=mid-1
    #         else:
    #             left=mid+1
    #     return left

# 2nd Refactor and clearest
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j - i)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return i




# 3rd Refactor using for loop
    # def searchInsert3(self, nums: List[int], target: int) -> int:
    #     for i in range(len(nums)):
    #         if nums[i]==target:
    #             return i
    #         elif target<nums[i]:
    #             return i
    #     return len(nums)
