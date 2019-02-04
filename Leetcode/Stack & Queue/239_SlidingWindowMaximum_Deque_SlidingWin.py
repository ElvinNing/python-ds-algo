from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        # https://www.youtube.com/watch?v=ShbRCjvB_yQ
        # idx is a deque storing potential candidates, ordered both in indices and values. 
        # The head is always the largest that we should return. 
        # Note we store indices instead of elements for out-of-window left pop convenience.
        idx = collections.deque()
        for i, n in enumerate(nums):
            # If current head is out of window.
            if idx and idx[0] == i-k:
                idx.popleft()
            # We pop all the smaller elements when we meet larger and newer candidate n.
            # Current element n, if it's larger, is always more "useful" than idx[-1].
            # Deque isn't empty and current element > deque tail, pop.
            while idx and n > nums[idx[-1]]:
                idx.pop()
            # We always append i. If it's not the largest, 
            # it is newer and may be useful for later windows.
            idx.append(i)
            # Trivially we only start the return when iterated at least k elements.  
            if i >= k-1:
                output.append(nums[idx[0]])
                
        return output
