class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])

        x = sum(grid[0][1:])
        y = 0

        res = x
        for i in range(cols-1):
            x -= grid[0][i+1]
            y += grid[1][i]
            a = max(x, y)
            if res>=a:
                res = a
            else:
                break
        return res