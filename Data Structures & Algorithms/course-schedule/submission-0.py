class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)

        v = set()

        def dfs(c):
            if c in v: return False
            if not graph[c]: return True

            v.add(c)
            
            for p in graph[c]:
                if not dfs(p): return False
            
            v.remove(c)
            graph[c] = []
            return True 

        for c in range(numCourses):
            if not dfs(c): return False

        return True 