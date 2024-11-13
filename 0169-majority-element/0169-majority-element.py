class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums)/2
        hashmap = {i: 0 for i in nums}
        mcount = k
        for i in nums:
            hashmap[i]+=1
            if hashmap[i]>=mcount:
                res = i
                mcount = max(mcount,hashmap[i])
        return res

