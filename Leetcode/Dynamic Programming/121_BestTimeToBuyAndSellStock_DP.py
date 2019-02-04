class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """     
        try:        
            max_profit, min_price = 0, prices[0]
            for x in prices[1:]:
                min_price = min(min_price, x)
                max_profit = max(max_profit, x - min_price) # not sell at x vs sell at x
            return max_profit    
        except:
            return 0