#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        count = 0

        # All 8 directions (horizontal, vertical, diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 'L':
                return
            grid[i][j] = 'V'  # Mark as visited
            for dx, dy in directions:
                dfs(i + dx, j + dy)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L':
                    count += 1
                    dfs(i, j)

        return count

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends