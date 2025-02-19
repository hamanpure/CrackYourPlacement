class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        total_happy = 3*(2**(n-1))

        res = []
        choices = "abc"
        left, right = 1, total_happy

        for i in range(n):
            cur = left
            partion = (right - left + 1)//len(choices)

            for c in choices:

                if k in range(cur, cur+partion):
                    res.append(c)
                    left = cur
                    right = cur+partion - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partion

        return "".join(res)

