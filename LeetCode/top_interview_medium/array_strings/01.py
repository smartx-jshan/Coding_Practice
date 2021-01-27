class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort first
        nums.sort()
        
        result = []
        
        # i is pointer from 0 to len-2
        for i in range (len(nums)-2):
            
            # avoid repeatition
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                
                temp_sum = nums[i] + nums[left] + nums[right]
                # if find
                if temp_sum < 0:
                    left+=1
                elif temp_sum >0:
                    right-=1
                else:
                    # sum == 0
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    
                    left +=1
                    right -=1
                    
                    
        
        return result
