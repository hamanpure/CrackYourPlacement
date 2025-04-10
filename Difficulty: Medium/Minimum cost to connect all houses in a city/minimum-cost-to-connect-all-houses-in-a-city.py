#User function Template for python3
import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        heap = [(0, 0)]  # (cost, node)
        result = 0

        while heap:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue

            in_mst[u] = True
            result += cost

            for v in range(n):
                if not in_mst[v]:
                    new_cost = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if new_cost < min_dist[v]:
                        min_dist[v] = new_cost
                        heapq.heappush(heap, (new_cost, v))

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends