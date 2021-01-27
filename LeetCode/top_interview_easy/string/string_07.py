class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # exception
        # both haystack and needle are ""
        if haystack =="" and needle == "":
            return 0
        # only needle is ""
        if haystack !="" and needle =="":
            return 0
        
        # split with needle
        words = haystack.split(needle)
        
        # the first splited word is words[0]
        
        # fail the split with needle (it means words[0] is same as haystack)
        if len(words[0]) == len(haystack):
            return -1
        
        # else return length of words[0]
        return len(words[0])
