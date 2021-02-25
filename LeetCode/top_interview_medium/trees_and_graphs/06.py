class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        def dfs(i,j,m,n): #네 방향의 섬 진행해야 함
            
            if i < 0 or i>=m or j < 0 or j>=n: #범위 밖이면
                return 0#그냥 리턴
            
            
            # 범위 안에 있으면
            if grid[i][j] == "1":#있으면
                grid[i][j] ="0" #0으로 만들고
                
                #동서남북 다 들어간다
                dfs(i-1,j,m,n)
                dfs(i+1,j,m,n)
                dfs(i,j-1,m,n)
                dfs(i,j+1,m,n)
                
                return 1 #마지막에 1을 추가
                
            else: # 0이면
                return 0
                
        
        m = len(grid) # Y축
        n = len(grid[0]) # X 축
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += dfs(i,j, m,n)
        
        return count
