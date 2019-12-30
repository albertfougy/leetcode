# Given a string containing digits from 2-9 inclusive, return all possible letter 
# combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. 

# https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

# Note that 1 does not map to any letters.


# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# Note:

# Although the above answer is in lexicographical order, your answer could be in 
# any order you want.


class Solution:
    def letterCombinations(self, digits):
      def dfs(digits, d, l, cur, ans):
        if l == len(digits):
          if l > 0: ans.append("".join(cur))
          return
        
        for c in d[ord(digits[l]) - ord('0')]:
            cur[l] = c
            dfs(digits, d, l + 1, cur, ans)
        
      d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
      cur = [' ' for _ in range(len(digits))]
      ans = []
      dfs(digits, d, 0, cur, ans)
      return ans