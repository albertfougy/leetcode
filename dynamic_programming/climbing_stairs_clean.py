class Solution:
    def climbStairs(self, n):
        if n in (1, 2):
            return n
        else:
            a, b = 0, 1
            for _ in range(n + 1):
                a, b = b, a + b
            return a