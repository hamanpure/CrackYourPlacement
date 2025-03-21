class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
    
        # Initialize previous values
        prev2 = arr[0]  # Looting only the first house
        prev1 = max(arr[0], arr[1])  # Max of first two houses
    
        for i in range(2, n):
            current = max(prev1, arr[i] + prev2)  # Choose to loot or skip
            prev2 = prev1
            prev1 = current
    
        return prev1  # Maximum loot possible

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends