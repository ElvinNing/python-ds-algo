class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        if len(nums) == 1:
            return nums[0]
        
        def rob1(num):
            if not nums:
                return 0
            previous2 = previous1 = 0
            for x in nums:
                # Python evaluation order of assignment: expr3, expr4 = expr1, expr2
                # max(previous1, previous2 + x): not steal x and use p1, or use p2 and steal x
                previous2, previous1 = previous1, max(previous1, previous2 + x)
            return previous1
            
        return max(rob1(nums[:-1]), rob1(nums[1:]))