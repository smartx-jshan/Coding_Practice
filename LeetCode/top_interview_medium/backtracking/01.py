class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs (index, path):
            
            if len(path) == len(digits): #끝까지 했으면
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in phone[digits[i]]:
                    dfs(i+1, path + j)
            
        if not digits:
            return []
        
        
        
        phone = {}
        phone['2'] = ['a','b','c']
        phone['3'] = ['d','e','f']
        phone['4'] = ['g','h','i']
        phone['5'] = ['j','k','l']
        phone['6'] = ['m','n','o']
        phone['7'] = ['p','q','r','s']
        phone['8'] = ['t','u','v']
        phone['9'] = ['w','x','y','z']
        
        result = []
        
        dfs(0, "")
        return result
            
