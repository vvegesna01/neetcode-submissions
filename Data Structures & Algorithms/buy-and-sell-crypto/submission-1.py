class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy, sell = 0, 1
        #consider l as buying price
        while sell < len(prices):
            #if profit possible
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            else:
                buy = sell
            sell += 1

        return max_profit


        