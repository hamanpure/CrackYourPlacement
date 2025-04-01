#User function Template for python3

class Solution:
    def __init__(self):
        self.res = []
        self.visited = set()
    #Function to return a list containing the DFS traversal of the graph.
    def dd(self, start, graph):
        self.visited.add(start)
        self.res.append(start)
        
        for nei in graph[start]:
            if nei not in self.visited:
                self.dd(nei, graph)
        
    def dfs(self, adj):
        # code here
        self.dd(0, adj)
        return self.res
        
        
        
#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())
        adj = []

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.dfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends