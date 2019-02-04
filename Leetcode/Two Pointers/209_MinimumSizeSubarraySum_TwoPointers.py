class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        output, i, total = len(nums) + 1, 0, 0  # i is the left pointer.
        for j, n in enumerate(nums):  # j is the right pointer.
            total += n
            while total >= s:
                output = min(output, j - i + 1)
                total -= nums[i]
                i += 1
        if output == len(nums) + 1:
            return 0
        else:
            return output
   