# 136. Single  Number

# Given a non-empty array of integers, every element appears twice 
# except for one. Find that single one.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ Using set DS to find number """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber2(self, nums: List[int]) -> int:
        """ Using XOR """
        sngle = 0
        for num in nums:
            sngle ^= num
        return num


if __name__ == "__main__":
    print(Solution().singleNumber([4,1,2,1,2]))



# It is a so called "type hint" (or "function annotation"; these are available 
# since Python 3.0).

# -> List[int] means that the function should return a list of integers.
# nums: List[int], target: int means that nums is expected to be a list of 
# integers and that target is expected to be an integer.

# This is not a hard requirement, though, i.e. you can still call the function 
# with objects of different types passed for these parameters and the function 
# can as well return something different than a list of intergers (unlike in 
# other languages like Java where providing wrong types would result in a compile error). 
# To put it differently: Type hints are irrelevant for the program execution, 
# they are ignored at runtime (ignoring the type hints is just the default behavior, 
# but they are available at runtime via __annotations__, so you could do something with them).

# Type hints can express the intent of the author and can be checked before 
# program execution by tools like mypy (these can check e.g. that a function is 
# only called with parameters of the correct type and returns something of the 
# correct type).

# Note that List is not available in the standard namespace (unlike list), but 
# instead needs to be imported from typing which also

# provides other types for standard types, like Set, Dict, Tuple, Callable etc.
# allows to define own types
# provides typed versions of other types, like NamedTuple instead of namedtuple
