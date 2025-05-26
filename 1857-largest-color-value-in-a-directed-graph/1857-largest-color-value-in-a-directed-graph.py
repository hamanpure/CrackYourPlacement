class Solution:
    @cache
    def dp(self, node, color):
        if node in self.visited:
            return float("inf")
        
        ans = 1 if self.color[node] == color else 0
        if self.graph[node]:
            self.visited.add(node)
            ans += max(self.dp(k, color) for k in self.graph[node])
            self.visited.remove(node)
        return ans
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        self.colorSet = set(colors)
        self.graph = defaultdict(list)
        self.color = colors
        self.visited = set()
        [self.graph[k].append(v) for (k,v) in edges]
        ans = max(self.dp(k, c) for k in range(len(colors)) for c in  self.colorSet)
        #[print(f'{k},{c} :: {self.dp(k,c)}') for k in range(len(colors)) for c in  self.colorSet]
        return -1 if ans == float("inf") else ans
