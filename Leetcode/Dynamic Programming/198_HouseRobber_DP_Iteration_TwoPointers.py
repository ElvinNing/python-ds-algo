# https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        previous2 = previous1 = 0
        for x in nums:
            # Python evaluation order of assignment: expr3, expr4 = expr1, expr2
            # max(previous1, previous2 + x): not steal x and use p1, or use p2 and steal x
            previous2, previous1 = previous1, max(previous1, previous2 + x)
        return previous1