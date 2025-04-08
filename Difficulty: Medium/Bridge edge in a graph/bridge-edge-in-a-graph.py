class Solution:
    def isBridge(self, V, edges, c, d):
        from collections import defaultdict
        
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # since undirected

        # Step 2: Initialize discovery and low time arrays
        disc = [-1] * V
        low = [-1] * V
        time = [0]  # using list to make it mutable in dfs
        found = [False]  # will store if the bridge is found

        def dfs(u, parent):
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # Check if (u, v) is a bridge
                    if low[v] > disc[u]:
                        if (u == c and v == d) or (u == d and v == c):
                            found[0] = True
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        # Step 3: Run DFS from all unvisited nodes
        for i in range(V):
            if disc[i] == -1:
                dfs(i, -1)

        return 1 if found[0] else 0




#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends