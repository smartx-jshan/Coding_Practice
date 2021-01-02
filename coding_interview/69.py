class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        col = len(matrix[0]) -1
        row_max = len(matrix)
        row = 0
        
        while row < row_max and col >=0 :
            if matrix[row][col] < target:
                row +=1
            elif matrix[row][col] > target:
                col -=1
            else:
                return True
        return False
