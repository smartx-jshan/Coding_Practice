class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # sort first!
        nums.sort()
    
        # setting index
        index = 0
        
        # repeat without last value
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                index +=2
            else:
                return nums[index]
        
        # if last value in array
        return nums[index]
        
            
