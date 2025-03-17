class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always achievable
        
        for num in arr:
            for j in range(target, num - 1, -1):  # Iterate backwards
                dp[j] = dp[j] or dp[j - num]
    
        return dp[target]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends