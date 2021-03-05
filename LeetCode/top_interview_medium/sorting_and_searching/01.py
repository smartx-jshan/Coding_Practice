class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red_pointer = 0
        blue_pointer = len(nums)
        white_pointer = 0
        
        while white_pointer < blue_pointer:
            
            if nums[white_pointer] < 1: #red면
                nums[red_pointer], nums[white_pointer] = nums[white_pointer], nums[red_pointer]
                white_pointer +=1
                red_pointer +=1
            elif nums[white_pointer] > 1: #blue 값이면
                blue_pointer -=1
                nums[white_pointer], nums[blue_pointer] = nums[blue_pointer], nums[white_pointer]
                
            else:
                white_pointer +=1
        
