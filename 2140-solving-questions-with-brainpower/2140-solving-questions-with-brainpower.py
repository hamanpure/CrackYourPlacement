class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        cache = [0] * N
        for i in reversed (range(N)):
            points, brainpower = questions[i]
            next_i = i + 1 + brainpower

            choose = points + (cache[next_i] if next_i < N else 0)
            skip = cache[i + 1] if i + 1 < N else 0

            cache[i] = max(choose, skip)
        return cache[0]

        def backtrack(i):
            if i >= len(questions):
                return 0
            if cache[i]:
                return cache[i]
            points, brainpower = questions[i]

            cache[i] = max(
            backtrack(i + 1), # skip
            points + backtrack(i + 1 + brainpower) # choose
            ) 
            return cache[i]
        return backtrack(0)