class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = sys.maxsize
        second = sys.maxsize
        
        for i in nums:
            if i > second: #second 보다 크면 true이다
                return True
            else:
                if i > first: #first 보다 크면 second를 갱신한다
                    second = i
                else:
                    first = i # first 보다 작으면 first를 갱신한다
                    
        #여기까지 왔으면 모두 검색했으므로 false를 리턴
        return False
        
