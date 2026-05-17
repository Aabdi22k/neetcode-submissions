class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = 0
        graph = {i: [] for i in range(n)}
        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)

        visited = set()

        def dfs(v):
            if v in visited: return
            visited.add(v)
            for e in graph[v]:
                dfs(e)
            
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                cc += 1
        
        return cc
        