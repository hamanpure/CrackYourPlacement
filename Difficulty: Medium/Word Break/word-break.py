#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        dp = [0]*(len(s)+1)
        
        dp[len(s)] = 1
        
        for i in range(len(s) - 1, -1, -1 ):
            for w in dictionary:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break 
        return dp[0]
                

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        n = int(input())
        dictionary = [word for word in input().strip().split()]
        s = input().strip()
        ob = Solution()
        res = ob.wordBreak(n, s, dictionary)
        if res:
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends