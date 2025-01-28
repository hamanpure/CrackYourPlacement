#User function Template for python3

class Solution:
    def solve(self, i, n, s, permu, st):
        if len(permu) == n:
            st.add(permu)
            return

        for j in range(i, n):
            # Swap characters in the string
            s = list(s)
            s[i], s[j] = s[j], s[i]
            s = ''.join(s)

            self.solve(i + 1, n, s, permu + s[i], st)

            # Backtrack by swapping back
            s = list(s)
            s[i], s[j] = s[j], s[i]
            s = ''.join(s)
            
    def findPermutation(self, s):
        # Code here
        st = set()
        permu = ""
        n = len(s)
        self.solve(0, n, s, permu, st)
        return list(st)




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends