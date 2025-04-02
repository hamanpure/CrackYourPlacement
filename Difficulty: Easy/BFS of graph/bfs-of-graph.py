#User function Template for python3
from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def __init__(self):
        self.res = []
    def bb(self, start, graph):
        q = deque([start])
        visited = set([start])
        
        while q:
            node = q.popleft()
            self.res.append(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        
        
    def bfs(self, adj):
        # code here
        self.bb(0, adj)
        return self.res


#{ 
 # Driver Code Starts
import sys


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends