class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        d = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for i in s:
            stack.append(i)
            #print(stack)
            if i in d:
                if d[i] in stack and d[i] == stack[-2]:
                    stack.pop()
                    stack.pop()
           
        if len(stack) ==0:
            return True
        return False