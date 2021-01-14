class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # in case of array size == 0
        if len(nums) == 0:
            return 0
        
        index = 0
        size = len(nums)
        
        while True:
            # next element checking 
            if index == size -1:
                break
            # if current element == next element
            if nums[index] == nums[index+1]:
                del nums[index+1]
                size -=1
            # else, increase index
            else:
                index +=1
        
        return len(nums)
        
