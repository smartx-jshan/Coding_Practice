class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # panlindrome check
        def expand(left: int, right: int) -> str:
            while left >=0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left +1: right -1]
        
        # skip in case of exception
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        
        # O(n) * expand O(n) = O(n2)
        for i in range (len(s) -1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result
