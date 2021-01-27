class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result = []
        
        # set can reduce duplicated value
        set_x = set()
        set_y = set()
        
        
        # find x, y with value = 0
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                
                # zero 
                if matrix[i][j] == 0:
                    set_x.add(i)
                    set_y.add(j)
                    
        # for x, y with value = 0
        
        for i in set_x:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
            
        for j in set_y:
            for k in range(len(matrix)):
                matrix[k][j] = 0
                
                
        
