class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        n = len(s)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if s[j] > s[j + 1]:  # Swap for descending order
                    s[j], s[j + 1] = s[j + 1], s[j]
    




#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


        print("~")
# } Driver Code Ends