#User function Template for python3
from functools import lru_cache
class Solution:
	def countWays(self, digits):
		# Code here
		n = len(digits)
        if n == 0:
            return 0  # Edge case: empty string

        @lru_cache(None)
        def solve(i):
            if i == n:
                return 1
            if digits[i] == '0':  # Can't decode '0' alone
                return 0
            
            # One-digit decoding
            one = solve(i + 1)
            
            # Two-digit decoding (10-26 range)
            two = 0
            if i < n - 1 and (digits[i] == '1' or (digits[i] == '2' and digits[i + 1] <= '6')):
                two = solve(i + 2)
            
            return one + two

        return solve(0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends