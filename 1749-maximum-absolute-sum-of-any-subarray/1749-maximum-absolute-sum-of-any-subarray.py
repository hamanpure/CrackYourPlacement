class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = 0
        max_sum = 0
        res = 0
        cur = 0
        for n in nums:
            cur+=n
            res = max(res, abs(cur - min_sum), abs(cur - max_sum))
            min_sum = min(cur, min_sum)
            max_sum = max(cur, max_sum)
        return res