class Solution:
    def wordBreak(self, s, dictionary):
        word_set = set(dictionary)  # Convert list to set for O(1) lookup
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string is always valid

        for i in range(1, n + 1):  # Iterate over the string length
            for j in range(max(0, i - max(map(len, dictionary))), i):  # Check only relevant substrings
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Stop early if a valid segmentation is found
        
        return dp[n]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends