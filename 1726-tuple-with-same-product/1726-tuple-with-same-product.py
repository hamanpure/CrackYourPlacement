class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_cnt = defaultdict(int) # n1 * n2 -> count
        pair_cnt = defaultdict(int) # n1 * n2 -> count of pairs (a, b) and (c, d)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prd = nums[i] * nums[j]
                pair_cnt[prd] += product_cnt[prd]
                product_cnt[prd]+=1


        res = 0
        for i in pair_cnt.values():
            res += 8*i
        
        return res
        