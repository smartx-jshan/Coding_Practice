class Solution:
    def myAtoi(self, s: str) -> int:
        
        # 2^31-1 , -2^31 definition
        max_plus = 2147483647 
        max_minus = -2147483648
        
        # first word
        words = str(s).split()
        
        # exception
        if len(words) == 0:
            return 0
        
        
        word = words[0]
        
        ops = 0 # default 0 
        # ops checking 
        if word[0] == '-':
            ops = 1
            word = word[1:]
        elif word[0] == '+':
            word = word[1:]
        
        # we append sucessful elements (0-9, '.')
        result = []
        
        for i in word:
            # number?
            if i.isdigit():
                result.append(i)
            # . ?
            elif i == '.':
                result.append(i)
            else:
                break
                
        # if result is None
        if len(result) == 0:
            return 0
        
        # list to number, float to int
        number = ''.join(result)
        number = int(float(number))
        
        # if have minus ops
        if ops == 1:
            number = -number
        
        
        if max_plus <= number:
            return max_plus
        if max_minus >= number:
            return max_minus
        return number
        
        
        
        
        
        
        
        
