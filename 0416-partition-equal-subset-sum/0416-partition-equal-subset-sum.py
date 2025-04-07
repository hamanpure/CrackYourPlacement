class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        # If sum is odd, we can't partition it equally
        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # base case: zero sum is always possible

        for num in nums:
            # Iterate backwards to avoid using the same number twice
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[target]
