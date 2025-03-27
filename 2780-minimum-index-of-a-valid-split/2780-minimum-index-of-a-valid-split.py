from collections import Counter

class Solution:
    def minimumIndex(self, nums):
        # Step 1: Find the dominant element using Boyer-Moore Majority Voting Algorithm
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Step 2: Verify the dominant element
        total_count = nums.count(candidate)  # Count occurrences of the candidate
        if total_count * 2 <= len(nums):  
            return -1  # Shouldn't happen as per problem statement

        # Step 3: Find the minimum valid split index
        left_count = 0
        for i in range(len(nums) - 1):  # Can't split at the last index
            if nums[i] == candidate:
                left_count += 1
            right_count = total_count - left_count  # Remaining count in the right half
            
            # Check if it's dominant in both halves
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - (i + 1)):
                return i  # Return the first valid split index

        return -1  # No valid split found