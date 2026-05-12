class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        q = deque()
        v = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append([r, c])
                    v.add((r, c))

        def addCell(r, c):
            if (r<0 or c<0 or r>=R or c>=C or grid[r][c]==-1 or (r, c) in v): return

            v.add((r, c))
            q.append([r, c])

        
        d = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = d
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            d += 1
        

