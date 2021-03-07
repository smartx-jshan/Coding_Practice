class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        peak_index =0
        
        for i in range(len(nums)):
            if nums[i] > nums[peak_index]:
                peak_index = i  
        return peak_index
        
