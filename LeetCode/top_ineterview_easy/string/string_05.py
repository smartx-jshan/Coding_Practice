class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # lower character
        s = s.lower()
        
        # only alphanumeric charcter
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
        
