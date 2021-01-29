class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        a = collections.defaultdict(list)
        
        
        for i in strs:
            a["".join(sorted(i))].append(i)
            
        
        result = []
        
        for j in a:
            result.append(a[j])
        return result
        
        
