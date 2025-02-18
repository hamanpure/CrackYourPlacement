class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O','U','a','e','i','o','u'}
        v=[]
        for i in range(len(s)):
            if s[i] in vowels:
                v.append(s[i])
        
        v = v[::-1]
        res = ""
        i = 0
        for j in s:
            if j in vowels:
                res+=v[i]
                i+=1
            else:
                res+=j
        return res


