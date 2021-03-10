class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        value = len(nums)-1 #그리디 방법 활용
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= value:
                value = i
        
        if value == 0:
            return True
        else:
            return False
