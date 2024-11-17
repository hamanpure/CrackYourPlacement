class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, h = 0, len(s)-1
        while l<=h:
            if s[l] != s[h]:
                return (s[l+1:h+1] == s[l+1:h+1][::-1] or s[l:h] == s[l:h][::-1] )
            l+=1
            h-=1
        return True