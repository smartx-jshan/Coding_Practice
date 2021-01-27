class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        #table create
        table = { ')':'(', '}':'{', ']':'['}
        
        for char in s:
            if not char in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        
        if len(stack) == 0:
            return True
