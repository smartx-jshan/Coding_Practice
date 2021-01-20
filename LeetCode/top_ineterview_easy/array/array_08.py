class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        # assign non-zero elements in increasing order
        
        # remember the number of non-zero elements
        non_zero = 0
        
        for i in nums:
            if i != 0:
                nums[non_zero] = i
                non_zero +=1
                
        # assign zero elements after non-zero elements
        for i in range(len(nums) - non_zero):
            nums[-1-i] = 0
        
        
