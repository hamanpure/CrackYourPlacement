class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashset = {i: 0 for i in nums}
        res = []
        for i in nums:
            hashset[i]+=1
            if hashset[i]>=2:
                res.append(i)
            
        # print(hashset)
        return res