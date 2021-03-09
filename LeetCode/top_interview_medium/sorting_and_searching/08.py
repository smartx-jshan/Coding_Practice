class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        
        row = 0
        col = len(matrix[0]) -1
        
        while row <= len(matrix)-1 and col >=0: 
            #전략은 맨 첫 행 맨 오른쪽부터 비교해가면서 간다
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target: #매트릭스 값이 타겟보다 크면
                #col을 줄인다
                col -=1
            else: #매트릭스 값이 타겟보다 작으면
                #row를 늘린다
                row +=1
        return False
                
