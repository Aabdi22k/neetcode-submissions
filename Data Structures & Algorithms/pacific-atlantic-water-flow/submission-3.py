class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        p, a = set(), set() 
        ROWS , COLS = len(heights), len(heights[0])

        def dfs(r, c, ocean, prev):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prev or (r, c) in ocean): return

            ocean.add((r, c))
            dfs(r+1, c, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, p, heights[0][c])
            dfs(ROWS - 1, c, a, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, p, heights[r][0])
            dfs(r, COLS - 1, a, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in p and (r, c) in a:
                    res.append([r, c])
        return res

            

