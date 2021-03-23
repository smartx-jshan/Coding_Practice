class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = []
        dp.append(1) #초기화
        
        #dp 를 채우자
        
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[j] < nums[i]: #크기가 증가하는 거라면
                    maxval = max(maxval, dp[j])
            
            dp.append(maxval + 1) #dp 하나를 채우고
        
        #print (dp)
        #dp에서의 맥스값을 리턴
        return max(dp)
