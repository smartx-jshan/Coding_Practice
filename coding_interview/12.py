class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        min_profit = sys.maxsize
        
        for i in prices:
            min_profit = min(min_profit, i)
            profit = max (profit, i - min_profit)
        return profit
