class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        visited = set()
        traced = set()
        
        def dfs(x):
            if x in traced:
                return False
            if x in visited:
                return True
            
            traced.add(x)
            
            for y in graph[x]:
                if not dfs(y):
                    return False
            visited.add(x)
            traced.remove(x)
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
        return True
        
