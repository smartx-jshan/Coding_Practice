class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        result = []
        
        for i in points:
            dist = math.sqrt((0-i[0])**2 + (0-i[1])**2)
            heapq.heappush(heap,(dist, i[0], i[1]))
        
        print (heap)
        
        for _ in range (K):
            dist, x, y= heapq.heappop(heap)
            result.append([x,y])
        
        return result
