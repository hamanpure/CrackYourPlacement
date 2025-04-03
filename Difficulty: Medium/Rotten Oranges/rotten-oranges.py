from collections import deque

class Solution:
    def orangesRotting(self, mat):
        if not mat:
            return -1
        
        n, m = len(mat), len(mat[0])
        queue = deque()
        fresh_oranges = 0
        
        # Step 1: Add all rotten oranges to queue & count fresh oranges
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif mat[i][j] == 1:
                    fresh_oranges += 1
        
        # Step 2: BFS from rotten oranges
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time_elapsed = 0
        
        while queue:
            i, j, time = queue.popleft()
            time_elapsed = max(time_elapsed, time)
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                # If it's a fresh orange, rot it
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 1:
                    mat[ni][nj] = 2  # Rot it
                    fresh_oranges -= 1
                    queue.append((ni, nj, time + 1))  # Add new rotten orange
        
        # If there are still fresh oranges left, return -1
        return time_elapsed if fresh_oranges == 0 else -1


#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends