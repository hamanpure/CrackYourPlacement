class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        row_count = [0]*rows
        col_count = [0]*cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    row_count[i] +=1
                    col_count[j] +=1
        c = 0            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    if row_count[i] > 1 or col_count[j] > 1:
                        c+=1

        return c
