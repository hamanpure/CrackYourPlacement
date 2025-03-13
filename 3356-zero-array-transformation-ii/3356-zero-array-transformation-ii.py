class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        k = 0
        for q in queries:
            if sum(nums) == 0:
                return k
            l, r, v = q[0], q[1], q[2]
            for a in range(l, r+1):
                if nums[a]!=0 and nums[a] >= v:
                    nums[a] -= v
            k +=1
            
            
        return -1