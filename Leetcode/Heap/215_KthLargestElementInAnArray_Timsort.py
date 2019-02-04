class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1]

'''Time Complexity: O(nlogn)        
Python's built in sort algorithm: https://en.wikipedia.org/wiki/Timsort
kth order statistic linear complexity algorithm: https://en.wikipedia.org/wiki/Selection_algorithm
'''