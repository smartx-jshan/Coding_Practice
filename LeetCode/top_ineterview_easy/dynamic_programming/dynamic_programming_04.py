class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # tabulation
        
        if not nums:
            return 0
        
        if len(nums) <=2:
            return max(nums)
        
        # dynamic programming
        dp = collections.defaultdict(int)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        
        for i in range (2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[i]
    
