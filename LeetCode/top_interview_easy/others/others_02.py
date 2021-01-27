class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        # x XOR y and count '1'
        return bin(x ^ y ).count('1')
    
