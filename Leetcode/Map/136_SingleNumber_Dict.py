class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        # Will leave the single number after iteration.
        for n in nums:
            try:
                h.pop(n)  # h is a hash map. Search complexity avg O(1)
            except:
                h[n] = None
        return h.popitem()[0]
        
        