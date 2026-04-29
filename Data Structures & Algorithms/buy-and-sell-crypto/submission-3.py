class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        maxProfit = 0

        # if only one price
        if len(prices) == 1:
            return maxProfit
        
        # intialize pointers
        buy, sell = 0, 1

        for sell in range(len(prices)):
            currProfit = 0
            # if profit is not being made, move buy ptr
            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1

            else:
                currProfit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, currProfit)
        
        return maxProfit
