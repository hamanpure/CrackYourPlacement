class Solution:
    def maxProfit(self, prices, k):
        # code here
        n = len(prices)
        if n == 0 or k == 0:
            return 0
    
        # If k is very large, problem reduces to unlimited transactions case
        if 2 * k > n:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
    
        # DP table
        dp = [[0] * n for _ in range(k + 1)]
    
        for i in range(1, k + 1):
            max_diff = -prices[0]  # Equivalent to max(dp[i-1][m] - prices[m])
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
    
        return dp[k][n-1]
    

#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends