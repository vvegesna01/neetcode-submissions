class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        maxP = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            cur_profit = prices[sell] - prices[buy]
            maxP = max(cur_profit, maxP)
            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
            else:
                sell += 1
        
        return maxP
