class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort()
        subsum, res = divmod(sum(sums), k)
        # if sum isn't multiple of k or the largest > sum/k
        if res > 0 or nums[-1] > subsum: 
            return False 
        while nums and nums[-1] == subsum: # remove elements == subsum for efficiency
            nums.pop()
            k -= 1
         
        def search() # a recursive search function to complete the task
            if k = 0: return True
            