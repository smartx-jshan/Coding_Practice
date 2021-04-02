class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        offset = 64 #아스키코드의 오프셋
        
        #print (ord('Z') -offset) #대문자에 한정한 숫자 매핑 공식
        
        size = len(columnTitle) - 1 #곱할 지수를 먼저 구한뒤
        
        sum = 0
        for i in columnTitle:
            sum = sum + (ord(i) - offset) * (26**size)
            size -=1 #곱할 지수를 감소
        
        return sum
