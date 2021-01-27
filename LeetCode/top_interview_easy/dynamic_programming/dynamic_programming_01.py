class Solution:
    # same as fibonacci
    dp = collections.defaultdict(int)
    dp[1] =1
    dp[2] =2
    def climbStairs(self, n: int) -> int:
        
        # memoization method
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.dp[n]
