class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.Counter(nums)
        heap = []
        result = []
        for i in count:
            heapq.heappush(heap, (-count[i], i))
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
