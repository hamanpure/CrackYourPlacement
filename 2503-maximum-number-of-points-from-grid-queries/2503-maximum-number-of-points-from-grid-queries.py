from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid, queries):
        m, n = len(grid), len(grid[0])
        k = len(queries)
        
        # Sort queries and keep track of their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        # Result array
        result = [0] * k
        
        # Min-Heap: Store (grid value, row, col)
        heap = [(grid[0][0], 0, 0)]
        
        # Visited set
        visited = set()
        visited.add((0, 0))
        
        # Directions for movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Count of cells we can visit
        points = 0
        
        # Process queries in sorted order
        for idx, query in sorted_queries:
            while heap and heap[0][0] < query:
                value, r, c = heappop(heap)
                points += 1  # We can visit this cell
                
                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        heappush(heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            
            result[idx] = points  # Store result in the original query order
        
        return result
