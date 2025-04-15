#User function Template for python3
class Solution:
    def bellmanFord(self, V, edges, src):
        INF = 100000000  # Use 100000000 instead of 108

        # Step 1: Initialize distances
        dist = [INF] * V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]

        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        edges = []
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            edges.append([u, v, w])
        S = int(input())
        ob = Solution()

        res = ob.bellmanFord(V, edges, S)
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends