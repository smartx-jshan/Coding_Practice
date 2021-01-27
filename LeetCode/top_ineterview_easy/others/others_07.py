class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # use Gauss's foumula
        
        expected = len(nums) * (len(nums)+1) // 2
        
        return expected - sum(nums)
    
        
