class Solution:
    def minimumLength(self, s: str) -> int:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i,0) + 1
        
        res = 0
        for i in hashmap.values():
            c = i
            while c>=3:
                c-=2
            res+=c
        
        return res