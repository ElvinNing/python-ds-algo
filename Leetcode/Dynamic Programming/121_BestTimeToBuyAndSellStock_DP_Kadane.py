class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        price_delta = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        '''Problem 53: Max Subarray using DP and Kadane Algorithm'''
        def maxSubArray(nums):
            max_so_far = max_with_cur = 0
            for x in nums:
                # At current position, max is either including x or not.
                max_with_cur = max(max_with_cur + x, 0)
                max_so_far = max(max_so_far, max_with_cur)
            return max_so_far    
        
        return maxSubArray(price_delta)