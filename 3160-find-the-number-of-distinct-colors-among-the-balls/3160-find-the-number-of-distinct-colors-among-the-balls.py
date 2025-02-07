class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colMap = defaultdict(int)
        revMap = defaultdict(int)

        ans = [0]*len(queries)
        for i in range(len(queries)):
            x, y = queries[i][0], queries[i][1]
            exy = colMap[x]
            if exy in revMap:
                revMap[exy]-=1
                if revMap[exy] ==0:
                    revMap.pop(exy)

            revMap[y]+=1
            colMap[x] = y
            ans[i] = len(revMap)
        
        return ans