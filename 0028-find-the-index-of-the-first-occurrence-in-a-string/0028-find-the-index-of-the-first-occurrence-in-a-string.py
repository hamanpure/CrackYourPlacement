class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        h= len(needle)-1
        while h<len(haystack):
            if haystack[l:h+1] == needle:
                return l
            l+=1
            h+=1
        return -1