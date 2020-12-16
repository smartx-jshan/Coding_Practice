class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dict = {}
        count = 0
        start_index = 0
        
        for i in range (len(s)):
            if s[i] in dict and start_index <= dict[s[i]]:
                start_index = dict[s[i]] +1
            else:
                count = max (count, i-start_index + 1)
            dict[s[i]] = i
        
        return count
