class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 5단위로 뒷자리 0의 개수가 늘어남
        
        if n == 0:
            return 0
        
        return (n//5) + self.trailingZeroes(n//5)
        
