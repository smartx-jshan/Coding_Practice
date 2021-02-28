class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # 백트레킹
        result = []
        
        def backtrack(S= '', left = 0, right = 0):
            if len(S) == 2 * n: #N만큼 괄호가 붙여졌으면 append
                result.append(S)
                return
            
            if left < n: #n보다 작으면 계속 왼쪽 괄호 추가
                backtrack(S+'(', left+1, right)
            if right < left: #그리고 왼쪽 괄호가 추가되었을때는 오른쪽 괄호도 추가
                backtrack(S+')', left, right+1)
        
        backtrack()
        
        return result
            
