class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Step 1: If any number is less than k, return -1
        if any(num < k for num in nums):
            return -1

        # Step 2: Get all unique numbers greater than k
        greater_than_k = set(num for num in nums if num > k)

        # Step 3: Count them — each one takes an operation
        return len(greater_than_k)