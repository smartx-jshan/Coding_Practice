class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #먼저 정렬하자
        
        intervals.sort(key=lambda x: x[0])
        
        result = []
        
        for i in intervals:
            if not result or result[-1][1] < i[0]: #새롭게 넣을 범위가 이전 범위에 벗어나면
                result.append(i)
            else:
                
                result[-1][1] = max(result[-1][1], i[1])
        
        return result
                    
        
