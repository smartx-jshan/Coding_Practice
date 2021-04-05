class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0: #0일때는 예외처리
            return 0
        
        # 이진 검색 기법을 활용하여 탐색
        left = 1
        right = x-1
        
        temp = x -1 # mid가 일정한 값으로 수렴되는 경우가 있음. 이를 판별하기 위한 변수
        
        while left <= right:
        
            mid = left + ((right-left) // 2)
            if temp == mid:
                return mid
            temp = mid
            #print (mid)
            if mid* mid < x: # 곱한 값이 x보다 작으면
                left = mid
            elif mid* mid > x: #곱한 값이 x보다 크면
                right = mid
            else: #맞으면
                return mid
        
            
        return left
