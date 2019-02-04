class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = max_with_cur = nums[0]

        for x in nums[1:]:
            # At current position, max is either including x or not.
            max_with_cur = max(max_with_cur + x, x)
            max_so_far = max(max_so_far, max_with_cur)
            
        return max_so_far