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
        
        length = len(nums)    
        # output[i][s]: whether s is sums of some elements from nums[0] to nums[i]
        # (length + 1) * (total + 1) matrix
        output = [[False for i in range(total + 1)] for s in range(length + 1)] 
        for i in range(length + 1):
            output[i][0] = True          
        for i, n in enumerate(nums): # counter, value in enumerate, start=0
            for s in range(1, total + 1): 
                if s >= n:
                    output[i+1][s] = output[i][s] or output[i][s-n]
                else:
                    output[i+1][s] = output[i][s]
                
        return output[length][int(total/2)]