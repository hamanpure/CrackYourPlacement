class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(arr)
        rows = len(mat)
        cols = len(mat[0])

        r = [0]*rows
        c = [0]*cols

        m = {}
        for i in range(rows):
            for j in range(cols):
                m[mat[i][j]] = (i, j)

        for a in range(n):
            
            i, j = m[arr[a]]
            r[i] += 1
            c[j] += 1
            if rows in r or cols in c:
                return a
        return -1

            
