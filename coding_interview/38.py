class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # graph creation
        
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        print (graph)
        
        results = []
        
        def dfs (v):
            
            while graph[v]:
                dfs (graph[v].pop(0))
            results.append(v)
            
                
        
        dfs('JFK')
        return results[::-1]
