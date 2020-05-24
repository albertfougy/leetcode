# recursive implementation with O(n) memory.

def memoize(f):
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return wrapper


class Solution(object):
    @memoize
    def numDecodings(self, s):
        if len(s) == 0:
            return 1
        elif len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1


        if int(s[-1]) > 0:
            if 9 < int(s[-2:]) < 27:
                return self.numDecodings(s[:-1]) + self.numDecodings(s[:-2])
            else:
                return self.numDecodings(s[:-1])
        elif 9 < int(s[-2:]) < 27:
            return self.numDecodings(s[:-2])
        else:
            return 0