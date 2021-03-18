class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [sys.maxsize] * (amount + 1)
        
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
                
        
        if dp[amount] != sys.maxsize:
            return dp[amount]
        else:
            return -1
        
        
        
