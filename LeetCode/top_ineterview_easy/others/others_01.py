class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        # bin(x) is binary translation 
        for i in bin(n):
            if i == '1':
                count += 1
        return count
