class Solution:
    def isHappy(self, n: int) -> bool:
        
        number = n
        memorize = collections.defaultdict(int)
        
        memorize[n] += 1
        
        while True:
            sum = 0
            for i in str(number):
                sum += int(i) *int(i)
            
            if sum == 1:
                return True
            
            # sum이 이전 결과에 있는 경우
            if sum in memorize:
                return False
            else: #아니면 넣는다
                memorize[sum] +=1 
           
            number = sum
            
            
        
        
