class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        l, r = 0, k

        mini = float("inf")
        while r<=n:
            c = 0
            for i in blocks[l:r]:
                if i == "W":
                    c+=1
            mini = min(c, mini)
            l+=1
            r+=1
        return mini

