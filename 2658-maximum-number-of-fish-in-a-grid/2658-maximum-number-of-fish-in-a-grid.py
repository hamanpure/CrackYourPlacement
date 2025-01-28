class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r< 0 or c< 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0 or visit[r][c]
            ):
                return 0
            visit[r][c] = True
            res = grid[r][c]
            neighbors = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
            for nr, nc in neighbors:
                res += dfs(nr, nc)
            return res
        ROWS, COLS = len (grid), len(grid[0])
        res = 0
        visit = [[False] * COLS for _ in range (ROWS)]
        for r in range (ROWS):
            for c in range(COLS):
                if grid[r][c] or not visit[r][c]:
                    res = max(res, dfs(r, c))
        return res