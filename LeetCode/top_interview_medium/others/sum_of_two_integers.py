class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # bit operation
        mask = 0xffffffff 
        
        while ( b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
            
        if b > 0:
            return a & mask
        else:
            return a
