class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        R, C = len(heights), len(heights[0])
        def dfs(r, c, v, prev):
            if (r<0 or c<0 or r>=R or c>=C or (r, c) in v or heights[r][c] < prev):return

            v.add((r, c))
            dfs(r+1, c, v, heights[r][c])
            dfs(r-1, c, v, heights[r][c])
            dfs(r, c+1, v, heights[r][c])
            dfs(r, c-1, v, heights[r][c])
        
        for c in range(C):
            dfs(0, c, pacific, heights[0][c])
            dfs(R-1, c, atlantic, heights[R-1][c])

        for r in range(R):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, C-1, atlantic, heights[r][C-1])
        
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
