class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            
            # Check if the left portion is sorted
            if nums[low] <= nums[mid]:
                # If the target lies in the sorted left portion
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right portion must be sorted
            else:
                # If the target lies in the sorted right portion
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        # If the target is not found
        return -1
