class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        return n > 0 and pow(3, 31, n) == 0

        
        
        
