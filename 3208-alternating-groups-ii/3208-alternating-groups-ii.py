class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        if k > n:
            return 0
        non_alternating = 0

        for i in range(1, k):
            if colors[i-1] == colors[i]:
                non_alternating +=1
        
        c = 1 if non_alternating == 0 else 0

        for i in range(1, n):
            if colors[i-1] == colors[i]:
                non_alternating -= 1
            
            if colors[(i+k-2)%n] == colors[(i+k-1)%n]:
                non_alternating +=1

            if non_alternating == 0:
                c+=1
        return c
        