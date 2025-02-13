import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        n = len(nums)
        while nums[0] < k and n>1:
            x,y = heapq.heappop(nums),heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y) )
            count+=1
            n-=1

        return count

