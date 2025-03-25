#User function Template for python3
class Solution:
    def countWays(self, s):
        def countWaysUtil(s, i, j, isTrue, dp):
            if i > j:
                return 0
            if i == j:  # Base Case: Single character
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0

            if (i, j, isTrue) in dp:
                return dp[(i, j, isTrue)]

            ways = 0

            for k in range(i + 1, j, 2):  # k is the operator index
                leftTrue = countWaysUtil(s, i, k - 1, True, dp)
                leftFalse = countWaysUtil(s, i, k - 1, False, dp)
                rightTrue = countWaysUtil(s, k + 1, j, True, dp)
                rightFalse = countWaysUtil(s, k + 1, j, False, dp)

                if s[k] == '&':
                    if isTrue:
                        ways += leftTrue * rightTrue
                    else:
                        ways += leftFalse * rightFalse + leftTrue * rightFalse + leftFalse * rightTrue

                elif s[k] == '|':
                    if isTrue:
                        ways += leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        ways += leftFalse * rightFalse

                elif s[k] == '^':
                    if isTrue:
                        ways += leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        ways += leftTrue * rightTrue + leftFalse * rightFalse

            dp[(i, j, isTrue)] = ways
            return ways

        n = len(s)
        dp = {}  # Memoization dictionary
        return countWaysUtil(s, 0, n - 1, True, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends