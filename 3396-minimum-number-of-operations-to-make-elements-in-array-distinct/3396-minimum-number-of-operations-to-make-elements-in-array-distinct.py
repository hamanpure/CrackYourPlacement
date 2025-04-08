class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                # All elements are distinct
                break
            # Remove first 3 elements
            nums = nums[3:]
            ops += 1
            
        return ops