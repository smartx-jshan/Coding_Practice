class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        left_pointer = 0
        right_pointer = len(height)-1
        left_max = height[left_pointer]
        right_max = height[right_pointer]
        
        vol = 0
        
        while (left_pointer < right_pointer):
            left_max = max(height[left_pointer],left_max)
            right_max = max(height[right_pointer],right_max)
            if (left_max <= right_max):
                vol = vol + left_max - height[left_pointer]
                left_pointer = left_pointer + 1
            else:
                vol = vol + right_max -height[right_pointer]
                right_pointer = right_pointer - 1
        return vol
