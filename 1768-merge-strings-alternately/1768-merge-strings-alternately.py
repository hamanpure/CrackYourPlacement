class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n1, n2 =  len(word1), len(word2)
        i, j = 0, 0
        while i<n1 and j< n2:
            res += word1[i] + word2[j]
            i+=1
            j+=1
        
        if i<n1:
            res += word1[i:]
        if j<n2:
            res+= word2[j:]
        return res
