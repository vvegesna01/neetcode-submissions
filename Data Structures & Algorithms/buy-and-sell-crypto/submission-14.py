class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        # prices = [10, 5, 4, 8, 9, 7]
        #           1.  2  3. 4  5. 6

        buy = 0
        sell = 0

        max_profit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)

            if prices[sell] < prices[buy]:
                buy = sell
            else:
                sell += 1
            
        return max_profit

                
