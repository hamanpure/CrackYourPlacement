class Solution:
    def rob_linear(self, arr):
        """Standard House Robber DP solution (without circular constraint)"""
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        prev2, prev1 = 0, arr[0]
        for i in range(1, n):
            curr = max(prev1, prev2 + arr[i])
            prev2, prev1 = prev1, curr
        return prev1

    def maxValue(self, arr):
        """Finds the maximum stolen value considering circular houses"""
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        # Case 1: Consider from index 0 to n-2
        case1 = self.rob_linear(arr[:-1])
        # Case 2: Consider from index 1 to n-1
        case2 = self.rob_linear(arr[1:])

        return max(case1, case2)



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends