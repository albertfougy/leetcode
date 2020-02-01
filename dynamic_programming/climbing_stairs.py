# Climbing Stairs 70

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step



# Solution 1 Brute Force

# Time: O(2^n)
# Space: O(n)
	

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2 or n == 3:
            return n
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

# This solution will experience runtime error


# Solution 2 memoization

class Solution:
    cache = {}    
    def climbStairs(self, n):
        if n < 3:
            return n
        else:
            return self._climbStairs(n-1) + self._climbStairs(n-2)
    def _climbStairs(self, n):
        if n not in self.cache.keys():
            self.cache[n] = self.climbStairs(n)
        return self.cache[n]

# use memoization to reduce redundant processing


# Solution 3 Loop Fibonacci

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        else:
            res, step_1, step_2 = 0,1,2
            for i in range(2, n):
                res = step_2 + step_1
                step_1 = step_2
                step_2 = res
            return res

    def climbStairs(self, n):
        if n in (1, 2):
            return n
        else:
            a, b = 0, 1
            for _ in range(n + 1):
                a, b = b, a + b
            return a

# Time: O(n)
# Space: O(1)

# Similar questions:

# 91. Decode ways
# 62. Unique Paths
# 509. Fibonacci Number

# Practice them in a row for better understanding