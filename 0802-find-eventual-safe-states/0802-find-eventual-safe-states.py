class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(state, node):
            if state[node] != 0:
                return state[node] == 2

            state[node] = 1
            for n in graph[node]:
                if state[n] == 1 or not dfs(state, n):
                    return False
            
            state[node] = 2
            return True         

        n = len(graph)
        state = [0]*n
        res = []
        for i in range(n):
            if dfs(state, i):
                res.append(i)
        return res