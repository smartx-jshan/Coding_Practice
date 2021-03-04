class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        def dfs (i, j, index):
            
            if index >= len(word): #끝까지 한거면
                return True
            
            if i >=0 and i<len(board) and j >=0 and j<len(board[0]): #범위 조건에 부합하면
                
                if board[i][j] == word[index]: #단어가 맞으면
            
                    origin = board[i][j] #해당 포인트를 임시로 저장하고
                    board[i][j] = '0' #해당포인트를 탐색했다고 마킹
                    if dfs(i, j+1, index+1):
                        return True
                    if dfs(i, j-1, index+1):
                        return True
                    if dfs(i+1, j, index+1):
                        return True
                    if dfs(i-1, j, index+1):
                        return True
                    
                    board[i][j] = origin #해당 포인트를 복구
                    
                else: #범위 조건에 부합하지 않으면
                    return False
                    
                
            else: #범위 조건에 안맞으면
                return False
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == word[0]: #일단 첫 단어가 맞으면 dfs로 간다
                    #origin = board[i][j] #해당 값을 가지고 있다가
                    #board[i][j] = '0' # 0으로 마킹한다
                    answer = dfs (i,j, 0)
                    #print (check_board)
                    if answer == True:

                        return True
                    #board[i][j] = origin #해당 값을 복구함
                
        
        return False
