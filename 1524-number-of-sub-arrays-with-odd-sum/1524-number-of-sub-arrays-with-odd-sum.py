class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        sum_count = 0
        res = 0
        odd_cnt = 0
        even_cnt = 0

        mod = 10**9 + 7

        for i in arr:
            sum_count += i

            if sum_count%2 == 1:
                res = (res + 1 + even_cnt)
                odd_cnt += 1
            else:
                res = (res + odd_cnt)
                even_cnt += 1

        return res%mod
                
