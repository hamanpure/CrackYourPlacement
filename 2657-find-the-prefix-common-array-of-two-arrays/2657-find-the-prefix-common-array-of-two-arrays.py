class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        b_set = set()
        for i in range(len(A)):
            c = 0 
            b_set.add(B[i])
            for j in range(i+1):
                if A[j] in b_set:
                    c += 1
            ans.append(c)
        return ans
            