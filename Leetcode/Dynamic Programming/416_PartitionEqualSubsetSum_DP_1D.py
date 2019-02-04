class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None:
            return True
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        output = [False] * (total + 1)
        output[0] = True
        for n in nums:
            # Have to be reversed. Cannot reuse smaller elements.
            for s in reversed(range(n, total + 1)): 
                output[s] = output[s] or output[s-n]
        
        return output[int(total/2)]