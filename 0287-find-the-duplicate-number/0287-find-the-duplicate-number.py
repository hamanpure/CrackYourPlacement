class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=abs(nums[i])
            if nums[x-1]<0:
                return x
            nums[x-1]=-nums[x-1]