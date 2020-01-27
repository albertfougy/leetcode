class Solution:

        def reverseString(self, str):
            return str.reverse()
            
        def reverseStr(self, strng2):
            """ 2nd option, but less readable """
            strng2[:] = strng2[::-1]
            return strng2

        