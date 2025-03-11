class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l = 0
        res = 0
        count = [0]*3

        for r in range(n):
            count[ord(s[r]) - ord('a')]+=1

            while count[0] and count[1] and count[2]:
                res += (n-r)
                count[ord(s[l]) - ord('a')] -= 1
                l+=1
        return res