class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
        
        l = 0
        for i in range(len(nums)):
            if nums[l] == 0 and nums[i]!=0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            if nums[l] != 0:
                l+=1
        return nums
        
            