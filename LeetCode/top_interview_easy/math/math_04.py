class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Total number
        number = 0
        
        # current chracters (compare with next chracters)
        cur = 0
        for i in s:
            if i == 'M':
                # in case of 900
                if cur == 100:
                    number = number - cur - cur
                number = number + 1000
                cur = 1000
            elif i =='D':
                # in case of 400
                if cur ==100:
                    number = number - cur - cur
                number = number + 500
                cur = 500
            elif i == 'C':
                # in case of 90
                if cur == 10:
                    number = number - cur - cur
                number = number + 100
                cur = 100
            elif i == 'L':
                # in case of 40
                if cur == 10:
                    number = number - cur - cur
                number = number + 50
                cur = 50
            elif i == 'X':
                # in case of 9
                if cur == 1:
                    number = number - cur - cur
                number = number + 10
                cur = 10
            elif i == 'V':
                # in case of 4
                if cur == 1:
                    number = number - cur -cur
                number = number + 5
                cur = 5
            elif i == 'I':
                number = number + 1
                cur = 1
        
        return number
