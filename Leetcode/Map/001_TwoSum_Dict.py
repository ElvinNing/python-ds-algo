# https://wiki.python.org/moin/TimeComplexity


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}  # Implemented as hash table.
        for i, n in enumerate(nums):
            comp = target - n
            if comp in dic:  # in operation O(1)
                return [dic[comp], i]
            dic[n] = i
        return False
