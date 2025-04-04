from collections import deque
class Solution:
        
    def cycle(self, start, graph):
        visited = set([start])
        q = deque([start])
        
        while q:
            node = q.popleft()
            
            for nei in graph[node]:
                if nei in visited:
                    return True
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return False
        
	def isCycle(self, V, edges):
		#Code here
		if edges:
		    return self.cycle(0, edges)
		return False


#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


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
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends