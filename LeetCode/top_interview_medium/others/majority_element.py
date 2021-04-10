class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num_count = collections.defaultdict(int) #각 엘리먼트의 개수를 저장
        max_size = 1 #초기 사이즈와 answer를 저장
        answer = nums[0]
        
        for element in nums: 
            num_count[element] += 1 
            if num_count[element] > max_size: #저장한 엘리먼트가 현재 누적 엘리먼트 개수 사이즈보다 큰 경우
                answer = element #값을 갱신
                max_size +=1
                
        return answer
        
        
    
