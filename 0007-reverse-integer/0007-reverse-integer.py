class Solution:
    def reverse(self, x: int) -> int:
        
        res = 0
        c = 1
        if x<0:
            x = -x
            c = -1

        while x>0:
            res = res*10+x%10
            x = x//10
        
        res = res*c
        if (res<(-2**31) or res> (2**31 - 1)):
            return 0
        return res
