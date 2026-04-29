class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0


        buy = 0
        maxProfit = 0
        for sell in range(1, len(prices)):
            
            # sell prices is less than buy price
            # we would be making a loss
            print("buy:", buy)
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                maxProfit = max(profit, maxProfit)

        return maxProfit
