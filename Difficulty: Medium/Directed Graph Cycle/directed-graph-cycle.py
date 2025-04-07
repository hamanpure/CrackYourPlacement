class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict

        # Step 1: Create adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Step 2: Initialize visited and recursion stack
        visited = [False] * V
        recStack = [False] * V

        # Step 3: DFS helper function
        def dfs(node):
            visited[node] = True
            recStack[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True

            recStack[node] = False
            return False

        # Step 4: Call DFS for each vertex
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True

        return False

#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends