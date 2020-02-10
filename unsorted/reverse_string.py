class Solution:
        def reverseString(self, s):
            s.reverse()
            return s

        # def reverseString(self, s):
        #     return s[::-1]


if __name__ == "__main__":
    print(Solution().reverseString(["t","e","a"]))