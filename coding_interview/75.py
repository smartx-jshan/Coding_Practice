class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        deque = collections.deque()
        results = []
        
        for i, n in enumerate(nums):
            if deque and i - deque[0] == k:
                deque.popleft()
            
            while deque and n > nums[deque[-1]]:
                deque.pop()
            
            deque.append(i)
            
            if i >= k-1:
                results.append(nums[deque[0]])
            
          
                
        return results
                
