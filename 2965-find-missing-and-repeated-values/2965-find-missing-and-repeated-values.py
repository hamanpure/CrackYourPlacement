class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        r = len(grid)
        c = len(grid[0])
        mp = {}
        res = []
        for i in range(r):
            for j in range(c):
                mp[grid[i][j]] = mp.get(grid[i][j], 0) + 1
        
        for k, v in mp.items():
            if v > 1:
                res.append(k)
                break

        for i in range(1,r*c+1):
            if i not in mp:
                res.append(i)
                break
                
        return res
