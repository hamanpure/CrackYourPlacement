class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # Parent array for Union-Find

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        self.parent[y] = x  # Mark x as the new parent of y

class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        
        # Step 1: Sort jobs by descending profit
        jobs = sorted(zip(profit, deadline), reverse=True)
        
        # Step 2: Find the maximum deadline
        max_deadline = max(deadline)
        
        # Step 3: Initialize Disjoint Set for efficient slot finding
        ds = DisjointSet(max_deadline)
        
        job_count = 0
        max_profit = 0

        # Step 4: Iterate over sorted jobs
        for p, d in jobs:
            available_slot = ds.find(d)  # Find latest available slot
            if available_slot > 0:  # If slot is available
                ds.union(available_slot - 1, available_slot)  # Mark slot as occupied
                job_count += 1
                max_profit += p

        return [job_count, max_profit]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends