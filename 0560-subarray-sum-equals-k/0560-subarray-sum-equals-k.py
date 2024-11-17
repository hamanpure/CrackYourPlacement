class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0

        prefix_ct =defaultdict(int)
        prefix_ct[0] = 1

        for n in nums:
            prefix_sum += n
            s = prefix_sum-k

            if s in prefix_ct:
                res = prefix_ct[s]
            if prefix_sum not in prefix_ct:
                prefix_ct[prefix_sum] = 1
            prefix_ct[prefix_sum] +=1


        return res
