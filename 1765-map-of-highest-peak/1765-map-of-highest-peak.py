class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])

        res = [[0]*cols for _ in range(rows)]

        q = deque()
        visit = set()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]:
                    q.append((i,j))
                    visit.add((i,j))
                    res[i][j] = 0
        
        #BFS
        while q:
            r, c = q.popleft()
            h = res[r][c]

            neighbour = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]

            for nr, nc in neighbour:
                if (
                    nr<0 or nc<0 or 
                    nr == rows or nc == cols or
                    (nr, nc) in visit
                ):
                    continue
                
                q.append((nr, nc))
                visit.add((nr, nc))
                res[nr][nc] = h+1
        return res