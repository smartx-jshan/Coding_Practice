class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2**31 and divisor == -1:
            return 2 ** 31 - 1 #예외 처리
        
        
        quotient = 0
        check = 1
        
        if dividend * divisor < 0:
            check = -1 #음수
            
        dividend = abs(dividend) #절대값
        divisor = abs(divisor)
        
        while dividend - divisor >=0:
            x = 0
            while dividend - (divisor << 1 << x) > 0:
                x += 1
            dividend -= (divisor << x)
            quotient += (2**x)
        quotient *= check
        
        return quotient
        
