class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #일단 최소값을 찾자
        
        if not nums:
            return -1
        
        left = 0
        right = len(nums) -1
        
        while left< right:
            mid = left + (right -left) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left) //2
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid-1
            else:
                return mid_pivot
        
        return -1
