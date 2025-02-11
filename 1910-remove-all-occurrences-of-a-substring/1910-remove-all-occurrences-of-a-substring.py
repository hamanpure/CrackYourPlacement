class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack = []
        n = len(part)

        for i in s:
            stack.append(i)

            if len(stack)>=n:
                if "".join(stack[-n:]) == part:
                    j = n
                    while j>0:
                        stack.pop()
                        j-=1
        return "".join(stack)