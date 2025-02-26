class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a, b = len(s), len(t)

        i, j = 0, 0
        c = a
        while i < a and j < b:
            if s[i] == t[j]:
                c -= 1
                i+=1
            j+=1

        return c == 0 
            
            
            
