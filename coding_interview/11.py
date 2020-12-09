class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []
        
        p = 1
        
        for i in range (0, len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        for j in range (len(nums)-1, 0-1, -1):
            out[j] = out[j] * p
            p = p * nums[j]
            
        return out
            
            
        
