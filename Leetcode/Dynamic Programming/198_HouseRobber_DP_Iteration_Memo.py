# https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        memo = [None] * (len(nums) + 1) 
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(2, len(nums)+1):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i-1])
                
        return memo[len(nums)]