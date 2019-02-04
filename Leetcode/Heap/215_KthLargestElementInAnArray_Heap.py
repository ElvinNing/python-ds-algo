import heapq


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
        
'''
heapq.nlargest(k):
1. heapify k elements as h_k. O(k)
2. heappushpop the remaining n-k elements to the heap h_k. O((n-k)*logk)
3. sort h_k. O(k*logk)
The time complexity of heapq.nlargest(k) is O(k + (n-k)*logk + k*logk) = O(n*logk)
Trivially, if k isn't specified (k = n), complexity is O(n*logn).
If k is sufficiently small, complexity is O(n).

https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity
https://stackoverflow.com/questions/23038756/how-does-heapq-nlargest-work

kth order statistic linear complexity algorithm: https://en.wikipedia.org/wiki/Selection_algorithm
'''