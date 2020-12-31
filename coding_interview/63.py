class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_p = 0
        white_p = 0
        blue_p = len(nums)
        white = 1
        
        while white_p < blue_p:
            if nums[white_p] < white:
                nums[white_p], nums[red_p] = nums[red_p], nums[white_p]
                white_p +=1
                red_p +=1
            elif nums[white_p] == white:
                white_p += 1
            else:
                blue_p -= 1
                nums[white_p], nums[blue_p] = nums[blue_p], nums[white_p]
        
        return nums
