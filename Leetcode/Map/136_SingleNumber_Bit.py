# https://docs.python.org/3/library/stdtypes.html?highlight=bit%20manipulation

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for n in nums:
            a ^= n  # XOR bit operation
        return a
        