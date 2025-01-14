class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        f = [0]*(len(A)+1)
        c = 0
        for i in range(len(A)):
            f[A[i]] += 1
            f[B[i]] += 1

            
            if f[A[i]] > 1:
                c += 1
            if f[B[i]] > 1:
                c+=1
            if A[i] == B[i]:
                c-=1

            ans.append(c)
        return ans

        
        return ans
            