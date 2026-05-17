class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            d[c].append(p)

        visited = set()

        def dfs(c):
            if c in visited: return True

            visited.add(c)
            for p in d[c]:
                if dfs(p): return True
            
            visited.remove(c)

            return False
        
        for c in range(numCourses):
            if dfs(c): return False
        
        return True