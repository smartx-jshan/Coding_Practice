class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
     
     
        size = len(nums)
        
        # reduce k <= n
        k %= size
        
        count = 0
        start = 0
        
        while count < size:
            i = start
            temp = nums[start]
        
            while True:
                
                index = (i+k) % size
                
                nums[index], temp = temp, nums[index]
                i = index
                count += 1
                
                # check cycle
                if i == start:
                    break
            # move to start point
            start +=1
        
            
        
        
