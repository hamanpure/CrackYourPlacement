class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res = 0
        targetsetbits = bin(num2).count("1")

        for i in range(31, -1, -1):
            if targetsetbits > 0:
                if (num1 & (1<<i)):
                    res |= (1<<i)
                    targetsetbits-=1
           

        for i in range(32):
            if targetsetbits > 0:
                if not (res & (1<<i)):
                    res |= (1<<i)
                    targetsetbits-=1
               
       
        return res

         