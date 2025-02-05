class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        p = 0
        d = {}
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                p+=1
            d[s1[i]] = d.get(s1[i], 0) + 1
        for i in range(len(s2)):
            if s2[i] not in d:
                return False
            d[s2[i]] -=1
        for i in d.values():
          if i>0:
            return False
        if sum(d.values()) == 0 and p == 0 or p == 2:
            return True
        return False
        