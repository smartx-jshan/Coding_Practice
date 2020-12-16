class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewels = collections.defaultdict(int)
        
        count = 0
        
        for char in S:
            jewels[char] += 1
        
        for char in J:
            count = count + jewels[char]
            
        return count
