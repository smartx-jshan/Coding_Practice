class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # verify vertical and horizon elements    
        for i in range(9):
            # use hash table
            horizon = collections.defaultdict(int)
            vertical = collections.defaultdict(int)
            for j in range(9):
                horizon[board[i][j]] += 1
                vertical[board[j][i]] += 1
            
                # more than two repeated elements 
                if (board[i][j] != '.' and horizon[board[i][j]] > 1) or (board[j][i] != '.' and vertical[board[j][i]] > 1):
                    return False
                
        # verify sub_box elements
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # use hash table
                sub_box = collections.defaultdict(int)
                for k in range(3):
                    for m in range(3):
                        # more than two repeated elements
                        if board[i+k][j+m] != '.' and sub_box[board[i+k][j+m]] == 1:
                            return False
                        else:
                            sub_box[board[i+k][j+m]] += 1
        # all of elements are satisfied with the rules
        return True
