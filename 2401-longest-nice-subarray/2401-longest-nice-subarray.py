class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        bitmask = 0
        max_length = 0

        for right in range(len(nums)):
            # If there's a bitwise conflict, move left pointer
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]  # Remove nums[left] from bitmask
                left += 1  # Shrink window

            # Add nums[right] to bitmask
            bitmask |= nums[right]

            # Update max length
            max_length = max(max_length, right - left + 1)

        return max_length