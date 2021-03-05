class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [] #힙에 넣기
        
        for i in nums:
            heapq.heappush(heap, -i)
            
        
        result = 0
        for i in range(k): #K번째 수를 뺐을 때 값을 저장
            result = -heapq.heappop(heap)
        
        return result
