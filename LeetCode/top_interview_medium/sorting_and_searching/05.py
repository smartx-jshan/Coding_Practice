class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        index_start = -1
        index_end = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                if index_start < 0 or nums[index_start] != target: #시작점도 세팅되있다면
                    #print ("here")
                    index_start = i
                    index_end = i
                else: #시작점이 세팅안되어있다면
                    index_end = i
        
        return [index_start, index_end]
        
