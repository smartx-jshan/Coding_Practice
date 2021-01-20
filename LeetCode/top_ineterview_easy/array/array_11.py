class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        
        size = len(matrix)
        
        # roate four ractangles
        for i in range (size //2 + size %2):
            for j in range (size // 2):
                row, col = i, j
                tmp = [0] *4
                
                # copy 4 elements to tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, size-1-row
                
                # rotate 4 elements
                for k in range(4):
                    matrix[row][col] = tmp[(k-1) % 4]
                    row, col = col, size-1-row
        
                
