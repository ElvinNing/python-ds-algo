from collections import Counter


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        # return max(counts.keys(), key=(lambda x: counts[x]))