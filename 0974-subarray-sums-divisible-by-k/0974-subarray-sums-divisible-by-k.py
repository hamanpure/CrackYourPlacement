class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0

        prefix_ct =defaultdict(int)
        prefix_ct[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k

            if remain in prefix_ct:
                res+=prefix_ct[remain]
            prefix_ct[remain] +=1

        return res
