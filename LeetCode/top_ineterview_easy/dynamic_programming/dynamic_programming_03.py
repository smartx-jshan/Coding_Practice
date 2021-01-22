class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        result = -sys.maxsize
        
        # 지금까지의 합 (양수 이상만 저장)
        cur_sum = 0
        
        for i in range(len(nums)):
            # calculate max_sum
            result = max(result, cur_sum + nums[i])
            
            # cur_sum calculate
            cur_sum += nums[i]
            # if cur_sum is negative, reset to zero
            if cur_sum < 0:
                cur_sum = 0
        
        return result
                
