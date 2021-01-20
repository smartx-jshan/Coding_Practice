class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # use counter method
        counter = collections.Counter(s)
    
        for index, value in enumerate(s):
            if value in counter and counter[value] ==1:
                return index
        return -1
        
        
