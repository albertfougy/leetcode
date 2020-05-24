# The way to make the number as small as possible is that make the rightmost digit as small as possible.

# We know we can remove at most the k digit to generate a new digit
# so we can add/remove until k == 0

# Example "1432219"
# []
# ['1'] => since stack is empty , just add into stack
# ['1', '4'] => since 1 < 4, we do not need to replace
# ['1', '3'] => since 3 is less than 4, and we have k(3)-- times able to remove,so we can
# replace 4 with 3
# ['1', '2'] => 2 < 3, replace 3 with 2 k(2) --
# ['1', '2', '2'] => 2 == 2, continue
# ['1', '2', '1'] => since 1 < 2, replace it k(1)--
# ['1', '2', '1', '9'] => does not matter if the next number is lesser or greater, since k is zero, we
# can not remove any more digits, so this is the end of program.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            while True:
                if  k == 0 or not stack:
                    break
                if stack[-1] > num[i]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[i])
        while k != 0:
            stack.pop()
            k -= 1
        for i in range(len(stack)):
            if stack[i] != "0":
                break
        stack = stack[i:]
        if not stack:
            return "0"
        else:
            return "".join(stack)


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num): return '0'
        num = [l for l in num]
        
        while k > 0:
            flag = True
            for i in range(len(num)-1):
                if str(num[i]) > str(num[i+1]):
                    num.pop(i)
                    k, flag = k - 1, False
                    break
                    
            if flag == True and num[i+1] == num[-1]: 
                num.pop(i+1)
                k -= 1
        
        return str(int(''.join(num)))


class Solution:
def maxNumber(self, nums1, nums2, k):

    def prep(nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

    def merge(a, b):
        return [max(a, b).pop(0) for _ in a+b]

    return max(merge(prep(nums1, i), prep(nums2, k-i))
               for i in range(k+1)
               if i <= len(nums1) and k-i <= len(nums2))