class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for digit in num:
            # you can directly compare them, because the 
            # ascii value of '9' is greater than that of '0'.
            while k and stack and stack[-1] > digit: 
                stack.pop()
                k -= 1
            stack.append(digit)
        # replace while loop with a simple slice
        if k: 
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'


