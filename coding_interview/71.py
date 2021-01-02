class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        x = bin(x^y)
        print (x.count('1'))
        return x.count('1')
