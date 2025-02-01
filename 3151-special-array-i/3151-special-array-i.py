class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        
        for i in range(1, len(nums)):
            if nums[i-1]%2 == 0 and nums[i]%2==0:
                return False
            if nums[i-1]%2 != 0 and nums[i]%2!=0:
                return False
        return True