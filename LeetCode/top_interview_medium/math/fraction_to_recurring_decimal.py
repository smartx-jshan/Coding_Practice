class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        #예외 처리부터
        if numerator == 0:
            return '0'
        
        result = []
        
        #음수 처리
        if (numerator < 0 and denominator > 0) or (numerator >=0 and denominator < 0):
            result.append('-') #마이너스를 붙여줌
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        result.append(str(numerator//denominator)) # 몫을 먼저 추가
        
        remainder = numerator % denominator
        
        if remainder ==0:
            return ''.join(result)
        
        result.append('.')
        
        temp = {}
        
        while remainder != 0:
            if remainder in temp:
                result.insert(temp[remainder], '(')
                result.append(')') # ()을 붙여준다
                return ''.join(result)
            
            temp[remainder] = len(result)
            
            remainder *= 10
            result += str(remainder // denominator)
            remainder = remainder % denominator
            
        return ''.join(result)
        
        
        
