class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxprofit = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            curr_profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, curr_profit)
            sell += 1
            
        
        return maxprofit