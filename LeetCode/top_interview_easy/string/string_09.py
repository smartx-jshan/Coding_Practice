class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # exception
        if len(strs) == 0:
            return ""
        
        # sort first!
        strs.sort()
        # strategy
        # compare first and last string in sorted strings!
        
        # pick first element in strs
        pick = strs[0]
        prefix = ''
        
        for i in range (len(pick)):
            if strs[len(strs)-1][i] == pick[i]:
                prefix += strs[len(strs)-1][i]
            else:
                break
        return prefix
