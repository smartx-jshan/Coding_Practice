class Solution:
    def reverse(self, x: int) -> int:
        
        number = 0
        # minus check
        minus = 0
        # 10^index (exp)
        index = 0
        for i in str(x):
            # minus keeping
            if i == '-':
                minus = 1
            # accumulate number 
            else:
                number = number + (10**index *int(i))
                index +=1
        
        # minus check
        if minus == 1:
            number = -number
        
        #32bit interger check
        if -(2**31) <= number <= (2**31 -1):
            return number
        
        return 0
