class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequent = collections.Counter(nums) #값을 카운터하고
        
        heap = []
        
        for i in frequent:
            heapq.heappush(heap, (-frequent[i], i)) #힙에 저장, 힙에 저장시 음수 값으로 저장
            
        #print (heap)
        
        result = []
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
