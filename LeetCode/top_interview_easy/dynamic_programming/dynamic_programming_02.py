class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # use min_prices
        min_prices = sys.maxsize
        profit = 0
        
        for i in prices:
            min_prices = min(min_prices, i)
            profit = max(profit, i - min_prices)
        
        return profit
