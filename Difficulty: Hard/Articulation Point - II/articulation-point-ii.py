class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        ap = [False] * V  # articulation point marker
        time = [0]  # mutable time counter for DFS

        def dfs(u):
            children = 0
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if disc[v] == -1:
                    parent[v] = u
                    children += 1
                    dfs(v)

                    low[u] = min(low[u], low[v])

                    # Case 1: u is root and has 2+ children
                    if parent[u] == -1 and children > 1:
                        ap[u] = True

                    # Case 2: u is not root and low[v] >= disc[u]
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        # Run DFS from all components
        for i in range(V):
            if disc[i] == -1:
                dfs(i)

        result = [i for i, is_ap in enumerate(ap) if is_ap]
        return result if result else [-1]


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends