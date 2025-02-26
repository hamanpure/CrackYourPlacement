class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        c = len(s)
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                c -= 1
                i+=1
            j+=1

        return c == 0 
            
            
            
