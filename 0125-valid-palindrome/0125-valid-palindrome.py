class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        s = s.lower()
        a = 'abcdefghijklmnopqrstuvwxyz123456789'
        for i in s:
            if i in a:
                ss+=i
        return ss == ss[::-1]