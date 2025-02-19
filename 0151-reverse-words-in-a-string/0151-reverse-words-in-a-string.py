class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = s.split()

        return " ".join(res[::-1])