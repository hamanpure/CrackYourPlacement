class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            s = str(i)
            if len(s) % 2 != 0:
                continue
            s1 = sum(int(d) for d in s[:len(s)//2])
            s2 = sum(int(d) for d in s[len(s)//2:])
            if s1==s2:
                count+=1
        return count


